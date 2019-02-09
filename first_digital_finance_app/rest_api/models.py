from sqlalchemy import Column, Integer, String, Date, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import DB_CONNECTION_STRING, SCHEMA

Base = declarative_base(metadata=MetaData(schema=SCHEMA))
engine = create_engine(DB_CONNECTION_STRING, echo=True)
session = sessionmaker()

session.configure(bind=engine)
session = session()


class Client(Base):
    __tablename__ = "tt_clients"

    id = Column(Integer, primary_key=True)
    last_name = Column(String(255))
    first_name = Column(String(255))
    dob = Column(Date)
    social_status_id = Column(Integer)
    gender = Column(String(1))


class Dictionary(Base):
    __tablename__ = 'tt_dictionary'

    id = Column(Integer, primary_key=True)
    category = Column(String(25))
    str_id = Column(String(50))
    int_id = Column(String(Integer))
    value = Column(String(255))
