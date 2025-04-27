from new_page_company import New_page_company

name = "Поток_100"
company_id = "ae23443f-caa3-49bb-aad9-78810990b1a1"
bearer = "Bearer DnPNWaWclaanUqec0sABF6Yi4HX5ERrijbd2SC0Z5wzOYDTsf5DUyhc2Rm9q460h"
company = New_page_company(company_id, bearer)

def test_post_project():
    name = "some_name"
    id_project = company.post_project(name)
    assert id_project.status_code == 201

def test_put_project():
    name = "name_2"
    response = company.put_project(name)
    assert response.status_code == 200


def test_get():
    name = "namename"
    response = company.get_project(name)
    assert response.status_code == 200


def test_negative_post():
    name = ""
    id_project = company.post_project(name)
    assert id_project.status_code == 201

def test_negative_put():
    name = "$%#^#**@^*@"
    response = company.put_project(name)
    assert response.status_code == 200


def test_negative_get():
    name = "namename"
    response = company.get_project(name)
    assert response.status_code == 400
