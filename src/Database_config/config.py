from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url = URL.create(
    drivername="postgresql",
    username="dei",
    password="dei12345",
    host="db",
    port=5432,
    database="fastapi_db",
)

engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
