from dataclasses import dataclass, field
from Src.Models import TrainingExercise


@dataclass
class Training:
    '''
    Модель тренировки
    '''
    monday: list[TrainingExercise] = field(default_factory=list[TrainingExercise])
    tuesday: list[TrainingExercise] = field(default_factory=list[TrainingExercise])
    wednesday: list[TrainingExercise] = field(default_factory=list[TrainingExercise])
    thursday: list[TrainingExercise] = field(default_factory=list[TrainingExercise])
    friday: list[TrainingExercise] = field(default_factory=list[TrainingExercise])
    saturday: list[TrainingExercise] = field(default_factory=list[TrainingExercise])
    sunday: list[TrainingExercise] = field(default_factory=list[TrainingExercise])


    def __getitem__(self, key: int | str):
        if (isinstance(key, int) and (key > 6 or key < 0)) or \
            isinstance(key, str) and key not in self.days():
            return Exception('Immposible weekday.')

        if isinstance(key, int):
            return getattr(self, self.days()[key])

        return getattr(self, key)


    def json(self):
        result = {}

        for day, exercises in self.items():
            if len(exercises) <= 0: continue

            result[day] = []
            for exercise in exercises:
                result[day].append(exercise.json())

        return result


    def __str__(self):
        result = ''
        for day, exercises in self.json().items():
            result += f'\n{self.ru_days()[self.days().index(day)]}\n'
            for i, exercise in enumerate(exercises):
                result += f'   {i+1}. {exercise["description"]}[{exercise["link"]}]\n'

        return result
                

    def keys(self):
        return list(range(0, 7))


    def values(self):
        return [getattr(self, day) for day in self.days()]


    def items(self):
        return list(zip(self.days(), self.values()))


    def days(self):
        return ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    
    def ru_days(self):
        return ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

