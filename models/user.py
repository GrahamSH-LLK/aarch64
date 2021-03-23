from typing import List

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str


class Project(BaseModel):
    name: str
    users: List[str]