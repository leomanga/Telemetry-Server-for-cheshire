from pymongo import MongoClient
from abc import ABC, abstractmethod
from icecream import ic

from server.telemetries import TelemetryData
from server.env import (
    MONGODB_PATH, MONGODB_CLIENT, MONGODB_COLLECTION
    )

class Database(ABC):
    @abstractmethod
    def store_telemetry(self, telemetry: TelemetryData):
        """Store telemetry data in the database."""
        pass

    @abstractmethod
    def close(self):
        """Close the database connection."""
        pass

class MongoDB(Database):
    def __init__(self):
        self._client = MongoClient(MONGODB_PATH)
        self._db = self._client[MONGODB_CLIENT]
        self._collection = self._db[MONGODB_COLLECTION]
    
    def store_telemetry(self, telemetry: TelemetryData):
        try:
            self._collection.insert_one(telemetry.model_dump())

        except Exception as e:
            raise Exception(f"Error occurred while saving telemetry data") from e
        
    def close(self):
        self._client.close()
