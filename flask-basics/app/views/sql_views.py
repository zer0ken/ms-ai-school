from datetime import datetime
from flask import Blueprint, abort

from app.db import db
from app.models import User, Question, Answer

bp = Blueprint('sql', __name__, url_prefix='/sql')


@bp.route('/user/create')
def create_user():
    user = User(
        username='test_user',
        password='test_password',
        email='test_user@example.com'
    )
    db.session.add(user)
    db.session.commit()

    return '사용자 정보가 생성되었습니다.'


@bp.route('/question/create')
def create_question():
    user = User.query.filter_by(username='test_user').first()
    if user is None:
        abort(404, '사용자 정보를 찾을 수 없습니다.')
    question = Question(
        subject='질문 제목',
        content='질문 내용',
        created_at=datetime.now(),
        user=user
    )
    db.session.add(question)
    db.session.commit()

    return '질문이 생성되었습니다.'


@bp.route('/question/read')
def read_questions():
    questions = Question.query.all()
    
    if not questions:
        return '질문이 없습니다.'
    
    results = ['<h1>질문 목록</h1>']
    for question in questions:
        results.append(f'질문 제목: {question.subject}, 질문 내용: {question.content}')
    return '<br>'.join(results)


@bp.route('/question/update')
def update_question():
    question = Question.query.get(1)
    if question is None:
        abort(404, '질문 정보를 찾을 수 없습니다.')
    
    question.subject = '수정된 질문 제목'
    question.content = '수정된 질문 내용'
    question.updated_at = datetime.now()
    
    db.session.commit()
    log.debug(f'Question updated: {question}')
    return '질문이 수정되었습니다.'


@bp.route('/question/delete')
def delete_question():
    question = Question.query.get(1)
    if question is None:
        abort(404, '질문 정보를 찾을 수 없습니다.')
    
    db.session.delete(question)
    db.session.commit()
    return '질문이 삭제되었습니다.'
