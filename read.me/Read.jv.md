**Basa: Basa Jawa · [Bali menyang pilihan basa](../readme.md)**

# Asisten Omah Pinter Multibasa


**Waca nganggo basa:** [Basa Jawa](Read.jv.md) · [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Proyèk iki njlentrehaké cara masang ekosistem omah pinter lokal ing Raspberry Pi kanthi asisten swara multibasa.

## Asal-usulé jeneng Mina

**Mina** asalé saka oyod tembung basa Jermanik kuna *minna*, sing tegesé “pangeling-eling”, “tresna”, utawa “kenangan”. Jeneng iki uga ana ing basa liya: ing basa Persia, *mīnā* ana gandhèngané karo “cahya” utawa “kaca biru”, déné ing basa Jepang, *mina* tegesé “kabèh wong” utawa “kabèh bebarengan”.

Teges-teges iki nglambangaké **pangeling-eling bebarengan lan paguyuban**, nilai-nilai sing cocog karo asisten sing ngancani lan nyengkuyung urip saben dina ing omah.

Saka swarané, Mina alus nanging cetha. Jeneng iki diucapaké saben wanda, `Mi-na`, lan ora gampang kliru dirungokaké kaya tembung-tembung sing umum dienggo ing lingkungan omah.

## Tujuan

Nggawe sistem omah pinter sing njaga privasi, bisa dipercaya, lan cepet, supaya piranti omah bisa dikendhalèkaké nganggo printah swara tanpa kudu gumantung marang layanan méga.

Arsitekturé nggabungaké:

- Pangolahan lokal kanggo printah omah pinter lan njaga privasi.
- Kaprigelan lokal nganggo Ollama kanggo pitakon umum.
- Modhèl méga kanggo pitakon sing ruwet lan informasi paling anyar.

## Piranti keras

- Disaranaké Raspberry Pi 5 nganggo RAM 8 GB. Kompatibilitas winates nganti Raspberry Pi 3B+.
- Gunakna SSD NVMe, aja nganggo kertu SD. Dhukungan kanggo kertu SD winates.
- Mikrofon lan spiker USB rong arah.
- Piranti omah pinter sing cocog karo Zigbee, Matter, Philips Hue, utawa Wi-Fi lokal.
- Pendinginan aktif kanggo nyegah throttling amarga panas.

## Arsitektur

1. Home Assistant OS ngatur piranti lan otomatisasi.
2. openWakeWord ndeteksi tembung pangurip kanthi lokal.
3. Whisper nyalin printah swara dadi tulisan nganggo basa sing lagi aktif liwat Wyoming.
4. Prosesor maksud nglakokaké printah omah pinter sacara lokal.
5. Piper nyintesis wangsulan nganggo basa Katalan.
6. Ollama mangsuli pitakon umum tanpa ngirim data menyang internet.
7. Pitakon sing kanthi cetha mbutuhaké AI tingkat lanjut waé sing dikirim menyang AI méga.

## Fitur sing dirancang

- Ngendhalèkaké lampu, stopkontak, AC, tirai, lan piranti liyané nganggo swara.
- Jeneng liya ing manéka basa.
- Timer sing diatur nganggo swara.
- Njaluk ramalan cuaca lokal.
- Muter lan ngendhalèkaké musik.
- Ngalih kanthi privat menyang modhèl Ollama.
- Ngenali wong saka swarané.
- Élingan konteks jangka dawa.
- Pangoperan opsional menyang modhèl AI méga.
- Serepan lan ngawasi kinerja.

## Prinsip rancangan

- Printah omah pinter kudu bisa dienggo sanajan ora ana sambungan internet.
- Prosesor maksud lokal diutamakaké tinimbang LLM.
- Data swara lan pacelathon pribadi sabisa-bisa diproses sacara lokal.
- Modhèl méga mung dienggo kanggo pitakon sing dijaluk kanthi cetha utawa sing ruwet, lan mung yèn pangguna kanthi cetha ngaktifaké nalika nyetel asisten.
- Suhu lan wektu tanggepan sistem kudu tetep stabil nalika digunakaké terus-terusan.

## Status proyèk

Proyèk iki saiki dirumusaké minangka dhaptar gawéan fungsi. Konfigurasi rinci, otomatisasi, lan skrip panyebaran bakal ditambahaké nalika crita pangguna dirampungaké.
