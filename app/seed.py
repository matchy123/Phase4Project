# seed.py
from app import app
from models import Animal, Category, Specie, db

with app.app_context():

    # Clear existing data
    db.session.query(Animal).delete()
    db.session.query(Category).delete()
    db.session.query(Specie).delete()

    # Categories
    carnivore = Category(name='Carnivore', color='Red')
    herbivore = Category(name='Herbivore', color='Green')

    # Species
    lion = Specie(name='Lion', habitat='Savannah')
    zebra = Specie(name='Zebra', habitat='Grasslands')

    # Animals
    animals = [
        Animal(name='Leo', image='path/to/leo.jpg', gender='Male', species=lion, category=carnivore),
        Animal(name='Zara', image='path/to/zara.jpg', gender='Female', species=zebra, category=herbivore),
    ]

    # Add to the session
    db.session.add(carnivore)
    db.session.add(herbivore)
    db.session.add(lion)
    db.session.add(zebra)
    db.session.add_all(animals)

    # Commit the changes
    db.session.commit()

"""if __name__ == '__main__':
    seed_data()"""
