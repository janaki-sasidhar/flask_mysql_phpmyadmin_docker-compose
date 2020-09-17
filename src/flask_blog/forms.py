from flask_wtf import FlaskForm
from wtforms import StringField ,  SubmitField
from wtforms.validators import DataRequired

class ProfileForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    country = StringField('country',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired()])
    hobbies = StringField('hobbies')
    submit = SubmitField('Update')
