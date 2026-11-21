**Runasimi · [Runasimi akllayman kutiy](../readme.md)**
# Achka simipi wasi yanapaq

**Simi:** Runasimi

**Kay simikunapi ñawinchay:** [Runasimi](Read.qu.md) · [English](Read.en.md) · [Català](Read.ca.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Kay llamk’ayqa Raspberry Pi patapi wasi ukhupi llamk’achiyta, achka simipi rimay yanapaqwanmi willan.

## Mina sutipa paqarisqan

**Mina** sutipa sapin ñawpa germánico *minna* simipi, chayqa «yuyay», «munakuy» utaq «yuyarina» nin. Huk simikunapipas kashan: persa simipi *mīnā* «k’anchay» utaq «anqas q’ispiy» nisqawan tinkun; japonés simipi *mina* «llapan runakuna» utaq «llapanchik kuska» nin.

Kay yuyaykuna **kuska yuyayta, aylluta** rikuchin; wasi kawsaypi punchaw punchaw yanapaqwan kuska purin.

Mina suti sumaq uyarikun, ichaqa sut’i; `Mi-na` iskay sílaba nispa rimakun, wasipi sapa kuti nisqa simikunawan pantayqa pisi.

## Munasqan

Sapaq, atipay atina, utqay wasi sistema ruwana, wasi kaqkunata rimay kamachiywan kamachinapaq; nube serviciokunaman mana sapa kuti watasqa.

Arquitectura kaykunata huñun:

- Wasi kamachiy, sapaq kay ima kananpaq local procesamiento.
- Ollama-wan local inteligencia, llapanmanta tapukuykunapaq.
- Sasachaq tapukuykunapaq, musuq willaykunapaq nube modelokuna.

## Hardware

- Raspberry Pi 5, 8 GB RAM nisqayuq alli yuyay. Raspberry Pi 3B+ kama pisi compatibilidad.
- NVMe SSD disco, SD tarjeta mana llamk’achispa. SD tarjeta-wan pisi compatibilidad.
- USB micrófono, iskay ñiqinpi llamk’aq altavoz.
- Zigbee, Matter, Philips Hue utaq local Wi-Fi-wan allin domótica kaqkuna.
- K’uyay ñit’iy ama ruphaywan rendimiento pisiyananpaq.

## Arquitectura

1. Home Assistant OS kaqkunata, automatizaciónkunata kamachin.
2. openWakeWord qallariy rimayta local riqsiy.
3. Whisper llamk’achisqa simipi kamachiykunata qillqaman tikran, Wyoming-ta llamk’achispa.
4. Intenciones procesador wasi kamachiykunata local ruray.
5. Piper kutichiykunata catalán simipi rimachin.
6. Ollama llapanmanta tapukuykunata kutichin, Internetman willayta mana kachaspa.
7. Nube IA-taqa sut’i tapukuykuna, ñawpaq IA munaspa, chayllapi llamk’achin.

## Ñawpaqman ruwasqa ruraykuna

- K’anchay, enchufe, wayra llamk’achiy, cortina, huk kaqkunata rimaywan kamachiy.
- Achka simipi suti/alias.
- Rimaywan temporizador.
- Kay llaktapi para, wayra willaykunata tapuy.
- Takiyta uyarichiy, kamachiy.
- Ollama modelowan sapaq fallback.
- Runata rimayninwan riqsiy.
- Unay pacha contexto yuyay.
- Munaspa nube IA modeloman apachiy.
- Copias de seguridad, rendimiento qhawariy.

## Ruray kamachikuna

- Wasi kamachiykuna Internet mana kaptinpas llamk’ananku.
- Local intenciones procesador LLM-kunamanta ñawpaq kanan.
- Audio willaykuna, pakasqa rimaykuna ñawpaqta local llamk’achisqa kanan.
- Nube modelokunaqa sut’i utaq sasa tapukuykunapaqlla llamk’achisqa kananku; usuario asistente configuración ruwaspa sut’ita mañakuspan.
- Sistema ruphayta, latency nisqata sapa kuti carga kaptinpas allin, sayasqa waqaychanan.

## Proyectopa kashqan

Proyectoqa llamk’achina backlog hinam churakun. Sapa usuario historia tukuchisqa kasqanman hina, específico configuración, automatización, despliegue script yapasqa kanqa.
