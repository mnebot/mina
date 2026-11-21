**Diné bizaad · [Bizaad íiyisíí nihá shá yátiʼ](../Read.md)**
# Hooghan tʼáá ałtsoh bizaadígíí bee tʼáá íiyisíí naaltsoos

**Bizaad:** Diné bizaad

**Díí bizaad bee naʼanish:** [Diné bizaad](Read.nv.md) · [English](Read.en.md) · [Català](Read.ca.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Díí project tʼáá ałtsoh hooghan biyiʼ naashá, Raspberry Pi bá hooghan bee íiyisíí yáʼátʼééhgo tʼáá íiyisíí bizaadígíí bee naasháʼígíí baa yátiʼ.

## Mina biyiʼ átʼéego

**Mina** bizaad íiyisíí German yázhíí *minna* níigo tʼáá íiyisíí nááʼał, biniinaa «nitsáhákees», «ayóo anííníshní» dóó «nitsáhákeesígíí». Persian bizaad *mīnā* «shash» dóó «doołʼizhii glass» baa haneʼ; Japanese bizaad *mina* «tʼáá ałtsoh» dóó «tʼáá ałtsoh hólǫ́» níigo.

Díí baa haneʼígíí **tʼáá ałtsoh nitsáhákees dóó k’é** bee yáʼátʼééh, hooghan biyiʼ ííníłʼįįʼ dóó ił hózhǫ́ʼ naasháʼígíí.

Mina bizaad tʼáá yáʼátʼééhgo náásgóó łííʼ; `Mi-na` naaki syllable, hooghan biyiʼ bizaad tʼáá áłtsé baa yátiʼígíí dóó doo chʼį́į́h da.

## Hózhǫ́ʼgo naʼanish

Hooghan biyiʼ tʼáá íiyisíí privacy, tʼáá yáʼátʼééh, dóó tʼáá łahgo naasháʼígíí naʼanish naʼanishígíí; bizaad bee hooghan biyiʼ naʼanish naalnish, cloud service doo tʼáá baa ájítʼéego da.

Architecture díí dóó yáʼátʼééhgo ííłʼį́:

- Hooghan biyiʼ processing domotic commands dóó privacy bee.
- Ollama biyiʼ intelligence hooghan biyiʼ, tʼáá áłtsé questions bee.
- Cloud model tʼáá íiyisíí questions dóó tʼáá áłtsé information bee.

## Hardware

- 8 GB RAM Raspberry Pi 5 nízhónígo ádaatʼé. Raspberry Pi 3B+ dóó yáʼátʼééhgo compatibility tʼáá áłtsé.
- NVMe SSD disk, SD card doo naashá da. SD card dóó tʼáá áłtsé compatibility.
- USB microphone dóó speaker naaki háálá.
- Zigbee, Matter, Philips Hue dóó local Wi-Fi bee compatibility hooghan device.
- Active cooling, tʼáá íiyisíí hot níigo thermal throttling doo nízhóní.

## Architecture

1. Home Assistant OS device dóó automation bee naashá.
2. openWakeWord hooghan biyiʼ wake word bee naʼanish.
3. Whisper Wyoming bee active bizaadígíí commands transcribe.
4. Intent processor hooghan biyiʼ domotic commands bee naʼanish.
5. Piper Catalan bizaad bee answers speech.
6. Ollama general questions doo Internet data yáʼátʼééh da.
7. Cloud AI tʼáá explicit advanced AI questions yáʼátʼééh.

## Bee adoolʼį́į́łígíí feature

- Lights, outlets, climate, blinds dóó tʼáá áłtsé devices bizaad bee control.
- Multi-language aliases.
- Voice bee timers.
- Hooghan kʼad weather questions.
- Music playback dóó control.
- Ollama model bee private fallback.
- Person voice bee recognition.
- Long-term context memory.
- Optional cloud AI model bee direction.
- Backups dóó performance monitoring.

## Design principles

- Domotic commands Internet doo da atʼéego naashá.
- Local intent processor LLM bá hooghaní.
- Audio data dóó private conversations tʼáá hooghan biyiʼ processing.
- Cloud models tʼáá explicit dóó complex questions bee, user assistant configuration tʼáá explicit yáʼátʼééhgo nítʼééʼígíí díí.
- System temperature dóó latency stable nihá yáʼátʼééhgo continuous load biyiʼ.

## Project status

Project functional backlog bee yáʼátʼééhgo ádaatʼé. Specific configurations, automations dóó deployment scripts user stories biyiʼ ádaałtséʼgo yáʼátʼééhgo ádaałtsʼá.
