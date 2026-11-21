# Meertalige domotica-assistent

**Taal:** Nederlands · [Terug naar de taalselectie](../readme.md)

**Lees in:** [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Dit project beschrijft de uitrol van een lokaal domotica-ecosysteem op een Raspberry Pi met een meertalige spraakassistent.

## De oorsprong van de naam Mina

**Mina** heeft een oude Germaanse wortel in *minna*, wat „herinnering”, „genegenheid” of „gedachtenis” betekent. De naam komt ook in andere talen voor: in het Perzisch wordt *mīnā* geassocieerd met „licht” of „blauw glas”, en in het Japans betekent *mina* „iedereen” of „allemaal samen”.

Deze betekenissen staan voor **gedeelde herinnering en gemeenschap**: waarden die passen bij een assistent die het dagelijks leven thuis ondersteunt.

Fonetisch is Mina een zachte maar duidelijke naam van twee lettergrepen (`Mi-na`), die in een huiselijke omgeving waarschijnlijk niet met gewone woorden wordt verward.

## Doel

Een privé, betrouwbaar en snel domoticasysteem bouwen waarmee huishoudelijke apparaten met spraakopdrachten kunnen worden bediend, zonder verplichte afhankelijkheid van clouddiensten.

De architectuur combineert:

- Lokale verwerking van domoticaopdrachten voor privacy.
- Lokale AI met Ollama voor algemene vragen.
- Cloudmodellen voor complexe vragen en actuele informatie.

## Hardware

- Raspberry Pi 5 met aanbevolen 8 GB RAM. Beperkte compatibiliteit tot en met de Raspberry Pi 3B+.
- NVMe-SSD, zodat geen SD-kaart nodig is. De compatibiliteit is beperkt bij gebruik van een SD-kaart.
- Bidirectionele USB-microfoon en -luidspreker.
- Domotica-apparaten die compatibel zijn met Zigbee, Matter, Philips Hue of lokaal wifi.
- Actieve koeling om thermische throttling te voorkomen.

## Architectuur

1. Home Assistant OS beheert apparaten en automatiseringen.
2. openWakeWord detecteert lokaal het activeringswoord.
3. Whisper zet opdrachten via Wyoming om naar tekst in de actieve taal.
4. De intentieverwerker voert domoticaopdrachten lokaal uit.
5. Piper spreekt antwoorden uit in het Catalaans.
6. Ollama beantwoordt algemene vragen zonder gegevens naar het internet te sturen.
7. Cloud-AI ontvangt alleen expliciete vragen waarvoor geavanceerde AI nodig is.

## Geplande functies

- Spraakbediening van verlichting, stekkers, klimaatregeling, jaloezieën en andere apparaten.
- Meertalige aliassen.
- Timers die met spraak worden ingesteld.
- Lokale weersinformatie.
- Muziek afspelen en bedienen.
- Een privéterugvaloptie met een Ollama-model.
- De spreker herkennen aan de stem.
- Langetermijngeheugen voor context.
- Optionele doorschakeling naar een cloud-AI-model.
- Back-ups en prestatiebewaking.

## Ontwerpprincipes

- Domoticaopdrachten moeten zonder internetverbinding werken.
- De lokale intentieverwerker heeft voorrang op LLM's.
- Audio en privégesprekken worden bij voorkeur lokaal verwerkt.
- Cloudmodellen worden alleen gebruikt voor expliciete of complexe vragen, en alleen als de gebruiker dit bij het instellen van de assistent uitdrukkelijk heeft aangevraagd.
- Het systeem moet bij continue belasting stabiele temperaturen en latentie behouden.

## Projectstatus

Het project is opgezet als een functionele backlog. Specifieke configuraties, automatiseringen en implementatiescripts worden toegevoegd zodra de gebruikersverhalen zijn afgerond.
