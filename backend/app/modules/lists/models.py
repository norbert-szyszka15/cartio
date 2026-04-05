from sqlmodel import SQLModel, Field
from typing import Optional

class List(SQLModel, table=True):
    __tablename__ = "lists"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str