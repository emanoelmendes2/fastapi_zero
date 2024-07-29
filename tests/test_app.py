from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World"}


def test_read_html_deve_retornar_ok_e_html(client):
    response = client.get("/html")
    assert response.status_code == HTTPStatus.OK
    assert "Olá Mundo" in response.text


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "teste",
            "email": "teste@gmail.com",
            "password": "teste",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "username": "teste",
        "email": "teste@gmail.com",
    }


def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [{"id": 1, "username": "teste", "email": "teste@gmail.com"}]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "password": "teste2",
            "username": "teste2",
            "email": "teste@gmail.com",
            "id": 1,
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "teste2",
        "email": "teste@gmail.com",
    }


def test_wread_users_one(client):
    response = client.get("/users_one/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "teste2",
        "email": "teste@gmail.com",
    }


def test_read_users_not_found(client):
    response = client.get("/users_one/2")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted successfully"}
