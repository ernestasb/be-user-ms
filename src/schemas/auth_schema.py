from pydantic import BaseModel, ConfigDict, EmailStr, constr


class LoginSchema(BaseModel):
    """Schema for login"""

    email: EmailStr
    password: constr(min_length=4, max_length=20)


class TokenSchema(BaseModel):
    """Schema to return and accept token"""

    access_token: str
