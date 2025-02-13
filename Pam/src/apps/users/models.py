# from typing import Self

# from django.contrib.auth.models import AbstractUser
# from django.db.models import CharField, EmailField
# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _

# from apps.users.managers import UserManager

from sqlalchemy import Column, String, ForeignKey, DECIMAL, TIMESTAMP, Text
from sqlalchemy.orm import relationship
from src.database import Base

class User(Base):

    __tablename__ = "user"
    userID = Column(String, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50))

    annotations = relationship("Annotation", back_populates="user")


    # """Default custom user model."""

    # email = EmailField(_("email address"), unique=True)
    # username = None  # type: ignore
    # first_name = CharField(max_length=200)
    # last_name = CharField(max_length=200)

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []

    # objects = UserManager()

    # def get_absolute_url(self: Self) -> str:
    #     """Get URL for user's detail view.

    #     Returns
    #     -------
    #         str: URL for user detail.

    #     """
    #     return reverse("users:detail", kwargs={"pk": self.id})
