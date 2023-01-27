from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from models import *

class SignupForm(FlaskForm):
    nro_socio = StringField('nro_socio', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('Nombre', validators=[DataRequired()])
    last_name = StringField('Apellido', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email') #, validators=[DataRequired(), Email()]
    submit = SubmitField('Registrar')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
    
    def validate(self, *args):
        initial_validation = super(SignupForm, self).validate()
        if not initial_validation:
            return False
        
        padron = Padron.query.filter_by(nro_socio = self.nro_socio.data).first()
        if not padron:
            self.nro_socio.errors.append('El nro de socio no está en el padron')
            return False
        return True
       
class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    def validate(self, *args):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        user = User.query.filter_by(username = self.username.data).first()
        if not user:
            self.username.errors.append('Usuario no existe')
            return False
        if not User.query.filter_by(password = self.password.data).first():
            self.password.errors.append('Invalid password')
            return False
        return True
	