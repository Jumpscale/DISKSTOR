
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of



class Payload(Form):
    
    data = FileField(validators=[DataRequired(message=""), Length(max=1048576)])
    key = TextField(validators=[DataRequired(message="")])
