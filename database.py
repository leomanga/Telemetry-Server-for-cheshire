from pymongo import MongoClient

from telemetries import TelemetryData
from variables import (
    MONGODB_PATH, MONGODB_CLIENT, MONGODB_COLLECTION
    )

def store_telemetry(telemetry: TelemetryData):
    db = MongoDB()

    try:
        db.insertTelemetry(telemetry)

    except Exception as e:
        raise Exception(f"Error occurred while saving telemetry data")  
    
    finally:
        db.close()

class MongoDB():
    def __init__(self):
        self._client = MongoClient(MONGODB_PATH)
        self._db = self._client[MONGODB_CLIENT]
        self._collection = self._db[MONGODB_COLLECTION]
    
    def insertTelemetry(self, telemetry: TelemetryData):
        try:
            self._collection.insert_one(telemetry.model_dump())

        except Exception as e:
            raise e
        
    def close(self):
        self._client.close()
