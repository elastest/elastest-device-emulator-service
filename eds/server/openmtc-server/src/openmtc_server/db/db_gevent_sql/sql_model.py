'''
Created on 01.04.2014

@author: bro
'''

class Table(object):
    def __init__(self, name, *columns):
        self.name = name
        self.columns = columns
        
    def __repr__(self):
        return 'Table: %s' % (self.name)
        # return 'Table: %s has the following columns: %s' % (self.name, self.columns)


class Column(object):
    def __init__(self, name, type, primary_key=False, foreign_key=None, nullable=True, autoincrement=False, unique=False):
        self.name = name
        self.type = type
        self.primary_key = primary_key
        self.foreign_key = foreign_key
        self.nullable = nullable
        self.autoincrement = autoincrement
        self.unique = unique

    def __repr__(self):
        return 'Column: %s with type: %s' % (self.name, self.type)


class ForeignKey(object):

    def __init__(self, to, onupdate=False, ondelete=False):
        self.to = to
        self.onupdate = onupdate
        self.ondelete = ondelete

    def __repr__(self):
        return 'ForeignKey: %s onupdate: %s ondelete: %s' % (self.to, self.onupdate, self.ondelete)
