from openmtc_server.util.async import async_all


def create_subresources(resources, dbsession, request_indication):
    subresources = []
    promises = []

    for resource in resources:
        for attr in resource.subresources:
            if not attr.virtual:
                sr = getattr(resource, attr.name)
                subresources.append(sr)
                dbsession.store(request_indication, sr)

    if subresources:
        create_subresources(subresources, dbsession,
                            request_indication)
