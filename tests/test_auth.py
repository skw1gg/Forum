def test_user_registration(client):
    # Проверяем регистрацию нового пользователя
    response = client.post('/register', data={
        'username': 'newuser',
        'password': 'newpassword'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data


def test_user_login(client):
    # Регистрируем пользователя для логина
    client.post('/register', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)

    # Проверяем логин
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Welcome" in response.data
