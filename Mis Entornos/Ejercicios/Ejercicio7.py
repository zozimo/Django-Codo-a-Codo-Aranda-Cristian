from Ejercicio6 import *           
            
class Cuenta():
    def __init__(self,titular):
        self.titular = titular
        self.__cantidad = 0.0
    @property
    def cantidad(self):
        return self.__cantidad
# @cantidad.setter
# def cantidad(self,nuevo_cantidad):
#     self.__cantidad = self.__cantidad + nuevo_cantidad
    def ingresar(self,cantidad):
        self.__cantidad = self.__cantidad + cantidad
        print("Usted a ingresado ${}".format(cantidad))   
    def retirar(self,cantidad):
        self.__cantidad = self.__cantidad - cantidad
        print("Usted a retirado ${}".format(cantidad))   
    def mostrar(self):
        self.titular.mostrar()
        # print(" Cliente{} {} con DNI: {}".format(super().__nombre,super().__apellido,super().__dni))   
        print("Su saldo en cuenta es de ${}".format(self.__cantidad)) 
        

# persona1 = Persona()
# persona1.nombre = 'Cristian'
# persona1.apellido = 'Aranda'
# persona1.edad = '25'
# persona1.dni = '34156156'
# # persona1.mostrar()
# cuenta1 = Cuenta(persona1)
# cuenta1.ingresar(100000)
# cuenta1.retirar(602)
# cuenta1.mostrar()
# cuenta1.titular.es_mayor_de_edad()



