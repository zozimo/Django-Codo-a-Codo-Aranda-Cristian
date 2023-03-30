from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context, loader
from django.template.loader import get_template
from django.shortcuts import render
import datetime
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.

def saludo(request):
    return HttpResponse("Hola a todos!")
def saludo_html(request):
    documento="""<html><body><h1>Hola a todos!</h1></body></html>"""
    return HttpResponse(documento)
def despedida(request):
    return HttpResponse("Hasta luego!")
def get_fecha(request):
        fecha_actual = datetime.datetime.now()
        documento = """<html><body><h1>Fecha: %s</h1></body></html>"""%fecha_actual
        return HttpResponse(documento)
def calcular_edad(request,edad,agno):
    periodo = agno-2023
    edad_futura = edad + periodo
    documento = "<html><body><h2>En el año %s tendrás %s años"%(agno,edad_futura)
    return HttpResponse(documento)
def saludo_desde_template(request):
    # os.path.join(os.getcwd(),RutaExcel+'\DatosCalibracion'+ Marca + titulo)
      
    arch = open("C:/Users/caranda/Desktop/Repositorios/Django-Codo-a-Codo-Aranda-Cristian/Mis Entornos/proyectoDjango/templates/plantilla.html")
    # arch = open("C:\Users\caranda\Desktop\Repositorios\Django-Codo-a-Codo-Aranda-Cristian\Mis Entornos\proyectoDjango\templates\plantilla.html")
    # 'C:\\Users\\caranda\\Desktop\\Repositorios\\Django-Codo-a-Codo-Aranda-Cristian'
    plt = Template(arch.read())
    arch.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)
def paso_var_de_view_a_plantilla(request):
    nombre = "Juan"
    apellido = "Gonzalez"
    fecha = datetime.datetime.now()
    arch = open("C:/Users/caranda/Desktop/Repositorios/Django-Codo-a-Codo-Aranda-Cristian/Mis Entornos/proyectoDjango/templates/plantilla.html")
    plt = Template(arch.read())
    arch.close()
    # ctx = Context({"nombre_persona":nombre, "apellido_persona": apellido, "now":fecha})
    # tambien puedo pasar el valor directamente en el contexto
    ctx = Context({"nombre_persona":"Pedro", "apellido_persona": "Escamoso", "now":fecha})
    documento = plt.render(ctx)
    return HttpResponse(documento   )
    
def lista_iter_plantilla(request):
    temas = ["Plantillas","Modelos","Formularios","Vistas"]
    # arch = open(os.path.join(BASE_DIR,'Mis Entornos/proyectoDjango/templates/plantilla2.html'))
    arch = open("C:/Users/caranda/Desktop/Repositorios/Django-Codo-a-Codo-Aranda-Cristian/Mis Entornos/proyectoDjango/templates/plantilla2.html")
    plt = Template(arch.read())
    arch.close()
    ctx = Context({"temas_curso":temas})
    documento = plt.render(ctx)
    return HttpResponse(documento)
    
def lista_iter_plantilla_simplex(request):
    temas = ["Plantillas","Modelos","Formularios","Vistas"]
    # arch = open(os.path.join(BASE_DIR,'Mis Entornos/proyectoDjango/templates/plantilla2.html'))
    return render(request,"plantilla2.html",{"temas_curso":temas})

def curso(request):
    fecha = datetime.datetime.now()
    return render(request,"superior/curso.html",{"now":fecha})
# ruta = saludo_desde_template()

