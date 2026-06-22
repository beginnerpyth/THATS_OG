from sqlalchemy import create_engine,text,MetaData,Integer,Column,Table,String,select,func,ForeignKey
from sqlalchemy.orm import declarative_base,relationship,sessionmaker,Session
from  dotenv import load_dotenv 
import os
load_dotenv()
engine=create_engine(os.getenv('DATABASE_URL'))



conn=engine.connect()

conn.execute(text('drop table if exists hari'))
conn.commit()
conn.execute(text('create table hari(nepali varchar(55),age int)'))
conn.commit()
conn.execute(text("insert into hari values('k_rey',12)"))
conn.commit()
selecto=conn.execute(text('select * from hari'))
for x in selecto:
    print(x)
pession=Session(engine)

pession.execute(text('drop table if exists jhari'))
pession.commit()
pession.execute(text('create table jhari(nepali varchar(55),type varchar(44))'))
pession.commit()
pession.execute(text("insert into jhari values('k_rey','zuma')"))
pession.commit()

meta=MetaData()
jjk=Table('ssk',meta,Column('name',String),Column('age',Integer))
meta.create_all(engine)
insert_stat=jjk.insert().values(name='shyam',age=15)
pession.execute(insert_stat)
pession.commit()
select_stat=select().with_only_columns(jjk.c.name)
be=pession.execute(select_stat)
for r in be:
    print(r)
where_stat=select(jjk).where(jjk.c.age>3)
bes=pession.execute(where_stat)
for j in bes:
    print(j,'here')
func_stat=select(func.count()).select_from(jjk)
func_stat_result=pession.execute(func_stat)
for x in func_stat_result:
    print(x,'there')
fuc_stat2=select(func.sum(jjk.c.age)).select_from(jjk)
cc=pession.execute(fuc_stat2)
for c in cc:
    print(c)


#just like metadata haleko thyo creaate garney bela testai yaha pani base.metadata.create_all(engine) garney
base=declarative_base()
class shit(base):
    __tablename__='rama'
    name=Column(String(44))
    age=Column(Integer)
    id=Column(Integer,primary_key=True)
    shi=relationship('shit2',back_populates='phi')

  

class shit2(base):
    __tablename__='sama'
    name=Column(String(44))
    age=Column(Integer)
    id=Column(Integer,primary_key=True)

    pd=Column(Integer,ForeignKey(shit.id))
    phi=relationship('shit',back_populates='shi')



base.metadata.create_all(engine)
gession=sessionmaker(bind=engine)
mession=gession()



object1=shit(name='samamoto',age=33)
mession.add(object1)
mession.flush()
mession.commit()


object2=shit2(name='kamamoto',age=22,id=object1.id,pd=object1.id)
mession.add(object2)
mession.commit()
print(object1.name)
print(object2.name)
select_stat=mession.execute(select(func.count(shit2.id))).all()
select_where=mession.execute(select(shit).where(shit.id==2)).all()
for x in select_stat:
    print(x)
print(select_where,'here i')
print(mession.execute(select(func.count(shit2.id))).all(),'here we got this')

# join example (fixed typo: oin_stat -> join_stat, and fixed join condition to use FK pd)
join_stat=mession.execute(select(shit).join(shit2,shit.id==shit2.pd)).all()
for j in join_stat:
    print(j,'and here')


# scalars example (fixed: .scalar() -> .scalars())
select_stat2=mession.execute(select(shit)).scalars().all()
print(select_stat2,'gogog')
#jj = mession.execute(select(shit)).scalars().all()
#print(jj)
join_stat = mession.execute(select(shit).join(shit2, shit.id == shit2.pd)).scalars().all()
for j in join_stat:
    print(j.id)          # j is a Row containing ONE shit object → looks like object repr
jj = mession.execute(select(shit).where(shit.id==shit2.pd)).scalars().all()
for bb in jj:
    print(bb.id)

for x in jj:
  print(x.id, 'jjjjk')
  result = mession.execute(select(shit)).scalars().all()#scalars juts there to unwrap the tuples 
for obj in result:
    print(obj.id, obj.name, obj.age)   # only real columns

bara=mession.execute(select(*shit.__table__.c)).all()#*it means seperate the data of table name 
print(bara)
mara=mession.execute(select(*shit.__table__.c)).all()
print(mara)
result = mession.execute(select(shit)).all()
for row in result:
    print(row[0].id)#here we dont use scalars so it doenst unwrap and its same as tuple and we nned to unwrap tuple and get the attribute

