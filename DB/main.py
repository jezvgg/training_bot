import psycopg2
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = "person"

    ssn = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    age = Column("age", Integer, )
    gender = Column("gender", CHAR)

    def __init__(self, ssn, name, age, gender):
        self.ssn = ssn
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"({self.ssn}, {self.name}, {self.age}, {self.gender})"


engine = create_engine("postgresql://postgres:zkkur9fn@127.0.0.1:5432/postgres", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(3, "Mike", 18, "f")
print
session.add(person)
session.commit()


















# conn = psycopg2.connect(host='127.0.0.1', dbname='postgres', user='postgres',
#                         password='zkkur9fn', port=5432)

# cur = conn.cursor()

# cur.execute('''CREATE TABLE IF NOT EXISTS person (
#     id INT PRIMARY KEY,
#     name VARCHAR(255),
#     age INT,
#     gender CHAR
# );
# ''')

# cur.execute('''INSERT INTO person (id, name, age, gender) VALUES
# (1, 'Mike', 30, 'm'),
# (2, 'Lisa', 30, 'f');
# ''')

# conn.commit()
# conn.close()