from sqlalchemy import Integer,Column,create_engine,String,Table,Boolean
from database import Base




class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    phone = Column(String, nullable=True)  # NEW
    test= Column(String,nullable=False)
    



