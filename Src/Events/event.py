from typing import Protocol
from aiogram import types
from Src.Models import User


class event(Protocol):

    def activate(self, user: User, message: types.Message) -> str:
        pass