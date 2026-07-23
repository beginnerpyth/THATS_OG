from sqlalchemy  import create_engine,text,MetaData,Integer,String,Column,Table,Insert
from sqlalchemy.orm import Session

engine=create_engine('mysql+pymysql://root:password123@localhost/CORK')

conn=engine.connect()
conn.execute(text('DROP TABLE SASA'))
conn.commit()
conn.execute(text('CREATE TABLE SASA (ID INT,NAME VARCHAR(555),SALARY INT)'))
conn.commit()
session=Session(engine)
#conn=session.connect()
session.execute(text('INSERT INTO SASA VALUES(1,"REINA",22000)'))
session.commit()
conn.execute(text('DROP TABLE justein'))
conn.commit()
meta=MetaData()
just=Table('justein',meta,Column('id',Integer,primary_key=True),Column('name',String(666)),Column('age',Integer))
bust=Table('neil',meta,Column('owner',Integer,primary_key=True),Column('Description',String(333)),Column('price',Integer))
meta.create_all(engine)
#tamesi=just.insert()
jon=just.insert().values([{'name':'reiko','age':15},{'name':'seiko','age':19}])
conn.execute(jon)#we used just as variablt to store the table,MetaData, i.e imported from sqlalchemy
conn.commit()
#update_statement=just.update().where(just.c.id==1).values(name='phonsi')
#conn.execute(update_statement)#so we need to insert the variable name where table is stored
#conn.commit()

#delete_statement=just.delete().where(just.c.id==1)
#conn.execute(delete_statement)
#conn.commit()
#join through sqlalchemy
#join_alc=
son=bust.insert().values([{'Description':'labtop','price':2200},{'Description':'books','price':300}])
conn.execute(son)
conn.commit()
join_alc=bust.join(just,bust.c.owner==just.c.id)
specific_c=bust.select().with_only_columns(just.c.id,bust.c.price,bust.c.Description).select_from(join_alc)
baby=conn.execute(specific_c)
for x in baby.fetchall():
    print(x)








