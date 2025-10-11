import requests

BASE_URL = "https://reqres.in/api/users"
HEADERS = {"x-api-key": "reqres-free-v1"}

def test_get_users():
    response = requests.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200

    data = response.json()
    assert "total" in data


def test_create_user():
    response = requests.post(f"{BASE_URL}/register", headers=HEADERS)
    assert response.status_code == 201

    data = response.json()
    assert "id" in data


def test_update_user():
    response = requests.put(f"{BASE_URL}/1", headers=HEADERS)
    assert response.status_code == 200

    data = response.json()
    assert "updatedAt" in data

