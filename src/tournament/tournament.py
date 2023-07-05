import sys
sys.path.append('..')

from app import app


# endpoint /tournament
@app.get('/tournament')
def show_tournaments():
    return "success"

@app.post('/tournament')
def change_tournament(): #belum kepikiran apa yg diganti
    return "success"

@app.put('/tournament')
def create_new_tournament():
    return "success"

@app.delete('/tournament')
def delete_tournament():
    return "success"



