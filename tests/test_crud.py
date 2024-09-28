import requests
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user():
    response = requests.get(BASE_URL+"/users/1")
    #print(response.json())
    assert response.status_code == 200, f"For successful request the status code is 200, but got {response.status_code}"


def test_get_post():
    response = requests.get(BASE_URL+"/posts/1")
    #print(response.json())
    assert response.status_code == 200, f"For successful request the status code is 200, but got {response.status_code}"


def test_add_new_user():
    payload = {
        "name": "PK",
        "username": "pk",
        "email": "pk@example.com"
    }

    response = requests.post(BASE_URL+"/users", json=payload)
    assert response.status_code == 201, f"For successful adding of user the status code is 201, but got {response.status_code}"


def test_update_user():
    payload = {
        "name": "PK updated",
        "username": "pk updated",
        "email": "pkup@example.com"
    }

    response = requests.put(BASE_URL+"/users/1", json=payload)
    assert response.status_code == 200, f"For successful adding of user the status code is 201, but got {response.status_code}"
    #print(response.json())



def test_delete_user():
    response = requests.delete(BASE_URL+"/users/1")
    assert response.status_code == 200, f"For successful adding of user the status code is 201, but got {response.status_code}"


if __name__ == "__main__":
    test_get_user()
    test_get_post()
    test_add_new_user()
    test_update_user()
    test_delete_user()