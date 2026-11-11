from typing import Annotated

from pydantic import BaseModel, HttpUrl, StringConstraints


class ServiceCreate(BaseModel):
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    url: HttpUrl


class ServiceUpdate(BaseModel):
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    url: HttpUrl


class ServiceResponse(BaseModel):
    id: int
    name: str
    url: HttpUrl
