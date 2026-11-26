# =============================================================
# LECCIÓN 3: Diccionarios, sets y funciones
# Ejecuta: python leccion3.py
# =============================================================


# --- 1. DICCIONARIOS: pares clave -> valor ---------------------
# En vez de dos listas alineadas, un solo diccionario.
carrito = {}                    # vacío, se llena después
carrito["Polo"] = 25.90         # agrega (o actualiza si la clave ya existe)
carrito["Gorra"] = 80.00
print(carrito)                  # {'Polo': 25.9, 'Gorra': 80.0}

print(carrito["Polo"])          # 25.9 -> se accede por CLAVE, no por posición
print(carrito.get("Medias", 0)) # 0    -> si no existe, devuelve el valor por defecto
del carrito["Gorra"]            # elimina
carrito["Gorra"] = 80.00        # (lo volvemos a agregar para los ejemplos)

# ¿Existe la clave?  `in` ya devuelve True o False: no le pongas == True
if "Polo" in carrito:
    print("Polo ya está en el carrito")


# --- 2. KEYS, VALUES, ITEMS ------------------------------------
print(list(carrito.keys()))     # ['Polo', 'Gorra']   -> solo claves
print(list(carrito.values()))   # [25.9, 80.0]        -> solo valores
print(list(carrito.items()))    # [('Polo', 25.9), ('Gorra', 80.0)] -> pares

print(sum(carrito.values()))    # 105.9 -> sumar todos los precios
print(len(carrito))             # 2     -> cantidad de productos

for producto, precio in carrito.items():     # (clave, valor) en cada vuelta
    print(f"{producto}: S/ {precio:.2f}")

# OJO: los diccionarios NO tienen .index() (eso es solo de listas).

# Un diccionario también puede describir UN objeto con varios datos
item = {"nombre": "Polo", "precio": 25.90, "stock": 10}
print(item["stock"])            # 10


# --- 3. BUSCAR EL MAYOR RECORRIENDO ----------------------------
# Patrón: guardar "el mejor visto hasta ahora" y compararlo en cada vuelta.
precio_max = 0
nombre_max = ""
for producto, precio in carrito.items():
    if precio > precio_max:
        precio_max = precio     # guardo el precio
        nombre_max = producto   # y a quién pertenece
print(f"Más caro: {nombre_max} (S/ {precio_max:.2f})")


# --- 4. SETS: colección SIN repetidos --------------------------
tallas = ["S", "M", "S", "L", "M"]
print(set(tallas))              # {'S', 'M', 'L'} -> quita repetidos


# --- 5. FUNCIONES ----------------------------------------------
# def nombre(parámetro):
#     ...
#     return resultado

def calcular_descuento(subtotal):       # espera un NÚMERO
    if subtotal > 200:
        return subtotal * 0.15
    elif subtotal > 100:
        return subtotal * 0.10
    return 0

# Llamarla: le pasas el dato y GUARDAS lo que devuelve
descuento = calcular_descuento(129.50)
print(f"S/ {descuento:.2f}")    # S/ 12.95

# Pasa el tipo de dato correcto:
#   calcular_descuento(129.50)    -> bien, es un número
#   calcular_descuento(carrito)   -> ERROR, es un diccionario

# Parámetro con valor por defecto
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"
print(saludar("Eros"))          # Hola, Eros

# return DEVUELVE el valor para usarlo después.
# print solo lo MUESTRA; una función sin return devuelve None.


# --- 6. ALCANCE (SCOPE) ----------------------------------------
# Las variables creadas DENTRO de una función solo existen ahí.
# Lo que la función necesita, se lo pasas como parámetro.
def total_con_igv(monto):
    igv = monto * 0.18          # 'igv' solo existe dentro de la función
    return monto + igv
print(total_con_igv(100))       # 118.0
# print(igv)                    # ERROR: igv no existe aquí afuera


# --- 7. ORDEN DE UN PROGRAMA -----------------------------------
# Python ejecuta de ARRIBA hacia ABAJO y NO recalcula solo.
#   1. Funciones (def)
#   2. Entrada de datos (while / input)
#   3. Cálculos (DESPUÉS de tener los datos)
#   4. Mostrar resultados (print)
# Si calculas antes de llenar los datos, calculas sobre algo vacío.


# =============================================================
# BUENAS PRÁCTICAS
# =============================================================
# - Datos relacionados juntos: un diccionario, no dos listas alineadas.
# - Funciones al inicio del archivo.
# - Una función = una tarea. Nombre con verbo: calcular_total.
# - Las funciones RETORNAN; los print van fuera.
# - Guarda el resultado de una función en una variable si lo usas
#   más de una vez (DRY): subtotal = calcular_subtotal(carrito)

# =============================================================
# ERRORES COMUNES
# =============================================================
# - KeyError: pedir una clave que no existe. Usa .get() o revisa con `in`.
# - Escribir `x in dic == True`: Python lo lee mal. Basta con `x in dic`.
# - Usar una variable de afuera dentro de la función sin pasarla.
# - Pasar a una función un tipo distinto al que espera.
# - Calcular antes de tener los datos (resultados en 0).
# - Olvidar el return: la función devuelve None.