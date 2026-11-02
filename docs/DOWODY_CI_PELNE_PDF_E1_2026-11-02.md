# Dowody pełnych PDF i naprawy CI — Tom I / E1 (2026-11-02)

## Przyczyna awarii i zmiany

Analiza logów GitHub Actions wykazała, że [E1-08/E1-09, run 41395104462](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41395104462) kończył się błędem `LaTeX Error: File lmodern.sty not found`. Zmieniono **tylko pliki workflow** na `main`, dodając pakiet `lmodern` do instalacji TeX. Po kolejnych testach błędów E1-02, E1-05 i E1-06/E1-07 do poleceń Pandoc dopisano parser `markdown+tex_math_dollars+tex_math_single_backslash`, aby poprawnie interpretować istniejące `\(...\)` i `\[...\]`. Nie zmieniano treści tych manuskryptów.

## Potwierdzone zielone przebiegi

| Rozdział | Run | Testy | Pełny PDF | Rozmiar PDF | Artefakt |
|---|---|---|---|---|---|
| E1-01 | [41400317753](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400317753) | wykonane w CI, wynik `success` | workflow zakończony sukcesem | niepobrane w tej turze | sprawdzić w run |
| E1-02 | [41400605417](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400605417) | 8/8 | 10 stron A4; teoria 5, ćwiczenia 5 | 79 082 B | 13121182672 |
| E1-05 | [41400615544](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400615544) | 11/11 | 7 stron A4 | 69 894 B | 13120623976 |
| E1-06 | [41400620392](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400620392) | 12/12 | 7 stron A4 | 65 251 B | 13121640331 |
| E1-07 | [41400620392](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400620392) | 13/13 | 7 stron A4 | 65 304 B | 13121640331 |
| E1-08 | [41400284879](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400284879) | 25/25 łącznie z E1-09 | 6 stron A4 | 70 837 B | 13121082603 |
| E1-09 | [41400284879](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400284879) | 25/25 łącznie z E1-08 | 6 stron A4 | 70 877 B | 13121082603 |
| E1-10 | [41400277877](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400277877) | 12/12 | 7 stron A4 | 74 142 B | 13120248942 |

Zielony przebieg oznacza poprawną kompilację **pełnego pliku źródłowego** z repozytorium, a nie tylko wybranego fragmentu. Artefakty E1-02, E1-05, E1-06/E1-07, E1-08/E1-09 i E1-10 pobrano lokalnie z GitHub Actions i sprawdzono przez `pdfinfo`; E1-08/E1-09 i E1-10 dodatkowo zweryfikowano przez zgodność SHA-256 z manifestem artefaktu.

**Znane SHA-256 pełnych PDF:** E1-02 `481b8ebad97bd847f35d21c19bd664e4eb3d30a4bf1b7f25237f06ee3736904c`; E1-05 `478eaf46fb03e7a0825933e50c9a20567c9affb43422666855730b00422b7da0`; E1-06 `1413d6c66c4691f7618da2f11e921df401ba9f642dbf5c4f44396afb14a3f431`; E1-07 `11271ab4f04022b68726228e4dcfff3b7b72f46f035e21803cf9de1bde17795e`; E1-08 `55c8852688bbb42f14a62944c1fbbf528916998b6c3f8e92b4d828a7f86f50ca`; E1-09 `ac4171ec6fff8b56ca142ef6dad69cb9d29838a91456c5b3edfcf90112a26d91`; E1-10 `514252e11b2677acc85168f644e8e6f428f0b73cee12e8eea85a3674357603c2`.

## Status niezamknięty

- E1-04: najnowszy przebieg [41400610631](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400610631) był w toku w chwili spisania protokołu; nie oznaczać go jako zielony bez zakończenia.
- E1-03: brak istniejącego workflow `tom1-e103.yml`; rozdział i testy istnieją, lecz pełny CI nie został potwierdzony.
- Powyższe strony są stronami **samodzielnych PDF poszczególnych rozdziałów**, a nie zintegrowanego Tomu I. **Historyczny bilans 585 stron nie został zwiększony.** Obowiązuje limit końcowego PDF tomu <99 000 000 bajtów; 1222 strony nie są obowiązkowym celem.
- Formalna recenzja każdego dowodu matematycznego oraz integracja z kanonicznym monolitem 0.20 pozostają otwarte. Wstęp historyczny i wcześniejszy manuskrypt nie zostały zmienione; bez finalnego spisu treści i bez Tomu II.
