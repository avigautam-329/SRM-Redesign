from django.shortcuts import render

# Create your views here.

def AcademicsDepartments(request):
    return render(request,'academics_pages/academics-departments.html')

def LibraryAbout(request):
    return render(request,'academics_pages/library-about.html')