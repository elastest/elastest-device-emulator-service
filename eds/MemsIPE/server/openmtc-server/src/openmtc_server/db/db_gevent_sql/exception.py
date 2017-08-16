class SQLDBAdapterException(Exception):
    def __init__(self, description):
        self.description = description
        
    def __str__(self):
        return repr(self.description)

class SQLCreatorException(Exception):
    def __init__(self, description):
        self.description = description
        
    def __str__(self):
        return repr(self.description)

    