import sys
sys.path.append('..')

from app import app


# endpoint /tournament/<id>
@app.get('/tournament/<id>')
def show_tournament_data(id=None):
    return id

@app.post('/tournament/<id>')
def adjust_tournament_config(id=None):
    return id

@app.put('/tournament/<id>')
def add_participant(id=None):
    return id

@app.delete('/tournament/<id>')
def remove_participant(id=None):
    return id
