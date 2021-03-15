from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'foryou_pages'

urlpatterns = [
    url(r"Faculty/$",views.Faculty,name='faculty'),
    url(r"Student/Gateway-For-Students/$",views.StudentGateway,name='studgateway'),
    url(r"Student/Feekart/$",views.StudentFeekart,name='studfeekart'),
    url(r"Student/Examinations/$",views.StudentExaminations,name='studexaminations'),
    url(r"Student/SRM-Bio-Info/$",views.StudentBioInfo,name='studbioinfo'),
    url(r"Student/Academics/$",views.StudentAcademics,name='studacademics'),
    url(r"Student/Twining-Dual-Degree/$",views.StudentTwining,name='studtwining'),
    url(r"Student/Placements/$",views.StudentPlacements,name='studplacements'),
    url(r"Student/Scholarship/$",views.StudentScholarship,name='studscholarship'),
    url(r"Student/Events-And-Clubs/$",views.StudentEventsAndClubs,name='studevents'),
    url(r"Student/Achievements/$",views.StudentAchievements,name='studachievements'),
    url(r"Student/Life-On-Campus/$",views.StudentAchievements,name='studlifeoncampus'),
    url(r"Student/Center-For-Skill-Development/$",views.StudentCenterForSkillDevelopment,name='studskilldev'),
    url(r"Visit/$",views.Visit,name='visit'),
]
