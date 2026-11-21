**Papiamento · [Bai bek pa skohe idioma](../Read.md)**
# Asistente di kas inteligente den diferente idioma

**Idioma:** Papiamento

**Les’e den:** [Papiamento](Read.pap.md) · [English](Read.en.md) · [Català](Read.ca.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

E proyekto aki ta deskribí kon pa instalá un ekosistema di kas inteligente lokal riba un Raspberry Pi, ku un asistente di bos ku ta papia diferente idioma.

## Origen di e nomber Mina

**Mina** tin su rais den e palabra germániko antiguo *minna*, ku ta nifiká «memoria», «afekto» òf «rekuerdo». E ta aparesé tambe den otro idioma: na persa, *mīnā* ta relashoná ku «lus» òf «glas blou»; na japonés, *mina* ta nifiká «tur hende» òf «tur huntu».

E interpretashonnan aki ta simbolisá **memoria komun i komunidat**, balornan ku ta kuadra ku un asistente ku ta akompañá i sostené bida diario di kas.

Mina ta un nomber suave pero kla ora bo bisa’é: ta pronunsiá den dos sílaba, `Mi-na`, i tin tiki chens pa konfundi’é ku palabra ku ta usá hopi den kas.

## Meta

Krea un sistema di kas inteligente privá, konfiabel i lihé ku ta permití kontrolá aparato di kas ku òrdu di bos, sin dependensia obligá di servisio den nube.

E arkitektura ta kombiná:

- Prosessamentu lokal pa òrdu di kas inteligente i privasidat.
- Inteligensia lokal ku Ollama pa pregunta general.
- Modelo den nube pa pregunta kompliká i informashon aktualisá.

## Hardware

- Raspberry Pi 5 ku 8 GB RAM ta rekomendá. Kompatibilidat limitá te ku Raspberry Pi 3B+.
- Disk SSD NVMe sin usa karta SD. Kompatibilidat limitá ku karta SD.
- Mikrófono i altavoz USB bidirekshonal.
- Aparato di kas inteligente kompatibel ku Zigbee, Matter, Philips Hue òf Wi-Fi lokal.
- Refreskamentu aktivo pa prevení ku kalor ta baha e prestashon.

## Arkitektura

1. Home Assistant OS ta atendé aparato i automatizashon.
2. openWakeWord ta deskubrí palabra di aktivashon lokalmente.
3. Whisper ta transkribí òrdu den e idioma aktivo pa medio di Wyoming.
4. E prosesadó di intenshon ta ehèkutá òrdu di kas inteligente lokalmente.
5. Piper ta produsí kontesta papia na katalan.
6. Ollama ta kontestá pregunta general sin manda dato pa Internet.
7. IA den nube ta risibí solamente pregunta eksplísito ku ta rekerí IA avansá.

## Funshon ku ta na plan

- Kontrolá lus, tomakorriente, klima, persiana i otro aparato ku bos.
- Alyas den diferente idioma.
- Temporisadó ku òrdu di bos.
- Konsulta meteo lokal.
- Toka i kontrolá músika.
- Alternativa privá ku un modelo di Ollama.
- Rekonosé persona pa medio di bos.
- Memoria di kontèsto pa largu término.
- Mandamentu opshonal pa un modelo di IA den nube.
- Kopia di seguridat i monitoreo di prestashon.

## Prinsipio di diseño

- Òrdu di kas inteligente mester funshoná sin konekshon na Internet.
- E prosesadó lokal di intenshon tin prioridat riba e LLM.
- Dato di audio i konversashon privá ta wordu prosesá preferiblemente lokalmente.
- Modelo den nube ta usa solamente pa pregunta eksplísito òf kompliká, i solamente si e usuario a pidi esaki eksplísitamente ora a konfigura e asistente.
- E sistema mester mantené temperatura i latensia stabil bou di karga kontinuo.

## Estado di proyekto

E proyekto ta definí komo un backlog funshonal. Konfigurashon spesífiko, automatizashon i script di despliegue lo agregá segun ku ta kompletá e historia di usuario.
