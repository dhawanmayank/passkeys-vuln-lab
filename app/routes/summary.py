from flask import Blueprint, render_template
from flags import FLAGS

bp = Blueprint("summary", __name__)

@bp.route("/flags")
def flag_summary():
    return render_template("flag_summary.html", flags=FLAGS)
