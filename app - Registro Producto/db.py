from pymongo import MongoClient
import certifi
import urllib

MONGO_URI = "mongodb+srv://adminDatademy:" + urllib.parse.quote('P@ssw0rd1') + "@clusterdatademy.qduii2a.mongodb.net/?retryWrites=true&w=majority"
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile = ca)
        db = client["db_app_product"]
    except ConnectionError as e:
        print("Error de conexión con la base de datos!")
    else:
        print("Estás conectado!")
        return db