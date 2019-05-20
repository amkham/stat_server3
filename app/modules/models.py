# coding: utf-8
from app import db


class Criterion(db.Model):
    __tablename__ = 'criterions'

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('criterias_id_seq'::regclass)"))
    name = db.Column(db.String)


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.Text)
    value = db.Column(db.String)
    subkod1 = db.Column(db.String)
    date = db.Column(db.String)
    oktmo = db.Column(db.Text, unique=True)
    regions_id = db.Column(db.Integer)
    subject = db.Column(db.Text)


class Subject(db.Model):
    __tablename__ = 'subject'

    id = db.Column(db.Integer, primary_key=True, server_default=db.text("nextval('subject_id_seq'::regclass)"))
    name = db.Column(db.String)
    kod = db.Column(db.String, unique=True)


class Statistic(db.Model):
    __tablename__ = 'statistic'

    id = db.Column(db.Integer, primary_key=True, unique=True, server_default=db.text("nextval('statistic_id_seq'::regclass)"))
    value = db.Column(db.Integer)
    date = db.Column(db.Integer)
    criterions_id = db.Column(db.ForeignKey('criterions.id', ondelete='CASCADE', onupdate='CASCADE'))
    locations_id = db.Column(db.ForeignKey('locations.id', ondelete='CASCADE', onupdate='CASCADE'))
    locations = db.Column(db.String)

    criterions = db.relationship('Criterion')
    locations1 = db.relationship('Location')

