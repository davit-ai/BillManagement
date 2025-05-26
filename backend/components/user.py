from fastapi import HTTPException, Request
from model.models import User
from sqlalchemy.orm import Session
from utilities.getTimeDate import now
from utilities.security import hash_password


async def create_user(request: Request, db: Session):
    try:
        data = await request.json()
        print("Received data:", data)  # Debug print

        username = data.get("name")
        email = data.get("email")
        password = data.get("password")

        print(f"Name: {username}, Email: {email}")  # Debug print

        if not username or not email or not password:
            raise HTTPException(status_code=400, detail="All field are required")

        existing = (
            db.query(User)
            .filter(User.email == email, User.username == username)
            .first()
        )
        if existing:
            raise HTTPException(
                status_code=400, detail="User with this email already exists"
            )
        print("Creating new user...")  # Debug print
        new_user = User(
            username=username,
            email=email,
            password=hash_password(password),
            created_at=now(),
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return "User created successfully"
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error creating user: {str(e)}")  # Debug print
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


# def read_items(db: Session):
#     return db.query(Item).all()

# def read_item(db: Session, item_id: int):
#     item = db.query(Item).filter(Item.id == item_id).first()
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item

# def update_item(db: Session, item_id: int, data: dict):
#     item = db.query(Item).filter(Item.id == item_id).first()
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     for key, value in data.items():
#         setattr(item, key, value)
#     db.commit()
#     db.refresh(item)
#     return item

# def delete_item(db: Session, item_id: int):
#     item = db.query(Item).filter(Item.id == item_id).first()
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     db.delete(item)
#     db.commit()
#     return {"detail": "Item deleted"}
