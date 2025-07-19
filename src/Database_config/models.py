from sqlalchemy.orm import Mapped, mapped_column
from .config import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    correo: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
