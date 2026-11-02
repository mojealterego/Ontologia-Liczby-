# ONTOLOGIA LICZBY — Korpus Formalny Nauk Matematycznych

**Autor:** Andrzej Mikulski · **Rok:** 2026  
**Stan:** wydanie rozwojowe, Tom I otwarty. Wszystkie poziomy i punkty podlegają audytowi.

## Bezwzględna kolejność redakcyjna

1. Okładka „ONTOLOGIA LICZBY — TOM I”.
2. **Wstęp historyczny „O początkach liczby: między genezą a statusem bytowym” — zachować dotychczasową treść bez ingerencji.**
3. **Opracowania Tomu I według wewnętrznej mapy „TAKSONOMII MATEMATYKI — Wydanie jednolite pełne 2026”.** Mapa jest tylko narzędziem redakcyjnym do planowania i kontroli kompletności; nie stanowi gotowego spisu treści książki.
4. Rozwinięte, indywidualnie weryfikowane rozdziały matematyczne według uzgodnionej progresji nauczania.
5. Zachowany blok 81 opracowań MSC2020 (197 stron wcześniejszego materiału) — **nie wliczać do bilansu Tomu I**, dopóki nie zostanie przeniesiony redakcyjnie do właściwego tomu.
6. **Dopiero po ukończeniu, weryfikacji i finalnym składzie całego Tomu I utworzyć ostateczny spis treści**, na podstawie rzeczywistych rozdziałów i numeracji stron; w gotowej książce umieścić go po niezmienionym wstępie historycznym.

**Tom I:** zamknięcie po 1222 stronach części merytorycznej; bez dzielenia rozpoczętego rozdziału, dowodu ani monografii. Ostateczny spis treści opracować **wyłącznie po ukończeniu Tomu I**, a następnie umieścić go po wstępie historycznym. **Wydanie jest nadal nieukończone.**

## Minimalna liczba stron rzeczywistej treści na punkt

| Poziom trudności | Przeznaczenie | Minimum |
|---|---|---:|
| I | Edukacja wczesnoszkolna i szkoła podstawowa | 4 |
| II | Liceum, technikum i początek studiów | 11 |
| III | Kanon uniwersytecki / matematyka akademicka | 44 |
| IV | Zaawansowane specjalizacje i doktorat | 111 |
| V | Współczesne teorie i programy badawcze | 333 |
| VI | Siedem Problemów Milenijnych | 1444 |

Strony muszą zawierać rzeczywistą, niepowtarzalną treść: definicje, twierdzenia, dowody (z wyszczególnionymi założeniami), przykłady, obliczenia, kontrprzykłady, rozwiązane ćwiczenia, ograniczenia i bibliografię. **Nie zaliczać pustych lub sztucznie rozdzielonych stron.** Odróżniać kontrolę paginacji od naukowej recenzji.

## Taksonomia jako wewnętrzna mapa redakcyjna

Autorska klasyfikacja obejmuje 7 rodzin matematycznych (A–G), poziomy I–VI, 514 autorskich podtematów oraz autorski indeks 6006 pozycji MSC2020. **MSC2020 jest klasyfikacją piśmiennictwa, nie stopniowaniem trudności ani listą twierdzeń.** Redakcyjne LEVEL I–VI są niezależne i mogą się różnić od charakteru samego kodu MSC.

Porządek klas:
- **A:** podstawy, historia, kombinatoryka — MSC 00, 01, 03, 05, 06, 08.
- **B:** liczby, algebra, kategorie — MSC 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22.
- **C:** analiza, równania, optymalizacja — MSC 26, 28, 30, 31, 32, 33, 34, 35, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49.
- **D:** geometria i topologia — MSC 51, 52, 53, 54, 55, 57, 58.
- **E:** losowość, obliczenia, informatyka — MSC 60, 62, 65, 68.
- **F:** fizyka matematyczna i nauki o Ziemi — MSC 70, 74, 76, 78, 80, 81, 82, 83, 85, 86.
- **G:** optymalizacja, biologia, informacja, edukacja — MSC 90, 91, 92, 93, 94, 97.

Pełen dokument źródłowy: **„TAKSONOMIA_MATEMATYKI_WYDANIE_JEDNOLITE_PELNE_2026.pdf” (637 stron)**, przekazany przez autora. Należy dodać ten plik binarny do `references/` i sprawdzić SHA-256; **jego obecności w repo nie wolno deklarować, dopóki upload nie zostanie potwierdzony**.

## Reguły weryfikacji

- Materiał historyczny chronić przed niezamierzonymi zmianami; badać jego poprawność w osobnej liście uwag.
- Dla każdego punktu utrzymywać ID, nazwę, poziom trudności, powiązania z taksonomią, minimalną i rzeczywistą liczbę stron, dowody/źródła, status recenzji.
- Wewnętrzną mapę i indeksy odróżniać od finalnego spisu treści; przed zamknięciem Tomu I nie publikować spisu jako gotowego.
- Wymagane kontrole: integralność źródeł, poprawność kompilacji PDF, numeracja, niepuste strony, brak duplikatów, poprawność wzorów i dowodów.
- Problemy otwarte opisywać jako otwarte; nie tworzyć fikcyjnych rozwiązań.
- Zachować ciągłość wersji i pełną historię zmian.

**Uwaga:** repo zainicjowano tekstową dokumentacją. Brak binarnych plików PDF w danym commicie nie oznacza, że ich upload został wykonany.


## Dyrektywa wydawnicza — 2026-11-02: limit rozmiaru tomów

- **Nie obowiązuje sztywne 1222 stron na tom.** Tom może liczyć mniej stron, jeżeli jego zawartość jest kompletna i spełnia wymagania merytoryczne oraz redakcyjne. Dawne `585/1222` jest wyłącznie historycznym wskaźnikiem wcześniejszego planu, nie aktualnym kryterium ukończenia.
- **Twardy limit artefaktu:** każdy końcowy PDF pojedynczego tomu musi mieć rozmiar **ściśle mniejszy niż 99 MB** (konserwatywnie przyjmować 99 000 000 bajtów jako górny próg, a test odbiorczy wymaga `size < 99000000`).
- Kontrola rozmiaru następuje po ostatecznym składzie, osadzeniu fontów, grafik i optymalizacji. Preferować tekst i wzory wektorowe; obrazy kompresować z zachowaniem czytelności. Gdy optymalizacja nie wystarcza, dzielić materiał na logiczne tomy bez pomijania treści.
- Liczba stron w nowych materiałach pozostaje niezaliczona do kanonicznego Tomu I przed rzeczywistą integracją z monolitem 0.20. Wstęp historyczny pozostaje bez zmian; nie tworzyć końcowego spisu treści przed ukończeniem Tomu I.
