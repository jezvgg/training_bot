from dataclasses import dataclass

@dataclass
class Standart:
    smt: int

s = Standart()

s = Standart()
print(vars(s), dir(s), '\n\n')

class Standart2:
    some_field: int = 0

s2 = Standart2()
print(vars(s2), dir(s2), '\n\n', s2.__annotations__)