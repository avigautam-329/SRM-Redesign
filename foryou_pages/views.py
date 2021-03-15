from django.shortcuts import render

# Create your views here.

def Faculty(request):
    return render(request,'foryou_pages/faculty.html')

def StudentGateway(request):
    return render(request,'foryou_pages/student-gateway.html')

def StudentFeekart(request):
    return render(request,'foryou_pages/student-feekart.html')

def StudentExaminations(request):
    return render(request,'foryou_pages/student-examinations.html')

def StudentBioInfo(request):
    return render(request,'foryou_pages/student-srmbio.html')

def StudentAcademics(request):
    return render(request,'foryou_pages/student-academics.html')

def StudentTwining(request):
    return render(request,'foryou_pages/student-twining.html')

def StudentPlacements(request):
    return render(request,'foryou_pages/student-placement.html')

def StudentScholarship(request):
    return render(request,'foryou_pages/student-scholarship.html')

def StudentEventsAndClubs(request):
    return render(request,'foryou_pages/student-events.html')

def StudentAchievements(request):
    return render(request,'foryou_pages/student-achievements.html')

def StudentLifeOnCampus(request):
    return render(request,'foryou_pages/student-lifeoncampus.html')

def StudentCenterForSkillDevelopment(request):
    return render(request,'foryou_pages/student-skilldev.html')

def Visit(request):
    return render(request,'foryou_pages/visit.html')