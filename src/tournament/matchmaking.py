import sys
sys.path.append('..')

from app import app

# endpoint /user/<id>/match
@app.get('/tournament/<id>/match')
def show_matchmaking(id=None):
    return id + "match"

@app.post('/tournament/<id>/match')
def update_score(id=None):
    return id

@app.put('/tournament/<id>/match')
def start_round(id=None):
    return id

@app.delete('/tournament/<id>/match')
def reset(id=None):
    return id