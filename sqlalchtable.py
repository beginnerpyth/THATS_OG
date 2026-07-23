from sqlalchemy import create_engine,Integer,Column,String,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker,relationship


engine=create_engine("mysql+pymysql://root:password123@localhost/CORK")
base=declarative_base()
class dalley(base):
    name=Column(String(444))
    age=Column(Integer)
    id=Column(Integer,primary_key=True)
    sam=relationship("talley",back_populates="mama")
class talley(base):
    name=Column(String(555))
    age=Column(Integer)
    id=Column(Integer,primary_key=False)
    owner_id=Column(Integer,ForeignKey(dalley.id))
    mama=relationship("dalley",back_populates="sam")

base.metadata.create_all(engine)

Session=sessionmaker(bind="engine")
session=Session()
object1=dalley()
session.add()


