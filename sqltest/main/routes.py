from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/index")
def index():
    return render_template("index.html", title="My Web App", active_dashboard="active")


@main.route("/projects")
def projects():
    return render_template("projects.html", title="Projects", active_data="active")


@main.route("/projects/add")
def projects_add():
    return render_template("projects_add.html", title="Data", active_data="active")


@main.route("/about")
def about():
    return render_template("about.html", title="About", active_about="active")
