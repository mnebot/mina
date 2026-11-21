**Euskara · [Itzuli hizkuntza-hautaketara](../Read.md)**

# Etxe adimendunerako laguntzaile eleaniztuna

**Hizkuntza:** Euskara

**Irakurri hemen:** [Katalana](Read.ca.md) · [Ingelesa](Read.en.md) · [Gaztelania](Read.es.md) · [Frantsesa](Read.fr.md) · [Alemana](Read.de.md) · [Italiera](Read.it.md) · [Portugesa](Read.pt.md) · [Nederlandera](Read.nl.md)

Proiektu honek Raspberry Pi batean tokiko domotika-ekosistema bat hedatzea deskribatzen du, hizkuntza anitzeko ahots-laguntzaile batekin.

## Mina izenaren jatorria

**Mina** izenak antzinako erro germaniarra du, *minna*, eta «oroimena», «maitasuna» edo «oroitzapena» esan nahi du. Beste hizkuntza batzuetan ere ageri da: persieraz, *mīnā* «argiarekin» edo «beira urdinarekin» lotzen da; japonieraz, berriz, *mina* hitzak «denak» edo «denok batera» esan nahi du.

Interpretazio horiek **oroimen partekatua eta komunitatea** sinbolizatzen dituzte; etxeko eguneroko bizitzan lagundu eta babesten duen laguntzailearekin bat datozen balioak dira.

Soinuari dagokionez, Mina izen leuna baina argia da; `Mi-na` silabaka ahoskatzen da, eta etxeko ingurunean ohikoak diren hitzekin nahasteko aukera txikia du.

## Helburua

Etxeko gailuak ahots-komandoen bidez kontrolatzeko aukera emango duen domotika-sistema pribatu, fidagarri eta azkar bat sortzea, hodeiko zerbitzuekiko nahitaezko mendekotasunik gabe.

Arkitekturak honako hauek uztartzen ditu:

- Tokiko prozesamendua domotika-komandoetarako eta pribatutasunerako.
- Tokiko adimena Ollamarekin, galdera orokorretarako.
- Hodeiko ereduak, kontsulta konplexuetarako eta informazio eguneraturako.

## Hardwarea

- Raspberry Pi 5, 8 GB RAM gomendatuta. Bateragarritasun mugatua Raspberry Pi 3B+ arte.
- NVMe SSD diskoa, SD txartelik erabili gabe. Bateragarritasun mugatua SD txartelarekin.
- Noranzko biko USB mikrofonoa eta bozgorailua.
- Zigbee, Matter, Philips Hue edo tokiko Wi-Fi-rekin bateragarriak diren domotika-gailuak.
- Hozte aktiboa, throttling termikoa saihesteko.

## Arkitektura

1. Home Assistant OSek gailuak eta automatizazioak kudeatzen ditu.
2. openWakeWord-ek aktibazio-hitza tokian detektatzen du.
3. Whisperrek komandoak hizkuntza aktiboan transkribatzen ditu Wyoming bidez.
4. Asmo-prozesadoreak domotika-komandoak tokian exekutatzen ditu.
5. Piperrek erantzunak katalanez sintetizatzen ditu.
6. Ollamak galdera orokorrei erantzuten die, daturik Internetera bidali gabe.
7. Hodeiko IAk IA aurreratua behar duten kontsulta esplizituak baino ez ditu jasotzen.

## Aurreikusitako funtzionalitateak

- Argien, entxufeen, klimatizazioaren, pertsianen eta beste gailu batzuen ahots bidezko kontrola.
- Hizkuntza anitzeko ezizenak.
- Ahots bidez kudeatutako tenporizadoreak.
- Tokiko eguraldi-kontsulta.
- Musika erreproduzitzea eta kontrolatzea.
- Ollama eredu batera itzultzeko aukera pribatua.
- Pertsona ahotsaren bidez ezagutzea.
- Epe luzeko testuinguru-memoria.
- Aukerako bideratzea hodeiko IA-eredu batera.
- Segurtasun-kopiak eta errendimenduaren monitorizazioa.

## Diseinu-printzipioak

- Domotika-komandoek Interneteko konexiorik gabe funtzionatu behar dute.
- Tokiko asmo-prozesadoreak LLMek baino lehentasun handiagoa du.
- Audio-datuak eta elkarrizketa pribatuak, ahal dela, tokian prozesatzen dira.
- Hodeiko ereduak berariaz eskatutako edo konplexuak diren kontsultetarako soilik erabiltzen dira, eta erabiltzaileak laguntzailea konfiguratzean berariaz eskatu badu bakarrik.
- Sistemak tenperatura eta latentzia egonkorrak mantendu behar ditu etengabeko kargapean.

## Proiektuaren egoera

Proiektua funtzionalitateen backlog gisa zehaztuta dago. Konfigurazio espezifikoak, automatizazioak eta hedapen-scriptak gehituko dira erabiltzaile-istorioak osatu ahala.
