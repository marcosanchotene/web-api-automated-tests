import requests

BASE_URL = "http://localhost:3000"


class TestPost:

    def test_create_profile(self):
        body = {"name": "Collaborator"}
        response = requests.post(BASE_URL + "/profiles", json=body)
        assert response.status_code == 200

    def test_create_post(self):
        body = {"title": "test", "author": "Collaborator"}
        response = requests.post(BASE_URL + "/posts", json=body)
        assert response.status_code == 201

    def test_add_comment(self):
        body = {"body": "some comment 2", "postId": 1}
        response = requests.post(BASE_URL + "/comments", json=body)
        assert response.status_code == 201
        response_body = response.json()
        assert response_body["body"] == "some comment 2"
        assert response_body["postId"] == 1


class TestGet:

    def test_see_post(self):
        response = requests.get(BASE_URL + "/posts/1")
        assert response.status_code == 200
        response_body = response.json()
        assert response_body["title"] == "json-server"
        assert response_body["author"] == "typicode"

    def test_see_comments(self):
        response = requests.get(BASE_URL + "/comments?postId=1")
        assert response.status_code == 200
        response_body = response.json()
        first_comment = response_body[0]
        assert first_comment["id"] == 1
        assert first_comment["body"] == "some comment"
        assert first_comment["postId"] == 1

    def test_see_profiles(self):
        response = requests.get(BASE_URL + "/profiles?name=typicode")
        assert response.status_code == 200
        response_body = response.json()
        first_profile = response_body[0]
        assert first_profile["name"] == "typicode"
