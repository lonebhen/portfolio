from django.urls import path

from . import views


urlpatterns=[
    path("",views.home,name='home'),   
    path("home",views.home,name='home'),
    path("resume",views.resume,name='resume'),
    path("portfolio",views.portfolio,name='portfolio'),
    path("contact",views.contact,name='contact')
]