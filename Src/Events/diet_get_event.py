from Src.Events.event import event
from aiogram import types
from Src.Models import User, Message
from Src.dialogue_manager import dialogue_manager
from DB.DBInterface import DBInterface
from DB.Tables import UserInfoTable
from DB.Tables import DietInfoTable
from Src.settings import settings
from requests import post

class diet_get_event(event):
    '''
    Ивент для получения диеты без опроса.
    '''
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
        text = user.current_message.text.format(
            diet=gpt_answer

            
        )

        finish_message = Message(0, text, 0)
        return finish_message


    
    def get_diet(self):

        

        with open('gpt_request.json') as json_file:
            gpt_request = json_file.read()

        gpt_request=gpt_request.replace("{token}", self.__settings.token_for_gpt)
        gpt_request=gpt_request.replace("{bot_id}", self.__settings.id_bot_gpt)
        gpt_request=gpt_request.replace("{gender}", {True:'Мужской', False:'Женский'}[self.__info_body.gender])
        gpt_request=gpt_request.replace("{age}", str(self.__info_body.age))
        gpt_request=gpt_request.replace("{weight}", str(self.__info_body.weight))
        gpt_request=gpt_request.replace("{height}", str(self.__info_body.height))
        gpt_request=gpt_request.replace("{product}", self.__info_diet.product)
        gpt_request=gpt_request.replace("{goal}", self.__info_diet.diet_goal)
        gpt_request=gpt_request.replace("{count_traings}", self.__info_diet.count_trainings)
        
        gpt_request= eval(gpt_request)

        url=gpt_request['url']
        headers= gpt_request['headers']
        data=gpt_request['data']
        response = post(url, headers=headers, json=data)
        response=response.json()
        return response["messages"][0]["content"]
    


  


        

        

        


        
        

        