from futile.logging import LoggerMixin
from ResourcesList import LWM2MResourceAttributes
from mgmt_objects import lwm2m_dict_objects
from lwm2m_lib.operations.ObservationNotification import SpecificObservationInformation

ATTRIBUTE_PMAX = 20  #1 accordng to spec
ATTRIBUTE_PMIN = 5   #1 according to spec

class DeviceMgmtResource(LoggerMixin):
    
    def __init__(self, res_id, res_inst_id, resource_params, local_ip, local_port):
        self.res_id = res_id
        self.res_inst_id = res_inst_id
        self.attributes = LWM2MResourceAttributes(pmax=ATTRIBUTE_PMAX, pmin=ATTRIBUTE_PMIN)
        
        self.res_name = resource_params["resName"]
        self.res_operation = resource_params["operation"]
        self.res_value = resource_params["resValue"]
        self.res_multi_inst = resource_params["multiInst"]
        self.observe_info = SpecificObservationInformation(local_ip, local_port)
    
    #not used now.  
    def resource_update(self, res_value):
        if "W" in self.res_operation:
            self.res_value = res_value
            self.logger.info("Resource Value updated")
        else:
            self.logger.exception("Cannot write the Resource Value. Write Operation is not allowed")
        
        
        
    

