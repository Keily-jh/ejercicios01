class Vehiculo:
    def __init__(self, Marca, Modelo, velocidad_máxima):
        self.Marca = Marca
        self.Modelo = Modelo
        self.velocidad_máxima = velocidad_máxima 
    def __str__(self):
        return f'Vehiculo => Marca: {self.Marca}, Modelo: {self.Modelo}, velocidad_máxima: {self.velocidad_máxima}'

class Automóvil(Vehiculo):
    def __init__(self, Marca, Modelo, velocidad_máxima, numero_puertas):
        super().__init__(Marca, Modelo, velocidad_máxima)
        self.numero_puertas = numero_puertas
    def __str__(self):
        return f'Automóvil => Marca: {self.Marca}, Modelo: {self.Modelo}, velocidad_máxima: {self.velocidad_máxima}, numero_puertas: {self.numero_puertas}'
class Motocicleta(Vehiculo):
    def __init__(self, Marca, Modelo, velocidad_máxima, Tipo):
        super().__init__(Marca, Modelo, velocidad_máxima)
        self.Tipo = Tipo
    def __str__(self):
        return f'Vehiculo => Marca: {self.Marca}, Modelo: {self.Modelo}, velocidad_máxima: {self.velocidad_máxima, Tipo: {Tipo}}'


