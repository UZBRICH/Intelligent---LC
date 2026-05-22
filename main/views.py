from django.shortcuts import render, redirect
from main.models import Course, Trainer
from django.shortcuts import get_object_or_404
from .forms import RegistrationForm
from django.core.mail import send_mail
from django.conf import settings



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
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.course = course
            registration.save()

            send_mail(
                subject=f"Yangi ro'yxatdan o'tish: {course.title}",
                message=f"""
Yangi o'quvchi ro'yxatdan o'tdi!

Ismi: {registration.name}
Telefon: {registration.phone}
Kurs: {course.title}
Kategoriya: {course.category}
Narx: {course.price} UZS
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            return redirect('registration_success')

    return render(request, 'course_details.html', {'course': course, 'form': form})


def registration_success(request):
    return render(request, 'registration_success.html')

def events(request):
    return render(request, 'events.html')

def pricing(request):
    return render(request, 'pricing.html')

def starter_page(request):
    return render(request, 'starter-page.html')

def trainers(request):
    all_trainers = Trainer.objects.all() 
    return render(request, 'trainers.html', {'trainers': all_trainers})