#!/usr/bin/env python3
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import subprocess
import re

app = Flask(__name__)
api = Api(app)

class upsapi(Resource):
    def get(self):
        status = subprocess.Popen(['pwrstat', '-status'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
        ups = {}

        model_match = "Model Name"
        firmware_match = "Firmware Number"
        rating_volt_match = "Rating Voltage"
        rating_watt_match = "Rating Power"
        state_match = "State"
        utility_volt_match = "Utility Voltage"
        output_volt_match = "Output Voltage"
        battery_capacity_match = "Battery Capacity"
        load_watt_match = "Load"

        period_to_end = r"(?<=\.\.\s)(.*)"
        load_percent_re = r"(?<=\()(.*?)(?=\s*%\))"
        load_watt_re = r"(?<=\.\.\s)(.*?)(?= Watt)"
        only_digits_re = r"\D"

        ups = {}
        for line in status.splitlines():
            if model_match in line:
                ups['model_name'] = re.search(period_to_end, line).group().strip()
            if firmware_match in line:
                ups['firmware'] = re.search(period_to_end, line).group().strip()
            if rating_volt_match in line:
                ups['rating_volt'] = int(re.sub(only_digits_re, '', line))
            if rating_watt_match in line:
                ups['rating_watt'] = int(re.sub(only_digits_re, '', line))
            if state_match in line:
                ups['state'] = re.search(period_to_end, line).group().strip()
            if utility_volt_match in line:
                ups['utility_volt'] = int(re.sub(only_digits_re, '', line))
            if output_volt_match in line:
                ups['output_volt'] = int(re.sub(only_digits_re, '', line))
            if battery_capacity_match in line:
                ups['battery_capacity'] = int(re.sub(only_digits_re, '', line))
            if load_watt_match in line:
                ups['load_watt'] = int(re.search(load_watt_re, line).group().strip())
                ups['load_percent'] = int(re.search(load_percent_re, line).group().strip())

        return jsonify(ups)

api.add_resource(upsapi, '/ups-api') # return all parameters

if __name__ == '__main__':
     app.run(port=5002, host='0.0.0.0')