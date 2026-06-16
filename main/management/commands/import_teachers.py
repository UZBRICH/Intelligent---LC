from django.core.management.base import BaseCommand
from main.models import Trainer

TEACHERS = [
    {
        "name": "Mustafo Khusniddinov",
        "phone": "998905000000",
        "specialty": "Ingliz tili o'qituvchisi",
        "bio": "IELTS 7.0 (Speaking 7.0). Tajriba: 2+ yil. Talabalar: 300+."
    },
    {
        "name": "Xurshidbek Qodirjonov",
        "phone": "998932000000",
        "specialty": "Ingliz tili o'qituvchisi",
        "bio": "CEFR C1. Tajriba: 3+ yil. Talabalar: 500+."
    },
    {
        "name": "Hayotbek Ismoilov",
        "phone": "998944000000",
        "specialty": "Ingliz tili o'qituvchisi",
        "bio": "CEFR C1. Tajriba: 2+ yil. Talabalar: 300+."
    },
    {
        "name": "Muhammadamin Usarboev",
        "phone": "998879000000",
        "specialty": "Ingliz tili yordamchi o'qituvchisi",
        "bio": "IELTS 6.0, CEFR B2. Tajriba: 1+ yil. Talabalar: 100+."
    },
    {
        "name": "Oyshabegim Ismoilova",
        "phone": "998919000000",
        "specialty": "Ingliz tili yordamchi o'qituvchisi",
        "bio": "CEFR B2. Tajriba: 1+ yil. Talabalar: 10+."
    },
    {
        "name": "Niyozbek To'raboyev",
        "phone": "998780000000",
        "specialty": "Ingliz tili yordamchi o'qituvchisi",
        "bio": "IELTS 6.0. Tajriba: 6+ oy. Talabalar: 100+."
    },
    {
        "name": "Xojiraxon Omonova",
        "phone": "998508000000",
        "specialty": "Matematika O'qituvchisi",
        "bio": "A darajadagi milliy sertifikat sohibasi. Tajriba: 2+ yil. Talabalar: 300+."
    },
    {
        "name": "Husnida Abdusalomova",
        "phone": "998922000000",
        "specialty": "Ona tili O'qituvchisi",
        "bio": "A darajadagi milliy sertifikat sohibasi. Tajriba: 2+ yil. Talabalar: 200+."
    },
    {
        "name": "Ziynatoy",
        "phone": "998990000000",  # Placeholder phone number for new entry
        "specialty": "Matematika Yordamchi o'qituvchi",
        "bio": "Tajriba: 6+ oy. Talabalar: 50+."
    }
]


class Command(BaseCommand):
    help = "Import or update trainers from the local dataset into the database."

    def handle(self, *args, **kwargs):
        created_count = 0
        updated_count = 0

        for data in TEACHERS:
            obj, created = Trainer.objects.update_or_create(
                name=data["name"],
                defaults={
                    "phone": data["phone"],
                    "specialty": data["specialty"],
                    "bio": data["bio"],
                },
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"  ✔ Created trainer: {obj.name}"))
            else:
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f"  ⚡ Updated info for: {obj.name}"))

        self.stdout.write(
            self.style.SUCCESS(
                f"\nDone! {created_count} trainer(s) created, {updated_count} trainer(s) updated."
            )
        )