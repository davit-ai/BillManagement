from fastapi import HTTPException, Request
from sqlalchemy.orm import Session
from model.models import User
import logging

async def create_user(request: Request, db: Session):
    try:
        data = await request.json()
        print("Received data:", data)  # Debug print
        
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        
        print(f"Name: {name}, Email: {email}")  # Debug print

        if not name or not email:
            raise HTTPException(status_code=400, detail="Name and email are required")

        existing = db.query(User).filter(User.email == email).first()
        if existing:
            raise HTTPException(status_code=400, detail="User with this email already exists")

        new_user = User(name=name, email=email, password=password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"id": new_user.id, "name": new_user.name, "email": new_user.email}
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error creating user: {str(e)}")  # Debug print
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")