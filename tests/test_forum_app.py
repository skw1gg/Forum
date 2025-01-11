import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from forum_app import app, db, User, Post


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        db.session.remove()
        db.drop_all()

def test_register(client):
    response = client.post('/register', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    assert b'login' in response.data  

def test_login(client):
    
    user = User(username='testuser', password='hashedpassword')
    db.session.add(user)
    db.session.commit()

    
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'hashedpassword'  
    })
    assert response.status_code == 200
    assert b'Invalid username or password!' not in response.data

def test_create_post(client):
    client.post('/register', data={'username': 'author', 'password': 'password123'})
    client.post('/login', data={'username': 'author', 'password': 'password123'})
    response = client.post('/create', data={'title': 'Test Post', 'content': 'Test Content'}, follow_redirects=True)
    assert b'Test Post' in response.data
