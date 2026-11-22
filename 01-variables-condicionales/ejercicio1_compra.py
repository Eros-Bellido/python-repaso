producto = input("Ingrese producto: ")
precio = float(input("Ingrese precio: "))
cantidad = int(input("Ingrese cantidad: "))

subtotal = precio * cantidad

if subtotal > 200:
    descuento = subtotal * 0.15
elif subtotal > 100:
    descuento = subtotal * 0.10
else:
    descuento = 0

total = subtotal - descuento

print(f"Producto: {producto}")
print(f"Subtotal: S/{subtotal:.2f}")
print(f"Descuento: S/{descuento:.2f}")
print(f"Total: S/{total:.2f}")

