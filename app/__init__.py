from flask import Flask
from app.routes import main
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Config
    app.config.from_object('instance.config')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

    db.init_app(app)
    CORS(app)
    app.register_blueprint(main)

    return app
