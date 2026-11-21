**Slovenčina · [Späť na výber jazyka](../readme.md)**

# Viacjazyčný asistent pre inteligentnú domácnosť

**Jazyk:** slovenčina

**Čítať v:** [Katalánčine](Read.ca.md) · [Angličtine](Read.en.md) · [Španielčine](Read.es.md) · [Francúzštine](Read.fr.md) · [Nemčine](Read.de.md) · [Taliančine](Read.it.md) · [Portugalčine](Read.pt.md) · [Holandčine](Read.nl.md)

Tento projekt opisuje nasadenie lokálneho ekosystému domácej automatizácie na Raspberry Pi s viacjazyčným hlasovým asistentom.

## Pôvod názvu Mina

**Mina** má pôvod v starogermánskom koreni *minna*, ktorý znamená „pamäť“, „náklonnosť“ alebo „spomienka“. Vyskytuje sa aj v iných jazykoch: v perzštine sa *mīnā* spája so „svetlom“ alebo „modrým sklom“ a v japončine *mina* znamená „všetci“ alebo „všetci spolu“.

Tieto výklady symbolizujú **spoločnú pamäť a komunitu** – hodnoty, ktoré sú v súlade s asistentom sprevádzajúcim a podporujúcim každodenný život domácnosti.

Zvukovo je Mina jemné, ale jasné meno so slabičnou výslovnosťou `Mi-na` a malou pravdepodobnosťou zámeny s bežnými slovami v domácom prostredí.

## Cieľ

Vytvoriť súkromný, spoľahlivý a rýchly systém domácej automatizácie, ktorý umožňuje ovládať domáce zariadenia hlasovými príkazmi bez povinnej závislosti od cloudových služieb.

Architektúra kombinuje:

- Lokálne spracovanie príkazov domácej automatizácie a ochranu súkromia.
- Lokálnu inteligenciu s Ollama na všeobecné otázky.
- Cloudové modely na zložité otázky a aktuálne informácie.

## Hardvér

- Raspberry Pi 5 s odporúčanými 8 GB RAM. Obmedzená kompatibilita až po Raspberry Pi 3B+.
- Disk SSD NVMe bez použitia SD karty. Obmedzená kompatibilita s SD kartou.
- Obojsmerný USB mikrofón a reproduktor.
- Zariadenia domácej automatizácie kompatibilné so Zigbee, Matter, Philips Hue alebo lokálnou Wi-Fi.
- Aktívne chladenie na predchádzanie tepelnému obmedzeniu výkonu.

## Architektúra

1. Home Assistant OS spravuje zariadenia a automatizácie.
2. openWakeWord lokálne rozpoznáva aktivačné slovo.
3. Whisper prepisuje príkazy v aktívnom jazyku prostredníctvom Wyoming.
4. Procesor zámerov lokálne vykonáva príkazy domácej automatizácie.
5. Piper syntetizuje odpovede v katalánčine.
6. Ollama odpovedá na všeobecné otázky bez odosielania údajov na internet.
7. Cloudová AI dostáva iba výslovné otázky, ktoré vyžadujú pokročilú AI.

## Plánované funkcie

- Hlasové ovládanie svetiel, zásuviek, klimatizácie, žalúzií a ďalších zariadení.
- Viacjazyčné alternatívne názvy.
- Časovače ovládané hlasom.
- Lokálne zisťovanie počasia.
- Prehrávanie a ovládanie hudby.
- Súkromný záložný model Ollama.
- Rozpoznávanie osoby podľa hlasu.
- Dlhodobá pamäť kontextu.
- Voliteľné odovzdanie požiadavky cloudovému modelu AI.
- Zálohovanie a monitorovanie výkonu.

## Princípy návrhu

- Príkazy domácej automatizácie musia fungovať bez internetového pripojenia.
- Lokálny procesor zámerov má prednosť pred LLM.
- Zvukové údaje a súkromné rozhovory sa spracúvajú prednostne lokálne.
- Cloudové modely sa používajú iba na výslovné alebo zložité otázky a iba vtedy, ak o to používateľ výslovne požiadal pri konfigurácii asistenta.
- Systém musí pri nepretržitej záťaži udržiavať stabilné teploty a latencie.

## Stav projektu

Projekt je definovaný ako funkčný backlog. Konkrétne konfigurácie, automatizácie a skripty nasadenia sa budú pridávať podľa toho, ako sa budú dokončovať používateľské príbehy.
