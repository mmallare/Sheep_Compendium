from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():

# TODO: Prepare the new sheep data in a dictionary format.
    new_sheep = {
        "id": 7,
        "name": "Suffern",
        "breed": "Suffolk",
        "sex":"ram"
    }

# TODO: Send a POST request to the endpoint "/sheep" with the new sheep data.
# Arguments should be your endpoint and new sheep data.
    response = client.post("/sheep", json=new_sheep)

# TODO: Assert that the response status code is 201 (Created)
    assert response.status_code == 201
# TODO: Assert that the response JSON matches the new sheep data
    assert response.json() == new_sheep
# TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
# include as assert statement to see if the new sheep data can be retrieved.
    get_response = client.get(f"/sheep/{new_sheep['id']}")
    assert get_response.status_code == 200
    assert get_response.json() == new_sheep

def test_read_all_sheep():
    response = client.get("/sheep")
    sheep_list = response.json()

    assert response.status_code == 200
    assert len(sheep_list) >= 6
    assert {
               "id": 1,
               "name": "Spice",
               "breed": "Gotland",
               "sex": "ewe"
           } in sheep_list

def test_update_sheep():
    updated_sheep = {
        "id": 2,
        "name": "Blondie",
        "breed": "Polypay",
        "sex" : "ewe" #initially was 'ram'
    }

    response = client.put(f"/sheep/{updated_sheep['id']}", json=updated_sheep)

    assert response.status_code == 200
    assert response.json() == updated_sheep

def test_delete_sheep():
    sheep_to_delete = {
        "id": 3,
        "name": "Deedee",
        "breed": "Jacobs Four Horns",
        "sex" : "ram"
    }

    response = client.delete(f"/sheep/{sheep_to_delete['id']}")
    assert response.status_code == 204
    get_response = client.get(f"/sheep/{sheep_to_delete['id']}")
    assert get_response.status_code == 200
    assert get_response.json() is None