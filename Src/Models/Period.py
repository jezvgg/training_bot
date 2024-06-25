from datetime import datetime
from dataclasses import dataclass


@dataclass
class Period:
    start: datetime
    end: datetime