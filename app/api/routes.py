from fastapi import APIRouter, Depends, HTTPException
from app.domain.schemas import User
from app.infrastructure import orm_model
from typing import List, Annotated
from pydantic import BaseModel
from app.infrastructure.database import engine, SessionLocal
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/rutas',
    tags=['ingredientes']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/createuser")
async def create_users(user: User, db:db_dependency):
    db_user = orm_model.Users(email= user.email, hashed_password= user.hashed_password,fullname= user.fullname,rol= user.rol)
    db.add(db_user)
    db.commit()
    