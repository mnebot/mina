**Suomi · [Takaisin kielen valintaan](../Read.md)**

# Monikielinen älykodin avustaja

**Kieli:** suomi

**Lue kielellä:** [Katalaani](Read.ca.md) · [Englanti](Read.en.md) · [Espanja](Read.es.md) · [Ranska](Read.fr.md) · [Saksa](Read.de.md) · [Italia](Read.it.md) · [Portugali](Read.pt.md) · [Hollanti](Read.nl.md)

Tässä projektissa kuvataan paikallisen kodinautomaatioekosysteemin käyttöönotto Raspberry Pi -laitteella monikielisen ääniavustajan kanssa.

## Mina-nimen alkuperä

**Mina** juontuu muinaisgermaanisesta juuresta *minna*, joka tarkoittaa ”muistia”, ”kiintymystä” tai ”muistoa”. Nimi esiintyy myös muissa kielissä: persiassa *mīnā* liittyy ”valoon” tai ”siniseen lasiin”, ja japanissa *mina* tarkoittaa ”kaikkia” tai ”kaikkia yhdessä”.

Nämä tulkinnat symboloivat **yhteistä muistia ja yhteisöllisyyttä** – arvoja, jotka sopivat avustajalle, joka kulkee kodin arjessa mukana ja tukee sitä.

Äänteellisesti Mina on pehmeä mutta selkeä nimi, joka lausutaan tavuittain `Mi-na`. Se sekoittuu vain harvoin kodin ympäristössä tavallisiin sanoihin.

## Tavoite

Luoda yksityinen, luotettava ja nopea kodinautomaatiojärjestelmä, jonka avulla kodin laitteita voidaan ohjata äänikomennoilla ilman pakollista riippuvuutta pilvipalveluista.

Arkkitehtuuri yhdistää:

- Paikallisen käsittelyn kodinautomaation komentoja ja tietosuojaa varten.
- Paikallisen älykkyyden Ollaman avulla yleisiin kysymyksiin.
- Pilvimallit monimutkaisiin kyselyihin ja ajantasaiseen tietoon.

## Laitteisto

- Raspberry Pi 5, jossa suositellaan olevan 8 Gt RAM-muistia. Rajoitettu yhteensopivuus Raspberry Pi 3B+:aan asti.
- NVMe SSD -levy ilman SD-kortin käyttöä. Rajoitettu yhteensopivuus SD-kortin kanssa.
- Kaksisuuntainen USB-mikrofoni ja -kaiutin.
- Zigbee-, Matter-, Philips Hue- tai paikallisen Wi-Fi-verkon kanssa yhteensopivat kodinautomaatiolaitteet.
- Aktiivinen jäähdytys lämpökuristuksen ehkäisemiseksi.

## Arkkitehtuuri

1. Home Assistant OS hallitsee laitteita ja automaatioita.
2. openWakeWord tunnistaa herätesanan paikallisesti.
3. Whisper litteroi komennot aktiivisella kielellä Wyomingin kautta.
4. Tarkoitteiden käsittelijä suorittaa kodinautomaation komennot paikallisesti.
5. Piper tuottaa vastaukset katalaaniksi.
6. Ollama vastaa yleisiin kysymyksiin lähettämättä tietoja internetiin.
7. Pilvi-tekoälylle välitetään vain nimenomaiset kyselyt, jotka edellyttävät kehittynyttä tekoälyä.

## Suunnitellut ominaisuudet

- Valojen, pistorasioiden, ilmastoinnin, kaihtimien ja muiden laitteiden ääniohjaus.
- Monikieliset aliakset.
- Äänellä hallittavat ajastimet.
- Paikallinen säätietojen kysely.
- Musiikin toisto ja hallinta.
- Yksityinen vararatkaisu Ollama-mallilla.
- Henkilön tunnistaminen äänen perusteella.
- Pitkäaikainen kontekstimuisti.
- Valinnainen ohjaus pilvipohjaiseen tekoälymalliin.
- Varmuuskopiot ja suorituskyvyn seuranta.

## Suunnitteluperiaatteet

- Kodinautomaation komentojen on toimittava ilman internetyhteyttä.
- Paikallinen tarkoitteiden käsittelijä ohittaa LLM-mallit.
- Äänidata ja yksityiset keskustelut käsitellään ensisijaisesti paikallisesti.
- Pilvimalleja käytetään vain nimenomaisiin tai monimutkaisiin kyselyihin ja vain, jos käyttäjä on erikseen pyytänyt sitä avustajan määrityksen yhteydessä.
- Järjestelmän on pidettävä lämpötilat ja viiveet vakaina jatkuvassa kuormituksessa.

## Projektin tila

Projekti on määritelty toiminnalliseksi backlogiksi. Tarkat määritykset, automaatiot ja käyttöönoton komentosarjat lisätään käyttäjätarinoiden valmistuessa.
