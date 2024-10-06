# config.py
import os
from flask import Flask
from extensions import db, migrate
from routes import routes_bp
from dotenv import load_dotenv

load_dotenv()  # Lädt die .env-Datei

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///database.db')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

    # Initialisieren der Erweiterungen
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrieren des Blueprints
    app.register_blueprint(routes_bp, url_prefix='/')

    return app
