from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret"
    db.init_app(app)
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app


