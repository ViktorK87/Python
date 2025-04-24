import requests

def test_post_projects():
    url = "https://ru.yougile.com/api-v2/projects"
    bearer = "Bearer DnPNWaWclaanUqec0sABF6Yi4HX5ERrijbd2SC0Z5wzOYDTsf5DUyhc2Rm9q460h"
    payload = {
        "title": "ГосУслуги"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": bearer
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)
    assert response.status_code == 201

