from http.client import HTTPException

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from user_management import database, schemas, oauth2
from user_management.repository import user


router = APIRouter(
    prefix="/users",
    tags=['users']
)

get_db = database.get_db


@router.post('/register', response_model=schemas.User)
def register(request: schemas.User, db: Session = Depends(get_db)):
    existing_user = user.fetch(request.username, db)
    if existing_user :
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Username is already registered.")

    new_user = user.create(request, db)
    if new_user :
        return new_user
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Could not create user.")

@router.get('/{id}', response_model=schemas.Login)
def get_user(id : int, db : Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)) :
    return user.get(id, db)

