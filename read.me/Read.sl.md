**Slovenščina · [Nazaj na izbiro jezika](../readme.md)**

# Večjezični pomočnik za pametni dom

**Jezik:** slovenščina

**Beri v:** [Katalonščini](Read.ca.md) · [Angleščini](Read.en.md) · [Španščini](Read.es.md) · [Francoščini](Read.fr.md) · [Nemščini](Read.de.md) · [Italijanščini](Read.it.md) · [Portugalščini](Read.pt.md) · [Nizozemščini](Read.nl.md)

Ta projekt opisuje vzpostavitev lokalnega ekosistema za avtomatizacijo doma na napravi Raspberry Pi z večjezičnim glasovnim pomočnikom.

## Izvor imena Mina

**Mina** izvira iz starogermanske besede *minna*, ki pomeni »spomin«, »naklonjenost« ali »spominjanje«. Pojavlja se tudi v drugih jezikih: v perzijščini je *mīnā* povezano s »svetlobo« ali »modrim steklom«, v japonščini pa *mina* pomeni »vsi« ali »vsi skupaj«.

Te razlage simbolizirajo **skupni spomin in skupnost**, vrednoti, skladni s pomočnikom, ki spremlja in podpira vsakdanje življenje doma.

Po zvenu je Mina nežno, a jasno ime s skladenjsko izgovarjavo `Mi-na` in majhno verjetnostjo zamenjave z običajnimi besedami v domačem okolju.

## Cilj

Ustvariti zaseben, zanesljiv in hiter sistem za avtomatizacijo doma, ki omogoča upravljanje domačih naprav z glasovnimi ukazi brez obvezne odvisnosti od storitev v oblaku.

Arhitektura združuje:

- Lokalno obdelavo ukazov za avtomatizacijo doma in varovanje zasebnosti.
- Lokalno inteligenco z Ollama za splošna vprašanja.
- Modele v oblaku za zahtevna vprašanja in posodobljene informacije.

## Strojna oprema

- Raspberry Pi 5 s priporočenimi 8 GB RAM-a. Omejena združljivost do Raspberry Pi 3B+.
- Disk SSD NVMe brez uporabe kartice SD. Omejena združljivost s kartico SD.
- Dvosmerni mikrofon in zvočnik USB.
- Naprave za avtomatizacijo doma, združljive z Zigbee, Matter, Philips Hue ali lokalnim omrežjem Wi-Fi.
- Aktivno hlajenje za preprečevanje toplotnega zmanjšanja zmogljivosti.

## Arhitektura

1. Home Assistant OS upravlja naprave in avtomatizacije.
2. openWakeWord lokalno zazna aktivacijsko besedo.
3. Whisper prek Wyoming prepiše ukaze v aktivnem jeziku.
4. Procesor namenov lokalno izvede ukaze za avtomatizacijo doma.
5. Piper sintetizira odgovore v katalonščini.
6. Ollama odgovarja na splošna vprašanja, ne da bi podatke pošiljal v internet.
7. Umetna inteligenca v oblaku prejme samo izrecna vprašanja, ki zahtevajo napredno UI.

## Načrtovane funkcionalnosti

- Glasovno upravljanje luči, vtičnic, klimatizacije, rolet in drugih naprav.
- Večjezična nadomestna imena.
- Glasovno upravljani časovniki.
- Lokalni vremenski podatki.
- Predvajanje in upravljanje glasbe.
- Zasebna nadomestna možnost z modelom Ollama.
- Prepoznavanje osebe po glasu.
- Dolgoročni spomin konteksta.
- Neobvezna preusmeritev na model umetne inteligence v oblaku.
- Varnostne kopije in spremljanje zmogljivosti.

## Načela oblikovanja

- Ukazi za avtomatizacijo doma morajo delovati brez internetne povezave.
- Lokalni procesor namenov ima prednost pred LLM-i.
- Zvočni podatki in zasebni pogovori se prednostno obdelujejo lokalno.
- Modeli v oblaku se uporabljajo samo za izrecna ali zahtevna vprašanja in samo, če je uporabnik to izrecno zahteval med nastavitvijo pomočnika.
- Sistem mora pri neprekinjeni obremenitvi vzdrževati stabilne temperature in zakasnitve.

## Stanje projekta

Projekt je opredeljen kot funkcionalni backlog. Določene konfiguracije, avtomatizacije in namestitveni skripti bodo dodani, ko bodo uporabniške zgodbe zaključene.
