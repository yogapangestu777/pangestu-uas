from flask import Blueprint
from app.controllers.client.homepage_controller import home, about 

main_routes = Blueprint('main', __name__)

@main_routes.route("/")
def homepage():
    return home()

@main_routes.route("/about")
def about_page():
    return about()