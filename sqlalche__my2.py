from sqlalchemy import Integer,String,Float,MetaData,create_engine,Column,ForeignKey,text
from sqlalchemy.orm import declarative_base,relationship,sessionmaker
engine=create_engine('mysql+pymysql://root:password123@localhost/CORK')
base=declarative_base()
conn=engine.connect()

conn.execute(text('DROP TABLE IF EXISTS things'))
conn.commit()
conn.execute(text('DROP TABLE IF EXISTS people'))
conn.commit()
class Person (base):
    __tablename__ = 'people'
    id=Column(Integer,primary_key=True)
    name=Column(String(555),nullable=False)
    age=Column(Integer)
    things=relationship('Thing',back_populates='person')
class Thing(base):
    __tablename__ = 'things'
    owner =Column(Integer,ForeignKey('people.id'))#because the foreign key is here and mutltiple row of things can relate
    #to one row of people so thats why Person.things.description is should be list not single object but when i do Thing.person.name it
    #fetches the exact name cause it should be only one because id is primary_keyth
    description=Column(String(555),nullable=False)
    value = Column(Float)
    id=Column(Integer,primary_key=True)
    person=relationship('Person',back_populates='things')

base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()
new_object1=Person(name='tsukamoto',age=59)
session.add(new_object1)
session.flush()

new_object2=Thing(description='gentsuki',value=250000,owner=new_object1.id,id=new_object1.id)
session.add(new_object2)
session.commit()

print([x.description for x in new_object1.things])#just because foreignkey is in things it emans the person can be acesed single but interms
#of things it can have many data referring to person class so we have tpo access the data of thig class in a list
print(new_object2.person.name)

#first=session.query(Person.name).all()
#print(first)





