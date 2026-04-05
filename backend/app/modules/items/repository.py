from sqlmodel import Session, select
from app.modules.items.models import Item


class ItemRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[Item]:
        statement = select(Item)
        return list(self.session.exec(statement))

    def get_by_id(self, item_id: int) -> Item | None:
        return self.session.get(Item, item_id)

    def create(self, item: Item) -> Item:
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item

    def update(self, item: Item) -> Item:
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item

    def delete(self, item: Item) -> None:
        self.session.delete(item)
        self.session.commit()