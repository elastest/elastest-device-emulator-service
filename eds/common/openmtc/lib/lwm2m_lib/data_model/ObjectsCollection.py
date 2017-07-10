from ResourcesCollection import DeviceMgmtResource
from ResourcesList import Parameters, LWM2MResourceAttributes
from futile.logging import LoggerMixin
from mgmt_objects import lwm2m_dict_objects
from lwm2m_lib.operations.ObservationNotification import SpecificObservationInformation

ATTRIBUTE_PMAX = 20  #1 accordng to spec
ATTRIBUTE_PMIN = 5   #1 according to spec

class DeviceMgmtObject(object):
    def __init__(self, object_id_object_inst_id, local_ip, local_port):
        self.object_id_object_inst_id = object_id_object_inst_id
        self.attributes = LWM2MResourceAttributes(pmax=ATTRIBUTE_PMAX, pmin=ATTRIBUTE_PMIN)
        self.observe_info = SpecificObservationInformation(local_ip, local_port)
        self.resources_id_dict = {}

class ObjectsCollection(LoggerMixin):     

    def __init__(self, ):
        super(ObjectsCollection, self).__init__()

    def process_object(self, object_, object_id, local_ip, local_port):
        object_resources = lwm2m_dict_objects[str(object_id)]["resource_list"]
        for res_id, resource_details in object_resources.iteritems():
            #res_inst_id  check for creating more res inst
            if not resource_details["multiInst"]:
                res_inst_id = 0
            else:
                res_inst_id = 0
                pass #do something here while creating resources..
            res_id_res_inst_id = res_id + "_" + str(res_inst_id)
            resource_object = DeviceMgmtResource(res_id, res_inst_id, resource_details, local_ip, local_port)
            object_.resources_id_dict.update({
                res_id_res_inst_id : {"object" : resource_object}
            })
    
        