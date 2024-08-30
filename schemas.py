from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import List, Optional

class BookBase(BaseModel):
    title: str
    year: int
    isbn: str = Field(..., min_length=10, max_length=13)

class BookCreate(BookBase):
    author_id: int

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True

class AuthorBase(BaseModel):
    name: str
    email: EmailStr
    birthdate: date
    bio: Optional[str] = None

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: List[Book] = []

    class Config:
        orm_mode = True
