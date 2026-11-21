**Føroyskt · [Aftur til málval](../readme.md)**

# Fleirmálsligur snildheima-assistari

**Mál:** Føroyskt

**Les á:** [Katalanskum](Read.ca.md) · [Enskum](Read.en.md) · [Spanskum](Read.es.md) · [Fronskum](Read.fr.md) · [Týskum](Read.de.md) · [Italskum](Read.it.md) · [Portugisiskum](Read.pt.md) · [Niðurlendskum](Read.nl.md)

Hetta verkætlanarskjalið lýsir, hvussu eitt staðbundið heimstýringarskipan verður sett upp á einari Raspberry Pi við einum fleirmálsligum raddassistent.

## Upprunin til navnið Mina

**Mina** hevur røtur í forngermanska orðinum *minna*, sum merkir „minni“, „kærleiki“ ella „minning“. Navnið finst eisini í øðrum málum: á persiskum verður *mīnā* sett í samband við „ljós“ ella „blátt glas“, og á japanskum merkir *mina* „øll“ ella „øll saman“.

Hesar tulkingar ímynda **felags minni og felagsskap**, virði sum samsvara við ein assistent, ið fylgir og stuðlar gerandisdegnum heima.

Í ljóðinum er Mina eitt mjúkt, men greitt navn, við stavilsisframburðinum `Mi-na` og lítlum vanda fyri at verða blandað saman við vanlig orð í heimumhvørvinum.

## Endamál

At skapa eina privata, álítandi og skjóta heimstýringarskipan, sum ger tað møguligt at stýra heimstólum við raddarskipanum, uttan at vera treytað av skýntænastum.

Skipanin sameinir:

- Staðbundna viðgerð av heimstýringarskipanum og verju av privatlívinum.
- Staðbundna intelligens við Ollama til almennar spurningar.
- Skýmodell til torførar fyrispurningar og dagførdar upplýsingar.

## Tólbúnaður

- Raspberry Pi 5 við viðmæltum 8 GB RAM. Avmarkaður stuðul niður til Raspberry Pi 3B+.
- NVMe SSD-diskur uttan SD-kort. Avmarkaður stuðul fyri SD-kort.
- Tvívegis USB-mikrofonur og hátalari.
- Heimstýringartól, ið eru sambærilig við Zigbee, Matter, Philips Hue ella staðbundið Wi-Fi.
- Virkin køling fyri at forða hitastýrdari niðurseting av avrikinum.

## Bygnaður

1. Home Assistant OS umsitur tólini og sjálvvirknu skipanirnar.
2. openWakeWord kennir vekjiorðið staðbundið.
3. Whisper umskrivar skipanir á virka málinum gjøgnum Wyoming.
4. Endamálstilgongdin fremur heimstýringarskipanirnar staðbundið.
5. Piper myndar svarini á katalanskum.
6. Ollama svarar almennum spurningum uttan at senda dátur á internetið.
7. Ský-IA fær bert greiðar fyrispurningar, sum krevja framkomna IA.

## Ætlaðir eginleikar

- Raddarstýring av ljósum, stikkum, hitaskipan, rullugardinum og øðrum tólum.
- Fleirmálslig alias.
- Tíðarstýrarar, ið verða stýrdir við rødd.
- Staðbundin veðurfyrispurningur.
- Spæling og stýring av tónleiki.
- Privat varaskipan við einum Ollama-modelli.
- Kennsla av persóni eftir røddini.
- Langtíðar minni um samanhang.
- Valfrí víðaristending til eitt ský-IA-modell.
- Trygdaravrit og eftirlit við avrikinum.

## Meginreglur fyri sniðgeving

- Heimstýringarskipanir skulu virka uttan netsamband.
- Staðbundna endamálstilgongdin hevur framíhjárætt fram um LLM.
- Ljóðdátur og privatar samrøður verða helst viðgjørdar staðbundið.
- Skýmodell verða bert nýtt til greiðar ella torførar fyrispurningar, og bert um brúkarin greitt hevur biðið um tað, tá assistenturin varð settur upp.
- Skipanin skal halda hitastig og seinking støðug undir samanhangandi last.

## Støðan í verkætlanini

Verkætlanin er lýst sum eitt virkisligt backlog. Serstakar uppsetingar, sjálvvirknar skipanir og innleggingarskript verða løgd afturat, so hvørt sum brúkarasøgurnar verða lidnar.
