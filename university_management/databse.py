from sqlalchemy.orm  import sessionmaker,Session,DeclarativeBase
from sqlalchemy import Integer,Table,Column,create_engine
from pydantic_settings import BaseSettings
from pydantic import BaseModel


class BaseMl(BaseModel):
    pass

class CaseML(DeclarativeBase):
    pass

class google(BaseSettings):
    database_url:str
    secret_pass:str='password'


    class Config():
        env_file='.env'
runny=google()

eng=create_engine(runny.database_url)
lession=sessionmaker(bind=eng)

def get_db():
    ossion=lession()
    try:
        yield ossion
    finally:
        ossion.close()

gg=CaseML()





        











