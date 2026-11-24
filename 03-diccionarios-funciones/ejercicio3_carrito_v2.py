carrito = {}

def calcular_subtotal(carrito):
    return sum(carrito.values())

def calcular_descuento(subtotal):
    if subtotal > 200:
        return subtotal * 0.15
    elif subtotal > 100:
        return subtotal * 0.10
    return 0

def producto_mas_caro(carrito):
    caro = 0
    nombre_caro = ""
    for producto, precio in carrito.items():
        if precio > caro:
            caro = precio
            nombre_caro = producto

    return nombre_caro 

subtotal = calcular_subtotal(carrito)
descuento = calcular_descuento(subtotal)
total = subtotal - descuento

while True:
    producto = input("Ingrese producto o 'fin' para terminar: ")
    if producto == 'fin':
        break
    elif producto in carrito:
        print("Producto ya registrado")
        continue
    precio =  float(input("Ingrese precio: "))
    carrito[producto] = precio

if len(carrito) == 0:
    print("Carrito vacío")
else:
    for producto, precio in carrito.items():
        print(f"{producto} - S/ {precio:.2f}")

    print(f"Hay {len(carrito)} productos")
    print(f"Producto caro: {producto_mas_caro(carrito)}")
    print(f"Subtotal: S/ {subtotal:.2f}")
    print(f"Descuento: S/ {descuento:.2f}")
    print(f"Total: S/ {total:.2f}")