from flask import Flask
from logging.handlers import RotatingFileHandler

from . import config
from .db import db, migrate
from .views import main_views, star_views, auth_views, question_views, answer_views


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_views.bp)
    app.register_blueprint(star_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    # if not os.path.exists('logs'):
    #     os.makedirs('logs')

    # log_level = logging.DEBUG if app.debug else logging.INFO

    # file_handler = RotatingFileHandler(
    #     'logs/flask.log',
    #     maxBytes=1024 * 1024 * 10,
    #     backupCount=10,
    #     encoding='utf-8'
    # )
    # file_handler.setLevel(log_level)
    # file_handler.setFormatter(logging.Formatter(
    #     '%(asctime)s - %(levelname)s - %(message)s'))

    # app.logger.setLevel(log_level)
    # app.logger.addHandler(file_handler)

    return app
