class Vehiculo:
    def __init__(self, Marca, Modelo, velocidad_máxima):
        self.Marca = Marca
        self.Modelo = Modelo
        self.velocidad_máxima = velocidad_máxima 
    def detalles(self):
        return f'Vehiculo => Marca: {self.Marca}, Modelo: {self.Modelo}, velocidad_máxima: {self.velocidad_máxima}'

class Automóvil(Vehiculo):
    def __init__(self, Marca, Modelo, velocidad_máxima, numero_puertas):
        super().__init__(self. Marca, Modelo, velocidad_máxima)
        self.numero_puertas = numero_puertas
    def detalles(self):
        return f'Vehiculo => Marca: {self.Marca}, Modelo: {self.Modelo}, velocidad_máxima: {self.velocidad_máxima, Número de puertas: {numero_puertas}}'

class Motocicleta(Vehiculo):
    def __init__(self, Marca, Modelo, velocidad_máxima, Tipo):
        super().__init__(self. Marca, Modelo, velocidad_máxima)
        self.Tipo = Tipo
    def detalles(self):
        return f'Vehiculo => Marca: {self.Marca}, Modelo: {self.Modelo}, velocidad_máxima: {self.velocidad_máxima, Tipo: {Tipo}}'


