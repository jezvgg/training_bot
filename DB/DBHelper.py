from DB.Tables import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Engine


class DBHelper:
    session: sessionmaker
    engine: Engine

    def __init__(self, user: str, password: str, host: str, port: str, database: str):
        url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        # TODO: сделать проверку на наличие БД
        self.engine = create_engine(url, echo=True)

        Base.metadata.create_all(bind=self.engine)

        self.session = sessionmaker(bind=self.engine)()
