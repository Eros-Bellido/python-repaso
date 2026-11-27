# =============================================================
# LECCIÓN 5: POO 1 - Clases, objetos, atributos y métodos
# Ejecuta: python leccion5.py
# =============================================================


# --- 1. CLASE Y OBJETO -----------------------------------------
# Clase  = el molde (la definición).  Ej: "Producto"
# Objeto = algo hecho con el molde.    Ej: un Polo de S/ 25.90
#
# Hasta ahora usabas diccionarios: {"nombre": "Polo", "precio": 25.90}
# Una clase junta los DATOS y las ACCIONES sobre esos datos.

class Producto:                         # nombre de clase en PascalCase
    def __init__(self, nombre, precio):  # se ejecuta al CREAR el objeto
        self.nombre = nombre            # atributos: datos del objeto
        self.precio = precio

    def aplicar_descuento(self, porcentaje):   # método: una acción
        self.precio = self.precio * (1 - porcentaje)

    def __str__(self):                  # cómo se ve al hacer print()
        return f"{self.nombre} - S/ {self.precio:.2f}"


polo = Producto("Polo", 25.90)          # crear un objeto (llama a __init__)
gorra = Producto("Gorra", 80.00)        # otro objeto, con SUS propios datos

print(polo.nombre)                      # Polo  -> acceder a un atributo
print(gorra)                            # Gorra - S/ 80.00 (usa __str__)
gorra.aplicar_descuento(0.10)           # llamar a un método
print(gorra)                            # Gorra - S/ 72.00
print(polo)                             # Polo - S/ 25.90 (no cambió)


# --- 2. ¿QUÉ ES self? ------------------------------------------
# self = "este objeto". Cuando haces gorra.aplicar_descuento(0.10),
# Python lo convierte en: Producto.aplicar_descuento(gorra, 0.10)
# Por eso self va primero en cada método, pero NO lo escribes al llamar.
# Sin self.precio, el método no sabría DE QUÉ objeto es el precio.


# --- 3. UNA CLASE QUE GUARDA OTROS OBJETOS ---------------------
class Carrito:
    def __init__(self):
        self.productos = {}             # atributo que empieza vacío
                                        # clave: nombre, valor: objeto Producto

    def agregar(self, producto):
        if producto.nombre in self.productos:
            return False                # avisa que no se agregó
        self.productos[producto.nombre] = producto
        return True

    def subtotal(self):
        return sum(p.precio for p in self.productos.values())
        # equivale a: total = 0; for p in ...: total += p.precio

    def descuento(self):
        sub = self.subtotal()           # un método puede llamar a OTRO con self.
        if sub > 200:
            return sub * 0.15
        elif sub > 100:
            return sub * 0.10
        return 0

    def cantidad(self):
        return len(self.productos)


carrito = Carrito()
print(carrito.agregar(Producto("Polo", 25.90)))    # True
print(carrito.agregar(Producto("Polo", 30.00)))    # False -> repetido
carrito.agregar(Producto("Short", 90.00))

for producto in carrito.productos.values():        # recorre los OBJETOS
    print(producto)                                # usa __str__
print(f"Productos: {carrito.cantidad()}")          # 2
print(f"Subtotal: S/ {carrito.subtotal():.2f}")    # S/ 115.90
print(f"Descuento: S/ {carrito.descuento():.2f}")  # S/ 11.59


# =============================================================
# BUENAS PRÁCTICAS
# =============================================================
# - Clases en PascalCase (Producto, Carrito); métodos y atributos en snake_case.
# - Una clase = un concepto. Producto no calcula descuentos del carrito.
# - Los atributos se crean en __init__, aunque empiecen vacíos.
# - Métodos que calculan RETORNAN; los print van fuera de la clase.
# - Define __str__ para que tus objetos se vean bien al imprimirlos.

# =============================================================
# ERRORES COMUNES
# =============================================================
# - Olvidar self como primer parámetro del método -> TypeError.
# - Escribir precio en vez de self.precio dentro del método -> NameError.
# - Olvidar los () al llamar: carrito.subtotal  (sin paréntesis no se ejecuta).
# - Escribir _init_ con un solo guion bajo: son DOS a cada lado: __init__.
# - Crear el objeto sin los datos que pide __init__: Producto() -> TypeError.