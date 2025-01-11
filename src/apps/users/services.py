from typing import Annotated, Protocol, Self

from fastapi import Depends

from src.apps.users.enums import NotificationProviderEnum
from src.apps.users.repositories import (
    NotificationEmailRepository,
    NotificationRepositoryProtocol,
    NotificationSmslRepository,
)
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
    async def make(self: Self, provider: NotificationProviderEnum) -> NotificationServiceProtocol:
        pass


class NotificationFactoryImpl(Protocol):
    def __init__(self: Self, settings: Settings) -> None:
        self.settings = settings

    async def make(self: Self, provider: NotificationProviderEnum) -> NotificationServiceProtocol:
        repository = None

        match provider:
            case NotificationProviderEnum.EMAIL:
                repository = NotificationEmailRepository(self.settings)
            case NotificationProviderEnum.SMS:
                repository = NotificationSmslRepository(self.settings)

        return NotificationServiceImpl(repository)


async def get_notification_factory(settings: SettingsService) -> NotificationFactoryProtocol:
    return NotificationFactoryImpl(settings)


NotificationFactory = Annotated[NotificationFactoryProtocol, Depends(get_notification_factory)]
