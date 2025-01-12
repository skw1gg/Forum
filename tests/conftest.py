import pytest
from forum_app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # SQLite для тестов
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Создание таблиц перед каждым тестом
        yield client

        # Удаление всех данных после теста
        with app.app_context():
            db.session.remove()
            db.drop_all()
