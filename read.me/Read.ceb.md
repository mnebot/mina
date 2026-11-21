**Pinulongan: Sinugboanon · [Balik sa pagpili og pinulongan](../readme.md)**

# Multilingguwal nga Smart Home Assistant


**Basaha sa:** [Sinugboanon](Read.ceb.md) · [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Gihulagway niini nga proyekto ang pagpatuman og lokal nga smart home ecosystem sa Raspberry Pi, uban sa voice assistant nga makasabot og daghang pinulongan.

## Sinugdanan sa ngalan nga Mina

Ang **Mina** naggikan sa karaang gamot sa pulong nga *minna* sa pinulongang Germanic, nga nagpasabot og “panumduman,” “pagmahal,” o “handumanan.” Anaa usab kini nga ngalan sa ubang pinulongan: sa Persian, may kalabotan ang *mīnā* sa “kahayag” o “asul nga bildo,” ug sa Japanese, ang *mina* nagpasabot og “tanan” o “tanang tawo nga nagkahiusa.”

Kini nga mga kahulogan nagsimbolo sa **gipaambit nga panumduman ug komunidad**, mga prinsipyo nga nahiuyon sa assistant nga mouban ug mosuporta sa adlaw-adlaw nga kinabuhi sa panimalay.

Sa paminawon, humok apan klaro ang ngalan nga Mina. Litokon kini matag silaba nga `Mi-na`, ug gamay ra ang posibilidad nga masayop kini sa kasagarang mga pulong nga gigamit sa balay.

## Tumong

Maghimo og pribado, kasaligan, ug paspas nga smart home system aron makontrol ang mga gamit sa balay pinaagi sa mga sugo sa tingog, nga dili kinahanglan mosalig sa mga serbisyo sa cloud.

Gihiusa sa arkitektura ang:

- Lokal nga pagproseso sa mga sugo sa smart home ug pagpanalipod sa pribasiya.
- Lokal nga paniktik gamit ang Ollama alang sa kinatibuk-ang mga pangutana.
- Mga cloud model alang sa komplikadong pangutana ug bag-ong impormasyon.

## Hardware

- Girekomenda ang Raspberry Pi 5 nga adunay 8 GB nga RAM. Limitado ang pagkaangay hangtod sa Raspberry Pi 3B+.
- Gamita ang NVMe SSD ug ayaw paggamit og SD card. Limitado ang suporta sa SD card.
- Bidirectional nga USB microphone ug speaker.
- Mga smart home device nga compatible sa Zigbee, Matter, Philips Hue, o lokal nga Wi-Fi.
- Aktibong pagpabugnaw aron malikayan ang paghinay tungod sa kainit.

## Arkitektura

1. Ang Home Assistant OS maoy modumala sa mga device ug automation.
2. Lokal nga makamatikod ang openWakeWord sa wake word.
3. I-transcribe sa Whisper ang mga sugo sa aktibong pinulongan pinaagi sa Wyoming.
4. Lokal nga ipatuman sa intent processor ang mga sugo sa smart home.
5. Maghimo ang Piper og sinultihang tubag sa Catalan.
6. Motubag ang Ollama sa kinatibuk-ang mga pangutana nga walay datos nga ipadala sa Internet.
7. Ang mga pangutana lamang nga tin-aw nga nanginahanglan og advanced AI ipadala ngadto sa cloud AI.

## Giplanong mga feature

- Kontrol sa mga suga, saksakan, air conditioning, blinds, ug uban pang device pinaagi sa tingog.
- Mga alias sa daghang pinulongan.
- Mga timer nga madumala pinaagi sa tingog.
- Pangutana bahin sa lokal nga panahon.
- Pagpatugtog ug pagkontrol sa musika.
- Pribadong pagbalhin ngadto sa Ollama model.
- Pag-ila sa tawo pinaagi sa tingog.
- Dugayng memorya sa konteksto.
- Opsyonal nga pagpaagi sa pangutana ngadto sa cloud AI model.
- Backup ug pagmonitor sa performance.

## Mga prinsipyo sa disenyo

- Kinahanglang molihok ang mga sugo sa smart home bisan walay koneksyon sa Internet.
- Unahon ang lokal nga intent processor kaysa sa mga LLM.
- Iproseso sa lokal kutob sa mahimo ang audio data ug pribadong panag-istoryahanay.
- Ang mga cloud model gamiton lamang sa tin-aw nga gihangyo o komplikadong mga pangutana, ug kung tin-aw nga gi-enable kini sa user sa pag-configure sa assistant.
- Kinahanglang magpabiling lig-on ang temperatura ug latency sa sistema ubos sa padayon nga load.

## Kahimtang sa proyekto

Gihubit ang proyekto isip usa ka backlog sa mga feature. Idugang ang espesipikong mga configuration, automation, ug deployment script samtang mahuman ang mga user story.
