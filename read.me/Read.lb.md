**Lëtzebuergesch** · [Zréck zur Sproochauswiel](../Read.md)

# Méisproochegen Hausassistent

Dëse Projet beschreift den lokalen Androck vun engem méisproochegen Stëmmassistents-Ekosystem op engem Raspberry Pi.

## Hierkonft vum Numm Mina

**Mina** huet eng algermanesch Wuerzel am *minna*, dat „Erënnerung“, „Affekt“ oder „Erënnerung“ bedeit. Dat ass och a anere Sprooche present: am Persesche hänkt *mīnā* mat „Liicht“ oder „bloem Glas“ zesummen, am Japanesche bedeit *mina* „jidderee“ oder „all zesummen“.

Dës Interpretatiounen symboliséiere eng **gedeelten Erënnerung a Gemeinschaft** — Wäerter, déi zu engem Assistent passen, deen den Alldag am Haus begleet a ënnerstëtzt.

Akoustesch ass Mina e mëllen, awer kloeren Numm, mat der Silbepronunciatioun `Mi-na` an enger klenger Verwiesselungswahrscheinlechkeet mat heefegen Wierder am Haus.

## Zil

E privaten, zouverlässegen a séieren Heembetriebssystem ze schaffen, deen Hausapparater mat Stëmmkommanden steiert, ouni obligatoresch Ofhängegkeet vu Cloudservicer.

D’Architektur kombinéiert:

- Lokal Veraarbechtung fir Hauskommanden a Privatsphär.
- Lokal Intelligenz mat Ollama fir allgemeng Froen.
- Cloudmodeller fir komplex Ufroen an aktuell Informatioun.

## Hardware

- Raspberry Pi 5 mat 8 GB RAM recommandéiert. Limitéiert Kompatibilitéit bis Raspberry Pi 3B+.
- NVMe SSD ouni SD-Kaart. Limitéiert Kompatibilitéit mat enger SD-Kaart.
- Bidirektionale USB-Mikrofon a Lautsprecher.
- Hausapparater kompatibel mat Zigbee, Matter, Philips Hue oder lokalem Wi-Fi.
- Aktiv Kühlung fir thermescht Drosslung ze vermeiden.

## Architektur

1. Home Assistant OS verwalt d’Apparater an d’Automatisatiounen.
2. openWakeWord erkennt lokal d’Aktivéierungswuert.
3. Whisper transkribéiert iwwer Wyoming d’Kommanden an der aktiver Sprooch.
4. Den Absichtsprcessor executéiert Hauskommanden lokal.
5. Piper synthetiséiert d’Äntwerten op Lëtzebuergesch.
6. Ollama léist allgemeng Froen, ouni Daten an d’Internet ze schécken.
7. Cloud-KI kritt nëmme explizit Ufroen, déi fortgeschratt KI erfuerderen.

## Geplangten Funktiounen

- Stëmmkontroll fir Luuchten, Steckdosen, Klima, Stores a weider Apparater.
- Méisproocheg Aliase.
- Per Stëmm verwaltte Timer.
- Lokal Wiederufroen.
- Musek ofspillen a steieren.
- Privaten Fallback op Ollama.
- Persounenunerkennung iwwer d’Stëmm.
- Laangfristeg Kontextspäicher.
- Optional Weiderleedung op e Cloud-KI-Modell.
- Sécherungen a Leeschtungsiwwerwachung.

## Designprinzipien

- Hauskommanden musse ouni Internetverbindung funktionéieren.
- De lokalen Absichtsprcessor huet Virrang virun LLMs.
- Toundaten a privat Gespréicher solle léiwer lokal veraarbecht ginn.
- Cloudmodeller ginn nëmme fir explizit oder komplex Ufroe benotzt, nëmme wann de Benotzer dat beim Konfiguréieren explizit gefrot huet.
- De System muss ënner konstanter Belaaschtung stabil Temperaturen a Latenzen behalen.

## Projektstatus

De Projet ass als funktionale Backlog definéiert. Spezifesch Konfiguratiounen, Automatisatiounen a Déploiementsskripte musse bäigefüügt ginn, sou wéi d’Benotzergeschichten ofgeschloss ginn.
