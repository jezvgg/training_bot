from datetime import datetime
from dataclasses import dataclass


@dataclass
class Period:
    '''
   Временой период.
   У него есть начало (start) и конец (end)
    '''
    start: datetime
    end: datetime