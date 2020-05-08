from db import db

class StateModel(db.Model):

    __tablename__= 'states'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    cases = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    recoveries = db.Column(db.Integer)

    def __init__(self, name, cases, deaths, recoveries):
        self.name = name
        self.cases = cases
        self.deaths = deaths
        self.recoveries = recoveries

    def json(self):
        return {'name': self.name, 'cases': self.cases, 'deaths': self.deaths, 'recoveries': self.recoveries}

    @classmethod
    def find_by_state(cls, name):
        return cls.query.filter_by(name=name).first()
