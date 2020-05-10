import datetime
import sqlalchemy
from flask import Flask
from data.db_session import SqlAlchemyBase

app = Flask(__name__)
app.config["SECRET_KEY"] = 'z_k.,k._gbwwe'

class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.16')