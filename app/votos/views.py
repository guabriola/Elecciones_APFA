from flask import Blueprint, render_template,redirect,url_for,session
from models import *
from config import db
from .forms import VotoForm
from sqlalchemy import func
from auth.views import has_role, login_required

# defino el blueprint
votos_bp = Blueprint('votos_bp', __name__,
    template_folder='templates')


#Votar
@votos_bp.route('/votar', methods=['GET','POST'])
@login_required
@has_role([ "std", "admin"])
def vote():

    username = session['username']
    user = User.query.filter_by(username = username).first()
    if user.ya_voto == 'si':
        return redirect(url_for('votos_bp.ya_voto'))

    form= VotoForm()
    if form.validate_on_submit():
        voto = Votos(
            lista_id = form.lista_id.data
        )
        db.session.add(voto)
        user = User.query.filter_by(username = username).first()
        user.ya_voto = 'si'
        db.session.add(user)


        db.session.commit()


        # redirect resultados
        return redirect(url_for('votos_bp.resultado'))
    return render_template ("vote.html", form=form)
   # return '<h1>Ingrese su voto</h1>'

# Ver Votos
@votos_bp.route('/resultado', methods=['GET','POST'])
def resultado():
    print("El total de votos: ")
    print(Votos.query.count())

    votosXlista = Votos.query.with_entities(Votos.lista_id, func.count(Votos.lista_id)).group_by(Votos.lista_id).all()
    print(votosXlista)
    return render_template ("cantidad_votos.html")


# Ya votó
@votos_bp.route('/ya_voto', methods=['GET','POST'])
def ya_voto():
    return render_template ("ya_voto.html")