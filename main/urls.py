from django.urls import path
from main import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses_page, name='courses_page'),
    path('course/<int:id>/', views.course_details, name='course-details'),
    path('events/', views.events, name='events'),
    path('pricing/', views.pricing, name='pricing'),
    path('starter-page/', views.starter_page, name='starter-page'),
    path('trainers/', views.trainers, name='trainers'),
]