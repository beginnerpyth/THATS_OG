from sqlalchemy import create_engine,text,MetaData,Insert,Select,Table,Column,String,Integer
from sqlalchemy.orm import Session
engine=create_engine('mysql+pymysql://root:password123@localhost/CORK')
conn=engine.connect()
conn.execute(text('DROP TABLE JOHN'))
conn.execute(text('CREATE TABLE JOHN(NAME VARCHAR(555),AGE INT)'))
conn.commit()
session=Session(engine)
session.execute(text('INSERT INTO JOHN VALUES("yusuke",20)'))
session.execute(text('INSERT INTO JOHN VALUES("sakai",23)'))
session.commit()
meta=MetaData()

son=Table('son',meta,Column('id',Integer,primary_key=True),Column('age',Integer,primary_key=False),Column('name',String(555),nullable=False))
meta.create_all(engine)
conn.execute(text('DELETE FROM son'))
conn.commit()
insert_statement=son.insert().values(age=22,name='RAI ABHISHEK')#in this one insert and values are both functions
conn.execute(insert_statement)
conn.commit()
where_statement=son.select().where(son.c.age>21)
result=conn.execute(where_statement)
for x in result.fetchall():
    print(x)

conn.execute(insert_statement)
conn.commit()
update_statement=son.update().where(son.c.age==22).values(name='RAI')
conn.execute(update_statement)
conn.commit()

people=Table('people',meta,Column('id',Integer),Column('name',String(555)))
meta.create_all(engine)

insert_people=people.insert().values([{'id':1,'name':'reiko'},{'id':2,'name':'seiko'}])
conn.execute(insert_people)
conn.commit()
#conn.execute(text('DROP TABLE EXE'))
#conn.execute(text('CREATE TABLE EXE(ID INT,NAME VARCHAR(444))'))
#conn.commit()
session.execute(text('INSERT INTO EXE VALUES(1,"SAM"),(2,"RAM")'))
session.commit()

#insert_statement=insert().values(1,'hari')
#conn.execute(insert_statement)
#conn.commit()
conn.execute(text('DROP TABLE loks'))
conn.commit()
bishal=Table('loks',meta,Column('id',Integer),Column('name',String(666)),Column('amount',Integer))
meta.create_all(engine)
session.execute(text("INSERT INTO loks VALUES(1,'MANI',33000),(2,'KUMAR',40000)"))#so i created table with meta and inserted with session
session.commit()
join_statement=exe.join(loks,exe.c.ID==loks.c.id)
select_statement=join_statement.select().with_only_columns(EXE.c.id,bishal.c.amount).select_from(join_statementf)