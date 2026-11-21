# Assistente de automação residencial multilíngue

**Idioma:** Português · [Voltar à seleção de idioma](../Read.md)

**Ler em:** [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Este projeto descreve a implementação de um ecossistema local de automação residencial numa Raspberry Pi com um assistente de voz multilíngue.

## Origem do nome Mina

**Mina** tem uma antiga raiz germânica em *minna*, que significa «memória», «afeição» ou «recordação». O nome também existe noutras línguas: em persa, *mīnā* está associado a «luz» ou «vidro azul», e, em japonês, *mina* significa «todos» ou «todos juntos».

Estas interpretações simbolizam **memória partilhada e comunidade**, valores que combinam com um assistente que acompanha e apoia o quotidiano em casa.

Do ponto de vista fonético, Mina é um nome suave mas claro, pronunciado em duas sílabas (`Mi-na`), com baixa probabilidade de ser confundido com palavras comuns num ambiente doméstico.

## Objetivo

Criar um sistema de automação residencial privado, fiável e rápido que permita controlar os dispositivos da casa por comandos de voz, sem depender obrigatoriamente de serviços na nuvem.

A arquitetura combina:

- Processamento local dos comandos de automação residencial para proteger a privacidade.
- Inteligência local com Ollama para perguntas gerais.
- Modelos na nuvem para pedidos complexos e informações atualizadas.

## Hardware

- Raspberry Pi 5 com 8 GB de RAM recomendados. Compatibilidade limitada até à Raspberry Pi 3B+.
- SSD NVMe para evitar o uso de um cartão SD. Compatibilidade limitada quando se utiliza um cartão SD.
- Microfone e coluna USB bidirecionais.
- Dispositivos de automação residencial compatíveis com Zigbee, Matter, Philips Hue ou Wi-Fi local.
- Refrigeração ativa para evitar o throttling térmico.

## Arquitetura

1. O Home Assistant OS gere os dispositivos e as automatizações.
2. O openWakeWord deteta localmente a palavra de ativação.
3. O Whisper transcreve os comandos no idioma ativo através do Wyoming.
4. O processador de intenções executa localmente os comandos de automação residencial.
5. O Piper sintetiza as respostas em catalão.
6. O Ollama responde a perguntas gerais sem enviar dados para a Internet.
7. A IA na nuvem só recebe pedidos explícitos que exigem IA avançada.

## Funcionalidades previstas

- Controlo por voz de luzes, tomadas, climatização, estores e outros dispositivos.
- Aliases multilíngues.
- Temporizadores controlados por voz.
- Consultas meteorológicas locais.
- Reprodução e controlo de música.
- Alternativa privada com um modelo Ollama.
- Reconhecimento da pessoa pela voz.
- Memória contextual de longo prazo.
- Encaminhamento opcional para um modelo de IA na nuvem.
- Cópias de segurança e monitorização do desempenho.

## Princípios de conceção

- Os comandos de automação residencial devem funcionar sem ligação à Internet.
- O processador local de intenções tem prioridade sobre os LLM.
- Os dados de áudio e as conversas privadas são processados preferencialmente localmente.
- Os modelos na nuvem só são utilizados para pedidos explícitos ou complexos, e apenas se o utilizador o tiver solicitado expressamente ao configurar o assistente.
- O sistema deve manter temperaturas e latências estáveis sob carga contínua.

## Estado do projeto

O projeto está definido como um backlog funcional. As configurações específicas, as automatizações e os scripts de implementação serão adicionados à medida que as histórias de utilizador forem concluídas.
