def test_read_all_planets_returns_empty_list(client):
    #arrange 

    #act
    response = client.get("/planets")
    response_body = response.get_json()

    #assert
    assert response_body == []
    assert response.status_code == 200


def test_read_planet_by_id(client, make_two_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name":"Mercury",
        "description":"powdery gray",
        "moon_number": 0
    }
    
def test_read_planet_by_invalid_id(client, make_two_planets):
    response = client.get("/planets/1000")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body == {"message":'planet 1000 not found'}
    

def test_create_planet(client):
    response = client.post("/planets", json={        
        "name": "Earth",
        "description": "blue and green",
        "moon_number": 1
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"