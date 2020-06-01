from db import db
from sqlalchemy import text, desc

class StateModel(db.Model):

    __tablename__= 'states'

    name = db.Column(db.String(50), primary_key=True)
    date = db.Column(db.String(50), primary_key=True)
    cases = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    recoveries = db.Column(db.Integer)

    def __init__(self, name, date, cases, deaths, recoveries):
        self.name = name
        self.date = date
        self.cases = cases
        self.deaths = deaths
        self.recoveries = recoveries


    def json(self):
        return {'name': self.name, 'date': self.date, 'cases': self.cases, 'deaths': self.deaths, 'recoveries': self.recoveries}

    @classmethod
    def find_by_state(cls, name):
        return cls.query.filter_by(name=name).order_by(desc(cls.date)).first()
