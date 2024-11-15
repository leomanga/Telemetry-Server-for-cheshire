from flask import Flask, request, jsonify
from icecream import ic
import pydantic

from server.telemetries import parse_telemetry
from server.database import Database, MongoDB
from server.database import DatabaseSaveError

from server.env import SERVER_PORT

app = Flask(__name__)

database: Database = MongoDB()
        
@app.route('/telemetry', methods=['POST'])
def receive_telemetries():
    data = request.get_json()
    try: 
        telemetry = parse_telemetry(data)

        database.store_telemetry(telemetry)
        ic(f"Added telemetry: \n{telemetry}")
        
        return jsonify({"message": "Success"}), 200
    
    except pydantic.ValidationError as e: 
        # TODO: separate different ValidationError types 
        # (empty required field, error in UUID pasing)

        # TODO: Determine whether to delete all data or retain the received telemetry entries.
        # This point may be reached if a new REQUIRED telemetry field is added in a future version, 
        # as older versions won't send this field and will always have missing data.

        ic(f"Parsing error:\n{e}")
        return jsonify({"error": "Error occurred while parsing telemetry data"}), 400

    except DatabaseSaveError as e:
        ic(f"Database error:\n{e}")
        return jsonify({"error": "Error occurred while saving telemetry data"}), 500

    except Exception as e:
        ic(f"Unexpected error:\n{e}")
        return jsonify({"error": "Unexpected error occurred"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = SERVER_PORT, debug = False) # TODO: FIX - "Debug mode" attempts to connect to the DB twice.
    database.close()

