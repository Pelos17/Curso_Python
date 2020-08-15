import requests
import json
url_base = "http://www.montevideo.gub.uy/ubicacionesRest/calles/?nombre="

def busca_calles():
    parametro = input("Ingrese string a buscar:")
    url_buscar= url_base+parametro
    r = requests.get(url_buscar,headers={"User-Agent":"Manuel"})
    datos=json.loads(r.text)
    for x in datos:
        print(x["nombre"])
    if datos == []:
        print("No se encontro el string.")

busca_calles()