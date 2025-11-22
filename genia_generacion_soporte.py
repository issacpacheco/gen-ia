import os
from google import genai

# IMPORTANTE: ¡REEMPLAZA ESTA SECCIÓN CON TU CLAVE API REAL!
# Nota: La clave proporcionada en el código original es un ejemplo.
CLAVE_API = "<token de acceso real>" 

cliente = genai.Client(api_key=CLAVE_API)

# 1. Definir la lista de archivos que quieres leer
# ¡REEMPLAZA estos nombres con los archivos que realmente quieres analizar!
archivos_a_leer = [
    "onu_info.txt"
] 

# 2. Configuración inicial del prompt
prompt_inicial = (
    "Eres un exporto en soporte tecnico en redes informaticas, ciberseguridad y telecomunicaciones. "
    "Entiendes los archivos de logs y puedes ayudar a diagnosticar problemas de red."
    "\n\n--- INICIO DE CONTENIDO DE ARCHIVOS ---\n\n"
)

# Variable para almacenar todo el contenido de los archivos
contenido_combinado = ""
archivos_procesados = []

# 3. Iterar sobre la lista de archivos y leer su contenido
for nombre_archivo in archivos_a_leer:
    try:
        # El bloque 'with open' se encarga de abrir y cerrar el archivo
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
            # Añadir una etiqueta para distinguir el contenido de cada archivo
            contenido_combinado += f"===== ARCHIVO: {nombre_archivo} =====\n"
            contenido_combinado += contenido
            contenido_combinado += "\n\n" # Separador entre archivos
            archivos_procesados.append(nombre_archivo)
            print(f"✅ Archivo leído: {nombre_archivo}")
    except FileNotFoundError:
        print(f"⚠️ ¡Error! El archivo no se encontró: {nombre_archivo}")
    except Exception as e:
        print(f"❌ Ocurrió un error al leer el archivo {nombre_archivo}: {e}")


# 4. Construir el prompt final
# Solo enviamos el contenido si logramos leer al menos un archivo
if contenido_combinado:
    prompt_final = prompt_inicial + contenido_combinado
    
    # Añadir la instrucción final para el modelo
    prompt_final += "\n\n--- FIN DE CONTENIDO DE ARCHIVOS ---\n\n"
    prompt_final += (
        "Analiza el contenido de TODOS los archivos proporcionados y "
        "proporciona un diagnóstico detallado de cualquier problema potencial que "
        "puedas identificar, junto con recomendaciones para solucionarlo. "
        "Especifica a qué archivo corresponde cada problema."
    )

    print("\n--- Enviando solicitud al modelo Gemini ---\n")
    print(f"Archivos incluidos en el análisis: {', '.join(archivos_procesados)}")

    # 5. Generar contenido con el prompt final
    respuesta = cliente.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_final,
    )

    print("\n--- Respuesta del modelo ---\n")
    print(respuesta.text)

else:
    print("\nNo se pudo leer el contenido de ningún archivo. No se envió la solicitud a la API.")