from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields import TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Email

class UploadForm(FlaskForm):
    description= TextAreaField('description', validators=[DataRequired()])
    photo= FileField('photo', validators=[FileRequired(),FileAllowed(['jpg', 'jpeg', 'png'])])
    


