from sqlalchemy.orm import Session
import sys
sys.path.append('.')
import models, schemas

def create_author(db: Session, author: schemas.AuthorCreate):
    """
    Creates a new author in the database.

    Args:
        db (Session): The database session.
        author (AuthorCreate): The author data to insert.

    Returns:
        Author: The created author object.
    """
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def create_book(db: Session, book: schemas.BookCreate):
    """
    Creates a new book in the database.

    Args:
        db (Session): The database session.
        book (BookCreate): The book data to insert.

    Returns:
        Book: The created book object.
    """
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books_by_author(db: Session, author_id: int, skip: int = 0, limit: int = 10):
    """
    Retrieves books written by a specific author, with pagination support.

    Args:
        db (Session): The database session.
        author_id (int): The ID of the author whose books are to be retrieved.
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to return. Defaults to 10.

    Returns:
        List[Book]: List of books written by the specified author.
    """
    return db.query(models.Book).filter(models.Book.author_id == author_id).offset(skip).limit(limit).all()
