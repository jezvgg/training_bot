from DB.Tables import BaseTable
from Src.Models import Command, Message
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class CommandsTable(BaseTable):
    __tablename__ = 'commands'

    commandtext = Column('command_text', String, unique=True, primary_key=True)
    message_id = Column('message_id', Integer, ForeignKey('dialogue.id'), nullable=False)

    _message = relationship('DialogueTable')


    @staticmethod
    def build(model: Command):
        return CommandsTable(model.name, model.message.id)


    def __init__(self, command_text: str, message_id: int):
        self.commandtext = command_text
        self.message_id = message_id


    def model(self) -> Command:
        args = ['']
        if self._message: args.append(self._message.model())
        else: args.append(Message.error_message())
        args.append(self.commandtext)
        return Command(*args)