from django.urls import path
from . import views
urlpatterns = [

    path("",views.Inicio),
    path("contact/",views.contact),
    path("about/",views.About),  
]