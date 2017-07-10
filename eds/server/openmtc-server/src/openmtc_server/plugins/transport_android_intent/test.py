from openmtc_scl.serializer import JsonSerializer
from IntentHandling import IntentHandler
from openmtc.response import RetrieveResponseConfirmation, CreateResponseConfirmation, DeleteResponseConfirmation, ErrorResponseConfirmation

def test_read_params(request_handler, logger, config):
    payload = {"method":"retrieve",
               "path":"/m2m",
               "replyAction":"intent://test_action",
               "requestId":"123"
               }
    intentHandler = IntentHandler(logger, config)
    request = intentHandler.parseRequest("test_issuer",payload, None)
    result = intentHandler.handleParsedRequest(request, request_handler, None)
#    result = json.loads(result.decode("utf-8"))
    logger.info("result is "+str(result))
    #f result is not None:
#    if  isinstance(result[1], IntentError):
 #          logger.info("error while sending request")
#       #result.sendIntent(context, self.action, self.issuer)
#    elif isinstance(result[1], Response):
 #          logger.info("hurray"+str(result["response"]))

        
def test_create_app(request_handler, logger, config, app_name):
    payload = {"method":"create",
               "content_type":"application/json", 
               "path":"/m2m/applications",
               "content":"{\"application\":{\"appId\":\""+app_name+"\"}}",
               "replyAction":"intent://test_action",
               "requestId":"123"
               }
#    reference = "someRef"
#    subscriptionId = "someSubscrId"
    intentHandler = IntentHandler(logger, config)
    request = intentHandler.parseRequest("test_issuer",payload, None)
    result = intentHandler.handleParsedRequest(request, request_handler, None)
    logger.info("result is "+str(result))
   
def test_create_app_with_search_str(request_handler, logger, config, app_name, search_string):

    if search_string is None:
	test_create_app(request_handler, logger, config, app_name)
    else:
	    payload = {"method":"create",
        	       "content_type":"application/json",
	               "path":"/m2m/applications",
        	       "content":"{\"application\":{\"appId\":\""+app_name+"\", \"searchStrings\":{\"searchString\":[\""+search_string+"\"]}}}",
	               "replyAction":"intent://test_action",
        	       "requestId":"123"
	               }
#    reference = "someRef"
#    subscriptionId = "someSubscrId"
	    intentHandler = IntentHandler(logger, config)
	    request = intentHandler.parseRequest("test_issuer",payload, None)
	    result = intentHandler.handleParsedRequest(request, request_handler, None)
	    logger.info("result is "+str(result))
   
def test_create_app_property(request_handler, logger, config, app_name, prop_name):
    payload = {"method":"create",
               "content_type":"application/json",
               "path":"/m2m/applications/"+app_name+"/containers",
               "content":"{\"container\":{\"id\":\""+prop_name+"\"}}",
               "replyAction":"intent://test_action",
               "requestId":"123"
               }
#    reference = "someRef"
#    subscriptionId = "someSubscrId"
    intentHandler = IntentHandler(logger, config)
    request = intentHandler.parseRequest("test_issuer",payload, None)
    result = intentHandler.handleParsedRequest(request, request_handler, None)
    logger.info("result is "+str(result))
    
def test_get_latest_data_of_property(request_handler, logger, config, app_name, prop_name):
    payload = {"method":"retrieve",
               "content_type":"application/json",
               "path":"/m2m/applications/"+app_name+"/containers/"+prop_name+"/contentInstances/latest",
               "replyAction":"intent://test_action",
               "requestId":"123"
               }
#    reference = "someRef"
#    subscriptionId = "someSubscrId"
    intentHandler = IntentHandler(logger, config)
    request = intentHandler.parseRequest("test_issuer",payload, None)
    result = intentHandler.handleParsedRequest(request, request_handler, None)
    logger.info("result is "+str(result))

    response = result["response"]
    if isinstance(response, RetrieveResponseConfirmation):
	if response.resource is not None:
	    serializer = JsonSerializer()
	    content = serializer.encode(response.resource)
       	    logger.info("response content is "+content)
    
def test_get_all_properties(request_handler, logger, config, app_name):
    payload = {"method":"retrieve",
               "content_type":"application/json",
               "path":"/m2m/applications/"+app_name+"/containers",
               "replyAction":"intent://test_action",
               "requestId":"123"
               }
