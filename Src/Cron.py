import sched
from typing import Callable
from datetime import timedelta
import asyncio
import time


class Cron:
    func: Callable
    delta: float


    def __init__(self, func: Callable, delay: timedelta) -> None:
        self.func = func
        self.scheduler = sched.scheduler(timefunc=time.monotonic, delayfunc=asyncio.sleep)
        self.delta = float(delay.seconds)


    async def __call__(self) -> None:
        while True:
            asyncio.create_task(self.func())
            await asyncio.sleep(self.delta)


def every(period: timedelta):

    def scheduler(func):

        async def wrapper(*args, **kwargs):
            cron = Cron(func, period)
            asyncio.ensure_future(cron())

        return wrapper

    return scheduler
