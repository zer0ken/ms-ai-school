from flask import Flask
from .views import main_views, auth_views, board_views

app = Flask(__name__)


app.register_blueprint(main_views.bp)
app.register_blueprint(auth_views.bp)
app.register_blueprint(board_views.bp)
