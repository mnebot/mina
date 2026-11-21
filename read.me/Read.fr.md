# Assistant domotique multilingue

**Langue :** Français · [Retour au choix de la langue](../readme.md)

**Lire en :** [Català](Read.ca.md) · [English](Read.en.md) · [Español](Read.es.md) · [Français](Read.fr.md) · [Deutsch](Read.de.md) · [Italiano](Read.it.md) · [Português](Read.pt.md) · [Nederlands](Read.nl.md)

Ce projet décrit le déploiement d'un écosystème domotique local sur un Raspberry Pi avec un assistant vocal multilingue.

## Origine du nom Mina

**Mina** a une ancienne racine germanique, *minna*, qui signifie « mémoire », « affection » ou « souvenir ». Le nom existe également dans d'autres langues : en persan, *mīnā* est associé à la « lumière » ou au « verre bleu », tandis qu'en japonais, *mina* signifie « tout le monde » ou « tous ensemble ».

Ces interprétations symbolisent une **mémoire partagée et la communauté**, des valeurs qui correspondent à un assistant accompagnant le quotidien du foyer.

Sur le plan phonétique, Mina est un nom doux mais clair, prononcé en deux syllabes (`Mi-na`), et peu susceptible d'être confondu avec des mots courants dans un environnement domestique.

## Objectif

Créer un système domotique privé, fiable et rapide permettant de contrôler les appareils de la maison par la voix, sans dépendance obligatoire aux services cloud.

L'architecture associe :

- Un traitement local des commandes domotiques, au service de la confidentialité.
- Une intelligence locale avec Ollama pour les questions générales.
- Des modèles cloud pour les demandes complexes et les informations actualisées.

## Matériel

- Raspberry Pi 5 avec 8 Go de RAM recommandés. Compatibilité limitée jusqu'au Raspberry Pi 3B+.
- Disque SSD NVMe pour éviter l'utilisation d'une carte SD. Compatibilité limitée avec une carte SD.
- Microphone et haut-parleur USB bidirectionnels.
- Appareils domotiques compatibles avec Zigbee, Matter, Philips Hue ou le Wi-Fi local.
- Refroidissement actif pour éviter le throttling thermique.

## Architecture

1. Home Assistant OS gère les appareils et les automatisations.
2. openWakeWord détecte localement le mot d'activation.
3. Whisper transcrit les commandes dans la langue active via Wyoming.
4. Le processeur d'intentions exécute localement les commandes domotiques.
5. Piper synthétise les réponses en catalan.
6. Ollama répond aux questions générales sans envoyer de données sur Internet.
7. L'IA cloud ne reçoit que les demandes explicites nécessitant une IA avancée.

## Fonctionnalités prévues

- Commande vocale des lumières, prises, du chauffage et de la climatisation, des stores et d'autres appareils.
- Alias multilingues.
- Minuteries commandées à la voix.
- Consultation locale de la météo.
- Lecture et contrôle de la musique.
- Solution de secours privée avec un modèle Ollama.
- Reconnaissance de la personne par la voix.
- Mémoire contextuelle à long terme.
- Transfert facultatif vers un modèle d'IA cloud.
- Sauvegardes et suivi des performances.

## Principes de conception

- Les commandes domotiques doivent fonctionner sans connexion Internet.
- Le processeur d'intentions local est prioritaire sur les LLM.
- Les données audio et les conversations privées sont traitées de préférence localement.
- Les modèles cloud ne sont utilisés que pour les demandes explicites ou complexes, et uniquement si l'utilisateur l'a expressément demandé lors de la configuration de l'assistant.
- Le système doit maintenir des températures et une latence stables en fonctionnement continu.

## État du projet

Le projet est défini comme un backlog fonctionnel. Les configurations spécifiques, les automatisations et les scripts de déploiement seront ajoutés au fur et à mesure de la réalisation des récits utilisateurs.
