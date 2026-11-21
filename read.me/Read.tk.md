**Türkmen dili**

# Köpmanyly öý kömekçisi

**Dil:** Türkmençe · [Dil saýlamasyna gaýdyp bar](../Read.md)

Bu taslama Raspberry Pi-de köpmanyly sesli kömekçi bilen ýerli akylly öý ekosistemasyny ýerleşdirmegi suratlandyrýar.

## Mina adynyň gelip çykyşy

**Mina** ady köne german dilli *minna* sözünden gelip çykýar, onuň manysy «ýat», «söýgi» ýa-da «süňňük»dir. Ol beýleki dillerde hem bolýar: parsça *mīnā* «ýagtylyk» ýa-da «gök aýna» bilen baglanyşykly, ýaponçada bolsa *mina* «hemmeler» ýa-da «hemmesi bilelikde» diýmekdir.

Bu düşündirişler **umumy ýady we jemgyýeti** nyşana alýar; gündelik öý durmuşyna ýoldaş bolup goldaw berýän kömekçiniň gymmatlyklaryna laýykdyr.

Ses nukdaýnazaryndan Mina ýumşak, emma aýdyň at; `Mi-na` ýaly bogunlabaryş bilen aýdylýar we öý gurşawynda adaty sözlerden ýalňyşdyrylmagynyň ähtimallygy pes.

## Maksat

Ses buýruklary arkaly öý enjamlaryny dolanmaga mümkinçilik berýän hususy, ygtybarly we çalt işjeň öý ulgamyny döretmek, bulut hyzmatlaryna hökmany garaşmazdan.

Gurluşy aşakdakylary birleşdirýär:

- Öý buýruklary we gizlinlik üçin ýerli gaýtadan işlemegiň.
- Umumy soraglar üçin Ollama arkaly ýerli akyl.
- Çylşyrymly soraglar we täzelenen maglumat üçin bulut modelleri.

## Enjamlar

- 8 GB RAM bilen Raspberry Pi 5 maslahat berilýär. Raspberry Pi 3B+ çenli çäkli laýyklyk.
- SD kartasy ulanylmazdan NVMe SSD disk. SD kartasy bilen çäkli laýyklyk.
- Iki taraplaýyn USB mikrofon we dinamik.
- Zigbee, Matter, Philips Hue ýa-da ýerli Wi-Fi bilen gabat gelýän öý enjamlary.
- Yssylyk sebäpli tizligi peseldip götermezligi üçin işjeň sowatma.

## Gurluşy

1. Home Assistant OS enjamlary we awtomatlaşdyrmany dolandyrylýar.
2. openWakeWord işjeňleşdiriji sözi ýerli ýagdaýda anyklaýar.
3. Whisper Wyoming arkaly işjeň dilde buýruklary tekste öwürýär.
4. Niyet prosessory öý buýruklaryny ýerli ýerine ýetirýär.
5. Piper jogaplary türkmen dilinde sintez edýär.
6. Ollama umumy soraglary Internetine maglumat ibermän çözýär.
7. Bulut AI diňe ösen AI talap edýän aç-açan soraglary kabul edýär.

## Garaşylýan aýratynlyklar

- Çyralary, rozetkalary, howany, perdesi we beýleki enjamlary ses bilen dolamak.
- Köpmanyly lakamlar.
- Ses bilen dolanylýan taýmerler.
- Ýerli howa maglumatyny soramak.
- Sazyň çalynyşy we dolanmagy.
- Ollama modeli üçin hususy ätiýaçlyk.
- Sesiň kömegi bilen adamy tanamak.
- Uzak möhletli kontekst ýady.
- Bulut AI modeline islege görä ugrukdyrmak.
- Ätiýaç nusga almak we öndürijiligi gözegçilikde saklamak.

## Dizaýn ýörelmeleri

- Öý buýruklary Internet birikmesiz işlemegi zerur.
- Ýerli niýet prosessory LLMlerden ileri tutulýar.
- Ses maglumatlary we şahsy söhbetdeşlikler mümkin boldugyça ýerli gaýtadan işlenýär.
- Bulut modelleri diňe aç-açan ýa-da çylşyrymly soraglar üçin ulanylýar, we diňe ulanyjy kömekçini sazlamak wagtynda muny aç-açan haýyş eden ýagdaýynda.
- Ulgam üznüksiz ýük astynda durnukly temperatura we gijikdirmegi saklamaly.

## Taslamanyň ýagdaýy

Taslama funksional backlog hökmünde kesgitlenen. Aýratyn konfigurasiýalar, awtomatlaşdyrmalar we ýerleşdirme skriptleri ulanyjy hekaýalarynyň tamamlanmagy bilen goşulmalydyr.
