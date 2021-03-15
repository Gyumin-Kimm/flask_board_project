from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')  # 이름, 모듈명, URL prefix


@bp.route('/hello')  # 주소에 접속하면 아래 함수 호출
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))

    # question_list = Question.query.order_by(Question.create_date.desc())
    # return render_template('question/question_list.html', question_list=question_list)

    # return 'Pybo index'
