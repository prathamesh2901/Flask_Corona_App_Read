from db import db

class CountryModel(db.Model):

    __tablename__= 'countries'

    name = db.Column(db.String(50), primary_key=True)
    date = db.Column(db.String(50), primary_key=True)
    cases = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    recoveries = db.Column(db.Integer)

    def __init__(self, name, date, cases, deaths, recoveries):
        self.name = name
        self.cases = cases
        self.deaths = deaths
        self.recoveries = recoveries
        self.date = date


    def json(self):
        return {'name': self.name, 'date': self.date, 'cases': self.cases, 'deaths': self.deaths, 'recoveries': self.recoveries}

    @classmethod
    def find_by_country(cls, name, date):
        return cls.query.filter_by(name=name, date=str(date)).first()
