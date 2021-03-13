from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'about_pages'

urlpatterns = [
    url(r"Facts/SRM-in-focus/$",views.AboutSRMInFocus,name='srminfocus'),
    url(r"Facts/Vision-and-Mission/$",views.AboutVisionandMission,name='visionandmission'),
    url(r"Facts/Core-Values/$",views.AboutCoreValues,name='corevalues'),
    url(r"Facts/Ethics/$",views.AboutEthics,name='ethics'),
    url(r"Facts/History/$",views.AboutHistory,name='history'),
    url(r"Facts/Administration/$",views.AboutAdministration,name='administration'),
    url(r"Facts/Programmes/$",views.AboutProgrammes,name='programmes'),
    url(r"Facts/Research/$",views.AboutResearch,name='research'),
    url(r"Facts/StrategicAlliance/$",views.AboutStrategicAlliance,name='stratalliance'),
    url(r"Facts/ForeignFaculty/$",views.AboutForeignFaculty,name='foreignfaculty'),
    url(r"Campus/Our-Campus/$",views.CampusOurCampus,name='ourcampus'),
    url(r"Campus/Campus-View/$",views.CampusCampusView,name='campusview'),
    url(r"Campus/Student-Services/$",views.CampusStudentServices,name='studservices'),
    url(r"Campus/Sustainability-Cell/$",views.CampusSustainabilityCell,name='suscell'),
]
