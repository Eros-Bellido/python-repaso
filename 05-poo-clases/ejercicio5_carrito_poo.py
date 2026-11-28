class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - S/ {self.precio:.2f}"

polo = Producto("Polo",25.6)

print(polo)
print(polo.precio)