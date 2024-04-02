class Calcular():
    def __init__(self,peso,altura):
        self.peso = peso
        self.altura = altura    
    def calcular_imc(self,peso = 0,altura = 0):
        self.peso = float(input("Digita tu peso"))
        self.altura = float(input("Digite su altura"))
        imc = self.peso/self.altura**2
        if imc < 20:
            imc = -1
            print("Estas en un peso ideal")
        elif imc >= 20 and imc <= 25:
            imc = 0
            print("Estas por debajo de tu peso ideal")
        else:
            imc = 1
            print("Tienes sobrepeso")
        return f"Este es el resultado del imc {imc}"


class Edad(): 
    def __init__(self,estado_edad = False,edad = 0):
            self.estado_edad = estado_edad
            self.edad = edad
    def es_mayor(self):
        self.edad = int(input("Digita tu edad"))     
        if self.edad >= 18:
            self.estado_edad = True
            print("La persona es mayor de edad")
        else:
            self.estado_edad = False
            print("La persona es menor de edad")
        return f"Este es el resultado de la edad {self.estado_edad}"
    
class Sexo():
    def __init__(self,sexo = ""):
        self.sexo = sexo
    def comprobrar(self):
            self.sexo = input("Digite su sexo").strip()
            if self.sexo  ==  "Hombre":
                self.sexo = "Hombre"
                
            elif self.sexo == "Mujer":
                self.sexo = "Mujer"
                
            else:
                self.sexo = "H"
            return f"Este es el resultado del sexo {self.sexo}"
            
class Datos():
    def __init__(self,nombre = "",edad = 0,sexo = "",peso = 0,altura = 0,dni = 0):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
    def string(self):
        self.nombre = input("Digita tu nombre")
        self.dni = input("Digita tu dni")
        info = f"El nombre de la persona es{self.nombre} su edad es {self.edad} su sexo es {self.sexo} la altura es {self.altura} su peso es {self.peso} y su dni es  {self.dni}"
        return info


class Persona(Calcular,Edad,Sexo,Datos):
    def __init__(self,nombre = "",edad = 0,sexo = "",peso = 0,altura = 0,dni = 0):
        pass
persona_2 = Persona()
print(f"{persona_2.es_mayor()} {persona_2.comprobrar()} {persona_2.calcular_imc()}")
print(f"{persona_2.string()}")