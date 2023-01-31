from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from models import *


class AddList(FlaskForm):
    nro_lista = StringField("Numero de Lista", validators=[DataRequired()])
    presidente = StringField("Presidente", validators=[DataRequired()])
    vice_presidente = StringField("Vicepresidente", validators=[DataRequired()])
    submit = SubmitField("Ingresar")

    def __init__(self, *args, **kwargs):
        super(AddList, self).__init__(*args, **kwargs)

    def validate(self, *args):
        initial_validation = super(AddList, self).validate()
        if not initial_validation:
            return False

        Lista = Listas.query.filter_by(nro_lista=self.nro_lista.data).first()
        if Lista:
            self.nro_lista.errors.append("La lista ya existe")
            return False
        return True
