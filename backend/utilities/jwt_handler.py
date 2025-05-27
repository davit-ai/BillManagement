from datetime import datetime, timedelta

from jose import JWTError, jwt
from utilities.getTimeDate import now_withoutstring

# Secret key — should be kept secure
SECRET_KEY = "helloworldthisismyapp"  # Replace with env var in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 hour


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = now_withoutstring() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
