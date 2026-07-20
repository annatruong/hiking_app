from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange 

class HikeForm(FlaskForm):
    ascent = IntegerField("Ascent (m):", validators=[DataRequired(), NumberRange(min=0)])
    distance = IntegerField("Distance (km):",validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField("Calculate")
