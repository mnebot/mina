**Svenska** · [Tillbaka till språkväljaren](../Read.md)

# Flerspråkig hemassistent

Det här projektet beskriver driftsättningen av ett lokalt ekosystem för en flerspråkig röstassistent på en Raspberry Pi.

## Namnet Minas ursprung

**Mina** har en urgermansk rot i *minna*, som betyder ”minne”, ”kärlek” eller ”påminnelse”. Namnet finns också i andra språk: på persiska associeras *mīnā* med ”ljus” eller ”blått glas”, och på japanska betyder *mina* ”alla” eller ”alla tillsammans”.

Dessa betydelser symboliserar ett **gemensamt minne och en gemenskap**, värden som passar en assistent som följer med och stöder vardagslivet i hemmet.

När det gäller klang är Mina ett mjukt men tydligt namn, med stavelseuttalet `Mi-na` och låg risk för förväxling med vanliga ord i hemmet.

## Mål

Skapa ett privat, pålitligt och snabbt hemsystem som gör det möjligt att styra hemanordningar med röstkommandon utan obligatoriskt beroende av molntjänster.

Arkitekturen kombinerar:

- Lokal bearbetning av hemliga kommandon och integritet.
- Lokal intelligens med Ollama för allmänna frågor.
- Molnmodeller för komplexa frågor och aktuell information.

## Hårdvara

- Raspberry Pi 5 med 8 GB RAM rekommenderas. Begränsad kompatibilitet upp till Raspberry Pi 3B+.
- NVMe-SSD utan SD-kort. Begränsad kompatibilitet med SD-kort.
- Tvåvägs USB-mikrofon och högtalare.
- Hemanordningar som stöder Zigbee, Matter, Philips Hue eller lokalt Wi-Fi.
- Aktiv kylning för att undvika termisk begränsning.

## Arkitektur

1. Home Assistant OS hanterar enheterna och automatiseringarna.
2. openWakeWord upptäcker aktiveringsordet lokalt.
3. Whisper transkriberar kommandon på det aktiva språket via Wyoming.
4. Avsiktsprocessorn kör hemautomation lokalt.
5. Piper syntetiserar svar på svenska.
6. Ollama löser allmänna frågor utan att skicka data till Internet.
7. Molnbaserad AI tar emot endast explicita förfrågningar som kräver avancerad AI.

## Planerade funktioner

- Röststyrning av lampor, uttag, klimatanläggning, persienner och andra enheter.
- Flerspråkiga alias.
- Röststyrda timers.
- Lokala väderfrågor.
- Uppspelning och styrning av musik.
- Privat fallback till en Ollama-modell.
- Personigenkänning via rösten.
- Långsiktigt kontextminne.
- Valbar dirigering till en molnbaserad AI-modell.
- Säkerhetskopiering och prestationsövervakning.

## Designprinciper

- Hemkommandon måste fungera utan internetanslutning.
- Den lokala avsiktsprocessorn har företräde framför LLM.
- Ljuddata och privata samtal bör behandlas lokalt.
- Molnmodeller används endast för explicita eller komplexa förfrågningar och bara om användaren uttryckligen begärt det när assistenten konfigurerats.
- Systemet ska bibehålla stabila temperaturer och svarstider under kontinuerlig belastning.

## Projektstatus

Projektet är definierat som en funktionell backlog. Specifika konfigurationer, automatiseringar och distributionsskript kommer att läggas till allt eftersom användarhistorierna slutförs.
