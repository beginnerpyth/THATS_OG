from sqlalchemy import text,create_engine,Integer,Table,String,MetaData,Column
from sqlalchemy.orm import sessionmaker,relationship,Session
engine=create_engine('postgresql+psycopg2://postgres@localhost:5432/haha')
conn=engine.connect()
#normal table creation
#conn.execute(text('drop table if exists library'))
#conn.commit()
#conn.execute(text('create table library (name varchar(44),ref_no int)'))
#conn.commit()
#conn.execute(text("insert into library(name,ref_no) values('musashino_library',1)"))
#conn.commit()
#using Session from sqlalchemy.orm
#pession=Session(engine)
#pession.execute(text('create table vast(name varchar(66),age int)'))
#pession.commit()
#using meta
meta=MetaData()
bb=Table('lala',meta,Column('nana',String(44)),Column('age',Integer))
meta.create_all(engine)
has=bb.insert().values([{'nana':'name','age':2}])
conn.execute(has)
conn.commit()
has=bb.insert().values(nana='kname',age=3)
conn.execute(has)
conn.commit()
