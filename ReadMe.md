# FastAPI Project

This project is a FastAPI application with a MySQL backend, demonstrating basic CRUD operations for authors and books. It includes endpoints to create authors, create books, and retrieve books by author.

## Prerequisites

Before you start, ensure you have the following installed:

- Python 3.8 or higher
- MySQL Server

## Installation

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/ziptie_fastapi_test.git
cd fastapi_test
```
### 2. Set Up the Virtual Environment

Create and activate a virtual environment:

#### On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Create a MySQL database.

```bash
CREATE DATABASE bookstore_db;
```

Create a `.env` file in the root of the project with the following content:
```bash
DATABASE_URL=mysql+mysqlconnector://yourusername:yourpassword@localhost/bookstore_db
```

### 5. Start the FastAPI Server

Run the FastAPI application with Uvicorn:

```bash
uvicorn main:app --reload

```

The application should now be accessible at http://127.0.0.1:8000.

## API Testing
To test the API endpoints, you can use the provided Postman collection.

### 1. Import the Postman Collection

- Open Postman.
- Go to File -> Import.
- Select ZipTie_Test.postman_collection.json and import it.

### 2. Run the Collection

- Once imported, you can run the collection to test the API endpoints. The collection includes various requests to test the functionality of the API.

## Project Structure

- main.py: Entry point for the FastAPI application.
- models.py: SQLAlchemy ORM models.
- schemas.py: Pydantic schemas for request and response validation.
- crud.py: CRUD operations for interacting with the database.
- database.py: Database setup and connection configuration.
- requirements.txt: List of Python dependencies.
