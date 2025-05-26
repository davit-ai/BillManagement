import sys
from database.database import Base
from sqlalchemy import Column, Integer, String, DateTime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    item_id = Column(Integer)
    amount = Column(Integer)
    description = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    status = Column(String)  # e.g., 'pending', 'completed', 'failed'

class Enum(Base):
    __tablename__ = "enums"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(String, index=True)
    description = Column(String)