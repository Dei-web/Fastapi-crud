import bcrypt
from jose import jwt
from jose.exceptions import JWTError
from typing import Optional
import os
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from Database_config.config import SessionLocal

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


ENCODING = "utf-8"


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def Code_Pass(passs: str):
    Salt = bcrypt.gensalt()
    Hashed = bcrypt.hashpw(passs.encode(ENCODING), Salt)
    return Hashed.decode(ENCODING)


def Verify_Password(Pass_Insert: str, Hashed_Password: str) -> bool:
    return bcrypt.checkpw(
        Pass_Insert.encode(ENCODING), Hashed_Password.encode(ENCODING)
    )


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    from Controllers.crud import get_user_by_name

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        if not SECRET_KEY:
            raise ValueError("SECRET_KEY no está definida. Verifica tu archivo .env")

        payload = jwt.decode(token, str(SECRET_KEY), algorithms=[ALGORITHM])
        username: Optional[str] = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user_by_name(db, username)
    if user is None:
        raise credentials_exception

    return user
