from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from DB.Tables import DialogueTable
from DB.Tables import KeyboardsTable
from DB.Tables import MessagesTable
from DB.Tables import UserTable