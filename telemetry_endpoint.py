from flask import Flask, request, jsonify

from telemetries import parse_telemetry, TelemetryData
from database import store_telemetry
from variables import SERVER_PORT

app = Flask(__name__)

@app.route('/telemetry', methods=['POST'])
def receive_telemetries():

    data = request.get_json()
    telemetry_fields = list(TelemetryData.model_fields.keys())

    if not all(key in data for key in telemetry_fields):
        # TODO: Determine whether to delete all data or retain the received telemetry entries.
        
        # This point may be reached if a new telemetry field is added in a future version, 
        # as older versions won't send this field and will always have missing data.

        return jsonify({"error": "Incomplete telemetry data received. Some required fields are missing."}), 400
    
    telemetry = parse_telemetry(data)

    try: 
        store_telemetry(telemetry)
        return jsonify({"message": "Success"}), 200
    
    except Exception as e:
        return jsonify({"error": e}), 400

if __name__ == '__main__':
    app.run(port = SERVER_PORT, debug = True)

