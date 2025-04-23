from flask import Blueprint, render_template, current_app, url_for, g, flash, request
from werkzeug.utils import redirect

from app.db import db
from app.models import Question, User, Answer
from app.forms import QuestionForm, AnswerForm
from datetime import datetime

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list/')
def list_():
    current_app.logger.info('list_() 함수')
    questions = Question.query.order_by(Question.created_at.desc())

    return render_template('question/question_list.html', questions=questions)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)

    return render_template('question/question_detail.html', question=question)


@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()

    if request.method == 'POST' and form.validate_on_submit():
        # 글쓴이 데이터 확인 (g.user가 없으면 Anonymous로 설정)
        # 익명 사용자 처리
        anonymous_user = User.query.filter_by(username='anonymous').first()
        user = g.user if g.user else anonymous_user
        # user = g.user if g.user else anonymous_user

        question = Question(
            subject=form.subject.data,
            content=form.content.data,
            created_at=datetime.now(),
            user=user
        )
        db.session.add(question)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template('question/question_form.html', form=form)


@bp.route('/modify/<int:question_id>/', methods=('GET', 'POST'))
def modify(question_id):
    question = Question.query.get_or_404(question_id)

    if g.user != question.user:
        flash('수정권한이 없습니다')

        return redirect(url_for('question.detail', question_id=question_id))

    if request.method == 'POST':  # POST 요청
        form = QuestionForm()

        if form.validate_on_submit():
            form.populate_obj(question)
            question.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()

            return redirect(url_for('question.detail', question_id=question_id))
    else:  # GET 요청
        form = QuestionForm(obj=question)

    return render_template('question/question_form.html', form=form)


@bp.route('/delete/<int:question_id>/')
def delete(question_id):
    question = Question.query.get_or_404(question_id)

    if g.user != question.user:
        flash('삭제권한이 없습니다')

        return redirect(url_for('question.detail', question_id=question_id))

    db.session.delete(question)
    db.session.commit()

    return redirect(url_for('question.list_'))
