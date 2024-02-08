from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String)
    gender = db.Column(db.String(100), nullable=False)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    
    # Relationship 
    species = db.relationship('Specie', back_populates='animals')
    category = db.relationship('Category', back_populates='animals')

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  
    color = db.Column(db.String(100))  

    # Relationship to Animal
    animals = db.relationship('Animal', back_populates='category')

class Specie(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    habitat = db.Column(db.String(100), nullable=False)

    # Relationship to Animal
    animals = db.relationship('Animal', back_populates='species')
