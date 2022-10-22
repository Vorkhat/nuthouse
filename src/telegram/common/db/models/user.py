from ..base import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    state = Column(String)
    position = Column(String)
