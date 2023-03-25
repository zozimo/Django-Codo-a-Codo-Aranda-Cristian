from Ejercicio7 import *
from Ejercicio6 import *
            
class CuentaJoven(Cuenta):
    def __init__(self):
        super().__init__()
        self.__bonificacion=30
    @property
    def bonificacion(self):
        return self.__bonificacion
    @bonificacion.setter
    def bonificacion(self,nueva_bonificacion):
        self.__bonificacion = nueva_bonificacion
    def es_titular_valido(self):
        # edad pertenece a persona pero lo puedo llamar con self.edad porque lo herede
        if int(self.edad) > 18 and int(self.edad) < 25:
            print("Sos un titular valido entonces:")
            return True
        else:
            return False
    def retirar(self,cantidad):
        if self.es_titular_valido() == True:
            Cuenta.retirar(self,cantidad)
            
        else:
            print("No cumple con los requisitos de edad y no puede retirar")
    def mostrar(self):
        Cuenta.mostrar(self)
        if self.es_titular_valido() == True:
            print("Usted posse una bonificación de {}%".format(self.__bonificacion))   
        else:
            print("No cumple con los requisitos de edad para la bonificación")
            

ClienteJoven1 = CuentaJoven()
ClienteJoven1.nombre = 'Bob'
ClienteJoven1.apellido = 'Patino'
ClienteJoven1.edad = '19'
ClienteJoven1.dni = '34156156'
ClienteJoven1.ingresar(100)
ClienteJoven1.retirar(10)
ClienteJoven1.mostrar()