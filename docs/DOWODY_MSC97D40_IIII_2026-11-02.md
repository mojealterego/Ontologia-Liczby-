# Dowody MSC 97D40 III-I — 2026-11-02

## Zakres zapisany na `main`

- Manuskrypt: `manuscript/tom-01/MSC97/97D40_IIII_MODELE_OPANOWANIA_I_POWTOREK.md`, commit `b3d951949b8136ff352ca5afb8d901684cd6be8b`. **D86–D104 (19 definicji), T97–T116 (20 twierdzeń z dowodami), K53–K60 (8 kontrprzykładów), Z129–Z144 (16 zadań rozwiązanych)**.
- Testy: `tests/test_msc97d40_mastery.py`, commit `5af2c8a889805706d82b91e01605188fe96ecaab`.
- Workflow: `.github/workflows/tom1-msc97d40.yml`, commit `2786484496e819c8ecc23278b09001e9b4d75a89`, uruchamia nowy plik testów i włącza III-I do pełnej kompilacji źródeł.

## Faktyczna weryfikacja lokalna

- `python -m unittest discover -s /mnt/data/ontologia_run5 -p 'test_msc97d40_mastery.py' -v`: **14/14 testów OK**, w tym wyczerpujące siatki ułamków wymiernych, warunki brzegowe Markowa, indukcja prerekwizytów na małych DAG, wygładzanie beta–Bernoulli, identyfikowalność testu i przykłady liczbowe.
- Lokalny plik manuskryptu i zawartość odczytana ponownie z GitHub `main` mają zgodną długość **12076 znaków** i zgodną sumę kontrolną FNV-1a po jednostkach UTF-16 **`c7ff2589`**. Plik testowy lokalny i na `main`: **6080 znaków**, FNV-1a **`10740e77`**. To kontrola zgodności zawartości, nie kryptograficzna atestacja.
- `pandoc --from markdown+tex_math_dollars+tex_math_single_backslash --pdf-engine=xelatex`: skompilowano **pełny** suplement III-I do PDF A4 **4 strony, 69837 B**, SHA-256 **`ae0d59c361c973f275db93c5b2175e77b4d2ef53b56d79095465ca2084033d5a`**. Tekst PDF zawiera D104, T116, K60 i Z144. Na wszystkich czterech stronach kontrola współrzędnych nie wykryła słów poza marginesem 15 pt. Wizualnie skontrolowano stronę pierwszą i ostatnią.
- `PyMuPDF`: dołączono **4 pełne strony III-I** do istniejącego **663-stronicowego podglądu roboczego**. Wynik: **667 stron, 8139550 B**, SHA-256 **`79aa2fa6cc5fd13e3a0950e87dde2728855672e2f36d770eb44780327c78a08f`**. Sprawdzono zgodność tekstu **663/663** poprzednich stron i **4/4** nowych, zachowano **4/4** odsyłacze oraz **589/589** poprzednich zakładek (nowy PDF ma 590 zakładek).
- Lokalny manifest: `MANIFEST_III_I.json`, z hashami, licznikami stron, linków i zakładek.

## Ograniczenia odbioru

- **Niepotwierdzone:** nowy zielony przebieg GitHub Actions dla commita `27864844`; pełny złożony PDF wszystkich części MSC 97D40 na dokładnym aktualnym HEAD; niezależna formalna recenzja wszystkich dowodów.
- **Niespełnione:** minimum **44 stron** dla MSC 97D40 poziomu III. Cztery strony III-I są pełnym składem tylko tego suplementu, nie całego rozdziału.
- **Blokada kanoniczna:** dostępny podgląd bazuje na przekazanym monolicie 629 stron, a nie na właściwym binarnym wydaniu **0.20** (864 strony według rejestru). **Historyczny bilans 585 stron bez zmian**; 1222 stron nieobowiązkowe; limit końcowego PDF <99 000 000 B. Bez ingerencji we wstęp historyczny, bez końcowego spisu treści, bez Tomu II.
