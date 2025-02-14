from fastapi import APIRouter

from .routes import books

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])
