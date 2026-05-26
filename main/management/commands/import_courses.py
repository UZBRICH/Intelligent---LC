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

 
"""
Django Management Command: import_courses
==========================================
Place this file at:
  main/management/commands/import_courses.py

Run with:
  python manage.py import_courses
"""

from django.core.management.base import BaseCommand
from main.models import Course

COURSES = [
    # ── English – Kids ────────────────────────────────────────────────────────
    {"title": "English – Kids", "category": "English", "price": "300000.00", "instructor_name": "TBD", "student_count": 0},

    # ── English – General (each level separate) ───────────────────────────────
    {"title": "General English – Beginner", "category": "English", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "General English – Elementary", "category": "English", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "General English – Pre-Intermediate", "category": "English", "price": "370000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "General English – Intermediate", "category": "English", "price": "370000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "General English – Upper-Intermediate", "category": "English", "price": "390000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "General English – Advanced", "category": "English", "price": "390000.00", "instructor_name": "TBD", "student_count": 0},

    # ── English – Exam Prep ───────────────────────────────────────────────────
    {"title": "English – IELTS Preparation", "category": "English", "price": "450000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "English – CEFR Preparation", "category": "English", "price": "450000.00", "instructor_name": "TBD", "student_count": 0},

    # ── English – Intensive ───────────────────────────────────────────────────
    {"title": "English – Intensive", "category": "English", "price": "650000.00", "instructor_name": "TBD", "student_count": 0},

    # ── English – Premium & Individual ───────────────────────────────────────
    {"title": "English – Mini-group Intensive (Premium)", "category": "English", "price": "890000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "English – Individual (VIP)", "category": "English", "price": "1390000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "English – Individual 3-day/week (Flexible)", "category": "English", "price": "890000.00", "instructor_name": "TBD", "student_count": 0},

    # ── Russian – General (each level separate) ───────────────────────────────
    {"title": "Russian – Beginner", "category": "Russian", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Russian – Elementary", "category": "Russian", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Russian – Pre-Intermediate", "category": "Russian", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Russian – Intermediate", "category": "Russian", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},

    # ── Russian – Conversation & Intensive ────────────────────────────────────
    {"title": "Russian – Conversation Classes", "category": "Russian", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Russian – Intensive", "category": "Russian", "price": "650000.00", "instructor_name": "TBD", "student_count": 0},

    # ── Russian – Premium & Individual ───────────────────────────────────────
    {"title": "Russian – Mini-group Intensive (Premium)", "category": "Russian", "price": "890000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Russian – Individual (VIP)", "category": "Russian", "price": "1390000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Russian – Individual 3-day/week (Flexible)", "category": "Russian", "price": "890000.00", "instructor_name": "TBD", "student_count": 0},

    # ── Uzbek – General (each level separate) ────────────────────────────────
    {"title": "Uzbek – Beginner", "category": "Uzbek", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Uzbek – Elementary", "category": "Uzbek", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Uzbek – Pre-Intermediate", "category": "Uzbek", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Uzbek – Intermediate", "category": "Uzbek", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},

    # ── Uzbek – Exam Prep & Intensive ────────────────────────────────────────
    {"title": "Uzbek – Certificate Preparation", "category": "Uzbek", "price": "390000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Uzbek – Intensive", "category": "Uzbek", "price": "650000.00", "instructor_name": "TBD", "student_count": 0},

    # ── Uzbek – Premium & Individual ─────────────────────────────────────────
    {"title": "Uzbek – Mini-group Intensive (Premium)", "category": "Uzbek", "price": "790000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Uzbek – Individual (VIP)", "category": "Uzbek", "price": "1290000.00", "instructor_name": "TBD", "student_count": 0},

    # ── Mathematics – General (each level separate) ───────────────────────────
    {"title": "Mathematics – Beginner", "category": "Mathematics", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Mathematics – Elementary", "category": "Mathematics", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Mathematics – Intermediate", "category": "Mathematics", "price": "350000.00", "instructor_name": "TBD", "student_count": 0},

    # ── Mathematics – Exam Prep & Intensive ───────────────────────────────────
    {"title": "Mathematics – SAT Preparation", "category": "Mathematics", "price": "390000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Mathematics – National Certificate Preparation", "category": "Mathematics", "price": "390000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Mathematics – Intensive", "category": "Mathematics", "price": "650000.00", "instructor_name": "TBD", "student_count": 0},

    # ── Mathematics – Premium & Individual ───────────────────────────────────
    {"title": "Mathematics – Mini-group Intensive (Premium)", "category": "Mathematics", "price": "790000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Mathematics – Individual (VIP)", "category": "Mathematics", "price": "1290000.00", "instructor_name": "TBD", "student_count": 0},
    {"title": "Mathematics – Individual 3-day/week (Flexible)", "category": "Mathematics", "price": "790000.00", "instructor_name": "TBD", "student_count": 0},
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
 