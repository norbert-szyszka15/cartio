from typing import Optional
from sqlmodel import SQLModel


class ItemCreate(SQLModel):
    name: str


class ItemRead(SQLModel):
    id: int
    name: str
    is_done: bool


class ItemUpdate(SQLModel):
    name: Optional[str] = None
    is_done: Optional[bool] = None