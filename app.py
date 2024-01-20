from flask import Flask, render_template, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)


class Todo(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    content= db.Column(db.Integer,default=0)
    date_created= db.Column(db.DateTime,default=datetime.utcnow)


    def __repr__(self) -> str:
        return '<Task %r>' % self.id


'''
/// --->Relative path 
////--->Absolute path


'''


@app.route('/')
def index():
    return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)