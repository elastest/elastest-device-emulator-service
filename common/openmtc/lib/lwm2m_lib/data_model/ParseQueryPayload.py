
class ParseQuery(object):
    def __init__(self, ):
        super(ParseQuery, self).__init__()
        
    def parse_query(self, query):
        temp_query = query.split("=")
        
        return temp_query

class ParsePayload(object):
    def __init__(self, ):
        super(ParsePayload, self).__init__()
    
    def parse_payload(self, payload):
        self.payload_list = []
        self.payload = payload
        self.payload = self.payload.replace(' ', '')
        list_of_objects = self.payload.split(",")
        
        for obj_list in list_of_objects:
            split_obj = obj_list.split("/")
            self.payload_list.append({"objectID" : split_obj[0], "objectInstID" : split_obj[1]})
            
        
        return self.payload_list

class ParsePath(object):
    def __init__(self, ):
        super(ParsePath, self).__init__()
        
    def parse_path(self, path, remote):
        temp = []
        temp_dict = {}
        cf = 0 #cf = correction factor
        
        for path_element in path:
            temp.append(path_element.value)
       
        if "attachedDevices" in temp:
            endpoint_name = "/".join(temp[1:4])
        else:
            endpoint_name = temp[1]
            cf = 2
        
        if len(temp) == (4-cf):
            temp_dict = {"rd": temp[0], "endpoint_name" : endpoint_name, "sender_ip" : remote[0], \
                         "sender_port" : remote[1]}
        elif len(temp) == (5-cf):
            temp_dict = {"rd": temp[0], "endpoint_name" : endpoint_name, "object_id" : temp[4-cf], \
                         "sender_ip" : remote[0], "sender_port" : remote[1]}
        elif len(temp) == (6-cf):
            temp_dict = {"rd": temp[0], "endpoint_name" : endpoint_name, "object_id" : temp[4-cf],
                         "object_inst_id" : temp[5-cf], "sender_ip" : remote[0], \
                         "sender_port" : remote[1]}
        elif len(temp) == (7-cf):
            temp_dict = {"rd": temp[0], "endpoint_name" : endpoint_name, "object_id" : temp[4-cf], 
                         "object_inst_id" : temp[5-cf], "res_id" : temp[6-cf], "sender_ip" : remote[0], \
                         "sender_port" : remote[1]}
        elif len(temp) == (8-cf):
            temp_dict = {"rd": temp[0], "endpoint_name" : endpoint_name, "object_id" : temp[4-cf], 
                         "object_inst_id" : temp[5-cf], "res_id" : temp[6-cf], "res_inst_id" : temp[7-cf], \
                         "sender_ip" : remote[0], "sender_port" : remote[1]}
        
        return temp_dict