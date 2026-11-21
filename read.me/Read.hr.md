**Hrvatski · [Natrag na odabir jezika](../Read.md)**

# Višejezični asistent za pametni dom

**Jezik:** hrvatski

**Čitaj na:** [Katalonskom](Read.ca.md) · [Engleskom](Read.en.md) · [Španjolskom](Read.es.md) · [Francuskom](Read.fr.md) · [Njemačkom](Read.de.md) · [Talijanskom](Read.it.md) · [Portugalskom](Read.pt.md) · [Nizozemskom](Read.nl.md)

Ovaj projekt opisuje postavljanje lokalnog ekosustava kućne automatizacije na Raspberry Pi uređaju s višejezičnim glasovnim asistentom.

## Podrijetlo imena Mina

**Mina** potječe od starogermanskog korijena *minna*, koji znači „sjećanje“, „naklonost“ ili „uspomena“. Ime se pojavljuje i u drugim jezicima: na perzijskom se *mīnā* povezuje sa „svjetlom“ ili „plavim staklom“, a na japanskom *mina* znači „svi“ ili „svi zajedno“.

Ova tumačenja simboliziraju **zajedničko sjećanje i zajednicu**, vrijednosti koje odgovaraju asistentu koji prati i podupire svakodnevni život u domu.

Zvučno gledano, Mina je nježno, ali jasno ime, slogovnog izgovora `Mi-na`, s malom vjerojatnošću zamjene s uobičajenim riječima u kućnom okruženju.

## Cilj

Stvoriti privatan, pouzdan i brz sustav kućne automatizacije koji omogućuje upravljanje kućnim uređajima glasovnim naredbama bez obvezne ovisnosti o uslugama u oblaku.

Arhitektura objedinjuje:

- Lokalnu obradu naredbi kućne automatizacije i zaštitu privatnosti.
- Lokalnu inteligenciju uz Ollama za opća pitanja.
- Modele u oblaku za složene upite i ažurirane informacije.

## Hardver

- Raspberry Pi 5 s preporučenih 8 GB RAM-a. Ograničena kompatibilnost do Raspberry Pi 3B+.
- NVMe SSD disk bez korištenja SD kartice. Ograničena kompatibilnost sa SD karticom.
- Dvosmjerni USB mikrofon i zvučnik.
- Uređaji kućne automatizacije kompatibilni sa Zigbee, Matter, Philips Hue ili lokalnim Wi-Fi-jem.
- Aktivno hlađenje radi sprječavanja termičkog usporavanja.

## Arhitektura

1. Home Assistant OS upravlja uređajima i automatizacijama.
2. openWakeWord lokalno prepoznaje riječ za aktivaciju.
3. Whisper transkribira naredbe na aktivnom jeziku putem Wyoming-a.
4. Procesor namjera lokalno izvršava naredbe kućne automatizacije.
5. Piper sintetizira odgovore na katalonskom.
6. Ollama odgovara na opća pitanja bez slanja podataka na internet.
7. Umjetna inteligencija u oblaku prima samo izričite upite koji zahtijevaju naprednu umjetnu inteligenciju.

## Planirane funkcionalnosti

- Glasovno upravljanje svjetlima, utičnicama, klimatizacijom, roletama i drugim uređajima.
- Višejezični aliasi.
- Glasovno upravljani mjerači vremena.
- Lokalni upit o vremenskoj prognozi.
- Reprodukcija i upravljanje glazbom.
- Privatni rezervni izbor modela Ollama.
- Prepoznavanje osobe prema glasu.
- Dugoročna memorija konteksta.
- Neobavezno prosljeđivanje modelu umjetne inteligencije u oblaku.
- Sigurnosne kopije i nadzor performansi.

## Načela dizajna

- Naredbe kućne automatizacije moraju raditi bez internetske veze.
- Lokalni procesor namjera ima prednost pred LLM-ovima.
- Audio podaci i privatni razgovori obrađuju se prvenstveno lokalno.
- Modeli u oblaku koriste se samo za izričite ili složene upite, i to samo ako je korisnik to izričito zatražio pri konfiguriranju asistenta.
- Sustav mora održavati stabilne temperature i latencije pri kontinuiranom opterećenju.

## Stanje projekta

Projekt je definiran kao funkcionalni backlog. Konkretne konfiguracije, automatizacije i skripte za postavljanje dodavat će se kako se korisničke priče budu dovršavale.
