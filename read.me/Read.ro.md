**Română** · [Înapoi la alegerea limbii](../readme.md)

# Asistent casnic multilingv

Acest proiect descrie implementarea locală a unui ecosistem de asistent vocal multilingv pe un Raspberry Pi.

## Originea numelui Mina

**Mina** are o rădăcină germanică veche în *minna*, care înseamnă „memorie”, „afecțiune” sau „amintire”. Este prezent și în alte limbi: în persană, *mīnā* se leagă de „lumină” sau „sticlă albastră”, iar în japoneză, *mina* înseamnă „toți” sau „toți împreună”.

Aceste interpretări simbolizează o **memorie comună și comunitate**, valori potrivite pentru un asistent care însoțește și sprijină viața cotidiană din locuință.

Din punct de vedere sonor, Mina este un nume blând, dar clar, cu pronunția silabică `Mi-na` și o probabilitate mică de confuzie cu cuvinte obișnuite în mediul domestic.

## Obiectiv

Crearea unui sistem casnic privat, sigur și rapid, care permite controlul dispozitivelor din locuință prin comenzi vocale, fără dependență obligatorie de servicii cloud.

Arhitectura combină:

- Procesare locală pentru comenzile casnice și confidențialitate.
- Inteligență locală cu Ollama pentru întrebări generale.
- Modele cloud pentru întrebări complexe și informații actualizate.

## Hardware

- Raspberry Pi 5 cu 8 GB RAM — recomandat. Compatibilitate limitată până la Raspberry Pi 3B+.
- SSD NVMe, fără utilizarea unui card SD. Compatibilitate limitată cu cardul SD.
- Microfon și difuzor USB bidirecționale.
- Dispozitive casnice compatibile cu Zigbee, Matter, Philips Hue sau Wi-Fi local.
- Răcire activă pentru evitarea limitării termice.

## Arhitectură

1. Home Assistant OS gestionează dispozitivele și automatizările.
2. openWakeWord detectează local cuvântul de activare.
3. Whisper transcrie comenzile în limba activă prin Wyoming.
4. Procesorul de intenții execută comenzile casnice local.
5. Piper sintetizează răspunsurile în română.
6. Ollama rezolvă întrebări generale fără a trimite date pe Internet.
7. IA din cloud primește numai solicitări explicite care necesită IA avansată.

## Funcții planificate

- Control vocal pentru lumini, prize, climatizare, jaluzele și alte dispozitive.
- Aliasuri multilingve.
- Temporizatoare gestionate vocal.
- Consultări locale despre vreme.
- Redarea și controlul muzicii.
- Fallback privat către un model Ollama.
- Recunoașterea persoanei după voce.
- Memorie de context pe termen lung.
- Redirecționare opțională către un model AI în cloud.
- Copii de rezervă și monitorizarea performanței.

## Principii de proiectare

- Comenzile casnice trebuie să funcționeze fără conexiune la Internet.
- Procesorul local de intenții are prioritate față de LLM-uri.
- Datele audio și conversațiile private trebuie procesate preferabil local.
- Modelele cloud sunt utilizate numai pentru solicitări explicite sau complexe și doar dacă utilizatorul cere acest lucru în mod explicit la configurarea asistentului.
- Sistemul trebuie să mențină temperaturi și latențe stabile sub sarcină continuă.

## Starea proiectului

Proiectul este definit ca o listă funcțională de sarcini. Configurările specifice, automatizările și scripturile de implementare se adaugă pe măsură ce poveștile utilizatorului sunt finalizate.
