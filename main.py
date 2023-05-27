from fastapi import FastAPI
from db import Base, engine
from routers import employee_router, employer_router, image_router

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(employee_router, tags=['Employees'])
app.include_router(employer_router, tags=['Employers'])
app.include_router(image_router, tags=['Images'])
