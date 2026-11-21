**Lietuvių** · [Grįžti į kalbos pasirinkimą](../readme.md)

# Daugiakalbis namų asistentas

Šiame projekte aprašomas daugiakalbė namų automatizavimo ekosistema su balso asistentu, diegiama vietoje „Raspberry Pi“.

## Vardo Mina kilmė

**Mina** turi seną germanų šaknį *minna*, reiškiančią „atmintį“, „priešiškumą“ arba „prisiminimą“. Žodis sutinkamas ir kitose kalbose: persų kalboje *mīnā* siejamas su „šviesa“ arba „mėlynu stiklu“, japonų kalboje *mina* reiškia „visi“ arba „visi kartu“.

Šios reikšmės simbolizuoja **bendrą atmintį ir bendruomenę** — vertybes, tinkamas asistentui, lydinčiam ir palaikančiam kasdienį namų gyvenimą.

Pagal garsą Mina yra švelnus, bet aiškus vardas, tariamas skiemenimis `Mi-na`; mažai tikėtina, kad jis bus painiojamas su įprastais žodžiais namų aplinkoje.

## Tikslas

Sukurti privačią, patikimą ir greitą namų sistemą, kuria įrenginiai valdomi balso komandomis, nepriklausant nuo debesų paslaugų.

Architektūra jungia:

- Vietinį buities komandų apdorojimą ir privatumą.
- Vietinį intelektą su Ollama bendriems klausimams.
- Debesų modelius sudėtingoms užklausoms ir naujoms informacijoms.

## Aparatinė įranga

- Rekomenduojama „Raspberry Pi 5“ su 8 GB RAM. Ribotas suderinamumas iki „Raspberry Pi 3B+“.
- NVMe SSD diskas be SD kortelės naudojimo. Ribotas suderinamumas su SD kortele.
- Dvipusis USB mikrofonas ir garsiakalbis.
- Zigbee, Matter, Philips Hue arba vietinio Wi-Fi palaikomi buities įrenginiai.
- Aktyvus aušinimas nuo terminio sulėtinimo.

## Architektūra

1. „Home Assistant OS“ valdo įrenginius ir automatizacijas.
2. openWakeWord vietoje aptinka aktyvinimo žodį.
3. „Whisper“ per „Wyoming“ transkribuoja komandas aktyvia kalba.
4. Užduočių apdorojimo modulis vietoje vykdo buities komandas.
5. „Piper“ sintezuoja atsakymus lietuvių kalba.
6. „Ollama“ sprendžia bendrus klausimus, nesiųsdama duomenų į internetą.
7. Debesų DI gauna tik aiškias užklausas, reikalaujančias pažangesnio DI.

## Planuojamos funkcijos

- Balso valdomos lempos, lizdai, klimatas, žaliuzės ir kiti įrenginiai.
- Daugiakalbiai slapyvardžiai.
- Balso valdomi laikmačiai.
- Vietiniai orų užklausimai.
- Muzikos atkūrimas ir valdymas.
- Privatus atsarginis sprendimas į Ollama modelį.
- Asmens atpažinimas balsu.
- Ilgalaikė konteksto atmintis.
- Pasirenkamas nukreipimas į debesų DI modelį.
- Atsarginės kopijos ir našumo stebėjimas.

## Projektavimo principai

- Buitinės komandos turi veikti be interneto.
- Vietinis užduočių apdorojimo modulis turi pirmenybę prieš LLM.
- Garso duomenys ir privatūs pokalbiai turėtų būti apdorojami vietoje.
- Debesų modeliai naudojami tik aiškioms ar sudėtingoms užklausoms ir tik jei naudotojas tai aiškiai nurodė konfigūruodamas asistentą.
- Sistema nuolatinei apkrovai veikiant turi išlaikyti pastovią temperatūrą ir delsą.

## Projekto būsena

Projektas apibrėžtas kaip funkcinis darbų sąrašas. Specifinės konfigūracijos, automatizacijos ir diegimo scenarijai bus pridedami, kai bus įgyvendintos vartotojo istorijos.
