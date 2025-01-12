import pytest
from forum_app import app, db, User, Post

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  
        yield client


def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code == 302  

def test_register_route(client):
    response = client.get('/register')
    assert response.status_code == 200
    assert b"Register" in response.data

def test_login_route(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data

def test_create_post_redirect(client):
    response = client.get('/create')
    assert response.status_code == 302  
