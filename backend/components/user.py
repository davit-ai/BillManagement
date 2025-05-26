import logging

from fastapi import HTTPException, Request
from model.models import User
from sqlalchemy.orm import Session


async def create_user(request: Request, db: Session):
    try:
        data = await request.json()
        print("Received data:", data)  # Debug print

        username = data.get("name")
        email = data.get("email")
        password = data.get("password")

        print(f"Name: {username}, Email: {email}")  # Debug print

        if not username or not email:
            raise HTTPException(status_code=400, detail="Name and email are required")

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
        new_user = User(username=username, email=email, password=password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return "User created successfully"
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error creating user: {str(e)}")  # Debug print
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
