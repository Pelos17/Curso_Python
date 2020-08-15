def extraer_nombre(archivo):
    with open(archivo,"r") as archivo:
        archivo = archivo.read()
        print(archivo)



extraer_nombre("./archivos-nombres/baby1990.html")