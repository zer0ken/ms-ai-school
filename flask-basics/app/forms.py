from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목을 입력하세요.')])
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력하세요.')])


class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력하세요.')])


class UserSignUpForm(FlaskForm):
    username = StringField(
        '사용자 이름',
        validators=[
            DataRequired('사용자 이름을 입력하세요.'),
            Length(min=3, max=25)
        ]
    )
    password1 = PasswordField(
        '비밀번호',
        validators=[
            DataRequired('비밀번호를 입력하세요.')
        ]
    )
    password2 = PasswordField(
        '비밀번호 확인',
        validators=[
            DataRequired('비밀번호를 입력하세요.'),
            EqualTo('password1', '비밀번호 확인이 비밀번호와 일치하지 않습니다.')
        ]
    )
    email = EmailField(
        '이메일',
        validators=[
            DataRequired('이메일을 입력하세요.'),
            Email('유효하지 않은 이메일 주소입니다.')
        ]
    )


class UserSignInForm(FlaskForm):
    username = StringField(
        '사용자 이름',
        validators=[
            DataRequired('사용자 이름을 입력하세요.'),
            Length(
                min=3,
                max=25,
                message='사용자 이름은 %(min)d ~ `%(max)d` 글자로 입력하세요.'
            )
        ]
    )
    password = PasswordField('비밀번호', validators=[DataRequired('비밀번호를 입력하세요.')])
