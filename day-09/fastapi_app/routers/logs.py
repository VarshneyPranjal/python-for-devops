from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/logs",status_code=200)
def get_logs():
    try:
        return {"message":"logs are in progress"}
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )