
from http import server
from lib2to3.pytree import Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib as url
from .config import Server,Database


# params=url.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + Server + ';DATABASE=' + Database + ';')
# engine=create_engine("mssql+pyodbc:///?odbc_connect=%s&trusted_connection=yes" % params)
print(Database+" and "+ Server)
engine=create_engine('mssql+pyodbc://' + Server + '/' + Database + '?trusted_connection=yes&driver=ODBC Driver 17 for SQL Server')

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()