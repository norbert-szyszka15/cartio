from sqlmodel import SQLModel, Field
from typing import Optional


class Item(SQLModel, table=True):
    __tablename__ = "items"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_done: bool = Field(default=False, nullable=False)