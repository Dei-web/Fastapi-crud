from dataclasses import field
from fastapi.openapi.models import Example
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Generic, TypeVar


T = TypeVar("T")


class UsersSchema(BaseModel):
    id: int
    name: Optional[str] = None
    correo: Optional[str] = None
    password: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class UsersSchemaCreate(BaseModel):
    name: str
    correo: str
    password: str


class TokenPayload(BaseModel):
    sub: str
    # role: str


# queria hacer implementaciones de schemas por defecto pero perdia
# el modo de hacerlo como se deberia hacer incurria en malas practicas
# class UsersSchemaLogin(BaseModel):
#     name: Optional[str] = None
#     password: Optional[str] = None
#
#     model_config = ConfigDict(
#         {
#             "json_schema_extra": {
#                 "examples": [
#                     {"name": "Enter your Name", "password": "enter your password"}
#                 ]
#             }
#         }
#     )
#


class UserDelete(BaseModel):
    id: int


class Response(BaseModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class Request(BaseModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestUsers(BaseModel):
    parameter: UsersSchema = Field(...)
