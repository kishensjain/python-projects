from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
  
app = FastAPI()

class Book(BaseModel):
    id : int
    name: str
    author: str

books: List[Book] = []