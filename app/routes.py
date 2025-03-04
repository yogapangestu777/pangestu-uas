from flask import Blueprint, render_template

main_routes = Blueprint('main', __name__)

@main_routes.route("/")
def homepage():
    return render_template("pages/client/homepage.html")

@main_routes.route("/about-me")
def about_me():
    return render_template("pages/client/about-me.html")

@main_routes.route("/projects")
def project():
    return render_template("pages/client/project.html")

@main_routes.route("/blogs")
def blog():
    return render_template("pages/client/blog.html")

@main_routes.route("/contact-me")
def contact_me():
    return render_template("pages/client/contact-me.html")