from DB.Tables import BaseTable
from Src.Models import Message
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class DialogueTable(BaseTable):
    __tablename__ = 'dialogue'

    id = Column("id", Integer, unique=True, primary_key=True)
    text = Column("text", Integer, ForeignKey("messages.id"), nullable=False)
    keyboard = Column("keyboard", Integer, ForeignKey("keyboards.id"))
    eventname = Column("eventname", String)
    next_message = Column("next_message", Integer, ForeignKey("dialogue.id"), nullable=False)

    _text = relationship('MessagesTable')
    _keyboard = relationship('KeyboardsTable')


    @staticmethod
    def build(model: Message):
        dialog = DialogueTable(model.id, model.text, model.next_message_id)
        if model.keyboard: dialog.keyboard = model.keyboard.id
        if model.event_name: dialog.eventname = model.event_name
        return dialog


    def __init__(self, id: int, text: int, next_message: int, keyboard: int = None, eventname: str = None):
        self.id = id
        self.text = text
        self.keyboard = keyboard
        self.eventname = eventname
        self.next_message = next_message


    def model(self) -> Message:
        args = {"_Message__id":self.id}
        if self._text: args|={"_Message__text":self._text.text}
        else: args |= {"_Message__text":Message.error_message().text}
        args|={"_Message__next_message_id":self.next_message}
        if self.eventname: args|={"_Message__event_name":self.eventname}
        if self._keyboard: args|={"_Message__keyboard":self._keyboard.model()}
        return Message(**args)
    