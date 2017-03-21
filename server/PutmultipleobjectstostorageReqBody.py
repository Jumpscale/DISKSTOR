
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of

from Payload import Payload


class PutmultipleobjectstostorageReqBody(Form):
    
    consumers = FieldList(TextField('consumers', [required()]), )
    dataSecret = TextField(validators=[])
    payload = FieldList(FormField(Payload))
    requesterUID = TextField(validators=[DataRequired(message="")])
