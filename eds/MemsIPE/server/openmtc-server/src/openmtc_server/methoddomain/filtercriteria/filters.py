from futile.collections import get_iterable


# ifModifiedSince     DateTime[0..1]  A resource matches this criterion if and
#                            only if the lastModified attribute of the
#                            resource is chronologically after the
#                            specified value.
#                            It is specifically useful to suppress the
#                            initial notify when used in a create
#                            subscription (see clause 10.25.2).
def modifiedSince(resource, value):
    try:
        return resource.lastModifiedTime > value
    except AttributeError:
        pass


#ifUnmodifiedSince   DateTime[0..1]  A resource matches this criterion if and
#                            only if the lastModifiedAttribute of the
#                            resource is chronologically before the
#                            specified value.
def unmodifiedSince(resource, value):
    try:
        return resource.lastModifiedTime < value
    except AttributeError:
        pass


# createdAfter        DateTime[0..1]  A resource matches this criterion if and
#                            only if the creationTime attribute of the
#                            resource is chronologically after the
#                            specified value.
def createdAfter(resource, value):
    try:
        return resource.creationTime > value
    except AttributeError:
        pass


#createdBefore       DateTime[0..1]  A resource matches this criterion if and
#                            only if the creationTime attribute of the
#                            resource is chronologically before the
#                            specified value.
def createdBefore(resource, value):
    try:
        return resource.creationTime < value
    except AttributeError:
        pass


# contentInstance stuff


# contentType         String[0..unbounded]    A contentInstance resource matches this
# criterion if any of the values in the
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
def contentType(resource, value):
    try:
        return any(map(resource.contentType.__contains__, get_iterable(value)))
    except AttributeError:
        pass

