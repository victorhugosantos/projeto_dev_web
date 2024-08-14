from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class VolunteerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone')
    availability = StringField('Availability')
    submit = SubmitField('Register Volunteer')

class DonationForm(FlaskForm):
    item_name = StringField('Item Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    expiration_date = DateField('Expiration Date', validators=[DataRequired()])
    submit = SubmitField('Register Donation')

class DistributionForm(FlaskForm):
    recipient_name = StringField('Recipient Name', validators=[DataRequired()])
    item_name = StringField('Item Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    distribution_date = DateField('Distribution Date', validators=[DataRequired()])
    submit = SubmitField('Register Distribution')
