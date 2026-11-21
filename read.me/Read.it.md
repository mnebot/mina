# Assistente domotico multilingue

**Lingua:** Italiano · [Torna alla scelta della lingua](../Read.md)

**Leggi in:** [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Questo progetto descrive la realizzazione di un ecosistema domotico locale su Raspberry Pi con un assistente vocale multilingue.

## Origine del nome Mina

**Mina** ha un'antica radice germanica in *minna*, che significa «memoria», «affetto» o «ricordo». Il nome è presente anche in altre lingue: in persiano, *mīnā* è associato a «luce» o «vetro blu», mentre in giapponese *mina* significa «tutti» o «tutti insieme».

Queste interpretazioni simboleggiano **memoria condivisa e comunità**, valori coerenti con un assistente che accompagna e sostiene la vita quotidiana in casa.

Dal punto di vista fonetico, Mina è un nome dolce ma chiaro, pronunciato in due sillabe (`Mi-na`), con poche probabilità di essere confuso con parole comuni in un ambiente domestico.

## Obiettivo

Creare un sistema domotico privato, affidabile e veloce che permetta di controllare i dispositivi di casa con comandi vocali, senza dipendere necessariamente dai servizi cloud.

L'architettura combina:

- Elaborazione locale dei comandi domotici per tutelare la privacy.
- Intelligenza locale con Ollama per le domande generali.
- Modelli cloud per richieste complesse e informazioni aggiornate.

## Hardware

- Raspberry Pi 5 con 8 GB di RAM consigliati. Compatibilità limitata fino a Raspberry Pi 3B+.
- SSD NVMe per evitare l'uso di una scheda SD. Compatibilità limitata quando si usa una scheda SD.
- Microfono e altoparlante USB bidirezionali.
- Dispositivi domotici compatibili con Zigbee, Matter, Philips Hue o Wi-Fi locale.
- Raffreddamento attivo per evitare il throttling termico.

## Architettura

1. Home Assistant OS gestisce i dispositivi e le automazioni.
2. openWakeWord rileva localmente la parola di attivazione.
3. Whisper trascrive i comandi nella lingua attiva tramite Wyoming.
4. Il processore delle intenzioni esegue localmente i comandi domotici.
5. Piper sintetizza le risposte in catalano.
6. Ollama risponde alle domande generali senza inviare dati su Internet.
7. L'IA cloud riceve solo richieste esplicite che richiedono un'IA avanzata.

## Funzionalità previste

- Controllo vocale di luci, prese, climatizzazione, tapparelle e altri dispositivi.
- Alias multilingue.
- Timer gestiti con la voce.
- Consultazioni meteo locali.
- Riproduzione e controllo della musica.
- Alternativa privata con un modello Ollama.
- Riconoscimento della persona tramite la voce.
- Memoria contestuale a lungo termine.
- Instradamento facoltativo verso un modello di IA cloud.
- Backup e monitoraggio delle prestazioni.

## Principi di progettazione

- I comandi domotici devono funzionare senza connessione a Internet.
- Il processore locale delle intenzioni ha la priorità sugli LLM.
- I dati audio e le conversazioni private vengono elaborati preferibilmente in locale.
- I modelli cloud vengono usati solo per richieste esplicite o complesse e soltanto se l'utente lo ha richiesto esplicitamente durante la configurazione dell'assistente.
- Il sistema deve mantenere temperature e latenza stabili anche sotto carico continuo.

## Stato del progetto

Il progetto è definito come un backlog funzionale. Le configurazioni specifiche, le automazioni e gli script di distribuzione verranno aggiunti man mano che saranno completate le storie utente.
