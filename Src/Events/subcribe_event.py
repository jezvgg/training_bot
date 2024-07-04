from Src.Events.event import event
from aiogram import types
from Src.Models import User, Message
from Src.dialogue_manager import dialogue_manager
from DB.Tables import SubscribeInfo
from DB.DBInterface import DBInterface
from Src.settings import settings
import datetime
from Src.Models import Subscribe
from yookassa import Configuration,Payment
import asyncio
import uuid
import json


class subscribe_event(event):
    '''
    Ивент для подписки.
    В нем  производиться полата и выдается стартовая подписка на 7 дней.
    '''

    _db: DBInterface
    __settings:settings



    def __init__(self, db: DBInterface):
        self._db = db
        self.__settings=settings.from_env()

    def activate(self, user: User, message: types.Message) -> Message:
        subscribes = self._db._get_ones(SubscribeInfo, user.id)
        subscribes= sorted(subscribes, key=lambda x: x.subscribe_id)
        if len(subscribes)==0:
            user.current_message.text=self.get_start(user)
        elif subscribes[-1].subscribe_end > datetime.datetime.now():
            user.current_message.next_message_id=0
            return user.current_message
        else:

            user.current_message.text=self.pay_subscribe(user)   
            
            

        return user.current_message
    
    # Функция выдачи стартовой подписки 
    def get_start(self, user: User):
        sub=SubscribeInfo(user.id, datetime.datetime.now().date(), (datetime.datetime.now()+datetime.timedelta(days=7)).date(),0)
        self._db._add(sub)
        

        return user.current_message.text
    

    def pay_subscribe(self, user: User):
        subscribes = self._db._get_ones(SubscribeInfo, user.id)
        pay=self.pay()
        pay_link=pay['confirmation']['confirmation_url']
        pay_id=pay['id']
        asyncio.ensure_future(self.check_payment(pay_id,user))       
        
        return user.current_message.text.format(link=pay_link)
    
    
    def pay(self): 

        Configuration.account_id = self.__settings.account_id
        Configuration.secret_key = self.__settings.secret_key

        payment = Payment.create({
            "amount": {
                "value": "100",
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://t.me/Teaching138bot"
            },
            "capture": True,
            "description": "Подписка на бота"
        }, uuid.uuid4())
        return json.loads(payment.json())

    async def check_payment(self, payment_id, user: User,):
        payment = json.loads((Payment.find_one(payment_id)).json())
        while payment['status'] == 'pending':
            payment = json.loads((Payment.find_one(payment_id)).json())
            await asyncio.sleep(3)

        if payment['status']=='succeeded':
            subscribes = self._db._get_ones(SubscribeInfo, user.id)
            subscribes= sorted(subscribes, key=lambda x: x.subscribe_id)[-1]
            if subscribes.count_subskribe_day==0:
                sub_day=7
            else:
                sub_day=subscribes.count_subskribe_day
            sub=SubscribeInfo(user.id, datetime.datetime.now().date(), (datetime.datetime.now()+datetime.timedelta(days=30)).date(), sub_day)
            self._db._add(sub)
            
    
    