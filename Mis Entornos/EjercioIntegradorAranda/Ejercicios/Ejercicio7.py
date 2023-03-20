class Persona():
    # contructor
    def __init__(self): 
        self.__nombre = ''
        self.__apellido = ''
        self.__edad = ''
        self.__dni = ''
    # def __str__(self) -> str:
    #     return f'{self.__nombre} {self.__apellido}'  
    
    #GETTER
    @property
    def nombre(self):
        return self.__nombre

    #SETTER
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self,nuevo_apellido):
        self.__apellido  = nuevo_apellido
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,nueva_edad):
        self.__edad = nueva_edad
        
    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,nuevo_dni):
        self.__dni = nuevo_dni

    def mostrar(self):
        print("{} {} de {} años, con DNI: {}".format(self.__nombre,self.__apellido,self.__edad,self.__dni))   
    def es_mayor_de_edad(self):
        if int(self.__edad) >=18:
            print("{} {} es mayor de edad".format(self.__nombre,self.__apellido))
        else:
            print("{} {} es menor de edad".format(self.__nombre,self.__apellido))
            
            
class Cuenta(Persona):
    def __init__(self):
        super().__init__()
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
        Persona.mostrar(self)
        # print(" Cliente{} {} con DNI: {}".format(super().__nombre,super().__apellido,super().__dni))   
        print("Su saldo en cuenta es de ${}".format(self.__cantidad)) 
        

Cliente1Cuenta = Cuenta()
Cliente1Cuenta.nombre = 'Bob'
Cliente1Cuenta.apellido = 'Patino'
Cliente1Cuenta.edad = '45'
Cliente1Cuenta.dni = '34156156'
Cliente1Cuenta.ingresar(5.5)
Cliente1Cuenta.retirar(2)
Cliente1Cuenta.mostrar()
Cliente1Cuenta.es_mayor_de_edad()

