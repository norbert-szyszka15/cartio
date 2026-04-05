from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.db.session import get_session
from app.modules.items.schemas import ItemCreate, ItemRead, ItemUpdate
from app.modules.items.service import ItemService
from app.modules.items.repository import ItemRepository

router = APIRouter()


def get_service(session: Session = Depends(get_session)) -> ItemService:
    repo = ItemRepository(session)
    return ItemService(repo)


@router.get("/", response_model=list[ItemRead])
def list_items(service: ItemService = Depends(get_service)):
    return service.list_items()


@router.get("/{item_id}", response_model=ItemRead)
def get_item(item_id: int, service: ItemService = Depends(get_service)):
    item = service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=ItemRead, status_code=201)
def create_item(
    data: ItemCreate,
    service: ItemService = Depends(get_service),
):
    return service.create_item(data)


@router.patch("/{item_id}", response_model=ItemRead)
def update_item(
    item_id: int,
    data: ItemUpdate,
    service: ItemService = Depends(get_service),
):
    item = service.update_item(item_id, data)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}", status_code=204)
def delete_item(
    item_id: int,
    service: ItemService = Depends(get_service),
):
    ok = service.delete_item(item_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Item not found")
    return None