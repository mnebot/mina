**Mapudungun · [Amutuy tañi zugun kimün](../Read.md)**
# Ruka kelluay ka küme zugun mew

**Zugun:** Mapudungun

**Feyentun tüfachi zugun mew:** [Mapudungun](Read.arn.md) · [English](Read.en.md) · [Català](Read.ca.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Tüfachi küdaw nütramkakey kiñe ruka domótico sistema Raspberry Pi mew, fey mew kiñe küme zugun ñi azkintun ka femngechi müley.

## Mina ñi üy ñi tuwün

**Mina** ñi üy tüfachi füta german zugun *minna* mew küpay, ñi kimel «rakizuam», «ayün» kam «rakizuamün». Ka femngechi müley ka zugun mew: persa zugun mew *mīnā* «pelom» kam «kallfü vidrio» mew müley; japonés zugun mew *mina* «kom pu che» kam «kom kiñe mew» ñi pin.

Tüfachi kimün **kiñe rakizuam ka kom pu che** ñi nentun, fey tüfachi küme kelluay ñi müleal pu ruka ñi antü küdaw mew.

Mina ñi üy küme allkügey ka pepi kimngey: `Mi-na` epu sílaba mew nütramgey, ka ruka mew ñi pepi zugun mew niewelay tañi azkintun.

## Nütram

Kiñe ruka domótico sistema ñi küme, feyentun ka utut küdaw, ñi pepi küdaw mew, ka zugun mew pu dispositivo ñi kelluael, nube servicios mew tañi pepi mülewel.

Tüfachi arquitectura kelluay:

- Local procesamiento ñi domótico comandos ka ñi feyentun.
- Ollama ñi local inteligencia ñi general preguntas.
- Nube modelos ñi küme preguntas ka we kimün.

## Hardware

- Raspberry Pi 5 8 GB RAM mew, küme kimel. Raspberry Pi 3B+ mew pichi compatibilidad.
- NVMe SSD disco, SD tarjeta mülewel. SD tarjeta mew pichi compatibilidad.
- USB micrófono ka altavoz epu tuwün.
- Zigbee, Matter, Philips Hue kam local Wi-Fi mew müley pu domótico dispositivo.
- Küme enfriamiento ñi küdaw, ama kütral mew rendimiento ñi pichi.

## Arquitectura

1. Home Assistant OS kelluay pu dispositivo ka automatización.
2. openWakeWord local kimgey ñi activación zugun.
3. Whisper nütramgey ñi comando ñi zugun, Wyoming mew.
4. Intenciones procesador kelluay pu domótico comando local mew.
5. Piper zugunentuy ñi respuesta catalán mew.
6. Ollama kelluay ñi general pregunta, Internet mew kimün trürwel.
7. Nube IA müley ñi pregunta ñi chemkün, ñi müley küme IA.

## Ñi küdaw femngechi

- Kelluay ñi luz, enchufe, kütralko, persiana ka ka dispositivo zugun mew.
- Achka zugun ñi alias.
- Zugun mew ñi temporizador.
- Ruka ñi meteorología kimün.
- Música ñi playback ka control.
- Ollama modelo ñi feyentun fallback.
- Che ñi kimün ñi zugun mew.
- Füta pichi contexto memoria.
- Nube IA modelo mew ñi optional derivación.
- Backups ka rendimiento nentun.

## Diseño ñi principios

- Domótico comandos ñi küdaw Internet mülewel mew.
- Local intenciones procesador ñi LLM ñi müleal ñi prioridad.
- Audio datos ka privado conversaciones ñi local küdaw ñi müley.
- Nube modelos ñi küdaw explicit preguntas kam küme preguntas mew, ka user ñi asistente ñi configuración mew ñi explicit kelluay.
- Sistema ñi temperatura ka latencia ñi küme müleal fey ñi küdaw mew.

## Proyecto ñi müleal

Tüfachi proyecto kiñe functional backlog mew müley. Configuraciones específicas, automatizaciones ka deployment scripts ñi yapamun user historias ñi küzaw ñi tukuluwün mew.
