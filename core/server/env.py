import os

SERVER_PORT = os.getenv("SERVER_PORT", 5000)

MONGODB_PATH = os.getenv("MONGODB_PATH", '"mongodb://mongodb_container:27017"/')
MONGODB_CLIENT = os.getenv("MONGODB_CLIENT", 'telemetry_db')
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION", 'telemetries')


    




    