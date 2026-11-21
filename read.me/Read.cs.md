**Čeština · [Zpět na výběr jazyka](../readme.md)**

# Vícejazyčný asistent pro chytrou domácnost

**Jazyk:** čeština

**Číst v:** [Katalánštině](Read.ca.md) · [Angličtině](Read.en.md) · [Španělštině](Read.es.md) · [Francouzštině](Read.fr.md) · [Němčině](Read.de.md) · [Italštině](Read.it.md) · [Portugalštině](Read.pt.md) · [Nizozemštině](Read.nl.md)

Tento projekt popisuje nasazení lokálního ekosystému domácí automatizace na Raspberry Pi s vícejazyčným hlasovým asistentem.

## Původ názvu Mina

**Mina** má kořeny ve starogermánském slově *minna*, které znamená „paměť“, „náklonnost“ nebo „vzpomínka“. Vyskytuje se také v dalších jazycích: v perštině souvisí *mīnā* se „světlem“ nebo „modrým sklem“ a v japonštině znamená *mina* „všichni“ nebo „všichni společně“.

Tyto výklady symbolizují **sdílenou paměť a komunitu**, tedy hodnoty odpovídající asistentovi, který doprovází a podporuje každodenní život domácnosti.

Po zvukové stránce je Mina jemné, ale zřetelné jméno se slabičnou výslovností `Mi-na` a malou pravděpodobností záměny s běžnými slovy v domácím prostředí.

## Cíl

Vytvořit soukromý, spolehlivý a rychlý systém domácí automatizace, který umožní ovládat domácí zařízení hlasovými příkazy bez nutné závislosti na cloudových službách.

Architektura kombinuje:

- Lokální zpracování příkazů domácí automatizace a ochranu soukromí.
- Lokální inteligenci s Ollama pro obecné otázky.
- Cloudové modely pro složité dotazy a aktuální informace.

## Hardware

- Raspberry Pi 5 s doporučenými 8 GB RAM. Omezená kompatibilita až po Raspberry Pi 3B+.
- SSD NVMe bez použití SD karty. Omezená kompatibilita s SD kartou.
- Obousměrný USB mikrofon a reproduktor.
- Zařízení domácí automatizace kompatibilní se Zigbee, Matter, Philips Hue nebo lokální Wi-Fi.
- Aktivní chlazení bránící tepelnému omezování výkonu.

## Architektura

1. Home Assistant OS spravuje zařízení a automatizace.
2. openWakeWord lokálně rozpoznává aktivační slovo.
3. Whisper přepisuje příkazy v aktivním jazyce prostřednictvím Wyoming.
4. Procesor záměrů lokálně provádí příkazy domácí automatizace.
5. Piper syntetizuje odpovědi v katalánštině.
6. Ollama odpovídá na obecné otázky, aniž by odesílala data na internet.
7. Cloudová AI přijímá pouze výslovné dotazy vyžadující pokročilou AI.

## Plánované funkce

- Hlasové ovládání světel, zásuvek, klimatizace, žaluzií a dalších zařízení.
- Vícejazyčná alternativní označení.
- Hlasově ovládané časovače.
- Lokální dotaz na počasí.
- Přehrávání a ovládání hudby.
- Soukromý záložní model Ollama.
- Rozpoznávání osoby podle hlasu.
- Dlouhodobá paměť kontextu.
- Volitelné předání dotazu cloudovému modelu AI.
- Zálohování a sledování výkonu.

## Principy návrhu

- Příkazy domácí automatizace musí fungovat bez připojení k internetu.
- Lokální procesor záměrů má přednost před LLM.
- Zvuková data a soukromé konverzace se zpracovávají přednostně lokálně.
- Cloudové modely se používají pouze pro výslovné nebo složité dotazy, a jen pokud o to uživatel výslovně požádal při konfiguraci asistenta.
- Systém musí při nepřetržité zátěži udržovat stabilní teploty a latence.

## Stav projektu

Projekt je vymezen jako funkční backlog. Konkrétní konfigurace, automatizace a nasazovací skripty se budou doplňovat podle toho, jak budou dokončovány uživatelské příběhy.
