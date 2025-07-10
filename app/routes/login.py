from flask import Blueprint, render_template
from flags import FLAGS

bp = Blueprint("login", __name__)

@bp.route("/")
def login():
    flag = FLAGS.get("no_biometric_verification")
    return render_template("flag.html", flag=flag)
