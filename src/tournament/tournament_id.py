from flask import Blueprint

tournament_data = Blueprint('tournament_data', __name__)


# endpoint /tournament/<id>
@tournament_data.get('/tournament/<id>')
def show_tournament_data(id=None):
    return id

@tournament_data.post('/tournament/<id>')
def adjust_tournament_config(id=None):
    return id

@tournament_data.put('/tournament/<id>')
def add_participant(id=None):
    return id

@tournament_data.delete('/tournament/<id>')
def remove_participant(id=None):
    return id
