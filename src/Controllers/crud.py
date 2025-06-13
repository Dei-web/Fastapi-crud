from sqlalchemy import text
from sqlalchemy.engine import result
from Database_config.models import User
from sqlalchemy.orm import Session, query
from Schemas.schemas import UsersSchema


def Get_all_users(db: Session, skip: int = 0, limit: int = 100):
    query = text("SELECT * FROM Get_all_users() OFFSET :skip LIMIT :limit")
    result = db.execute(query, {"skip": skip, "limit": limit})
    users = [dict(row) for row in result]
    return users


def Get_user_by_ID(db: Session, Users_id: int):
    query = text("SELECT Get_user(:Users_id)")
    result = db.execute(query, {"Users_id": Users_id})
    return Users_id


def Delete_User(db: Session, Users_id: int):
    query = text("SELECT Delete_user(:Users_id)")
    db.execute(query, {"Users_id": Users_id})
    db.commit()
    return Users_id


def Create_user(db: Session, USER: UsersSchema):
    query = text("CALL Insert_users(:name, :correo, :password)")
    db.execute(
        query, {"name": USER.name, "correo": USER.correo, "password": USER.password}
    )
    db.commit()
    return USER


def Update_user(db: Session, User: UsersSchema):
    query = text("SELECT Update_user(:name, :correo, :password)")
    db.execute(
        query, {"name": User.name, "correo": User.correo, "password": User.password}
    )
    db.commit()
    return User
