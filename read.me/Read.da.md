**Dansk · [Tilbage til sprogvalg](../readme.md)**

# Flersproget assistent til det intelligente hjem

**Sprog:** Dansk

**Læs på:** [Catalansk](Read.ca.md) · [Engelsk](Read.en.md) · [Spansk](Read.es.md) · [Fransk](Read.fr.md) · [Tysk](Read.de.md) · [Italiensk](Read.it.md) · [Portugisisk](Read.pt.md) · [Hollandsk](Read.nl.md)

Dette projekt beskriver implementeringen af et lokalt hjemmeautomatiseringsøkosystem på en Raspberry Pi med en flersproget stemmeassistent.

## Oprindelsen af navnet Mina

**Mina** har rødder i det oldgermanske *minna*, som betyder „hukommelse“, „hengivenhed“ eller „minde“. Navnet findes også på andre sprog: På persisk forbindes *mīnā* med „lys“ eller „blåt glas“, og på japansk betyder *mina* „alle“ eller „alle sammen“.

Disse fortolkninger symboliserer **fælles hukommelse og fællesskab** – værdier, der passer til en assistent, som ledsager og støtter hverdagen i hjemmet.

Lydmæssigt er Mina et blødt, men tydeligt navn med stavelsesudtalen `Mi-na` og lille risiko for forveksling med almindelige ord i hjemmet.

## Formål

At skabe et privat, pålideligt og hurtigt hjemmeautomatiseringssystem, der gør det muligt at styre hjemmets enheder med stemmekommandoer uden obligatorisk afhængighed af cloudtjenester.

Arkitekturen kombinerer:

- Lokal behandling af hjemmeautomatiseringskommandoer og beskyttelse af privatlivet.
- Lokal intelligens med Ollama til generelle spørgsmål.
- Cloudmodeller til komplekse forespørgsler og opdaterede oplysninger.

## Hardware

- Raspberry Pi 5 med anbefalede 8 GB RAM. Begrænset kompatibilitet ned til Raspberry Pi 3B+.
- NVMe-SSD-disk uden brug af SD-kort. Begrænset kompatibilitet med SD-kort.
- Tovejs USB-mikrofon og højttaler.
- Hjemmeautomatiseringsenheder, der er kompatible med Zigbee, Matter, Philips Hue eller lokalt Wi-Fi.
- Aktiv køling for at undgå termisk neddrosling.

## Arkitektur

1. Home Assistant OS administrerer enheder og automatiseringer.
2. openWakeWord registrerer aktiveringsordet lokalt.
3. Whisper transskriberer kommandoer på det aktive sprog via Wyoming.
4. Intentionsprocessoren udfører hjemmeautomatiseringskommandoer lokalt.
5. Piper syntetiserer svarene på catalansk.
6. Ollama besvarer generelle spørgsmål uden at sende data til internettet.
7. Cloud-AI modtager kun udtrykkelige forespørgsler, der kræver avanceret AI.

## Planlagte funktioner

- Stemmestyring af lys, stikkontakter, klimaanlæg, persienner og andre enheder.
- Flersprogede aliasser.
- Stemmestyrede timere.
- Lokal vejrudsigtsforespørgsel.
- Afspilning og styring af musik.
- Privat reservefunktion med en Ollama-model.
- Genkendelse af personen via stemmen.
- Langtidshukommelse for kontekst.
- Valgfri videresendelse til en cloudbaseret AI-model.
- Sikkerhedskopiering og overvågning af ydeevnen.

## Designprincipper

- Hjemmeautomatiseringskommandoer skal fungere uden internetforbindelse.
- Den lokale intentionsprocessor har forrang frem for LLM'er.
- Lyddata og private samtaler behandles fortrinsvis lokalt.
- Cloudmodeller bruges kun til udtrykkelige eller komplekse forespørgsler, og kun hvis brugeren udtrykkeligt har anmodet om det under opsætningen af assistenten.
- Systemet skal opretholde stabile temperaturer og latenstider under vedvarende belastning.

## Projektstatus

Projektet er defineret som en funktionel backlog. Specifikke konfigurationer, automatiseringer og implementeringsscripts tilføjes, efterhånden som brugerhistorierne færdiggøres.
