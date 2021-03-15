from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'more_pages'

urlpatterns=[
    url(r"Campus-Life/Arts-And-Culture/$",views.CampusLifeArtsAndCulture,name='campartsnculture'),
    url(r"Campus-Life/Athletics-And-Fitness/$",views.CampusLifeAthleticsAndFitness,name='campathleticsnfitness'),
    url(r"Campus-Life/Student-Life/$",views.CampusLifeStudentLife,name='campstudentlife'),
    url(r"Campus-Life/Public-Service/$",views.CampusLifePublicService,name='camppublicservice'),
    url(r"Campus-Life/Caste-Discrimination/$",views.CampusCasteDiscrimination,name='campcaste'),
    url(r"Campus-Life/International-Complaints/$",views.CampusInternationalComplaints,name='campintcomplaints'),
    url(r"Group-Institutions/All-Campuses/$",views.GroupInstitutions,name='grpinstitutions'),
    url(r"Announcements/$",views.Announcements,name='announcements'),
    url(r"News/$",views.News,name='news'),
    url(r"Events/$",views.Events,name='events'),
]