**Srpski** · [Nazad na izbor jezika](../Read.md)

# Višejezični kućni pomoćnik

Ovaj projekat opisuje lokalno postavljanje ekosistema višjezičnog glasovnog pomoćnika na Raspberry Pi.

## Poreklo imena Mina

**Mina** ima starogermanski koren u *minna*, što znači „sećanje“, „privrženost“ ili „uspomena“. Prisutno je i u drugim jezicima: na persijskom, *mīnā* se povezuje sa „svetlošću“ ili „plavim staklom“, a na japanskom *mina* znači „svi“ ili „svi zajedno“.

Ova tumačenja simbolizuju **zajedničko sećanje i zajednicu**, vrednosti u skladu sa pomoćnikom koji prati i podržava svakodnevni život domaćinstva.

Po zvuku, Mina je mekano, ali jasno ime, sa slogovnim izgovorom `Mi-na` i malom verovatnoćom zabune sa uobičajenim rečima u kućnom okruženju.

## Cilj

Stvoriti privatni, pouzdani i brz kućni sistem koji omogućava upravljanje uređajima glasovnim komandama bez obavezne zavisnosti od cloud usluga.

Arhitektura kombinuje:

- Lokalnu obradu kućnih komandi i privatnosti.
- Lokalnu inteligenciju sa Ollama za opšta pitanja.
- Cloud modele za složena pitanja i ažurne informacije.

## Hardver

- Raspberry Pi 5 sa 8 GB RAM-a preporučeno. Ograničena kompatibilnost do Raspberry Pi 3B+.
- NVMe SSD bez upotrebe SD kartice. Ograničena kompatibilnost sa SD karticom.
- Dvostruji USB mikrofon i zvučnik.
- Kućni uređaji kompatibilni sa Zigbee, Matter, Philips Hue ili lokalnim Wi-Fi.
- Aktivno hlađenje radi sprečavanja termičkog throttlinga.

## Arhitektura

1. Home Assistant OS upravlja uređajima i automatizacijama.
2. openWakeWord lokalno otkriva aktivacijsku reč.
3. Whisper preko Wyoming transkribuje komande na aktivnom jeziku.
4. Procesor namera lokalno izvršava kućne komande.
5. Piper sintetiše odgovore na srpskom.
6. Ollama rešava opšta pitanja bez slanja podataka na Internet.
7. Cloud AI prima samo izričite upite koji zahtevaju naprednu veštačku inteligenciju.

## Planirane funkcije

- Glasovno upravljanje svetlima, utičnicama, klimatizacijom, roletnama i drugim uređajima.
- Višejezični pseudonimi.
- Tajmeri upravljani glasom.
- Lokalno pretraživanje vremena.
- Reprodukcija i upravljanje muzikom.
- Privatni fallback na Ollama model.
- Prepoznavanje osobe po glasu.
- Dugoročna memorija konteksta.
- Izborno preusmeravanje na cloud AI model.
- Rezervne kopije i nadzor performansi.

## Principi dizajna

- Kućne komande moraju raditi bez Internet veze.
- Lokalni procesor namera ima prednost nad LLM modelima.
- Zvučni podaci i privatni razgovori treba da se obrađuju lokalno.
- Cloud modeli se koriste samo za izričite ili složene upite i samo ako je korisnik to izričito zahtevao pri podešavanju pomoćnika.
- Sistem mora održavati stabilne temperature i latencije pod stalnim opterećenjem.

## Status projekta

Projekt je definisan kao funkcionalna lista zadataka. Specifične konfiguracije, automatizacije i skripte za implementaciju dodavaće se kako se korisničke priče završavaju.
