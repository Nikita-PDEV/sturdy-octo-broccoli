from fastapi import APIRouter, HTTPException  
from .database import Database  
from .models import Pereval  

router = APIRouter()  
db = Database()  

@router.on_event("startup")  
async def startup_event():  
    await db.connect()  

@router.on_event("shutdown")  
async def shutdown_event():  
    await db.close()  

@router.post("/submitData/", response_model=dict)  
async def submit_data(pereval: Pereval):  
    try:  
        await db.add_pereval(  
            beautyTitle=pereval.beautyTitle,  
            title=pereval.title,  
            other_titles=pereval.other_titles,  
            connect=pereval.connect,  
            coord_id=pereval.coord_id,  
            level_winter=pereval.level_winter,  
            level_spring=pereval.level_spring,  
            level_summer=pereval.level_summer,  
            level_autumn=pereval.level_autumn,  
        )  
        return {"message": "Pereval added successfully", "status": "new"}  
    except Exception as e:  
        raise HTTPException(status_code=500, detail=str(e))