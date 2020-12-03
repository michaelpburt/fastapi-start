from fastapi import APIRouter, HTTPException

from doodlebug.utils import JSONResponse
from doodlebug.schemas import item


router = APIRouter()


@router.get("/{item_id}", response_model=item.Item)
def get_item(item_id) -> JSONResponse:
    """
    Retrieve an item by `item_id`.
    """
    if item_id == item.Item.example_factory().item_id:
        return JSONResponse(
            content=item.Item.example_factory().dict(by_alias=True)
        )
    else:
        raise HTTPException(status_code=404, detail="item not found")
