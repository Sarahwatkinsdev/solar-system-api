from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, moon_number):
        self.id = id
        self.name = name
        self.description = description
        self.moon_number = moon_number
        

planets = [
    Planet(1, "Mercury", "Dark gray", 0),
    Planet(2, "Venus", "Light yellowish", 0),
    Planet(3, "Earth", "Blue and green", 1)
    ]

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("", methods=["GET"])
def handle_planets():
    planet_response = []
    for planet in planets:
        planet_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moon_number": planet.moon_number
        })
    return jsonify(planet_response)