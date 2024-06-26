from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from DB.Tables.BaseTable import BaseTable
from DB.Tables.DialogueTable import DialogueTable
from DB.Tables.KeyboardsTable import KeyboardsTable
from DB.Tables.MessagesTable import MessagesTable
from DB.Tables.UserTable import UserTable
from DB.Tables.CommandsTable import CommandsTable
from DB.Tables.UserInfoTable import UserInfoTable
<<<<<<< HEAD
from DB.Tables.DietInfoTable import DietInfoTable
from DB.Tables.FeaturesTable import FeaturesTable
=======
from DB.Tables.FeaturesTable import FeaturesTable
>>>>>>> main
