from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


#/src/auth blueprint modules
from auth.session import user_session
from auth.user import user_data
from auth.deck import user_deck

#/src/tournament blueprint modules
from tournament.tournament import tournaments
from tournament.tournament_id import tournament_data
from tournament.matchmaking import matchmaking

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # Setup the Flask-JWT-Extended extension
    app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
    jwt = JWTManager(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/wx_db'
    db.init_app(app)
    
    app.register_blueprint(user_session)
    app.register_blueprint(user_deck)
    app.register_blueprint(user_data)
    app.register_blueprint(tournaments)
    app.register_blueprint(tournament_data)
    app.register_blueprint(matchmaking)

    return app