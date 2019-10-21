from flask import Flask
from flask_restful import Api, Resource, reqparse, request

import subprocess
import os
import socket

app = Flask(__name__)
api = Api(app)

dnszone = "private.p2spoc"
resourcegroup = "p2spoc"

class Host(Resource):
    def post(self, host):
        print("\n")
        print("Attempting to add DNS A record for "+host +" with IP address " +request.remote_addr)

        parser = reqparse.RequestParser()
        args = parser.parse_args()

        req = 'az network private-dns record-set a add-record -g ' +resourcegroup +' -z ' +dnszone +' -a ' +request.remote_addr +' -n ' +host

        os.system(req)

        host_ret = host +"." + dnszone +" created"
        return host_ret, 201

    def delete(self, host):
        # TDB
        return

api.add_resource(Host, "/host/<string:host>")

app.run(debug=True, port=8080, host= '0.0.0.0')
