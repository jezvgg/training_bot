from typing import Protocol
from aiogram.types import message
from Src.Models import User


class event(Protocol):

    @staticmethod
    def activate(user: User, message: message) -> str:
        pass