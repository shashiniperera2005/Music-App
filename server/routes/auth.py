from fastapi import HTTPException
import bcrypt
from models.user import User
from pydantic_schemas.user_create import UserCreate
import uuid
from fastapi import APIRouter
from database import db

router = APIRouter()

@router.post("/signup")
def signup_user(user: UserCreate):
    # check if the user already exists in the db
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(400, "User with this email already exists")
        
    # add the user to the db
    
    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(
        id=str(uuid.uuid4()),
        name=user.name,
        email=user.email,
        password=hashed_pw
    )
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db