**Furlan · [Torne ae selezion de lenghe](../readme.md)**

# Assistint multilengâl pe cjase inteligjente

**Lenghe:** furlan

**Lei in:** [Catalan](Read.ca.md) · [Inglês](Read.en.md) · [Spagnûl](Read.es.md) · [Francês](Read.fr.md) · [Todesc](Read.de.md) · [Talian](Read.it.md) · [Portughês](Read.pt.md) · [Olandês](Read.nl.md)

Chest progjet al descrîf la metude in vore di un ecosisteme locâl di domotiche suntune Raspberry Pi cun un assistint vocâl multilengâl.

## Origjin dal non Mina

**Mina** e à lidrîs te forme gjermaniche antighe *minna*, che e significhe «memorie», «afezion» o «ricuart». Il non al è presint ancje in altris lenghis: in persian, *mīnā* al è leât ae «lûs» o al «vieri blu», e in gjaponês *mina* al significhe «ducj» o «ducj insiemi».

Chestis interpretazions a simbolezin une **memorie condividude e une comunitât**, valôrs coerents cun un assistint che al acompagne e al sosten la vite di ogni dì de cjase.

Dal pont di viste dal sun, Mina al è un non dolç ma clâr, cun la pronunzie a sillabis `Mi-na` e une basse probabilitât di confusion cun peraulis comunis tal ambient domestic.

## Obietîf

Creâ un sisteme di domotiche privât, afidabil e svelt che al permeti di controlâ i dispositîfs de cjase cu lis comantadis vocâls, cence dipendence obligade dai servizis in nûl.

La architeture e combìne:

- Elaborazion locâl pes comantadis di domotiche e pe riservatece.
- Inteligjence locâl cun Ollama pes domandis gjenerâls.
- Modei in nûl pes richiestis complessis e lis informazions inzornadis.

## Hardware

- Raspberry Pi 5 cun 8 GB di RAM conseâts. Compatibilitât limitade fin a Raspberry Pi 3B+.
- Disc SSD NVMe cence doprâ une schede SD. Compatibilitât limitade cu la schede SD.
- Microfon e altoparlant USB bidirezionâi.
- Dispositîfs di domotiche compatibii cun Zigbee, Matter, Philips Hue o Wi-Fi locâl.
- Refredament atîf par evitâ il throttling termic.

## Architeture

1. Home Assistant OS al gjestìs i dispositîfs e lis automatizazions.
2. openWakeWord al rileve in maniere locâl la peraule di ativazion.
3. Whisper al trascrîf lis comantadis inte lenghe ative midiant Wyoming.
4. Il processôr des intencions al eseguìs in maniere locâl lis comantadis di domotiche.
5. Piper al sintetize lis rispuestis in catalan.
6. Ollama al rispuint a domandis gjenerâls cence mandâ dâts su Internet.
7. La IA in nûl e ricef dome richiestis esplicitis che a domandin IA avanzade.

## Funzionalitâts previodudis

- Control vocâl di lûs, prese, climatizazion, scuris e altris dispositîfs.
- Alias multilengâi.
- Temporizadôrs gjestîts cu la vôs.
- Consultazion locâl dal timp.
- Riproduzion e control de musiche.
- Ripiegament privât su un model di Ollama.
- Ricognizion de persone par mieç de vôs.
- Memorie dal contest a lunc tiermin.
- Inviament opzionâl a un model di IA in nûl.
- Copiis di sigurece e monitorament des prestazions.

## Principis di dissegn

- Lis comantadis di domotiche a àn di funzionâ cence conession a Internet.
- Il processôr locâl des intencions al à la precedence sui LLM.
- I dâts audio e lis conversazions privadis a vegnin elaborâts preferibilmentri in maniere locâl.
- I modei in nûl a vegnin doprâts dome par richiestis esplicitis o complessis, e dome se l'utent lu à domandât in maniere esplicite cuant che al à configurât l'assistent.
- Il sisteme al à di mantignî stabilis lis temperaduris e lis latençis sot caric continuatîf.

## Stât dal progjet

Il progjet al è definît come un backlog funzionâl. Lis configurazions specifichis, lis automatizazions e i script di implementazion a vignaran zontâts cuant che lis storis dai utents a vignaran completadis.
