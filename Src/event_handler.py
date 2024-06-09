from Src.Events import *


class event_handler:
    __map: dict[str, event] = {'show': show_event}

    @classmethod
    def get_event(cls, eventname: str):
        return cls.__map[eventname]