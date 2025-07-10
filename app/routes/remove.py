from flask import Blueprint, render_template
from flags import FLAGS

bp = Blueprint("remove", __name__)

@bp.route("/")
def remove():
    flag = FLAGS.get("credential_injected")
    return render_template("flag.html", flag=flag)
