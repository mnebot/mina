**O‘zbekcha**

# Ko‘p tilli uy yordamchisi

**Til:** O‘zbekcha · [Til tanlashga qaytish](../readme.md)

Bu loyiha Raspberry Pi kompyuterida ko‘p tilli ovozli yordamchi bilan mahalliy aqlli uy ekotizimini joylashtirishni tavsiflaydi.

## Mina nomining kelib chiqishi

**Mina** nomi qadimgi germancha *minna* so‘zidan kelib chiqqan bo‘lib, u «xotira», «mehri» yoki «sevimlik» ma’nolarini anglatadi. U boshqa tillarda ham uchraydi: fors tilida *mīnā* «nur» yoki «ko‘k shisha» bilan bog‘liq, yapon tilida esa *mina* «barcha» yoki «barcha birga» deganidir.

Bu talqinlar **umumiy xotira va jamoani** ramziy ifodalaydi — ular kundalik uy hayotiga hamroh bo‘lib yordam beradigan yordamchiga mos qadriyatlar.

Tovush jihatidan Mina yumshoq, biroq aniq nom bo‘lib, `Mi-na` tarzida bo‘g‘inlarga bo‘linadi va uy muhitidagi odatiy so‘zlar bilan aralashib ketish ehtimoli past.

## Maqsad

Bulutli xizmatlarga majburiy bog‘liq bo‘lmagan holda ovozli buyruqlar orqali uy qurilmalarini boshqarishni ta'minlovchi xususiy, ishonchli va tezkor aqlli uy tizimini yaratish.

Arxitektura quyidagilarni birlashtiradi:

- Uy buyruqlari va maxfiylik uchun mahalliy qayta ishlash.
- Umumiy savollar uchun Ollama bilan mahalliy sun'iy intellekt.
- Murakkab so‘rovlar va yangilangan ma’lumotlar uchun bulut modellari.

## Uskuna

- 8 GB RAM bilan Raspberry Pi 5 tavsiya etiladi. Raspberry Pi 3B+ gacha cheklangan moslik mavjud.
- SD karta ishlatilmaydigan NVMe SSD disk. SD karta bilan cheklangan moslik.
- Ikki yo‘nalishli USB mikrofon va karnay.
- Zigbee, Matter, Philips Hue yoki mahalliy Wi-Fi bilan mos uy qurilmalari.
- Termal throttlingning oldini olish uchun faol sovutish.

## Arxitektura

1. Home Assistant OS qurilmalar va avtomatlashtirishlarni boshqaradi.
2. openWakeWord faollashtiruvchi so‘zni mahalliy aniqlaydi.
3. Whisper Wyoming orqali faol tildagi buyruqlarni matnga aylantiradi.
4. Niyat protsessori uy buyruqlarini mahalliy bajaradi.
5. Piper javoblarni o‘zbek tilida sintez qiladi.
6. Ollama umumiy savollarga ma’lumotni Internetga yubormasdan javob beradi.
7. Bulut sun'iy intellekti faqat ilg‘or sun'iy intellekt talab qiladigan aniq so‘rovlarni qabul qiladi.

## Rejalashtirilgan imkoniyatlar

- Chiroqlar, rozetkalar, konditsioner, pardalar va boshqa qurilmalarni ovoz bilan boshqarish.
- Ko‘p tilli taxalluslar.
- Ovozi bilan boshqariladigan taymerlar.
- Mahalliy ob-havo ma’lumotini so‘rash.
- Musiqani ijro etish va boshqarish.
- Ollama modeliga xususiy zaxira o‘tish.
- Ovozi bo‘yicha shaxsni tanish.
- Uzoq muddatli kontekst xotirasi.
- Bulut sun'iy intellekt modeliga ixtiyoriy yo‘naltirish.
- Zaxira nusxalar va unumdorlik nazorati.

## Dizayn tamoyillari

- Uy buyruqlari Internet aloqasisiz ishlashi kerak.
- Mahalliy niyat protsessori LLMlardan ustunlikka ega.
- Audio ma’lumotlar va shaxsiy suhbatlar imkon qadar mahalliy qayta ishlanadi.
- Bulut modellari faqat aniq yoki murakkab so‘rovlar uchun va faqat foydalanuvchi yordamchini sozlash paytida buni aniq so‘raganida ishlatiladi.
- Tizim doimiy yuk ostida barqaror harorat va kechikishni saqlashi kerak.

## Loyihaning holati

Loyiha funktsional backlog sifatida belgilangan. Muayyan konfiguratsiyalar, avtomatlashtirishlar va joylashtirish skriptlari foydalanuvchi hikoyalari bajarilgach qo‘shiladi.
