def test_user_model(client):
    user = User(username="testuser", password="hashedpassword")
    db.session.add(user)
    db.session.commit()

    queried_user = User.query.filter_by(username="testuser").first()
    assert queried_user is not None
    assert queried_user.username == "testuser"

def test_post_model(client):
    post = Post(title="Test Post", content="Test content", author="testuser")
    db.session.add(post)
    db.session.commit()

    queried_post = Post.query.filter_by(title="Test Post").first()
    assert queried_post is not None
    assert queried_post.content == "Test content"
