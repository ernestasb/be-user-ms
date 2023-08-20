"""
Module containing the schemas for the user model
"""

from pydantic import BaseModel, ConfigDict, EmailStr, constr


class UserGet(BaseModel):
    """
    Schema for getting a user
    """

    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    name: str
    surname: str


class UserCreate(BaseModel):
    """
    Schema for creating a user
    """

    email: EmailStr
    password: constr(min_length=4, max_length=20)
    name: constr(min_length=4, max_length=20)
    surname: constr(min_length=4, max_length=20)


class UserChangePassword(BaseModel):
    """
    Schema for changing user password
    """

    id: int
    old_password: str
    new_password: constr(min_length=4, max_length=20)


class UserUpdate(BaseModel):
    """
    Schema for updating user data
    """

    name: constr(min_length=4, max_length=20) | None = None
    surname: constr(min_length=4, max_length=20) | None = None
