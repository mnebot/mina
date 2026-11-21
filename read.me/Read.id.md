**Bahasa: Indonesia · [Kembali ke pilihan bahasa](../readme.md)**

# Asisten Rumah Pintar Multibahasa


**Baca dalam:** [Indonesia](Read.id.md) · [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Proyek ini menjelaskan penerapan ekosistem rumah pintar lokal pada Raspberry Pi dengan asisten suara multibahasa.

## Asal-usul nama Mina

**Mina** berakar dari kata *minna* dalam bahasa Jermanik kuno, yang berarti “ingatan”, “kasih sayang”, atau “kenangan”. Nama ini juga ditemukan dalam bahasa lain: dalam bahasa Persia, *mīnā* berkaitan dengan “cahaya” atau “kaca biru”, sedangkan dalam bahasa Jepang, *mina* berarti “semua orang” atau “semuanya bersama”.

Makna-makna tersebut melambangkan **ingatan bersama dan komunitas**, nilai-nilai yang selaras dengan asisten yang menemani dan mendukung kehidupan sehari-hari di rumah.

Dari segi bunyi, Mina terdengar lembut tetapi jelas. Namanya diucapkan per suku kata sebagai `Mi-na`, dan kecil kemungkinannya tertukar dengan kata-kata yang umum digunakan di lingkungan rumah.

## Tujuan

Membangun sistem rumah pintar yang privat, andal, dan cepat, sehingga perangkat rumah dapat dikendalikan melalui perintah suara tanpa harus bergantung pada layanan cloud.

Arsitektur ini menggabungkan:

- Pemrosesan lokal untuk perintah rumah pintar dan perlindungan privasi.
- Kecerdasan lokal dengan Ollama untuk pertanyaan umum.
- Model cloud untuk pertanyaan rumit dan informasi terkini.

## Perangkat keras

- Raspberry Pi 5 dengan RAM 8 GB direkomendasikan. Kompatibilitas terbatas hingga Raspberry Pi 3B+.
- Gunakan SSD NVMe, bukan kartu SD. Dukungan untuk kartu SD terbatas.
- Mikrofon dan speaker USB dua arah.
- Perangkat rumah pintar yang kompatibel dengan Zigbee, Matter, Philips Hue, atau Wi-Fi lokal.
- Pendinginan aktif untuk mencegah throttling termal.

## Arsitektur

1. Home Assistant OS mengelola perangkat dan otomatisasi.
2. openWakeWord mendeteksi kata pemicu secara lokal.
3. Whisper mentranskripsikan perintah dalam bahasa yang sedang aktif melalui Wyoming.
4. Pemroses intent menjalankan perintah rumah pintar secara lokal.
5. Piper menyintesis jawaban dalam bahasa Katalan.
6. Ollama menjawab pertanyaan umum tanpa mengirim data ke internet.
7. Hanya permintaan eksplisit yang memerlukan AI tingkat lanjut yang dikirim ke AI cloud.

## Fitur yang direncanakan

- Mengendalikan lampu, stopkontak, pendingin ruangan, tirai, dan perangkat lain dengan suara.
- Alias multibahasa.
- Timer yang dikelola melalui suara.
- Memeriksa cuaca setempat.
- Memutar dan mengendalikan musik.
- Fallback privat ke model Ollama.
- Mengenali orang dari suaranya.
- Memori konteks jangka panjang.
- Pengalihan opsional ke model AI cloud.
- Pencadangan dan pemantauan kinerja.

## Prinsip desain

- Perintah rumah pintar harus tetap berfungsi tanpa koneksi internet.
- Pemroses intent lokal diprioritaskan daripada LLM.
- Data audio dan percakapan pribadi sedapat mungkin diproses secara lokal.
- Model cloud hanya digunakan untuk permintaan eksplisit atau rumit, dan hanya jika pengguna secara tegas mengaktifkannya saat mengonfigurasi asisten.
- Suhu dan latensi sistem harus tetap stabil di bawah beban terus-menerus.

## Status proyek

Proyek ini didefinisikan sebagai daftar pekerjaan fungsional. Konfigurasi khusus, otomatisasi, dan skrip penerapan akan ditambahkan seiring penyelesaian cerita pengguna.
