from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
