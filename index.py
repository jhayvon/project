from flask import Flask, render_template, url_for, redirect

from form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HELLO'

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

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return f"the username is {form.username.data} and the password is {form.password.data}."
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)