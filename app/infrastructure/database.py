from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_DATABASE_URL = 'postgresql://postgres:17101717@localhost:5432/Restaurant_API_DB'

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

