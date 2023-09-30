from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    super_name = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime , onupdate=datetime.utcnow)
    powers = db.relationship('Powers',secondary='hero_powers',back_populates='heroes')

class Powers(db.Model):
    __tablename__ = 'power'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(100))
    created_at = db.Column(db.DateTime , default=datetime.utcnow)
    updated_at = db.Column(db.DateTime , onupdate=datetime.utcnow)
    heroes = db.relationship('Hero', secondary='hero_powers', back_populates='powers')

class Hero_Powers(db.Model):
    __tablename__= 'hero_powers'

    id = db.Column(db.Integer,primary_key=True)
    strength = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    hero_id = db.Column(db.Integer,db.ForeignKey('hero.id'))
    power_id = db.Column(db.Integer , db.ForeignKey('power.id'))



# add any models you may need. 