import requests

def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1sdf")
    #print(response.status_code)
    assert response.status_code == 200, f"For successful request the status code is 200, but got {response.status_code}"


def test_get_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print(response.json())
    assert response.status_code == 200, f"For successful request the status code is 200, but got {response.status_code}"



if __name__ == "__main__":
    test_get_user()
    test_get_post()