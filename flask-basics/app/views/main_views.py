from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html', title='홈 / flask-practice')


@bp.route('/<username>')
def index_for_user(username):
    return render_template('index.html', title='홈 / flask-practice', username=username)


@bp.route('/admin')
def index_for_admin():
    return render_template('index.html', title='홈 / flask-practice', username='admin')


@bp.route('/hello')
def hello():
    return 'Hello again!'


@bp.route('/star')
def star_info():
    return render_template('star.html', title='별찍기 / flask-practice')


@bp.route('/star/<int:N>')
def star(N):
    if N <= 0:
        return render_template('star.html', title='별찍기 / flask-practice', stars='자연수를 입력하세요.')

    last = ['*', '*_*', '*****']
    stars = []

    for i in range(N):
        if i == len(last):
            gap = len(last[-1])
            last.extend(last[j] + '_'*(gap - 2*j) + last[j]
                        for j in range(len(last)))
        spaces = '_' * (N - i - 1)
        stars.append(spaces + last[i] + spaces + '\n')

    return render_template('star.html', title='별찍기 / flask-practice', N=N, stars=stars)
