# F17.3 — dodatni semigroup cieplny, wymuszenie i schemat Eulera (31 października 2026)

## Zmiana rzeczywiście zapisana na main

- Rozszerzono istniejący plik `manuscript/tom-01/F17/F17.3_UZUPELNIENIE_GEOMETRIA_DYSKRETNA.md`, **wyłącznie przez dopisanie** sekcji 22–24. Commit źródła `7f787ae5430f8bea630f9c86210c4d8a38f44f34`; commit normalizacji jednej nadmiarowej pustej linii `7ee6d8663e416a7b03a29226e29cdcf1ede8c21c`. Końcowy Git blob SHA `2e501f099b5d83deb78adfa7e12706a25c8b7068`, zgodny z lokalnym źródłem użytym do kompilacji.
- Zakres dopisany: D29–D32 (4 definicje), T81–T89 (9 twierdzeń z dowodami), K39–K44 (6 kontrprzykładów), Z86–Z97 (12 rozwiązanych zadań). Całość F17.3: D1–D32, T1–T89 (w tym wnioski), K1–K44, Z1–Z97.
- Zakres matematyczny: dodatniość i substochastyczność macierzy `exp(-tL)`, ścisła dodatniość dla `t>0`, porównanie i kontrakcja w normie maksimum, semigrupa, symetria, jawny krok Eulera, wzór Duhamela, stałe wymuszenie i granica Greena, ślad i wyznacznik.

## Testy i kompilacja

- Plik testów: `tests/test_f173_heat_semigroup.py`, commit `7d82c6c76088236aba1b7dfae4f6ea70706324c4`, Git blob `c8bc34e076a9b48d8c7f6e4ab25b6187b7ed02a1`, zgodny z testowanym lokalnym źródłem.
- Lokalne polecenia: `python -m unittest discover -s tests -p 'test_f173_heat_semigroup.py' -q` — **15/15 OK**; `python -m pytest tests/test_f173_heat_semigroup.py -q` — **15 passed**; `python -m compileall -q tests` — **kod 0**. Testy obejmują m.in. jądro dodatnie, sumy wierszy, semigrupę, symetrię, normę, dokładne współczynniki Eulera, granicę schematu, ślad, wyznacznik i rozwiązanie wymuszone. Pierwsza wersja testu numeracji błędnie pomijała etykiety „Wniosek” oraz „Kontrprzykład”; poprawiono wyrażenie regularne przed publikacją.
- PDF: Pandoc + XeLaTeX, FreeSerif, A4, 11 pt, margines 20 mm. **24 strony**, każda niepusta (2221–3682 znaków ekstrakcji), **0 słów poza marginesem bezpieczeństwa 8 pt** w PyMuPDF. Kompilacja zakończona kodem 0. SHA-256 PDF: `aef3db5dc1be9c95c4cab266c5f74b5a9fb00d87aea8e037287ae13e0adf2014`. PDF jest wyłącznie lokalnym artefaktem; nie opublikowano binarium na GitHub.
- Kontrola integralności: lokalny `git hash-object` źródła = `2e501f099b5d83deb78adfa7e12706a25c8b7068`, testu = `c8bc34e076a9b48d8c7f6e4ab25b6187b7ed02a1`. Obie wartości odpowiadają odczytanym blobom na `main`.

## Granice dowodów i blokady

- Testy są skończonymi kontrolami obliczeniowymi, nie mechanizacją twierdzeń ani niezależną recenzją naukową. Nie przeprowadzono pełnej regresji repozytorium ani testu integracyjnego całego Tomu I.
- Brak kompletnego źródła rzeczywistego monolitu 0.20 uniemożliwia integrację, kontrolę paginacji wydania głównego i doliczenie stron. **Bilans 585/1222 pozostaje bez zmian.**
- Historyczny wstęp i wcześniejsze rozdziały pozostały nietknięte. Nie utworzono końcowego spisu treści ani nie rozpoczęto Tomu II.
