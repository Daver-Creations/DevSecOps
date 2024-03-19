import datetime
from db.database_generator import *
from flask import request
from flask_restful import Resource


def request_validation(data, *keys):
    for key in keys:
        if key not in data.keys():
            return key
    return None


class Greet(Resource):
    def get(self):
        return 'Hello get'

    def post(self):
        return 'Hello post'

    def put(self):
        return 'Hello put'

    def delete(self):
        return 'Hello delete'
    

class Checkin(Resource):
    def post(self):
        data = request.json
        val = request_validation(data, 'location', 'client_id')
        if val:
            return {
            'status': 'success',
            'message': f'missing -> {val}'
            }
        location = data['location']
        client_id = data['client_id']
        date = datetime.datetime.now()
        
        insert_start_time(client_id, date, location)

        print(f'location->{location} date->{date}')
        response = {
            'status': 'success',
            'message': 'parking is valid'
        }
        return response

    def put(self):
        return 'Hello put'

    def delete(self):
        return 'Hello delete'
    

class Checkout(Resource):
    def get(self):
        return 'Hello get'

    def post(self):
        data = request.json
        client_id = data["client_id"]
        current_time = datetime.datetime.now()
        insert_end_time(client_id, current_time)
        return {
            'status': 'success',
            'message': 'have a nice day'
        }


    def put(self):
        return 'Hello put'

    def delete(self):
        return 'Hello delete'
    

class Logs(Resource):
    def get(self):
        data = request.json
        val = request_validation(data, 'client_id')
        if val:
            return {
            'status': 'success',
            'message': f'missing -> {val}'
            }
        client_id = data["client_id"]
        res = get_sessions_by_user(client_id)
        print(res)
        return res


    def post(self):
        return 'Hello post'

    def put(self):
        return 'Hello put'

    def delete(self):
        return 'Hello delete'