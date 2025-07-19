# Third-Party Libraries
from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.engine import result
from sqlalchemy.orm import Session
from starlette.routing import Router

# Internal Application Imports
from Controllers import crud
from Database_config.config import SessionLocal
from Database_config.models import User
from Schemas.schemas import (
    Request,
    RequestUsers,
    Response,
    TokenPayload,
    UserDelete,
    UsersSchema,
    UsersSchemaCreate,
)
from autenticate.dependencies import Verify_Password, get_current_user
from autenticate.jwt import create_access_token

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def ALL_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100,
):
    try:
        users = crud.Get_all_users(db, skip, limit)
        return Response(
            code="200", status="success", message="list Users", result=users
        )

    except Exception as e:
        print(f"Error al obtener usuarios : {e}")
        raise HTTPException(status_code=500, detail="error interno")


@router.post("/login")
async def Login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = crud.get_user_by_name(db, form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="user not found")
    elif not Verify_Password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="user not found")
    payload = TokenPayload(sub=user.name)
    access_token = create_access_token(payload)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/create")
async def Create_user(request: UsersSchemaCreate, db: Session = Depends(get_db)):
    try:
        user = crud.Create_user(db, request)
        return Response(
            code="200", status="success", message="User create", result=user
        )
    except Exception as error:
        return Response(code="200", status="ERROR", message=str(error), result=None)


@router.put("/delete")
async def Delete_user(
    request: UserDelete,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        if request.id is None or request.id is None:
            raise ValueError("Se requiere un ID válido para eliminar el usuario.")
        Users_id = int(request.id)
        crud.Delete_User(db, Users_id)
        return Response(
            code="200", status="success", message="User deleted", result=None
        )
    except Exception as error:
        return Response(code="500", status="ERROR", message=str(error), result=None)


@router.patch("/update")
async def Update_user(
    request: UsersSchemaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        user = crud.Update_user(db, request)
        return Response(
            code="200", status="success", message="User create", result=user
        )
    except Exception as error:
        return Response(code="500", status="ERROR", message=str(error), result=None)
