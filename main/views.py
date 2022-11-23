from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Inventory,Supplier

def index(response):
    try:
        strReturn=''
        ls = Inventory.objects.all()
        for row in ls:
            strReturn += "<p>name :{} supplier:{} availability:{}</p>".format(str(row.name),str(row.supplier),str(row.availability))
        return HttpResponse("<h1>Inventory</h>{}".format(strReturn))
    except Exception as e:
        return HttpResponse(str(e))
        
def index3(response,id):
    try:
        ls = Inventory.objects.get(id=id)
        values = list(ls.__dict__.values())
        return HttpResponse("<p>{}</p>".format(values))
    except Exception as e:
        return HttpResponse(str(e))