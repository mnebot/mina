**Lian: Tetum · [Fila ba hili lian](../readme.md)**

# Asistente Uma Inteligente Multilingue


**Lee iha:** [Tetum](Read.tet.md) · [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Projetu ida-ne'e deskreve implementasaun ekosistema uma inteligente lokál iha Raspberry Pi, ho asistente vokál ne'ebé suporta lian oioin.

## Orijen naran Mina

**Mina** mai husi abut liafuan *minna* iha lian Jermániku antigu, ne'ebé signifika “memória”, “domin” ka “lembransa”. Naran ne'e mos iha lian seluk: iha lian Pérsia, *mīnā* iha relasaun ho “naroman” ka “vidru azul”; iha lian Japonés, *mina* signifika “ema hotu” ka “hotu hamutuk”.

Interpretasaun hirak-ne'e simboliza **memória ne'ebé fahe hamutuk no komunidade**, valór sira ne'ebé koerente ho asistente ida ne'ebé akompaña no apoia moris loroloron iha uma.

Iha parte sonu nian, Mina mak naran ne'ebé malirin maibé klaru. Pronúnsia tuir sílaba mak `Mi-na`, no iha posibilidade ki'ik atu konfuze ho liafuan komún iha ambiente uma nian.

## Objetivu

Kria sistema uma inteligente ne'ebé privadu, fiável no lalais, atu bele kontrola dispozitivu uma nian ho komandu vokál, sein dependénsia obrigatória ba servisu cloud.

Arkitetura ne'e kombina:

- Prosesamentu lokál ba komandu uma inteligente no privasidade.
- Intelijénsia lokál ho Ollama ba pergunta jerál.
- Modelu cloud ba pergunta kompleksu no informasaun atualizada.

## Hardware

- Recomenda Raspberry Pi 5 ho RAM 8 GB. Kompatibilidade limitadu to'o Raspberry Pi 3B+.
- Uza SSD NVMe; la uza karta SD. Suporta karta SD ho limitasaun.
- Mikrofone no altavoz USB bidireksionál.
- Dispozitivu uma inteligente kompatível ho Zigbee, Matter, Philips Hue ka Wi-Fi lokál.
- Refrijerasaun ativa atu prevene throttling térmiku.

## Arkitetura

1. Home Assistant OS jere dispozitivu no automasaun.
2. openWakeWord deteta liafuan atu ativa sistema iha lokál.
3. Whisper transkreve komandu iha lian ne'ebé ativa hela liuhusi Wyoming.
4. Prosesadór intensaun hala'o komandu uma inteligente iha lokál.
5. Piper sintetiza resposta vokál iha lian Katalán.
6. Ollama responde pergunta jerál sein haruka dadus ba Internet.
7. Pergunta ne'ebé husu AI avansada no ne'ebé husu klaramente de'it mak haruka ba AI cloud.

## Funsionalidade ne'ebé planeadu

- Kontrola naroman, tomada, klimatizasaun, kortina no dispozitivu seluk ho lian.
- Alias multilingue.
- Temporizadór ne'ebé jere ho lian.
- Husik pergunta kona-ba tempu lokál.
- Reprodús no kontrola múzika.
- Fallback privadu ba modelu Ollama.
- Rekonese ema husi lian.
- Memória kontextu ba tempu naruk.
- Haruka ba modelu AI cloud tuir opsaun.
- Kópia seguransa no monitorizasaun prestasaun.

## Prinsípiu dezenhu

- Komandu uma inteligente tenke funsiona maski la iha ligasaun Internet.
- Prosesadór intensaun lokál iha prioridade liu LLM.
- Dadus áudio no konversa privadu tenke prosesadu iha lokál bainhira bele.
- Modelu cloud uza de'it ba pergunta ne'ebé husu klaramente ka kompleksu, no uza de'it bainhira utilizadór ativa ho klaru bainhira konfigura asistente.
- Sistema tenke mantein temperatura no laténsia estável iha karga kontínua.

## Estadu projetu

Projetu ne'e define ona hanesan lista servisu funsionál. Konfigurasaun espesífika, automasaun no script implantasaun sei aumenta bainhira istória utilizadór sira remata.
