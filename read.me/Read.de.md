# Mehrsprachiger Smart-Home-Assistent

**Sprache:** Deutsch · [Zur Sprachauswahl](../readme.md)

**Lesen auf:** [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Dieses Projekt beschreibt den Aufbau eines lokalen Smart-Home-Ökosystems auf einem Raspberry Pi mit einem mehrsprachigen Sprachassistenten.

## Herkunft des Namens Mina

**Mina** hat eine alte germanische Wurzel in *minna*, was „Erinnerung“, „Zuneigung“ oder „Andenken“ bedeutet. Der Name kommt auch in anderen Sprachen vor: Im Persischen wird *mīnā* mit „Licht“ oder „blauem Glas“ verbunden, und im Japanischen bedeutet *mina* „alle“ oder „alle zusammen“.

Diese Deutungen stehen für **gemeinsame Erinnerung und Gemeinschaft** – Werte, die zu einem Assistenten passen, der den Alltag zu Hause unterstützt.

Klanglich ist Mina ein weicher, aber klarer Name mit zwei Silben (`Mi-na`), der wahrscheinlich nicht mit alltäglichen Wörtern im häuslichen Umfeld verwechselt wird.

## Ziel

Ein privates, zuverlässiges und schnelles Smart-Home-System schaffen, mit dem sich Geräte im Haushalt per Sprachbefehl steuern lassen, ohne zwingend auf Cloud-Dienste angewiesen zu sein.

Die Architektur kombiniert:

- Lokale Verarbeitung von Smart-Home-Befehlen für mehr Datenschutz.
- Lokale KI mit Ollama für allgemeine Fragen.
- Cloud-Modelle für komplexe Anfragen und aktuelle Informationen.

## Hardware

- Raspberry Pi 5 mit empfohlenen 8 GB RAM. Eingeschränkte Kompatibilität bis hinunter zum Raspberry Pi 3B+.
- NVMe-SSD, sodass keine SD-Karte benötigt wird. Bei Verwendung einer SD-Karte ist die Kompatibilität eingeschränkt.
- Bidirektionales USB-Mikrofon und -Lautsprecher.
- Smart-Home-Geräte mit Zigbee, Matter, Philips Hue oder lokalem WLAN.
- Aktive Kühlung zur Vermeidung von thermischem Throttling.

## Architektur

1. Home Assistant OS verwaltet Geräte und Automatisierungen.
2. openWakeWord erkennt das Aktivierungswort lokal.
3. Whisper transkribiert Befehle in der aktiven Sprache über Wyoming.
4. Der Intent-Prozessor führt Smart-Home-Befehle lokal aus.
5. Piper erzeugt Antworten auf Katalanisch.
6. Ollama beantwortet allgemeine Fragen, ohne Daten ins Internet zu senden.
7. Cloud-KI erhält nur ausdrückliche Anfragen, für die fortgeschrittene KI erforderlich ist.

## Geplante Funktionen

- Sprachsteuerung für Beleuchtung, Steckdosen, Heizung und Klimaanlage, Jalousien und weitere Geräte.
- Mehrsprachige Aliase.
- Sprachgesteuerte Timer.
- Lokale Wetterabfragen.
- Musikwiedergabe und -steuerung.
- Privater Rückgriff auf ein Ollama-Modell.
- Erkennung der sprechenden Person anhand der Stimme.
- Langfristiges Kontextgedächtnis.
- Optionale Weiterleitung an ein Cloud-KI-Modell.
- Sicherungen und Leistungsüberwachung.

## Gestaltungsprinzipien

- Smart-Home-Befehle müssen auch ohne Internetverbindung funktionieren.
- Der lokale Intent-Prozessor hat Vorrang vor LLMs.
- Audiodaten und private Gespräche werden vorzugsweise lokal verarbeitet.
- Cloud-Modelle werden nur für ausdrückliche oder komplexe Anfragen genutzt und nur, wenn der Nutzer dies bei der Einrichtung des Assistenten ausdrücklich aktiviert hat.
- Das System muss auch bei Dauerlast stabile Temperaturen und Latenzen gewährleisten.

## Projektstatus

Das Projekt ist als funktionales Backlog definiert. Konkrete Konfigurationen, Automatisierungen und Bereitstellungsskripte werden ergänzt, sobald die User Stories umgesetzt werden.
