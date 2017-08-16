from futile.collections import get_iterable
from openmtc_server.methoddomain.filtercriteria.filters import contentType
#ContentInstancesFilterCriteria extends FilterCriteria
#-----------------------------------------------------
from openmtc_scl.methoddomain.filtercriteria.filters import attributeAccessor, \
    createdAfter, createdBefore, ifModifiedSince, ifNoneMatch, \
    ifUnmodifiedSince, searchString


#sizeFrom            Long[0..1       A contentInstance resource matches this
#                            criterion if and only if the contentSize attribute
#                            of the resource is greater than the specified
#                            value.
def sizeFrom(resource, value):
    return resource.contentSize > value


#sizeUntil           Long[0..1]      A contentInstance resource matches this
#                            criterion if and only if the contentSize attribute
#                            of the resource is smaller than the specified
#                            value.
def sizeUntil(resource, value):
    return resource.contentSize < value


# contentType         String[0..unbounded]    A contentInstance resource matches this
#                                    criterion if any of the values in the
#                                    contentTypes attribute of the resource
#                                    matches the specified value The specified
#                                    value may include wildcards. E.g. image/*
#                                    matches all images.
#                                    If a contentInstance resource matches, only
#                                    the matching representations shall be
#                                    returned. If more than one of its alternative
#                                    representation matches then multiple
#                                    representations are returned inside a
#                                    multipart/alternative content-type.
# todo: this is a transformer :)
# def contentType(resource, value):
#     try:
#         return any(map(resource.contentType.__contains__, get_iterable(value)))
#     except AttributeError:
#         pass
contentType = contentType


#metaDataOnly        Boolean[0..1]   Return only meta-data and not the content of
#                            contentInstances.
#                            If not specified this defaults to FALSE, i.e. the
#                            content is returned as well.
def metaDataOnly(resource, value):
    #TODO
    return True
