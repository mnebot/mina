**Malti** · [Lura għall-għażla tal-lingwa](../Read.md)

# Assistent domestiku multilingwi

Dan il-proġett jiddeskrivi l-installazzjoni lokali ta’ ekosistema ta’ assistent vokali multilingwi fuq Raspberry Pi.

## Oriġini tal-isem Mina

**Mina** għandha għerq Ġermaniku antik f’*minna*, li tfisser “memorja”, “affett” jew “rikord”. Hija preżenti wkoll f’lingwi oħra: bil-Persjan, *mīnā* tirreferi għal “dawl” jew “ħġieġ blu”, u bil-Ġappuniż, *mina* tfisser “kulħadd” jew “lkoll flimkien”.

Dawn it-tifsiriet jissimbolizzaw **memorja kondiviża u komunità**, valuri konsistenti ma’ assistent li jakkumpanja u jsostni l-ħajja ta’ kuljum fid-dar.

F’termini ta’ ħoss, Mina huwa isem artab imma ċar, bil-pronunzja sillabika `Mi-na` u probabbiltà baxxa ta’ konfużjoni ma’ kliem komuni f’ambjent domestiku.

## Għan

Joħloq sistema domestika privata, affidabbli u veloċi li tippermetti kontroll ta’ apparati tad-dar permezz ta’ kmandi vokali mingħajr dipendenza obbligatorja minn servizzi tal-cloud.

L-arkitettura tgħaqqad:

- Proċessar lokal għal kmandi domestiċi u privatezza.
- Intelliġenza lokali b’Ollama għal mistoqsijiet ġenerali.
- Mudelli tal-cloud għal mistoqsijiet kumplessi u informazzjoni aġġornata.

## Hardware

- Raspberry Pi 5 bi 8 GB RAM rakkomandati. Kompatibilità limitata sa Raspberry Pi 3B+.
- SSD NVMe mingħajr karta SD. Kompatibilità limitata ma’ karta SD.
- Mikrofonu USB bidirezzjonali u lawdsprecher.
- Apparati domestiċi kompatibbli ma’ Zigbee, Matter, Philips Hue jew Wi-Fi lokali.
- Tkessiħ attiv biex jiġi evitat it-throttling termali.

## Arkitettura

1. Home Assistant OS jimmaniġġja apparati u awtomazzjonijiet.
2. openWakeWord jiskopri lokalment il-kelma tal-attivazzjoni.
3. Whisper jittraskrivi kmandi bil-lingwa attiva permezz ta’ Wyoming.
4. Il-proċessur tal-intenzjonijiet iwettaq kmandi domestiċi lokalment.
5. Piper jissintetizza tweġibiet bil-Malti.
6. Ollama ssolvi mistoqsijiet ġenerali mingħajr ma tibgħat data lill-Internet.
7. Il-cloud AI jirċievi biss mistoqsijiet espliċiti li jeħtieġu AI avvanzata.

## Karatteristiċi ppjanati

- Kontroll b’leħen ta’ dwal, sokits, klima, blinds u apparati oħra.
- Aliases multilingwi.
- Timers ġestiti bil-vok.
- Konsulti lokali tat-temp.
- Riproduzzjoni u kontroll tal-mużika.
- Fallback privat għal mudell Ollama.
- Rikonoxximent tal-persuna bil-vuċi.
- Memorja ta’ kuntest għal żmien twil.
- Devjazzjoni fakultattiva għal mudell AI fil-cloud.
- Backup u monitoraġġ tal-prestazzjoni.

## Prinċipji tad-disinn

- Il-kmandi domestiċi jridu jaħdmu mingħajr Internet.
- Il-proċessur tal-intenzjonijiet lokal għandu prijorità fuq LLMs.
- Id-data tal-awdjo u l-konversazzjonijiet privati għandhom jiġu pproċessati lokalment.
- Il-mudelli tal-cloud jintużaw biss għal mistoqsijiet espliċiti jew kumplessi, u biss jekk l-utent ikun talabha espliċitament meta jikkonfigura l-assistent.
- Is-sistema għandha żżomm temperaturi u dewmien stabbli taħt tagħbija kontinwa.

## Status tal-proġett

Il-proġett huwa definit bħala backlog funzjonali. Konfigurazzjonijiet speċifiċi, awtomazzjonijiet u skripts ta’ tħaddim se jkunu miżjuda hekk kif l-istejjer tal-utent jiġu kompluti.
