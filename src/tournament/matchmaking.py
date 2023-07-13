from flask import Blueprint

matchmaking = Blueprint('matchmaking', __name__)

# endpoint /user/<id>/match
@matchmaking.get('/tournament/<id>/match')
def show_matchmaking(id=None):
    return id + "match"

@matchmaking.post('/tournament/<id>/match')
def update_score(id=None):
    return id

@matchmaking.put('/tournament/<id>/match')
def start_round(id=None):
    return id

@matchmaking.delete('/tournament/<id>/match')
def reset(id=None):
    return id