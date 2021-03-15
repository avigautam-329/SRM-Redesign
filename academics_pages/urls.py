from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'academics_pages'

urlpatterns = [
    url(r"Departments/$",views.AcademicsDepartments,name='academicsdep'),
    url(r"Library/About-Library/$",views.LibraryAbout,name='libabt'),
]