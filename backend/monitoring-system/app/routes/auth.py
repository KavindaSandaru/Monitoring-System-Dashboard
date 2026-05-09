from fastapi import APIRouter

from app.database import SessionLocal
from app.models.user import User
from app.schemas.auth_schema import RegisterUser
from app.auth.hash import hash_password

from app.schemas.auth_schema import LoginUser
from app.auth.hash import verify_password
from app.auth.jwt_handler import create_access_token

router = APIRouter()


@router.post("/register")
def register(user: RegisterUser):

    db = SessionLocal()

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()

    return {
        "message": "User created successfully"
    }

@router.post("/login")
def login(user: LoginUser):

    db = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        return {
            "error": "User not found"
        }

    valid_password = verify_password(
        user.password,
        existing_user.password
    )

    if not valid_password:
        return {
            "error": "Invalid password"
        }

    token = create_access_token({
        "sub": existing_user.email
    })

    return {
        "access_token": token
    }