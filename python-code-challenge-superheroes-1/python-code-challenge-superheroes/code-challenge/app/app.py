#!/usr/bin/env python3

from flask import Flask, jsonify , request , abort
from flask_migrate import Migrate


from models import db, Hero , Powers , Hero_Powers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1> Welcome </h1>'

@app.route('/heroes' , methods=['GET'])
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

    if hero is None:

        return jsonify({"error": "Hero not found"}),404
    
    serialized_hero = {
            "id":hero.id,
            "name":hero.name,
            "super_name": hero.super_name
    }
    return jsonify(serialized_hero)
    

    # if hero is not None:
    #     powers = hero.powers
    #     serialized_powers = [
    #         {
    #              "id": power.id,
    #             "name": power.name,
    #             "description": power.description
    #         }
    #         for power in powers
    #     ]

    #     serialized_hero = {
    #          "id": hero.id,
    #         "name": hero.name,
    #         "super_name": hero.super_name,
    #         "powers": serialized_powers
    #     }

    #     return jsonify(serialized_hero)
    # else :
    #     response = jsonify({"error":"Hero not found"})
    #     response.status_code = 404
    #     return response
    
@app.route('/powers' , methods=['GET'])
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

@app.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):

    power = Powers.query.get(id)

    if power is None:

        return jsonify({"error": "Power not found"}),404
    
    serialised_power = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }

    return jsonify(serialised_power)

@app.route('/power/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Powers.query.get(id)

    if power is None:
        return jsonify({"error": "Power not found"}), 404

    updated_description = request.json.get('description')

    if updated_description:
        power.description = updated_description

        try:
            db.session.commit()

            serialized_power = {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }

            return jsonify(serialized_power)
        except Exception as e:
            db.session.rollback()
            return jsonify({"errors": ["validation errors"]}), 400
    else:
        return jsonify({"errors": ["description is required"]}), 400

@app.route('/hero_powers' , methods=['POST'])

def create_hero_power():

    data = request.json

    strength = data.get('strength')
    power_id = data.get('power_id')
    hero_id = data.get('hero_id')

    if not (strength and power_id and hero_id):
        return jsonify({"errors": ["strength, power_id, and hero_id are required"]}), 400
    
    hero = Hero.query.get(hero_id)

    if hero is None:

        return jsonify({"error": "Hero not found"}), 404
    
    power = Powers.query.get(power_id)

    if power is None:
        return jsonify({"error": "Power not found"}), 404
    
    hero_power = Hero_Powers(strength=strength, hero=hero, power=power)

    try:
        db.session.add(hero_power)
        db.session.commit()

        serialized_hero = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "powers": [
                {
                    "id": p.id,
                    "name": p.name,
                    "description": p.description
                }
                for p in hero.powers
            ]
        }
        return jsonify(serialized_hero)
    except Exception as e:

        db.session.rollback()
        return jsonify({"errors": ["validation errors"]}), 400






if __name__ == '__main__':
    app.run(port=5555,debug=True)
@app.route('/power/<int:id>', methods=['PATCH'])
def update_power_by_id(id):

    power = Powers.query.get(id)

    if power is None :

        return jsonify({"error": "Power not found"}), 404
    
    updated_description = request.json.get('description')

    if updated_description :

        power.description = updated_description

        try:

            db.session.commit()

            serialised_power = {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }

            return jsonify(serialised_power)
        except Exception as e :

            db.session.rollback()
            return jsonify({"errors": ["validation errors"]}), 400
        else:
             return jsonify({"errors": ["description is required"]}), 400
