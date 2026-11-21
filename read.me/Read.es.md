# Asistente domótico multilingüe

**Idioma:** Español · [Volver a elegir idioma](../Read.md)

**Leer en:** [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Este proyecto describe el despliegue de un ecosistema domótico local en una Raspberry Pi con un asistente de voz multilingüe.

## Origen del nombre Mina

**Mina** tiene una raíz germánica antigua en *minna*, que significa «memoria», «afecto» o «recuerdo». También está presente en otras lenguas: en persa, *mīnā* se relaciona con «luz» o «vidrio azul», y en japonés, *mina* significa «todo el mundo» o «todos juntos».

Estas interpretaciones simbolizan **memoria compartida y comunidad**, valores coherentes con un asistente que acompaña y apoya la vida cotidiana del hogar.

En cuanto a su sonido, Mina es un nombre suave pero claro, pronunciado en dos sílabas (`Mi-na`), con pocas probabilidades de confundirse con palabras habituales en el entorno doméstico.

## Objetivo

Crear un sistema domótico privado, fiable y rápido que permita controlar los dispositivos del hogar mediante comandos de voz, sin depender necesariamente de servicios en la nube.

La arquitectura combina:

- Procesamiento local para los comandos domóticos y la privacidad.
- Inteligencia local con Ollama para preguntas generales.
- Modelos en la nube para consultas complejas e información actualizada.

## Hardware

- Raspberry Pi 5 con 8 GB de RAM recomendados. Compatibilidad limitada hasta Raspberry Pi 3B+.
- Disco SSD NVMe para evitar el uso de una tarjeta SD. Compatibilidad limitada al usar una tarjeta SD.
- Micrófono y altavoz USB bidireccionales.
- Dispositivos domóticos compatibles con Zigbee, Matter, Philips Hue o Wi-Fi local.
- Refrigeración activa para evitar el throttling térmico.

## Arquitectura

1. Home Assistant OS gestiona los dispositivos y las automatizaciones.
2. openWakeWord detecta localmente la palabra de activación.
3. Whisper transcribe los comandos en el idioma activo mediante Wyoming.
4. El procesador de intenciones ejecuta localmente los comandos domóticos.
5. Piper sintetiza las respuestas en catalán.
6. Ollama responde a preguntas generales sin enviar datos a Internet.
7. La IA en la nube solo recibe consultas explícitas que requieren IA avanzada.

## Funcionalidades previstas

- Control por voz de luces, enchufes, climatización, persianas y otros dispositivos.
- Alias multilingües.
- Temporizadores controlados por voz.
- Consultas meteorológicas locales.
- Reproducción y control de música.
- Alternativa privada con un modelo de Ollama.
- Reconocimiento de la persona por la voz.
- Memoria contextual a largo plazo.
- Derivación opcional a un modelo de IA en la nube.
- Copias de seguridad y monitorización del rendimiento.

## Principios de diseño

- Los comandos domóticos deben funcionar sin conexión a Internet.
- El procesador local de intenciones tiene prioridad sobre los LLM.
- Los datos de audio y las conversaciones privadas se procesan preferentemente en local.
- Los modelos en la nube solo se utilizan para consultas explícitas o complejas, y únicamente si el usuario lo solicitó expresamente al configurar el asistente.
- El sistema debe mantener temperaturas y latencias estables con carga continua.

## Estado del proyecto

El proyecto está definido como un backlog funcional. Las configuraciones específicas, las automatizaciones y los scripts de despliegue se añadirán a medida que se completen las historias de usuario.
