**Azərbaycan dili**

# Çoxdilli ev asistenti

**Dil:** Azərbaycan · [Dil seçiminə qayıt](../readme.md)

Bu layihə Raspberry Pi üzərində çoxdilli səsli assistentlə yerli ağıllı ev ekosisteminin yerləşdirilməsini təsvir edir.

## Mina adının mənşəyi

**Mina** adı qədim german kökli *minna* sözündəndir və “yaddaş”, “məhəbbət” və ya “sevgi” mənasını verir. O, digər dillərdə də mövcuddur: fars dilində *mīnā* “işıq” və ya “mavi şüşə” ilə əlaqələndirilir, yapon dilində isə *mina* “hamı” və ya “birlikdə” deməkdir.

Bu mənalar **ortaq yaddaşı və ictimaiyyətimizi** simvolizə edir; bunlar gündəlik ev həyatına qoşulan və dəstək verən assistentə uyğun dəyərlərdir.

Səs baxımından Mina yumşaq, lakin aydın bir addır; hecalarına `Mi-na` kimi təyin olunur və ev mühitində adi sözlərlə qarışdırılma ehtimalı aşağıdır.

## Məqsəd

Bulud xidmətlərinə məcburi asılılıq olmadan ev cihazlarını səs əmrləri ilə idarə etməyə imkan verən xüsusi, etibarlı və sürətli ağıllı ev sistemi yaratmaq.

Memarlıq aşağıdakıları birləşdirir:

- Ev əmrləri və məxfilik üçün yerli emal.
- Ümumi suallar üçün Ollama ilə yerli AI.
- Mürəkkəb sorğular və yenilənmiş məlumat üçün bulud modelləri.

## Avadanlıq

- 8 GB RAM ilə Raspberry Pi 5 tövsiyə olunur. Raspberry Pi 3B+ qədər məhdud uyğunluq var.
- SD kart istifadə etmədən NVMe SSD disk. SD kartla məhdud uyğunluq.
- İki istiqamətli USB mikrofon və dinamik.
- Zigbee, Matter, Philips Hue və ya yerli Wi-Fi ilə uyğun ev cihazları.
- Termal throttlingin qarşısını almaq üçün aktiv soyutma.

## Memarlıq

1. Home Assistant OS cihazları və avtomatlaşdırmaları idarə edir.
2. openWakeWord aktivləşdirici sözü lokal olaraq aşkarlayır.
3. Whisper Wyoming vasitəsilə cari dildəki əmrləri mətnə çevrir.
4. Niyyət emalçısı ev əmrlərini yerli olaraq icra edir.
5. Piper cavabları Azərbaycan dilində sintez edir.
6. Ollama ümumi sualların cavabını İnternetə məlumat göndərmədən verir.
7. Bulud AI-si yalnız inkişaf etmiş AI tələb edən açıq sorğuları alır.

## Gözlənilən xüsusiyyətlər

- İşıqların, rozetkaların, kondisionerlərin, pərdələrin və başqa cihazların səslə idarə olunması.
- Çoxdilli adlar.
- Səsle idarə olunan taymerlər.
- Yerli hava məlumatı.
- Musiqinin oxudulması və idarə olunması.
- Ollama modelinə şəxsi fallback.
- Səsə görə şəxs tanıma.
- Uzunmüddətli kontekst yaddaşı.
- İstəyə görə bulud AI modelinə yönləndirmə.
- Yedəkləmə və performansın izlənməsi.

## Dizayn prinsipləri

- Ev əmrləri İnternet bağlantısı olmadan işləməlidir.
- Yerli niyyət emalçısı LLM-lərdən üstün olmalıdır.
- Səs məlumatları və şəxsi söhbətlər mümkün qədər yerli emal edilməlidir.
- Bulud modelləri yalnız açıq və ya mürəkkəb sorğular üçün, həm də yalnız istifadəçinin assistenti qurarkən bunu açıq istəməsi hallarında istifadə edilməlidir.
- Sistem davamlı yük altında sabit temperatur və gecikməni saxlamalıdır.

## Layihənin statusu

Layihə funksional iş siyahısı kimi müəyyən edilmişdir. Müəyyən konfiqurasiyalar, avtomatlaşdırmalar və yerləşdirmə skriptləri istifadəçi hekayələri tamamlandıqca əlavə edilməlidir.
