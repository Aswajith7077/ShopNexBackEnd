from fastapi import APIRouter, Body, Query

from app.dependencies import check_access_token
from models.products import SearchFormData
from services.application.products import (
    get_products,
    retrive_product_details,
    search_product_details,
)

router = APIRouter(
    prefix="/products",
    # dependencies = [Depends(check_access_token)],
    tags=["Products"],
)


@router.get("/list_products")
async def list_products(limit: int = Query()):
    result = await get_products(limit=limit)
    return result


@router.get("/get_details")
async def get_product_details(id: str):
    result = await retrive_product_details(id)
    result["DESC"] = result["DESC"].split("ã€")
    return result


@router.post("/search/")
async def search_products(form_data: SearchFormData = Body()):
    result = await search_product_details(form_data=form_data)
    return result
