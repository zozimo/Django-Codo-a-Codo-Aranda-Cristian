from Ejercicio7 import *
from Ejercicio6 import *
class CuentaJoven(Cuenta):
    def __init__(self, titular):
        super().__init__(titular)
        self.__bonificacion=30
    @property
    def bonificacion(self):
        return self.__bonificacion
    @bonificacion.setter
    def bonificacion(self,nueva_bonificacion):
        self.__bonificacion = nueva_bonificacion
    def es_titular_valido(self):
        # edad pertenece a persona pero lo puedo llamar con self.edad porque lo herede
        if int(self.titular.edad) > 18 and int(self.titular.edad) < 25:
            print("Sos un titular valido entonces:")
            return True
        else:
            return False
    def retirar(self,cantidad):
        if self.es_titular_valido() == True:
            super().retirar(cantidad) # Llamo al metodo de la clase padre entonces no hace falta poner self
            
        else:
            print("No cumple con los requisitos de edad y no puede retirar")
    def mostrar(self):
        Cuenta.mostrar(self)
        if self.es_titular_valido() == True:
            print("Usted posse una bonificación de {}%".format(self.__bonificacion))   
        else:
            print("No cumple con los requisitos de edad para la bonificación")
            
persona1 = Persona()
persona1.nombre = 'Cristian'
persona1.apellido = 'Aranda'
persona1.edad = '24'
persona1.dni = '34156156'
# persona1.mostrar()
cuentaJoven1 = CuentaJoven(persona1)
cuentaJoven1.ingresar(100000)
cuentaJoven1.retirar(100123)
cuentaJoven1.mostrar()
# cuenta1.titular.es_mayor_de_edad()