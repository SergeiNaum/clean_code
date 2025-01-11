from pydantic import BaseModel, EmailStr, Field


class UserRegisterSchema(BaseModel):
    user_name: str
    password: str
    email: EmailStr


class AccessToken(BaseModel):
    access_token: str
    expired_at: int


class UserSchema(UserRegisterSchema):
    id: int = Field(default_factory=int)
