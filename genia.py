from google import genai

CLAVE_API = "<YOUR_API_KEY_HERE>"

cliente = genai.Client(api_key=CLAVE_API)

prompt = ("Actua como un urbanista regenerativo y "
          "genera 3 claves para el diseño de sistema de agua en una ciudad circular."
          "Formato: lista numerada.")


respuesta = cliente.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print("Respuesta del modelo:")
print(respuesta.text)
