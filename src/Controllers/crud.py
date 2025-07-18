from sqlalchemy import text
from sqlalchemy.engine import result
from Database_config.models import User
from sqlalchemy.orm import Session, query
from Schemas.schemas import UsersSchemaCreate, UsersSchema
from autenticate.dependencies import Code_Pass


def Get_all_users(db: Session, skip: int = 0, limit: int = 100):
    query = text("SELECT * FROM Get_all_users(:skip, :limit)")
    result = db.execute(query, {"skip": skip, "limit": limit})
    users = [dict(row._mapping) for row in result]
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


# aqui uso orm ya que me dio flojera
def Get_user_by_name(db: Session, name: str):
    return db.query(UsersSchema).filter(User.name == name).first()


def get_user_by_name(db, name: str):
    query = text("SELECT * FROM users WHERE name = :name")
    result = db.execute(query, {"name": name}).fetchone()
    return result


def Create_user(db: Session, USER: UsersSchemaCreate):
    hashed_password = Code_Pass(USER.password)
    query = text("CALL Insert_users(:name, :correo, :password)")
    db.execute(
        query, {"name": USER.name, "correo": USER.correo, "password": hashed_password}
    )
    db.commit()


def Update_user(db: Session, User: UsersSchemaCreate):
    query = text("SELECT Update_user(:name, :correo, :password)")
    db.execute(
        query, {"name": User.name, "correo": User.correo, "password": User.password}
    )
    db.commit()
    return User
