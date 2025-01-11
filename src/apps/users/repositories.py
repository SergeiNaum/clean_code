from typing import Protocol, Self

from src.settings import Settings


class NotificationRepositoryProtocol(Protocol):
    async def notify(self: Self, message: str) -> bool:
        pass


class NotificationEmailRepository:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def notify(self: Self, message: str) -> bool:
        print(f"send Email message: {message}, Сайт: {self.settings.base_url}")
        return True


class NotificationSmslRepository:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def notify(self: Self, message: str) -> bool:
        print(f"send SMS message: {message}, Сайт: {self.settings.base_url}")
        return True
