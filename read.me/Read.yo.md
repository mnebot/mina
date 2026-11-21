**Èdè: Yorùbá · [Padà sí àṣàyàn èdè](../Read.md)**

# Olùrànlọ́wọ́ ilé ọlọ́gbọ́n ní onírúurú èdè

Iṣẹ́ yìí ṣàlàyé bí a ṣe lè kọ́ ètò àwọn ẹ̀rọ ilé tí ń ṣiṣẹ́ ní agbègbè kan lórí Raspberry Pi, pẹ̀lú olùrànlọ́wọ́ ohùn tí ó lè lóye ọ̀pọ̀ èdè.

## Ìpilẹ̀ orúkọ Mina

**Mina** wá láti inú ọ̀rọ̀ Jámánì àtijọ́ *minna*, tí ó túmọ̀ sí “ìrántí”, “ìfẹ́” tàbí “ohun tí a rántí”. Orúkọ náà tún wà ní àwọn èdè mìíràn: ní Páṣíà, *mīnā* ní ìbáṣepọ̀ pẹ̀lú “ìmọ́lẹ̀” tàbí “gíláàsì aláwọ̀ búlúù”; ní Japan, *mina* túmọ̀ sí “gbogbo ènìyàn” tàbí “gbogbo wa papọ̀”.

Àwọn ìtumọ̀ wọ̀nyí dúró fún **ìrántí àjọ àti ìbáṣepọ̀ àwùjọ**, àwọn ìlànà tó bá olùrànlọ́wọ́ kan mu tí ń ṣètìlẹ́yìn fún ìgbésí ayé ojoojúmọ́ nílé.

Ní ti ohùn, Mina jẹ́ orúkọ pẹ̀lẹ́ ṣùgbọ́n tí ó ṣe kedere. A ń pè é ní sílébù `Mi-na`, kò sì ṣeé ṣe kí a da á pọ̀ mọ́ àwọn ọ̀rọ̀ tí a sábà máa ń lò nílé.

## Ète

Láti ṣẹ̀dá ètò ilé ọlọ́gbọ́n tó ń dáàbò bo àṣírí, tó ṣeé gbẹ́kẹ̀lé, tó sì yára; ètò náà yóò jẹ́ kí a lè ṣàkóso àwọn ẹ̀rọ ilé pẹ̀lú àṣẹ ohùn láìjẹ́ dandan láti gbẹ́kẹ̀ lé iṣẹ́ ìkùukùu.

Ìṣètò náà so àwọn nǹkan wọ̀nyí pọ̀:

- Ṣíṣe àṣẹ ilé ní agbègbè àti dídáàbò bo àṣírí.
- Ọgbọ́n atọwọ́dá agbègbè tó ń lo Ollama láti dáhùn àwọn ìbéèrè gbogbogbòò.
- Àwọn àwòṣe ìkùukùu fún àwọn ìbéèrè tó díjú àti ìròyìn tuntun.

## Ẹ̀rọ

- Raspberry Pi 5 pẹ̀lú RAM 8 GB ni a dámọ̀ràn. Ìbámu rẹ̀ ní ààlà títí dé Raspberry Pi 3B+.
- Ẹ̀rọ ìpamọ́ NVMe SSD láìlo káàdì SD. Ìbámu pẹ̀lú káàdì SD ní ààlà.
- Maíkírófóònù USB àti ẹ̀rọ agbọ́hùn tó lè gbé ohùn jáde kí ó sì gba ohùn wọlé.
- Àwọn ẹ̀rọ ilé tó bá Zigbee, Matter, Philips Hue tàbí Wi-Fi agbègbè mu.
- Ẹ̀rọ ìtútù tó ń ṣiṣẹ́ láti dènà kí ooru má bàa dín agbára iṣẹ́ kù.

## Ìṣètò ètò

1. Home Assistant OS ń ṣàkóso àwọn ẹ̀rọ àti iṣẹ́ aládàáṣe.
2. openWakeWord ń dá ọ̀rọ̀ ìjí olùrànlọ́wọ́ mọ̀ ní agbègbè.
3. Whisper ń kọ àwọn àṣẹ sílẹ̀ ní èdè tó ń ṣiṣẹ́, nípasẹ̀ Wyoming.
4. Ẹ̀rọ ìtúpalẹ̀ èrò ń mú àwọn àṣẹ ilé ṣẹ ní agbègbè.
5. Piper ń ṣe àwọn ìdáhùn ohùn ní èdè Katalani.
6. Ollama ń dáhùn àwọn ìbéèrè gbogbogbòò láìfi dátà ránṣẹ́ sí Íńtánẹ́ẹ̀tì.
7. Ọgbọ́n atọwọ́dá ìkùukùu ń gba àwọn ìbéèrè tí olùlò ti béèrè ní kedere tí wọ́n sì nílò AI tó ti ní ìlọsíwájú nìkan.

## Àwọn ohun èlò tí a ṣètò fún ọjọ́ iwájú

- Lílo ohùn láti ṣàkóso iná, àwọn píláǹkì iná, ẹ̀rọ amúnáyé tàbí amútútù, aṣọ ìbòjú fèrèsé àti àwọn ẹ̀rọ mìíràn.
- Àwọn orúkọ àfikún ní ọ̀pọ̀ èdè.
- Àwọn aago ìkànsí tí a fi ohùn ṣàkóso.
- Béèrè nípa ojú-ọjọ́ agbègbè.
- Ṣíṣeré àti ṣíṣàkóso orin.
- Ọ̀nà àfikún tó ń dáàbò bo àṣírí nípasẹ̀ àwòṣe Ollama.
- Dídá ẹni tó ń sọ̀rọ̀ mọ̀ nípasẹ̀ ohùn rẹ̀.
- Ìrántí àyíká ọ̀rọ̀ fún ìgbà pípẹ́.
- Àṣàyàn láti fi ìbéèrè ránṣẹ́ sí àwòṣe AI ìkùukùu.
- Àwọn ẹ̀dà ààbò àti ìtọ́pinpin bí ètò ṣe ń ṣiṣẹ́.

## Àwọn ìlànà ìṣẹ̀dá

- Àwọn àṣẹ ilé gbọ́dọ̀ ṣiṣẹ́ láìsí Íńtánẹ́ẹ̀tì.
- Ẹ̀rọ ìtúpalẹ̀ èrò agbègbè ló ní ààyò ju LLM lọ.
- A gbọ́dọ̀ ṣe àtúpalẹ̀ ohùn àti ìjíròrò àṣírí ní agbègbè nígbà tí ó bá ṣeé ṣe.
- A máa ń lo àwòṣe ìkùukùu fún àwọn ìbéèrè tí a béèrè ní kedere tàbí tó díjú nìkan, àti pé kí olùlò ti yàn án ní kedere nígbà tó ń ṣètò olùrànlọ́wọ́.
- Ètò náà gbọ́dọ̀ pa ìwọ̀n ooru àti àkókò ìdáhùn mọ́ ní ìdúróṣinṣin nígbà iṣẹ́ tó ń lọ lọ́wọ́.

## Ipò iṣẹ́ náà

A ti ṣàlàyé iṣẹ́ náà gẹ́gẹ́ bí àkójọ àwọn iṣẹ́ tó wà fún ṣíṣe. A ó fi àwọn ètò pàtó, iṣẹ́ aládàáṣe àti àwọn àkọsílẹ̀ ìfisílẹ̀ kún un bí a ṣe ń parí àwọn ìtàn olùlò.
