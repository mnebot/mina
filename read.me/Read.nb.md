**Norsk bokmål** · [Tilbake til språkvalget](../readme.md)

# Flerspråklig hjemmeassistent

Dette prosjektet beskriver utplassering av et lokalt økosystem for en flerspråklig taleassistent på en Raspberry Pi.

## Opprinnelsen til navnet Mina

**Mina** har en gammalgermansk rot i *minna*, som betyr «minne», «kjærlighet» eller «erindring». Navnet finnes også i andre språk: på persisk forbindes *mīnā* med «lys» eller «blått glass», og på japansk betyr *mina* «alle» eller «alle sammen».

Disse betydningene symboliserer en **delt hukommelse og et fellesskap**, verdier som passer en assistent som følger og støtter hverdagslivet i hjemmet.

Når det gjelder klang, er Mina et mykt, men tydelig navn, med stavelseuttalen `Mi-na` og liten sannsynlighet for forveksling med vanlige ord i hjemmet.

## Mål

Skape et privat, pålitelig og raskt system for hjemmet som gjør det mulig å styre husholdningsenheter med tale kommandoer uten å være avhengig av skytjenester.

Arkitekturen kombinerer:

- Lokal behandling av hjemmekommandoer og personvern.
- Lokal intelligens med Ollama for generelle spørsmål.
- Skymodeller for komplekse spørsmål og oppdatert informasjon.

## Maskinvare

- Raspberry Pi 5 med 8 GB RAM anbefales. Begrenset kompatibilitet opp til Raspberry Pi 3B+.
- NVMe SSD uten SD-kort. Begrenset kompatibilitet med SD-kort.
- Toveis USB-mikrofon og høyttaler.
- Hjemmeenheter som støtter Zigbee, Matter, Philips Hue eller lokalt Wi-Fi.
- Aktiv kjøling for å unngå termisk nedbremsing.

## Arkitektur

1. Home Assistant OS styrer enhetene og automatiseringene.
2. openWakeWord oppdager aktiveringsordet lokalt.
3. Whisper transkriberer kommandoer på det aktive språket via Wyoming.
4. Intensjonsprosessoren kjører hjemmekommandoer lokalt.
5. Piper syntetiserer svar på valgt språk.
6. Ollama løser generelle spørsmål uten å sende data til Internett.
7. Skybasert KI får bare eksplisitte forespørsler som krever avansert KI.

## Planlagte funksjoner

- Tale kontroll av lys, stikkontakter, klimaanlegg, persienner og andre enheter.
- Flerspråklige aliaser.
- Stemmesstyrte tidtakere.
- Lokale værforespørsler.
- Musikkavspilling og kontroll.
- Privat tilbakefall til en Ollama-modell.
- Persongjenkjennelse ved stemmen.
- Langsiktig kontekstminne.
- Valgfri videresending til en skybasert KI-modell.
- Sikkerhetskopiering og ytelsesovervåking.

## Designprinsipper

- Hjemmekommandoer må fungere uten internettforbindelse.
- Den lokale intensjonsprosessoren har prioritet over LLM-er.
- Lyddata og private samtaler bør behandles lokalt.
- Skymodeller brukes bare for eksplisitte eller komplekse forespørsler, og bare hvis brukeren har bedt om det uttrykkelig ved konfigurering.
- Systemet må holde stabile temperaturer og responstider under kontinuerlig belastning.

## Prosjektstatus

Prosjektet er definert som en funksjonell backlog. Spesifikke konfigurasjoner, automatiseringer og distribusjonsskript må legges til etter hvert som brukerhistoriene fullføres.
