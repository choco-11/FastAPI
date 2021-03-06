from email.policy import default
from enum import unique
from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key = True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer,ForeignKey('users.id'))

    owner = relationship('Users', back_populates='todos')


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key =True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name =Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    todos = relationship('Todos', back_populates = 'owner')
