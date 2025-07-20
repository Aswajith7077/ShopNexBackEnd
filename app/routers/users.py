from typing import Annotated

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Response, status

from app.dependencies import check_access_token
from models.users import User
from services.application.users import find_single_user, insert_user, update_user

router = APIRouter(
    prefix="/users",
    # dependencies = [Depends(check_access_token)],
    tags=["Users"],
)


@router.get("/get_user/{id}")
async def get_single_user(id: str):

    result, e = await find_single_user(id)
    if e is not None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail={"message": e})

    result.pop("_id")
    return result


@router.put("/update_user/")
async def update_single_user(username: str, user: User):

    result, exception = await update_user(username, user)
    if result:
        return Response(status_code=status.HTTP_202_ACCEPTED, content="User Updated")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail={"message": exception}
    )
