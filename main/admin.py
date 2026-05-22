from django.contrib import admin
from .models import Course, Trainer


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'instructor_name', 'student_count')
    search_fields = ('title', 'category', 'instructor_name')
    list_filter = ('category',)


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty')
    search_fields = ('name', 'specialty')