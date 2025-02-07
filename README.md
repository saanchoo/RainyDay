# RainyDay

## Descripción

RainyDay es una aplicación que proporciona pronósticos meteorológicos y envía mensajes SMS para alertar si va a llover o si va a haber sol. Utiliza la API de OpenWeatherMap para obtener los datos meteorológicos y Twilio para enviar los mensajes SMS.

## Características

- Obtiene pronósticos del clima de la API de OpenWeatherMap.
- Envía un SMS si va a llover o si está soleado utilizando Twilio.
- Configuración flexible mediante variables de entorno.
  
## Requisitos

- Python 3.x
- Librerías necesarias:
  - `requests`
  - `twilio`
  - `python-dotenv`

## Instalación

### 1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/RainyDay.git
cd RainyDay
