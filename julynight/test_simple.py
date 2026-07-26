import services
from fastapi import FastAPI
import pytest

from main import app
from fastapi.testclient import TestClient

@pytest.fixture(autouse=True)
def before_everything():
    services.fake_users.clear()
    
    services.fake_users.extend([
    {'id': 1, 'name': 'Alice', 'email': 'alice@test.com', 'role': 'admin'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@test.com', 'role': 'user'},
    {'id': 3, 'name': 'Carol', 'email': 'carol@test.com', 'role': 'user'},
])


client=TestClient(app)
test_put_user_dic={'id': 1, 'name': 'library', 'role': 'admin'}
test_post_user_dic={'name':'mugen','id':5,'role':'user','email':'musashino@gmail.com'}

def test_get_user():
    response=client.get('/all_data?id=1')
    assert response.json() == {'id': 1, 'name': 'Alice', 'email': 'alice@test.com', 'role': 'admin'}


def test_put_user():#the FastAPI TestClient allows you to pass
# a clean Python dictionary using the params keyword. This handles all URL formatting safely behind the scenes.
    response=client.put('/update_user?',params=test_put_user_dic)
    assert response.json()=={'id': 1, 'name': 'library', 'email': 'alice@test.com', 'role': 'admin'}

def test_post_user():
    response=client.post('/add_user',params=test_post_user_dic)
    assert response.json()=={'name':'mugen','id':5,'role':'user','email':'musashino@gmail.com'}



def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0






