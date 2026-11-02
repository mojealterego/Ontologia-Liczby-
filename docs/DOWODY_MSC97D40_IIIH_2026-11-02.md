# Dowody MSC 97D40 III-H — 2026-11-02

## Zakres zmian na `main`

- Nowy rozdział: `manuscript/tom-01/MSC97/97D40_IIIH_PRZYDZIAL_I_SPRAWIEDLIWOSC.md`, commit `dcf8b86a0a6406d4ccc888b34b67dc11d62f2c0a`. Zawiera D75–D85 (11 definicji), T85–T96 (12 twierdzeń z dowodami), K45–K52 (8 kontrprzykładów) i Z109–Z128 (20 rozwiązanych zadań). Nie nadpisano wcześniejszych plików manuskryptu.
- Nowe testy: `tests/test_msc97d40_matching.py`, commit `fd8c5cd7ea3c641b078aa77fc9d58144bb818eca`. Sprawdzają wyczerpująco skończone grafy dwudzielne, uogólnienie Halla z pojemnościami, monotoniczność, EF1, minimalną nierównowagę i dolne ograniczenie wąskiego gardła.
- Workflow: `.github/workflows/tom1-msc97d40.yml`, commit `1b683a9f4c27c362f083e01fb02233db63a8228e`. Dodano test III-H, źródło III-H do pełnej kompilacji Pandoc oraz znaczniki `T96` i `Z128`.

## Weryfikacja lokalna

- `python -m unittest discover -s /mnt/data/ontologia_iii_h -p 'test_msc97d40_*.py' -v`: **22/22 testów OK**; obejmuje testy III-F (6), III-G (7), III-H (9). Nie jest to pełny zestaw wszystkich testów repozytorium.
- Test III-H enumeruje wszystkie grafy dwudzielne dla `0 <= |U|,|R| <= 3` oraz wszystkie `3^3` wektory pojemności dla grafów `3x3`; porównuje kryterium Halla z niezależną enumeracją dopuszczalnych przydziałów.
- Kompilacja lokalna `pandoc --pdf-engine=xelatex`: **2-stronicowy A4 podgląd wybranych dowodów III-H**, niepełny względem manuskryptu. Plik `ONTOLOGIA_MSC97D40_IIIH_PODGLAD_DOWODOW.pdf`: **59 618 B**, SHA-256 `4ed5ba8540fd57aa209de7c732a4578682a62b6f4170e90533552937f6e407f8`. Obie strony wyrenderowano i obejrzano.
- Lokalny scalony podgląd: **663 strony, 8 067 235 B**, SHA-256 `0488748f4c92149b38af4766c589136d49a3ed45a13d4cec6e9b02411cf81ff1`. Składa się z **661 stron wcześniejszego roboczego PDF** i **2 stron podglądu III-H**. Porównano tekst **661/661** wcześniejszych stron oraz **2/2** dodanych stron; zachowano **589 zakładek** i **4/4** oryginalne odsyłacze (dwa wewnętrzne odtworzono jako funkcjonalne odsyłacze do tych samych stron i współrzędnych).
- Plik manifestu lokalnego: `ONTOLOGIA_TOM_I_IIIH_MANIFEST.json`.

## Ograniczenia i warunki odbioru

- **Niepotwierdzone:** nowy przebieg GitHub Actions po commicie workflow, pełny skład źródeł MSC 97D40 z III-H w CI, niezależna recenzja wszystkich dowodów.
- **Niespełnione:** minimum **44 stron** MSC 97D40 na poziomie III; dokładnej liczby stron po pełnej kompilacji III-G i III-H jeszcze nie ustalono.
- **Blokada kanoniczna:** nie uzyskano binarnego monolitu **0.20**, opisanego jako 864-stronicowy. PDF 663-stronicowy jest **niekanonicznym podglądem roboczym**; historyczne **585 stron pozostaje bez zmian**, a 1222 strony nie są obowiązkowe.
- Limit rozmiaru końcowego PDF: **mniej niż 99 000 000 bajtów**. Nie tworzono końcowego spisu treści, nie rozpoczęto Tomu II, nie modyfikowano historycznego wstępu.
