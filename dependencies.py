#In order to remove the need for implementing DB session initialization for each endpoints, we use book_dal as a dependency of our endpoint.


from database.config import async_session
from database.dals.book_dal import BookDAL


async def get_book_dal():
    async with async_session() as session:
        async with session.begin():
            yield BookDAL(session)
