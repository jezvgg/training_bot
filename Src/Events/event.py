from typing import Protocol
from aiogram.types import message
from Src.Models import User


class event(Protocol):

    def activate(self, user: User, message: message) -> str:
        pass