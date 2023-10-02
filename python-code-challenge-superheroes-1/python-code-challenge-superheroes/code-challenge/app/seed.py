from models import db, Hero, Powers, Hero_Powers
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def seed_data():
    with app.app_context():
        hero1 = Hero(name="Superman", super_name="Clark Kent")
        hero2 = Hero(name="Batman", super_name="Bruce Wayne")
        hero3 = Hero(name="The Rock", super_name="Dwayne Johnson")

        db.session.add(hero1)
        db.session.add(hero2)
        db.session.add(hero3)

        power1 = Powers(name="Can Fly", description="Very powerful")
        power2 = Powers(name="Stealthy", description="Powerful Gadgets")
        power3 = Powers(name="Strong", description="Can Fight")

        db.session.add(power1)
        db.session.add(power2)
        db.session.add(power3)

        heropower1 = Hero_Powers(strength="High", hero=hero1, power=power1)
        heropower2 = Hero_Powers(strength="Medium", hero=hero2, power=power2)
        heropower3 = Hero_Powers(strength="Low", hero=hero3, power=power3)

        db.session.add(heropower1)
        db.session.add(heropower2)
        db.session.add(heropower3)

        db.session.commit()

if __name__ == '__main__':
    seed_data()
