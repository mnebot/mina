**Corsu · [Torna à a scelta di a lingua](../Read.md)**

# Assistente multilingue per a casa intelligente

**Lingua:** Corsu

**Leghje in:** [Catalanu](Read.ca.md) · [Inglese](Read.en.md) · [Spagnolu](Read.es.md) · [Francesu](Read.fr.md) · [Tedescu](Read.de.md) · [Talianu](Read.it.md) · [Portughese](Read.pt.md) · [Olandese](Read.nl.md)

Stu prughjettu discrive a messa in opera d'un ecosistema lucale di domòtica nant'à una Raspberry Pi, cù un assistente vocale multilingue.

## Origine di u nome Mina

**Mina** vene da a radica germanica antica *minna*, chì significa «memoria», «affettu» o «ricordu». U nome esiste ancu in altre lingue: in persianu, *mīnā* hè assuciatu à a «luce» o à u «vetru turchinu», è in giappunese *mina* significa «tutti» o «tutti inseme».

St'interpretazioni simbulizeghjanu una **memoria spartuta è una cumunità**, valori in armunia cù un assistente chì accumpagna è sustene a vita cutidiana in casa.

Da u puntu di vista sonoru, Mina hè un nome dolce ma chjaru, cù a prununcia sillabica `Mi-na` è poca pussibilità di cunfusione cù e parolle cumune in casa.

## Scopu

Creà un sistema di domòtica privatu, affidabile è rapidu chì permette di cuntrullà i dispositivi di casa cù cumandi vocali, senza dipende di manera ubligatoria da servizii in nuvola.

L'architettura combina:

- Trattamentu lucale per i cumandi di domòtica è a privacy.
- Intelligenza lucale cù Ollama per e dumande generali.
- Mudelli in nuvola per e dumande cumplesse è l'infurmazione aghjurnata.

## Ferru

- Raspberry Pi 5 cù 8 GB di RAM cunsigliati. Cumpatibilità limitata fin'à Raspberry Pi 3B+.
- Discu SSD NVMe senza aduprà una carta SD. Cumpatibilità limitata cù a carta SD.
- Microfonu è altoparlante USB bidirezziunali.
- Dispositivi di domòtica cumpatibili cù Zigbee, Matter, Philips Hue o Wi-Fi lucale.
- Raffreddamentu attivu per evità u rallentamentu termicu.

## Architettura

1. Home Assistant OS gestisce i dispositivi è l'automatizazioni.
2. openWakeWord rileva lucalmente a parolla d'attivazione.
3. Whisper trascrive i cumandi in a lingua attiva per mezu di Wyoming.
4. U processore d'intenzioni esegue lucalmente i cumandi di domòtica.
5. Piper sintetizeghja e risposte in catalanu.
6. Ollama risponde à e dumande generali senza mandà dati nant'à Internet.
7. L'IA in nuvola riceve solu e dumande esplicite chì richiedenu un'IA avanzata.

## Funziunalità previste

- Cuntrollu vocale di lumi, prese, climatizazione, persiane è altri dispositivi.
- Alias multilingui.
- Timer gestiti à voce.
- Cunsulta lucale di u tempu.
- Ripruduzzione è cuntrollu di a musica.
- Ripiegu privatu à un mudellu Ollama.
- Ricunniscenza di a persona per via di a voce.
- Memoria di cuntestu à longu andà.
- Trasferimentu facultativu à un mudellu d'IA in nuvola.
- Copie di salvezza è surviglianza di e prestazioni.

## Principii di cuncepimentu

- I cumandi di domòtica devenu funziunà senza cunnessione à Internet.
- U processore lucale d'intenzioni hà a priorità nant'à i LLM.
- I dati audio è e cunversazioni private sò trattati di preferenza in lucale.
- I mudelli in nuvola sò aduprati solu per dumande esplicite o cumplesse, è solu s'è l'utilizatore l'hà dumandatu esplicitamente quand'ellu hà cunfiguratu l'assistente.
- U sistema deve mantene temperature è latenze stabili sottu à una carica cuntinua.

## Statu di u prughjettu

U prughjettu hè definitu cum'è un backlog funziunale. E cunfigurazioni specifiche, l'automatizazioni è i script di messa in opera seranu aghjunti à misura chì e storie d'utilizatore seranu compie.
