from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_STORAGE = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_STORAGE}'
    db.init_app(app)

    #-----------------------------
    # 'views' is a varaibel name
    #-----------------------------
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    #----------------------------
    # 'Expense' is a class name
    #----------------------------
    from .models import Expense
    with app.app_context():
        db.create_all()
    return app