from Src.Events.event import event
from aiogram import types
from Src.Models import User, Message
from Src.dialogue_manager import dialogue_manager
from DB.DBInterface import DBInterface
from DB.Tables import UserInfoTable
from DB.Tables import DietInfoTable
from Src.settings import settings
from requests import post
import json


            
    
class diet_get_event(event):
    '''
    Ивент для получения диеты без опроса.
    '''
    _db: DBInterface
    __settings:settings
    __info_body:UserInfoTable=None
    __info_diet:DietInfoTable=None


    def __init__(self, db: DBInterface):
        self._db = db
        self.__settings=settings.from_json()


    def activate(self, user: User, message: types.Message) -> Message:
        self.__info_body = self._db._get_one(UserInfoTable, user.id)
        self.__info_diet = self._db._get_one(DietInfoTable, user.id)

        
        gpt_answer=self.get_diet()

        return user.current_message.text.format(text=gpt_answer)

    
    def get_diet(self):

        

        with open('gpt_request.json') as json_file:
            gpt_request = json_file.read()

        arg={
        "{token}": self.__settings.token_for_gpt,
        "{bot_id}": self.__settings.id_bot_gpt,
        "{gender}": {True:'Мужской', False:'Женский'}[self.__info_body.gender],
        "{age}": str(self.__info_body.age),
        "{weight}": str(self.__info_body.weight),
        "{height}": str(self.__info_body.height),
        "{product}": self.__info_diet.product,
        "{goal}": self.__info_diet.diet_goal,
        "{count_traings}": self.__info_diet.count_trainings}
        gpt_request=self.__format_rpompt(gpt_request,**arg)

        gpt_request= json.loads(gpt_request)

        url=gpt_request['url']
        headers= gpt_request['headers']
        data=gpt_request['data']
      
        response = post(url, headers, data)
        return response["messages"][0]["content"]
    

    def __format_rpompt(self,text,**kwargs):
        for i in kwargs.items():
            text=text.replace(i[0],i[1])
        return text
    

    
    


  


        

        

        


        
        

        