from flask import Flask
from flask_restful import Api, Resource, reqparse, request

import os
import socket

app = Flask(__name__)
api = Api(app)

dnszone = "dns.ptspoc"
resourcegroup = "PTS-PoC"

class User(Resource):
    def post(self, name):
        print("\n")
        print("Attempting to add DNS A record for "+name +" and IP " +request.remote_addr)

        parser = reqparse.RequestParser()
        args = parser.parse_args()

        req = 'az network private-dns record-set a add-record -g ' +resourcegroup +' -z ' +dnszone +' -a ' +request.remote_addr +' -n ' +name
        os.system(req)

        return name, 201

    def delete(self, name):
        # TDB

api.add_resource(User, "/user/<string:name>")

app.run(debug=True, port=8080, host= '0.0.0.0')
