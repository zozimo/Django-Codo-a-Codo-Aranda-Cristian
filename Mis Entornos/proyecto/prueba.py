from recursos_humanos.nomina import Nomina
from recursos_humanos.personal.empleados import EmpleadoFullTime
from recursos_humanos.personal.estudiantes import EstudiantePasante

Pasante1 = EstudiantePasante("Carlos","Guevara",1235)
Pasante1.salario
print(Pasante1)

nomina = Nomina()
nomina.print()

empleado = EmpleadoFullTime('Mario','Lobo',123333)
nomina.agregar_empleado(empleado)
nomina.print()
