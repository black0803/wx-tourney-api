import sys
sys.path.append('..')

from app import app

# endpoint /user/<id>/deck
@app.get('/user/<id>/deck')
def list_user_deck(id=None):
    return id + "deck"

@app.post('/user/<id>/deck')
def update_user_deck(id=None):
    return id

@app.put('/user/<id>/deck')
def create_user_deck(id=None):
    return id

@app.delete('/user/<id>/deck')
def delete_deck(id=None):
    return id