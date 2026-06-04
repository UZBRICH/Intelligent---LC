"""
Django Management Command: import_courses
==========================================

Fields populated:
  - title           : Course name (e.g. "General English – Beginner")
  - category        : Subject area ("English", "Russian", "Uzbek", "Mathematics")
  - price           : Monthly price as a decimal/string (e.g. "350000.00")
  - instructor_name : Assigned teacher name from the system records
  - student_count   : Initialized to 0
  - description     : Detailed course description and syllabus overview
"""

from django.core.management.base import BaseCommand
from main.models import Course


COURSES = [
    # ── English – Kids ────────────────────────────────────────────────────────
    {
        "title": "English – Kids", 
        "category": "English", 
        "price": "300000.00", 
        "instructor_name": "Oyshabegim Ismoilova", 
        "student_count": 0,
        "description": "Bolalar uchun maxsus moslashtirilgan interaktiv va qiziqarli ingliz tili darslari. Asosiy so'z boyligi, so'zlashuv va xotirani rivojlantiruvchi o'yinlarga qaratilgan."
    },

    # ── English – General (each level separate) ───────────────────────────────
    {
        "title": "General English – Beginner", 
        "category": "English", 
        "price": "350000.00", 
        "instructor_name": "Xurshidbek Qodirjonov", 
        "student_count": 0,
        "description": "Mutlaqo yangi boshlovchilar uchun kirish kursi. Asosiy alifbo, muhim so'z boyligi va oddiy gap tuzilmalari o'rgatiladi."
    },
    {
        "title": "General English – Elementary", 
        "category": "English", 
        "price": "350000.00", 
        "instructor_name": "Xurshidbek Qodirjonov", 
        "student_count": 0,
        "description": "Boshlang'ich muloqot ko'nikmalarini rivojlantiradi. Kundalik standart iboralar, oddiy tasvirlar va grammatika asoslarini qamrab oladi."
    },
    {
        "title": "General English – Pre-Intermediate", 
        "category": "English", 
        "price": "370000.00", 
        "instructor_name": "Hayotbek Ismoilov", 
        "student_count": 0,
        "description": "Erkin so'zlashuvga o'tish bosqichi. O'rta darajadagi zamonlar, fikr bildirish va eshitib tushunish ko'nikmalariga qaratilgan."
    },
    {
        "title": "General English – Intermediate", 
        "category": "English", 
        "price": "370000.00", 
        "instructor_name": "Hayotbek Ismoilov", 
        "student_count": 0,
        "description": "Nutq ravonligini chuqurlashtiring. Murakkab grammatik qoidalarni sayqallash bilan birga ish, o'qish va dam olish faoliyatlari haqida batafsil suhbatlar olib boriladi."
    },
    {
        "title": "General English – Upper-Intermediate", 
        "category": "English", 
        "price": "390000.00", 
        "instructor_name": "Sarvar Rahmatullayev", 
        "student_count": 0,
        "description": "Tilni yuqori darajada egallang. Murakkab fikrlarni aniq ifodalash, mavhum matnlarni tushunish va erkin (tayyorgarliksiz) gapirishni o'rganing."
    },
    {
        "title": "General English – Advanced", 
        "category": "English", 
        "price": "390000.00", 
        "instructor_name": "Sarvar Rahmatullayev", 
        "student_count": 0,
        "description": "Professional va akademik ingliz tili iboralarini mukammal egallang. Tilning nozik jihatlari, xalqona iboralar (idiomalar) va ilg'or yozma ish turlari ustida ishlanadi."
    },

    # ── English – Exam Prep ───────────────────────────────────────────────────
    {
        "title": "English – IELTS Preparation", 
        "category": "English", 
        "price": "450000.00", 
        "instructor_name": "Muhammadamin Usarboev", 
        "student_count": 0,
        "description": "IELTS imtihonining barcha 4 ta komponentiga qaratilgan jiddiy tayyorgarlik. Har haftalik sinov (mock) testlari, yuqori ball olish strategiyalari va intensiv insho (writing) tahlilini qamrab oladi."
    },
    {
        "title": "English – CEFR Preparation", 
        "category": "English", 
        "price": "450000.00", 
        "instructor_name": "Niyozbek To'raboyev", 
        "student_count": 0,
        "description": "Milliy Idoralararo (CEFR) talablariga to'liq mos keladigan dastur. Asosan leksik-grammatik kompetensiya, o'qish va og'zaki nutq testlariga chuqur e'tibor qaratiladi."
    },

    # ── English – Intensive ───────────────────────────────────────────────────
    {
        "title": "English – Intensive", 
        "category": "English", 
        "price": "650000.00", 
        "instructor_name": "Mustafo Khusniddinov", 
        "student_count": 0,
        "description": "Haftada 5 marta o'tiladigan jadallashtirilgan kurs dasturi. Tilni tez fursatda o'rganish va qisqa vaqt ichida natijaga erishish kerak bo'lgan o'quvchilar uchun mo'ljallangan."
    },

    # ── English – Premium & Individual ───────────────────────────────────────
    {
        "title": "English – Mini-group Intensive (Premium)", 
        "category": "English", 
        "price": "890000.00", 
        "instructor_name": "Mustafo Khusniddinov", 
        "student_count": 0,
        "description": "Faqatgina 3-4 o'quvchi bilan cheklangan eksklyuziv sinf muhiti. Interaktiv guruh dinamikasini saqlagan holda, har bir o'quvchiga individual e'tibor qaratish imkonini beradi."
    },
    {
        "title": "English – Individual (VIP)", 
        "category": "English", 
        "price": "1390000.00", 
        "instructor_name": "Mustafo Khusniddinov", 
        "student_count": 0,
        "description": "Premium darajadagi moslanuvchan dars jadvaliga ega bo'lgan 1-ga-1 individual yondashuv. To'liq sizning professional maqsadlaringizga moslab tuzilgan maxsus o'quv dasturi."
    },
    {
        "title": "English – Individual 3-day/week (Flexible)", 
        "category": "English", 
        "price": "890000.00", 
        "instructor_name": "Niyozbek To'raboyev", 
        "student_count": 0,
        "description": "Haftada 3 kun o'tiladigan xususiy individual mashg'ulotlar. Mustaqil moslanuvchan dars jadvali va shaxsiy o'qituvchi nazoratining mukammal balansi."
    },

    # ── Russian – General (each level separate) ───────────────────────────────
    {
        "title": "Russian – Beginner", 
        "category": "Russian", 
        "price": "350000.00", 
        "instructor_name": "Malika Tursunova", 
        "student_count": 0,
        "description": "Kirill alifbosi asoslari, to'g'ri fonetik talaffuz va kundalik rus hayotidagi kirish so'zlashuv iboralarini mukammal o'rganing."
    },
    {
        "title": "Russian – Elementary", 
        "category": "Russian", 
        "price": "350000.00", 
        "instructor_name": "Malika Tursunova", 
        "student_count": 0,
        "description": "Kundalik so'z boyligini oshiring, otlarning kelishiklar bo'yicha o'zgarishini o'rganing va xaridlar hamda sayohatlar uchun oddiy muloqotlar quring."
    },
    {
        "title": "Russian – Pre-Intermediate", 
        "category": "Russian", 
        "price": "350000.00", 
        "instructor_name": "Tolibjon Khayumov", 
        "student_count": 0,
        "description": "Grammatik bilimlarni kengaytiradi, fe'l turlari (aspektlari) bilan tanishtiradi va keng tarqalgan ijtimoiy muhitda ishonchli so'zlashuv ravonligini shakllantiradi."
    },
    {
        "title": "Russian – Intermediate", 
        "category": "Russian", 
        "price": "350000.00", 
        "instructor_name": "Tolibjon Khayumov", 
        "student_count": 0,
        "description": "Rus tili kelishiklarini, gap sintaksisi va murakkab iboralarni chuqurroq qo'llash. Korporativ va ishbilarmonlik muhitlari uchun juda mos keladi."
    },

    # ── Russian – Conversation & Intensive ────────────────────────────────────
    {
        "title": "Russian – Conversation Classes", 
        "category": "Russian", 
        "price": "350000.00", 
        "instructor_name": "Malika Tursunova", 
        "student_count": 0,
        "description": "Til to'sig'ini butunlay yo'q qilishga qaratilgan 100% so'zlashuv asosidagi kurs. Munozaralar, jonli bahslar va og'zaki nutq uslublariga qaratilgan."
    },
    {
        "title": "Russian – Intensive", 
        "category": "Russian", 
        "price": "650000.00", 
        "instructor_name": "G'iyosiddin Khusniddinov", 
        "student_count": 0,
        "description": "Har kuni o'tiladigan formatdagi yuqori tezlikdagi dastur. Qisqa muddat ichida standart o'quv rejasidan ikki baravar ko'p materialni qamrab oladi."
    },

    # ── Russian – Premium & Individual ───────────────────────────────────────
    {
        "title": "Russian – Mini-group Intensive (Premium)", 
        "category": "Russian", 
        "price": "890000.00", 
        "instructor_name": "G'iyosiddin Khusniddinov", 
        "student_count": 0,
        "description": "Rus tilini professional darajada tezlashtirilgan holda o'rganish uchun premium kichik guruh formati. Biznes muloqotining maxsus talablariga chuqur e'tibor qaratiladi."
    },
    {
        "title": "Russian – Individual (VIP)", 
        "category": "Russian", 
        "price": "1390000.00", 
        "instructor_name": "Tolibjon Khayumov", 
        "student_count": 0,
        "description": "Rus tili bo'yicha elita darajasidagi 1-ga-1 individual repetitorlik. To'liq mijozning soha faoliyati yoki aniq maqsadlariga qaratilgan maxsus o'quv dasturi."
    },
    {
        "title": "Russian – Individual 3-day/week (Flexible)", 
        "category": "Russian", 
        "price": "890000.00", 
        "instructor_name": "Malika Tursunova", 
        "student_count": 0,
        "description": "Haftada 3 marta o'tiladigan moslanuvchan xususiy darslar, to'liq sizning band ish jadvalingiz va o'rganish sur'atingizga moslashtiriladi."
    },

    # ── Uzbek – General (each level separate) ────────────────────────────────
    {
        "title": "Uzbek – Beginner", 
        "category": "Uzbek", 
        "price": "350000.00", 
        "instructor_name": "Husnida Abdusalomova", 
        "student_count": 0,
        "description": "O'zbek tilining eng muhim asoslarini o'rganing. Asosiy grammatika, madaniy odob-axloq qoidalari va boshlang'ich muloqot ko'nikmalariga qaratilgan."
    },
    {
        "title": "Uzbek – Elementary", 
        "category": "Uzbek", 
        "price": "350000.00", 
        "instructor_name": "Husnida Abdusalomova", 
        "student_count": 0,
        "description": "So'z boyligi va kundalik iboralar qo'llanilishini kengaytiring. Jamiyatda va kundalik hayotda ishlatiladigan amaliy so'zlashuv tuzilmalariga qaratilgan."
    },
    {
        "title": "Uzbek – Pre-Intermediate", 
        "category": "Uzbek", 
        "price": "350000.00", 
        "instructor_name": "Husnida Abdusalomova", 
        "student_count": 0,
        "description": "Til tuzilishini yanada chuqurroq o'rganish uchun oraliq bosqich. Qo'shma gap bog'lanishlari va ta'sirchan xalqona iboralarni qamrab oladi."
    },
    {
        "title": "Uzbek – Intermediate", 
        "category": "Uzbek", 
        "price": "350000.00", 
        "instructor_name": "Husnida Abdusalomova", 
        "student_count": 0,
        "description": "Kundalik ravon so'zlashuvning yuqori bosqichi. Mahalliy matnlarni o'qish, xat yozish va jamoat oldida nutq so'zlashda to'liq mustaqillikka erishing."
    },

    # ── Uzbek – Exam Prep & Intensive ────────────────────────────────────────
    {
        "title": "Uzbek – Certificate Preparation", 
        "category": "Uzbek", 
        "price": "390000.00", 
        "instructor_name": "Husnida Abdusalomova", 
        "student_count": 0,
        "description": "Milliy standart testlariga maqsadli tayyorgarlik. Adabiy til normalari, ona tili morfologiyasi va test topshirishning o'ziga xos usullarini chuqur o'rganish."
    },
    {
        "title": "Uzbek – Intensive", 
        "category": "Uzbek", 
        "price": "650000.00", 
        "instructor_name": "Husnida Abdusalomova", 
        "student_count": 0,
        "description": "Grammatika o'rganish vaqtini qisqa muddatga jamlash uchun mo'ljallangan yuqori intensivlikdagi chuqurlashtirilgan kurs."
    },

    # ── Uzbek – Premium & Individual ─────────────────────────────────────────
    {
        "title": "Uzbek – Mini-group Intensive (Premium)", 
        "category": "Uzbek", 
        "price": "790000.00", 
        "instructor_name": "Husnida Abdusalomova", 
        "student_count": 0,
        "description": "Tilni tez fursatda o'zlashtirish uchun mo'ljallangan kichik, 3 kishilik guruh. Dars soatlari davomida yuqori darajadagi so'zlashuv zichligi."
    },
    {
        "title": "Uzbek – Individual (VIP)", 
        "category": "Uzbek", 
        "price": "1290000.00", 
        "instructor_name": "Husnida Abdusalomova", 
        "student_count": 0,
        "description": "Maxsus tayyorlangan VIP individual dastur. Tilni chuqur o'rganishni xohlovchi xorijiy rahbarlar, diplomatlar yoki til mutaxassislari uchun juda mos keladi."
    },

    # ── Mathematics – General (each level separate) ───────────────────────────
    {
        "title": "Mathematics – Beginner", 
        "category": "Mathematics", 
        "price": "350000.00", 
        "instructor_name": "Xojiraxon Omonova", 
        "student_count": 0,
        "description": "Asosiy sonli tasavvurni rivojlantiring. Fundamental arifmetika, amallar, kasrlar va boshlang'ich geometriyaga kirish darslariga qaratilgan."
    },
    {
        "title": "Mathematics – Elementary", 
        "category": "Mathematics", 
        "price": "350000.00", 
        "instructor_name": "Xojiraxon Omonova", 
        "student_count": 0,
        "description": "Algebra asoslariga kirish, tenglamalar tizimi, chiziqli grafiklar va matnli masalalarni yechish uslublari."
    },
    {
        "title": "Mathematics – Intermediate", 
        "category": "Mathematics", 
        "price": "350000.00", 
        "instructor_name": "Xojiraxon Omonova", 
        "student_count": 0,
        "description": "Murakkab algebraik funksiyalar, kvadrat tenglamalar, koordinatali trigonometriya va tahliliy logarifmik mantiq tizimlari."
    },

    # ── Mathematics – Exam Prep & Intensive ───────────────────────────────────
    {
        "title": "Mathematics – SAT Preparation", 
        "category": "Mathematics", 
        "price": "390000.00", 
        "instructor_name": "Bekzodbek Komilov", 
        "student_count": 0,
        "description": "Digital SAT Math bo'limi uchun maxsus strategiyalar. Algebraning asosi (Heart of Algebra), masalalar yechish va ma'lumotlar tahlili hamda oliy matematikani qamrab oladi."
    },
    {
        "title": "Mathematics – National Certificate Preparation", 
        "category": "Mathematics", 
        "price": "390000.00", 
        "instructor_name": "Xojiraxon Omonova", 
        "student_count": 0,
        "description": "Davlat test markazi (DTM) sertifikatlash modullarini muvaffaqiyatli topshirish va oliy o'quv yurtlariga kirishda imtiyozlarni qo'lga kiritish uchun maxsus tayyorlangan jiddiy dastur."
    },
    {
        "title": "Mathematics – Intensive", 
        "category": "Mathematics", 
        "price": "650000.00", 
        "instructor_name": "Bekzodbek Komilov", 
        "student_count": 0,
        "description": "Asosiy imtihon mavzularini tezlashtirilgan tarzda o'rgatuvchi intensiv kurs. Muhim imtihonlar oldidan maktab dasturi mantiqiy tizimlarini takrorlashni xohlovchi o'quvchilar uchun ideal."
    },

    # ── Mathematics – Premium & Individual ───────────────────────────────────
    {
        "title": "Mathematics – Mini-group Intensive (Premium)", 
        "category": "Mathematics", 
        "price": "790000.00", 
        "instructor_name": "Xojiraxon Omonova", 
        "student_count": 0,
        "description": "Har bir xato aniqlanishi va o'qituvchi bilan interaktiv tarzda ko'rib chiqilishini ta'minlaydigan kichik guruh dinamikasi."
    },
    {
        "title": "Mathematics – Individual (VIP)", 
        "category": "Mathematics", 
        "price": "1290000.00", 
        "instructor_name": "Xojiraxon Omonova", 
        "student_count": 0,
        "description": "O'rganishdagi qiyinchiliklarni bartaraf etish va tahliliy muammolarni yechish ko'nikmalarini tezlashtirish uchun mo'ljallangan maxsus premium individual repetitorlik kursi."
    },
    {
        "title": "Mathematics – Individual 3-day/week (Flexible)", 
        "category": "Mathematics", 
        "price": "790000.00", 
        "instructor_name": "Bekzodbek Komilov", 
        "student_count": 0,
        "description": "Haftalik moslanuvchan 3 kunlik grafik asosidagi shaxsiy matematika kursi. Maxsus olimpiada masalalari yoki muayyan kirish imtihonlari mezonlarini maqsad qiladi."
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
                    "description": data["description"],
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