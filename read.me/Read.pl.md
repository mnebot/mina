**Polski** · [Powrót do wyboru języka](../readme.md)

# Wielojęzyczny asystent domowy

Projekt opisuje wdrożenie lokalnego ekosystemu wielojęzycznego asystenta głosowego na Raspberry Pi.

## Pochodzenie nazwy Mina

**Mina** ma starogermański rdzeń w słowie *minna*, oznaczającym „pamięć”, „miłość” lub „wspomnienie”. Nazwa występuje też w innych językach: po persku *mīnā* odnosi się do „światła” lub „niebieskiego szkła”, a po japońsku *mina* oznacza „wszyscy” lub „wszyscy razem”.

Te znaczenia symbolizują **wspólną pamięć i społeczność** — wartości zgodne z asystentem towarzyszącym i wspierającym codzienne życie w domu.

Pod względem brzmienia Mina jest łagodną, ale wyraźną nazwą, z sylabową wymową `Mi-na` i niewielkim prawdopodobieństwem pomylenia z potocznymi słowami w domu.

## Cel

Stworzyć prywatny, niezawodny i szybki system domowy umożliwiający sterowanie urządzeniami za pomocą poleceń głosowych bez obowiązkowej zależności od usług chmurowych.

Architektura łączy:

- Lokalne przetwarzanie poleceń domowych i prywatność.
- Lokalną inteligencję z Ollama do pytań ogólnych.
- Modele chmurowe do złożonych zapytań i aktualnych informacji.

## Sprzęt

- Raspberry Pi 5 z 8 GB RAM — rekomendowane. Ograniczona zgodność do Raspberry Pi 3B+.
- Dysk SSD NVMe bez używania karty SD. Ograniczona zgodność z kartą SD.
- Dwukierunkowy mikrofon i głośnik USB.
- Urządzenia domowe zgodne z Zigbee, Matter, Philips Hue lub lokalnym Wi-Fi.
- Aktywne chłodzenie, aby zapobiec termicznemu ograniczaniu wydajności.

## Architektura

1. Home Assistant OS zarządza urządzeniami i automatyzacją.
2. openWakeWord lokalnie wykrywa słowo uruchamiające.
3. Whisper, przez Wyoming, transkrybuje polecenia w aktywnym języku.
4. Procesor intencji wykonuje polecenia domowe lokalnie.
5. Piper syntezuje odpowiedzi po polsku.
6. Ollama rozwiązuje ogólne pytania bez wysyłania danych do Internetu.
7. Chmurowa AI otrzymuje tylko jawne zapytania wymagające zaawansowanej AI.

## Planowane funkcje

- Sterowanie głosowe światłami, gniazdami, klimatyzacją, roletami i innymi urządzeniami.
- Wielojęzyczne aliasy.
- Minutniki obsługiwane głosowo.
- Lokalne pytania o pogodę.
- Odtwarzanie i sterowanie muzyką.
- Prywatny fallback do modelu Ollama.
- Rozpoznawanie osoby na podstawie głosu.
- Długoterminowa pamięć kontekstu.
- Opcjonalne przekierowanie do chmurowego modelu AI.
- Kopie zapasowe i monitorowanie wydajności.

## Zasady projektowe

- Polecenia domowe muszą działać bez połączenia z Internetem.
- Lokalny procesor intencji ma priorytet nad LLM.
- Dane audio i prywatne rozmowy powinny być przetwarzane lokalnie.
- Modele chmurowe są używane tylko do jawnych lub złożonych zapytań i tylko wtedy, gdy użytkownik wyraźnie o to poprosi podczas konfiguracji.
- System musi utrzymywać stabilne temperatury i opóźnienia przy ciągłym obciążeniu.

## Stan projektu

Projekt jest zdefiniowany jako funkcjonalny backlog. Specyficzne konfiguracje, automatyzacje i skrypty wdrożeniowe zostaną dodane wraz z realizacją kolejnych historii użytkownika.
