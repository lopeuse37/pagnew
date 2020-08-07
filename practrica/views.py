from django.shortcuts import render

# Create your views here.
def Inicio (request):
    return render(request,"index.html")

def Acercade (request):
    return render(request,"about.html")

def Contacto  (request):
    return render(request,"contact.html")

def Portafolio (request):
    return render(request,"portafolio.html")
