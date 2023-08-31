from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from models import Students

def custom_email_checker(form, field):
    if Students.query.filter(Students.email==field.data).first() is not None:
        raise ValidationError("Email already taken!")       
    
def custom_email_validator(form, field):
    if field.data.endswith("mail.ru"):
        raise ValidationError("This mail is in blacklist!") 

class RegisterForm(FlaskForm):  
    name = StringField("Adinizi qeyd edin", validators=[DataRequired(), 
                                            Length(2, 30, message="Length is small")])
    surname = StringField("Soyadinizi qeyd edin", validators=[DataRequired()])
    gender = StringField("Cinsinizi qeyd edin", validators=[DataRequired()])
    image = StringField("Sekil")
    status = StringField("Status")
    bio = StringField("Haqqinizda")
    password = PasswordField("Sifre", validators=[DataRequired()])
    confirm_password = PasswordField("Sifrenin tekrari", validators=[DataRequired(),
                                                         EqualTo("password", message="Passwords not same")])
    email = EmailField("Email", validators=[DataRequired(), custom_email_checker, custom_email_validator])

    submit = SubmitField("Gonder")
