import requests

respuesta = requests.get("http://0.0.0.0:8000/")

respuesta.json()

requests.get("http://0.0.0.0:8000/listado/").json()
requests.get("http://0.0.0.0:8000/listado/1e19afb8-cf98-46b9-a2e0-7e219b7cbf57").json()
requests.get("http://0.0.0.0:8000/listado/108f4c0c-2b79-484f-acfc-57054541755a").json()

requests.delete("http://0.0.0.0:8000/listado/108f4c0c-2b79-484f-acfc-57054541755a").json()
requests.get("http://0.0.0.0:8000/listado/").json()

datos = {"titulo": "Mensaje desde Python", 
         "contenido": "Este mensaje se ha introducido desde un script de Python"}

requests.post("http://0.0.0.0:8000/publicacion/", params = datos).json()
requests.get("http://0.0.0.0:8000/listado/").json()

datos_nuevos = {"titulo": "Primer mensaje modificado",
                "contenido": "Se ha modificado desde Python",
                "autor": "Otra persona"}

requests.put("http://0.0.0.0:8000/listado/1e19afb8-cf98-46b9-a2e0-7e219b7cbf57", 
             params = datos_nuevos).json()

requests.get("http://0.0.0.0:8000/listado/").json()
