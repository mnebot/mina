**Asturianu · [Volver a escoyer l'idioma](../Read.md)**

# Asistente multillingüe pa la llar intelixente

**Idioma:** Asturianu

**Lleer en:** [Catalán](Read.ca.md) · [Inglés](Read.en.md) · [Español](Read.es.md) · [Francés](Read.fr.md) · [Alemán](Read.de.md) · [Italianu](Read.it.md) · [Portugués](Read.pt.md) · [Neerlandés](Read.nl.md)

Esti proyectu describe'l despliegue d'un ecosistema domóticu llocal nun Raspberry Pi con un asistente de voz multillingüe.

## Oríxen del nome Mina

**Mina** tien la so raigañu nel xermánicu antiguu *minna*, que significa «memoria», «afectu» o «recuerdu». Tamién apaez n'otres llingües: en persa, *mīnā* rellaciónase con «lluz» o «vidriu azul», y en xaponés, *mina* significa «tol mundu» o «toos xuntos».

Estes interpretaciones simbolicen una **memoria compartida y comunidá**, valores coherentes con un asistente que acompaña y sofita la vida diaria de la casa.

Nel aspeutu sonoru, Mina ye un nome suave pero claro, cola pronunciación silábica `Mi-na` y una baxa probabilidá de confundise con pallabres habituales nel entornu domésticu.

## Oxetivu

Crear un sistema domóticu priváu, fiable y rápidu que permita controlar los dispositivos de la casa con órdenes de voz, ensin depender obligatoriamente de servicios na nube.

L'arquitectura combina:

- Procesamientu llocal pa órdenes domótiques y privacidá.
- Intelixencia llocal con Ollama pa entrugues xenerales.
- Modelos na nube pa consultes complexes ya información actualizada.

## Hardware

- Raspberry Pi 5 con 8 GB de RAM recomendados. Compatibilidá llendada hasta Raspberry Pi 3B+.
- Disc SSD NVMe ensin usar tarxeta SD. Compatibilidá llendada con tarxeta SD.
- Micrófonu y altavoz USB bidireccionales.
- Dispositivos domóticos compatibles con Zigbee, Matter, Philips Hue o Wi-Fi llocal.
- Refrigeración activa pa evitar el throttling térmicu.

## Arquitectura

1. Home Assistant OS xestiona los dispositivos y les automatizaciones.
2. openWakeWord detecta llocalmente la pallabra d'activación.
3. Whisper trescribe les órdenes nel idioma activu per Wyoming.
4. El procesador d'intenciones executa llocalmente les órdenes domótiques.
5. Piper sintetiza les respuestes en catalán.
6. Ollama resuelve entrugues xenerales ensin unviar datos a Internet.
7. La IA na nube namás recibe consultes esplícites que precisen IA avanzada.

## Funcionalidaes previstes

- Control por voz de lluces, enchufes, climatización, persianes y otros dispositivos.
- Alies multillingües.
- Temporizadores controlaos por voz.
- Consulta meteorolóxica llocal.
- Reproducción y control de música.
- Alternativa privada con un modelu d'Ollama.
- Reconocimientu de la persona pola voz.
- Memoria de contestu a llargu plazu.
- Derivación opcional a un modelu d'IA na nube.
- Copies de seguridá y monitorización del rindimientu.

## Principios de diseñu

- Les órdenes domótiques tienen que funcionar ensin conexón a Internet.
- El procesador llocal d'intenciones tien prioridá sobre los LLM.
- Los datos d'audiu y les conversaciones privaes procésense preferentemente llocalmente.
- Los modelos na nube namás s'usen pa consultes esplícites o complexes, y namás si l'usuariu lo solicitó esplícitamente al configurar l'asistente.
- El sistema tien de caltener temperatures y llatencies estables baxo carga continua.

## Estáu del proyectu

El proyectu ta definíu como un backlog funcional. Les configuraciones específiques, les automatizaciones y los scripts de despliegue van amestase según se completen les histories d'usuariu.
