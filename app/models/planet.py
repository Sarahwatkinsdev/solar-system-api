from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moon_number = db.Column(db.Integer)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "moon_number": self.moon_number
        }
        
    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(
            name=planet_data["name"],
            color=planet_data["description"],
            powers=planet_data["moon_number"]
        )
        return new_planet