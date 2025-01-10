from fastapi import APIRouter

from src.apps.users.schemas import AccessToken, UserRegisterSchema
from src.apps.users.use_cases import UsersUseCase

router = APIRouter(tags=["users"])


@router.post("/users/register")
async def users_register(user_data: UserRegisterSchema, users_use_case: UsersUseCase) -> AccessToken:
    return await users_use_case.register(user_data)