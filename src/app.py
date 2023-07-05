from datetime import timedelta
from flask import Flask, Request, jsonify

from flask_jwt_extended import JWTManager

app = Flask(__name__)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)


from auth import session, user, deck
from tournament import tournament, matchmaking, tournament_id

if __name__ == '__main__':
    print("running flask")
    app.run()   