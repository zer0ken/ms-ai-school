from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/login')


@bp.route('/')
def login():
    return '아이디와 비밀번호로 로그인'


@bp.route('/<username>')
def login_with_username(username):
    return f'아이디 {username}로 로그인'
