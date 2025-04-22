from flask import Flask

from .database import *
from .views import main_views, auth_views, board_views, sql_views

app = Flask(__name__)

app.config.from_object(config)
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(main_views.bp)
app.register_blueprint(auth_views.bp)
app.register_blueprint(board_views.bp)
app.register_blueprint(sql_views.bp)
