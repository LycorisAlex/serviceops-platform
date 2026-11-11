from fastapi import APIRouter, HTTPException, status

from app.schemas.service import ServiceCreate, ServiceResponse, ServiceUpdate
from app.services import service_service

router = APIRouter(prefix="/services", tags=["Services"])


@router.post(
    "",
    response_model=ServiceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_service(data: ServiceCreate):
    try:
        return service_service.create_service(
            name=data.name,
            url=str(data.url),
        )
    except service_service.ServiceAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Service with this URL already exists",
        )


@router.get("", response_model=list[ServiceResponse], status_code=status.HTTP_200_OK)
def get_services():
    return service_service.get_services()


@router.get("/{id}", response_model=ServiceResponse, status_code=status.HTTP_200_OK)
def get_service(id: int):
    try:
        return service_service.get_service(id)
    except service_service.ServiceNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service with this id not found",
        )


@router.put("/{id}", response_model=ServiceResponse, status_code=status.HTTP_200_OK)
def update_service(id: int, data: ServiceUpdate):
    try:
        return service_service.update_service(id, name=data.name, url=str(data.url))
    except service_service.ServiceNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service with this id not found",
        )
    except service_service.ServiceAlreadyExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Service with this URL already exists",
        )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(id: int):
    try:
        service_service.delete_service(id)
    except service_service.ServiceNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Service with this id not found",
        )
