from flask import Flask
from sqltest.config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # import blueprints
    from sqltest.main.routes import main
    from sqltest.projects.routes import projects

    # register the blueprints
    app.register_blueprint(main)
    app.register_blueprint(projects)

    return app
