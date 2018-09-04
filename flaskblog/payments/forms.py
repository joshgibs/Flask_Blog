from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Email, Length


class ChargeForm(FlaskForm):
    AccountNumber = StringField('Account Number', validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    amount = FloatField('Amount', validators=[DataRequired()])
    submit = SubmitField('Post')
