**Íslenska · [Aftur í tungumálaval](../readme.md)**

# Fjöltyngdur aðstoðarmaður fyrir snjallheimili

**Tungumál:** íslenska

**Lesa á:** [Katalónsku](Read.ca.md) · [Ensku](Read.en.md) · [Spænsku](Read.es.md) · [Frönsku](Read.fr.md) · [Þýsku](Read.de.md) · [Ítölsku](Read.it.md) · [Portúgölsku](Read.pt.md) · [Hollensku](Read.nl.md)

Verkefnið lýsir uppsetningu staðbundins vistkerfis sjálfvirknivæðingar heimilis á Raspberry Pi með fjöltyngdum raddaðstoðarmanni.

## Uppruni nafnsins Mina

**Mina** á rætur að rekja til forngermanska orðsins *minna*, sem merkir „minni“, „ástúð“ eða „minning“. Nafnið kemur einnig fyrir í öðrum tungumálum: á persnesku tengist *mīnā* „ljósi“ eða „bláu gleri“, en á japönsku merkir *mina* „allir“ eða „allir saman“.

Þessar túlkanir tákna **sameiginlegt minni og samfélag**, gildi sem eiga vel við aðstoðarmann sem fylgir og styður daglegt líf á heimilinu.

Hljómrænt er Mina mjúkt en skýrt nafn, borið fram í atkvæðum `Mi-na`, og litlar líkur eru á að því verði ruglað saman við algeng orð á heimilinu.

## Markmið

Að skapa einkvæmt, áreiðanlegt og hraðvirkt sjálfvirknikerfi fyrir heimilið sem gerir kleift að stjórna heimilistækjum með raddskipunum án þess að vera háð skýjaþjónustum.

Byggingin sameinar:

- Staðbundna úrvinnslu fyrir skipanir í sjálfvirkni heimilisins og persónuvernd.
- Staðbundna gervigreind með Ollama fyrir almennar spurningar.
- Skýjalíkön fyrir flóknar fyrirspurnir og nýjustu upplýsingar.

## Vélbúnaður

- Raspberry Pi 5 með ráðlögðu 8 GB vinnsluminni. Takmörkuð samhæfni niður í Raspberry Pi 3B+.
- NVMe SSD-diskur án SD-korts. Takmörkuð samhæfni við SD-kort.
- Tvíátta USB-hljóðnemi og hátalari.
- Tæki fyrir sjálfvirkni heimilisins sem samrýmast Zigbee, Matter, Philips Hue eða staðbundnu Wi-Fi.
- Virk kæling til að koma í veg fyrir hitatengda skerðingu á afköstum.

## Bygging

1. Home Assistant OS stýrir tækjum og sjálfvirkniverkum.
2. openWakeWord greinir virkjunarorðið staðbundið.
3. Whisper umritar skipanir á virka tungumálinu með Wyoming.
4. Ásetningsvinnslan framkvæmir skipanir sjálfvirkni heimilisins staðbundið.
5. Piper myndar svörin á katalónsku.
6. Ollama svarar almennum spurningum án þess að senda gögn á internetið.
7. Skýjagervigreind fær aðeins skýrar fyrirspurnir sem krefjast háþróaðrar gervigreindar.

## Fyrirhugaðir eiginleikar

- Raddstýring á ljósum, innstungum, loftslagsstýringu, gluggahlerum og öðrum tækjum.
- Samheiti á mörgum tungumálum.
- Tímastillar sem stýrt er með rödd.
- Staðbundin veðurfyrirspurn.
- Spilun og stýring tónlistar.
- Einkvæm varaleið með Ollama-líkani.
- Greining á einstaklingi eftir rödd.
- Langtímaminni fyrir samhengi.
- Valfrjáls framsending til skýjalíkans fyrir gervigreind.
- Afritun og vöktun á afköstum.

## Hönnunarreglur

- Skipanir sjálfvirkni heimilisins verða að virka án nettengingar.
- Staðbundin ásetningsvinnsla hefur forgang fram yfir LLM.
- Hljóðgögn og einkasamtöl eru að jafnaði unnin staðbundið.
- Skýjalíkön eru aðeins notuð fyrir skýrar eða flóknar fyrirspurnir, og aðeins ef notandinn hefur sérstaklega óskað eftir því við uppsetningu aðstoðarmannsins.
- Kerfið þarf að halda hitastigi og töfum stöðugum við stöðugt álag.

## Staða verkefnisins

Verkefnið er skilgreint sem virkur backlog. Sérstökum stillingum, sjálfvirkniverkum og uppsetningarforskriftum verður bætt við eftir því sem notendasögur klárast.
