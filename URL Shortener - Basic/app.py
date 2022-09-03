from flask import Flask,render_template,request
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pyshorteners

user_url, shorter="", ""

app=Flask(__name__)
basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
Migrate(app,db)

class sabji(db.Model):
    __tablename__='url_short'
    id=db.Column(db.Integer, primary_key=True)
    user_url=db.Column(db.String(200))
    shorter=db.Column(db.String(200))
    def __init__(self,user_url,shorter):
        self.user_url=user_url
        self.shorter=shorter


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/',methods=["GET","POST"])
def home_page():
    global user_url,shorter
    if request.method=="POST":
        user_url=request.form.get("in_1")
        url_short = pyshorteners.Shortener()
        shorter = url_short.tinyurl.short(user_url)
        new_URL=sabji(user_url,shorter)
        db.session.add(new_URL)
        db.session.commit()

    return render_template("home.html", shorter=shorter)

@app.route('/DataBase')
def db_page():
    url_shorter=sabji.query.all()
    return render_template("display.html",url_shorter=url_shorter)


if __name__=='__main__':
    app.run(debug=True)