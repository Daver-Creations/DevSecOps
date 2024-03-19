from flask import Flask
from flask_restful import Api, Resource

from db.database_generator import *
from resources.res import *

app = Flask('Mango')
api = Api(app, prefix = '/api')

api.add_resource(Greet, '/hello')
api.add_resource(Checkin, '/checkin')
api.add_resource(Checkout, '/checkout')
api.add_resource(Logs, '/logs')

@app.after_request
def after(response):
    print(f'response -> {response}')
    return response

if __name__ == '__main__':
    init_db()
    app.run(use_reloader = True, debug = True, host = '0.0.0.0', port = 80)

# @app.get('/hello')
# def greet():
#     return 'hi'

# @app.post('/hello')
# def greet1():
#     return 'hi'