from datetime import datetime, date
from flask import Blueprint, render_template, redirect, url_for
from sqltest import db
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
    projs_num = str(len(projs) + 1)
    if form.validate_on_submit():
        mode = form.mode.data
        code = f"{mode.upper()}-{str(year)[2:]}-00-{projs_num.zfill(3)}"
        project = Project(
            key=code,
            title=form.title.data,
            abc=form.abc.data,
            mode=form.mode.data,
            cls=form.proj_class.data,
            status="On-going",
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
    proj = Project.query.filter(Project.key.contains(key)).first()
    lots = proj.lots_id
    form_lot = NewLot()
    if form_lot.validate_on_submit():
        lots = Lots(
            project_id=proj.id,
            lot_key=proj.key[:7] + str(len(proj.lots_id) + 1).zfill(2) + proj.key[9:],
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
        proj=proj,
        form_lot=form_lot,
        lots=lots,
    )
