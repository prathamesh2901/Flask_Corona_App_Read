from flask_restful import Resource, reqparse
from models.state import StateModel
from cache.state import CountryCache


class State(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('cases', type = int, required = True, help = 'This is a required field')
    parser.add_argument('deaths', type = int, required = True, help = 'This is a required field')
    parser.add_argument('recoveries', type = int, required = False,)

    def get(self, name, country):
        cached_state = StateCache(name)
        if cached_state.find_by_state():
            return cached_state.find_by_state()
        else:
            state = StateModel.find_by_state(name)
            if state:
                cached_state.cache(state.json())
                return state.json()
            return {'message': 'State not found'}, 404


class States(Resource):
    def get(self):
        return {'states': [state.json() for state in StateModel.query.all()]}
