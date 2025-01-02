#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:53:01 2023

@author: laptop
"""

# Crear un entorno virtual 
# Con Anaconda
# C:\proyecto> create --name API-REST python=3
# Con venv
# C:\proyecto> python -m venv venv

# Activar el entorno virtual
# Con Anaconda
# C:\proyecto> conda activate API-REST
# Con venv
# Para dar permisos de ejecución al PowerShell
# C:\proyecto> Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# C:\proyecto> .\venv\Scripts\Activate

# pip install fastapi
# pip install uvicorn
# en linux $ sudo apt-get install uvicorn
# pip freeze > requirements.txt

# Desactivar el entorno virtual
# !conda deactivate

# Para ver dónde está el environment
"""
import sys
print(sys.executable)
"""
# Usar -> API-REST/lib/python3.10/site-packages

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:53:01 2023

@author: laptop
"""

import pickle
from datetime import datetime
from fastapi import FastAPI, HTTPException
from uuid import uuid4 as uuid   # Para generar identificadores únicos

app = FastAPI()

# uvicorn app:app --reload
# En el navegador ya estaría funcionando http://127.0.0.1:8000/docs

# Función para guardar datos en un archivo pickle
def guarda_datos(publicaciones):
    with open("publicaciones.pckl", 'wb') as archivo:
        pickle.dump(publicaciones, archivo)

# Función para cargar datos desde un archivo pickle
def carga_datos():
    try:
        with open("publicaciones.pckl", 'rb') as archivo:
            publicaciones = pickle.load(archivo)
        return publicaciones
    except FileNotFoundError:
        return []

# Lista para almacenar las publicaciones
publicaciones = carga_datos()

@app.get("/")
def lee_raiz():
    return {"Bienvenida": "Bienvenidos a mi API"}

@app.get("/listado")
def lee_listado():
    return {"listado": publicaciones}

@app.post("/publicacion")
def guardar_publicacion(titulo: str, contenido: str, autor: str = "Aitor Donado"):
    nueva_publicacion = {
        "id": str(uuid()),
        "titulo": titulo,
        "autor": autor,
        "contenido": contenido,
        "fecha_creacion": datetime.now().isoformat(),
        "fecha_publicacion": None
    }
    publicaciones.append(nueva_publicacion)
    guarda_datos(publicaciones)
    return nueva_publicacion

@app.get("/listado/{identificador}")
def lee_publicacion_id(identificador: str):
    for publicacion in publicaciones:
        if publicacion["id"] == identificador:
            return publicacion
    raise HTTPException(status_code=404, detail="Publicación no encontrada")

@app.delete("/listado/{identificador}")
def elimina_publicacion_id(identificador: str):
    for indice, publicacion in enumerate(publicaciones):
        if publicacion["id"] == identificador:
            publicaciones.pop(indice)
            guarda_datos(publicaciones)
            return {"mensaje": "La publicación ha sido eliminada"}
    raise HTTPException(status_code=404, detail="Publicación no encontrada")

@app.put("/listado/{identificador}")
def actualiza_publicacion_id(identificador: str, titulo: str, contenido: str, autor: str = "Aitor Donado"):
    for publicacion in publicaciones:
        if publicacion["id"] == identificador:
            publicacion["titulo"] = titulo
            publicacion["contenido"] = contenido
            publicacion["autor"] = autor
            publicacion["fecha_publicacion"] = datetime.now().isoformat()
            guarda_datos(publicaciones)
            return {"mensaje": "La publicación ha sido actualizada"}
    raise HTTPException(status_code=404, detail="Publicación no encontrada")