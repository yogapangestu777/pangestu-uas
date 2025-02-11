from flask import Blueprint, render_template

main_routes = Blueprint('main', __name__)

@main_routes.route("/")
def homepage():
    return render_template("pages/client/homepage.html")

@main_routes.route("/about-me")
def about_me():
    return render_template("pages/client/about-me.html")