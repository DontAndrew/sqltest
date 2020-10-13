from datetime import datetime, date
from flask import Blueprint, render_template, redirect, url_for
from sqltest import db
from .utils import create_code, create_lot_code
from .forms import ProjectAdd, NewLot
from sqltest.models import Project, Contractor, Lots


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
        return redirect(url_for(".details", key=code))
    return render_template(
        "projects/projects.html",
        title="Projects",
        active_data="active",
        form=form,
        projs=projs,
    )


@projects.route("/projects/<key>", methods=["GET", "POST"])
def details(key):
    detail = Project.query.filter(Project.key.contains(key)).first()
    lots = detail.lots_id
    form_lot = NewLot()
    if form_lot.validate_on_submit():
        lots = Lots(
            project_id=detail.id,
            lot_key=create_lot_code(key),
            lot_title=form_lot.title.data,
            abc=form_lot.abc.data,
        )
        db.session.add(lots)
        db.session.commit()
        return redirect(url_for(".details", key=key))
    return render_template(
        "projects/details.html",
        title=key,
        active_data="active",
        detail=detail,
        form_lot=form_lot,
        lots=lots,
    )
