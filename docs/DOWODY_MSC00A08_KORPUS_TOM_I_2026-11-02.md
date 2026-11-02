# Tom I — MSC 00A08 i rzeczywisty ciągły korpus książki (2026-11-02)

## Zakres i źródła

- Repozytorium: mojealterego/Ontologia-Liczby-, wyłącznie gałąź main.
- Przed pracą odczytano aktualne docs/POSTEP_TOM_I.md (Git blob c79fe13d9cb735f512331f527e41164d7de04b26), README.md, docs/WYDANIE_20_STATUS.md, taxonomy/TEKST_ZRODLOWY_01.md i taxonomy/index/MSC_LEVEL_I.tsv.
- Zgodnie z mapą po E1-11 następny niezrealizowany wpis poziomu I to **00A08 — Recreational mathematics**, rodzina A, MSC2020, strona 9 źródła, minimum 4 strony. Przeszukanie indeksu GitHub przed zapisem nie wykazało istniejącego rozdziału 00A08; wyniki dotyczyły jedynie taksonomii.
- Wstęp historyczny, oryginalny monolit, rozdziały E0/E1/F i wcześniejsze dokumenty nie zostały nadpisane.

## Zapisane pliki na main — potwierdzone commity

| Plik | Rzeczywisty commit |
| --- | --- |
| manuscript/tom-01/MSC00/00A08_MATEMATYKA_REKREACYJNA.md | e1a51d38de2f00bf87018655ecdf93ce6b16f116; korekta dowodu dwudzielności dc0b373b2133b14aaaa27108055a3d177ba61b4b |
| tests/test_msc00a08_recreation.py | ee8922d01680e8c3bff4c4bc2818985ead4a7dee |
| .github/workflows/tom1-msc00a08.yml | 55930e9dd7dc4f77627ad848495a33441126f546 |
| scripts/assemble_tom1.py | 90340f9bf51eb881755d3cf66d70c20a6cfb3942 |
| tests/test_assemble_tom1.py | bebc091e2e0a75595a579c366fc0cfbc792f04a9 |
| docs/TOM_I_KORPUS_ROBOCZY.md | f0c45abc62e25f0c989ecc81f2e6546e81971afa |
| .github/workflows/tom1-book-working.yml | b151a87c5d0257314a2f6ff49cb53323f5d24aad |

Rozdział 00A08: **12 definicji, 20 twierdzeń z samodzielnymi dowodami, 10 kontrprzykładów, 24 zadania rozwiązane**, 18 556 znaków po korekcie. Zagadnienia: niezmienniki, pokrycia domino, obwód polimina, grafy Eulera i dwudzielne, wzór Eulera, gry bezstronne, Grundy, Hanoi, Josephus, Ramsey R(3,3), granice informacyjne ważeń. Nie należy utożsamiać testów skończonych z formalną recenzją każdego dowodu.

## Faktyczne testy lokalne

1. W niezależnym skrypcie lokalnym wykonano **12/12** kontroli własności matematycznych 00A08, w tym pełne wyliczenie 32 768 dwukolorowań krawędzi K6, 1024 grafów na pięciu wierzchołkach dla lematu o stopniach, rekurencje gier dla n < 200, pokrycia 2×5 i przykład K5. To kontrole wybranych twierdzeń, **nie uruchomienie dokładnego pliku testowego z GitHub**.
2. Skrypt scalania PDF przetestowano lokalnie na dwóch rzeczywistych plikach PDF (2 strony łącznie) oraz sprawdzono, że odrzuca fałszywy oryginał 0.20 przy błędnym SHA-256.
3. Z istniejących, zweryfikowanych osobnych PDF E1-01–E1-10 (wszystkie 10 SHA-256 zgodne z archiwalnym manifestem) i E1-11 (SHA-256 2806d4e9e55956b1e892472f084adcba9e2a9cfd9da646b230c36ff1ae71c379) wykonano **jeden ciągły roboczy PDF z 11 rozdziałami E1** i osobną stroną tytułową: **80 stron A4, 937 498 bajtów, SHA-256 200c5559ab053a207744191c1134ffb067f94581c03c27c52df34a82eb3f2f30**. Zweryfikowano pdfinfo, pdftotext, zawartość E1-06/E1-10/E1-11 oraz obrazy stron 1 i 80. Ten plik jest **lokalnym artefaktem, nie binarium zapisanym na main**.
4. Zapisany na main workflow tom1-book-working.yml ma kompilować **17 pełnych rozdziałów** (5 E0, 11 E1 i 00A08) do jednego roboczego PDF, wraz z manifestem SHA-256 i kontrolą limitu 99 MB. Workflow tom1-msc00a08.yml ma osobno skompilować pełny rozdział 00A08 i uruchomić 20 testów. **Nie potwierdzono zielonego wyniku GitHub Actions ani pełnego PDF 00A08 w chwili zapisu tego protokołu.**

## Ograniczenia i blokady

- **Kanoniczny PDF 0.20** ma według docs/WYDANIE_20_STATUS.md 864 strony i SHA-256 ea888d112cc255856c03cead7428d4f817ad2c692d0e6e6d61f46ae17738dd43. Nie jest obecny binarnie na main. W Bibliotece odnaleziono odrębny ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf, ale autoryzacja nie pozwoliła pobrać jego bajtów do środowiska kompilacji; wcześniejsze dowody wskazują, że to wydanie robocze 764 stron, **nie 0.20**. Nie wolno zastępować nim oryginału.
- Skrypt scripts/assemble_tom1.py ma tryb with-base, który bezwzględnie sprawdza SHA-256 i 864 strony oryginału, zachowuje kolejność jego stron i porównuje tekst wszystkich 33 stron wstępu po scaleniu. Tryb ten **nie został uruchomiony na prawdziwym 0.20**, bo brak jego autoryzowanych bajtów.
- Roboczy korpus 80 stron nie zawiera oryginalnego wstępu historycznego ani dawnych rozdziałów F; nie jest kompletnym Tomem I. W żadnym miejscu nie zadeklarowano integracji z monolitem 0.20.
- **585 stron historycznego bilansu pozostaje bez zmian.** Dawny cel 1222 stron jest nieobowiązkowy. Limit finalnego PDF to < 99 000 000 bajtów.
- Nie tworzono końcowego spisu treści ani Tomu II. Nie przeprowadzono niezależnej recenzji matematycznej wszystkich twierdzeń ani pełnej regresji wszystkich testów repozytorium.

## Następna jednostka według źródłowej taksonomii

**00A09 — Popularization of mathematics**, rodzina A, poziom I, minimum 4 strony. Priorytet równoległy: potwierdzenie zielonego CI 17-rozdziałowego korpusu oraz rzeczywista integracja z oryginałem 0.20 po uzyskaniu autoryzowanego binarium.
