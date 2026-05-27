import json
import os
from models import Book

DATA_FILE = "books.json"

def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [Book.from_dict(item) for item in data]

def save_books(books):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([book.to_dict() for book in books], f,
                  ensure_ascii=False, indent=4)

def add_book(book):
    books = load_books()
    for b in books:
        if b.author == book.author and b.title == book.title:
            raise ValueError("Книга с таким автором и названием уже существует")
    books.append(book)
    save_books(books)

def delete_book(author, title):
    books = load_books()
    new_books = [b for b in books
                 if not (b.author == author and b.title == title)]
    if len(new_books) == len(books):
        raise ValueError("Книга не найдена")
    save_books(new_books)

def get_all_books():
    return load_books()