service_storage = {}
next_id = 1


def get_by_url(url: str):
    for service in service_storage.values():
        if service["url"] == url:
            return service

    return None


def get_by_id(id: int):
    return service_storage.get(id)


def create(name: str, url: str):
    global next_id

    service = {"id": next_id, "name": name, "url": url}

    service_storage[next_id] = service
    next_id += 1

    return service


def get_all():
    return list(service_storage.values())


def update_by_id(id: int, name: str, url: str):

    service = {"id": id, "name": name, "url": url}

    service_storage[id] = service
    return service


def delete_by_id(id: int):
    return service_storage.pop(id)
