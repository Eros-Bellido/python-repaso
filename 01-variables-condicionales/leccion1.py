# =============================================================
# LECCIÓN 1: Variables, tipos, input y condicionales
# Ejecuta este archivo con: python leccion1.py
# Lee cada bloque, mira lo que imprime y compáralo con el comentario.
# =============================================================


# -------------------------------------------------------------
# 1. VARIABLES Y TIPOS
# -------------------------------------------------------------
# Una variable es un nombre que guarda un dato.
# Python detecta solo el tipo según el valor que le das.

producto = "Polo"      # str   -> texto, siempre entre comillas
cantidad = 3           # int   -> número entero (sin decimales)
precio = 25.90         # float -> número decimal (se usa punto, no coma)
es_oferta = False      # bool  -> solo puede ser True o False

print("--- 1. Variables y tipos ---")
print(producto, type(producto))     # Polo <class 'str'>
print(cantidad, type(cantidad))     # 3 <class 'int'>
print(precio, type(precio))         # 25.9 <class 'float'>
print(es_oferta, type(es_oferta))   # False <class 'bool'>
# type() te dice de qué tipo es una variable. Útil cuando algo falla.


# -------------------------------------------------------------
# 2. INPUT: SIEMPRE DEVUELVE TEXTO
# -------------------------------------------------------------
# input() pide un dato al usuario. Lo que escribas llega como str,
# aunque escribas un número.
#
#   edad = input("Edad: ")     # si escribes 27, edad = "27" (texto)
#
# Para operar con él, hay que convertirlo:
#   int()   -> a entero      int("27")     = 27
#   float() -> a decimal     float("25.9") = 25.9

print("\n--- 2. Por qué hay que convertir ---")
texto = "27"                 # simula lo que devuelve input()
print(texto * 2)             # 2727  -> repite el texto, NO multiplica
print(int(texto) * 2)        # 54    -> ahora sí es un número

# ERROR TÍPICO: int() no acepta decimales.
#   int("25.90")  -> ValueError: invalid literal for int()
# Por eso: precio con float(), cantidad con int().


# -------------------------------------------------------------
# 3. OPERACIONES BÁSICAS
# -------------------------------------------------------------
print("\n--- 3. Operaciones ---")
a = 10
b = 3
print(a + b)    # 13   suma
print(a - b)    # 7    resta
print(a * b)    # 30   multiplicación
print(a / b)    # 3.333...  división normal (siempre da float)
print(a // b)   # 3    división entera (descarta decimales)
print(a % b)    # 1    residuo (sirve para saber si es par: n % 2 == 0)
print(a ** b)   # 1000 potencia


# -------------------------------------------------------------
# 4. CONDICIONALES: if / elif / else
# -------------------------------------------------------------
# Python revisa las condiciones DE ARRIBA HACIA ABAJO
# y se detiene en la PRIMERA que se cumple.
# Reglas de sintaxis:
#   - dos puntos ":" al final de if, elif y else
#   - el bloque de adentro va con 4 espacios de sangría

print("\n--- 4. Condicionales ---")
nota = 15

if nota >= 18:
    print("Excelente")
elif nota >= 11:
    print("Aprobado")       # <- entra aquí, porque 15 >= 11
else:
    print("Desaprobado")

# Comparadores:  ==  igual      !=  distinto
#                >   mayor      <   menor
#                >=  mayor o igual   <= menor o igual
# Combinar condiciones:  and (ambas)   or (alguna)   not (lo contrario)

edad = 20
tiene_dni = True
if edad >= 18 and tiene_dni:
    print("Puede votar")


# -------------------------------------------------------------
# 5. EL ORDEN DE LOS IF IMPORTA
# -------------------------------------------------------------
print("\n--- 5. Orden de las condiciones ---")
subtotal = 250

# MAL: la condición menos exigente va primero
if subtotal > 100:
    print("MAL -> 10% (250 también es > 100, se queda aquí)")
elif subtotal > 200:
    print("MAL -> 15% (nunca llega aquí)")

# BIEN: la más exigente primero
if subtotal > 200:
    print("BIEN -> 15%")
elif subtotal > 100:
    print("BIEN -> 10%")


# -------------------------------------------------------------
# 6. F-STRINGS: MOSTRAR RESULTADOS
# -------------------------------------------------------------
# La f antes de las comillas permite meter variables entre {}.
# :.2f muestra el número con 2 decimales.

print("\n--- 6. f-strings ---")
total = 77.7
print(f"Producto: {producto}")         # Producto: Polo
print(f"Total: S/ {total:.2f}")        # Total: S/ 77.70
print(f"{cantidad} x {precio} = {cantidad * precio:.2f}")  # puedes operar dentro


# -------------------------------------------------------------
# 7. BUENA PRÁCTICA: DRY (Don't Repeat Yourself)
# -------------------------------------------------------------
# Si una línea se repite en cada rama del if, sácala fuera.

print("\n--- 7. DRY ---")
subtotal = 129.50

# En vez de repetir total = subtotal - descuento en cada rama:
if subtotal > 200:
    descuento = subtotal * 0.15
elif subtotal > 100:
    descuento = subtotal * 0.10
else:
    descuento = 0

total = subtotal - descuento          # se calcula UNA sola vez
print(f"Descuento: S/ {descuento:.2f}  Total: S/ {total:.2f}")


# -------------------------------------------------------------
# 8. TERMINAL Y GIT (recordatorio)
# -------------------------------------------------------------
# python carpeta/archivo.py   -> ejecuta un archivo en una subcarpeta
# cd carpeta / cd ..          -> entrar / salir de una carpeta
# git pull                    -> bajar cambios de GitHub (al EMPEZAR)
# git add .                   -> preparar los cambios
# git commit -m "mensaje"     -> guardar una foto en el historial
# git push                    -> subir a GitHub (al TERMINAR)
