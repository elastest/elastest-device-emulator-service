from futile.logging import LoggerMixin
from CommonParameters import CommonParameters

class GenericOperation(LoggerMixin):
    
    def __init__(self, ):
        super(GenericOperation, self).__init__()
        self.common_params = CommonParameters()
        