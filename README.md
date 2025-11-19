# 💡 Mini Repositorio: Guía Regenerativa con IA (Gemini)

## 🚀 Descripción del Proyecto

Este repositorio contiene el código base en **Python** que demuestra cómo utilizar los modelos de **Inteligencia Artificial Generativa (Gemini 2.5 Flash)** de Google para obtener *insights* estructurados y específicos en temas de **Guía Regenerativa**.

El objetivo es permitirte implementar rápidamente un agente de IA que pueda asistir en el análisis y la generación de contenido especializado, como los principios de diseño para una ciudad circular.

---

## 🛠️ Requisitos e Instalación

### 1. Requisitos de Python

Asegúrate de tener **Python 3.9 o superior** instalado en tu sistema.

### 2. Instalación de la Librería

Instala el SDK oficial de Google para IA Generativa ejecutando el siguiente comando en tu terminal:

```bash
pip install google-genai
```

O, si utilizas un archivo de requisitos:

```bash
pip install -r requirements.txt
```
### 3. Obtener tu Clave API

Para que el código funcione, necesitas una Clave API de Gemini. Puedes obtener una de forma gratuita en el Google AI Studio.

## 🔑 Configuración de la Clave API (¡Importante!)
El código está configurado para que puedas pegar tu clave directamente para una prueba rápida, aunque la mejor práctica es usar variables de entorno (consulta la documentación de Google para producción).

Abre el archivo 
```bash
genia.py.
```

Reemplaza la línea CLAVE_API = "<YOUR_API_KEY_HERE>" con tu clave real.

Código a modificar en genia.py:

Python
```bash
CLAVE_API = "AIzaSy...TU_CLAVE_REAL_AQUÍ...XYZ"
```

# 🧠 Siguientes Pasos (Mejora del Prompt)
El secreto para obtener resultados de alta calidad de la IA Generativa reside en el prompt. Te invito a:

Modificar el Prompt: Cambia el rol de la IA (Actúa como...) y el enfoque del problema.

Explorar Modelos: Cambia model="gemini-2.5-flash" por otro modelo compatible (ej. gemini-2.5-pro) para ver las diferencias en el resultado.

¡Feliz codificación!
