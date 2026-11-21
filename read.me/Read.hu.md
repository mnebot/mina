**Magyar · [Vissza a nyelvválasztáshoz](../Read.md)**

# Többnyelvű okosotthon-asszisztens

**Nyelv:** magyar

**Olvasás nyelve:** [Katalán](Read.ca.md) · [Angol](Read.en.md) · [Spanyol](Read.es.md) · [Francia](Read.fr.md) · [Német](Read.de.md) · [Olasz](Read.it.md) · [Portugál](Read.pt.md) · [Holland](Read.nl.md)

Ez a projekt egy helyi otthonautomatizálási ökoszisztéma Raspberry Pi eszközön történő üzembe helyezését írja le, többnyelvű hangasszisztenssel.

## A Mina név eredete

A **Mina** az ófelnémet *minna* szóból ered, jelentése „emlékezet”, „ragaszkodás” vagy „emlék”. Más nyelvekben is előfordul: perzsául a *mīnā* a „fénnyel” vagy a „kék üveggel” áll kapcsolatban, japánul pedig a *mina* jelentése „mindenki” vagy „mindannyian együtt”.

Ezek az értelmezések a **közös emlékezetet és közösséget** jelképezik – olyan értékeket, amelyek összhangban állnak egy, az otthoni mindennapokat kísérő és támogató asszisztenssel.

Hangzását tekintve a Mina lágy, mégis határozott név, szótagolva `Mi-na` ejtéssel; kicsi az esélye, hogy az otthoni környezetben gyakori szavakkal összetévesszék.

## Cél

Olyan privát, megbízható és gyors otthonautomatizálási rendszer létrehozása, amellyel hangutasításokkal vezérelhetők az otthoni eszközök anélkül, hogy feltétlenül felhőszolgáltatásokra kellene támaszkodni.

Az architektúra elemei:

- Helyi feldolgozás az otthonautomatizálási parancsokhoz és az adatvédelemhez.
- Helyi intelligencia Ollama használatával az általános kérdésekhez.
- Felhőmodellek az összetett lekérdezésekhez és a naprakész információkhoz.

## Hardver

- Raspberry Pi 5, ajánlott 8 GB RAM-mal. Korlátozott kompatibilitás egészen a Raspberry Pi 3B+ modellig.
- NVMe SSD meghajtó SD-kártya használata nélkül. Korlátozott kompatibilitás SD-kártyával.
- Kétirányú USB-mikrofon és -hangszóró.
- Zigbee, Matter, Philips Hue vagy helyi Wi-Fi technológiával kompatibilis otthonautomatizálási eszközök.
- Aktív hűtés a hő miatti teljesítménycsökkenés megelőzésére.

## Architektúra

1. A Home Assistant OS kezeli az eszközöket és az automatizálásokat.
2. Az openWakeWord helyben érzékeli az ébresztőszót.
3. A Whisper a Wyoming segítségével átírja a parancsokat az aktív nyelven.
4. A szándékfeldolgozó helyben hajtja végre az otthonautomatizálási parancsokat.
5. A Piper katalánul állítja elő a válaszokat.
6. Az Ollama úgy válaszol az általános kérdésekre, hogy nem küld adatokat az internetre.
7. A felhőalapú MI csak a fejlett MI-t igénylő, kifejezett lekérdezéseket kapja meg.

## Tervezett funkciók

- A világítás, konnektorok, légkondicionálás, redőnyök és más eszközök hangvezérlése.
- Többnyelvű aliasok.
- Hanggal vezérelt időzítők.
- Helyi időjárás-lekérdezés.
- Zenelejátszás és -vezérlés.
- Privát tartalék megoldás egy Ollama-modellel.
- A személy felismerése hang alapján.
- Hosszú távú kontextusmemória.
- Opcionális továbbítás egy felhőalapú MI-modellhez.
- Biztonsági mentések és teljesítményfigyelés.

## Tervezési alapelvek

- Az otthonautomatizálási parancsoknak internetkapcsolat nélkül is működniük kell.
- A helyi szándékfeldolgozó elsőbbséget élvez az LLM-ekkel szemben.
- A hangadatokat és a privát beszélgetéseket lehetőség szerint helyben dolgozzuk fel.
- Felhőmodelleket csak kifejezett vagy összetett lekérdezésekhez használunk, és csak akkor, ha a felhasználó az asszisztens beállításakor ezt kifejezetten kérte.
- A rendszernek folyamatos terhelés mellett is stabil hőmérsékletet és késleltetést kell fenntartania.

## A projekt állapota

A projekt funkcionális backlogként van meghatározva. A konkrét konfigurációk, automatizálások és telepítési szkriptek a felhasználói történetek elkészültével kerülnek be.
