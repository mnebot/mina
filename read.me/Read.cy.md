**Cymraeg** · [Nôl i’r dewis iaith](../Read.md)

# Cynorthwyydd cartref aml-ieithog

Mae’r prosiect hwn yn disgrifio gosod ecosystem gynorthwyydd lleferydd aml-ieithog yn lleol ar Raspberry Pi.

## Tarddiad yr enw Mina

Mae gwreiddyn Almaenaidd hynafol i **Mina** yn *minna*, sy’n golygu “cof”, “hoffter” neu “atgof”. Mae’r enw hefyd i’w weld mewn ieithoedd eraill: ym Mhersieg, mae *mīnā*’n gysylltiedig â “golau” neu “wydr glas”, ac yn Japaneaidd, mae *mina* yn golygu “pawb” neu “pawb gyda’i gilydd”.

Mae’r dehongliadau hyn yn symboli **cof a cymuned a rennir**, gwerthoedd sy’n cyd-fynd â chynorthwyydd sy’n cwmnio ac yn cefnogi bywyd dyddiol y cartref.

O ran sain, mae Mina yn enw meddal ond eglur, gyda’r ynganiad sillafog `Mi-na` a thebygolrwydd isel o’i gamgymryd â geiriau cyffredin o fewn cartrefi.

## Amcan

Creu system cartref breifat, ddibynadwy a chyflym sy’n galluogi rheoli dyfeisiau’r cartref trwy orchmynion llais heb ddibyniaeth orfodol ar wasanaethau cwmwl.

Mae’r bensaernïaeth yn cyfuno:

- Prosesu lleol ar gyfer gorchmynion cartref a phreifatrwydd.
- Deallusrwydd lleol gydag Ollama ar gyfer cwestiynau cyffredinol.
- Modelau cwmwl ar gyfer ymholiadau cymhleth a gwybodaeth ddiweddar.

## Caledwedd

- Raspberry Pi 5 gydag 8 GB o RAM a argymhellir. Cydnawsedd cyfyngedig hyd at Raspberry Pi 3B+.
- D disg NVMe heb ddefnyddio cerdyn SD. Cydnawsedd cyfyngedig â cherdyn SD.
- Meicroffon a siaradwr USB dwygyfeiriadol.
- Dyfeisiau cartref sy’n cyd-fynd â Zigbee, Matter, Philips Hue neu Wi-Fi lleol.
- Oeriad llawn i osgoi llwybredd thermol.

## Pensaernïaeth

1. Mae Home Assistant OS yn rheoli’r dyfeisiau a’r awtomeiddio.
2. Mae openWakeWord yn canfod y gair gweithredu’n lleol.
3. Mae Whisper yn trawsgrifio gorchmynion yn yr iaith weithredol trwy Wyoming.
4. Mae’r prosesydd bwriad yn gweithredu gorchmynion cartref yn lleol.
5. Mae Piper yn syntheseiddio ymatebion yn Gymraeg.
6. Mae Ollama yn datrys cwestiynau cyffredinol heb anfon data i’r Rhyngrwyd.
7. Dim ond ymholiadau eglur sy’n gofyn am AI uwch a gaiff yr AI cwmwl.

## Nodweddion arfaethedig

- Rheolaeth lais ar oleuadau, socedi, aerdymheru, llenni a dyfeisiau eraill.
- Aliasau aml-ieithog.
- Amseryddion a reolir â llais.
- Ymholiadau tywydd lleol.
- Chwarae a rheoli cerddoriaeth.
- Dewis preifat i fodel Ollama.
- Adnabod person drwy’r lais.
- Cof cyd-destun tymor hir.
- Ailgyfeirio dewisol i fodel AI cwmwl.
- Copïau wrth gefn a monitro perfformiad.

## Egwyddorion dylunio

- Rhaid i orchmynion cartref weithio heb gysylltiad Rhyngrwyd.
- Mae blaenoriaeth i’r prosesydd bwriad lleol dros LLMau.
- Dylai data sain a sgyrsiau preifat gael eu prosesu’n lleol lle bo modd.
- Defnyddir modelau cwmwl ond ar gyfer ymholiadau eglur neu gymhleth, a dim ond os yw’r defnyddiwr wedi gofyn amdanynt yn eglur wrth ffurfweddu’r cynorthwyydd.
- Rhaid i’r system gynnal tymhereddau a hwyrni sefydlog dan lwyth parhaus.

## Statws y prosiect

Diffiniwyd y prosiect fel rhestr ôl-stoc swyddogaethol. Bydd angen ychwanegu ffurfweddau penodol, awtomeiddio a sgriptiau gosod wrth i’r straeon defnyddwyr gael eu cwblhau.
