**Latviešu** · [Atpakaļ uz valodas izvēli](../Read.md)

# Daudzvalodu mājas asistents

Šis projekts apraksta vietējas daudzvalodu balss asistenta ekosistēmas izvietošanu Raspberry Pi ierīcē.

## Nosaukuma Mina izcelsme

**Mina** ir sena ģermāņu sakne vārdā *minna*, kas nozīmē “atmiņa”, “piederība” vai “piemiņa”. Tas sastopams arī citās valodās: persiešu valodā *mīnā* saistās ar “gaismu” vai “zilām stikla virsmām”, bet japāņu valodā *mina* nozīmē “visi” vai “visi kopā”.

Šīs nozīmes simbolizē **kopīgu atmiņu un kopienu** — vērtības, kas atbilst asistentam, kas pavada un atbalsta ikdienas mājsaimniecības dzīvi.

Izrunas ziņā Mina ir maigums, bet skaidrs nosaukums, ar zilbju izrunu `Mi-na` un mazu iespējamību sajaukt to ar bieži lietotiem vārdiem mājas vidē.

## Mērķis

Izveidot privātu, uzticamu un ātru mājas sistēmu, kas ļauj vadīt mājsaimniecības ierīces ar balss komandām, bez obligātas atkarības no mākoņpakalpojumiem.

Arhitektūra apvieno:

- Lokālu apstrādi mājas komandām un privātumam.
- Lokālu intelekta risinājumu ar Ollama vispārīgiem jautājumiem.
- Mākoņa modeļus sarežģītiem vaicājumiem un aktuālā informācijai.

## Aparatūra

- Ieteicams Raspberry Pi 5 ar 8 GB RAM. Ierobežota saderība līdz Raspberry Pi 3B+.
- NVMe SSD disks bez SD kartes lietošanas. Ierobežota saderība ar SD karti.
- Divvirzienu USB mikrofons un skaļrunis.
- Mājas ierīces, kas saderīgas ar Zigbee, Matter, Philips Hue vai lokālo Wi-Fi.
- Aktīva dzesēšana termiskā throttling novēršanai.

## Arhitektūra

1. Home Assistant OS pārvalda ierīces un automatizācijas.
2. openWakeWord lokāli nosaka aktivizācijas vārdu.
3. Whisper ar Wyoming pieraksta komandas aktīvajā valodā.
4. Nodomu apstrādātājs lokāli izpilda mājas komandas.
5. Piper sintētiski veido atbildes latviešu valodā.
6. Ollama risina vispārīgus jautājumus, nesūtot datus internetā.
7. Mākoņa AI saņem tikai skaidri norādītus vaicājumus, kuriem nepieciešams uzlabots AI.

## Plānotās funkcijas

- Balss vadība gaismām, kontaktligzdām, klimatam, žalūzijām un citām ierīcēm.
- Daudzvalodu aizstājvārdi.
- Ar balsi pārvaldīti taimeri.
- Lokāls laikapstākļu vaicājums.
- Mūzikas atskaņošana un vadība.
- Privāta aizstāšana ar Ollama modeli.
- Personas atpazīšana pēc balsi.
- Ilgtermiņa konteksta atmiņa.
- Neobligāta pāradresācija uz mākoņa AI modeli.
- Rezerves kopijas un veiktspējas uzraudzība.

## Projektēšanas principi

- Mājas komandām jādarbojas bez interneta savienojuma.
- Lokālais nodomu apstrādātājs ir prioritārāks par LLM.
- Audio dati un privātās sarunas pēc iespējas jāapstrādā lokāli.
- Mākoņa modeļi tiek izmantoti tikai skaidriem vai sarežģītiem vaicājumiem un tikai tad, ja lietotājs to skaidri pieprasījis asistenta konfigurēšanā.
- Sistēmai nepārtrauktas slodzes apstākļos jāsaglabā stabilas temperatūras un aizkaves.

## Projektu statuss

Šis projekts ir definēts kā funkcionāls uzdevumu saraksts. Konkrētās konfigurācijas, automatizācijas un ieviešanas skripti jāpievieno, kad lietotāju stāsti tiek pabeigti.
