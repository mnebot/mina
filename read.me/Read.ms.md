**Bahasa: Bahasa Melayu · [Kembali ke pilihan bahasa](../readme.md)**

# Pembantu Rumah Pintar Pelbagai Bahasa


**Baca dalam:** [Bahasa Melayu](Read.ms.md) · [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Projek ini menerangkan penggunaan ekosistem rumah pintar setempat pada Raspberry Pi dengan pembantu suara berbilang bahasa.

## Asal-usul nama Mina

**Mina** berakar daripada perkataan *minna* dalam bahasa Jermanik purba yang bermaksud “ingatan”, “kasih sayang” atau “kenangan”. Nama ini juga terdapat dalam bahasa lain: dalam bahasa Parsi, *mīnā* berkaitan dengan “cahaya” atau “kaca biru”, manakala dalam bahasa Jepun, *mina* bermaksud “semua orang” atau “semua bersama”.

Tafsiran ini melambangkan **ingatan bersama dan komuniti**, nilai yang selaras dengan pembantu yang menemani dan menyokong kehidupan harian di rumah.

Dari segi bunyi, Mina kedengaran lembut tetapi jelas. Namanya disebut mengikut suku kata sebagai `Mi-na`, dan kemungkinan untuk dikelirukan dengan perkataan lazim di rumah adalah rendah.

## Matlamat

Membina sistem rumah pintar yang menjaga privasi, boleh dipercayai dan pantas, supaya peranti di rumah boleh dikawal melalui arahan suara tanpa perlu bergantung pada perkhidmatan awan.

Seni bina ini menggabungkan:

- Pemprosesan setempat untuk arahan rumah pintar dan perlindungan privasi.
- Kecerdasan setempat menggunakan Ollama untuk soalan umum.
- Model awan untuk pertanyaan rumit dan maklumat terkini.

## Perkakasan

- Raspberry Pi 5 dengan RAM 8 GB disyorkan. Keserasian terhad sehingga Raspberry Pi 3B+.
- Gunakan SSD NVMe, bukan kad SD. Sokongan kad SD adalah terhad.
- Mikrofon dan pembesar suara USB dua hala.
- Peranti rumah pintar yang serasi dengan Zigbee, Matter, Philips Hue atau Wi-Fi setempat.
- Penyejukan aktif untuk mengelakkan pendikitan terma.

## Seni bina

1. Home Assistant OS mengurus peranti dan automasi.
2. openWakeWord mengesan kata pengaktifan secara setempat.
3. Whisper menyalin arahan dalam bahasa yang sedang aktif melalui Wyoming.
4. Pemproses niat menjalankan arahan rumah pintar secara setempat.
5. Piper mensintesis jawapan dalam bahasa Catalan.
6. Ollama menjawab soalan umum tanpa menghantar data ke Internet.
7. Hanya pertanyaan jelas yang memerlukan AI lanjutan dihantar kepada AI awan.

## Ciri yang dirancang

- Mengawal lampu, soket, penyaman udara, bidai dan peranti lain melalui suara.
- Alias pelbagai bahasa.
- Pemasa yang diurus melalui suara.
- Pertanyaan tentang cuaca setempat.
- Memainkan dan mengawal muzik.
- Pilihan sandaran peribadi kepada model Ollama.
- Mengenali orang melalui suara.
- Ingatan konteks jangka panjang.
- Pilihan untuk menyerahkan pertanyaan kepada model AI awan.
- Sandaran dan pemantauan prestasi.

## Prinsip reka bentuk

- Arahan rumah pintar mesti berfungsi tanpa sambungan Internet.
- Pemproses niat setempat diutamakan berbanding LLM.
- Data audio dan perbualan peribadi sebaik-baiknya diproses secara setempat.
- Model awan hanya digunakan untuk pertanyaan yang diminta dengan jelas atau rumit, dan hanya jika pengguna mengaktifkannya secara jelas semasa mengkonfigurasi pembantu.
- Sistem mesti mengekalkan suhu dan kependaman yang stabil di bawah beban berterusan.

## Status projek

Projek ini ditakrifkan sebagai tunggakan fungsi. Konfigurasi khusus, automasi dan skrip penggunaan akan ditambah apabila cerita pengguna diselesaikan.
