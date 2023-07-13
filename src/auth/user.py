from flask import Blueprint, jsonify, request

user_data = Blueprint('user_data', __name__)

# endpoint /user/<id>
@user_data.get('/user/<id>')
def user_info(id=None):
    return id

@user_data.post('/user/<id>')
def update_user_info(id=None):
    return id

@user_data.delete('/user/<id>')
def delete_user(id=None):
    return id