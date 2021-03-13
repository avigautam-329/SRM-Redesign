from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'about_pages'

urlpatterns = [
    url(r"SRM-in-focus/$",views.AboutSRMInFocus,name='srminfocus'),
    url(r"Vision-and-Mission/$",views.AboutVisionandMission,name='visionandmission'),
    url(r"Core-Values/$",views.AboutCoreValues,name='corevalues'),
    url(r"Ethics/$",views.AboutEthics,name='ethics'),
    url(r"History/$",views.AboutHistory,name='history'),
    url(r"Administration/$",views.AboutAdministration,name='administration'),
    url(r"Programmes/$",views.AboutProgrammes,name='programmes'),
    url(r"Research/$",views.AboutResearch,name='research'),
    url(r"StrategicAlliance/$",views.AboutStrategicAlliance,name='stratalliance'),
    url(r"ForeignFaculty/$",views.AboutForeignFaculty,name='foreignfaculty'),
    url(r"Campus/Our-Campus/$",views.CampusOurCampus,name='ourcampus'),
    url(r"Campus/Campus-View/$",views.CampusCampusView,name='campusview'),
    url(r"Campus/Student-Services/$",views.CampusStudentServices,name='studservices'),
    url(r"Campus/Sustainability-Cell/$",views.CampusSustainabilityCell,name='suscell'),
]
