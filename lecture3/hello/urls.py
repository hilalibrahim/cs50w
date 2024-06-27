from django.urls import path
from . import views
urlpatterns=[
    path("",views.index,name="index"),
    path("hilal",views.hilal,name="hilal"),
     path("alwin",views.alwin,name="alwin"),
     path("<str:name>",views.greet,name="greet")
]