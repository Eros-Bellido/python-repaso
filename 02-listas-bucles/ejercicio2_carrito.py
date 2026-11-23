productos = []
precios = []

while True:
    producto = input("Ingrese producto o 'fin' para terminar: ")
    if producto == 'fin':
        break 
    precio = float(input("Ingrese precio: "))
    productos.append(producto)
    precios.append(precio)

subtotal = sum(precios)
if subtotal > 200:
    descuento = subtotal * 0.15
elif subtotal > 100:
    descuento = subtotal * 0.10
else:
    descuento = 0

total = subtotal - descuento

for i, precio in enumerate(precios, start = 1):
    print(f"{i}. {productos[i-1]} - S/{precio:.2f}")

print(f"Hay {len(productos)} productos")

print(f"Producto más caro: S/ {max(precios):.2f}")

print(f"Subtotal: S/ {subtotal:.2f}")

print(f"Descuento: S/ {descuento:.2f}")

print(f"Total: S/ {total:.2f}")

