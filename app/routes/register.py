from flask import Blueprint, render_template
from flags import FLAGS

bp = Blueprint("register", __name__)

@bp.route("/")
def register():
    flag = FLAGS.get("attestation_not_verified")
    return render_template("flag.html", flag=flag)
