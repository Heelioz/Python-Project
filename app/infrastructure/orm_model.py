from sqlalchemy import Column, Integer, String, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:17101717@localhost:5432/Restaurant_API_DB"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Users(Base):
    __tablename__ ='Users'
    id = Column(Integer, primary_key=True, index= True)
    email= Column(String, index=True)
    hashed_password= Column(String, index=True)
    fullname = Column(String, index=True)
    rol = Column(String, index= True)

class Ingredients(Base):
    __tablename__ ='Ingredientes'
    id = Column(Integer, primary_key=True, index= True)
    fullname = Column(String, index=True)
    Almacen = Column(String, index= True)
    Cantidad = Column(String, index= True)

metadata = MetaData()
Base.metadata.create_all(bind=engine)


    