from flask import Blueprint, render_template

bp = Blueprint("register_real", __name__)

@bp.route("/")
def register_real():
    return render_template("register_real.html")
