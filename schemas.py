from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    releaseYear: int
    region: str
    language: str
    titleType: str
    isAdult: bool
    genre: str


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieBase):
    pass


class MovieInDBBase(MovieBase):
    id: int

    class Config:
        from_attributes = True
