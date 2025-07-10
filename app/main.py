from flask import Flask, render_template
from app.routes import register, login, fallback, phish, register_real, remove, summary
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "super-insecure-dev-key")

app.register_blueprint(register.bp, url_prefix="/register")
app.register_blueprint(login.bp, url_prefix="/login")
app.register_blueprint(fallback.bp, url_prefix="/fallback")
app.register_blueprint(phish.bp, url_prefix="/phish")
app.register_blueprint(register_real.bp, url_prefix="/register_real")
app.register_blueprint(remove.bp, url_prefix="/remove_key")
app.register_blueprint(summary.bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
