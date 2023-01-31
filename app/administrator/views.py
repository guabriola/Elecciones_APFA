from flask import Blueprint, render_template, redirect, url_for, session, flash
from models import *
from config import db
from .forms import AddList
from auth.views import has_role, login_required

#defino el blueprint
admin_bp = Blueprint("admin_bp", __name__,
                     template_folder="templates")


# Administrador - Carda de Lista
@admin_bp.route("/cargarLista", methods=["GET", "POST"])
@login_required
@has_role(["admin"])
def cargarLista():
    form = AddList()
    if form.validate_on_submit():
        newList = Listas(
            nro_lista=form.nro_lista.data,
            presidente=form.presidente.data,
            vice_presidente=form.vice_presidente.data
        )
        db.session.add(newList)
        db.session.commit()
        flash('La lista se cargó correctamente.')
    return render_template("new_list.html", form=form)
