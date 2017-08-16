from futile.collections import get_iterable
from openmtc_server.methoddomain.filtercriteria.filters import modifiedSince, unmodifiedSince, createdBefore, \
    createdAfter


# ifModifiedSince     DateTime[0..1]  A resource matches this criterion if and
#                            only if the lastModified attribute of the
#                            resource is chronologically after the
#                            specified value.
#                            It is specifically useful to suppress the
#                            initial notify when used in a create
#                            subscription (see clause 10.25.2).
# def ifModifiedSince(resource, value):
#     try:
#         return resource.lastModifiedTime > value
#     except AttributeError:
#         pass
ifModifiedSince = modifiedSince

#ifUnmodifiedSince   DateTime[0..1]  A resource matches this criterion if and
#                            only if the lastModifiedAttribute of the
#                            resource is chronologically before the
#                            specified value.
# def ifUnmodifiedSince(resource, value):
#     try:
#         return resource.lastModifiedTime < value
#     except AttributeError:
#         pass
ifUnmodifiedSince = unmodifiedSince


#ifNoneMatch         String[0..unbounded]    A resource matches this criterion if the
#                                    etag of the resource does NOT match any
#                                    of the specified values.
#                                    This is specifically useful to suppress the
#                                    initial notify when used in a create
#                                    subscription (see clause 10.25.2).
def ifNoneMatch(resource, value):
    #TODO
    return True


#attributeAccessor   AnyURI          Relative URI indicating the attribute or
#                            element in the resource. This is equivalent
#                            to including the similar attributeAccessor in
#                            a partial addressing retrieve operation, i.e.
#                            only the specified attribute or element
#                            value is represented in the response or
#                            equivalent notify.
# todo: this is a transformer :)
def attributeAccessor(resource, value):
    #for retrieve and subscriptions this is handled outside, through the retrieve method.
    #This filtering only applies to discovery. 
    #We filter out all resources that don't have an attribute specified by *value*

    parts = value.split("/")

    for part in parts:
        try:
            resource = getattr(resource, part)
        except AttributeError:
            try:
                resource = resource[part]
            except KeyError:
                return False

    return True


#searchString        String[0..unbounded]    A resource matches this criterion if the
#                                    resource has a searchStrings attribute and
#                                    one of the searchString values in the
#                                    searchStrings attribute is the same as the
#                                    specified value.
#                                    If multiple searchStrings are specified, the
#                                    logical operation is AND, i.e. only
#                                    resources that contain all the specified
#                                    searchStrings match the criterion.
def searchString(resource, value):
    try:
        return all(map(resource.searchStrings.__contains__,
                       get_iterable(value)))
    except AttributeError:
        pass


#createdAfter        DateTime[0..1]  A resource matches this criterion if and
#                            only if the creationTime attribute of the
#                            resource is chronologically after the
#                            specified value.
# def createdAfter(resource, value):
#     try:
#         return resource.creationTime > value
#     except AttributeError:
#         pass
createdAfter = createdAfter

#createdBefore       DateTime[0..1]  A resource matches this criterion if and
#                            only if the creationTime attribute of the
#                            resource is chronologically before the
#                            specified value.
# def createdBefore(resource, value):
#     try:
#         return resource.creationTime < value
#     except AttributeError:
#         pass
createdBefore = createdBefore