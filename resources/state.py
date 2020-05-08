from flask_restful import Resource, reqparse
from models.state import StateModel

class State(Resource):


    parser = reqparse.RequestParser()
    parser.add_argument('cases', type = int, required = True, help = 'This is a required field')
    parser.add_argument('deaths', type = int, required = True, help = 'This is a required field')
    parser.add_argument('recoveries', type = int, required = False,)

    def get(self, name, country):
        state = StateModel.find_by_state(name)
        if state:
             return state.json()
        return {'message': 'State not found'}, 404
        

class States(Resource):
    def get(self):
        return {'states': [state.json() for state in StateModel.query.all()]}
