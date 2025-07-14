from ocr import pdfToText
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import time

model = OllamaLLM(model="gemma3n", temperature=0)
result = pdfToText()

print("-----------------------------------")
print("Información obtenida correctamente...")

template = """
Extraé la información solicitada de la siguiente cadena de texto.  
Devolvé únicamente los valores requeridos, sin agregar explicaciones, formato extra o palabras adicionales.

Texto:
"{cadena}"

Información solicitada:
{instrucción_específica}

Resultado:
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n--------------------------------")
    user_query = input("Pregunta lo que quieras. (Presiona X para salir)... ")
    print("\n\n")
    if user_query == "X":
        break
    inputs = {
        "cadena": result,
        "instrucción_específica": user_query
    }
    start = time.time()
    response = chain.invoke(inputs)
    end = time.time()
    print(response)
    tiempo_total = end - start
    print(f"Tiempo transcurrido: {tiempo_total:.2f} segundos")