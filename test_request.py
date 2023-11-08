import requests

def test_request():
    return requests.get(
            'http://localhost:8000'
            ).json()

print(test_request())

