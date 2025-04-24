import requests

def test_get_with_id():
    url = "https://ru.yougile.com/api-v2/projects/1e0e34e8-a207-414a-9343-a6f605a70207"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer DnPNWaWclaanUqec0sABF6Yi4HX5ERrijbd2SC0Z5wzOYDTsf5DUyhc2Rm9q460h"
    }

    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
