**Basa: Basa Sunda · [Balik ka pilihan basa](../Read.md)**

# Asistén Imah Pinter Multibasa


**Baca dina:** [Basa Sunda](Read.su.md) · [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Proyék ieu ngajelaskeun cara masang ékosistem imah pinter lokal dina Raspberry Pi, dilengkepan ku asistén sora multibasa.

## Asal-usul ngaran Mina

**Mina** asalna tina akar kecap *minna* dina basa Jérmanik kuna, anu hartina “ingetan”, “kanyaah”, atawa “pangéling-ngéling”. Ngaran ieu ogé kapanggih dina basa séjén: dina basa Pérsia, *mīnā* patali jeung “cahaya” atawa “kaca biru”, ari dina basa Jepang, *mina* hartina “kabéh jalma” atawa “saréréa babarengan”.

Harti-harti éta ngalambangkeun **ingetan babarengan jeung masarakat**, ajén-inajén anu saluyu jeung asistén anu marengan sarta ngarojong kahirupan sapopoé di imah.

Tina jihat sorana, Mina kadéngé hipu tapi écés. Diucapkeun unggal engangna jadi `Mi-na`, sarta leutik kamungkinan kasaruakeun jeung kecap anu ilahar dipaké di imah.

## Tujuan

Nyieun sistem imah pinter anu ngajaga karusiahan, bisa dipercaya, sarta gancang, sangkan alat-alat di imah bisa dikadalikeun ku paréntah sora tanpa kudu ngandelkeun jasa awan.

Arsitéktur ieu ngahijikeun:

- Ngolah paréntah imah pinter sacara lokal sarta ngajaga karusiahan.
- Ngagunakeun Ollama pikeun ngajawab pananya umum sacara lokal.
- Ngagunakeun modél awan pikeun pananya anu ruwet jeung informasi panganyarna.

## Pakakas

- Disarankeun Raspberry Pi 5 kalawan RAM 8 GB. Kasaluyuan kawates nepi ka Raspberry Pi 3B+.
- Ngagunakeun SSD NVMe, henteu maké kartu SD. Pangrojong pikeun kartu SD kawates.
- Mikropon jeung spéker USB dua arah.
- Alat imah pinter anu cocog jeung Zigbee, Matter, Philips Hue, atawa Wi-Fi lokal.
- Pendinginan aktip pikeun nyegah throttling termal.

## Arsitéktur

1. Home Assistant OS ngatur alat jeung otomatisasi.
2. openWakeWord ngadeteksi kecap hudang sacara lokal.
3. Whisper ngarobah paréntah sora jadi tulisan dina basa anu keur aktip ngaliwatan Wyoming.
4. Prosésor maksud ngajalankeun paréntah imah pinter sacara lokal.
5. Piper nyintésis jawaban dina basa Katalan.
6. Ollama ngajawab pananya umum tanpa ngirim data ka internét.
7. Ngan pananya anu écés merlukeun AI tingkat lanjut anu dikirim ka AI awan.

## Fitur anu direncanakeun

- Ngadalikeun lampu, stop kontak, AC, hordéng, jeung alat séjén ku sora.
- Ngaran alias multibasa.
- Timer anu dikokolakeun ku sora.
- Nanyakeun cuaca lokal.
- Muterkeun jeung ngadalikeun musik.
- Pindah sacara pribadi ka modél Ollama.
- Mikawanoh jalma tina sorana.
- Émutan kontéks jangka panjang.
- Bisa milih ngirimkeun pananya ka modél AI awan.
- Nyieun cadangan jeung ngawas kinerja.

## Prinsip rarancang

- Paréntah imah pinter kudu bisa jalan sanajan teu aya sambungan internét.
- Prosésor maksud lokal diutamakeun tibatan LLM.
- Data audio jeung paguneman pribadi sabisa-bisa diolah sacara lokal.
- Modél awan ngan dipaké pikeun pananya anu dipénta kalawan écés atawa anu ruwet, sarta ngan lamun pamaké sacara écés ngaktipkeunana nalika nyetél asistén.
- Suhu jeung laténsi sistem kudu tetep ajeg dina beban anu terus-terusan.

## Status proyék

Proyék ieu ditetepkeun minangka daptar pagawéan fungsional. Konfigurasi husus, otomatisasi, jeung skrip panyebaran bakal ditambahkeun sabada carita pamaké réngsé.
