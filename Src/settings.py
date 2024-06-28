from dataclasses import dataclass
import json
import os


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


    @staticmethod
    def from_env():
        '''
        Создать конфиги из переменных сред
        '''
        return settings(os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'), os.environ.get('DB_HOST'),
                        os.environ.get('DB_PORT'), os.environ.get('DB_NAME'), os.environ.get('DB_URL'), 
                        os.environ.get('TOKEN'))

    @staticmethod
    def from_json():
        '''
        Создать конфиги из переменных сред
        '''
        with open('settings.json') as json_file:
            data = json.load(json_file)
        return settings(data['DB_USER'], data['DB_PASSWORD'], data['DB_HOST'],
                        data['DB_PORT'], data['DB_NAME'],data['DB_URL'], data['TOKEN'], data['account_id'],data["secret_key"])

    def database_kwargs(self) -> dict:
        return {
            'user':self.db_username,
            'password':self.db_password,
            'host':self.db_host,
            'port':self.db_port,
            'database':self.db_name
        }


    def database_args(self) -> list:
        return list(self.database_kwargs().values())


    @property
    def db_username(self) -> str:
        return self.__db_username


    @property
    def db_password(self) -> str:
        return self.__db_password


    @property
    def db_host(self) -> str:
        return self.__db_host


    @property
    def db_port(self) -> str:
        return self.__db_port


    @property
    def db_name(self) -> str:
        return self.__db_name


    @property
    def bot_token(self) -> str:
        return self.__bot_token

    
    @property
    def db_url(self) -> str:
        return self.__db_url
    

    @property
    def secret_key(self) -> str:
        return self.__secret_key

    
    @property
    def account_id(self) -> str:
        return self.__account_id