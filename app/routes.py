from flask import Blueprint, jsonify, abort, make_response

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
    
planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

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