**Galego · [Volver á selección do idioma](../readme.md)**

# Asistente multilingüe para o fogar intelixente

**Idioma:** galego

**Ler en:** [Catalán](Read.ca.md) · [Inglés](Read.en.md) · [Castelán](Read.es.md) · [Francés](Read.fr.md) · [Alemán](Read.de.md) · [Italiano](Read.it.md) · [Portugués](Read.pt.md) · [Neerlandés](Read.nl.md)

Este proxecto describe a implantación dun ecosistema local de domótica nunha Raspberry Pi cun asistente de voz multilingüe.

## Orixe do nome Mina

**Mina** ten a súa raíz no xermánico antigo *minna*, que significa «memoria», «afecto» ou «recordo». Tamén aparece noutras linguas: en persa, *mīnā* relaciónase coa «luz» ou co «vidro azul», e en xaponés *mina* significa «todos» ou «todos xuntos».

Estas interpretacións simbolizan unha **memoria compartida e comunidade**, valores coherentes cun asistente que acompaña e apoia a vida cotiá do fogar.

En canto ao son, Mina é un nome suave pero claro, coa pronuncia silábica `Mi-na` e pouca probabilidade de confundirse con palabras habituais no ámbito doméstico.

## Obxectivo

Crear un sistema domótico privado, fiable e rápido que permita controlar os dispositivos do fogar mediante ordes de voz, sen depender obrigatoriamente de servizos na nube.

A arquitectura combina:

- Procesamento local para as ordes domóticas e a privacidade.
- Intelixencia local con Ollama para preguntas xerais.
- Modelos na nube para consultas complexas e información actualizada.

## Hardware

- Raspberry Pi 5 con 8 GB de RAM recomendados. Compatibilidade limitada ata Raspberry Pi 3B+.
- Disco SSD NVMe sen usar unha tarxeta SD. Compatibilidade limitada coa tarxeta SD.
- Micrófono e altofalante USB bidireccionais.
- Dispositivos domóticos compatibles con Zigbee, Matter, Philips Hue ou Wi-Fi local.
- Refrixeración activa para evitar a redución térmica do rendemento.

## Arquitectura

1. Home Assistant OS xestiona os dispositivos e as automatizacións.
2. openWakeWord detecta localmente a palabra de activación.
3. Whisper transcribe as ordes no idioma activo mediante Wyoming.
4. O procesador de intencións executa localmente as ordes domóticas.
5. Piper sintetiza as respostas en catalán.
6. Ollama responde preguntas xerais sen enviar datos a Internet.
7. A IA na nube só recibe consultas explícitas que requiren IA avanzada.

## Funcionalidades previstas

- Control por voz das luces, enchufes, climatización, persianas e outros dispositivos.
- Alias multilingües.
- Temporizadores xestionados por voz.
- Consulta meteorolóxica local.
- Reprodución e control da música.
- Alternativa privada cun modelo de Ollama.
- Recoñecemento da persoa pola voz.
- Memoria de contexto a longo prazo.
- Derivación opcional a un modelo de IA na nube.
- Copias de seguridade e monitorización do rendemento.

## Principios de deseño

- As ordes domóticas deben funcionar sen conexión a Internet.
- O procesador local de intencións ten prioridade sobre os LLM.
- Os datos de audio e as conversas privadas procésanse preferentemente en local.
- Os modelos na nube só se usan para consultas explícitas ou complexas, e só se o usuario o solicitou expresamente ao configurar o asistente.
- O sistema debe manter temperaturas e latencias estables baixo carga continua.

## Estado do proxecto

O proxecto está definido como un backlog funcional. As configuracións específicas, as automatizacións e os scripts de implantación engadiranse a medida que se completen as historias de usuario.
