import os
from twilio.rest import Client
from dotenv import load_dotenv

# Cargar las variables del .env
load_dotenv()

# Obtener las variables de entorno de Twilio
ACC_SID = os.getenv("TWILIO_ACC_SID")
AU_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER")

# Crear el cliente de Twilio
client = Client(ACC_SID, AU_TOKEN)

def rainySMS():
    message = client.messages.create(
        body="☔️HOY LLUEVE️☔️",
        from_=TWILIO_PHONE_NUMBER,
        to=TO_PHONE_NUMBER,
    )

def sunnySMS():
    message = client.messages.create(
        body="☀️☀HOY SALE EL SOL️☀️",
        from_=TWILIO_PHONE_NUMBER,
        to=TO_PHONE_NUMBER,
    )
