from re import S
from fastapi import HTTPException, Path, APIRouter, requests, responses, status
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy.engine import result
from starlette.routing import Router
from Database_config.config import SessionLocal
from sqlalchemy.orm import Session
from Schemas.schemas import Request, RequestUsers, Response, UsersSchema
from Controllers import crud

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


@router.post("/create")
async def Create_user(request: UsersSchema, db: Session = Depends(get_db)):
    try:
        user = crud.Create_user(db, request)
        return Response(
            code="200", status="success", message="User create", result=user
        )
    except Exception as error:
        return Response(code="200", status="ERROR", message=str(error), result=None)


@router.put("/delete")
async def Delete_user(request: UsersSchema, db: Session = Depends(get_db)):
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
async def Update_user(request: UsersSchema, db: Session = Depends(get_db)):
    try:
        user = crud.Update_user(db, request)
        return Response(
            code="200", status="success", message="User create", result=user
        )
    except Exception as error:
        return Response(code="500", status="ERROR", message=str(error), result=None)
