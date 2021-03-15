from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'foryou_pages'

urlpatterns = [
    url(r"Faculty/$",views.Faculty,name='faculty')
]
