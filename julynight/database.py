from sqlalchemy.orm import DeclarativeBase,sessionmaker,Session
from sqlalchemy import create_engine
from pydantic_settings import BaseSettings


class Base(DeclarativeBase):
    pass



class Settings(BaseSettings):
    database_url=str
    debug:bool=False
    secret_key:str='nothing'
    algorithm:str='HS256'
    access_token:int=30

#Config is built in and make sure you put inside Settings so BaseSettings find the Config and search the env file
    class Config():
        env_file='.env'


settings=Settings()#with this it called class and env values are passed








engine=create_engine(settings.database_url)
sessionlocal=sessionmaker(bind=engine)

def get_db():
    pession=sessionlocal()
    try:
        yield pession
    finally:
        pession.close()


        