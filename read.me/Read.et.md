**Eesti · [Tagasi keelevalikusse](../readme.md)**

# Mitmekeelne targa kodu assistent

**Keel:** eesti

**Loe keeles:** [Katalaani](Read.ca.md) · [Inglise](Read.en.md) · [Hispaania](Read.es.md) · [Prantsuse](Read.fr.md) · [Saksa](Read.de.md) · [Itaalia](Read.it.md) · [Portugali](Read.pt.md) · [Hollandi](Read.nl.md)

Projekt kirjeldab kohaliku koduautomaatika ökosüsteemi juurutamist Raspberry Pi seadmel koos mitmekeelse häälassistendiga.

## Nime Mina päritolu

**Mina** pärineb vana germaani tüvest *minna*, mis tähendab „mälu“, „kiindumust“ või „mälestust“. Nimi esineb ka teistes keeltes: pärsia keeles seostub *mīnā* „valguse“ või „sinise klaasiga“ ning jaapani keeles tähendab *mina* „kõiki“ või „kõiki koos“.

Need tõlgendused sümboliseerivad **ühist mälu ja kogukonda** – väärtusi, mis sobivad assistendile, kes saadab ja toetab igapäevaelu kodus.

Kõlalt on Mina pehme, kuid selge nimi, mida hääldatakse silbitatult `Mi-na`; tõenäosus ajada see koduses keskkonnas segi tavaliste sõnadega on väike.

## Eesmärk

Luua privaatne, töökindel ja kiire koduautomaatika süsteem, mis võimaldab koduseid seadmeid häälkäsklustega juhtida, sõltumata kohustuslikult pilveteenustest.

Arhitektuur ühendab:

- Kohaliku töötluse koduautomaatika käskude ja privaatsuse jaoks.
- Kohaliku tehisintellekti Ollama abil üldiste küsimuste jaoks.
- Pilvemudelid keerukate päringute ja ajakohase teabe jaoks.

## Riistvara

- Raspberry Pi 5, soovitatavalt 8 GB RAM-i. Piiratud ühilduvus kuni Raspberry Pi 3B+ mudelini.
- NVMe SSD-ketas ilma SD-kaarti kasutamata. Piiratud ühilduvus SD-kaardiga.
- Kahesuunaline USB-mikrofon ja kõlar.
- Zigbee, Matteri, Philips Hue või kohaliku Wi-Fi-ga ühilduvad koduautomaatikaseadmed.
- Aktiivjahutus termilise jõudluse piiramise vältimiseks.

## Arhitektuur

1. Home Assistant OS haldab seadmeid ja automaatikaid.
2. openWakeWord tuvastab äratussõna kohapeal.
3. Whisper transkribeerib käsud aktiivses keeles Wyoming-protokolli kaudu.
4. Kavatsuste töötleja täidab koduautomaatika käsud kohapeal.
5. Piper sünteesib vastused katalaani keeles.
6. Ollama vastab üldistele küsimustele andmeid internetti saatmata.
7. Pilvepõhine tehisintellekt saab ainult selgesõnalisi päringuid, mis vajavad täiustatud tehisintellekti.

## Kavandatud funktsioonid

- Valgustite, pistikupesade, kliimaseadmete, ruloode ja muude seadmete hääljuhtimine.
- Mitmekeelsed varjunimed.
- Häälega juhitavad taimerid.
- Kohalik ilmateate päring.
- Muusika esitamine ja juhtimine.
- Privaatne varulahendus Ollama mudeliga.
- Isiku tuvastamine hääle järgi.
- Pikaajaline kontekstimälu.
- Valikuline edastamine pilvepõhisele tehisintellekti mudelile.
- Varukoopiad ja jõudluse jälgimine.

## Kujunduspõhimõtted

- Koduautomaatika käsud peavad toimima internetiühenduseta.
- Kohalik kavatsuste töötleja on LLM-idest tähtsam.
- Heliandmeid ja privaatseid vestlusi töödeldakse eelistatult kohapeal.
- Pilvemudeleid kasutatakse ainult selgesõnaliste või keerukate päringute jaoks ja ainult juhul, kui kasutaja on seda assistendi seadistamisel selgesõnaliselt soovinud.
- Süsteem peab pideva koormuse korral hoidma temperatuuri ja viivitused stabiilsena.

## Projekti seis

Projekt on määratletud funktsionaalse backlog'ina. Konkreetsed seadistused, automaatikad ja juurutusskriptid lisatakse kasutajalugude valmimise käigus.
