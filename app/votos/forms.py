from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SelectField, SubmitField
from models import Listas


class VotoForm(FlaskForm):
    lista_id = SelectField()
    submit = SubmitField("Ingresar")

    def __init__(self):
        super(VotoForm, self).__init__()
        self.lista_id.choices = [(c.id, c.nro_lista) for c in Listas.query.all()]
