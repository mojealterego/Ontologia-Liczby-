# Tom I — protokół MSC 97D40, rozszerzenie III-A (2026-11-02)

## Zmiany zapisane na gałęzi main

- Uzupełniono brakujący wpis **97D40, poziom III** w [indeksie MSC](../taxonomy/index/MSC_LEVEL_III.tsv), commit [785807ff](https://github.com/mojealterego/Ontologia-Liczby-/commit/785807ff3058dbcdd93b54b74acc4d4ab446926d). Źródło pierwotne: [MSC2020, s. 118](https://www.impan.pl/wydawnictwa/dla-autorow/msc2020.pdf), hasło „97D40 Mathematics teaching methods and classroom techniques”. Przed poprawką indeks poziomu III pomijał kod 97D40 między 97D30 a 97D50.
- Poprawiono oznaczenie poziomu rozdziału z I na **III** i dodano informację, że to wersja częściowa (minimum projektu: **44 strony**), commit [cc04cd30](https://github.com/mojealterego/Ontologia-Liczby-/commit/cc04cd303142c6eb5b3de21469acedb7ef3eb6ec).
- Dodano sekcję **III-A** do [MSC 97D40](../manuscript/tom-01/MSC97/97D40_METODY_NAUCZANIA_MATEMATYKI.md), commit [0f0f53ec](https://github.com/mojealterego/Ontologia-Liczby-/commit/0f0f53ec02a15a88e96c4ada611690627f6e85ec): D16–D19, T17–T24 z dowodami, K11–K14 i Z21–Z30 z rozwiązaniami. Matematyka: funkcja ważonego pokrycia, submodularność, gwarancja zachłanna dla ograniczenia liczby zadań, informacyjna granica testu binarnego, liniowość wartości oczekiwanej. Dotychczasowe definicje, twierdzenia i zadania pozostały w rozdziale.
- Dodano [10 testów rozszerzenia](../tests/test_msc97d40_advanced.py), commit [6cd33c17](https://github.com/mojealterego/Ontologia-Liczby-/commit/6cd33c17aec53a0ba0c77d24361b84c3b8b1ab8c). Dostosowano workflow książki do **21 rozdziałów** (commit [98c320d1](https://github.com/mojealterego/Ontologia-Liczby-/commit/98c320d1eb6fd93fc553be6a5d808959aef10c3e)), dodano [workflow pełnego PDF 97D40](../.github/workflows/tom1-msc97d40.yml), commit [1fc8d066](https://github.com/mojealterego/Ontologia-Liczby-/commit/1fc8d0665dafcdadd0ff64ad267a04ede9526ded). Oba workflow uruchamiają także nowe testy: commity [19b92265](https://github.com/mojealterego/Ontologia-Liczby-/commit/19b9226558132220753ebd9c11e2f28a35ad3f56) i [bb4ce0f0](https://github.com/mojealterego/Ontologia-Liczby-/commit/bb4ce0f0cac3397f64a5d25bdbe75ea39e596b7a).

## Wykonane kontrole lokalne

- **17/17 testów bazowych** MSC 97D40 zakończonych wynikiem OK. Zweryfikowano dokładną zgodność lokalnego pliku testowego z blobem na `main`: Git blob SHA-1 `d669beb6d57ac20ac3359cc4fe0aef38495aa6d8`.
- **3436 niezależnych kontroli** rozszerzenia III-A: pełne przeszukanie rodzin 3 zadań i 3 umiejętności dla dwóch systemów wag, sprawdzenie nierówności submodularności, granicy kodowej i kontrprzykładów. Wszystkie zakończone poprawnie. To **nie** jest dowód formalny wszystkich możliwych przypadków, lecz weryfikacja rachunkowa.
- Lokalnie skompilowano ReportLab **2-stronicowy PDF podglądu rozszerzenia III-A** (nie pełnego rozdziału). Następnie połączono go z wcześniejszym 641-stronicowym podglądem (629 oryginalnych stron + 97C20 + 97C30) do **643-stronicowego PDF niekanonicznego**.
- Wynik: 643 strony, **8 149 313 bajtów**, SHA-256 `3d10e3dcc6650c120272e1e5c6a2e0e31a2fce4a787fcd26742820a5984b2868`. Zachowano **tekst wszystkich 629 stron** oryginalnej kopii, zgodność renderów stron 1, 2, 33, 34, 629, **4 odsyłacze** i łącznie **589 zakładek**. Wersja źródłowa 629 stron: SHA-256 `cd2e5e9ef0adefc3344ff8a7a1bcaa4befd2e1b85b4a711a36c3a0c179cb1309`.
- **Nie zaliczono** 2 stron rozszerzenia do historycznych 585 stron części zasadniczej; to jedynie dodatkowy podgląd. Końcowego spisu treści nie sporządzono.

## Otwarte kryteria

- Odbiór pełnego PDF rozdziału 97D40 z aktualnego Markdown w GitHub Actions oraz wynik CI workflow 21-rozdziałowego — do potwierdzenia osobnym przebiegiem.
- Uzupełnienie MSC 97D40 do co najmniej **44 stron** poziomu III i redakcja jednolitego składu; bieżący rozdział pozostaje **częściowy**.
- Wydanie 0.20 (według dokumentacji 864 strony i odmienna suma SHA-256) **nie jest** tym samym co udostępniona kopia 629 stron. Nie deklarowano integracji z 0.20. Historyczny wstęp i pierwotne strony nie były zmieniane.
- Pełna recenzja matematyczna i walidacja empiryczna modeli dydaktycznych pozostają otwarte. W szczególności gwarancja zachłanna dotyczy ograniczenia liczby zadań, a nie arbitralnego budżetu czasu.

**Granice wydawnicze:** bez Tomu II, bez końcowego spisu treści, 585 stron w rejestrze bez zmian, 1222 stron nie jest obowiązkowym celem, limit końcowego PDF poniżej 99 MB.


## Aneks odbiorczy: pełny PDF i 647-stronicowa książka (2026-11-02)

- Lokalnie wykonano **27/27 testów** na plikach dokładnie zgodnych z blobami `main`: bazowy `d669beb6d57ac20ac3359cc4fe0aef38495aa6d8` (17 testów) i rozszerzony `3c15046856534c0126fae1572b922a1db6396e79` (10 testów). Dodatkowe 3436 niezależnych kontroli zachowuje odrębny status.
- [GitHub Actions — pełny rozdział 97D40, run 41445051738](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41445051738): **success**, commit `bb4ce0f0cac3397f64a5d25bdbe75ea39e596b7a`, artefakt **13141781622**. Z pobranego artefaktu odczytano **6 stron, 83 793 B**, SHA-256 `6f5392d53c5f6ef0ad6c45584a58295629108edb214f40ba97170d78d54be20a`; SHA-256 źródła Markdown w artefakcie: `d4c4209c97f75888032c56b71141cf939cfb73fae5d575024c4644776c3c3bd4`.
- **Rzeczywista integracja pełnego rozdziału**: sklonowano wcześniejszy podgląd 641 stron (zawierający niezmienione 629 stron przekazanego monolitu i pełne 97C20/97C30), dołączono sześć stron pełnego PDF 97D40 z CI, zachowując zakładki i odsyłacze za pomocą `pypdf.PdfWriter.clone_document_from_reader` i `append`. Wynik **647 stron, 8 187 625 B**, SHA-256 `d6bc2d8b3964b05ac598f8541d79f38b1ba967fd0178784b9866cce4e07288d7`. Zweryfikowano zgodność tekstową **629/629 stron** z oryginałem, **641/641 stron** z poprzednim podglądem, **6/6 stron** z artefaktem CI, zgodność pięciu renderów źródłowych, **589 zakładek**, **4 oryginalne odsyłacze**, brak pustych stron w nowej części i limit 99 MB.
- **Nie jest to kanoniczne 0.20**: oryginał 629 stron różni się od opisanego w repo wydania 0.20 (864 strony). Nowe strony nie są doliczane do historycznych 585.
- [CI korpusu 21 rozdziałów, run 41445046049](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41445046049) **failure** po pomyślnych testach i złożeniu 146 stron: końcowy `pdf_bounds.py` wykrył **jedno słowo poza marginesem bezpieczeństwa**. Workflow skorygowano, dodając `--repair` przed końcową walidacją, commit [601c8bdf](https://github.com/mojealterego/Ontologia-Liczby-/commit/601c8bdf7600f7f69f8030c342179b9ac0580aa9). Zielony odbiór tego poprawionego workflow wymaga osobnego potwierdzenia.

- **Korekta CI rozdziału:** log run 41445051738 potwierdza wykonanie tylko **17 bazowych** testów (pełny PDF przeszedł kompilację); wcześniejsza konfiguracja nie wywoływała jeszcze 10 testów rozszerzenia. Naprawiono krok testowy workflow, aby uruchamiał **oba** zestawy 17+10, commit [568e303e](https://github.com/mojealterego/Ontologia-Liczby-/commit/568e303ece25e3a52f75c91ef8edbbf49e700b8d). **27/27 lokalnie potwierdzone**; zielony CI po tej korekcie wymaga osobnego odbioru.
