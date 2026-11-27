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