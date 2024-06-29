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



    def __init__(self, db: DBInterface):
        self._db = db
        self.__settings=settings.from_json()


    def activate(self, user: User, message: types.Message) -> Message:
        info_body = self._db._get_one(UserInfoTable, user.id)
        info_diet = self._db._get_ones(DietInfoTable, user.id)

        info_diet = sorted(info_diet, key=lambda x: x.subscribe_id)[-1]


        
        gpt_answer=self.get_diet(info_body,info_diet)

        info_diet.diet=gpt_answer
        self._db._update()
  
        user.current_message.text=user.current_message.text.format(diet=gpt_answer)
        
        return user.current_message

    
    def get_diet(self,info_body,info_diet):

        

        with open('gpt_request.json') as json_file:
            gpt_request = json_file.read()
        
        
        arg={
        "{token}": self.__settings.token_for_gpt,
        "{bot_id}": self.__settings.id_bot_gpt,
        "{gender}": {True:'Мужской', False:'Женский'}[info_body.gender],
        "{age}": str(info_body.age),
        "{weight}": str(info_body.weight),
        "{height}": str(info_body.height),
        "{product}": info_diet.product,
        "{goal}": info_diet.diet_goal,
        "{count_traings}": info_diet.count_trainings}
        
        gpt_request=self.__format_prompt(gpt_request,**arg)
        gpt_request= json.loads(str(gpt_request))
        url=gpt_request['url']
        headers= gpt_request['headers']
        data=gpt_request['data']
        
        
        response = post(url, headers=headers, json=data)
        response = response.json()
        return response["messages"][0]["content"]
        
    

    def __format_prompt(self,text,**kwargs):
        for i in kwargs.items():
            text=text.replace(i[0],i[1])
        return text
    

    
    


  


        

        

        


        
        

        