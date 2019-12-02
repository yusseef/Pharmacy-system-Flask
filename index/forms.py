from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, TextAreaField, SubmitField,PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Optional, ValidationError
from index.models import Medicine


class AddForm(FlaskForm):
    name = StringField('medicine name', validators=[DataRequired(), Length(min=3, max=50)])
    dose = StringField('medicine dose', validators=[DataRequired(), Length(min=2, max=50)])
    price = StringField('Price',validators=[DataRequired()])
    package = StringField('package', validators=[DataRequired(), Length(min=2, max=50)])
    company = StringField('company', validators=[Optional(), Length(min=5, max=50)])
    purpose = StringField('purpose', validators=[DataRequired(), Length(min=3, max=50)])
    description = TextAreaField('Description', validators=[Optional(), Length(min=0, max=100)])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        name = Medicine.query.filter_by(name=name.data).first()
        if name:
            raise ValidationError('this medicine already in the stock')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class SellForm(FlaskForm):
    medicine_name = SelectField(choices=[],validators=[DataRequired()])
    quantity = DecimalField('QT', places=2,rounding=None,validators=[DataRequired()])
    price = StringField('Price')
    submit = SubmitField('submit')

