from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.country import CountryModel


class Country(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('cases', type = int, required = True, help = 'This is a required field')
    parser.add_argument('deaths', type = int, required = True, help = 'This is a required field')
    parser.add_argument('recoveries', type = int, required = False,)

    def get(self, name):
        country = CountryModel.find_by_country(name)
        if country:
            return country.json()
        return {'message': 'Country not found'}, 404


class Countries(Resource):
    def get(self):
        return {'countries': [ country.json() for country in CountryModel.query.all()]}
