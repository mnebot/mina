**Kan: Bamanankan** · [Segin kɔ kan sugandili ma](../readme.md)

# Kalanbaga min bɛ kan caman mɛn

Nin poroje bɛ so kɔnɔnafaamaw jɛkulu min bɛ sɔrɔ Raspberry Pi kan, o sigili kɛcogo ɲɛfɔ, ni kumakan dɛmɛbaa min bɛ kan caman fɔ.

## Tɔgɔ Mina bɔyɔrɔ

**Mina** bɛ bɔ jɛrmanikɛnɛ kan *minna* la, o kɔrɔ ye "hakili", "kanuya" walima "hakilijɛgɛrɛ". A bɛ kan wɛrɛw fana kɔnɔ: Pɛrɛsikɛ kan na, *mīnā* bɛ bɛn "yeelen" walima "fɛnɛrɛ bulu" ma, ani Japɔnkan na, *mina* kɔrɔ ye "mɔgɔ bɛɛ" walima "an bɛɛ ɲɔgɔn fɛ" ye.
O faamuyaliw bɛ **ɲɔgɔn fɛ hakilijigili ni jɛkulu** jira, o ye jogo ye minnu bɛ bɛn dɛmɛbaa ma min bɛ to ka mɔgɔw dɛmɛ u ka don o don ɲɛnamaya la so kɔnɔ.

Ni a bɛ ta tɔgɔ fɔli ta fan fɛ, Mina ye tɔgɔ dɔ ye min ka di nka a bɛ mɛn ka ɲɛ, a silabɛ fɔli ye `Mi-na` ye, ani a tɛ se ka wɔrɔ ni kumaw ye minnu bɛ fɔ tuma bɛɛ so kɔnɔ.

## Ɲɛfɔli
So kɔnɔfɛnw maraboli sisitɛmu kɛnɛman, lakika don ani joona min bɛ a to i bɛ so kɔnɔfɛnw mara ni kumakan fɛ k'a sɔrɔ a tɛ wajibi ye ka baara kɛ ni sankansɛbɛnωrɔw ye.

L'architecture bɛ nin kow nɔgɔya:

- Fɛɛrɛkɔnɔ baara kɛli so kɔnɔna minanw ka ciw ni dogoyako kama.
- Dugu kɔnɔ hakilina ni Ollama ye ɲininkaliw kosɔn minnu ye ɲininkaliw ye.
- Fɛɛrɛw minnu bɛ sanfɛyɔrɔ la ɲininkali gɛlɛnw ni kibaru kura caman kosɔn.

## Masinifɛnw
- Raspberry Pi 5 ni RAM 8 GB bɛ lajɛli la. Bɛnbaliya bɛ se ka se Raspberry Pi 3B+ ma.
- Disiki SSD NVMe min tɛ SD kariw kɛ. Bɛnbaliya dɔɔni bɛ ni SD kari ye.
- USB mɔgɔkɔrɔni ni kumabɔfɛn ɲɔgɔnna.
- Sɔrɔfana minnu bɛ bɛn Zigbee, Matter, Philips Hue walima Wi-Fi na.
- Fanga-fanga kɛlɛn bɛ kɛ walasa ka ɲɛgɛn kɛlɛn min bɛ kɛ ɲɛgɛn fanga kosɔn o bali.

## Bɔnba

1. Home Assistant OS bɛ masinw ni u ka yɛrɛ-kɛ-kɛ-liw ɲɛsin.
2. openWakeWord bɛ kɛnɛmafɛn lamɛnna kɛnɛma.
3. Whisper bɛ ciw sɛbɛn kan min bɛ baara la Wyoming fɛ.
4. Nɔfɛn kɔnɔfɛnw kɛcogo ɲɛfɔla bɛ so kɔnɔfɛnw ka ciw kɛ yɔrɔ kelen na.
5. Piper bɛ jaabiw kɛ katalan kan.
6. Ollama bɛ ɲininkali sɛbɛw jaabi k'a sɔrɔ a tɛ fɛn si ci Ɛntɛrinɛti kan.
7. Lasegɛn kɔnɔ IA bɛ ɲininkali kɛrɛnkɛrɛnnenw dɔrɔn sɔrɔ minnu mago bɛ IA kɔrɔsili la.

## Fɛɛrɛ minnu bɛna kɛ
- Yeelenw, kɔnɔbɔlɔw, kɔnɔfɛn sɔgɔsɔgɔniw, fenɛtɛrɛ kɔnɔbɔlɔw ani minɛn wɛrɛw ka kɔlɔlɔ ni kanfɛ.
- Tɔgɔw kan caman na.
- Waati-lajɛminɛnw minnu bɛ ɲɛminɛ ni kumakan ye.
- Sanfɛɲɛnamaya ɲininkali yɔrɔ la.
- Dɔnkili lamɛnni ani a marabali.
- Fɛɛrɛkɔrɔsigi kɛrɛnkɛrɛnnen min bɛ kɛ Ollama fɛɛrɛw la.
- Mɔgɔ dɔnni a ka kumakan fɛ.
- Fɛn minnu bɛ kɛ waati jan kɔnɔ, olu hakili sɔrɔli.
- A bɛ se ka yɛlɛma ka taa IA modɛli fɛ buluti kɔnɔ.
- Kɔnɔnɔgɔnaw ka kɛnɛya lajɛli ni u ka kɛnɛya mara.
## Labaara fɔlɔw

- So kɔnɔnafɛnw ka baara ka kan ka kɛ ni ɛntɛrinɛti nɔfɛn tɛ.
- Fɛɛrɛ-kɛcogo ɲɛfɔli min bɛ kɛ dugu kɔnɔ o bɛ kɛrɛnkɛrɛnnen ye LLMw ye.
- A ka fisa ka ɛrɛkɔrdiw ni kumaɲɔgɔnya kɛrɛnkɛrɛnnenw ɲɛnabɔ dugu kɔnɔ.
- Fɛn minnu bɛ sanfɛ, olu tɛ kɛ ka baara kɛ ni ɲininkali kɛrɛnkɛrɛnnenw wala ɲininkali gɛlɛnmanw dɔrɔn ye, ani ni cɛkɔrɔba ye o ɲini kɛrɛnkɛrɛnnenya la dɔrɔn tuma min na a bɛ dɛmɛbaga labɛn.
- Sistemɛ ka kan ka temparatiyɛri ni latansiw mara ka ɲɛ, k'a sɔrɔ a bɛ baara kɛ tuma bɛɛ.

## Poroje ka cogo

Proje kɔrɔ ye baara minnu bɛ kɛ ka kɔn ka sɔrɔ ka se ka baara kɛ. A bɛna kɛ cogo min na ka kɔnɔfɛnw, minɛnw ani kɔnɔfɛn kɛli siraw fara ɲɔgɔn kan, o bɛna kɛ ka kɛɲɛ ni tigiw ka tarikuw bɛ dafa cogo min na.
