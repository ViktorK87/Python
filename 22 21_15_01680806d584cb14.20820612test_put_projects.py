import requests

def test_put_projects():
  
    url = "https://ru.yougile.com/api-v2/projects/1e0e34e8-a207-414a-9343-a6f605a70207"

    bearer = "Bearer DnPNWaWclaanUqec0sABF6Yi4HX5ERrijbd2SC0Z5wzOYDTsf5DUyhc2Rm9q460h"

    payload = {
        "deleted": True,
        "title": "ГосУслуги"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": bearer
    }

    response = requests.request("PUT", url, json=payload, headers=headers)

    print(response.text)
    assert response.status_code == 200