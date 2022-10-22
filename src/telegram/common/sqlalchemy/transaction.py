from sqlalchemy.ext.asyncio import AsyncSession


async def set_transaction(db: AsyncSession):
    await db.connection()
