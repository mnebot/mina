**Avañe’ẽ · [Jevy eiporavo hag̃ua ñe’ẽ](../readme.md)**
# Óga pytyvõhára heta ñe’ẽme

**Ñe’ẽ:** Avañe’ẽ

**Emoñe’ẽ ko’ã ñe’ẽme:** [Avañe’ẽ](Read.gn.md) · [English](Read.en.md) · [Català](Read.ca.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Ko tembiapo omombe’u peteĩ sistema domótico oĩva nde rógape, Raspberry Pi ári, ha peteĩ pytyvõhára ñe’ẽ rupive oñe’ẽkuaáva heta ñe’ẽme.

## Moõguipa ou Mina réra

**Mina** oguereko hapo germánico yma guarépe, ñe’ẽ *minna*; he’ise «mandu’a», «mborayhu» térã «mandu’apy». Oĩ avei ambue ñe’ẽme: persa-pe, *mīnā* oñembojoaju «tesape» térã «vidrio hovy» rehe; japonés-pe, *mina* he’ise «opavave» térã «enterove oñondive».

Ko’ã he’iséva ohechauka **mandu’a oñondive ha tekojoja**, valores ojojáva peteĩ pytyvõhára omoirũva ha oipytyvõva óga rekove ára ha ára ndive.

Mina réra ipu porã, ipy’aguapy ha hesakã; oñe’ẽ `Mi-na` mokõi sílaba-pe ha sa’i ikatu oñembojoavy ñe’ẽ ojeipurúva jepi óga ryepýpe ndive.

## Hembipota

Jajapo peteĩ sistema domótico ñemigua, jeroviaha ha pya’e, ikatu hag̃ua jaipuru ñande rógape umi tembipuru ñane ñe’ẽ rupive, ha ndaha’éi tekotevẽva katuete jajesareko servicio nube rehe.

Ko arquitectura ombojoaju:

- Ñemba’apo tendápe, domótica ha ñemigua hag̃ua.
- Inteligencia tendápe Ollama ndive, porandu jepiveguápe g̃uarã.
- Modelos nube-pegua porandu hasýva ha marandu pyahúpe g̃uarã.

## Hardware

- Raspberry Pi 5 oguerekóva 8 GB RAM oñembojerovia. Raspberry Pi 3B+ peve compatibilidad sa’i.
- Disco SSD NVMe, tarjeta SD’ỹre. Tarjeta SD ndive compatibilidad sa’i.
- Micrófono ha altavoz USB mokõive hendáicha.
- Tembipuru domótico oñembojáva Zigbee, Matter, Philips Hue térã Wi-Fi tendápe rehe.
- Enfriamiento activo ani hag̃ua hakueterei ha omboguejy rendimiento.

## Arquitectura

1. Home Assistant OS omongu’e tembipuru ha automatizaciones.
2. openWakeWord ohechakuaa tendápe ñe’ẽ ñepyrũha.
3. Whisper ohai ñe’ẽme umi tembiapoukapy, ñe’ẽ ojeiporúva rupive Wyoming ndive.
4. Procesador de intenciones omboaje tendápe umi tembiapoukapy domótico.
5. Piper omoheñói mbohovái Catalán-pe.
6. Ollama ombohovái porandu jepivegua omondo’ỹre dato Internet-pe.
7. IA nube-pegua ohupyty porandu añoite, tekotevẽ jave IA ipu’akáva.

## Mba’e ikatútava ojapo

- Jaipuru ñe’ẽ rupive tesape, enchufe, aire acondicionado, persiana ha ambue tembipuru.
- Alias heta ñe’ẽme.
- Temporizador ñe’ẽ rupive.
- Jeporeka ára rehegua tendápe.
- Música ñembopu ha ñemongu’e.
- Fallback ñemigua peteĩ modelo Ollama-pe.
- Jaikuaa mávapa oñe’ẽ iñe’ẽ rupive.
- Memoria contexto puku ára g̃uarã.
- Opción-pe emondo peteĩ modelo IA nube-pegua.
- Copias de seguridad ha rendimiento monitorización.

## Principios de diseño

- Tembiapoukapy domótico omba’apova’erã Internet’ỹre.
- Procesador de intenciones tendápegua oguerekova’erã prioridad LLM ári.
- Datos audio ha conversación ñemigua ojeporavova’erã oñemba’apo tendápe.
- Modelos nube-pegua ojepuru porandu ojejeruréva térã hasývape g̃uarã añoite, ha usuario ojerure rire hesakãháicha configuración-pe.
- Sistema oñangarekova’erã temperatura ha latencia estable rehe carga meme jave.

## Mba’éichapa oĩ ko proyecto

Ko proyecto oñemohenda backlog funcional ramo. Configuraciones especiales, automatizaciones ha scripts de despliegue oñemoĩta ohóvo ojejapopa rire umi tembiapo usuario rehegua.
