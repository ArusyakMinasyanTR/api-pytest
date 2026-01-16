import requests

def test_get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_patch_and_delete_post():
    patch_data = {"title": "updated title"}
    patch_response = requests.patch(
        "https://jsonplaceholder.typicode.com/posts/1", json=patch_data
    )
    assert patch_response.status_code == 200
    assert patch_response.json()["title"] == "updated title"

    delete_response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert delete_response.status_code == 200