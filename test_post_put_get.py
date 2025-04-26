import requests

base_url = "https://ru.yougile.com"
bearer = "Bearer DnPNWaWclaanUqec0sABF6Yi4HX5ERr" \
         "ijbd2SC0Z5wzOYDTsf5DUyhc2Rm9q460h"


def test_post_projects():
    url = base_url+"/api-v2/projects"

    payload = {
        "title": "ГосУслуги"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": bearer
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response.json()["id"]


def test_negative_post_projects():
    url = base_url+"/api-v2/projects"

    payload = {
        "title": ""
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": bearer
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    assert response.status_code == 400


def test_put_projects():
    id = test_post_projects()
    url = base_url+"/api-v2/projects/"+id

    payload = {
        "deleted": True,
        "title": "Переименованные_услуги"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": bearer
    }

    response = requests.request("PUT", url, json=payload, headers=headers)
    assert response.status_code == 200


def test_negative_put_projects():
    url = base_url+"/api-v2/projects/1e0e34e8-a207-414a-9343-a6f605a70207"

    payload = {
        "deleted": True,
        "title": "*&&^^%^*&^*"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": bearer
    }

    response = requests.request("PUT", url, json=payload, headers=headers)
    assert response.status_code == 400


def test_get_projects():
    url = base_url+"/api-v2/projects/"+test_post_projects()

    headers = {
        "Content-Type": "application/json",
        "Authorization": bearer
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200


def test_negative_get_projects():
    url = base_url+"/api-v2/projects/"+test_post_projects()

    headers = {
        "Content-Type": "application/json",
        "Authorization": bearer
    }
    response = requests.request("GET", url, headers=headers)
    assert len(response.json()["users"]) > 0


# Старое:
# def test_get_with_id():
#     url = base_url+"/api-v2/projects/1e0e34e8-a207-414a-9343-a6f605a70207"

#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": bearer
#     }

#     response = requests.request("GET", url, headers=headers)
#     assert response.status_code == 200

# def test_negative_get_with_id():
#     url = base_url+"/api-v2/projects"

#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": bearer
#     }

#     response = requests.request("GET", url, headers=headers)
#     assert response.status_code == 200
