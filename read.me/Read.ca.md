# Assistent domòtic multiidioma

**Idioma:** Català · [Torna a triar l'idioma](../readme.md)

**Llegeix-ho en:** [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Aquest projecte descriu el desplegament d'un ecosistema domòtic local sobre una Raspberry Pi amb un assistent de veu multilingüe.

## Origen del nom Mina

**Mina** té arrel germànica antiga en *minna*, que significa «memòria», «afecte» o «record». També està present en altres llengües: en persa, *mīnā* es relaciona amb «llum» o «vidre blau», i en japonès, *mina* significa «tothom» o «tots junts».

Aquestes interpretacions simbolitzen una **memòria compartida i comunitat**, valors coherents amb un assistent que acompanya i dona suport a la vida quotidiana de la llar.

Pel que fa a l'aspecte sonor, Mina és un nom suau però clar, amb la pronunciació sil·làbica `Mi-na` i una baixa probabilitat de confusió amb paraules habituals dins dels entorns domèstics.

## Objectiu

Crear un sistema domòtic privat, fiable i ràpid que permeti controlar dispositius de la llar mitjançant ordres de veu sense dependència obligatòria de serveis al núvol.

L'arquitectura combina:

- Processament local per a ordres domòtiques i privadesa.
- Intel·ligència local amb Ollama per a preguntes generals.
- Models al núvol per a consultes complexes i informació actualitzada.

## Maquinari

- Raspberry Pi 5 amb 8 GB de RAM recomanats. Compatibilitat limitada fins a Raspberry Pi 3B+.
- Disc SSD NVMe sense ús de targeta SD. Compatibilitat limitada amb targeta SD.
- Micròfon i altaveu USB bidireccionals.
- Dispositius domòtics compatibles amb Zigbee, Matter, Philips Hue o Wi-Fi local.
- Refrigeració activa per evitar el throttling tèrmic.

## Arquitectura

1. Home Assistant OS gestiona els dispositius i les automatitzacions.
2. openWakeWord detecta localment la paraula d'activació.
3. Whisper transcriu ordres en l'idioma actiu mitjançant Wyoming.
4. El processador d'intencions executa les ordres domòtiques localment.
5. Piper sintetitza les respostes en català.
6. Ollama resol preguntes generals sense enviar dades a Internet.
7. La IA al núvol només rep consultes explícites que requereixen IA avançada.

## Funcionalitats previstes

- Control per veu de llums, endolls, climatització, persianes i altres dispositius.
- Àlies multiidioma.
- Temporitzadors gestionats per veu.
- Consulta meteorològica local.
- Reproducció i control de música.
- Fallback privat a un model d'Ollama.
- Reconeixement de la persona per la veu.
- Memòria de context a llarg termini.
- Derivació opcional a un model d'IA al núvol.
- Còpies de seguretat i monitorització del rendiment.

## Principis de disseny

- Les ordres domòtiques han de funcionar sense connexió a Internet.
- El processador d'intencions local té prioritat sobre els LLM.
- Les dades d'àudio i les converses privades es processen preferentment en local.
- Els models al núvol només s'utilitzen per a consultes explícites o complexes, i només si l'usuari ho ha sol·licitat explícitament en configurar l'assistent.
- El sistema ha de mantenir temperatures i latències estables sota càrrega contínua.

## Estat del projecte

El projecte està definit com un backlog funcional. Les configuracions específiques, les automatitzacions i els scripts d'implantació s'hauran d'afegir a mesura que les històries d'usuari es vagin completant.
