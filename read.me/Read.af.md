**Taal: Afrikaans** · [Terug na taalkeuse](../readme.md)

# Meertalige tuisautomatiseringsassistent

Hierdie projek beskryf die implementering van 'n plaaslike tuisoutomatiseringsekosisteem op 'n Raspberry Pi met 'n veeltalige stemassistent.

## Oorsprong van die naam Mina

**Mina** het 'n ou Germaanse wortel in *minna*, wat "geheue", "liefde" of "herinnering" beteken. Dit kom ook in ander tale voor: in Persies hou *mīnā* verband met "lig" of "blou glas", en in Japanees beteken *mina* "almal" of "almal saam".
Hierdie interpretasies simboliseer 'n **gedeelde geheue en gemeenskap**, waardes wat ooreenstem met 'n assistent wat die alledaagse lewe in die huishouding vergesel en ondersteun.

Wat die klankaspek betref, is Mina 'n sagte maar duidelike naam, met die lettergreepuitspraak `Mi-na` en 'n lae waarskynlikheid van verwarring met algemene woorde in huishoudelike omgewings.

## Doelwit
Skep 'n private, betroubare en vinnige tuisoutomasiestelsel wat dit moontlik maak om huishoudelike toestelle deur middel van stemopdragte te beheer, sonder verpligte afhanklikheid van wolkdienste.

Die argitektuur kombineer:

- Lokale verwerking vir tuisoutomatiseringsopdragte en privaatheid.
- Plaaslike intelligensie met Ollama vir algemene vrae.
- Wolkmodelle vir komplekse navrae en bygewerkte inligting.

## Hardeware
- Raspberry Pi 5 met 8 GB RAM word aanbeveel. Beperkte verenigbaarheid tot Raspberry Pi 3B+.
- SSD NVMe-skyf sonder die gebruik van 'n SD-kaart. Beperkte verenigbaarheid met SD-kaart.
- Tweerigting-USB-mikrofone en -luidsprekers.
- Domotika-toestelle wat versoenbaar is met plaaslike Zigbee, Matter, Philips Hue of Wi-Fi.
- Aktiewe verkoeling om termiese throttling te voorkom.

## Argitektuur

1. Home Assistant OS bestuur die toestelle en outomatisasies.
2. openWakeWord bespeur die aktiveringswoord plaaslik.
3. Whisper transkribeer opdragte in die aktiewe taal deur middel van Wyoming.
4. Die bedoelingsverwerker voer die tuisoutomatiseringsopdragte plaaslik uit.
5. Piper sintetiseer die antwoorde in Afrikaans.
6. Ollama beantwoord algemene vrae sonder om data na die internet te stuur.
7. Die KI in die wolk ontvang slegs eksplisiete navrae wat gevorderde KI vereis.

## Beplande funksies
- Stembeheer van ligte, stopkontakte, lugversorging, blindings en ander toestelle.
- Meertalige byname.
- Stembeheerde tydskakelaars.
- Plaaslike weervoorspelling.
- Musiekweergawe en -beheer.
- Privaat terugval na 'n Ollama-model.
- Stemherkenning van die persoon.
- Langtermyn-konteksgeheue.
- Opsionele verwysing na 'n KI-model in die wolk.
- Rugsteun en prestasiemonitering.
## Ontwerpbeginsels

- Tuisoutomatiseringsopdragte moet sonder 'n internetverbinding werk.
- Die plaaslike voorneme-verwerker het voorrang bo die LLM.
- Oudiogegewens en private gesprekke word verkieslik plaaslik verwerk.
- Wolkmodelle word slegs gebruik vir eksplisiete of komplekse navrae, en slegs indien die gebruiker dit eksplisiet versoek het tydens die opstel van die assistent.
- Die stelsel moet stabiele temperature en vertragings onder voortdurende belasting handhaaf.

## Status van die projek

Die projek word gedefinieer as 'n funksionele agterstand. Spesifieke konfigurasies, outomatisasies en implementeringskripte sal bygevoeg moet word namate die gebruikersverhale voltooi word.
