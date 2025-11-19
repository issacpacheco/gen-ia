💡 Mini Repositorio: Guía Regenerativa con IA (Gemini)
🚀 Descripción del Proyecto
Este repositorio contiene el código de Python que demuestra cómo utilizar los modelos de Inteligencia Artificial Generativa (Gemini 2.5 Flash) de Google para obtener insights estructurados y específicos en temas de Guía Regenerativa.

El objetivo es permitirte implementar rápidamente un agente de IA que pueda asistir en el análisis y la generación de contenido especializado, como los principios de diseño para una ciudad circular.

📁 Archivos Incluidos
regenerative_agent.py: Script principal que contiene el código para conectar con la API de Gemini y ejecutar el prompt del urbanista regenerativo.

requirements.txt: Archivo con las dependencias necesarias.

🛠️ Requisitos e Instalación
1. Requisitos de Python
Asegúrate de tener Python 3.9+ instalado.

2. Instalación de la Librería
Instala el SDK oficial de Google para IA Generativa:

Bash

pip install google-genai
O, si utilizas un archivo de requisitos:

Bash

pip install -r requirements.txt
3. Obtener tu Clave API
Para que el código funcione, necesitas una Clave API de Gemini. Puedes obtener una de forma gratuita en el Google AI Studio.

🔑 Configuración de la Clave API (¡Importante!)
El código está configurado para que puedas pegar tu clave directamente para una prueba rápida, aunque la mejor práctica es usar variables de entorno (consulta la documentación de Google para producción).

Abre el archivo regenerative_agent.py.

Reemplaza la línea CLAVE_API = "<YOUR_API_KEY_HERE>" con tu clave real.

Código a modificar en regenerative_agent.py:

Python

CLAVE_API = "AIzaSy...TU_CLAVE_REAL_AQUÍ...XYZ" 
▶️ Uso del Script
Una vez que hayas configurado tu clave API, ejecuta el script desde tu terminal:

Bash

python regenerative_agent.py
📄 Código de Ejemplo (regenerative_agent.py)
El script ejecutará el siguiente código para generar la respuesta:

Python

from google import genai

CLAVE_API = "<YOUR_API_KEY_HERE>"

cliente = genai.Client(api_key=CLAVE_API)

prompt = ("Actua como un urbanista regenerativo y "
          "genera 3 claves para el diseño de sistema de agua en una ciudad circular. "
          "Formato: lista numerada.")

respuesta = cliente.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print("Respuesta del modelo:")
print(respuesta.text)
🧠 Siguientes Pasos (Mejora del Prompt)
El secreto para obtener resultados de alta calidad de la IA Generativa reside en el prompt. Te invito a:

Modificar el Prompt: Cambia el rol de la IA (Actúa como...) y el enfoque del problema.

Explorar Modelos: Cambia model="gemini-2.5-flash" por otro modelo compatible (ej. gemini-2.5-pro) para ver las diferencias en el resultado.

¡Feliz codificación!
