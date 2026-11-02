# Protokół dowodowy — MSC 97C30 i scalony podgląd Tomu I (2026-11-02)

## Identyfikacja i zakres

Repozytorium: mojealterego/Ontologia-Liczby-, wyłącznie gałąź main. Przed zmianami odczytano aktualny rejestr docs/POSTEP_TOM_I.md (Git blob 80ae8e08072e843d0bf2ea7203673ce7244452da), workflow książki, rozdział 97C20 i indeks taxonomy/index/MSC_LEVEL_I.tsv (blob fe98b61b624e014eede902be18831d4c05f54c00). Następną nieopracowaną pozycją jest 97C30, poziom I, strona 10 taksonomii, minimum cztery strony.

## Zapisane na main

- [Manuskrypt 97C30](../manuscript/tom-01/MSC97/97C30_PROCESY_POZNAWCZE_I_TEORIE_UCZENIA.md), commit [0d03fb7](https://github.com/mojealterego/Ontologia-Liczby-/commit/0d03fb719cec4a47005d3280030dfa5cf8a50b87), blob a466a83b9c694d7434bd39daa32384a856e527e7, 17 250 znaków: **15 definicji, 16 twierdzeń z dowodami, 10 kontrprzykładów, 20 zadań z rozwiązaniami**.
- [Testy](../tests/test_msc97c30_cognition.py), commit [ec2f4be](https://github.com/mojealterego/Ontologia-Liczby-/commit/ec2f4be3f2a4716cee992c91820af05db772f02e), blob 81f5cb9b4b438042ad977a5ee929f01a952816a0.
- [Workflow rozdziału](../.github/workflows/tom1-msc97c30.yml), commit [f36c769](https://github.com/mojealterego/Ontologia-Liczby-/commit/f36c769713e8ab8b6e5b8b33b816427a0a85d603).
- [Workflow korpusu](../.github/workflows/tom1-book-working.yml), rozszerzony do **20** rozdziałów, commit [5fdc33e](https://github.com/mojealterego/Ontologia-Liczby-/commit/5fdc33e1b6e5f22846301fd2f6a94ac7c2939a0f).
- [Opis korpusu](TOM_I_KORPUS_ROBOCZY.md), commit [2201568](https://github.com/mojealterego/Ontologia-Liczby-/commit/220156828f68c5cbdb890e7c31ef8a33e9b9a795).
- [Skrypt integracji przekazanego monolitu](../scripts/assemble_supplied_monolith.py), commit [6073ef7](https://github.com/mojealterego/Ontologia-Liczby-/commit/6073ef7f09d21bf1d085cfbafb15fae9240b91f2), blob fc0f79db2d4720f1b8b30bd9dcaa447f2a8ac6cb. Skrypt wymaga dokładnego SHA i 629 stron, wykrywa duplikaty kodów, sprawdza niezmienność tekstu wszystkich stron i renderów wybranych stron.

## Weryfikacja lokalna

- Dokładny testowy plik Python zgodny z blob 81f5cb9b4b438042ad977a5ee929f01a952816a0: **28/28 testów unittest OK**, w tym dokładne rachunki wymierne, wyczerpująca kontrola domknięć i ideałów dla czterech wierzchołków, Bayes, Markow, logistyka, entropia i kontrprzykład zachłanny.
- Pełny manuskrypt zgodny z blob a466a83b9c694d7434bd39daa32384a856e527e7: Pandoc + XeLaTeX **success**; **6 stron A4**, **79 679 B**, SHA-256 PDF d1342701ca10f9d0a4003dab99ca563e18c2e4516474fc0f971cd8f87d7cc7c9; SHA-256 źródła cc63fa0d81f77b7fc5d95b6cb21e7453c52372c1bbde5012e98cfee62f46b04a. Strony zawierają tekst; znaczniki T16, K10 i Z20 obecne w PDF. Pierwszą stronę sprawdzono wizualnie.
- Dostarczony przez autora monolit ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT-2.pdf: **629 stron**, **8 006 168 B**, SHA-256 cd2e5e9ef0adefc3344ff8a7a1bcaa4befd2e1b85b4a711a36c3a0c179cb1309.
- Lokalnie złożono **641-stronicowy niekanoniczny podgląd**: 629 stron oryginału + pełne 97C20 (6 stron, SHA-256 412940731109a0972fd453fd3d95631bc0cbed446568865196cc74a11492f056) + pełne 97C30 (6 stron). Wynik: **7 724 099 B**, SHA-256 dbbe612b1a32bf4af53959ff8ea8d028c1e271936ab19b7aa7e8008b24621151. Porównano SHA-256 tekstu **wszystkich 629 oryginalnych stron** oraz renderowanie stron **1, 2, 33, 34, 629**: zgodność. W źródłowym 629-stronicowym monolicie nie znaleziono znaczników 97C20 ani 97C30.
- Ponownie uruchomiono skrypt integracyjny na tym samym zestawie danych; przeszedł wszystkie kontrole. Nowy wynik może mieć odmienny SHA-256 z powodu innych metadanych PDF, ale zachowuje te same strony i ich weryfikację.

## Granice dowodów i blokady

- **CI rozdziału potwierdzone:** [run 41438424204](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41438424204), zakończony **success** na commit f36c769713e8ab8b6e5b8b33b816427a0a85d603. Log zadania 125253930609 potwierdza **28/28 testów** i poprawną kompilację pełnego źródła; artefakt PDF: ID **13137857119**. [Książka 20 rozdziałów, run 41438448699](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41438448699) **success**, job 125254013553: **20 pełnych rozdziałów, 140 stron, 1 743 342 B**, artefakt **13137322247**; w logach łącznie **97/97 testów** (11 + 20 + 18 + 20 + 28). Jest to osobny korpus roboczy **bez** 629-stronicowego źródła i bez kanonicznego 0.20.
- **Niekanoniczny monolit 629 stron** nie jest binarnie tożsamy z wydaniem 0.20 (według wcześniejszej dokumentacji 864 strony, SHA-256 ea888d112cc255856c03cead7428d4f817ad2c692d0e6e6d61f46ae17738dd43). Wersja 641 stron jest *podglądem roboczym*, nie oficjalną integracją 0.20. Jej PDF nie został wysłany do repozytorium.
- Formalna recenzja wszystkich dowodów i empiryczna walidacja modeli dydaktycznych pozostają otwarte. Testy skończone nie stanowią ich zamiennika.
- Historyczny bilans **585 stron** niezmieniony. Dawne 1222 stron nie jest obowiązkowym limitem. Końcowy PDF tomu musi mieć **<99 000 000 B**. Wstęp historyczny i wszystkie poprzednie strony bez ingerencji. Bez końcowego spisu treści i bez Tomu II.

**Następny punkt taksonomii:** MSC 97D40 — *Mathematics teaching methods and classroom techniques*.
