from tests import client
from fastapi.testclient import TestClient
from main import app
from api.db.schemas import Book, Genre
from api.routes.books import db  # Import the in-memory DB instance

client = TestClient(app)
BASE_URL = "/api/v1/books"


def test_get_all_books():
    response = client.get(f"{BASE_URL}/")
    assert response.status_code == 200


def test_create_book():
    new_book = {
        "id": 4,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "publication_year": 1997,
        "genre": "Fantasy",
    }
    response = client.post(f"{BASE_URL}/", json=new_book)
    assert response.status_code == 201


def test_update_book():
    updated_book = {
        "id": 1,
        "title": "The Hobbit: An Unexpected Journey",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.put(f"{BASE_URL}/1", json=updated_book)
    assert response.status_code == 200


def test_delete_book():
    response = client.delete(f"{BASE_URL}/3")
    assert response.status_code == 204


def test_get_non_existent_book():
    response = client.get(f"{BASE_URL}/100")  # A non-existing book ID
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}
