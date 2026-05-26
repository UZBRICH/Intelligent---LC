from main.forms import RegistrationForm, TestimonialForm
from main.models import Course, Trainer, Testimonial
from django.shortcuts import render, get_object_or_404, redirect
import requests, os




def home(request):
    trainers = Trainer.objects.all()[:3]
    return render(request, 'index.html', {'trainers': trainers})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def courses_page(request):
    all_courses = Course.objects.all() 
    return render(request, 'courses.html', {'courses': all_courses})

def send_telegram(message):
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    requests.post(url, data={
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    })

def test_telegram(request):
    send_telegram("✅ Test xabar! Telegram ishlayapti.")
    return render(request, 'index.html')

def course_details(request, id):
    course = get_object_or_404(Course, id=id)
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.course = course
            registration.save()

            send_telegram(f"""
🎓 <b>Yangi ro'yxatdan o'tish!</b>

👤 <b>Ism:</b> {registration.name}
📞 <b>Telefon:</b> {registration.phone}
📚 <b>Kurs:</b> {course.title}
🏷 <b>Kategoriya:</b> {course.category}
💰 <b>Narx:</b> {course.price} UZS
            """)
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

def about(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    form = TestimonialForm()

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')

    return render(request, 'about.html', {
        'testimonials': testimonials,
        'form': form
    })