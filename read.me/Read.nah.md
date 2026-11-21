**Nāhuatl · [Mocuepa xicpepena in tlahtōlli](../readme.md)**
# Cencalli tēpalēhuīlli miyac tlahtōl

**Tlahtōlli:** Nāhuatl

**Xicmopōhua īpan:** [Nāhuatl](Read.nah.md) · [English](Read.en.md) · [Català](Read.ca.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Inin tēquitl quihtōhua quen motlalia ce sistema domótico īpan Raspberry Pi, īhuān ce tlahtōltepalehuilīlli miyac tlahtōl īpan.

## Inīn Mina tōcāitl īpeuhyan

**Mina** quipia īnelhuayōtl īpan huehcauh germánico *minna*, quītōznequi «ilnāmiki», «tēicnēlīlli» nōzo «ilnāmictli». No īpan occequintin tlahtōlli: īpan persa, *mīnā* motēnehuia īhuān «tlahuīlli» nōzo «xoxoctic vidrio»; īpan japonés, *mina* quītōznequi «mochintin» nōzo «mochintin san cen».

Inin tlanēxtīlli quimītōhua **ilnāmictli īhuān cēnca tlācameh**, tlamantli hueli ce tepalehuilīlli quichīhua īhuān quimopalehuia cecemilhuitl īpan cencalli.

Mina tōcāitl hueli caqui, yehhuātl yāuhyāuh īhuān chipāhuac: `Mi-na` ome sílaba, īhuān ahmo hueli mopātlā īhuān tlahtōlli occequintin īpan cencalli.

## Tēquitl

Ticchīhuazque ce sistema domótico ichtaca, temachti īhuān niman; ītēchpalehuil īpan cencalli ītlamantli tlahtōl īhuān amo monequi nochipa nube servicios.

Inin arquitectura quinelhuia:

- Local procesamiento para domotic commands īhuān privacidad.
- Ollama īpan local inteligencia para preguntas generales.
- Modelos nube para preguntas chicāhuac īhuān información yancuic.

## Hardware

- Raspberry Pi 5 īhuān 8 GB RAM motēnehuia. Compatibilidad amo hueyi hasta Raspberry Pi 3B+.
- NVMe SSD disco amo SD tarjeta. Compatibilidad amo hueyi īhuān SD tarjeta.
- USB micrófono īhuān altavoz ome tlamantli.
- Domotic dispositivos hueli Zigbee, Matter, Philips Hue nōzo local Wi-Fi.
- Activo enfriamiento para amo mocēcēya, amo mocuīca rendimiento.

## Arquitectura

1. Home Assistant OS quimīpia dispositivos īhuān automatizaciones.
2. openWakeWord local quimachilia in activación tlahtōlli.
3. Whisper quicuiloa comandos īpan tlahtōlli activo, Wyoming īpan.
4. Intenciones procesador quichīhua local domotic comandos.
5. Piper quipiya respuestas īpan catalán.
6. Ollama quinanquilia preguntas generales amo quititlan información Internet īpan.
7. Nube IA quipiya san preguntas explícitas ītēchmonequi avanzada IA.

## Funcionalidades tlein mochīhuaz

- Tlahtōl īpan control para luces, enchufes, clima, persianas īhuān occequintin dispositivos.
- Alias miyac tlahtōl.
- Temporizadores tlahtōl īpan.
- Local meteorología consulta.
- Música reproducción īhuān control.
- Ichtaca fallback para ce modelo Ollama.
- Tēixmatiliztli īpan tēnōtza.
- Huehca tiempo contexto memoria.
- Optional dirección īpan ce modelo nube IA.
- Backups īhuān rendimiento monitorización.

## Diseño principios

- Domotic comandos monequi tequitiz amo Internet.
- Local intenciones procesador quipia prioridad īpan LLM.
- Audio datos īhuān privado conversaciones achto local motequihuia.
- Nube modelos motequihuia san explícitas nōzo complejas preguntas, īhuān san tla usuario explícitamente quinequi īpan configuración in asistente.
- Sistema monequi quipiya estable temperaturas īhuān latencias nochipa tequitl.

## Proyecto estado

Inin proyecto functional backlog īpan motēca. Configuraciones específicas, automatizaciones īhuān deployment scripts mochīhuazque cuando se completen historias de usuario.
