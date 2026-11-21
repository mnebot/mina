**Türkçe** · [Dil seçimine dön](../readme.md)

# Çok Dilli Ev Asistanı

Bu proje, Raspberry Pi üzerinde çok dilli bir sesli asistan ekosisteminin yerel olarak kurulmasını anlatır.

## Mina adının kökeni

**Mina** adı, “bellek”, “sevgi” veya “hatıra” anlamına gelen eski Germen kökenli *minna* kelimesinden gelir. Başka dillerde de vardır: Farsçada *mīnā* “ışık” veya “mavi cam” ile ilişkilendirilir; Japoncada *mina* “herkes” veya “hep birlikte” anlamına gelir.

Bu yorumlar; evin günlük yaşamına eşlik eden ve destek olan bir asistana uygun olan **paylaşılan bellek ve topluluk** değerlerini simgeler.

Ses açısından Mina, `Mi-na` heceleme telaffuzu olan, yumuşak ama açık bir isimdir ve ev ortamında yaygın kelimelerle karıştırılma olasılığı düşüktür.

## Amaç

Bulut hizmetlerine zorunlu bağımlılık olmadan, sesli komutlarla ev cihazlarını kontrol etmeyi sağlayan özel, güvenilir ve hızlı bir ev sistemi oluşturmak.

Mimari şunları birleştirir:

- Ev komutları ve gizlilik için yerel işlem.
- Genel sorular için Ollama ile yerel yapay zekâ.
- Karmaşık sorgular ve güncel bilgiler için bulut modelleri.

## Donanım

- Raspberry Pi 5 için 8 GB RAM önerilir. Raspberry Pi 3B+ sürümüne kadar sınırlı uyumluluk vardır.
- SD kart kullanılmadan NVMe SSD. SD kartla sınırlı uyumluluk.
- Çift yönlü USB mikrofon ve hoparlör.
- Zigbee, Matter, Philips Hue veya yerel Wi-Fi ile uyumlu ev cihazları.
- Termal azaltmayı önlemek için aktif soğutma.

## Mimari

1. Home Assistant OS cihazları ve otomasyonları yönetir.
2. openWakeWord etkinleştirme kelimesini yerel olarak algılar.
3. Whisper, Wyoming üzerinden aktif dildeki komutları metne dönüştürür.
4. Niyet işlemcisi ev komutlarını yerel olarak çalıştırır.
5. Piper yanıtları Türkçe sentezler.
6. Ollama genel soruları veriyi İnternet'e göndermeden çözer.
7. Bulut yapay zekâsı yalnızca gelişmiş yapay zekâ gerektiren açık sorguları alır.

## Planlanan özellikler

- Işıkların, prizlerin, iklimlendirme sistemlerinin, panjurların ve diğer cihazların sesle kontrolü.
- Çok dilli takma adlar.
- Sesle yönetilen zamanlayıcılar.
- Yerel hava durumu sorguları.
- Müzik çalma ve kontrol.
- Ollama modeline özel yedek çözüm.
- Sese göre kişi tanıma.
- Uzun süreli bağlam belleği.
- İsteğe bağlı olarak bulut yapay zekâ modeline yönlendirme.
- Yedekleme ve performans izleme.

## Tasarım ilkeleri

- Ev komutları İnternet bağlantısı olmadan çalışmalıdır.
- Yerel niyet işlemcisinin LLM'lere göre önceliği vardır.
- Ses verileri ve özel konuşmalar tercihen yerel işlenir.
- Bulut modelleri yalnızca açık veya karmaşık sorgular için ve yalnızca kullanıcı asistanı yapılandırırken bunu açıkça istemişse kullanılır.
- Sistem sürekli yük altında kararlı sıcaklık ve gecikme sağlamalıdır.

## Proje durumu

Proje işlevsel bir backlog olarak tanımlanmıştır. Kullanıcı hikâyeleri tamamlandıkça özel yapılandırmalar, otomasyonlar ve dağıtım betikleri eklenmelidir.
