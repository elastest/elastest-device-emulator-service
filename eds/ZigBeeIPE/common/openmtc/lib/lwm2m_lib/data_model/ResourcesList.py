from futile.logging import LoggerMixin

class Parameters(object):
    endpoint_name = ""
    location = ""
    objectID = ""
    objectInstID = ""
    common_params = None
    
    def __init__(self, ):
        super(Parameters, self).__init__()
            
class LWM2MResourceAttributes(object):
    attributes_dict = {
            "pmax" :    {"attribute_name" : "MaximumPeriod", "attribute_value" : ""},
            "pmin" :    {"attribute_name" : "MinimumPeriod", "attribute_value" : ""},
            "gt" :      {"attribute_name" : "GreaterThan", "attribute_value" : ""},
            "lt" :      {"attribute_name" : "LessThan", "attribute_value" : ""},
            "st" :      {"attribute_name" : "Step", "attribute_value" : ""},
            "cancel" :  {"attribute_name" : "Cancel", "attribute_value" : ""}
    }
    
    def __init__(self, pmax=None, pmin=None, gt=None, lt=None, st=None, cancel=None):
        """ From LWM2M Specification :
            pmax = Maximum Period, pmin = Minimum Period, gt = Greater Than,
            lt = Less Than, st = Step, cancel = Cancel
        """
        self.pmax = pmax
        self.pmin = pmin
        self.gt = gt
        self.lt = lt
        self.st = st
        self.cancel = cancel
        
class CommonLists(object):
    observation_list = []
    timer_list = []
    def __init__(self, ):
        super(CommonLists, self).__init__()
        
