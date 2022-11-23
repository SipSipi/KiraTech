from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Inventory
from .serializer import IventorySerializer


@api_view(['GET'])
def index(request):
    str_name = request.query_params.get("name")
    ls = Inventory.objects.get(name = str_name)
    strReturn =  str(ls.__dict__) 
    return HttpResponse(strReturn)