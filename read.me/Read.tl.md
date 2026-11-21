**Wika: Filipino/Tagalog · [Bumalik sa pagpili ng wika](../readme.md)**

# Multilingual na Smart Home Assistant


**Basahin sa:** [Filipino/Tagalog](Read.tl.md) · [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Inilalarawan ng proyektong ito ang pagbuo ng lokal na smart home ecosystem sa Raspberry Pi, kasama ang isang voice assistant na maraming wika ang sinusuportahan.

## Pinagmulan ng pangalang Mina

Nagmula ang **Mina** sa sinaunang ugat na salitang Germanic na *minna*, na nangangahulugang “alaala,” “pagmamahal,” o “paggunita.” Matatagpuan din ang pangalang ito sa ibang mga wika: sa Persian, may kaugnayan ang *mīnā* sa “liwanag” o “asul na salamin,” at sa Japanese, nangangahulugan ang *mina* ng “lahat” o “sama-sama ang lahat.”

Sumasagisag ang mga kahulugang ito sa **pinagsasaluhang alaala at komunidad**, mga pagpapahalagang kaayon ng isang assistant na umaagapay at sumusuporta sa pang-araw-araw na buhay sa tahanan.

Sa tunog, banayad ngunit malinaw ang pangalang Mina. Binibigkas ito sa mga pantig na `Mi-na`, at maliit ang posibilidad na mapagkamalan ito sa karaniwang mga salita sa loob ng tahanan.

## Layunin

Lumikha ng pribado, maaasahan, at mabilis na smart home system na nagbibigay-daan sa pagkontrol ng mga device sa bahay gamit ang mga utos sa boses, nang hindi kinakailangang umasa sa mga cloud service.

Pinagsasama ng arkitektura ang:

- Lokal na pagproseso ng mga utos para sa smart home at proteksyon ng privacy.
- Lokal na paghawak ng mga pangkalahatang tanong gamit ang Ollama.
- Mga cloud model para sa masalimuot na tanong at napapanahong impormasyon.

## Hardware

- Inirerekomenda ang Raspberry Pi 5 na may 8 GB RAM. Limitado ang compatibility hanggang Raspberry Pi 3B+.
- Gumamit ng NVMe SSD at huwag gumamit ng SD card. Limitado ang suporta sa SD card.
- Bidirectional na USB microphone at speaker.
- Mga smart home device na tugma sa Zigbee, Matter, Philips Hue, o lokal na Wi-Fi.
- Aktibong pagpapalamig upang maiwasan ang thermal throttling.

## Arkitektura

1. Pinamamahalaan ng Home Assistant OS ang mga device at automation.
2. Lokal na nakakakita ang openWakeWord ng wake word.
3. Isinasalin ng Whisper ang mga utos sa wikang kasalukuyang aktibo sa pamamagitan ng Wyoming.
4. Isinasagawa ng intent processor ang mga utos para sa smart home nang lokal.
5. Bumubuo ang Piper ng mga pasalitang tugon sa Catalan.
6. Sinasagot ng Ollama ang mga pangkalahatang tanong nang hindi nagpapadala ng data sa internet.
7. Mga tahasang tanong lamang na nangangailangan ng mas advanced na AI ang ipinapadala sa cloud AI.

## Mga nakaplanong kakayahan

- Pagkontrol sa ilaw, saksakan, air conditioning, blinds, at iba pang device gamit ang boses.
- Mga alias sa maraming wika.
- Mga timer na pinamamahalaan sa pamamagitan ng boses.
- Pagtatanong tungkol sa lokal na lagay ng panahon.
- Pagpapatugtog at pagkontrol ng musika.
- Pribadong fallback sa Ollama model.
- Pagkilala sa nagsasalita batay sa boses.
- Pangmatagalang memorya ng konteksto.
- Opsyonal na pagpapasa sa cloud AI model.
- Mga backup at pagsubaybay sa performance.

## Mga prinsipyo sa disenyo

- Dapat gumana ang mga utos para sa smart home kahit walang koneksyon sa internet.
- Mas uunahin ang lokal na intent processor kaysa sa mga LLM.
- Hangga't maaari, lokal na ipoproseso ang audio data at mga pribadong usapan.
- Gagamitin lamang ang mga cloud model para sa tahasan o masalimuot na tanong, at kapag tahasang pinagana ito ng user habang kino-configure ang assistant.
- Dapat manatiling matatag ang temperatura at latency ng system sa tuloy-tuloy na load.

## Kalagayan ng proyekto

Itinakda ang proyekto bilang backlog ng mga kakayahan. Idaragdag ang mga partikular na configuration, automation, at deployment script habang nakukumpleto ang mga user story.
