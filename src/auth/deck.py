from flask import Blueprint

user_deck = Blueprint('user_deck', __name__)

# endpoint /user/<id>/deck
@user_deck.get('/user/<id>/deck')
def list_user_deck(id=None):
    return id + "deck"

@user_deck.post('/user/<id>/deck')
def update_user_deck(id=None):
    return id

@user_deck.put('/user/<id>/deck')
def create_user_deck(id=None):
    return id

@user_deck.delete('/user/<id>/deck')
def delete_deck(id=None):
    return id