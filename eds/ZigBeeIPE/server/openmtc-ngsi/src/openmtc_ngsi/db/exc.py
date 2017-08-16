class DBError(Exception):
    pass


class DBEntityNotFound(DBError):
    pass
