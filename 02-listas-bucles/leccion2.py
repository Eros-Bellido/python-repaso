# =============================================================
# LECCIÓN 2: Listas, tuplas y bucles
# Ejecuta: python leccion2.py
# =============================================================


# --- 1. LISTAS: colección ordenada y MODIFICABLE --------------
productos = ["Polo", "Short", "Gorra"]

print(productos[0])        # Polo   -> los índices empiezan en 0
print(productos[-1])       # Gorra  -> -1 es el último
print(len(productos))      # 3      -> cantidad de elementos
print(productos[0:2])      # ['Polo', 'Short'] -> slicing, el final NO se incluye

productos.append("Medias")   # agrega al final
productos.remove("Short")    # elimina por valor
productos[0] = "Polera"      # cambia un elemento
print(productos)             # ['Polera', 'Gorra', 'Medias']
print("Gorra" in productos)  # True -> ¿está en la lista?


# --- 2. TUPLAS: como una lista, pero NO se puede modificar -----
# Úsalas para datos fijos que no deben cambiar.
tienda = ("Mi Tienda", "Lima", 2026)
print(tienda[0])             # Mi Tienda
# tienda[0] = "Otra"         # ERROR: las tuplas son inmutables


# --- 3. FOR: recorrer una colección ----------------------------
precios = [25.90, 15.00, 40.50]

for precio in precios:
    print(f"S/ {precio:.2f}")

# enumerate da el índice y el valor a la vez
for i, precio in enumerate(precios, start=1):
    print(f"{i}. S/ {precio:.2f}")     # 1. S/ 25.90 ...


# --- 4. RANGE: repetir N veces ---------------------------------
for n in range(3):           # 0, 1, 2  -> el final NO se incluye
    print(n)

for n in range(1, 6, 2):     # 1, 3, 5  -> (inicio, fin, paso) ejemplo: del 1 al 6, pero de 2 en 2
    print(n)


# --- 5. WHILE: repetir mientras se cumpla una condición --------
intentos = 0
while intentos < 3:
    print(f"Intento {intentos + 1}")
    intentos += 1            # igual a: intentos = intentos + 1

# break sale del bucle; continue salta a la siguiente vuelta
for precio in precios:
    if precio > 30:
        break                # se detiene en 40.50
    print(precio)


# --- 6. FUNCIONES ÚTILES CON LISTAS ----------------------------
print(sum(precios))          # 81.4
print(max(precios))          # 40.5
print(min(precios))          # 15.0
print(sorted(precios))       # ordenada, sin cambiar la original

# --- 7. .index(): ¿en qué posición está un valor? ----------------------------
frutas = ["manzana", "pera", "uva"]
print(frutas.index("pera"))    # 1  -> "pera" está en la posición 1

# =============================================================
# BUENAS PRÁCTICAS
# =============================================================
# - Nombres en plural para listas: productos, precios.
#   En el for, el singular:  for producto in productos
# - Recorre la lista directo, no con range(len()):
#       for precio in precios          <- bien
#       for i in range(len(precios))   <- evitar
#   Si necesitas el índice, usa enumerate().
# - Usa sum(), max(), min() en vez de calcularlos a mano.
# - Lista si los datos cambian; tupla si son fijos.

# =============================================================
# ERRORES COMUNES
# =============================================================
# - IndexError: pedir un índice que no existe (productos[10]).
# - Olvidar que range(5) llega hasta 4, no hasta 5.
# - while infinito: olvidar actualizar la variable (intentos += 1).
# - Borrar elementos de una lista MIENTRAS la recorres con for.