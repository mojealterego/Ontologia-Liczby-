# Dowody wykonania — MSC 97D40, część III-D (2026-11-02)

## Zakres faktycznie zapisany na main

- Nowa sekcja: [97D40_IIID_OPTYMALIZACJA_PROGRAMU_ZAJEC.md](../manuscript/tom-01/MSC97/97D40_IIID_OPTYMALIZACJA_PROGRAMU_ZAJEC.md), commit [b874688b](https://github.com/mojealterego/Ontologia-Liczby-/commit/b874688b736dc6bfccdf01b170a70c52dc7105ca). **10 definicji D37–D46, 13 twierdzeń z dowodami T43–T55, 6 kontrprzykładów K23–K28 i 14 rozwiązanych zadań Z51–Z64.** Istniejący manuskrypt III-A–C nie był nadpisywany.
- Testy: [test_msc97d40_optimization.py](../tests/test_msc97d40_optimization.py), commit [6f7d022e](https://github.com/mojealterego/Ontologia-Liczby-/commit/6f7d022e3c78565cc112291c8e612526d42db494).
- Workflow rozdziału: [tom1-msc97d40.yml](../.github/workflows/tom1-msc97d40.yml), commit [7d5ed1fe](https://github.com/mojealterego/Ontologia-Liczby-/commit/7d5ed1fed25b63dcf1798ea3ada4c27b4486b6e9). Uruchamia nowy plik testów i kompiluje łącznie manuskrypt główny oraz III-D, z kontrolą znaczników T55/Z64 i limitu rozmiaru.

## Testy lokalne

Uruchomiono `python -m unittest -v test_msc97d40_optimization.py`: **8/8 testów OK**. Testy porównują algorytm plecakowy z pełnym przeglądem, minimalny koszt pokrycia przez maski z pełnym przeglądem, granice relaksacji ułamkowej, monotoniczność budżetu i wzór probabilistycznego pokrycia. Wykonano je na lokalnym pliku o Git blob SHA-1 **9aa7105a0782b2ec5350a3be91d2045900a0c093**, zgodnym z `main`.

Lokalny źródłowy Markdown III-D po usunięciu końcowego znaku nowej linii ma Git blob SHA-1 **697898f8664503620238cc70084cf1e0bff6665f**, zgodny z `main`. W kompilacji użyto tego samego tekstu z nieistotnym końcowym znakiem nowej linii.

## PDF i integracja

- Kompilacja samodzielnego III-D przez Pandoc/XeLaTeX: **4 strony A4**, SHA-256 `1916f5b6e2b456ab2bae525bf7bc3a38d86d05cefaf52208e207b5b834bf01e6`. Wszystkie strony mają tekst, **zero słów poza marginesem bezpieczeństwa 5 pt**; strona pierwsza obejrzana wizualnie.
- Pełny roboczy rozdział MSC 97D40: **16 stron**, złączenie wcześniej zweryfikowanych 12 stron III-A–C z 4 stronami III-D. **Nie jest to jeszcze jednolita kompilacja dokładnego HEAD Markdown** — taką kompilację przewiduje zmodyfikowany workflow CI.
- Podgląd Tomu I: **657 stron** = 629 stron przekazanego monolitu + 6 stron MSC 97C20 + 6 stron MSC 97C30 + 16 stron MSC 97D40. **8 383 427 B**, SHA-256 `974f492e55db92b99aabc5ec1cfa3a2659c5bc1b1e62befefbf4ec9aa25a020a`.
- Weryfikacja: **629/629** oryginalnych stron zachowanych tekstowo, identyczne rendery stron źródłowych **1, 2, 33, 34, 629**, zachowane **585/585** oryginalnych zakładek i **4/4** odsyłacze. Nowa książka ma **589 zakładek** łącznie. Wszystkie 28 stron suplementów mają tekst. Plik spełnia limit **<99 000 000 B**.
- Oryginalny monolit 629 stron: SHA-256 `cd2e5e9ef0adefc3344ff8a7a1bcaa4befd2e1b85b4a711a36c3a0c179cb1309`.

## Otwarte i niepotwierdzone

1. **Zielony wynik GitHub Actions po zmianie workflow nie został w tej turze potwierdzony.** Lokalny wynik 8/8 nie jest wynikiem CI.
2. **Poziom III nadal nieukończony:** minimum 44 stron dla MSC 97D40, obecnie 16 stron pełnego roboczego rozdziału.
3. Nie wykonano niezależnej, kompletnej recenzji wszystkich dowodów.
4. Nie ma binarnego kanonicznego monolitu **0.20**, opisanego w dokumentacji jako 864 strony. Dostarczony PDF ma 629 stron i inny hash. Integracja 657 stron jest rzeczywista, lecz **niekanoniczna**.
5. Historyczny bilans **585 stron bez zmian**; dawny cel 1222 nieobowiązkowy. Historyczny wstęp nienaruszony. Nie utworzono końcowego spisu treści ani Tomu II.
