"""
Django Management Command: import_courses
==========================================
Place this file at:
  yourapp/management/commands/import_courses.py
 
Make sure yourapp/management/__init__.py and
yourapp/management/commands/__init__.py both exist (they can be empty).
 
Run with:
  python manage.py import_courses
 
Fields populated:
  - title           : course name (e.g. "General English – Beginner–Intermediate")
  - category        : subject area (e.g. "English", "Russian", "Uzbek", "Mathematics")
  - price           : monthly price as an integer (e.g. 300000)
  - instructor_name : generic placeholder – update when you have real names
  - student_count   : left as 0 – update when the client provides this data
"""
from main.models import Course
from django.core.management.base import BaseCommand

 
COURSES = [
    # ── English Language Courses ─────────────────────────────────────────────
    {
        "title": "English – Kids",
        "category": "English",
        "price": 300000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "General English – Beginner–Intermediate",
        "category": "English",
        "price": 350000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "General English – Upper–Advanced",
        "category": "English",
        "price": 390000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    # ── English – Exam Prep ───────────────────────────────────────────────────
    {
        "title": "English – IELTS Preparation",
        "category": "English",
        "price": 430000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "English – CEFR Preparation",
        "category": "English",
        "price": 430000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "English – Intensive",
        "category": "English",
        "price": 650000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    # ── English – Premium & Individual ───────────────────────────────────────
    {
        "title": "English – Mini-group Intensive (Premium)",
        "category": "English",
        "price": 890000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "English – Individual (VIP)",
        "category": "English",
        "price": 1390000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "English – Individual 3-day/week (Flexible)",
        "category": "English",
        "price": 890000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    # ── Russian Language Courses ──────────────────────────────────────────────
    {
        "title": "Russian – Conversation Classes",
        "category": "Russian",
        "price": 350000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "Russian – Group",
        "category": "Russian",
        "price": 350000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "Russian – Intensive",
        "category": "Russian",
        "price": 650000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    # ── Russian – Premium & Individual ───────────────────────────────────────
    {
        "title": "Russian – Mini-group Intensive (Premium)",
        "category": "Russian",
        "price": 790000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "Russian – Individual (VIP)",
        "category": "Russian",
        "price": 1190000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "Russian – Individual 3-day/week (Flexible)",
        "category": "Russian",
        "price": 790000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    # ── Uzbek Language Courses ────────────────────────────────────────────────
    {
        "title": "Uzbek – Beginner",
        "category": "Uzbek",
        "price": 350000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "Uzbek – Certificate Preparation",
        "category": "Uzbek",
        "price": 390000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "Uzbek – Intensive",
        "category": "Uzbek",
        "price": 650000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    # ── Uzbek – Premium & Individual ─────────────────────────────────────────
    {
        "title": "Uzbek – Mini-group Intensive (Premium)",
        "category": "Uzbek",
        "price": 790000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "Uzbek – Individual (VIP)",
        "category": "Uzbek",
        "price": 1190000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    # ── Mathematics Courses ───────────────────────────────────────────────────
    {
        "title": "Mathematics – Beginner",
        "category": "Mathematics",
        "price": 350000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "Mathematics – SAT & National Certificate",
        "category": "Mathematics",
        "price": 390000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "Mathematics – Intensive",
        "category": "Mathematics",
        "price": 650000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    # ── Mathematics – Premium & Individual ───────────────────────────────────
    {
        "title": "Mathematics – Mini-group Intensive (Premium)",
        "category": "Mathematics",
        "price": 790000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "Mathematics – Individual (VIP)",
        "category": "Mathematics",
        "price": 1190000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
    {
        "title": "Mathematics – Individual 3-day/week (Flexible)",
        "category": "Mathematics",
        "price": 790000,
        "instructor_name": "TBD",
        "student_count": 0,
    },
]
 
 
class Command(BaseCommand):
    help = "Import all courses from the Course Catalogue into the database."
 
    def handle(self, *args, **kwargs):
        created_count = 0
        skipped_count = 0
 
        for data in COURSES:
            obj, created = Course.objects.get_or_create(
                title=data["title"],
                defaults={
                    "category": data["category"],
                    "price": data["price"],
                    "instructor_name": data["instructor_name"],
                    "student_count": data["student_count"],
                },
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"  ✔ Created: {obj.title}"))
            else:
                skipped_count += 1
                self.stdout.write(self.style.WARNING(f"  – Skipped (already exists): {obj.title}"))
 
        self.stdout.write(
            self.style.SUCCESS(
                f"\nDone! {created_count} course(s) created, {skipped_count} skipped."
            )
        )
 