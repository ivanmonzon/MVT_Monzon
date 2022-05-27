from django.http import HttpResponse
from django.template import loader
from AppMyFamily.models import Familia
# Create your views here.

def familia(self):
   
    familiar1 = Familia(nombre="Ramón", edad=40, fechaDeNacimiento="1982-11-11")
    familiar1.save()
    familiar2 = Familia(nombre="Pepe", edad=45, fechaDeNacimiento="1957-11-11")
    familiar2.save()
    familiar3 = Familia(nombre="Susana", edad=30, fechaDeNacimiento="1992-11-11")
    familiar3.save()
    
    documentoDeTexto1= f"Nombre del padre: {familiar1.nombre} Edad: {familiar1.edad} Fecha de nacimiento: {familiar1.fechaDeNacimiento}" 
    documentoDeTexto2= f"Nombre del hijo: {familiar2.nombre} Edad: {familiar2.edad} Fecha de nacimiento: {familiar2.fechaDeNacimiento}" 
    documentoDeTexto3= f"Nombre del espíritu santo: {familiar3.nombre} Edad: {familiar3.edad} Fecha de nacimiento: {familiar3.fechaDeNacimiento}"
    
    diccionario= {"Familiar1": documentoDeTexto1,"Familiar2": documentoDeTexto2,"Familiar3": documentoDeTexto3}
    template= loader.get_template("template.html")
    documento=template.render(diccionario)
    return HttpResponse(documento)



        