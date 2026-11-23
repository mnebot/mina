# Especificació base d'arquitectura: Assistent de veu minimalista i modular (Català)

## 1. Objectiu i abast

Construir un sistema d'assistent de veu i control domèstic **minimalista, de codi lliure i altament modular**, dissenyat per:

- Executar un **subconjunt concret de funcionalitats** sense sobrecàrrega.
- Funcionar en una **Raspberry Pi 3** (1 GB de RAM) connectada a un **Jabra SPEAK 510 USB** (`sound`, `/dev/snd/controlC2`).
- Reutilitzar el mateix **core lleuger** en maquinaris més potents (Raspberry Pi 5, mini-PC, servidor domèstic o contenidors) afegint o canviant adaptadors sense reescriure el domini.
- Treballar inicialment **només en català (`ca`)** (entrada i resposta), mantenint el disseny obert a futurs idiomes.

### Funcionalitats requerides

1. **Àudio bidireccional amb Jabra SPEAK 510 USB:** Captura de veu pel micròfon i reproducció d'àudio/resposta per l'altaveu.
2. **Sintonitzar emissores de ràdio:** Reproduir l'emissora sol·licitada per veu a partir d'un catàleg/streams d'àudio.
3. **Regular llums Philips Hue:** Controlar estat (`on`/`off`), brillantor i/o ambient de llums o zones.
4. **Reproduir música de Spotify:** Buscar i iniciar reproducció de la música sol·licitada (cançó, artista, àlbum o llista).
5. **Gestionar alarmes i temporitzadors:** Crear i controlar temporitzadors i alarmes.

---

## 2. Principis no funcionals i restriccions

- **Minimalisme i rendiment en RPi 3:** Evitar serveis pesants innecessaris o càrregues d'inferència STT/TTS grans directament a la Pi 3 si comprometen la memòria o la latència; descarregar tasques pesants a un altre node de la xarxa quan calgui (p. ex. via **Wyoming Protocol**).
- **Només codi lliure i reutilització:** Reutilitzar components i protocols oberts existents (ALSA, openWakeWord, Wyoming, Piper/Whisper, integracions existents) en lloc de reinventar infraestructures bàsiques.
- **Modularitat i expansivitat:** Separació estricta entre lògica de negoci/orquestració i integracions externes per facilitar l'evolució cap a maquinaris superiors o noves capacitats.
- **Idioma per defecte:** Català (`ca`) tant en la comprensió d'ordres com en la generació de respostes. Que es pugui triar també l'idioma a l'anglès (`en`). Filosofia i18n.

---

## 3. Decisió arquitectònica: Patró Hexagonal (Ports i Adapters)

S'adopta l'**arquitectura hexagonal (Ports i Adapters)** perquè:

- **Aïlla el domini i els casos d'ús** de detalls de maquinari (Jabra, ALSA, sensors, botons) i de proveïdors externs (Hue, Spotify, streams de ràdio, backends STT/TTS).
- **Permet escalar o migrar maquinari** canviant o activant adaptadors sense alterar el nucli comú.
- **Evita la complexitat d'arquitectures distribuïdes pesants** (com microserveis múltiples o brokers complexos) que penalitzarien un node d'1 GB de RAM.

---

## 4. Estructura de components

### 4.1. Core comú i lleuger (Domini i aplicació)

En la primera entrega (US-02), el core ofereix un port d'entrada per rebre una petició de text i un port de sortida que emet `He rebut: <petició>`. Els ports específics de ràdio, Hue, Spotify, àudio i alarmes s'afegiran amb les històries que implementin aquestes capacitats. La llista següent descriu l'arquitectura objectiu, no l'abast d'aquest primer increment.

- **Intent / Command Router (`ca`):** Interpreta i enruta ordres cap als casos d'ús corresponents (ràdio, llums Hue, Spotify, alarmes/temporitzadors).
- **Gestor d'alarmes i temporitzadors:** Manté i dispara temporitzadors i alarmes programades.
- **Gestor de reproducció / context:** Coordina l'estat d'àudio actiu (resposta TTS, emissora de ràdio o música).
- **Ports d'entrada (Driving Ports):** Contractes per rebre ordres/sessions de veu, esdeveniments o programacions.
- **Ports de sortida (Driven Ports):** Contractes abstractes cap a veu/àudio, ràdio, il·luminació Hue, música i notificacions/alarmes.

### 4.2. Adaptadors d'entrada (Driving Adapters)

- **Jabra Audio + WakeWord + STT Adapter:** Captura àudio amb el **Jabra SPEAK 510 USB** via ALSA, detecta la paraula d'activació (p. ex. *openWakeWord*) i envia la captura a STT en català (local en equips potents o remot via Wyoming en RPi 3).
- **Altres entrades (extensibles):** CLI, API/webhook, botons o integració amb Home Assistant.

### 4.3. Adaptadors de sortida (Driven Adapters)

- **TTS + Jabra Playback Adapter:** Genera la resposta en català (p. ex. Piper) i la reprodueix per l'altaveu del Jabra.
- **Radio Adapter:** Resol el nom de l'emissora a la seva font/stream i en controla la reproducció.
- **Hue Adapter:** Executa accions d'encesa, apagada, intensitat i regulació sobre llums/zones Philips Hue.
- **Spotify Adapter:** Inicia reproducció del contingut sol·licitat a Spotify.
- **Alarm & Timer Adapter:** Materialitza avisos sonors o accions quan caduca un temporitzador o sona una alarma.

---

## 5. Perfils de desplegament (Portabilitat de maquinari)


| Component                                       | Perfil RPi 3 (1 GB RAM)                | Perfil maquinari superior (RPi 5 / Mini-PC / Servidor) |
| :---------------------------------------------- | :------------------------------------- | :----------------------------------------------------- |
| **Core + Ports**                                | Actiu (lleuger)                        | Mateix core sense modificacions                        |
| **Entrada/Sortida àudio**                      | Jabra SPEAK 510 USB (ALSA)             | Jabra USB o dispositius/satèl·lits addicionals       |
| **STT i TTS (`ca`)**                            | Preferentment en node extern (Wyoming) | Local o remot segons latència/recursos desitjats      |
| **Adaptadors Hue / Ràdio / Spotify / Alarmes** | Actius només els necessaris           | Mateixos adaptadors + nous adaptadors extensibles      |

---

## 6. Directrius per a la generació d'especificacions a OpenSpec

Quan es generin les especificacions formals a **OpenSpec** a partir d'aquest document, cal desglossar-les com a mínim en els blocs següents:

1. **`core-domain-and-intents`:** Regles de negoci, contractes de ports d'entrada/sortida i resolució d'ordres en català per a ràdio, Hue, Spotify i alarmes/temporitzadors.
2. **`audio-and-voice-pipeline`:** Captura i reproducció amb Jabra SPEAK 510 USB, detecció de paraula d'activació i integració STT/TTS en català (amb suport local i remot via Wyoming).
3. **`device-adapters`:** Especificació individual dels adaptadors de ràdio, Philips Hue, Spotify i alarmes/temporitzadors.
4. **`runtime-profiles-and-portability`:** Configuració de perfils de rendiment (RPi 3 vs. maquinari més potent) i criteris per afegir nous adaptadors sense tocar el core.
