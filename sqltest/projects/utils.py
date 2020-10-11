from datetime import datetime, date
from sqltest.models import Project


def create_code(mode, year, projs):
    projs_num = len(projs) + 1

    if projs_num >= 100:
        projs_num_f = f"{projs_num}"
    elif projs_num >= 10:
        projs_num_f = f"0{projs_num}"
    else:
        projs_num_f = f"00{projs_num}"

    return f"{mode.upper()}-{str(year)[2:]}-00-{projs_num_f}"


def create_lot_code(key):
    proj = Project.query.filter_by(key=key).first()
    num_lots = len(proj.lots_id)
    li_key = key.split("-")
    li_key[2] = "0" + str(num_lots + 1)
    return "-".join(li_key)
