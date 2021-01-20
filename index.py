from flask import Flask, render_template, url_for, redirect, request

from form import LoginForm, destination_form

from database import connection 

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HELLO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tourist.db'
db =    SQLAlchemy(app)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    img = db.Column(db.BLOB)

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    Contact = db.Column(db.String(2000))
    fb = db.Column(db.String(50))
    products = db.relationship('Product', backref='store')

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(2000))
    img = db.Column(db.BLOB)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(50))
    municipal = db.Column(db.String(20))
    description = db.Column(db.String(2000))
    address = db.Column(db.String(60))
    operation = db.Column(db.String(50))
    fb = db.Column(db.String(40))
    contact = db.Column(db.String(20))
    web = db.Column(db.String(50))
    map = db.Column(db.String(2048))
    highlights = db.Column(db.String(2048))
    direction = db.Column(db.String(5000))
    img = db.Column(db.BLOB)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/destination")
def destination():
    return render_template("destination.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/dashboard", methods=["POST", "GET"])
def dashboard():
    form = destination_form()
    if form.validate_on_submit():
        return f"the {form.name.data} address is {form.address.data}."
    return render_template("ins_dest.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)