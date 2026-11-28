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

## CI, publicació i desplegament

El workflow de CI valida els canvis en les PR i els pushos a `master`. Després d'una PR validada de la mateixa repo, es publica una versió candidata a PyPI i es desplega a les Pi de prova. Després del merge, es publica i desplega un nou candidat de `master` als dispositius configurats. Les PRs de forks no publiquen ni despleguen candidats.

Per activar el desplegament, crea aquests **repository secrets** a GitHub, a **Settings → Secrets and variables → Actions**:

- `MINA_PR_TARGETS_JSON`: inventari JSON separat amb les Pi de prova que rebran candidats de PR.
- `MINA_TARGETS_JSON`: inventari JSON amb les Pi de desplegament que rebran candidats de `master`.

Cada inventari ha de contenir una llista no buida de dispositius. Cada dispositiu necessita un àlies únic, un host accessible pel tailnet de Tailscale i un usuari Linux sense privilegis de root. Exemple:

  ```json
  {"devices":[{"alias":"pi-cuina","host":"mina-cuina.<tailnet>.ts.net","user":"mina-deploy"}]}
  ```

- `TS_OAUTH_CLIENT_ID` i `TS_OAUTH_SECRET`: credencials d'un client OAuth de Tailscale amb l'etiqueta `tag:github-actions`. Limita les ACL perquè el runner només pugui accedir a les Pi de prova i de desplegament.

La publicació a PyPI utilitza **Trusted Publishing amb OIDC**: no cal crear ni desar cap token de PyPI a GitHub. Configura els workflows `candidate.yml` i `stable.yml` com a publicadors de GitHub Actions a PyPI. El candidat de PR només es prova a l'inventari separat; `stable` només es pot promocionar després del merge i de validar el candidat de `master`. Cal preparar cada Pi una vegada abans del primer desplegament.

Per a tots els passos de configuració i bootstrap, consulta el [procés de publicació](../docs/proces-de-publicacio.md).
