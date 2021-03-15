from django.shortcuts import render

# Create your views here.
def CampusLifeArtsAndCulture(request):
    return render(request,'more_pages/campuslife-artsnculture.html')

def CampusLifeAthleticsAndFitness(request):
    return render(request,'more_pages/campuslife-athleticnfitness.html')

def CampusLifeStudentLife(request):
    return render(request,'more_pages/campuslife-studentlife.html')

def CampusLifePublicService(request):
    return render(request,'more_pages/campuslife-publicservice.html')

def CampusCasteDiscrimination(request):
    return render(request,'more_pages/campuslife-caste.html')

def CampusInternationalComplaints(request):
    return render(request,'more_pages/campuslife-intcomplaints.html')

def GroupInstitutions(request):
    return render(request,'more_pages/groupinstitutions.html')

def Announcements(request):
    return render(request,'more_pages/announcements.html')

def News(request):
    return render(request,'more_pages/news.html')

def Events(request):
    return render(request,'more_pages/events.html')