from typing import Annotated, Protocol, Self

from fastapi import BackgroundTasks, Depends

from src.apps.users.enums import NotificationProviderEnum
from src.apps.users.schemas import AccessToken, UserRegisterSchema, UserSchema
from src.apps.users.services import NotificationFactory, NotificationFactoryProtocol, NotificationServiceProtocol


class UserUseCaseProtocol(Protocol):
    async def register(self: Self, user_data: UserRegisterSchema) -> AccessToken:
        pass


class UserUseCaseImpl:
    def __init__(self: Self, notification_factory: NotificationFactoryProtocol, bg_task: BackgroundTasks):
        self.notify_factory = notification_factory
        self.bg_task = bg_task

    async def register(self: Self, user_data: UserRegisterSchema) -> AccessToken:
        user: UserSchema = UserSchema.model_validate(user_data, from_attributes=True)
        notification_service: NotificationServiceProtocol = await self.notify_factory.make(
            NotificationProviderEnum.EMAIL
        )
        self.bg_task.add_task(notification_service.user_register, user)
        return AccessToken(access_token="123456789", expired_at=123456789)


async def get_users_use_case(notify_factory: NotificationFactory, bg_task: BackgroundTasks) -> UserUseCaseProtocol:
    return UserUseCaseImpl(notify_factory, bg_task)


UsersUseCase = Annotated[UserUseCaseProtocol, Depends(get_users_use_case)]
