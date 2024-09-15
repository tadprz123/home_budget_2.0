import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import flash
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import routes, models
        db.create_all()
        import_data_from_csv()

    return app

def import_data_from_csv():
    from .utils import import_csv  # Import wewnątrz funkcji, aby uniknąć cyklicznego importu
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            file_path = os.path.join(data_dir, filename)
            with open(file_path, 'r') as file:
                import_csv(file)
