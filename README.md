# 🌧️ RainyDay 🌞

**RainyDay** es una aplicación que proporciona pronósticos meteorológicos y te mantiene informado sobre el clima, enviando mensajes SMS para alertarte si va a llover o si hay sol. Utiliza la API de OpenWeatherMap para obtener los pronósticos y Twilio para enviar los SMS.

---

## ✨ Características

- 🌧️ Obtiene pronósticos meteorológicos de la **API de OpenWeatherMap**.
- 📲 Envía mensajes SMS a través de **Twilio** si está lloviendo o si hace sol.
- 🔒 Configuración flexible usando **variables de entorno**.

---

## 🚀 Requisitos

- Python 3.x
- Librerías necesarias:
  - \`requests\`
  - \`twilio\`
  - \`python-dotenv\`

---

## 📋 Instalación

Sigue estos pasos para poner en marcha **RainyDay** en tu entorno local.

### 1️⃣ Clona el repositorio:

\`\`\`bash
git clone https://github.com/tu-usuario/RainyDay.git
cd RainyDay
\`\`\`

### 2️⃣ Crea un entorno virtual (opcional pero recomendado):

\`\`\`bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
\`\`\`

### 3️⃣ Instala las dependencias:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4️⃣ Configura las variables de entorno:

- Crea un archivo \`.env\` en la raíz del proyecto.
- Añade las siguientes variables con tus valores:

\`\`\`env
MY_EMAIL=tu_email@example.com
PASSW=tu_contraseña
API_KEY=tu_api_key_de_openweathermap
TWILIO_ACCOUNT_SID=tu_account_sid_de_twilio
TWILIO_AUTH_TOKEN=tu_auth_token_de_twilio
TWILIO_PHONE_NUMBER=tu_numero_twilio
TO_PHONE_NUMBER=numero_destino
\`\`\`

### 5️⃣ Ejecuta la aplicación:

\`\`\`bash
python main.py
\`\`\`

---

## 🗂 Estructura del Proyecto

\`\`\`plaintext
RainyDay/
│
├── .gitignore          # Archivos y carpetas ignoradas por Git
├── .env                # Variables de entorno (no subir a GitHub)
├── main.py             # Código principal de la aplicación
├── smsSender.py        # Funciones para enviar SMS usando Twilio
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este archivo
\`\`\`

---

## 🤝 Contribuir

¡Me encantaría recibir tus contribuciones! Para hacerlo, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (\`git checkout -b mi-rama\`).
3. Realiza tus cambios y asegúrate de que el código sigue funcionando correctamente.
4. Envía un pull request para que podamos revisar tus cambios.

---

## 📜 Licencia

Este proyecto está bajo la **Licencia MIT**. Para más detalles, revisa el archivo [LICENSE](./LICENSE)." > README.md
