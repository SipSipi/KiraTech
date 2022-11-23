from django.urls import path
from . import views

urlpatterns = [
    path("api/inventory",views.index,name="api")
]