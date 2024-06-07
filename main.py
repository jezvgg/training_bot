from DB.DBHelper import DBHelper
from DB.creator import creator
from Src.Dialogue_manager import Dialogue_manager
from Src.Models import *


db = DBHelper('postgres', 'zkkur9fn', '127.0.0.1', '5432', 'training_bot')

res = db.get_models(User)
print(res)