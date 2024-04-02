class Coche():
    def __init__(self,num_puertas = 0,matricula = 0,velocidad = 0,cantidad_km = 0):
        self.num_puertas = num_puertas
        self.matricula = matricula
        self.velocidad = velocidad
        self.cantidad_km = cantidad_km
    def to_string(self):
        self.matricula = int(input("Digita tu matricula"))
        self.velocidad = int(input("Digite la velocidad del vehiculo"))
        self.puertas = int(input("Digita el numero de puertas del vehiculo"))
        return f"El numero de tu matricula es {self.matricula} y tu velocidad es de {self.velocidad}"
    def puertas(self):
        return f"su numero de puertas es {self.num_puertas}"

    def acelerar(self):
        self.cantidad_km = int(input("Digita los kilometros por hora para saber si el automovil tiene que acelerar"))
        if self.cantidad_km > 0  and self.cantidad_km <= 120:
            return "El vehiculo se esta acelerando"
        elif  self.cantidad_km < 0:
           return "No se esta acelerando digita una cantidad para acelerar valida"
        else:
           return "No se esta acelerando digita una cantidad para acelerar valida"
class Camion():
    def __init__(self,string = 0,matricula = 0,velocidad = 0,tipo_remolque = None,cantidad_km = 0,):
        self.matricula = matricula
        self.velocidad = velocidad
        self.tipo_remolque = tipo_remolque
        self.cantidad_km = cantidad_km
        super().__init__(string)
    def pon_remolque(self):
        self.tipo_remolque = int(input("Digite 1 para poner un remolque o digite 2 para no poner el remolque"))
        if self.tipo_remolque == 1:
            self.tipo_remolque = "Asignado"
            return "El remolque se a puesto correctamente"
        elif self.tipo_remolque == 2:
            self.tipo_remolque  = None
            return "El remolque no esta en funcionamiento"
        else:
            return "Digite un valor valido"
    def quita_remolque(self):
        if self.tipo_remolque == "Asignado":
            self.tipo_remolque = None
            return "Se a quitado el remolque correctamente"
        else:
            return"El remolque no se puede quitar porque no esta asignado"
    def informacion(self):
        self.matricula = int(input("Digita tu matricula"))
        self.velocidad = int(input("Digita tu velocidad"))
        return f"La matricula del remolque es {self.matricula} su velocidad es de {self.velocidad} y el estado del remolque es {self.tipo_remolque}"
    def acelerar(self):
            self.cantidad_km = int(input("Digite la cantidad de kilometros por hora del vehiculo"))
            if self.cantidad_km <= 0: 
                self.cantidad_km = None
                return "Digita un valor correcto"
            if self.cantidad_km <= 100 and self.tipo_remolque == "Asignado" or self.cantidad_km <= 100 and self.tipo_remolque == None:
                return "La velocidad del vehiculo es la adecuada"
            elif self.cantidad_km > 100 and self.tipo_remolque == None:
                return "La velocidad del vehiculo es adecuada"
            elif self.cantidad_km > 100 and self.tipo_remolque == "Asignado":
                return "El limite seguro de velocidad fue superado"
class remolque():
    def __init__(self,peso = float(input("Digite el peso del remolque"))):
        self.peso = peso
    def to_string(self):
            return f"El peso del remolque es {self.peso}"
            
camion_1 = remolque()
print(camion_1.to_string())
print(camion_1.acelerar())