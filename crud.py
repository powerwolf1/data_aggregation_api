from typing import Optional
from sqlalchemy.orm import Session

import models, schemas


def create_moovie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movie).offset(skip).limit(limit).all()


def get_movie_by_genre(db: Session, genre: Optional[str] = None, release_year: Optional[int] = None, skip: int = 0, limit: int = 100):
    query = db.query(models.Movie)
    if genre:
        query = query.filter(models.Movie.genre.contains(genre))

    if release_year:
        query = query.filter_by(releaseYear=release_year)

    return query.offset(skip).limit(limit).all()


def get_movies_stats_per_genre(db: Session, genre: str):
    return db.query(models.Movie).filter(models.Movie.genre.contains(genre)).count()
