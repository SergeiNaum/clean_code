from typing import Protocol, Self, Annotated
from fastapi import Depends

from src.apps.users.schemas import UserRegisterSchema, AccessToken


class UserUseCaseProtocol(Protocol):
    async  def register(self: Self, user_data: UserRegisterSchema) -> AccessToken:
        pass


class UserUseCaseImpl:
    async def register(self: Self, user_data: UserRegisterSchema) -> AccessToken:
        print(user_data)
        return AccessToken(access_token="123456789", expired_at=123456789)


async def get_users_use_case() -> UserUseCaseProtocol:
    return UserUseCaseImpl()


UsersUseCase = Annotated[UserUseCaseProtocol, Depends(get_users_use_case)]
