**Occitan** · [Tornar a la causida de la lenga](../readme.md)

# Assistent domestic multiidioma

Aqueste projècte descriu lo despliegament d’un ecosistèma d’assistent vocal multilingüe local sus una Raspberry Pi.

## Origina del nom Mina

**Mina** a una ràs germanica anciana dins *minna*, que significa «memòria», «afect» o «recòrd». Es tanben present dins d’autras lengas: en persan, *mīnā* se liga a «lum» o «veire blau», e en japonés, *mina* significa «cadun» o «totes ensems».

Aquestas interpretacions simbolizan una **memòria partejada e una comunitat**, de valors coerentas amb un assistent que acompana e ajuda la vida quotidiana de l’ostal.

Quant a la sonoritat, Mina es un nom dòç mas clar, amb la pronóncia silabica `Mi-na` e una febla probabilitat de confuson amb de mots abituals dins los environaments domestics.

## Objectiu

Crear un sistèma domestic privat, fisable e rapid que permeta de contrarotlar aparelhs de l’ostal amb de comandas vocalas, sens dependéncia obligatòria de servici de nuèvol.

L’arquitectura combina:

- Tractament local per las comandas domesticas e la privacitat.
- Intelligéncia locala amb Ollama per las questions generalas.
- Modèls del nuèvol per las consultacions complèxas e l’informacion actualizada.

## Material

- Raspberry Pi 5 amb 8 Go de RAM recomandats. Compatibilitat limitada fins a Raspberry Pi 3B+.
- Disc SSD NVMe sens utilizacion de carta SD. Compatibilitat limitada amb carta SD.
- Microfòn e naut-parlaire USB bidireccionals.
- Aparelhs compatibles amb Zigbee, Matter, Philips Hue o Wi-Fi local.
- Refredament actiu per evitar l’alentiment termic.

## Arquitectura

1. Home Assistant OS gerís los aparelhs e las automatizacions.
2. openWakeWord detecta localament la paraula d’activacion.
3. Whisper transcrivís las comandas dins la lenga activa via Wyoming.
4. Lo processor d’intencions executa las comandas domesticàs localament.
5. Piper sintetiza las responsas en occitan.
6. Ollama respon a las questions generalas sens mandar de donadas a Internet.
7. L’IA del nuèvol recebís pas que las consultacions explicitas que demandan una IA avançada.

## Foncionalitats previstas

- Contraròtle vocal de lum, preniadas, climatizacion, persianas e d’autres aparelhs.
- Aliasses multiidioma.
- Minutièrs gerits per la votz.
- Consulta meteorologica locala.
- Lectura e contraròtle de musica.
- Recors privat a un modèl Ollama.
- Reconeissença de persona per la votz.
- Memòria de contexte a long tèrme.
- Derivacion opcionala a un modèl de IA al nuèvol.
- Salvagardas e susvelhança de las performanças.

## Principis de dessenh

- Las comandas domesticàs devon foncionar sens connexion a Internet.
- Lo processor d’intencions local a prioritat suls LLM.
- Las donadas àudio e las conversacions privadas se tractan localament.
- Los modèls del nuèvol son utilizats pas que per de consultacions explicitas o complèxas, e sonque se l’utilizaire o demanda explicitament en configurant l’assistent.
- Lo sistèma deu gardar de temperaturas e laténcias estables jos carga continuala.

## Estat del projècte

Lo projècte es definit coma un backlog foncional. Las configuracions especificas, las automatizacions e los scripts de despliegament se devon apondre a mesura que las istorietas d’utilizaire se completan.
