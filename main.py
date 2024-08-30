from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import sys
sys.path.append('.')
import models, schemas, crud
from database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new author.

    Args:
        author (AuthorCreate): The author data.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        Author: The created author object.
    """
    return crud.create_author(db=db, author=author)

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new book.

    Args:
        book (BookCreate): The book data.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Raises:
        HTTPException: If the specified author does not exist.

    Returns:
        Book: The created book object.
    """
    author = db.query(models.Author).filter(models.Author.id == book.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return crud.create_book(db=db, book=book)

@app.get("/authors/{author_id}/books", response_model=List[schemas.Book])
def read_books(author_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Endpoint to retrieve books by a specific author.

    Args:
        author_id (int): The ID of the author.
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to return. Defaults to 10.
        db (Session, optional): The database session. Defaults to Depends(get_db).

    Returns:
        List[Book]: List of books written by the specified author.
    """
    books = crud.get_books_by_author(db, author_id=author_id, skip=skip, limit=limit)
    if not books:
        raise HTTPException(status_code=404, detail="Books not found")
    return books
