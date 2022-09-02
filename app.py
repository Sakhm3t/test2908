from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB

import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://flaskproject:flask_project@localhost/test2908db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Data(db.Model):
    __tablename__ = 'Data'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(JSONB)

    def __repr__(self):
        return f"{self.data}"


@app.route('/added', methods=['post'])
def add_data():
    try:
        d = Data(data=request.form['json'])
        db.session.add(d)
        db.session.flush()
        db.session.commit()
    except:
        db.session.rollback()
        print("Mistake ")
    return render_template('data_was_added.html', title='Success')


@app.route('/')
def index():
    return render_template('dynamicforms.html', title='Main page')


@app.route('/input')
def dynamic_forms():
    return render_template("dynamicforms.html", title='Input data')


class DataItem:
    def __init__(self, items):
        self.__dict__.update(items)


@app.route('/output')
def output_data():
    items = [DataItem(json.loads(item.data)) for item in Data.query.all()]
    return render_template("datalist.html", title='Output data', data_list=items)


if __name__ == "__main__":
    app.run(debug=True)