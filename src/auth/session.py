import sys
sys.path.append('..')

from app import app, jwt
from flask import jsonify, request


from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt


# endpoint /user
@app.get('/user')
@jwt_required()
def current_user():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.post('/user')
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # check user & pass from DB
    # ------------------ insert code here ------------------

    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    # ------------------- code ends here -------------------

    access_token = create_access_token(identity=username, fresh=True)
    refresh_token = create_refresh_token(identity=username)

    # store token to DB for TTL
    # ------------------ insert code here ------------------

    # ------------------- code ends here -------------------

    return jsonify(access_token=access_token, refresh_token=refresh_token)

@app.put('/user') # create user
def create_new_user():
    return "success"

@app.delete('/user') # logout
def logout():
    return "success"

@app.post('/refresh') # endpoint to refresh incase needed
@jwt_required(refresh=True)
def refresh_token():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity, fresh=False)
    return jsonify(access_token=access_token)

@app.get('/debug-jwt')
@jwt_required(verify_type=False)
def debug_jwt():
    return get_jwt()
