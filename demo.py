from pymongo import MongoClient
from gtts import gTTS
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config import MONGO_URI

# Conexion con MongoDB
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client["accidentesvialescmdx"]
collection = db["accidentesvialescmdx20222023"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    # print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Obtener accidente mas comun
def obtenerAccidenteMasComun(zona):
    pipeline = [
        {"$match": {"colonia": zona}},
        {"$group": {"_id": "$incidente_c4", "TotalAccidentes": {"$sum": 1}}},
        {"$sort": {"TotalAccidentes": -1}},
        {"$limit": 1}
    ]

    resultado = collection.aggregate(pipeline)
    resultado = list(resultado)
    print(resultado)
    
    if resultado:
        tipoAccidente = resultado[0]['_id']
        numeroTotalAccidentes = resultado[0]['TotalAccidentes']
        mensaje = f"El tipo de accidente más común en la zona {zona} es {tipoAccidente} con un total de {numeroTotalAccidentes} accidentes."
        print(mensaje)

        # Convertir el texto a voz
        tts = gTTS(text=mensaje, lang='es')
        tts.save("mensaje.mp3")
        os.system("start mensaje.mp3") 
    else:
        print(f"No hay datos de accidentes para la zona {zona}.")

def obtenerAccidenteMenosComun(zona):
    pipeline = [
        {"$match": {"colonia": zona}},
        {"$group": {"_id": "$incidente_c4", "TotalAccidentes": {"$sum": 1}}},
        {"$sort": {"TotalAccidentes": 1}},
        {"$limit": 1}
    ]

    resultado = collection.aggregate(pipeline)
    resultado = list(resultado)
    print(resultado)
    
    if resultado:
        tipoAccidente = resultado[0]['_id']
        numeroTotalAccidentes = resultado[0]['TotalAccidentes']
        mensaje = f"El tipo de accidente menos común en la zona {zona} es {tipoAccidente} con un total de {numeroTotalAccidentes} accidentes."
        print(mensaje)

        # Convertir el texto a voz
        tts = gTTS(text=mensaje, lang='es')
        tts.save("mensaje.mp3")
        os.system("start mensaje.mp3") 
    else:
        print(f"No hay datos de accidentes para la zona {zona}.")

def prueba():
    cursor = collection.find()
    for document in cursor:
        print(document)
    print("Acabo")


#zona = input("Ingrese la zona para obtener su informacion: ")
# obtenerAccidenteMasComun(zona)
#obtenerAccidenteMenosComun(zona)
# client.close()