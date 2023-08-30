import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}?user={os.getenv('POSTGRES_USER')}&password={os.getenv('POSTGRES_PASSWORD')}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={},
    future=True
    )

Sessionlocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True
)

Base = declarative_base()


def get_session():
    session = Sessionlocal()
    try:
        yield session

    finally:
        session.close()


def init_db():
    Base.metadata.create_all(bind=engine)












# import os
#
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from dotenv import load_dotenv
# from sqlalchemy.orm import sessionmaker
# from sqlmodel import create_engine, SQLModel, Session
#
# load_dotenv()
#
# DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
#
# engine = create_engine(DATABASE_URL, echo=True)



#
# def init_db():
#     SQLModel.metadata.create_all(engine)
#
#
# def get_session():
#     with Session(engine) as session:
#         yield session
#



# engine = create_engine(DATABASE_URL, echo=True)
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
#
#
# def init_db():
#     SQLModel.metadata.create_all(engine)
#
#
# def get_session():
#     with Session(engine) as session:
#         yield session
