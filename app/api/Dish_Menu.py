from fastapi import APIRouter, Depends, HTTPException
from app.domain.schemas import Menu
from app.domain.schemas import Platillos
from app.infrastructure import orm_model
from typing import List, Annotated
from pydantic import BaseModel
from app.infrastructure.database import engine, SessionLocal
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/Dish&Menu',
    tags=['Gestion Menu y Platos']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

#GESTION PLATILLOS

@router.post("/registrar_platillo")
async def create_dish(platillo: Platillos, db:db_dependency):
    db_dish = orm_model.Platillos(fullname= platillo.fullname, MetodoPreparacion= platillo.MetodoPreparacion, Ingredientes= platillo.Ingredientes, Menu= platillo.Menu, Precio=platillo.Precio)
    db.add(db_dish)
    db.commit()


@router.put("/modificar_platillo/{nombre}")
async def update_dish_by_name(nombre: str, platillo: Platillos, db:db_dependency):
    db_dish = db.query(orm_model.Platillos).filter(orm_model.Platillos.fullname == nombre).first()

    if not  db_dish:
        return {"message": "Platillo no encontrado"}, 404

    db_dish.fullname = platillo.fullname
    db_dish.MetodoPreparacion = platillo.MetodoPreparacion
    db_dish.Ingredientes = platillo.Ingredientes
    db_dish.Menu = platillo.Menu
    db_dish.Precio = platillo.Precio

    db.commit()
    return {"message": "Platillo actualizado exitosamente"}

@router.delete("/eliminar_platillo/{nombre}")
async def delete_dish_by_name(nombre: str, db: db_dependency):
    db_dish = db.query(orm_model.Platillos).filter(orm_model.Platillos.fullname == nombre).first()

    if not db_dish:
        return {"message": "Platillo no encontrado"}, 404

    db.delete(db_dish)
    db.commit()
    return {"message": "Platillo eliminado exitosamente"}

#GESTION MENUS

@router.post("/registrar_menu")
async def create_menu(menu: Menu, db:db_dependency):
    db_menu = orm_model.Menu(fullname= menu.fullname, Platos= menu.Platos)
    db.add(db_menu)
    db.commit()

@router.put("/modificar_menu/{nombre}")
async def update_menu_by_name(nombre: str, menu: Menu, db:db_dependency):
    db_menu = db.query(orm_model.Menu).filter(orm_model.Menu.fullname == nombre).first()

    if not  db_menu:
        return {"message": "Menu no encontrado"}, 404

    db_menu.fullname = menu.fullname
    db_menu.Platos = menu.Platos
   

    db.commit()
    return {"message": "Menu actualizado exitosamente"}

@router.delete("/eliminar_menu/{nombre}")
async def delete_menu_by_name(nombre: str, db: db_dependency):
    db_menu = db.query(orm_model.Menu).filter(orm_model.Menu.fullname == nombre).first()

    if not db_menu:
        return {"message": "Menu no encontrado"}, 404

    db.delete(db_menu)
    db.commit()
    return {"message": "Menu eliminado exitosamente"}

