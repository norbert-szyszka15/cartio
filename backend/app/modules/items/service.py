from app.modules.items.repository import ItemRepository
from app.modules.items.models import Item
from app.modules.items.schemas import ItemCreate, ItemUpdate


class ItemService:
    def __init__(self, repo: ItemRepository):
        self.repo = repo

    def list_items(self) -> list[Item]:
        return self.repo.get_all()

    def get_item(self, item_id: int) -> Item | None:
        return self.repo.get_by_id(item_id)

    def create_item(self, data: ItemCreate) -> Item:
        item = Item(name=data.name)
        return self.repo.create(item)

    def update_item(self, item_id: int, data: ItemUpdate) -> Item | None:
        item = self.repo.get_by_id(item_id)
        if not item:
            return None

        if data.name is not None:
            item.name = data.name
        if data.is_done is not None:
            item.is_done = data.is_done

        return self.repo.update(item)

    def delete_item(self, item_id: int) -> bool:
        item = self.repo.get_by_id(item_id)
        if not item:
            return False

        self.repo.delete(item)
        return True