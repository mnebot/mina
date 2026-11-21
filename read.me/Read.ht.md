**Kreyòl ayisyen · [Retounen chwazi lang](../Read.md)**
# Asistan kay entelijan plizyè lang

**Lang:** Kreyòl ayisyen

**Li nan:** [Kreyòl ayisyen](Read.ht.md) · [English](Read.en.md) · [Català](Read.ca.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Pwojè sa a dekri kijan pou deplwaye yon ekosistèm kay entelijan lokal sou yon Raspberry Pi, ak yon asistan vwa ki pale plizyè lang.

## Orijin non Mina

**Mina** soti nan ansyen rasin jèmanik *minna*, ki vle di «memwa», «afeksyon» oswa «souvni». Non an parèt nan lòt lang tou: an pès, *mīnā* gen rapò ak «limyè» oswa «vè ble»; an japonè, *mina* vle di «tout moun» oswa «tout ansanm».

Entèpretasyon sa yo senbolize **memwa nou pataje ak kominote**, valè ki mache ak yon asistan ki akonpaye epi ede lavi chak jou nan kay la.

Non Mina a dous men li klè lè w tande l: yo pwononse l an de silab, `Mi-na`, epi li pa fasil pou konfonn li ak mo moun itilize souvan lakay.

## Objektif

Kreye yon sistèm kay entelijan ki prive, fyab epi rapid, pou kontwole aparèy lakay ak kòmand vwa san depann nesesèman de sèvis nan nwaj la.

Achitekti a konbine:

- Pwosesis lokal pou kòmand kay entelijan ak vi prive.
- Entèlijans lokal ak Ollama pou kesyon jeneral.
- Modèl nan nwaj la pou kesyon konplèks ak enfòmasyon ki ajou.

## Materyèl

- Raspberry Pi 5 ak 8 GB RAM rekòmande. Konpatibilite limite jiska Raspberry Pi 3B+.
- Disk SSD NVMe san kat SD. Konpatibilite limite ak kat SD.
- Mikwofòn ak loudspeaker USB ki mache nan toude sans.
- Aparèy kay entelijan ki konpatib ak Zigbee, Matter, Philips Hue oswa Wi-Fi lokal.
- Refwadisman aktif pou anpeche twòp chalè diminye pèfòmans.

## Achitekti

1. Home Assistant OS jere aparèy ak automatisation yo.
2. openWakeWord detekte mo reveye a lokalman.
3. Whisper transkri kòmand yo nan lang aktif la atravè Wyoming.
4. Pwosesè entansyon an egzekite kòmand kay entelijan yo lokalman.
5. Piper fè repons yo pale an katalan.
6. Ollama reponn kesyon jeneral san li pa voye done sou Entènèt.
7. AI nan nwaj la resevwa sèlman kesyon eksplisit ki bezwen AI avanse.

## Fonksyon ki planifye

- Kontwole limyè, priz, èkondisyone, pèsyèn ak lòt aparèy ak vwa.
- Alyas nan plizyè lang.
- Minutri ki mache ak kòmand vwa.
- Chèche enfòmasyon lokal sou meteyo.
- Jwe mizik epi kontwole lekti mizik.
- Yon solisyon prive ak yon modèl Ollama kòm sekou.
- Rekonèt moun dapre vwa yo.
- Memwa kontèks sou yon peryòd long.
- Voye kesyon bay yon modèl AI nan nwaj la si itilizatè a vle.
- Sovgad ak siveyans pèfòmans.

## Prensip konsepsyon

- Kòmand kay entelijan yo dwe mache san koneksyon Entènèt.
- Pwosesè entansyon lokal la gen priyorite sou LLM yo.
- Done odyo ak konvèsasyon prive yo dwe trete lokalman an premye.
- Modèl nan nwaj la sèvi sèlman pou kesyon itilizatè mande klèman oswa kesyon konplèks, epi sèlman si itilizatè a te chwazi sa klèman pandan konfigirasyon asistan an.
- Sistèm nan dwe kenbe tanperati ak reta repons yo estab menm lè l ap travay san rete.

## Eta pwojè a

Pwojè a defini kòm yon backlog fonksyonèl. N ap ajoute konfigirasyon espesyal yo, automatisation yo ak scripts deplwaman yo pandan n ap fini istwa itilizatè yo.
