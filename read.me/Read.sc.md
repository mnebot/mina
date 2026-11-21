**Sardu** · [Torra a sa seberada de sa limba](../Read.md)

# Assistente domèsticu multilingua

Custu progetu descriet sa coloeada de unu ecosistema locale de assistente de boghe multilingua in Raspberry Pi.

## Origina de su nòmene Mina

**Mina** tenet una raighes germànica antiga in *minna*, chi bolet nàrrere «memòria», «affetu» o «recordu». Est presente fintzas in àteras limbas: in persianu, *mīnā* s’acapiat a «lughe» o «vidru birde-ieddu», e in giaponesu, *mina* bolet nàrrere «totus» o «totus paris».

Custas interpretationes simbolegiant una **memòria cumpartzida e una comunitate**, valores coherentes cun un’assistente chi accumpangiat e agat a sa vida de cada die de sa domu.

Pro sa sona, Mina est unu nòmene dòtzus ma craru, cun pronùntzia sillàbica `Mi-na` e piga probabilidade de cunfusione cun faeddos comuna in s’ambiente domèsticu.

## Obietivu

Creare unu sistema domèsticu privadu, afidàbile e lestru chi permitat de controllare dispositivos domèsticos cun comandos de boghe, chene dipendentzia obligatòria dae serbìtzios in nue.

S’architetura cumbinat:

- Elaboratzione locale pro comandos domèsticos e riservadesa.
- Intelligèntzia locale cun Ollama pro preguntas generales.
- Modellos in nue pro preguntas cumplessas e informatziones atualizadas.

## Hardware

- Raspberry Pi 5 cun 8 GB de RAM racomandados. Compatibilidade limitada fintzas a Raspberry Pi 3B+.
- Disc SSD NVMe chene impreu de carta SD. Compatibilidade limitada cun carta SD.
- Micròfonu e altoparlante USB bidiretzionales.
- Dispositivos domèsticos compatìbiles cun Zigbee, Matter, Philips Hue o Wi-Fi locale.
- Friscada ativa pro evitare su throttling tèrmicu.

## Architetura

1. Home Assistant OS gestit dispositivos e automatizatziones.
2. openWakeWord rilevat localmente sa faeddu de ativatzione.
3. Whisper trascribet comandos in sa limba ativa cun Wyoming.
4. Su protzessore de intentos esecutat comandos domèsticos localmente.
5. Piper sintetizat respostas in sardu.
6. Ollama risolvet preguntas generales chene imbiare datos a Internet.
7. Sa IA in nue retzet sceti preguntas explicitas chi rechiedent IA avantzada.

## Funtzionalidades previstas

- Controllu de boghe de lughes, pristas, climatizatzione, persianas e àteros dispositivos.
- Alias multilinguas.
- Temporizadores gestidos cun sa boghe.
- Consulta metereològica locale.
- Riprodutzione e controllu de màsica.
- Fallback privadu a unu modellu Ollama.
- Reconoscimentu de sa pessone pro sa boghe.
- Memòria de cuntestu a longu tèrmini.
- Derivatzione optzionale a unu modellu IA in nue.
- Copias de seguresa e monitoradgiu de prestaciones.

## Printzìpios de disinnu

- Is comandos domèsticos depent funtzionare chene connessione a Internet.
- Su protzessore locale de intentos tenet prioridade subra is LLM.
- Is datos àudio e is conversatziones privadas si depent elaborare de fàtzile localmente.
- Is modellos in nue si impreat in isceti preguntas explicitas o cumplessas, e sceti si s’usuariu ddu dimandat in manera esplicita in sa cunfiguratzione.
- Su sistema depet mantenere temperaturas e latèntzias istàbiles in su còrrere contìnuo.

## Istadu de su progetu

Su progetu est definitu comente unu backlog funtzionale. Configuratziones ispetzìficas, automatizatziones e script de instalatzione s’ant a annànghere in su mentres chi is istòrias de usuàriu si cumpretant.
