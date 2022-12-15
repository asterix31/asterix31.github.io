from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def homepage():
    return render_template("homepage.html")

@app.route("/products", methods=["POST"])
def products():
    return render_template("products.html")

@app.route("/tourisme", methods=["POST"])
def tourisme():
    return render_template("tourisme.html")

@app.route("/contacts", methods=["POST"])
def contacts():
    return render_template("contacts.html")