class cuenta():
    def __init__(self,titular = "",cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
    def persona_datos(self):
        self.titular = input("Digite el nombre del titular")
        self.cantidad = int(input("Digite la cantidad"))
        return f"El nombre del titular es{self.titular} y la cantidad es {self.cantidad}"
class caja_ahorro(cuenta):
    def __init__(self,titular = "" ,cantidad = 0):
     super().__init__(titular,cantidad)

class plazo_fijo(cuenta):
    def __init__(self,plazo = "" ,interes = 0,titular = "",cantidad = 0):
        self.plazo = plazo
        self.interes = interes
        super().__init__(titular,cantidad)
    def importe_interes(self,importe = 0):
       self.plazo = input("Digite el nombre del titular de plazo") 
       self.interes = int(input("Digite la cantidad del interes"))
       self.cantidad = int(input("Digite la cantidad"))
       self.importe = self.cantidad*self.interes/100
       return "Pudiste obtener con exito el importe del interes"
    def informacion_persona(self):
        return f"el nombre del titular plazo es{self.plazo} el interes que tiene es {self.interes} y el total del interes es {self.importe}"

cuenta_1 = caja_ahorro()
print(f"{cuenta_1.persona_datos()}")
cuenta_2 = plazo_fijo()
print(f"{cuenta_2.importe_interes()} y su informacion personal es: {cuenta_2.informacion_persona()}")