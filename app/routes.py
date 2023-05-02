from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"planet {planet_id} not found"}, 404))

    return planet

@planets_bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        moon_number=request_body["moon_number"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(
            {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moon_number": planet.moon_number
            }
        )
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moon_number": planet.moon_number
            }

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moon_number = request_body["moon_number"]
    
    db.session.commit()
    
    return make_response(f"planet {planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    
    db.session.delete(planet)
    db.session.commit()
    
    return make_response(f"planet #{planet.id} successfully deleted")

# class Planet:
#     def __init__(self, id, name, description, moon_number):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.moon_number = moon_number
        

# planets = [
#     Planet(1, "Mercury", "Dark gray", 0),
#     Planet(2, "Venus", "Light yellowish", 0),
#     Planet(3, "Earth", "Blue and green", 1)
#     ]

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message":f"planet {planet_id} invalid"}, 400))

#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
    
#     abort(make_response({"message":f"planet {planet_id} not found"}, 404))
    
# planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

# @planet_bp.route("", methods=["GET"])
# def handle_planets():
#     planet_response = []
#     for planet in planets:
#         planet_response.append({
#             "id": planet.id,
#             "name": planet.name,
#             "description": planet.description,
#             "moon_number": planet.moon_number
#         })
#     return jsonify(planet_response)

# @planet_bp.route("/<planet_id>", methods=["GET"])

# def handle_planets_by_id(planet_id):
#     planet = validate_planet(planet_id)
    
#     return {
#         "id": planet.id,
#         "name": planet.name,
#         "description": planet.description,
#         "moon_number": planet.moon_number
#     }