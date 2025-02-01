from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)
    # TODO как защитить hashed_password от случайного показа?
    hashed_password: Mapped[bytes]
    is_active: Mapped[bool] = mapped_column(default=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")


if TYPE_CHECKING:
    from src.posts.models import Post