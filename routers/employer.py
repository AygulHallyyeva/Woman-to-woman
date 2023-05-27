from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from models import baseSchema
from db import get_db
import crud
from models.models import Employer


employer_router = APIRouter()


@employer_router.post('/add-employer')
def add_employer(req: baseSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_employer(req, db)
        if result:
            return JSONResponse(status_code=status.HTTP_201_CREATED, content={'result': 'Successfully sign up!'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!!!')


@employer_router.get('/get-employer')
def get_employer( db: Session = Depends(get_db)):
    try:
        result = crud.read_employer(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')


@employer_router.delete('/delete-employer/{id}')
def delete_employer(id: int, db: Session = Depends(get_db)):
    try:
        result = crud.delete_employer(id, db)
        return JSONResponse(status_code=status.HTTP_200_OK, content={'result': 'Successfully deleted!!!'})
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')    


@employer_router.get('/search-employer')
def search_employer(q: str, db: Session = Depends(get_db)):
    try:
        result = crud.search_employer(q,db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Something went wrong!!!')   
    
    
    