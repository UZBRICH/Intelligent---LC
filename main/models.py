from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    description = models.TextField()
    instructor_name = models.CharField(max_length=100)
    student_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='courses/images/', blank=True, null=True) 

    def __str__(self):
        return self.title
    

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='trainers/images/', blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Registration(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.course.title}"