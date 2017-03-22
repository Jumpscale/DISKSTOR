
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of



class MakeReservationReqBody(Form):
    
    expirationEpoch = IntegerField(validators=[])
    reservationAdminSecret = TextField(validators=[])
    reservationId = TextField(validators=[])
    size = IntegerField(validators=[DataRequired(message="")])
