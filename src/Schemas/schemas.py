from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar("T")


class UsersSchema(BaseModel):
    id: int
    name: Optional[str] = None
    correo: Optional[str] = None
    password: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestUsers(BaseModel):
    parameter: UsersSchema = Field(...)
