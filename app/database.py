from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
from urllib.parse import quote_plus

# Encode the password so special characters like '@' are safely handled in the URL
password = quote_plus(settings.database_password)
print("ho")
print("ho")
print("ho")
print("ho")
print("ho")
print("ho")
print(password)
print(settings.database_password)

SQL_DATABASE_URL = f"postgresql+psycopg2://{settings.database_username}:{password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
print(SQL_DATABASE_URL)
# SQL_DATABASE_URL = f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"


engine = create_engine(SQL_DATABASE_URL)

engine = create_engine(SQL_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="fastapi",
#             user="postgres",
#             password="Postgre@#123",
#             cursor_factory=RealDictCursor,
#         )
#         cursor = conn.cursor()
#         print("database connection was succesdull")
#         break

#     except Exception as error:
#         print(error)
#         time.sleep(2)
