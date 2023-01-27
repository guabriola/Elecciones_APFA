from config import *
from models import *
from auth.views import auth_bp
from votos.views import votos_bp
from administrator.views import admin_bp
from flask import render_template


app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(votos_bp, url_prefix="/votos")
app.register_blueprint(admin_bp, url_prefix="/administrator")

# home
@app.route("/", methods=["GET"])
def home():
    return render_template ("home.html")

# error_sin_permisos
@app.route("/sinPermisos", methods=["GET"])
def sinPermisos():
    return render_template ("sin_permisos.html")

