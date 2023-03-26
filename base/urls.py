from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns=[
    path("",views.home,name='home'),   
    path("home",views.home,name='home'),
    path("resume",views.resume,name='resume'),
    path("portfolio",views.portfolio,name='portfolio'),
    path("contact",views.contact,name='contact'),
    path("send_email",views.send_email,name='send_email')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)