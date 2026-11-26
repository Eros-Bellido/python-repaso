# =============================================================
# LECCIÓN 4: Módulos, entornos virtuales, errores y JSON
# Ejecuta: python leccion4.py
# =============================================================
import json        # los import SIEMPRE van al inicio del archivo
import os
import random
from datetime import date


# --- 1. MÓDULOS: usar código de otros archivos -----------------
# Un módulo es un archivo .py con funciones que puedes reutilizar.
print(random.randint(1, 10))      # número al azar entre 1 y 10
print(date.today())               # fecha de hoy

# import modulo             -> se usa como modulo.funcion()
# from modulo import cosa   -> se usa directo: cosa()

# TUS PROPIOS MÓDULOS: si tienes funciones_carrito.py en la MISMA carpeta
#   from funciones_carrito import calcular_subtotal, calcular_descuento
# y ya las puedes usar aquí como si estuvieran escritas en este archivo.

# Para que un módulo no ejecute código al importarlo:
#   if __name__ == "__main__":
#       ...   # esto solo corre si ejecutas ESE archivo directamente


# --- 2. PIP Y ENTORNOS VIRTUALES (se usan en la TERMINAL) -------
# pip instala librerías de otros: pip install requests
#
# Un entorno virtual (venv) es una "caja" de librerías SOLO para un
# proyecto, para que no choquen versiones entre proyectos.
#
#   python -m venv venv            -> crea la caja (carpeta venv/)
#   venv\Scripts\activate          -> la activa (Windows). Verás (venv) al inicio
#   pip install requests           -> instala DENTRO de la caja
#   pip freeze > requirements.txt  -> guarda la lista de librerías
#   pip install -r requirements.txt -> otro instala lo mismo con un comando
#   deactivate                     -> sale de la caja
#
# La carpeta venv/ NO se sube a GitHub: va en un archivo .gitignore
# Lo que sí se sube es requirements.txt.


# --- 3. MANEJO DE ERRORES: try / except ------------------------
# Si algo puede fallar, lo intentas (try) y si falla lo atrapas (except)
# en lugar de que el programa se caiga.
entradas = ["25.90", "abc"]
for texto in entradas:
    try:
        precio = float(texto)
        print(f"Precio válido: {precio}")
    except ValueError:
        print(f"'{texto}' no es un número")

# Patrón clave: repetir la pregunta HASTA que el dato sea válido
#   while True:
#       try:
#           precio = float(input("Precio: "))
#           if precio <= 0:
#               print("Debe ser mayor a 0")
#               continue
#           break                       # dato válido -> sale del bucle
#       except ValueError:
#           print("Escribe un número, por ejemplo 25.90")

# Errores comunes que vas a atrapar:
#   ValueError        -> float("abc")
#   KeyError          -> carrito["no_existe"]
#   FileNotFoundError -> abrir un archivo que no existe
#   ZeroDivisionError -> 10 / 0


# --- 4. ARCHIVOS Y JSON: guardar datos para que no se pierdan ---
# JSON es texto con formato de diccionario. Es lo que usan las APIs.
carrito = {"Polo": 25.90, "Gorra": 80.00}

# GUARDAR: "w" = write (escribe y reemplaza el archivo)
with open("demo_carrito.json", "w", encoding="utf-8") as archivo:
    json.dump(carrito, archivo, indent=4, ensure_ascii=False)
# with cierra el archivo solo al terminar el bloque.
# indent=4 lo deja ordenado; ensure_ascii=False respeta ñ y tildes.

# CARGAR: "r" = read
with open("demo_carrito.json", "r", encoding="utf-8") as archivo:
    cargado = json.load(archivo)
print(cargado)                    # {'Polo': 25.9, 'Gorra': 80.0}

# Cargar si existe; si no, empezar vacío
try:
    with open("no_existe.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    datos = {}
print(datos)                      # {}

os.remove("demo_carrito.json")    # borra el archivo de prueba


# =============================================================
# BUENAS PRÁCTICAS
# =============================================================
# - Imports al inicio del archivo.
# - Separa tu código: funciones en un módulo, programa principal en otro.
# - Un venv por proyecto; venv/ en .gitignore, requirements.txt en el repo.
# - Atrapa el error ESPECÍFICO (except ValueError), no un except vacío.
# - Valida la entrada del usuario: nunca confíes en lo que escriben.
# - Usa with open(...) para archivos; se cierran solos.

# =============================================================
# ERRORES COMUNES
# =============================================================
# - except: solo, sin tipo -> oculta errores que sí deberías ver.
# - Abrir con "w" un archivo que querías leer -> lo borra.
# - Instalar librerías sin activar el venv -> se instalan "fuera de la caja".
# - Subir la carpeta venv/ a GitHub.
# - Importar un módulo propio que no está en la misma carpeta.