from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
  
app = FastAPI()

class Book(BaseModel):
    id : int
    name: str
    author: str

books: List[Book] = []

@app.get("/")
def read_root():
    return {"message":"Welcome to the library!"}

@app.get("/books")
def get_books():
    return books

@app.post("/book")
def add_book(book: Book):
    books.append(book)
    return {"message": "Book added successfully"}, 201 

@app.put("/book/{id}")
def update_book(book_id: int, updated_book: Book):
    for b in books:
        if b.id == book_id:
            b.name = updated_book.name
            b.author = updated_book.author
            return b, {"message": "Book updated successfully"}
    return {"message": "Book not found"}, 404

@app.delete("/book/{id}")
def delete_book(book_id: int):
    for b in books:
        if b.id == book_id:
            books.remove(b)
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}, 404