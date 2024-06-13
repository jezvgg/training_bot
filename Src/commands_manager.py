from Src.Models import Message, Command


class command_manager:
    '''
    Класс для работы и управлением коммандами.
    '''
    __messages: dict[str, Message]


    def __init__(self, commands: list[Command]):
        '''
        Args:
            commands - список моделей Command
        '''
        self.__messages = {}
        for command in commands:
            self.__messages[command.name] = command.message


    def __getitem__(self, key: str) -> Message:
        return self.get(key)


    def get(self, command_name: str) -> Message:
        '''
        Получить сообщение команды
        '''
        if command_name not in self.__messages.keys():
            raise Exception('Невозможно получить сообщение данной команды. Оно отсутствует.')

        return self.__messages[command_name]