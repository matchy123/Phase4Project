from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Api

from models import db, Animal, Category, Specie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

@app.route('/animals')
def get_animals():

    animals = Animal.query.all()
    animal_list = []
    for animal in animals:
        animal_dict= {
            'id':animal.id,
            'name': animal.name,
            'image': animal.image,
            'gender': animal.gender,
            'species_id': animal.species_id,
            'category_id': animal.category_id

    }
    animal_list.append(animal_dict)
    response = make_response(jsonify(animal_dict), 200)
    return response

@app.route('/category')
def get_categories():

    categories= Category.query.all()
    category_list = []
    for category in categories:
        category_dict= {
            'id':category.id,
            'name': category.name,
            'color': category.color,
            
    }
    category_list.append(category_dict)
    response = make_response(jsonify(category_dict), 200)
    return response

@app.route('/species')
def get_species():

    species= Specie.query.all()
    specie_list = []
    for specie in species:
        specie_dict= {
            'id':specie.id,
            'name':specie.name,
            'habitat':specie.habitat,
            
    }
    specie_list.append(specie_dict)
    response = make_response(jsonify(specie_dict), 200)
    return response

@app.route('/animals', methods=['POST'])
def add_animal():
    data = request.get_json()  # Get data from JSON body

    # Basic validation to check if all required fields are in the JSON body
    if not all(key in data for key in ('name', 'image', 'gender', 'species_id', 'category_id')):
        return make_response(jsonify({"error": "Missing data"}), 400)

    try:
        new_animal = Animal(
            name=data['name'],
            image=data['image'],
            gender=data['gender'],
            species_id=data['species_id'],
            category_id=data['category_id']
        )
        db.session.add(new_animal)  # Add new animal to the session
        db.session.commit()  # Commit the session to save changes to the database
        return make_response(jsonify({"message": "Animal added successfully", "id": new_animal.name}), 201)
    except Exception as e:
        db.session.rollback()  # Roll back the session in case of error
        return make_response(jsonify({"error": "Failed to add animal", "message": str(e)}), 500)
    

@app.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    animal = Animal.query.get(id)  # Try to find the animal by ID
    if animal is None:
        return make_response(jsonify({"error": "Animal not found"}), 404)  # Animal not found

    try:
        db.session.delete(animal)  # Delete the found animal
        db.session.commit()  # Commit the changes to the database
        return make_response(jsonify({"message": "Animal deleted successfully"}), 200)
    except Exception as e:
        db.session.rollback()  # Roll back the session in case of error
        return make_response(jsonify({"error": "Failed to delete animal", "message": str(e)}), 500)





if __name__ == '__main__':
    app.run(port=5555, debug=True)
