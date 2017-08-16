'''
Created on 01.04.2014

@author: bro
'''
import json
from collections import Iterable
from datetime import datetime
from enum import Enum

from openmtc_scl.methoddomain.db.db_gevent_sql.exception import \
    SQLCreatorException

from futile.logging import LoggerMixin
from openmtc.model import Resource, Entity
from openmtc_etsi.model import ContentInstance
from .serializer import b64_pickle


def _json_default(o):
    if isinstance(o, Iterable):
        return tuple(o)
    raise TypeError(repr(o) + " is not JSON serializable")

class SQLCreator(LoggerMixin):
    # some initial values to avoid null pointers
    content_shift = 0
    prettyprint = False
    DEFAULT_COUNT_VALUE = 10000

    def set_prettyprint(self, prettyprint, content_shift=0):
        self.prettyprint = prettyprint
        self.content_shift = content_shift

    def create_sql_string(self, table):
        return self._create_table_sql(table.name, *table.columns)

    def create_drop_table_sql(self, table):
        return 'DROP TABLE IF EXISTS `{}`'.format(table.name)

    def _create_table_sql(self, name, *columns):
        shifted_string = " " * self.content_shift
        table_sql_string = 'CREATE TABLE IF NOT EXISTS `%s`' % name
        table_sql_string += " ("

        if (self.prettyprint):
            table_sql_string += "\n"

        table_sql_string_array = []
        # create the columns string
        self._create_columns_sql(table_sql_string_array, *columns)
        self._create_keys_sql(table_sql_string_array, *columns)
        # concatenate table content by ",", shift and newline
        if (self.prettyprint):
            table_sql_string += shifted_string + (",\n" + shifted_string).join(table_sql_string_array) + "\n"
            table_sql_string += ")" + "\n"
        else:
            table_sql_string += ", ".join(table_sql_string_array)
            table_sql_string += ")"
        return table_sql_string

    def _create_columns_sql(self, table_sql_string_array, *columns):
        for column in columns:
            table_sql_string_array.append(self._create_column_sql(column))

        return table_sql_string_array

    def _create_keys_sql(self, table_sql_string_array, *columns):
        # allow more than one primary keys
        primary_keys_list = []
        foreign_keys_list = []
        for column in columns:
            if (column.primary_key):
                primary_keys_list.append(column.name)
            if (column.foreign_key):
                foreign_keys_list.append(self._create_foreign_key_sql(column))
        if primary_keys_list:
            table_sql_string_array.append("PRIMARY KEY (%s)" % ",".join(primary_keys_list))
        table_sql_string_array.extend(foreign_keys_list)
        return table_sql_string_array

    def _create_column_sql(self, column):
        # create base column
        column_sql_string = "%s %s" % (column.name, column.type)
        # add NOT NULL SUFFIX
        if not (column.nullable):
            column_sql_string += " NOT NULL"
        if column.autoincrement:
            column_sql_string += " PRIMARY KEY AUTO_INCREMENT"
        if column.unique:
            column_sql_string += " UNIQUE"
        return column_sql_string

    def _create_foreign_key_sql(self, column):
        foreign_key_string = "FOREIGN KEY(%s) REFERENCES %s" % (column.name, column.foreign_key.to)
        if (column.foreign_key.onupdate):
            foreign_key_string += " ON UPDATE " + column.foreign_key.onupdate
        if (column.foreign_key.ondelete):
            foreign_key_string += " ON DELETE " + column.foreign_key.ondelete
        return foreign_key_string

    def create_insert_sql(self, table, path=None, etsi_path=None, onem2m_path=None, parent_path=None, etsi_parent_path=None, onem2m_parent_path=None, values=None):
        insert_column = {}

        # iterate all sql table columns and grab the values from the model
        for column in table.columns:
            # get the mapped column name if there is one
            column_name = column.name
            mapped_column_name = self._get_mapped_colum_name(column_name)
            # append the value of the column and format to a sql type if necessary
            if (column_name == "path"):
                column_value = path
            elif (column_name == "parent_path"):
                if (parent_path):
                    column_value = parent_path
                else:
                    continue
            elif (column_name == "etsi_path"):
                column_value = etsi_path
            elif (column_name == "onem2m_path"):
                column_value = onem2m_path
            elif (column_name == "etsi_parent_path"):
                if (etsi_parent_path):
                    column_value = etsi_parent_path
                else:
                    continue
            elif (column_name == "onem2m_parent_path"):
                if (onem2m_parent_path):
                    column_value = onem2m_parent_path
                else:
                    continue
            else:
                # this is more probable
                if (not mapped_column_name):
                    column_value = self._get_column_value(column_name, values)
                else:
                    column_value = self._get_column_value(mapped_column_name, values)
            # format the value as we have strings 'value' or datetimes ''value or normal numbers

            if column_value is not None:
                column_value = self._format_column_value(column_value, column.type)
                insert_column[column_name] = column_value
            elif not column.nullable:
                raise SQLCreatorException("Not Null Error - The Column %s must contain a value in the OpenMTC Model. If not change the DB Schema!" % column_name)
        insert_sql = 'INSERT INTO `%s` (%s) VALUES (%s)' % (table.name, ",".join(insert_column.keys()), ",".join(insert_column.values()))
        return insert_sql

    def create_select_sql(self, table, path=None, parent_path=None, limited=None):
        # select, use LIMIT as it immediately returns the db values after finding 1 and increasing speed
        limiter = " LIMIT 1" if limited else ""

        if (path and not parent_path):
            return "SELECT * FROM \"%s\" WHERE PATH='%s'%s" % (table.name, path, limiter)
        elif (not path and parent_path):
            return "SELECT * FROM \"%s\" WHERE PARENT_PATH='%s'%s" % (table.name, parent_path, limiter)
        elif (path and parent_path):
            return "SELECT * FROM \"%s\" WHERE PATH='%s' AND PARENT_PATH='%s'%s" % (table.name, path, parent_path, limiter)
        else:
            return "SELECT * FROM \"%s\"%s" % (table.name, limiter)

    def _handle_filter(self, filter_criteria, filter_name, column_name, operator, discriminators):
        try:
            value = filter_criteria.pop(filter_name)
        except KeyError:
            return

        if isinstance(value, datetime):
            value = self._format_datetime(value)

        discriminators.append("%s%s%s" % (column_name, operator, value))

    def create_select_fields_sql(self, table, fields, path=None, etsi_path=None, onem2m_path=None,
                                 parent_path=None, etsi_parent_path=None, onem2m_parent_path=None, limited=None,
                                 order_by=None, filter_criteria=None):
        # select, use LIMIT as it immediately returns the db values after finding 1 and increasing speed
        # created to map the table names to the fields
        mapped_fields = []
        # map only columns the table really has
        for column in table.columns:
            column_name = column.name
            unmapped_column_name = self._get_mapped_colum_name(column_name)
            # the column was mapped - check if the mapped name is in fields
            if (unmapped_column_name):
                if (unmapped_column_name in fields):
                    mapped_fields.append(column_name)
            # the column was not mapped - check if the original name is in fields
            else:
                if (column_name in fields):
                    mapped_fields.append(column_name)
        # create them as tuple
        # selector = ",".join(fields)
        selector = ",".join(mapped_fields)

        discriminators = []

        if path:
            discriminators.append("PATH='%s'" % (path, ))
        if parent_path:
            discriminators.append("PARENT_PATH='%s'" % (parent_path, ))
        if etsi_path:
            discriminators.append("ETSI_PATH='%s'" % (etsi_path, ))
        if etsi_parent_path:
            discriminators.append("ETSI_PARENT_PATH='%s'" % (etsi_parent_path, ))
        if onem2m_path:
            discriminators.append("ONEM2M_PATH='%s'" % (onem2m_path, ))
        if onem2m_parent_path:
            discriminators.append("ONEM2M_PARENT_PATH='%s'" % (onem2m_parent_path, ))

        if filter_criteria:
            self._handle_filter(filter_criteria, "createdBefore",
                                "creationTime", "<", discriminators)
            self._handle_filter(filter_criteria, "ifUnmodifiedSince", "lastModifiedTime", "<", discriminators)
            self._handle_filter(filter_criteria, "createdAfter", "creationTime", ">", discriminators)
            self._handle_filter(filter_criteria, "ifModifiedSince", "lastModifiedTime", ">", discriminators)
            self._handle_filter(filter_criteria, "sizeFrom", "contentSize", ">", discriminators)
            self._handle_filter(filter_criteria, "sizeUntil", "contentSize", "<", discriminators)

        sql = "SELECT %s FROM `%s` WHERE %s" % (selector, table.name, " AND ".join(discriminators))

        if order_by:
            sql = "%s ORDER BY %s ASC" % (sql, order_by)

        if limited:
            sql += " LIMIT 1"

        return sql

    # sufficient to check the existence on the resource level as it is foreign key of all subresource types,
    # the EXISTS SQL is not possible in hsql
    def create_exist_sql(self, path):
        return "SELECT COUNT(path) AS C FROM resource WHERE PATH='%s' LIMIT 1" % path

    def create_exist_fields_sql(self, table, fields):
        try:
            fields = fields.items()
        except AttributeError:
            pass

        where_clause = ' AND '.join(["{}='{}'".format(k, v)
                                     for k, v in fields])

        sql = "SELECT COUNT(path) AS C FROM `{}` WHERE {} LIMIT 1"
        return sql.format(table.name, where_clause)

    def create_generic_exist_sql(self, table, column_value_dict):
        return self.create_count_sql(table, column_value_dict, limit=1)

    def create_count_sql(self, table, column_value_dict=None, limit=DEFAULT_COUNT_VALUE):
        # column value is a dict
        limit = " LIMIT %s" % (str(limit))
        if (column_value_dict):
            where_list = []
            for k,v in column_value_dict.items():
                # check if the key is really in the table column names
                for column in table.columns:
                    if k == column.name:
                        where_list.append("%s='%s'" % (k,v))
            return "SELECT COUNT(*) AS C FROM %s WHERE %s%s" % (table.name, " AND ".join(where_list), limit)
        else:
            return "SELECT COUNT(*) AS C FROM %s%s" % (table.name, limit)

    def create_update_sql(self, table, values, path=None, etsi_path=None, onem2m_path=None):
        set_sqls = []
        for column in table.columns:
            column_name = column.name
            mapped_column_name = self._get_mapped_colum_name(column_name)

            # append the value of the column and format to a sql type if necessary - skip path columns
            if (column_name == "path" or column_name == "parent_path"):
                continue

            if (column_name == "etsi_path" or column_name == "onem2m_path" or column_name == "etsi_parent_path" or column_name == "onem2m_parent_path"):
                continue

            # this is more probable
            if (not mapped_column_name):
                if (column_name in values):
                    column_value = self._get_column_value(column_name, values)
                else:
                    continue
            else:
                if (mapped_column_name in values):
                    column_value = self._get_column_value(mapped_column_name, values)
                else:
                    continue

            if column_value is not None:
                column_value = self._format_column_value(column_value, column.type)
                set_sqls.append("%s=%s" % (column_name, column_value))
            else:
                if column.nullable:
                    set_sqls.append("%s=NULL" % (column_name, ))
                else:
                    raise SQLCreatorException("Not Null Error - The Column %s must contain a value in the OpenMTC Model. If not change the DB Schema!" % column_name)
        if (path):
            return "UPDATE `%s` SET %s WHERE path='%s'" % (table.name, ",".join(set_sqls), path)
        elif (etsi_path and onem2m_path):
            return "UPDATE `%s` SET %s WHERE etsi_path='%s' AND onem2m_path='%s'" % (table.name, ",".join(set_sqls), etsi_path, onem2m_path)

    def create_delete_sql(self, table, path=None, etsi_path=None, onem2m_path=None):
        if (path):
            return "DELETE FROM `%s` WHERE path='%s'" % (table.name, path)
        if (etsi_path and onem2m_path):
            return "DELETE FROM `%s` WHERE etsi_path='%s' AND onem2m_path='%s'" % (table.name, etsi_path, onem2m_path)

    def create_delete_children_sql(self, table, parent_path):
        return "DELETE FROM `%s` WHERE parent_path='%s'" % (table.name, parent_path)

    def _get_column_value(self, column_name, values):
        try:
            return values[column_name]
        except KeyError:
            self.logger.error("Column Key: %s Not Found in the Values: %s you are trying to store. Check the Data!" % (column_name, values))

    def _format_datetime(self, value):
        time_pattern = "%Y-%m-%d %H:%M:%S"
        formatted_column_value = value.strftime(time_pattern)
        return "'%s'" % (formatted_column_value, )

    # TODO The best would be to use a common data type mapping between the sql creator and adapter to not use string comparison
    def _format_column_value(self, column_value, column_type):
        try:
            if isinstance(column_value, Resource):
                if not column_type.startswith("VARCHAR"):
                    raise TypeError("Cannot map resource object to column type %s" % (column_type, ))
                formatted_column_value = "'" + column_value.path + "'"
            elif (column_type.startswith("VARCHAR")):
                # for example for the searchStrings
                if (isinstance(column_value, (dict, list, tuple, set, frozenset))):
                    # try to use the json serializer, if object too complex, use pickle
                    formatted_column_value = self._serialize(column_value)
                elif (isinstance(column_value, Enum)):
                    # storing it as string means recreating it from a string. This is done with name and get_attr() to get the right type
                    formatted_column_value = "'" + column_value.name + "'"
                    # sometimes i watched are constructs like FilterCriteria objects to serialize..this is for the generic entity case
                elif (isinstance(column_value, Entity)):
                    formatted_column_value = self._serialize(column_value)
                else:
                    formatted_column_value = "'" + column_value + "'"
            elif (column_type == "DATETIME"):
                # do some datetime formatting - if datetime is a python datetime object -> format to iso

                # without the timezone (generating problems with mysql)
                formatted_column_value = self._format_datetime(column_value)

                # with timezone
                # formatted_column_value = "'" + column_value.isoformat(' ') + "'"
            elif (column_type == "INTEGER"):
                formatted_column_value = str(column_value)
            elif column_type == "BOOLEAN":
                formatted_column_value = column_value and "1" or "0"
            else:
                # per default not formatted
                formatted_column_value = column_value

            # this is a special fix, because the latest and oldest contentInstance are stored in the nodb adapter
            # directly to the contentInstances. UnifiedContentInstance is not used or mapped for this, but should be in the controllers!
            if (isinstance(column_value, ContentInstance)):
                formatted_column_value = self._serialize(column_value)

            return formatted_column_value
        except:
            self.logger.exception("Can not format the value %s", column_value)
            raise

    def _serialize(self, value):
        try:
            return "'" + json.dumps(value, default=_json_default) + "'"
        except:
            return "'" + b64_pickle(value) + "'"

    # returns the columns mapped name or None if there is none
    def _get_mapped_colum_name(self, column_name):
        try:
            return self.mapped_column_names[column_name]
        except:
            return None

    def _get_column_name(self, column_name):
        mapped_column_name = self._get_mapped_colum_name(column_name)
        if (mapped_column_name):
            return mapped_column_name
        else:
            return column_name


class SQLiteSQLCreator(SQLCreator):
    def _create_column_sql(self, column):
        # create base column
        column_sql_string = "%s %s" % (column.name, column.type)
        # add NOT NULL SUFFIX
        if not (column.nullable):
            column_sql_string += " NOT NULL"
        if column.autoincrement:
            column_sql_string += " PRIMARY KEY AUTOINCREMENT"
        if column.unique:
            column_sql_string += " UNIQUE"
        return column_sql_string
