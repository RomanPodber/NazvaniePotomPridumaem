import datetime
import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase
from data import db_session
from flask import render_template, redirect, Flask

app = Flask(__name__)


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')
    news = orm.relation("News", back_populates='user')

@app.route("/")
def index():
    session = db_session.create_session()
    news = session.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.16')