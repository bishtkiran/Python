from datetime import datetime, timedelta
from jose import JWTError, jwt

from user_management import schemas

SECRET_KEY = "0b8618223b3bd19158ca0d318e20fa9d259b516216b2c1c24c80090a4786ffa2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
