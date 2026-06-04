from main.forms import RegistrationForm, TestimonialForm
from main.models import Course, Trainer, Testimonial, Event
from django.shortcuts import render, get_object_or_404, redirect
import requests, os
from django.db.models import Avg




def home(request):
    trainers = Trainer.objects.all()[:3]
    return render(request, 'index.html', {'trainers': trainers})

def contact(request):
    return render(request, 'contact.html')

def courses_page(request):
    categories = ['English', 'Russian', 'Uzbek', 'Mathematics']
    grouped_courses = {}
    for category in categories:
        courses = Course.objects.filter(category=category)
        if courses.exists():
            grouped_courses[category] = courses
    return render(request, 'courses.html', {'grouped_courses': grouped_courses})

def send_telegram(message):
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    chat_id = os.environ.get('TELEGRAM_CHAT_ID')
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    requests.post(url, data={
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    })

def get_telegram_posts():
    token = os.environ.get('8757295120:AAFtTQDSQrdSnaLn9nc0Oo1_v1Uo7bFXGZU')
    channel = 'Intelligent_LC'
    try:
        url = f'https://api.telegram.org/bot{token}/getUpdates'
        url = f'https://api.telegram.org/bot{token}/forwardMessage'
        response = requests.get(
            f'https://api.telegram.org/bot{token}/getUpdates',
            params={'limit': 10, 'allowed_updates': ['channel_post']}
        )
        data = response.json()
        posts = []
        if data.get('ok'):
            for update in data.get('result', []):
                post = update.get('channel_post', {})
                if post and post.get('chat', {}).get('username') == channel.strip('@'):
                    posts.append({
                        'text': post.get('text', ''),
                        'date': post.get('date', 0),
                    })
        return posts[:6]
    except:
        return []
    
def get_latest_telegram_post():
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    try:
        response = requests.get(
            f'https://api.telegram.org/bot{token}/getUpdates',
            params={'limit': 1, 'allowed_updates': ['channel_post']}
        )
        data = response.json()
        if data.get('ok') and data.get('result'):
            for update in reversed(data['result']):
                post = update.get('channel_post', {})
                if post:
                    return post.get('message_id')
    except:
        pass
    return 693

def events(request):
    manual_events = Event.objects.all().order_by('-date')
    latest_post_id = get_latest_telegram_post()
    return render(request, 'events.html', {
        'manual_events': manual_events,
        'latest_post_id': latest_post_id,
    })

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
    from main.models import Event
    manual_events = Event.objects.all().order_by('-date')
    return render(request, 'events.html', {
        'manual_events': manual_events,
    })

def pricing(request):
    beginner_courses = Course.objects.filter(
        title__icontains='Beginner'
    ) | Course.objects.filter(
        title__icontains='Kids'
    ) | Course.objects.filter(
        title__icontains='Elementary'
    )

    intermediate_courses = Course.objects.filter(
        title__icontains='Intermediate'
    ) | Course.objects.filter(
        title__icontains='Upper'
    ) | Course.objects.filter(
        title__icontains='Advanced'
    ) | Course.objects.filter(
        title__icontains='Conversation'
    )

    exam_courses = Course.objects.filter(
        title__icontains='IELTS'
    ) | Course.objects.filter(
        title__icontains='CEFR'
    ) | Course.objects.filter(
        title__icontains='SAT'
    ) | Course.objects.filter(
        title__icontains='Certificate'
    ) | Course.objects.filter(
        title__icontains='National'
    )

    premium_courses = Course.objects.filter(
        title__icontains='Intensive'
    ) | Course.objects.filter(
        title__icontains='Individual'
    ) | Course.objects.filter(
        title__icontains='Premium'
    ) | Course.objects.filter(
        title__icontains='VIP'
    )

    return render(request, 'pricing.html', {
        'beginner_courses': beginner_courses.distinct(),
        'intermediate_courses': intermediate_courses.distinct(),
        'exam_courses': exam_courses.distinct(),
        'premium_courses': premium_courses.distinct(),
    })

def starter_page(request):
    return render(request, 'starter-page.html')

def trainers(request):
    all_trainers = Trainer.objects.all() 
    return render(request, 'trainers.html', {'trainers': all_trainers})

def about(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    average_rating = Testimonial.objects.aggregate(Avg('rating'))['rating__avg']
    average_rating = round(average_rating, 1) if average_rating else 0
    total_reviews = Testimonial.objects.count()
    form = TestimonialForm()

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')

    return render(request, 'about.html', {
        'testimonials': testimonials,
        'form': form,
        'average_rating': average_rating,
        'total_reviews': total_reviews,
    })