from sqlalchemy import Column, String, Boolean, Integer
from database import Base


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    region = Column(String, nullable=True)
    language = Column(String, nullable=True)
    titleType = Column(String, nullable=True)
    isAdult = Column(Boolean, nullable=True)
    releaseYear = Column(String, nullable=True)
    genre = Column(String, nullable=True)



