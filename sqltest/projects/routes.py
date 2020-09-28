from flask import Blueprint, render_template, redirect, request
from sqltest import db
from sqltest.projects.forms import ProjectAdd
from sqltest.models import Project, Contractor


projects = Blueprint("projects", __name__)


@projects.route("/projects")
def project_all():
    return render_template(
        "projects/projects.html", title="Projects", active_data="active"
    )


@projects.route("/project_add", methods=["GET", "POST"])
def project_add():
    form = ProjectAdd()
    if form.validate_on_submit():

        mode = form.mode.data
        print(f"{mode}")
        return redirect("projects")
    return render_template(
        "projects/form_add.html", title="New Project", active_data="active", form=form,
    )
