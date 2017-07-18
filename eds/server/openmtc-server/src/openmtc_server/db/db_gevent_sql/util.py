

# some constants used for table naming
TABLE_PREFIX = "tbl_"
UNIFIED_PREFIX = "unified_"
ETSI_PREFIX = "etsi_"
ONEM2M_PREFIX = "onem2m_"

SHELVE_PREFIX = "shelve_"
SHELVE_KEYNAME = "shelve_key"

def create_table_name(table_name, type="default"):
    if (type == "unified"):
        return TABLE_PREFIX + UNIFIED_PREFIX + table_name
    elif (type == "etsi"):
        return TABLE_PREFIX + ETSI_PREFIX + table_name
    elif (type == "onem2m"):
        return TABLE_PREFIX + ONEM2M_PREFIX + table_name
    elif (type == "shelve"):
        return TABLE_PREFIX + SHELVE_PREFIX + table_name
    elif (type == "default"):
        return TABLE_PREFIX + table_name