from fastapi import APIRouter, HTTPException
from services.health_service import get_system_health

router = APIRouter()

@router.get("/health",status_code=200)
def get_health():

    try:
        metrics = get_system_health()
        return metrics
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
