from django.shortcuts import render,redirect
from .models import*

def HOME(request):
    tas = TODO.objects.all()
    if request.method == "POST":
        if 'tasub' in request.POST:
            c = request.POST
            tnam = c['nam']
            ttask = c['tas']
            tdat = c['dat']
            TODO.objects.create(task=ttask,task_name=tnam,last_date=tdat)
            return redirect('home')
    d = {"tas":tas}
    return render(request,'index.html',d)

def TASK_DELETE(request,del_id):
    TODO.objects.get(id=del_id).delete()
    return redirect('home')

def TASK_UPDATE(request,tas_id):
    if request.method == "POST":
        if 'tasub' in request.POST:
            c = request.POST
            tnam = c['nam']
            ttask = c['tas']
            tdat = c['dat']
            blosi = TODO.objects.filter(id=tas_id)
            blosi.update(task=ttask,task_name=tnam,last_date=tdat)
            return redirect('home')
    tas = TODO.objects.all()
    blosingle = TODO.objects.get(id=tas_id)
    d = {"blosingle":blosingle,"tas":tas}
    return render(request, 'task_dynamic.html',d)