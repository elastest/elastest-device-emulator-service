from futile.logging import LoggerMixin


class StoreAndForward(LoggerMixin):
    
    def __init__(self, ):
        self.enabled = True
        self.endpoints = set()
        self.mgmtobj_infos = {}
        self.r_params = {} 
        self.ip_ports = {} 
        self.cb = {}
        
    def store_endpoints(self, endpoint_name):
        self.endpoints.add(endpoint_name)
    
    def store_mgmtobjs(self, endpoint_name, mgmt_obj_id_inst_id, payload):
        objects_info = {}
        if self.mgmtobj_infos.has_key(endpoint_name):
            objects_info = self.mgmtobj_infos[endpoint_name]
        objects_info[mgmt_obj_id_inst_id] = payload
        self.mgmtobj_infos[endpoint_name] = objects_info
    
    def store_reg_parameters(self, endpoint_name):
        self.r_params[endpoint_name] = registration_params()
    
    def store_ip_ports(self, endpoint_name):
        self.ip_ports[endpoint_name] = ip_infos()
    

class registration_params(LoggerMixin):
    
    def __init__(self, ):
        self.reg_params = {}
    
    def store_reg_params(self, **kwargs):
        self.reg_params = kwargs
        
        
class ip_infos(LoggerMixin):
    
    def __init__(self, ):
        self.all_ip_ports = {}
    
    def store_ip_info(self, **kwargs):
        self.all_ip_ports =  kwargs
        
    def update_ip_info(self, **kwargs):
        for element1, element2 in kwargs.iteritems():
            self.all_ip_ports[element1] = element2
    
        
        