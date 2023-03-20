from abc import ABC, abstractmethod

class Persona():
    # contructor
    def __init__(self, nombre, apellido, edad, dni): 
        self.__nombre = nombre
        self.__apellido = apellido    
        self.__edad = edad
        self.__dni = dni
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
            
nueva_persona = Persona("","","","")
nueva_persona.nombre = 'Cristian'
nueva_persona.apellido = 'Aranda'
nueva_persona.edad = '17'
nueva_persona.dni = '34156156'
nueva_persona.mostrar()
nueva_persona.es_mayor_de_edad()
