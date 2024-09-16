import csv
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import crud
import schemas
from dependencies import get_db
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/movies/")
async def get_movies_by_genre(genre: Optional[str] = None, release_year: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_movie_by_genre(db=db, genre=genre, release_year=release_year)


@app.get("/movies/count/")
async def get_movies_count_by_genre(genre: str, db: Session = Depends(get_db)):
    return crud.get_movies_stats_per_genre(db=db, genre=genre)


@app.get("/data_filler/")
async def data_filler(db: Session = Depends(get_db)):

    with open("./title.akas.tsv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = tuple(next(reader))

        for _ in range(0, 20000):
            for row in reader:
                line = ','.join(row).split('\t')

                if line[-1] == '1':
                    title_id = line[0]

                    with open("./title.basics.tsv", newline="") as basics_file:
                        reader2 = csv.reader(basics_file, delimiter=",")
                        header = tuple(next(reader2))

                        for row2 in reader2:
                            line2 = ','.join(row2).split('\t')

                            if line2[0] == title_id:
                                movie = schemas.MovieCreate(
                                    title=line[2],
                                    region=line[3],
                                    language=line[4],
                                    releaseYear=line2[5],
                                    titleType=line2[1],
                                    isAdult=line2[4],
                                    genre=line2[-1]
                                )
                                crud.create_moovie(db=db, movie=movie)

        return {"message": "Data filled successfully"}
