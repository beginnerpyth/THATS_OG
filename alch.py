from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# Database connection using MySQL
engine = create_engine('mysql+pymysql://root:password123@localhost/CORK')

# Part 1: Managing the Table Structure
with engine.connect() as conn:
    # Dropping and creating the table to ensure a fresh start
    conn.execute(text('DROP TABLE IF EXISTS ALCHEMY'))
    conn.commit()
    
    conn.execute(text('CREATE TABLE ALCHEMY (NAME VARCHAR(555), AGE INT)'))
    conn.commit()

# Part 2: Inserting Data using a Session
session = Session(engine)
try:
    # Inserting the 'ALCHEMIST' record
    session.execute(text("INSERT INTO ALCHEMY (NAME, AGE) VALUES ('ALCHEMIST', 22)"))
    session.commit()
    print("Data inserted successfully!")
except Exception as e:
    session.rollback()
    print(f"An error occurred: {e}")
finally:
    session.close()