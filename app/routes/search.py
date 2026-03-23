from fastapi import APIRouter

from app.schemas.search_schema import CarrierResponse, SearchRequest
from app.services.search_service import get_carriers


router = APIRouter(tags=["search"])


@router.post("/search", response_model=list[CarrierResponse], status_code=200)
async def search_carriers(payload: SearchRequest) -> list[CarrierResponse]:
    return get_carriers(payload.origin, payload.destination)
