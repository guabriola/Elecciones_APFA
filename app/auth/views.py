from flask import Blueprint, render_template,redirect,url_for,session
from functools import wraps
from models import *
from config import db
from .forms import SignupForm, LoginForm


# defino el blueprint
auth_bp = Blueprint('auth_bp', __name__,
    template_folder='templates')

#Requisito de Logeo
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("auth_bp.login"))
        return f(*args, **kwargs)
    return decorated_function

#Manejo de Roles
def has_role(roles=[]):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            username = session["username"]
            user = User.query.filter(User.username==username)
            lista_roles = []
            for aux in user[0].roles:
                lista_roles.append(aux.name)
            esta = False
            for r in roles:
                if r in lista_roles:
                    esta = True
            if not esta:
                return redirect(url_for("sinPermisos")) # no tiene permisos
            return f(*args, **kwargs)
        return decorated_function
    return decorator

#Login - es necesario que el Nro de Socio esté en el padron
@auth_bp.route('/login', methods=['GET','POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        if User.query.filter(User.username == form.username.data, User.password==form.password.data).first() != None:
            session['username'] = form.username.data
            return redirect(url_for('votos_bp.home'))
    return render_template ("login.html", form=form)

#LogOut
@auth_bp.route('/logout', methods=['GET','POST'])
def logout():
    session.pop("username")
    return redirect(url_for("home"))
    
#user = User.query.filter_by(username = username).first()
# register (form, necesita conf. de mail)
@auth_bp.route('/register', methods=['GET','POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
	# registro el nuevo usuario
		user = User(
		username=form.username.data,
		email = form.email.data,
		password = form.password.data,
		nro_socio = form.nro_socio.data	
	)
		rol = Role.query.filter(Role.name == "std").first()
		user.roles.append(rol)
		db.session.add(user)
		db.session.commit()
		# guardo el username en la sesión
		session["username"] = form.username.data
		# respuesta
		return redirect(url_for('auth_bp.login'))
    
	return render_template("register.html", form=form)