#    reference = "someRef"
#    subscriptionId = "someSubscrId"
    intentHandler = IntentHandler(logger, config)
    request = intentHandler.parseRequest("test_issuer",payload, None)
    result = intentHandler.handleParsedRequest(request, request_handler, None)
    logger.info("result is "+str(result))

    response = result["response"]
    if isinstance(response, RetrieveResponseConfirmation):
        if response.resource is not None:
            serializer = JsonSerializer()
            content = serializer.encode(response.resource)
            logger.info("response content is "+content)


def test_subscribe_apps_with_search_str(request_handler, logger, config, search_string, contact):

    content = "{\"subscription\":{\"contact\":\""+contact+"\""
    if search_string is not None:
        content = content+", \"filterCriteria\":{\"searchStrings\":{\"searchString\":[\""+search_string+"\"] }}"

    content = content+ "}}"
    logger.info("content is "+content)
    payload = {"method":"create",
       	       "path":"/m2m/applications/subscriptions",
               "replyAction":contact,
       	       "requestId":"123",
               "content_type":"application/json",
       	       "content":content
            }
    intentHandler = IntentHandler(logger, config)
    request = intentHandler.parseRequest("test_issuer",payload, None)
    result = intentHandler.handleParsedRequest(request, request_handler, None)
    logger.info("result is "+str(result))
    
'''
def update_subscription
def test_unsubscribe_apps_with_search_str(request_handler, logger, config, search_string, contact):
'''
    
def test_discover_apps_with_search_str(request_handler, logger, config, search_string, contact):
    payload = {"method":"retrieve",
               "path":"/m2m/discovery?searchStrings=\""+search_string+"\"",
               "replyAction":contact,
               "requestId":"123"
               }
#    reference = "someRef"
#    subscriptionId = "someSubscrId"
    intentHandler = IntentHandler(logger, config)
    request = intentHandler.parseRequest("test_issuer",payload, None)
    result = intentHandler.handleParsedRequest(request, request_handler, None)
    logger.info("result is "+str(result))

def test_get_app(request_handler, logger, config, app_name, contact):
    payload = {"method":"retrieve",
               "path":"/m2m/applications/"+app_name,
               "replyAction":contact,
               "requestId":"123"
               }
#    reference = "someRef"
#    subscriptionId = "someSubscrId"
    intentHandler = IntentHandler(logger, config)
    request = intentHandler.parseRequest("test_issuer",payload, None)
    result = intentHandler.handleParsedRequest(request, request_handler, None)
    logger.info("result is "+str(result))

def test_subscribe_pushed_data(request_handler, logger, config, app_name, property_name, contact):
    payload = {"method":"create",
               "content_type":"application/json",
               "path":"/m2m/applications/"+app_name+"/containers/"+property_name+"/contentInstances/subscriptions",
               "content":"{\"subscription\":{\"contact\":\""+contact+"\"}}",
               "replyAction":"intent://test_action",
               "requestId":"123"
               }
#    reference = "someRef"
#    subscriptionId = "someSubscrId"
    intentHandler = IntentHandler(logger, config)
    request = intentHandler.parseRequest("test_issuer",payload, None)
    result = intentHandler.handleParsedRequest(request, request_handler, None)
    logger.info("result is "+str(result))

def test_push_data(request_handler, logger, config, app_name, property_name):
    payload = {"method":"create",
               "content_type":"application/json",
               "path":"/m2m/applications/"+app_name+"/containers/"+property_name+"/contentInstances",
               "content":"{\"value\":75}",
               "replyAction":"intent://test_action",
               "requestId":"123"
               }
#    reference = "someRef"
#    subscriptionId = "someSubscrId"
    intentHandler = IntentHandler(logger, config)
    request = intentHandler.parseRequest("test_issuer",payload, None)
    result = intentHandler.handleParsedRequest(request, request_handler, None)
    logger.info("result is "+str(result))


def test_destroy_app(request_handler, logger, config, app_name):
    payload = {"method":"delete",
               "content_type":"application/json",
               "path":"/m2m/applications/"+app_name,
               "replyAction":"intent://test_action",
               "requestId":"123"
               }
#    reference = "someRef"
#    subscriptionId = "someSubscrId"
    intentHandler = IntentHandler(logger, config)
    request = intentHandler.parseRequest("test_issuer",payload, None)
    result = intentHandler.handleParsedRequest(request, request_handler, None)
    logger.info("result is "+str(result))

