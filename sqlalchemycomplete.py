from sqlalchemy import MetaData,Integer,String,Float,create_engine,text,Table,Column,func,select
from sqlalchemy.orm import Relationship,Session
engine=create_engine('mysql+pymysql://root:password123@localhost/CORK')
conn=engine.connect()
#using engine creating the table
conn.execute(text('DROP TABLE IF EXISTS RISAHA'))
conn.commit()
conn.execute(text('DROP TABLE IF EXISTS ANGER'))
conn.commit()
conn.execute(text('CREATE TABLE IF NOT EXISTS ANGER(NAME VARCHAR(555) ,CLASS VARCHAR(666),ID INT)'))
conn.commit()

session=Session(engine)
session.execute(text('INSERT INTO ANGER VALUES("RIVERSTONE","LOW",1)'))
session.commit()
#using meta creating the table 
meta=MetaData()
jay=Table('jain',meta,Column('name',String(555)),Column('id',Integer),Column('age',Integer))

play=Table('risaha',meta,Column('name',String(555)),Column('age',Integer),Column('id',Integer))
meta.create_all(engine)
damn=jay.insert().values([{'name':'abhishek','id':1,'age':33},{'name':'salim','id':2,'age':44}])
spit=play.insert().values([{'name':'ganeesha','age':3000,'id':3},{'name':'mansiha','age':33,'id':2},{'name':'kanisha','age':44,'id':2}])
conn.execute(spit)
conn.commit()
conn.execute(damn)
conn.commit()
groupe=play.select().with_only_columns(play.c.id,func.sum(play.c.age)).select_from(play).group_by(play.c.id)
b=conn.execute(groupe)
joinw=jay.join(play,jay.c.id==play.c.id)
select_joinw=select(play,jay).select_from(joinw)

#lets_see=conn.execute(select_joinw)
#for g in lets_see.fetchall():
#    print(g)

#for x in b.fetchall():
#    print(x)
justselect=joinw.select().with_only_columns("*").select_from(joinw)
justselectexe=conn.execute(justselect)
for n in justselectexe.fetchall():
    print(n)
group_by=play.select().with_only_columns(play.c.id,func.sum(play.c.age)).select_from(joinw).group_by(play.c.id)
gg=conn.execute(group_by)
for x in gg.fetchall():
    print(x)


