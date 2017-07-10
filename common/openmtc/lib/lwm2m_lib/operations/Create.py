from json import dumps

from OperationRequest import OperationRequest
from lwm2m_lib.api import lwm2m_api


class Create(OperationRequest):
    def __init__(self, lwm2m_resources):
        self.lwm2m_resources = lwm2m_resources

    def create_instance(self, path, remote, content_type, resources_collection):
        endpoint_name, object_id, object_inst_id, res_id, res_inst_id, \
                            _, _ = self.find_elements(path, remote)
        response = self.lwm2m_resources.create_object_object_inst(endpoint_name, object_id, object_inst_id=object_inst_id)

        if isinstance(response, int):
            object_inst_id = response
            endpoint = self.lwm2m_resources.return_endpoint_object(endpoint_name=endpoint_name)
            for _, resources in resources_collection.iteritems():
                res_id = resources["res_id"]
                res_inst_id = resources["res_inst_id"]
                res_value = resources["res_value"]
                if endpoint is not None:
                    self.lwm2m_resources.add_object_instance_resource_instance(endpoint, object_id, \
                                            res_id, res_value, object_inst_id=object_inst_id, res_inst_id=res_inst_id)

    def forward_request(self, path, remote, payload, content_type, client_port):
        endpoint_name, object_id, object_inst_id, res_id, res_inst_id, \
                            _, _ = self.find_elements(path, remote)
        endpoint = self.lwm2m_resources.return_endpoint_object(endpoint_name=endpoint_name)

        listener_ip = endpoint.listener_ip
        listener_port = endpoint.listener_port

        payload = dumps(payload)

        request = lwm2m_api()
        response = request.create_object_instance(listener_ip, listener_port, endpoint_name, object_id, \
                            payload, content_type, object_inst_id=object_inst_id, client_port=client_port)
