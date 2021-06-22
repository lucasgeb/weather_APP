import json
import requests

def obtener_clima(ruta):
    req = requests.get(ruta)
    if req.status_code == 200:
       dic = json.loads(req.text)
       return dic
    else:
        print('Error')


def clima_ciudad(ciudad):
    url_ciudad = 'https://api.openweathermap.org/data/2.5/weather?'
    api_key = '6a19af64431d36030095df61d4e2abdd'
    ciudad = ciudad
    unidades = "metric"

    parametros = {"q":ciudad, "units": unidades, "appid":api_key}

    response = requests.get(url_ciudad, params=parametros)

    data_clima_ciudad = json.loads(response.content)
    info = {
        'Temperatura' : data_clima_ciudad['main']['temp'],
        'Humedad' : data_clima_ciudad['main']['humidity'],
        'Sensación Térmica' : data_clima_ciudad['main']['feels_like']
    }
    return info


def clima_coord(lat, lon):

    url_lat_lon = 'https://api.openweathermap.org/data/2.5/weather?'
    api_key = '6a19af64431d36030095df61d4e2abdd'
    latitud = lat
    longitud = lon
    units = "metric"

    parametros = {"lat":latitud, "lon":longitud, "units": units, "appid":api_key}

    response = requests.get(url_lat_lon, params=parametros)

    data_clima_coord = json.loads(response.content)
    info = {
        'Temperatura' : data_clima_coord['main']['temp'],
        'Humedad' : data_clima_coord['main']['humidity'],
        'Sensación Térmica' : data_clima_coord['main']['feels_like']
    }
    return info




def pronostico_ciudad(ciudad):
    url_ciudad = 'https://api.openweathermap.org/data/2.5/forecast?'
    api_key = '6a19af64431d36030095df61d4e2abdd'
    ciudad = ciudad
    unidades = "metric"
    exclude = "current,minutely,hourly,alerts"

    parametros = {"q":ciudad, "units": unidades, "exclude": exclude, "appid":api_key}

    response = requests.get(url_ciudad, params=parametros)

    data_pronostico_ciudad = json.loads(response.content)
    for item in data_pronostico_ciudad['list']:
        info = {
        'Fecha' : item['dt_txt'],
        'Temperatura' : item['main']['temp'],
        'Sensación térmica' : item['main']['feels_like'],
        'Presión' : item['main']['pressure'],
        'Humedad' : item['main']['humidity'],
            }
    
    return info
   


def pronostico_coord(lat, lon):

    url_lat_lon = 'https://api.openweathermap.org/data/2.5/forecast?'
    api_key = '6a19af64431d36030095df61d4e2abdd'
    latitud = lat
    longitud = lon
    units = "metric"
    

    parametros = {"lat":latitud, "lon":longitud, "units": units, "appid":api_key}

    response = requests.get(url_lat_lon, params=parametros)

    data_pronostico_coord = json.loads(response.content)
    
    for item in data_pronostico_coord['list']:
        info = {
        'Fecha' : item['dt_txt'],
        'Temperatura' : item['main']['temp'],
        'Sensación térmica' : item['main']['feels_like'],
        'Presión' : item['main']['pressure'],
        'Humedad' : item['main']['humidity'],
            },
        
    return info
    




menu=True
while menu:
    print("""
    1.Consultar el clima actual buscando por ciudad
    2.Consultar el clima actual buscando por coordenadas
    3.consultar el pronostico buscando por ciudad
    4.Consultar el pronostico buscando por coordenadas
    5.Terminar
    """)
    menu=input("¿qué desea consultar?")
    if menu=="1":
        ciudad = input("ingrese la ciudad para la búsqueda: ")
        print(clima_ciudad(ciudad))
    elif menu=="2":
        lat = input("ingrese latitud: ")
        lon = input("ingre la longitud: ")
        print(clima_coord(lat,lon))
    elif menu=="3":
        ciudad = input("ingrese la ciudad para la búsqueda: ")
        print(pronostico_ciudad(ciudad))
    elif menu=="4":    
        lat = input("ingrese latitud: ")
        lon = input("ingre la longitud: ")
        print(pronostico_coord(lat,lon))
    elif menu=="5":
         print("Chau!") 
         menu = None    
    else:
       print("La opción ingresada no es correcta")