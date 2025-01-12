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

        
        with app.app_context():
            db.session.remove()
            db.drop_all()

def test_user_model(client):
    with app.app_context():  
        user = User(username="testuser", password="hashedpassword")
        db.session.add(user)
        db.session.commit()

        queried_user = User.query.filter_by(username="testuser").first()
        assert queried_user is not None
        assert queried_user.username == "testuser"

def test_post_model(client):
    with app.app_context():  
        post = Post(title="Test Post", content="Test content", author="testuser")
        db.session.add(post)
        db.session.commit()

        queried_post = Post.query.filter_by(title="Test Post").first()
        assert queried_post is not None
        assert queried_post.content == "Test content"
