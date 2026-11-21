# Multilingual home automation assistant

**Language:** English · [Back to language selection](../readme.md)

**Read this in:** [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

This project describes deploying a local home automation ecosystem on a Raspberry Pi with a multilingual voice assistant.

## The origin of the name Mina

**Mina** has an ancient Germanic root in *minna*, meaning “memory,” “affection,” or “remembrance.” The name also appears in other languages: in Persian, *mīnā* is associated with “light” or “blue glass,” while in Japanese, *mina* means “everyone” or “all together.”

These interpretations symbolize **shared memory and community**, values that fit an assistant supporting everyday life at home.

Phonetically, Mina is a gentle yet clear name, pronounced in two syllables (`Mi-na`), with a low likelihood of being confused with common words in a home environment.

## Goal

Build a private, reliable, and fast home automation system for controlling household devices by voice, without requiring cloud services.

The architecture combines:

- Local processing for home automation commands and privacy.
- Local AI with Ollama for general questions.
- Cloud models for complex queries and up-to-date information.

## Hardware

- Raspberry Pi 5 with 8 GB of RAM recommended. Limited compatibility down to Raspberry Pi 3B+.
- NVMe SSD, avoiding the use of an SD card. Compatibility is limited when using an SD card.
- Two-way USB microphone and speaker.
- Home automation devices compatible with Zigbee, Matter, Philips Hue, or local Wi-Fi.
- Active cooling to prevent thermal throttling.

## Architecture

1. Home Assistant OS manages devices and automations.
2. openWakeWord locally detects the wake word.
3. Whisper transcribes commands in the active language through Wyoming.
4. The intent processor executes home automation commands locally.
5. Piper synthesizes responses in Catalan.
6. Ollama answers general questions without sending data to the Internet.
7. Cloud AI only receives explicit queries that require advanced AI.

## Planned features

- Voice control for lights, plugs, climate control, blinds, and other devices.
- Multilingual aliases.
- Voice-managed timers.
- Local weather queries.
- Music playback and control.
- Private fallback to an Ollama model.
- Voice recognition to identify the speaker.
- Long-term contextual memory.
- Optional routing to a cloud AI model.
- Backups and performance monitoring.

## Design principles

- Home automation commands must work without an Internet connection.
- The local intent processor takes priority over LLMs.
- Audio data and private conversations are preferably processed locally.
- Cloud models are used only for explicit or complex queries, and only if the user explicitly requested this when configuring the assistant.
- The system must maintain stable temperatures and latency under continuous load.

## Project status

The project is defined as a functional backlog. Specific configurations, automations, and deployment scripts will be added as user stories are completed.
