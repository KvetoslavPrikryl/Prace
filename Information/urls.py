from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.singIn, name = "singIn"),
    path("logOut", views.logOut, name="logOut"),
    #path("singUp", views.singUp, name="singUp"),
    path("uvod", views.index, name= "index"),
    path("info", views.information, name="info"),
    path("novy", views.newEmployee, name = "new"),
    path("skoleni", views.newTrained, name= "trained"),    
    path("vymazat_zamestnance", views.deteteEmployee, name= "delete"),
    path("vymazat_skoleni", views.deleteTrained, name="deleteTrained" )
]