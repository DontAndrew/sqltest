from flask import Blueprint, render_template, send_file
from xlsxwriter import Workbook
from sqltest.models import Project

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/index")
def index():
    return render_template("index.html", title="My Web App", active_dashboard="active")


@main.route("/about")
def about():
    return render_template("about.html", title="About", active_about="active")


@main.route("/export_all", methods=["GET"])
def export_all():
    projs = Project.query.all()
    wb = Workbook("sqltest\static\exports\\all_proj.xlsx")
    ws = wb.add_worksheet("All Projects")

    ws.write(0, 0, "ID")
    ws.write(0, 1, "Unique Identifier")
    ws.write(0, 2, "Project Title")
    ws.write(0, 3, "Approved Budget")
    ws.write(0, 4, "Mode of Procurement")
    ws.write(0, 5, "Classification")
    ws.write(0, 6, "Status")

    for i, proj in enumerate(projs):
        ws.write(i + 1, 0, proj.id)
        ws.write(i + 1, 1, proj.key)
        ws.write(i + 1, 2, proj.title)
        ws.write(i + 1, 3, proj.abc)
        ws.write(i + 1, 4, proj.mode)
        ws.write(i + 1, 5, proj.cls)
        ws.write(i + 1, 6, proj.status)
    wb.close()

    return send_file(
        "static\exports\\all_proj.xlsx", as_attachment=True, cache_timeout=0
    )
