**Aragonés · [Tornar a triar a luenga](../readme.md)**

# Asistent de hogar intelichent multilingüe

**Luenga:** Aragonés

**Leye-lo en:** [Catalán](Read.ca.md) · [Inglés](Read.en.md) · [Espanyol](Read.es.md) · [Francés](Read.fr.md) · [Alemán](Read.de.md) · [Italiano](Read.it.md) · [Portugués](Read.pt.md) · [Neerlandés](Read.nl.md)

Este prochecto describe o despliegue d'un ecosistema local de domótica en una Raspberry Pi con un asistente de voz multilingüe.

## Orichen d'o nombre Mina

**Mina** tien una radiz chermánica antiga en *minna*, que significa «memoria», «afecto» u «recuerdo». Tamién ye present en atras luengas: en persa, *mīnā* se relaciona con «luz» u «vidrio azul», y en chaponés, *mina* significa «totz» u «totz chuntos».

Istas interpretacions simbolizan una **memoria compartida y comunidat**, valors coherents con un asistente que acompanya y da soporte a la vida cutiana d'a casa.

En l'aspecto sonoro, Mina ye un nombre suau pero claro, con a pronunciación silabica `Mi-na` y una baixa probabilidat de confusión con parolas habituals en l'entorno domestico.

## Obchetivo

Crear un sistema de domótica privau, fiable y rapido que permita controlar os dispositivos d'a casa con ordens de voz, sin depender obligatoriament de servicios en a boira.

L'arquitectura combina:

- Procesamiento local ta ordens de domótica y privacidat.
- Inteligencia local con Ollama ta preguntas chenerals.
- Modelos en a boira ta consultas complexas y información actualizada.

## Hardware

- Raspberry Pi 5 con 8 GB de RAM recomendaus. Compatibilidat limitada dica Raspberry Pi 3B+.
- Disco SSD NVMe sin usar una tarcheta SD. Compatibilidat limitada con tarcheta SD.
- Microfono y altavoz USB bidireccional.
- Dispositivos de domótica compatibles con Zigbee, Matter, Philips Hue u Wi-Fi local.
- Refrigeración activa ta evitar o throttling termico.

## Arquitectura

1. Home Assistant OS chestiona os dispositivos y as automatizacions.
2. openWakeWord detecta localment a parola d'activación.
3. Whisper transcribe ordens en a luenga activa per medio de Wyoming.
4. O procesador d'intencions executa localment as ordens de domótica.
5. Piper sintetiza as respuestas en catalán.
6. Ollama responde a preguntas chenerals sin ninviar datos a Internet.
7. A IA en a boira nomás recibe consultas explicitas que requieren IA abanzada.

## Funcionalidaz previstas

- Control por voz de luces, enchufes, climatización, persianas y atros dispositivos.
- Alias multilingües.
- Temporizadors chestionaus por voz.
- Consulta meteorolochica local.
- Reproducción y control de musica.
- Alternativa privada con un modelo d'Ollama.
- Reconocimiento de a persona por a voz.
- Memoria de contexto a largo plazo.
- Derivación opcional a un modelo d'IA en a boira.
- Copias de seguranza y monitorización de o rendimiento.

## Principios de diseño

- As ordens de domótica han de funcionar sin conexión a Internet.
- O procesador local d'intencions tien prioridat sobre os LLM.
- Os datos d'audio y as conversacions privadas se procesan preferentment localment.
- Os modelos en a boira nomás s'utilizan ta consultas explicitas u complexas, y nomás si l'usuario lo ha solicitau explicitament en configurar l'asistente.
- O sistema ha de mantener temperaturas y latencias establas baixo carga continua.

## Estau d'o prochecto

O prochecto ye definito como un backlog funcional. As configuracions especificas, as automatizacions y os scripts de despliegue s'adhibirán conforme se completen as historias d'usuario.
