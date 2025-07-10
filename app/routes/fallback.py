from flask import Blueprint, render_template
from flags import FLAGS

bp = Blueprint("fallback", __name__)

@bp.route("/")
def fallback():
    flag = FLAGS.get("mfa_downgrade_success")
    return render_template("flag.html", flag=flag)
