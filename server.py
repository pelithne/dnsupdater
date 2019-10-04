from flask import Flask
from flask_restful import Api, Resource, reqparse, request

import os
import socket

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "",
        "ipaddress": ""
    }
]

class User(Resource):
    def post(self, name):
        print(request.remote_addr)

        parser = reqparse.RequestParser()
        args = parser.parse_args()

        req = 'az network private-dns record-set a add-record -g PTS-PoC -z dns.ptspoc '+'-a '+request.remote_addr +' -n ' +name
        os.system(req)

        return name, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

api.add_resource(User, "/user/<string:name>")

app.run(debug=True, port=8080, host= '0.0.0.0')
