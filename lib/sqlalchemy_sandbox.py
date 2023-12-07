#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///students.db")

class Student(Base):
    __tablename = "students"
    id = Column(Integer,primary_key = True),
    name = Column(String),
    age = Column(Integer)

if __name__ == '__main__':
    pass