from jose import jwt
from jose.exceptions import JWTClaimsError, ExpiredSignatureError, JWTError
from datetime import timedelta, timezone, datetime
from typing import Optional
from Schemas.schemas import TokenPayload
import os
from dotenv import load_dotenv
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


def create_access_token(
    payload: TokenPayload, expires_delta: Optional[timedelta] = None
) -> str:
    to_encode = payload.model_dump()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": int(expire.timestamp())})
    return jwt.encode(to_encode, str(SECRET_KEY), algorithm=ALGORITHM)


def Decode_token(Token: str):
    try:
        if not SECRET_KEY:
            raise ValueError("SECRET_KEY no está definida. Verifica tu archivo .env")
        payload = jwt.decode(Token, str(SECRET_KEY), algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise Exception("⛔ El token ha expirado.")
    except JWTClaimsError:
        raise Exception("⚠️ El token no contiene los claims esperados.")
    except JWTError as e:
        raise Exception(f"❌ Token inválido: {e}")
