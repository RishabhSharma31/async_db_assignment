
from typing import List, Optional

from fastapi import APIRouter, Depends

# from database.config import async_session
from database.dals.book_dal import BookDAL
from database.models.book import Book
from dependencies import get_book_dal


router = APIRouter()


# @router.post("/books")
# async def create_book(name: str, author: str):
#     async with async_session() as session:
#         async with session.begin():
#             book_dal = BookDAL(session)
#             return await book_dal.create_book(name, author)


# @router.get("/books")
# async def get_all_books() -> List[Book]:
#     async with async_session() as session:
#         async with session.begin():
#             book_dal = BookDAL(session)
#             return await book_dal.get_all_books()

        
# @router.put("/books/{book_id}")
# async def update_book(book_id: int, name: Optional[str] = None, author: Optional[str] = None):
#     async with async_session() as session:
#         async with session.begin():
#             book_dal = BookDAL(session)
#             return await book_dal.update_book(book_id, name, author)

@router.post("/books")
async def create_book(name: str, author: str, book_dal: BookDAL = Depends(get_book_dal)):
    return await book_dal.create_book(name, author)


@router.put("/books/{book_id}")
async def update_book(book_id: int, name: Optional[str] = None, author: Optional[str] = None, book_dal: BookDAL = Depends(get_book_dal)):
    return await book_dal.update_book(book_id, name, author)


@router.get("/books")
async def get_all_books(book_dal: BookDAL = Depends(get_book_dal)) -> List[Book]:
    return await book_dal.get_all_books()