from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://eqdsjyhqltvodf:619892dab8d3e67b4669df36761c5870459322407e9ac8c79df6c243298b1d6c@ec2-54-235-169-191.compute-1.amazonaws.com:5432/d72cg2rtgrf6eb?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "human_data"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), unique = True)
    sex = db.Column(db.String(50))
    name = db.Column(db.String(50))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    age = db.Column(db.Integer)

    def __init__(self, email, sex, name, height, weight, age):
        self.email = email
        self.sex = sex
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        email = request.form['email_name']
        sex = request.form['sex_name']
        name = request.form['name_name']
        height = request.form['height_name']
        weight = request.form['weight_name']
        age = request.form['age_name']
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email, sex, name, height, weight, age)
            db.session.add(data)
            db.session.commit()
            #Obliczanie średniej -> func.avg ->oblicza średnią i daje wynik w postaci sql'owego SELECT'a, scalar()->robi z tego liczbę
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height, 1)
            average_weight = db.session.query(func.avg(Data.weight)).scalar()
            average_weight = round(average_weight, 1)
            average_age = db.session.query(func.avg(Data.age)).scalar()
            average_age = round(average_age, 1)
            count = db.session.query(Data.email).count()
            #Funkcja wyslij maila
            send_email(email, sex, name, height, weight, age, average_height, average_weight, average_age, count)
            return render_template("success.html")
    return render_template("index.html", text = "That mail address was already used!")


if __name__ == '__main__':
    app.debug = True
    app.run(port = 5025)
