**Tok Pisin · [Go bek long makim tok](../Read.md)**
# Planti tokples smart haus helpa

**Tokples:** Tok Pisin

**Ritim long:** [Tok Pisin](Read.tpi.md) · [English](Read.en.md) · [Català](Read.ca.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Dispela projek i stori long pasin bilong setimap wanpela lokal smart haus sistem long wanpela Raspberry Pi, wantaim voice helpa bilong planti tokples.

## Mina nem i kamap olsem wanem

**Mina** i gat as bilong en long olpela German tok *minna*, mining bilong en «tingting bek», «laikim» o «samting yu tingim». Dispela nem i stap tu long ol narapela tokples: long Persian, *mīnā* i poroman wantaim «lait» o «blu glas»; long Japanese, *mina* i mining «olgeta manmeri» o «olgeta wantaim».

Ol dispela mining i makim **tingting bilong yumi wantaim na komuniti**, ol samting i stret long wanpela helpa i stap wantaim na helpim laip bilong olgeta de long haus.

Nem Mina i gat isi tasol klia nek: ol i kolim long tupela silabel, `Mi-na`, na i no gat bikpela sans long paul wantaim ol tok ol i save yusim long haus.

## As tingting

Wokim wanpela smart haus sistem i gat pasin hait, i save wok gut na i hariap, bilong kontrolim ol haus samting long voice oda na i no mas dipen olgeta long ol cloud sevis.

Dispela arkitekja i bungim:

- Lokal proses bilong ol smart haus oda na pasin hait.
- Lokal save wantaim Ollama bilong ol askim nating.
- Ol cloud model bilong ol askim i hat na niupela infomesen.

## Kompiuta samting

- Raspberry Pi 5 wantaim 8 GB RAM i gutpela. Kompatibiliti i sot inap long Raspberry Pi 3B+.
- NVMe SSD disk, i no yusim SD kad. Kompatibiliti wantaim SD kad i sot.
- USB microphone na speaker i wok long tupela sait.
- Ol smart haus samting i kompatibel wantaim Zigbee, Matter, Philips Hue o lokal Wi-Fi.
- Aktif koling bilong pasim hat tumas na performance i no ken go daun.

## Arkitekja

1. Home Assistant OS i lukautim ol samting na automation.
2. openWakeWord i painim wake word long lokal.
3. Whisper i raitim ol oda long dispela tokples i stap, long rot bilong Wyoming.
4. Intent processor i mekim ol smart haus oda long lokal.
5. Piper i toktokim ol bekim long Tokples Katalan.
6. Ollama i bekim ol askim nating na i no salim data i go long Intenet.
7. Cloud AI i kisim ol askim man i askim klia tasol, taim ol i nidim advanced AI.

## Ol samting ol bai planim

- Yusim voice bilong kontrolim lait, outlet, klima, blind na ol narapela samting.
- Ol alias long planti tokples.
- Timer i wok long voice oda.
- Askim long lokal weda.
- Pilai na kontrolim musik.
- Pasin hait fallback long wanpela Ollama model.
- Luksave long man long nek bilong en.
- Longtaim memory bilong konteks.
- Salim askim long wanpela cloud AI model sapos man i laik.
- Backup na lukautim performance.

## Ol prinsip bilong design

- Ol smart haus oda i mas wok maski Intenet i no stap.
- Lokal intent processor i gat namba wan prioriti winim ol LLM.
- Audio data na privat toktok i mas wok long lokal pastaim.
- Ol cloud model i bilong ol askim man i askim klia o ol askim i hat, na sapos man i bin makim dispela taim em i setimap helpa.
- Sistem i mas holim gutpela temperature na latency taim em i wok i stap.

## Projek status

Ol i makim dispela projek olsem wanpela functional backlog. Ol spesel configuration, automation na deployment script bai kamap taim ol user story i pinis.
