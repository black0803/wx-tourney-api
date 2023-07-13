from flask import Blueprint

tournaments = Blueprint('tournaments', __name__)


# endpoint /tournament
@tournaments.get('/tournament')
def show_tournaments():
    return "success"

@tournaments.put('/tournament')
def create_new_tournament():
    return "success"

@tournaments.delete('/tournament')
def delete_tournament():
    return "success"



