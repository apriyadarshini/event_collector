from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from EventCollector.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from EventCollector.geolocation.routes import geolocation
    from EventCollector.events.routes import events
    from EventCollector.errors.handlers import errors
    app.register_blueprint(geolocation)
    app.register_blueprint(events)
    app.register_blueprint(errors)
    
    return app