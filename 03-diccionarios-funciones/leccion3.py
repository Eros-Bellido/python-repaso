# =============================================================
# LECCIÓN 3: Diccionarios, sets y funciones
# Ejecuta: python leccion3.py
# =============================================================


# --- 1. DICCIONARIOS: pares clave -> valor ---------------------
# En vez de dos listas alineadas, un solo diccionario.
carrito = {"Polo": 25.90, "Gorra": 80.00}

print(carrito["Polo"])          # 25.9  -> se accede por CLAVE, no por posición
carrito["Short"] = 40.00        # agrega (o actualiza si la clave ya existe)
del carrito["Gorra"]            # elimina
print(carrito)                  # {'Polo': 25.9, 'Short': 40.0}
print("Polo" in carrito)        # True -> ¿existe la clave?
print(carrito.get("Medias", 0)) # 0    -> si no existe, devuelve el valor por defecto

# Recorrer: .items() da (clave, valor) en cada vuelta
for producto, precio in carrito.items():
    print(f"{producto}: S/ {precio:.2f}")

# Un diccionario puede describir UN objeto con varios datos
producto = {"nombre": "Polo", "precio": 25.90, "stock": 10}
print(producto["stock"])        # 10


# --- 2. SETS: colección SIN repetidos y sin orden --------------
categorias = {"ropa", "accesorios", "ropa"}
print(categorias)               # {'ropa', 'accesorios'} -> el repetido se elimina
categorias.add("calzado")

# Truco útil: quitar repetidos de una lista
tallas = ["S", "M", "S", "L", "M"]
print(set(tallas))              # {'S', 'M', 'L'}


# --- 3. FUNCIONES: bloques de código reutilizables -------------
# def nombre(parámetros):
#     ...
#     return resultado

def calcular_descuento(subtotal):
    if subtotal > 200:
        return subtotal * 0.15
    elif subtotal > 100:
        return subtotal * 0.10
    return 0                    # si no entró a ningún if

descuento = calcular_descuento(129.50)
print(f"S/ {descuento:.2f}")    # S/ 12.95

# Parámetro con valor por defecto
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"

print(saludar("Eros"))              # Hola, Eros
print(saludar("Eros", "Buenas"))    # Buenas, Eros

# return vs print:
#   return DEVUELVE el valor para usarlo después (guardarlo, sumarlo...).
#   print solo lo MUESTRA en pantalla; la función devuelve None.


# =============================================================
# BUENAS PRÁCTICAS
# =============================================================
# - Datos relacionados juntos: un diccionario, no dos listas alineadas.
# - Una función = una sola tarea. Nombre con verbo: calcular_total, mostrar_detalle.
# - Las funciones RETORNAN datos; los print van fuera (separa cálculo de mostrar).
# - Si copias y pegas un bloque de código, conviértelo en función (DRY).
# - Usa .get() cuando no estés seguro de que la clave exista.

# =============================================================
# ERRORES COMUNES
# =============================================================
# - KeyError: pedir una clave que no existe -> carrito["Medias"]. Usa .get().
# - Olvidar el return: la función calcula pero devuelve None.
# - Definir la función DESPUÉS de llamarla: primero def, luego se usa.
# - Las claves distinguen mayúsculas: "polo" != "Polo".