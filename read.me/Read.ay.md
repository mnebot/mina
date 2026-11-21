**Aymar aru · [Ajlliñaru kutt’aña](../Read.md)**
# Utana yanapt’ir multiidioma

**Aru:** Aymara

**Aka arunakan ullaña:** [Aymara](Read.ay.md) · [English](Read.en.md) · [Català](Read.ca.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Aka luräwix Raspberry Pi ukar utt’ayata, utana apnaqañ local ecosistema ukat walja arunakan arumpi yanapt’ir asistente ukat parlasi.

## Mina sutina qalltäwipa

**Mina** sutix nayra germano arun *minna* arut jutiriwa, ukax «amtaña», «munasiña» jan ukax «amta» sañ muni. Yaqha arunakanx utjarakiwa: persa arun *mīnā* ukax «qhana» jan ukax «ch’uxña vidrio» ukamp chikt’atawa; japonés arun *mina* ukax «taqpach jaqinaka» jan ukax «taqpach mayaki» sañ muni.

Aka amuyunakax **mayacht’ata amta ukat marka** uñacht’ayi, ukax utana sapür jakañ yanapt’ir asistente ukampiw mayacht’asi.

Mina sutix sum ist’asi, ukampis qhanawa: `Mi-na` sasin pä silaba arsuñawa, ukat utana apnaqat arunakamp pantjasiñax juk’akiwa.

## Amtawi

Nayraru, atinuyañjama ukat jank’ak utana apnaqañ sistema luraña; utan dispositivo-naka arumpi apnaqañataki, nube servicios ukanakaru obligado dependenciani.

Arquitecturax akham mayach’i:

- Uta kamachinak ukat privacidad uñjañatak local procesamiento.
- Jach’a jiskt’awinakatak Ollama ukampi local inteligencia.
- Sinti ch’amani jiskt’awinakatak ukat machaq yatiyawinakatak nube modelos.

## Hardware

- 8 GB RAM ukani Raspberry Pi 5 iwxt’ata. Raspberry Pi 3B+ ukakama mä juk’a compatibilidad.
- Tarjeta SD jan apnaqasa NVMe SSD disco. SD tarjeta ukamp mä juk’a compatibilidad.
- USB micrófono ukat pä tuqit apnaqañ altavoz.
- Zigbee, Matter, Philips Hue jan ukax local Wi-Fi ukampi suma luriri utana dispositivos.
- Thaya apnaqañ activo sistema, thayañx jisk’achasiñapataki.

## Arquitectura

1. Home Assistant OS ukax dispositivos ukat automatizaciones ukanak apnaqi.
2. openWakeWord ukax activación arut local tuqit yatxati.
3. Whisper ukax activo arun arunak qillqiru tukuyi, Wyoming ukampi.
4. Intenciones procesador ukax utana kamachinak local tuqit phuqhi.
5. Piper ukax respuesta-naka catalán arun arsuwayi.
6. Ollama ukax Internet ukar yatiyawi jan apayasina general jiskt’awinak askichi.
7. Nube IA ukarux avanzadan IA munki ukat usuario qhanpach jiskt’ki ukhaki consulta apayasi.

## Nayrar sartañapatak wakichata luräwinaka

- Luces, enchufes, climatización, persianas ukat yaqha dispositivos arumpi apnaqaña.
- Walja arunakan sutipa/alias.
- Arumpi apnaqat temporizadores.
- Uta jak’an meteorología jiskt’aña.
- Música reproducción ukat control.
- Ollama model ukar privado fallback.
- Arut jaqir uñt’aña.
- Jaya pachan contexto memoria.
- Munaspa ukhax nube IA model ukar apayaña.
- Copias de seguridad ukat rendimiento monitorización.

## Diseño kamachinaka

- Uta kamachinakax Internet jan utjkipansa irnaqañapawa.
- Local intenciones procesador ukax LLM-nakat nayrankañapawa.
- Audio datos ukat privado parlt’awinakax nayraqata local tuqit apnaqatäñapawa.
- Nube modelos ukax qhanpach jiskt’awinakataki jan ukax ch’amani jiskt’awinakatakiw apnaqasïna; ukat asistente wakichañ pachan usuario qhanpach munki ukhaki.
- Sistema ukax sapa kuti carga utjkipan temperatura ukat latencia estable uñjañapawa.

## Luräwina estado

Aka proyecto ukax funcional backlog ukham utt’ayatawa. Configuraciones específicas, automatización ukat despliegue scripts yapxatañawa, usuario historias phuqhaskipan.
