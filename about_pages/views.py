from django.shortcuts import render

# Create your views here.
def AboutSRMInFocus(request):
    return render(request,'about_pages/about-srminfocus.html')

def AboutVisionandMission(request):
    return render(request,'about_pages/about-visionandmission.html')

def AboutCoreValues(request):
    return render(request,'about_pages/about-corevalues.html')
    
def AboutEthics(request):
    return render(request,'about_pages/about-ethics.html')

def AboutHistory(request):
    return render(request,'about_pages/about-history.html')

def AboutAdministration(request):
    return render(request,'about_pages/about-administration.html')

def AboutProgrammes(request):
    return render(request,'about_pages/about-programs.html')

def AboutResearch(request):
    return render(request,'about_pages/about-research.html')

def AboutStrategicAlliance(request):
    return render(request,'about_pages/about-strategicalliance.html')

def AboutForeignFaculty(request):
    return render(request,'about_pages/about-foreignfaculty.html')

def CampusOurCampus(request):
    return render(request,'about_pages/campus-ourcampus.html')

def CampusCampusView(request):
    return render(request,'about_pages/campus-campusview.html')

def CampusStudentServices(request):
    return render(request,'about_pages/campus-studentservices.html')

def CampusSustainabilityCell(request):
    return render(request,'about_pages/campus-sustainabilitycell.html')