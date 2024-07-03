from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
from pydantic import BaseModel
from app.infrastructure.database import engine, SessionLocal
from sqlalchemy.orm import Session
from app.api import routes
from app.api import auth


def get_application():
    app = FastAPI(
        title="Aplicación Gestion de Restaurants",
        version="1.0.0"
    )

    app.include_router(auth.router)
    app.include_router(routes.router)
   
    
    return app


app = get_application()






    