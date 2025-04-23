from flask import Blueprint, render_template, request, redirect, url_for, g, flash
from datetime import datetime
from app.forms import AnswerForm
from app.db import db
from app.models import Question, User, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer/')


@bp.route('/create/<int:question_id>', methods=['POST'])
def create(question_id):
    question = Question.query.get_or_404(question_id)
    content = request.form['content']

    user = g.user if g.user else User.query.filter_by(
        username='anonymous').first()

    answer = Answer(
        content=content,
        created_at=datetime.now(),
        user=user
    )
    question.answers.append(answer)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question.id))


@bp.route('/update/<int:answer_id>', methods=['GET', 'POST'])
def update(answer_id):
    answer = Answer.query.get_or_404(answer_id)

    if g.user.username == 'anonymous' or g.user != answer.user:
        flash('수정 권한이 없습니다.')
        return redirect(url_for('question.detail', question_id=answer.question.id))

    if request.method == 'GET':
        form = AnswerForm(obj=answer)
    else:
        form = AnswerForm()

        if form.validate_on_submit():
            content = form.content.data
            answer.content = content
            db.session.commit()

            return redirect(url_for('question.detail', question_id=answer.question.id))

    return render_template('update_answer_form.html', answer=answer, form=form)


@bp.route('/delete/<int:answer_id>', methods=['POST'])
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    question = answer.question
    if g.user.username == 'anonymous' or g.user != answer.user:
        flash('삭제 권한이 없습니다.')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question.id))
