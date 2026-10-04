import sqlalchemy
from sqlalchemy import URL
from sqlalchemy import create_engine
url_object = URL.create(
    "postgresql",
    username="postgres",
    password="Data",
    host="localhost",
    database="postgres",
)

engine = create_engine(url_object)
