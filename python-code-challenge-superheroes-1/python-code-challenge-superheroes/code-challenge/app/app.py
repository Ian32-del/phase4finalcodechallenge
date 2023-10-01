#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate


from models import db, Hero , Powers , Hero_Powers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_app.db'
app.config['SQLALCHEMY_TRACK-MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1> Welcome </h1>'

@app.route('/heroes' , method=['GET'])
def get_heroes():

    heroes = Hero.query.all()

    serialized_heroes = [
        {
            "id":hero.id,
            "name":hero.name,
            "super_name": hero.super_name
        }
        for hero in heroes
    ]

    return jsonify(serialized_heroes)

@app.route('/heroes/<int:id>' , methods=["GET"])
def get_hero_by_id(id):

    hero = Hero.query.get(id)

    if hero is not None:
        powers = hero.powers
        serialized_powers = [
            {
                 "id": power.id,
                "name": power.name,
                "description": power.description
            }
            for power in powers
        ]

        serialized_hero = {
             "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "powers": serialized_powers
        }

        return jsonify(serialized_hero)
    else :
        response = jsonify({"error":"Hero not found"})
        response.status_code = 404
        return response
    
@app.route('/powers' , method=['GET'])
def get_powers():

    powers = Powers.query.all()

    serialized_powers=[
        {
             "id": power.id,
            "name": power.name,
            "description": power.description
        }
        for power in powers
    ]

    return jsonify(serialized_powers)

if __name__ == '__main__':
    app.run(port=5555)
