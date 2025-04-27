import requests

class  New_page_company:


    def __init__(self, company_id, bearer):
        self.base_url = "https://ru.yougile.com"
        self.name = "Поток_100"
        self.company_id = company_id
        self.bearer = bearer


    def post_project(self, name)->str:
        url = self.base_url+"/api-v2/projects"
        bearer = self.bearer
        payload = {
            "title": name
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.bearer
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        return response
    

    def put_project(self, name)->str:
        name = name
        id = self.post_project("some_name").json()["id"]
        url = "https://ru.yougile.com/api-v2/projects/" + id

        payload = {
            "title": name,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.bearer
        }
        response = requests.request("PUT", url, json=payload, headers=headers)
        return response


    def get_project(self, name):
        name = name
        id = self.post_project(name).json()["id"]
        url = "https://ru.yougile.com/api-v2/projects/" + id

        headers = {
            "Content-Type": "application/json",
            "Authorization": self.bearer
        }

        response = requests.request("GET", url, headers=headers)
        return response