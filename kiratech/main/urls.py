from django.urls import path
from . import views

urlpatterns = [
    path("inventory/",views.index),
    path("inventory/<int:id>",views.index3,name='int'),
]