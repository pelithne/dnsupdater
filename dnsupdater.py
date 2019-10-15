from flask import Flask
from flask_restful import Api, Resource, reqparse, request

import subprocess
import os
import socket

app = Flask(__name__)
api = Api(app)

#{
#  "appId": "9307c405-b0d3-40d3-837f-5b97a506e028",
#  "displayName": "dnsupdatersp",
#  "name": "http://dnsupdatersp",
#  "password": "619b1652-368c-4300-aa09-cf07b4307c81",
#  "tenant": "72f988bf-86f1-41af-91ab-2d7cd011db47"
#}

dnszone = "dns.ptspoc"
resourcegroup = "PTS-PoC"

class Host(Resource):
    def post(self, host):
        print("\n")
        print("Attempting to add DNS A record for "+host +" with IP address " +request.remote_addr)

        parser = reqparse.RequestParser()
        args = parser.parse_args()

        req = 'az network private-dns record-set a add-record -g ' +resourcegroup +' -z ' +dnszone +' -a ' +request.remote_addr +' -n ' +host
        
#        print ("String: " +req)

#        p = subprocess.Popen(['req'])
#        try:
#            p.wait(30)
#        except subp.TimeoutExpired:
#            p.kill()

        os.system(req)

        host_ret = host +"." + dnszone +" created"
        return host_ret, 201

    def delete(self, host):
        # TDB
        return

api.add_resource(Host, "/host/<string:host>")

app.run(debug=True, port=8080, host= '0.0.0.0')
