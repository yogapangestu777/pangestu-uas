from flask import render_template

def home():
    return render_template("pages/client/homepage.html")

def about():
    return render_template("pages/client/about.html")
