import sched
from typing import Callable
from datetime import timedelta
import asyncio
import time


class Cron:
    '''
    Асинхронный класс вызывающий функцию которую в него передадут
    с периодом в delay.

    Работает только с асинхронными функциями.
    '''
    func: Callable
    delta: float


    def __init__(self, func: Callable, delay: timedelta) -> None:
        self.func = func
        self.delta = float(delay.total_seconds())


    async def __call__(self) -> None:
        while True:
            asyncio.create_task(self.func())
            await asyncio.sleep(self.delta)


def every(period: timedelta):
    '''
    Декоратор оборачивающий функцию в класс Cron.
    '''

    def scheduler(func):

        async def wrapper(*args, **kwargs):
            cron = Cron(func, period)
            asyncio.ensure_future(cron())

        return wrapper

    return scheduler
