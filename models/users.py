from pydantic import BaseModel, Field


class User(BaseModel):

    email: str = Field(title="email")
    username: str = Field(title="username")
    fullname: str = Field(title="fullname", default="GuestUser")
    password: str = Field(title="password")


class UserLogin(BaseModel):

    username: str = Field(title="username")
    password: str = Field(title="password")
