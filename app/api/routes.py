from fastapi import APIRouter, Depends, HTTPException
from app.domain.schemas import User
from app.domain.schemas import Ingredient
from app.infrastructure import orm_model
from typing import List, Annotated
from pydantic import BaseModel
from app.infrastructure.database import engine, SessionLocal
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/Inventario',
    tags=['Gestion Inventario']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/registrar_ingrediente")
async def create_ingredient(ingredient: Ingredient, db:db_dependency):
    db_ingredient = orm_model.Ingredients(fullname= ingredient.fullname, Almacen= ingredient.Almacen, Cantidad= ingredient.Cantidad)
    db.add(db_ingredient)
    db.commit()


@router.put("/modificar_ingrediente/{nombre}")
async def update_ingredient_by_name(nombre: str, ingredient: Ingredient, db:db_dependency):
    db_ingredient = db.query(orm_model.Ingredients).filter(orm_model.Ingredients.fullname == nombre).first()

    if not db_ingredient:
        return {"message": "Ingrediente no encontrado"}, 404

    db_ingredient.fullname = ingredient.fullname
    db_ingredient.Almacen = ingredient.Almacen
    db_ingredient.Cantidad = ingredient.Cantidad

    db.commit()
    return {"message": "Ingrediente actualizado exitosamente"}

@router.delete("/eliminar_ingrediente/{nombre}")
async def delete_ingredient_by_name(nombre: str, db: db_dependency):
    db_ingredient = db.query(orm_model.Ingredients).filter(orm_model.Ingredients.fullname == nombre).first()

    if not db_ingredient:
        return {"message": "Ingrediente no encontrado"}, 404

    db.delete(db_ingredient)
    db.commit()
    return {"message": "Ingrediente eliminado exitosamente"}