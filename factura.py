class Factura():
    def __init__(self,num_pieza = "",descripcion = "",cantidad = 0,precio = 0):
        self.num_pieza = str(num_pieza)
        self.descripcion = str(descripcion)
        self.cantidad = int(cantidad)
        self.precio = int(precio)
    def establecer(self):
        print("Ingrese la informacion para crear su articulo")
        self.num_pieza = input("Digite el numero de pieza")
        self.descripcion = input("Digite la descripcion del articulo")
        self.cantidad = int(input("Digite la cantidad de existencias del articulo"))
        self.precio = int(input("Digite el precio del articulo"))
        return"Creaste la informacion del articulo con exito"
    def obtener(self):
        return f"\nEl numero de pieza es:{self.num_pieza}\ndescripcion:{self.descripcion}\nla cantidad del articulo es: {self.cantidad}\nel precio del articulo es {self.precio}"
    def obtenerMontoFactura(self):
        if self.cantidad > 0 and self.precio > 0:
            total = self.cantidad * self.precio
            return total
        elif self.cantidad <= 0 and self.precio <= 0:
            self.cantidad = 0
            self.precio = 0
Factura_1 = Factura()
print(f"{Factura_1.establecer()}{Factura_1.obtener()} y el valor del monto de su articulo es: {Factura_1.obtenerMontoFactura()}")


