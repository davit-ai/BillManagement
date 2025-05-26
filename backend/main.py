from components import user
from database.database import SessionLocal, engine
from fastapi import Body, Depends, FastAPI, Request
from model import models
from sqlalchemy.orm import Session

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


@app.post("/user")
async def create_user(
    request: Request, db: Session = Depends(get_db), data: dict = Body(...)
):
    return await user.create_user(request, db)
