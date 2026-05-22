from django.shortcuts import render
from main.models import Course, Trainer
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def courses_page(request):
    all_courses = Course.objects.all() 
    return render(request, 'courses.html', {'courses': all_courses})

def course_details(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course_details.html', {'course': course})

def events(request):
    return render(request, 'events.html')

def pricing(request):
    return render(request, 'pricing.html')

def starter_page(request):
    return render(request, 'starter-page.html')

def trainers(request):
    all_trainers = Trainer.objects.all() 
    return render(request, 'trainers.html', {'trainers': all_trainers})