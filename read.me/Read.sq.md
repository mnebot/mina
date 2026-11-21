**Shqip · [Kthehu te zgjedhja e gjuhës](../readme.md)**

# Asistenti shumëgjuhësh për shtëpinë inteligjente

**Gjuha:** Shqip

**Lexoje në:** [Katalanisht](Read.ca.md) · [Anglisht](Read.en.md) · [Spanjisht](Read.es.md) · [Frëngjisht](Read.fr.md) · [Gjermanisht](Read.de.md) · [Italisht](Read.it.md) · [Portugalisht](Read.pt.md) · [Holandisht](Read.nl.md)

Ky projekt përshkruan vendosjen e një ekosistemi lokal të automatizimit të shtëpisë në një Raspberry Pi, me një asistent zanor shumëgjuhësh.

## Origjina e emrit Mina

**Mina** e ka origjinën në rrënjën e vjetër gjermanike *minna*, që do të thotë «kujtesë», «dashuri» ose «përkujtim». Emri gjendet edhe në gjuhë të tjera: në persisht, *mīnā* lidhet me «dritën» ose «xhamin blu», ndërsa në japonisht, *mina* do të thotë «të gjithë» ose «të gjithë së bashku».

Këto kuptime simbolizojnë **kujtesën e përbashkët dhe komunitetin**, vlera që përputhen me një asistent që shoqëron dhe mbështet jetën e përditshme në shtëpi.

Nga ana tingullore, Mina është emër i butë, por i qartë, me shqiptimin rrokjesor `Mi-na` dhe me pak gjasa të ngatërrohet me fjalë të zakonshme në mjedisin shtëpiak.

## Qëllimi

Të krijohet një sistem privat, i besueshëm dhe i shpejtë i automatizimit të shtëpisë, që lejon kontrollin e pajisjeve shtëpiake me komanda zanore pa varësi të detyrueshme nga shërbimet në renë kompjuterike.

Arkitektura ndërthur:

- Përpunim lokal për komandat e automatizimit të shtëpisë dhe privatësinë.
- Inteligjencë lokale me Ollama për pyetje të përgjithshme.
- Modele në re për pyetje komplekse dhe informacione të përditësuara.

## Pajisjet

- Raspberry Pi 5 me 8 GB RAM të rekomanduara. Përputhshmëri e kufizuar deri te Raspberry Pi 3B+.
- Disk SSD NVMe, pa përdorur kartë SD. Përputhshmëri e kufizuar me kartë SD.
- Mikrofon dhe altoparlant USB dydrejtimësh.
- Pajisje të automatizimit të shtëpisë të përputhshme me Zigbee, Matter, Philips Hue ose Wi-Fi lokal.
- Ftohje aktive për të shmangur uljen e performancës nga mbinxehja.

## Arkitektura

1. Home Assistant OS menaxhon pajisjet dhe automatizimet.
2. openWakeWord zbulon lokalisht fjalën e aktivizimit.
3. Whisper transkripton komandat në gjuhën aktive përmes Wyoming.
4. Përpunuesi i qëllimeve zbaton lokalisht komandat e automatizimit të shtëpisë.
5. Piper sintetizon përgjigjet në katalanisht.
6. Ollama u përgjigjet pyetjeve të përgjithshme pa dërguar të dhëna në internet.
7. IA-ja në re merr vetëm pyetje të shprehura qartë që kërkojnë IA të përparuar.

## Funksionalitetet e planifikuara

- Kontroll zanor i dritave, prizave, klimës, grilave dhe pajisjeve të tjera.
- Emërtime alternative në shumë gjuhë.
- Kohëmatës të menaxhuar me zë.
- Informacion lokal për motin.
- Riprodhim dhe kontroll i muzikës.
- Kthim privat te një model Ollama.
- Njohja e personit nga zëri.
- Kujtesë kontekstuale afatgjatë.
- Kalim opsional te një model IA-je në re.
- Kopje rezervë dhe monitorim i performancës.

## Parimet e projektimit

- Komandat e automatizimit të shtëpisë duhet të funksionojnë pa lidhje interneti.
- Përpunuesi lokal i qëllimeve ka përparësi ndaj LLM-ve.
- Të dhënat audio dhe bisedat private përpunohen mundësisht lokalisht.
- Modelet në re përdoren vetëm për pyetje të shprehura qartë ose komplekse, dhe vetëm nëse përdoruesi e ka kërkuar shprehimisht këtë gjatë konfigurimit të asistentit.
- Sistemi duhet të ruajë temperatura dhe vonesa të qëndrueshme nën ngarkesë të vazhdueshme.

## Gjendja e projektit

Projekti është përcaktuar si një listë pune funksionale. Konfigurimet specifike, automatizimet dhe skriptet e vendosjes do të shtohen ndërsa përfundohen historitë e përdoruesve.
