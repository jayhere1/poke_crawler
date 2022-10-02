from pymongo import MongoClient
from configparser import ConfigParser

import certifi

config = ConfigParser()
config.read('mongouri.ini')

CONNECTION_STRING = (config['DEV']['DB_URI'])


def get_db():
    client = MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
    db = client.get_database('poke_database')
    return db
