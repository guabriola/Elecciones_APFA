from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AddList(FlaskForm):
    nro_lista = StringField('Numero de Lista')
    presidente = StringField('Presidente')
    vice_presidente = StringField('Vicepresidente')
    submit = SubmitField('Ingresar')
