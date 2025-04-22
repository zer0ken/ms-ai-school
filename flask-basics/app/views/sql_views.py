from flask import Blueprint

from app.database import db
from app.database import User, Question, Answer

bp = Blueprint('sql', __name__, url_prefix='/sql')


@bp.route('/create-user')
def create_user():
    user = User(
        username='test_user',
        password='test_password',
        email='test_user@example.com'
    )
    db.session.add(user)
    db.session.commit()
    return '사용자 정보가 생성되었습니다.'
