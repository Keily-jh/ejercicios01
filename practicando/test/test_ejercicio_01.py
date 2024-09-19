import unittest
from practicando.ejercicio_01 import Vehiculo, Automóvil, Motocicleta

class Testvehiculo(unittest.TestCase):
    def test_propiedades_vehiculo(self):
        ve1 = Vehiculo('Porche', 'g34', 334)
        self.assertEqual(ve1.__str__(), 'Vehiculo => Marca: Porche, Modelo: g34, velocidad_máxima: 334')
    def test_propiedades_automovil(self):
        auto1 = Automóvil('Jeep', 'Rubicon', 122, 4)
        self.assertEqual(auto1.__str__(), 'Automóvil => Marca: Jeep, Modelo: Rubicon, velocidad_máxima: 122, numero_puertas: 4')
    def test_propiedades_moto(self):
        moto1 = Motocicleta('Honda', 'civic', 78, 'Deportiva')

if __name__ == '__main__':
 unittest.main() 

