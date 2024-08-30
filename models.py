from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Author(Base):
    """
    Represents an author in the database.

    Attributes:
        id (int): The primary key of the author.
        name (str): The name of the author.
        email (str): The email of the author (unique).
        birthdate (Date): The birthdate of the author.
        bio (str): A short biography of the author.
        books (List[Book]): List of books written by the author.
    """
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    birthdate = Column(Date, nullable=False)
    bio = Column(String(250), nullable=True)

    books = relationship("Book", back_populates="author")


class Book(Base):
    """
    Represents a book in the database.

    Attributes:
        id (int): The primary key of the book.
        title (str): The title of the book.
        year (int): The year the book was published.
        isbn (str): The ISBN of the book (unique).
        author_id (int): Foreign key referencing the author of the book.
        author (Author): The author of the book.
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    year = Column(Integer, nullable=False)
    isbn = Column(String(13), unique=True, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")
