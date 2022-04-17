from fastapi import APIRouter

from models.utils import get_dateset

router = APIRouter(prefix="/date")


@router.get("/create")
def create_dateset_api():
    return get_dateset()
