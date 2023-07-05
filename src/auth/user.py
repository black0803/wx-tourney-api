import sys
sys.path.append('..')

from app import app

# endpoint /user/<id>
@app.get('/user/<id>')
def user_info(id=None):
    return id

@app.post('/user/<id>')
def update_user_info(id=None):
    return id

@app.delete('/user/<id>')
def delete_user(id=None):
    return id