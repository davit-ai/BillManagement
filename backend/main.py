from components import user
from database.database import SessionLocal, engine
from fastapi import Body, Depends, FastAPI, Form, HTTPException, Request
from model import models
from sqlalchemy.orm import Session

# from fastapi.security import OAuth2PasswordBearer
# from utilities.jwt_handler import verify_access_token

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/register", status_code=201)
async def register_user(
    request: Request,
    db: Session = Depends(get_db),
    ## to have form while using swagger
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
):
    data = {"username": username, "email": email, "password": password}
    request._json = data
    return await user.register_user(request, db)

## added jwt authentication
@app.post("/login")
async def login_user(
    request: Request, db: Session = Depends(get_db), data: dict = Body(...)
):
    return await user.login_user(request, db)
