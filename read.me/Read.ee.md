**Keel: eesti · [Tagasi keele valiku juurde](../Read.md)**

# Mitmekeelne koduautomaatika assistent

See projekt kirjeldab Raspberry Pi-l töötava kohaliku koduautomaatika ökosüsteemi loomist koos mitmekeelse hääleassistendiga.

## Mina nime päritolu

**Mina** pärineb vana germaani sõnast *minna*, mis tähendab „mälu”, „kiindumust” või „mälestust”. Nimi esineb ka teistes keeltes: pärsia *mīnā* seostub „valguse” või „sinise klaasiga” ning jaapani *mina* tähendab „kõik” või „kõik koos”.

Need tähendused sümboliseerivad **ühist mälu ja kogukonda** – väärtusi, mis sobivad igapäevaelus kodu abistava assistendiga.

Kõlalt on Mina pehme, kuid selge nimi. Seda hääldatakse silpidena `Mi-na` ning koduses keskkonnas on seda vähe tõenäoline segi ajada tavaliste sõnadega.

## Eesmärk

Luua privaatne, töökindel ja kiire koduautomaatikasüsteem, mis võimaldab seadmeid häälkäsklustega juhtida ega sõltu tingimata pilveteenustest.

Arhitektuur ühendab:

- Kohaliku töötluse koduautomaatika käskude täitmiseks ja privaatsuse tagamiseks.
- Kohaliku tehisintellekti, mis kasutab üldküsimustele vastamiseks Ollamat.
- Pilvemudeleid keerukate päringute ja ajakohase teabe jaoks.

## Riistvara

- Raspberry Pi 5, soovitatavalt 8 GB muutmäluga. Piiratud ühilduvus kuni Raspberry Pi 3B+-ni.
- NVMe SSD, ilma SD-kaarti kasutamata. SD-kaardi tugi on piiratud.
- Kahesuunaline USB-mikrofon ja -kõlar.
- Zigbee, Matteri, Philips Hue'i või kohaliku Wi-Fi-ga ühilduvad koduseadmed.
- Aktiivjahutus termilise jõudluse languse vältimiseks.

## Arhitektuur

1. Home Assistant OS haldab seadmeid ja automaatikaid.
2. openWakeWord tuvastab äratussõna kohapeal.
3. Whisper transkribeerib Wyoming-protokolli kaudu käsud aktiivses keeles.
4. Kavatsuste töötleja täidab koduautomaatika käsud kohapeal.
5. Piper sünteesib vastused katalaani keeles.
6. Ollama vastab üldküsimustele ilma andmeid internetti saatmata.
7. Pilve tehisintellekt saab ainult selgesõnalisi päringuid, mille jaoks on vaja täiustatud tehisintellekti.

## Kavandatud funktsioonid

- Hääljuhtimine tuledele, pistikupesadele, kliimaseadmetele, ruloodele ja muudele seadmetele.
- Mitmekeelsed varjunimed.
- Häälega juhitavad taimerid.
- Kohaliku ilma pärimine.
- Muusika esitamine ja juhtimine.
- Privaatne varulahendus Ollama mudeliga.
- Kõneleja tuvastamine hääle järgi.
- Pikaajaline kontekstmälu.
- Valikuline päringute suunamine pilve tehisintellekti mudelile.
- Varukoopiad ja jõudluse jälgimine.

## Projekteerimispõhimõtted

- Koduautomaatika käsud peavad toimima internetiühenduseta.
- Kohalik kavatsuste töötleja on suurte keelemudelite ees eelistatud.
- Heliandmeid ja privaatseid vestlusi töödeldakse võimaluse korral kohapeal.
- Pilvemudeleid kasutatakse ainult selgesõnaliste või keerukate päringute jaoks ning üksnes siis, kui kasutaja on need assistendi seadistamisel selgesõnaliselt lubanud.
- Süsteem peab pideva koormuse juures hoidma temperatuuri ja viivituse stabiilsena.

## Projekti seis

Projekt on määratletud funktsionaalse tööde nimekirjana. Täpsemad seadistused, automaatikad ja juurutusskriptid lisatakse kasutajalugude valmimise käigus.
