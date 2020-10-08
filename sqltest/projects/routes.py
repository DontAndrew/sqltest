from datetime import datetime, date
from flask import Blueprint, render_template, redirect, request
from sqltest import db
from .utils import create_code
from .forms import ProjectAdd
from sqltest.models import Project, Contractor


projects = Blueprint("projects", __name__)


@projects.route("/projects", methods=["GET", "POST"])
def project_all():
    year = datetime.utcnow().year
    date_start = date(year=year, month=1, day=1)
    date_end = date(year=year, month=12, day=31)
    projs = (
        Project.query.filter(Project.date_created <= date_end)
        .filter(Project.date_created >= date_start)
        .all()
    )
    proj_num = len(projs)
    form = ProjectAdd()
    if form.validate_on_submit():
        mode = form.mode.data
        code = create_code(mode=mode, year=year, projs=projs)
        project = Project(
            key=code,
            title=form.title.data,
            abc=form.abc.data,
            mode=form.mode.data,
            cls=form.proj_class.data,
        )
        db.session.add(project)
        db.session.commit()
        return redirect("projects")
    return render_template(
        "projects/projects.html",
        title="Projects",
        active_data="active",
        form=form,
        projs=projs,
    )


# @projects.route("/project_add", methods=["GET", "POST"])
# def project_add():
#     form = ProjectAdd()
#     if form.validate_on_submit():
#         mode = form.mode.data
#         code = create_code(mode)
#         project = Project(
#             key=code,
#             title=form.title.data,
#             abc=form.abc.data,
#             mode=form.mode.data,
#             cls=form.proj_class.data,
#         )
#         db.session.add(project)
#         db.session.commit()
#         return redirect("projects")
#     return render_template(
#         "projects/form_add.html", title="New Project", active_data="active", form=form,
#     )
