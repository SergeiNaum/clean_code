from pydantic import BaseModel, EmailStr



class UserRegisterSchema(BaseModel):
    user_name: str
    password: str
    email: EmailStr


class AccessToken(BaseModel):
    access_token: str
    expired_at: int


class UserSchema(UserRegisterSchema):
    id: int
