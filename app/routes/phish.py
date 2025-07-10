from flask import Blueprint, render_template
from flags import FLAGS

bp = Blueprint("phish", __name__)

@bp.route("/")
def phish():
    flag = FLAGS.get("csrf_token_missing")
    return render_template("flag.html", flag=flag)
