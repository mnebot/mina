**Norsk nynorsk** · [Tilbake til språkvalet](../Read.md)

# Fleirspråkleg heimeassistent

Dette prosjektet skildrar utplassering av eit lokalt økosystem for ein fleirspråkleg taleassistent på ein Raspberry Pi.

## Opphavet til namnet Mina

**Mina** har ei gammalgermansk rot i *minna*, som tyder «minne», «kjærleik» eller «erindring». Namnet finst også i andre språk: på persisk er *mīnā* knytt til «lys» eller «blått glas», og på japansk betyr *mina* «alle» eller «alle saman».

Desse tolkingane symboliserer ei **delt minne og eit fellesskap**, verdiar som passar ein assistent som følgjer og støttar kvardagslivet i heimen.

Når det gjeld klang, er Mina eit mjukt men tydleg namn, med stavingsuttalen `Mi-na` og liten sannsyn for forveksling med vanlege ord i heimen.

## Mål

Skape eit privat, påliteleg og raskt heimesystem som let brukaren styra heimeeiningar med tale kommandoar utan å vera avhengig av skytjenester.

Arkitekturen kombinerer:

- Lokal behandling av heimekommandoar og personvern.
- Lokal intelligens med Ollama for allmenne spørsmål.
- Skymodellar for komplekse spørsmål og oppdatert informasjon.

## Maskinvare

- Raspberry Pi 5 med 8 GB RAM er tilrådd. Avgrensa kompatibilitet opp til Raspberry Pi 3B+.
- NVMe SSD utan SD-kort. Avgrensa kompatibilitet med SD-kort.
- Tovegs USB-mikrofon og høgtalar.
- Heimeeiningar som støttar Zigbee, Matter, Philips Hue eller lokalt Wi-Fi.
- Aktiv kjøling for å unngå termisk nedbremsing.

## Arkitektur

1. Home Assistant OS styrer einingane og automatiseringane.
2. openWakeWord oppdagar aktiveringsordet lokalt.
3. Whisper transkriberer kommandoar på det aktive språket via Wyoming.
4. Intensjonsprosessoren køyrer heimekommandoar lokalt.
5. Piper syntetiserer svar på valt språk.
6. Ollama løysar allmenne spørsmål utan å senda data til Internett.
7. Skybasert KI får berre uttrykte førespurnader som krev avansert KI.

## Planlagde funksjonar

- Talestyring av lys, stikkkontaktar, klimaanlegg, persienner og andre einingar.
- Fleirspråklege aliasar.
- Taletstyrte tidsur.
- Lokale vêrspørsmål.
- Musikkavspeling og kontroll.
- Privat fallback til ein Ollama-modell.
- Personattkjenning etter røyst.
- Langsiktig kontekstminne.
- Valfri videresending til ein skybasert KI-modell.
- Sikkerheitskopiering og ytingsovervaking.

## Designprinsipp

- Heimekommandoar må fungera utan internettforbindelse.
- Den lokale intensjonsprosessoren har prioritet framfor LLM-ar.
- Lyddata og private samtalar bør handsamast lokalt.
- Skymodellar blir brukte berre for uttrykte eller komplekse førespurnader, og berre dersom brukaren har bedt om det ved oppsett.
- Systemet må halda stabile temperaturar og svartider under kontinuerleg belastning.

## Prosjektstatus

Prosjektet er definert som ein funksjonell backlog. Spesifikke oppsett, automatiseringar og distribusjonsskript må leggast til etter kvart som brukarhistoriene blir fullførte.
