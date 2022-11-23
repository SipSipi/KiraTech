from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Inventory,Supplier

def index(response):
    strReturn=''
    ls = Inventory.objects.all()
    for row in ls:
        strReturn += "<p>name :{} supplier:{} availability:{}</p>".format(str(row.name),str(row.supplier),str(row.availability))
    return HttpResponse("<h1>Inventory</h>{}".format(strReturn))

def index3(response,id):
    ls = Inventory.objects.get(id=id)
    values = list(ls.__dict__.values())
    return HttpResponse("<p>{}</p>".format(values))
