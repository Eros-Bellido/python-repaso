import json
from funciones_carrito import calcular_subtotal, calcular_descuento, producto_mas_caro

try:
    with open("carrito.json", "r", encoding="utf-8") as archivo:
        carrito = json.load(archivo)
        print(f"Carrito recuperado con {len(carrito)} productos")
except FileNotFoundError:
    carrito = {}

while True:
    producto = input("Ingrese producto o 'fin' para terminar: ")
    if producto == 'fin':
        break
    elif producto in carrito:
        print("Producto ya registrado")
        continue

    while True:
        try: 
            precio =  float(input("Ingrese precio: "))
            if precio <= 0:
                print("Precio inválido")
                continue
            break
        except ValueError:
            print("No es un dato válido, tiene que ser un número. Ejemplo: 25.8")
    
    carrito[producto] = precio

if len(carrito) == 0:
    print("Carrito vacío")
else:
    subtotal = calcular_subtotal(carrito)
    descuento = calcular_descuento(subtotal)
    total = subtotal - descuento

    for producto, precio in carrito.items():
        print(f"{producto} - S/ {precio:.2f}")

    print(f"Hay {len(carrito)} productos")
    print(f"Producto caro: {producto_mas_caro(carrito)}")
    print(f"Subtotal: S/ {subtotal:.2f}")
    print(f"Descuento: S/ {descuento:.2f}")
    print(f"Total: S/ {total:.2f}")

with open("carrito.json", "w", encoding="utf-8") as archivo:
    json.dump(carrito, archivo, indent=4, ensure_ascii=False)