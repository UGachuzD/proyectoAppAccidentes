from pymongo import MongoClient
from gtts import gTTS
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Obtener accidente mas comun
def obtenerAccidenteMasComun(zona):
    # Conexion con MongoDB
    uri = "mongodb+srv://gachuz:kgL8Gjc0FCtnYSdU@accidentes-viales.x4eth4z.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["accidentesvialescmdx"]
    collection = db["accidentesvialescmdx20222023"]

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
        tts.save("assets/mensaje.mp3")
        # os.system("start mensaje.mp3") 
    else:
        print(f"No hay datos de accidentes para la zona {zona}.")

    client.close()
# obtenerAccidenteMasComun("LA JOYA")