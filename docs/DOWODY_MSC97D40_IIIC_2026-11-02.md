# Protokół wykonawczy MSC 97D40 III-B/III-C — 2026-11-02

## Zmiany na main

- [III-B — 67794720](https://github.com/mojealterego/Ontologia-Liczby-/commit/677947201bf12aa22725a6de099110940aa38d14): D20–D27, T25–T32 z dowodami, K15–K18, Z31–Z40.
- [III-C — f500ebce](https://github.com/mojealterego/Ontologia-Liczby-/commit/f500ebcebfc96510759758bf5eda0792ad6b3d63): D28–D36, T33–T42 z dowodami, K19–K22, Z41–Z50.
- [Korekta — 39e10a5b](https://github.com/mojealterego/Ontologia-Liczby-/commit/39e10a5b9a1e2ecaae1c996a78f2cbc2a7529074): D35 doprecyzowano dla grup o zerowej masie; K21 poprawiono na próbki strat z podaniem wariancji empirycznych.
- [Testy III-B — 1a8e7aa5](https://github.com/mojealterego/Ontologia-Liczby-/commit/1a8e7aa502a735eaec7783022a2897a1715870b1): 7 testów, blob SHA-1 9a4fdd2c1eadc7a187ad70cfb0ac515c7f4792b9.
- [Testy III-C — 1754c644](https://github.com/mojealterego/Ontologia-Liczby-/commit/1754c644a4d1897b65b74a8e2346a70759b361b2): 10 testów, blob SHA-1 575c82389c34362c1eb579295ad6bb992db9eea5.
- [CI rozdziału — ca408fbb](https://github.com/mojealterego/Ontologia-Liczby-/commit/ca408fbb3ee490bd040fbc521ec7dd4e8338ad1f), [CI korpusu — a4e332aa](https://github.com/mojealterego/Ontologia-Liczby-/commit/a4e332aa269d4a36836f6bb2281bf318d2522cca): dodano testy III-C; wcześniej dołączono III-B. [Próg stron — f2dd5e5b](https://github.com/mojealterego/Ontologia-Liczby-/commit/f2dd5e5b148f11a085a73aa47eb75e66d004fccd): minimum 10 stron w CI.
- [Assembler — 20918fb5](https://github.com/mojealterego/Ontologia-Liczby-/commit/20918fb548ed5a608ea2aece7a445a70f1e8fabd): scripts/assemble_supplied_monolith.py obsługuje 2 lub 3 suplementy w kolejności 97C20, 97C30, 97D40.

## Dowody lokalne

1. Python unittest: **17/17 OK** (7 testów III-B i 10 testów III-C). Zweryfikowano zgodność blob SHA-1 lokalnych testów z dokładnymi blobami main. Zakres: entropia, wartość informacji, TV, ryzyko, paradoks agregacji i zależność obserwacji.
2. Pandoc/XeLaTeX: pełne sekcje III-B **3 strony A4** i III-C **3 strony A4**. Zero słów poza marginesem 5 pt. Kompilacja dotyczy lokalnej transkrypcji treści sekcji; **nie** jest bezpośrednią kompilacją całego aktualnego pliku Markdown z main.
3. Pełny rozdział MSC 97D40: kompozycja poprzednich 6 stron i dwóch nowych sekcji po 3 strony, **12 stron**, SHA-256 **5db5484dc39192b09e9edf6f0589bcc3cf6ec4fa4338aa6185d4560aa4b00e26**.
4. Książka robocza: oryginalny monolit **629 stron**, MSC 97C20 **6**, MSC 97C30 **6**, MSC 97D40 **12**. Razem **653 strony**, **8 312 064 bajty**, SHA-256 **3302fae91920547116b0c537d0000f535d7bd6b7a022c71cdfc1606bc8819955**. Złożono przez pypdf 5.9.0. Sprawdzono tekstową identyczność wszystkich 629 stron oryginału i wszystkich 647 stron poprzedniej książki roboczej, pięć próbek identycznych renderów, zachowanie 4 odsyłaczy PDF i 589 zakładek. Strona 1 to okładka graficzna bez warstwy tekstowej; pozostałe strony zawierają tekst.
5. Oryginał 629 stron: SHA-256 **cd2e5e9ef0adefc3344ff8a7a1bcaa4befd2e1b85b4a711a36c3a0c179cb1309**. Kanoniczne wydanie 0.20 według dokumentacji: **864 strony**, SHA-256 **ea888d112cc255856c03cead7428d4f817ad2c692d0e6e6d61f46ae17738dd43**. Nie jest to ten sam plik.
6. Rozmiar PDF mieści się w ścisłym limicie **<99 000 000 bajtów**.

## Status

- **Zaimplementowane:** źródłowe III-B i III-C, testy, workflow, trzy-suplementowy assembler.
- **Przetestowane lokalnie:** 17/17 testów na dokładnych blobach main, kompilacja obu nowych sekcji, kontrola integralności 653-stronicowej książki.
- **Niepotwierdzone:** zielony przebieg GitHub Actions po ostatnich commitach; kompilacja całego aktualnego pliku Markdown z dokładnego HEAD; pełna niezależna recenzja matematyczna.
- **Niezamknięte:** poziom III wymaga **co najmniej 44 stron**, aktualny lokalny rozdział ma **12 stron**. Brak binarnego wydania 0.20 blokuje kanoniczną integrację. Historyczne **585 stron pozostaje bez zmian**. Bez końcowego spisu treści i bez Tomu II.

## Reprodukcja

Uruchomienie skryptu scripts/assemble_supplied_monolith.py z argumentami: --base (oryginalny PDF 629 stron), kolejno --chapter (97C20, 97C30, 97D40), --output (wynik PDF), --manifest (wynik JSON). Wymagany oryginalny SHA-256 jest sprawdzany przez skrypt. Nie jest to wydanie kanoniczne.
