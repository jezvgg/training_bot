from dataclasses import dataclass
import json
import os
import json


@dataclass
class settings:
    '''
    Конфигурационый класс
    '''
    __db_username: str
    __db_password: str
    __db_host: str
    __db_port: str
    __db_name: str
    __db_url: str
    __bot_token: str
    __account_id:int
    __secret_key:str
    __token_for_gpt: str
    __id_bot_gpt: str


    @staticmethod
    def from_env():
        '''
        Создать конфиги из переменных сред
        '''
        return settings(os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'), os.environ.get('DB_HOST'),
                        os.environ.get('DB_PORT'), os.environ.get('DB_NAME'), os.environ.get('DB_URL'), 
                        os.environ.get('TOKEN'), os.environ.get('account_id'), os.environ.get('secret_key'),
                        os.environ.get('TOKEN_FOR_GPT'), os.environ.get('BOT_ID'))
    
    
    @staticmethod
    def from_json(path: str = 'settings.json'):
        '''
        Создать конфиги из переменных сред
        '''
        with open(path) as json_file:
            data = json.load(json_file)
        return settings(data.get('DB_USER'), data.get('DB_PASSWORD'), data.get('DB_HOST'),
                        data.get('DB_PORT'), data.get('DB_NAME'),data.get('DB_URL'), 
                        data.get('TOKEN'), data.get('account_id'),data.get("secret_key"),
                        data.get('TOKEN_FOR_GPT'), data.get('BOT_ID'))


    def database_kwargs(self) -> dict:
        return {
            'user':self.db_username,
            'password':self.db_password,
            'host':self.db_host,
            'port':self.db_port,
            'database':self.db_name
        }


    def database_args(self) -> list:
        '''аргументы базы данных'''
        return list(self.database_kwargs().values())


    @property
    def db_username(self) -> str:
        '''имя пользователя бд'''
        return self.__db_username


    @property
    def db_password(self) -> str:
        '''название пароля от пользователя'''
        return self.__db_password


    @property
    def db_host(self) -> str:
        '''хост базы данных'''
        return self.__db_host


    @property
    def db_port(self) -> str:
        '''порт'''
        return self.__db_port


    @property
    def db_name(self) -> str:
        '''имя бд'''
        return self.__db_name


    @property
    def bot_token(self) -> str:
        '''токен бота'''
        return self.__bot_token


    @property
    def token_for_gpt(self) -> str:
        '''токен для gpt'''
        return self.__token_for_gpt
    

    @property
    def id_bot_gpt(self) -> str:
        '''айди бота и гпт'''
        return self.__id_bot_gpt


    
    @property
    def db_url(self) -> str:
        '''url для базы данных'''
        return self.__db_url

    

    @property
    def secret_key(self) -> str:
        return self.__secret_key

    
    @property
    def account_id(self) -> str:
        return self.__account_id
