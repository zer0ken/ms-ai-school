import logging
from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from app.db import db
from app.forms import UserSignUpForm, UserSignInForm
from app.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth/')
log = logging.getLogger(__name__)


@bp.route('sign-up/', methods=('GET', 'POST'))
def sign_up():
    form = UserSignUpForm()
    log.debug('signup함수 호출')

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if not user:
            user = User(
                username=form.username.data,
                password=generate_password_hash(form.password1.data),
                email=form.email.data
            )
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('main.index'))
        else:
            flash('이미 사용 중인 사용자 이름입니다.')

    return render_template('auth/sign_up.html', form=form)


@bp.route('/sign-in/', methods=('GET', 'POST'))
def sign_in():
    form = UserSignInForm()

    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()

        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."

        if error is None:
            session.clear()
            session['user_id'] = user.id

            return redirect(url_for('main.index'))

        flash(error)

    return render_template('auth/sign_in.html', form=form)


@bp.before_app_request
def load_logged_in_user():
    # 정적 파일 요청 무시
    if request.endpoint and 'static' in request.endpoint:
        return

    # 익명 사용자 확인 및 추가
    # 추후 로그인된 사용자만 글을 쓸수 있도록 수정할것
    anonymous_user = User.query.filter_by(username='anonymous').first()

    if not anonymous_user:
        anonymous_user = User(
            username='anonymous',
            password=generate_password_hash('anonymous'),
            email='anonymous@example.com'
        )
        db.session.add(anonymous_user)
        db.session.commit()

    # 세션에서 로그인된 사용자 정보 로드
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/sign-out/')
def sign_out():
    session.clear()
    return redirect(url_for('main.index'))
