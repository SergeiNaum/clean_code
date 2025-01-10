from typing import Protocol, Self, Annotated
from fastapi import Depends

from src.apps.users.repositories import NotificationRepositoryProtocol
from src.apps.users.schemas import UserSchema
from src.settings import Settings, SettingsService


class NotificationServiceProtocol(Protocol):
    async def user_register(self: Self, user: UserSchema) -> bool:

        return True


class NotificationServiceImpl:
    def __init__(self: Self, repository: NotificationRepositoryProtocol):
        self.repository = repository

    async def user_register(self: Self, user: UserSchema) -> bool:
        template = f"Hello, {user.user_name} !"
        await self.repository.notify(template)
        return True


class NotificationFactoryProtocol(Protocol):

    async def make(self: Self, provider: str) -> NotificationServiceProtocol:
        pass

class NotificationFactoryImpl(Protocol):
    def __init__(self: Self, settings: Settings) -> None:
        self.settings = settings


    async def make(self: Self, provider: str) -> NotificationServiceProtocol:
        pass


async def get_notification_factory() -> NotificationFactoryProtocol:
    return NotificationFactoryImpl()


async def get_notification_service(settings: SettingsService) -> NotificationServiceProtocol:
    return NotificationServiceImpl()


NotificationServiceUseCase = Annotated[NotificationServiceProtocol, Depends(get_notification_service)]
NotificationFactory = Annotated[NotificationFactoryProtocol, Depends(get_notification_factory)]