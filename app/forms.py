from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

aanhef_choices = [("meneer", "meneer"), ("mevrouw", "mevrouw")]

class AddNotaForm(FlaskForm):
    aanhef = SelectField('aanhef', choices=aanhef_choices, validators=[DataRequired()])
    naam = StringField('naam', validators=[DataRequired()])
    contributie = StringField('contributie', validators=[DataRequired()])
    pacht = StringField('pacht', validators=[DataRequired()])
    nr_tuinen = StringField('nr_tuinen', validators=[DataRequired()])
    borg = StringField('borg', validators=[DataRequired()])
    ploegen = StringField('ploegen', validators=[DataRequired()])
    roteren = StringField('roteren', validators=[DataRequired()])
    overig = StringField('overig', validators=[DataRequired()])
    submit = SubmitField('Okay')