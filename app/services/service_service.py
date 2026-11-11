from app.repositories import service_repository


class ServiceAlreadyExistsError(Exception):
    pass


class ServiceNotFoundError(Exception):
    pass


def create_service(name: str, url: str):
    existing_service = service_repository.get_by_url(url)

    if existing_service is not None:
        raise ServiceAlreadyExistsError("Service with this URL already exists")

    return service_repository.create(name, url)


def get_services():
    return service_repository.get_all()


def get_service(id: int):
    existing_service = service_repository.get_by_id(id)

    if existing_service is None:
        raise ServiceNotFoundError("Service with this id not found")

    return existing_service


def update_service(id: int, name: str, url: str):
    existing_service = service_repository.get_by_id(id)
    url_owner = service_repository.get_by_url(url)

    if existing_service is None:
        raise ServiceNotFoundError("Service with this id not found")

    if (url_owner is not None) and (url_owner["id"] != id):
        raise ServiceAlreadyExistsError("Service with this URL already exists")

    return service_repository.update_by_id(id, name, url)


def delete_service(id: int):
    existing_service = service_repository.get_by_id(id)

    if existing_service is None:
        raise ServiceNotFoundError("Service with this id not found")

    return service_repository.delete_by_id(id)
