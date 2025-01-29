from sqlalchemy.orm import Mapped, mapped_column

from src.models import Base


class User(Base):
    email: Mapped[str] = mapped_column(unique=True)
    # TODO как защитить hashed_password от случайного показа?
    hashed_password: Mapped[bytes]
    is_active: Mapped[bool] = mapped_column(default=True)
