from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine 

DATABASE_URL = 'postgresql://postgres:#256Shart@localhost:5432/fluttermusicapp'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()