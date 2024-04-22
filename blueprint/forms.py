import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired
from models import UserModel, EmailVerifyModel

from exts import db


# validate front-end data
class RegisForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Please check your E-mail Format")])
    captcha = wtforms.StringField(validators=[Length(min=6, max=6, message="Captcha should be 6 digits")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="Please check your username")])
    password = wtforms.StringField(
        validators=[Length(min=6, max=20, message="Wrong Password Format (6-20 characters)")])
    confirm_password = wtforms.StringField(validators=[EqualTo("password", message="Unmatched password")])

# check captcha/ repeated E-mail address

    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        verify = EmailVerifyModel.query.filter_by(email=email, captcha=captcha).first()
        if not verify:
            raise wtforms.ValidationError(message="Wrong E-mail/Captcha")
        # For deletion
        # else:
        #     db.session.delete(verify)
        #     db.session.commit()

    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="registed E-mail address")


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="Please check your E-mail Format")])
    password = wtforms.StringField(
        validators=[Length(min=6, max=20, message="Wrong Password Format (6-20 characters)")])


class PostsForm(wtforms.Form):
    title = wtforms.StringField(validators=[Length(min=3, max=100, message="Wrong Title Format")])
    content = wtforms.StringField(validators=[Length(min=3, message="Your Content should have more than 3 words")])


class ReplyForm(wtforms.Form):
    content = wtforms.StringField(validators=[Length(min=3, message="Your Content should have more than 3 words")])
    post_id = wtforms.IntegerField(validators=[InputRequired(message="Must have post id")])
