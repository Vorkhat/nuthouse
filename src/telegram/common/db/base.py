from src.config import Config
from sqlalchemy import MetaData
from typing import AsyncIterator
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


engine = create_async_engine(
        Config.SQLALCHEMY_POSTGRESQL_URL,
        future=True,
        echo=True
)
metadata = MetaData(bind=engine)

Base = declarative_base(metadata=metadata)


def session_factory(expire_on_commit: bool = True) -> AsyncSession:
    return sessionmaker(
            bind=engine,
            class_=AsyncSession,
            expire_on_commit=expire_on_commit
    )()


async def get_db() -> AsyncIterator[AsyncSession]:
    session = session_factory()
    try:
        yield session
        await session.commit()
    except:
        await session.rollback()
    finally:
        await session.close()

