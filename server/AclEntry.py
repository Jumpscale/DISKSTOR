
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of



class AclEntry(Form):
    
    acl = TextField(validators=[DataRequired(message="")])
    dataSecret = TextField(validators=[DataRequired(message="")])
