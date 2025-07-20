from datetime import datetime, timezone

from fastapi import APIRouter, Header, HTTPException, status

from config.config import jwt_refresh_token_expiry_time_minutes
from models.users import User, UserLogin
from services.application.auth import Authenticate, CurrentUser
from services.application.users import insert_user

router = APIRouter(prefix="/auth", tags=["Auth"])

a = Authenticate()
c = CurrentUser()


@router.get("/refresh")
async def refresh_access_token(refresh_token: str):
    user = await c.get_current_user_by_refresh_token(refresh_token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Refresh Token"
        )

    user.update({"lastlogin": datetime.now(timezone.utc).isoformat()})
    access_token = a.generate_access_token(user)
    return {"access_token": access_token, "refresh_token": refresh_token}


@router.get("/check_access_token")
async def check_access_token(authorization=Header()):
    print(authorization.split())


@router.post("/add_user")
async def add_user(form_data: User):
    print(form_data)

    result, e = await insert_user(form_data)
    print(result)
    if result:
        return {"message": "Created new User"}
    print(e)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)


@router.get("/check_refresh_token")
async def check_refresh_token(refresh_token: str):
    result = await c.get_current_user_by_refresh_token(refresh_token.encode())
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Invalid Refresh Token"
        )
    difference = datetime.now(timezone.utc) - datetime.fromisoformat(
        result["lastlogin"]
    )
    difference_in_minutes = difference.total_seconds() / 60

    if difference_in_minutes >= jwt_refresh_token_expiry_time_minutes:
        return {**result, "refresh_token_validity": False}
    else:
        return {**result, "refresh_token_validity": True}


@router.post("/login")
async def login_user(form_data: UserLogin):

    global a
    result = await a.authenticate_user(form_data.username, form_data.password)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Either User not present or Invalid password",
        )

    current_time = datetime.now(timezone.utc)
    user_data = {**result, "lastlogin": current_time.isoformat()}
    user_data.pop("_id")
    access_token = a.generate_access_token(user_data)
    refresh_token = a.generate_refresh_token(user_data)
    return {
        "username": form_data.username,
        "fullname": user_data["fullname"],
        "access_token": access_token,
        "refresh_token": refresh_token,
    }
