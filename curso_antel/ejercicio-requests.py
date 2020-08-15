import requests
import json
url_base = "http://www.montevideo.gub.uy/ubicacionesRest/calles/?nombre="

def busca_calles():
    parametro = input("Ingrese string a buscar:")
    url_buscar= url_base+parametro
    r = requests.get(url_buscar,headers={"User-Agent":"Juan"})
    print(r.text)
    if r.text == None:
        print("No se encontro una poronga")

busca_calles()

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("https://httpbin.org/get", data=payload)
# print(r.text)