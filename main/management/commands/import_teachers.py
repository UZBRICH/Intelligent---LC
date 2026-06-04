from django.core.management.base import BaseCommand
from main.models import Trainer

TEACHERS = [
    # ── Ingliz Tili O'qituvchilari ─────────────────────────────────────────────
    {
        "name": "Oyshabegim Ismoilova",
        "phone": "998919000000",
        "specialty": "Ingliz tili (Kids)",
        "bio": "Bolalar uchun ingliz tilini o'qitish bo'yicha mutaxassis. Interaktiv o'yinlar va qiziqarli zamonaviy metodikalar orqali yosh bolalarda tilga bo'lgan qiziqishni yuqori darajada uyg'ota oladi."
    },
    {
        "name": "Xurshidbek Qodirjonov",
        "phone": "998932000000",
        "specialty": "Ingliz tili (General)",
        "bio": "Boshlang'ich va fundamental ingliz tili (Beginner va Elementary) darajalari bo'yicha ko'p yillik muvaffaqiyatli tajribaga ega o'qituvchi. Talabalarga til poydevorini mustahkam qurishda yordam beradi."
    },
    {
        "name": "Hayotbek Ismoilov",
        "phone": "998944000000",
        "specialty": "Ingliz tili (General)",
        "bio": "O'rta darajadagi (Pre-Intermediate va Intermediate) o'quvchilar bilan ishlash va ularning kundalik hayotdagi muloqot to'siqlarini yo'qotib, nutq ravonligini ta'minlash bo'yicha mutaxassis."
    },
    {
        "name": "Sarvar Rahmatullayev",
        "phone": "998900000000",
        "specialty": "Ingliz tili (Advanced)",
        "bio": "Yuqori darajadagi akademik ingliz tili (Upper-Intermediate va Advanced) darslari ustasi. O'quvchilarga murakkab va mavhum mavzularda erkin, tayyorgarliksiz nutq so'zlash texnikalarini o'rgatadi."
    },
    {
        "name": "Muhammadamin Usarboev",
        "phone": "998879000000",
        "specialty": "Ingliz tili (IELTS)",
        "bio": "IELTS imtihoniga maqsadli va jiddiy tayyorlash, akademik insho (writing) tahlili hamda o'quvchilarni yuqori ballik strategiyalar bilan qurollantirish bo'yicha katta natijalarga ega professional murabbiy."
    },
    {
        "name": "Niyozbek To'raboyev",
        "phone": "998780000000",
        "specialty": "Ingliz tili (CEFR / Individual)",
        "bio": "Milliy Idoralararo CEFR imtihonlari talablari va leksik-grammatik kompetensiyalarni mukammal rivojlantirish bo'yicha mutaxassis. Moslanuvchan dars grafiklari asosida individual darslar o'tadi."
    },
    {
        "name": "Mustafo Khusniddinov",
        "phone": "998905000000",
        "specialty": "Ingliz tili (Intensive / VIP)",
        "bio": "Yuqori intensivlikdagi darslar, premium mikro-guruhlar va VIP individual o'quv dasturlarini professional muvofiqlashtiruvchi expert. Qisqa muddatda maksimal natijaga erishishni ta'minlaydi."
    },

    # ── Rus Tili O'qituvchilari ────────────────────────────────────────────────
    {
        "name": "Malika Tursunova",
        "phone": "998934000000",
        "specialty": "Rus tili (General / Conversation)",
        "bio": "Rus tili fonetikasi, to'g'ri talaffuz va talabalardagi so'zlashuv to'sig'ini (yuz foiz og'zaki nutq orqali) butunlay yo'q qilishga ixtisoslashgan tajribali pedagog."
    },
    {
        "name": "Tolibjon Khayumov",
        "phone": "998901000000",
        "specialty": "Rus tili (Intermediate / VIP)",
        "bio": "Korporativ soha va biznes muloqot muhiti uchun rus tili, murakkab kelishiklar tizimi hamda sintaksis qoidalarini eng sodda usullarda tushuntirib beruvchi elita darajasidagi o'qituvchi."
    },
    {
        "name": "G'iyosiddin Khusniddinov",
        "phone": "998908000000",
        "specialty": "Rus tili (Intensive / Premium)",
        "bio": "Rus tili bo'yicha jadallashtirilgan kundalik dasturlar va professional ishbilarmonlik aloqalari talablariga moslashtirilgan maxsus mikro-guruh darslarining yetakchi mutaxassisi."
    },

    # ── Ona Tili va O'zbek Tili ────────────────────────────────────────────────
    {
        "name": "Husnida Abdusalomova",
        "phone": "998922000000",
        "specialty": "O'zbek tili / Ona tili",
        "bio": "O'zbek tili va adabiyoti fanidan milliy sertifikat imtihonlariga mukammal tayyorlash, morfologiya tahlili hamda xorijliklar uchun o'zbek tilini chuqurlashtirilgan holda o'rgatuvchi asosiy o'qituvchi."
    },

    # ── Matematika va Fizika ──────────────────────────────────────────────────
    {
        "name": "Xojiraxon Omonova",
        "phone": "998508000000",
        "specialty": "Matematika / Fizika",
        "bio": "Fundamental arifmetika, oliy matematika va fizika fanlaridan DTM hamda milliy sertifikat modullariga mukammal tayyorlovchi professional ustoz. Har bir o'quvchining xatolarini individual tahlil qiladi."
    },
    {
        "name": "Bekzodbek Komilov",
        "phone": "998980000000",
        "specialty": "Matematika (SAT)",
        "bio": "Digital SAT Math xalqaro bo'limi, murakkab mantiqiy olimpiada masalalari va tahliliy muammolarni tezkor yechish strategiyalari bo'yicha ixtisoslashgan yuqori malakali murabbiy."
    },

    # ── Boshqa Ustozlar ────────────────────────────────────────────────────────
    {
        "name": "Tojiddin Jumaev",
        "phone": "998200000000",
        "specialty": "Aniq fanlar mantiqiy tizimi",
        "bio": "O'quvchilarda umumiy mantiqiy fikrlash va tahlil qilish tizimlarini shakllantirish, fanlararo bog'liqlikni tushuntirish bo'yicha ko'p yillik boy pedagogik tajribaga ega ustoz."
    }
]


class Command(BaseCommand):
    help = "Import or update trainers into the database."

    def handle(self, *args, **kwargs):
        created_count = 0
        updated_count = 0

        for data in TEACHERS:
            # update_or_create maps perfectly to your exact model properties
            obj, created = Trainer.objects.update_or_create(
                name=data["name"],
                defaults={
                    "phone": data["phone"],
                    "specialty": data["specialty"],  # Updated key name here
                    "bio": data["bio"],
                    # Keep URL fields empty strings during initial import 
                    # so they don't break if you leave them blank in your array
                    "facebook": data.get("facebook", ""),
                    "instagram": data.get("instagram", ""),
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


