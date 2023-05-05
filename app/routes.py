from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"planet {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"planet {model_id} not found"}, 404))

    return model

@planets_bp.route("", methods=["POST"])
def handle_planets():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)
    
    db.session.add(new_planet)
    db.session.commit()

    return jsonify(f"Planet {new_planet.name} successfully created"), 201

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    description_query = request.args.get("description")
    
    if description_query:
        planets = Planet.query.filter_by(description=description_query)
    else:
        planets = Planet.query.all()
        
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    return planet.to_dict(), 200

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    
    request_body = request.get_json()
    
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.moon_number = request_body["moon_number"]
    
    db.session.commit()
    
    return make_response(f"planet {planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    
    db.session.delete(planet)
    db.session.commit()
    
    return make_response(f"planet #{planet.id} successfully deleted")
