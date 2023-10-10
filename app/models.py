from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

connection_string = f'postgresql+psycopg2://postgres:admin@postgres:5432/test'
engine = create_engine(connection_string)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, nullable=False)
    question_text = Column(String, nullable=False)
    question_answer = Column(String, nullable=False)
    created_at = Column(DateTime)


def create_database_tables():
    connection = engine.connect()
    if not engine.dialect.has_table(connection, Question.__tablename__):
        Base.metadata.create_all(engine)
    connection.close()


create_database_tables()
