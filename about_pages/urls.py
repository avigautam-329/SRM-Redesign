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
    url(r"Facts/Ranking/$",views.AboutRanking,name='ranking'),
    url(r"Facts/International-Advisory-Board/$",views.AboutInternationalAdvisory,name='intadvisoryboard'),
    url(r"Facts/StrategicAlliance/$",views.AboutStrategicAlliance,name='stratalliance'),
    url(r"Facts/ForeignFaculty/$",views.AboutForeignFaculty,name='foreignfaculty'),
    url(r"Campus/Our-Campus/$",views.CampusOurCampus,name='ourcampus'),
    url(r"Campus/Buiilding-Details/$",views.CampusBuildingDetails,name='campusbuilddetails'),
    url(r"Campus/Campus-View/$",views.CampusCampusView,name='campusview'),
    url(r"Campus/Student-Services/$",views.CampusStudentServices,name='studservices'),
    url(r"Campus/Sustainability-Cell/$",views.CampusSustainabilityCell,name='suscell'),
    url(r"Accomodation/Welcome-To-SRM-Hostel/$",views.AccomodationWelcomeToSRMHostel,name='accwelcomehostel'),
    url(r"Accomodation/Vision/$",views.AccomodationVision,name='accvision'),
    url(r"Accomodation/Hostel-For-Men/$",views.AccomodationHostelMen,name='acchostelmen'),
    url(r"Accomodation/Hostel-For-Women/$",views.AccomodationHostelWomen,name='acchostelwomen'),
    url(r"Accomodation/Who-Can-Apply/$",views.AccomodationWhoCanApply,name='accwhoapply'),
    url(r"Accomodation/How-And-When-To-Apply/$",views.AccomodationHowAndWhenToApply,name='acchowwhenapply'),
    url(r"Accomodation/Hostel-NCR-Campus/$",views.AccomodationHostelNCR,name='acchostelncr'),
    url(r"Accomodation/Contact-Us/$",views.AccomodationContactUs,name='acccontactus'),
    url(r"Accomodation/International-Hostel/$",views.AccomodationInternationalHostel,name='accinthostel'),
    url(r"Visiting-SRM/About-KTR/$",views.VisitingSRMAboutKTR,name='visitingaboutktr'),
    url(r"Visiting-SRM/By-Rail/$",views.VisitingByRail,name='visitingbyrail'),
    url(r"Visiting-SRM/By-Air/$",views.VisitingByAir,name='visitingbyair'),
    url(r"Visiting-SRM/About-Other-Campuses-Layout/$",views.VisitingAboutOtherCampuses,name='visitingabtothercampuses'),
    url(r"Governance/Public-Interest/$",views.GovernancePublicInterest,name='govpublicinterest'),
    url(r"Governance/Contacts/$",views.GovernanceContacts,name='govcontacts'),
]
