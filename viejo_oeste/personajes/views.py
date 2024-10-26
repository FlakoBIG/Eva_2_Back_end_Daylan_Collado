from django.shortcuts import render
from personajes.Forms import Formvaquero
from personajes.models import vaquero

def index(request):
    return render(request,'index.html')

def lista(request):
    vaqueros = vaquero.objects.all()
    data = {'vaqueros':vaqueros}
    return render(request,'lista.html',data)

def agregar(request):
    form = Formvaquero()
    if request.method == 'POST':
        form = Formvaquero(request.POST)
        if form.is_valid():
            form.save()
            return lista(request)
    data = {'form':form}
    return render(request,'agregar.html',data)

def eliminar(request,id):
    P = vaquero.objects.get(id=id)
    P.delete()
    return lista(request)

def actualizar(request,id):
    P = vaquero.objects.get(id=id)
    form = Formvaquero(instance=P)
    if request.method=='POST':
        form = Formvaquero(request.POST,instance=P)
        if form.is_valid():
            form.save()
            return lista(request)
    data={'form':form}
    return render(request,'modificar.html',data)

