**Bosanski · [Nazad na izbor jezika](../Read.md)**

# Višejezični asistent za pametni dom

**Jezik:** Bosanski

**Čitaj na:** [Katalonskom](Read.ca.md) · [Engleskom](Read.en.md) · [Španskom](Read.es.md) · [Francuskom](Read.fr.md) · [Njemačkom](Read.de.md) · [Italijanskom](Read.it.md) · [Portugalskom](Read.pt.md) · [Nizozemskom](Read.nl.md)

Ovaj projekat opisuje postavljanje lokalnog ekosistema kućne automatizacije na Raspberry Pi uređaju uz višejezičnog glasovnog asistenta.

## Porijeklo imena Mina

**Mina** potiče od starogermanskog korijena *minna*, koji znači „sjećanje“, „naklonost“ ili „uspomena“. Ime se javlja i u drugim jezicima: u perzijskom se *mīnā* povezuje sa „svjetlošću“ ili „plavim staklom“, a u japanskom *mina* znači „svi“ ili „svi zajedno“.

Ova tumačenja simboliziraju **zajedničko sjećanje i zajednicu**, vrijednosti koje odgovaraju asistentu koji prati i podržava svakodnevni život u domu.

Zvučno gledano, Mina je nježno, ali jasno ime, sa slogovnim izgovorom `Mi-na` i malom vjerovatnoćom da se u kućnom okruženju pomiješa s uobičajenim riječima.

## Cilj

Napraviti privatan, pouzdan i brz sistem kućne automatizacije koji omogućava upravljanje kućnim uređajima glasovnim komandama, bez obavezne zavisnosti od usluga u oblaku.

Arhitektura objedinjuje:

- Lokalnu obradu za komande kućne automatizacije i zaštitu privatnosti.
- Lokalnu inteligenciju uz Ollama za opšta pitanja.
- Modele u oblaku za složene upite i ažurirane informacije.

## Hardver

- Raspberry Pi 5 sa preporučenih 8 GB RAM-a. Ograničena kompatibilnost do Raspberry Pi 3B+.
- NVMe SSD disk bez korištenja SD kartice. Ograničena kompatibilnost sa SD karticom.
- Dvosmjerni USB mikrofon i zvučnik.
- Uređaji kućne automatizacije kompatibilni sa Zigbee, Matter, Philips Hue ili lokalnim Wi-Fi-jem.
- Aktivno hlađenje radi sprečavanja termičkog usporavanja.

## Arhitektura

1. Home Assistant OS upravlja uređajima i automatizacijama.
2. openWakeWord lokalno prepoznaje riječ za aktivaciju.
3. Whisper transkribuje komande na aktivnom jeziku putem Wyoming-a.
4. Procesor namjera lokalno izvršava komande kućne automatizacije.
5. Piper sintetizira odgovore na katalonskom.
6. Ollama odgovara na opšta pitanja bez slanja podataka na internet.
7. AI u oblaku prima samo izričite upite koji zahtijevaju napredni AI.

## Planirane funkcionalnosti

- Glasovno upravljanje svjetlima, utičnicama, klimatizacijom, roletnama i drugim uređajima.
- Višejezični aliasi.
- Glasovno upravljani tajmeri.
- Lokalni upit o vremenskoj prognozi.
- Reprodukcija i upravljanje muzikom.
- Privatni rezervni izbor modela Ollama.
- Prepoznavanje osobe po glasu.
- Dugoročna memorija konteksta.
- Opcionalno prosljeđivanje modelu AI-ja u oblaku.
- Sigurnosne kopije i nadzor performansi.

## Principi dizajna

- Komande kućne automatizacije moraju raditi bez internetske veze.
- Lokalni procesor namjera ima prednost nad LLM-ovima.
- Audio podaci i privatni razgovori obrađuju se prvenstveno lokalno.
- Modeli u oblaku koriste se samo za izričite ili složene upite, i to samo ako je korisnik to izričito zatražio prilikom podešavanja asistenta.
- Sistem mora održavati stabilne temperature i kašnjenja pri kontinuiranom opterećenju.

## Status projekta

Projekat je definisan kao funkcionalni backlog. Konkretne konfiguracije, automatizacije i skripte za postavljanje dodavat će se kako se korisničke priče budu završavale.
