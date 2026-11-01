# AUDYT ZGODNOŚCI TAKSONOMICZNEJ — Tom I (stan początkowy, 2026-11-01)

## Zakres i podstawa
Odczytano na gałęzi main: README.md, docs/SPIS_TRESCI_NADRZEDNY.md, docs/WYDANIE_20_STATUS.md, taxonomy/TEKST_ZRODLOWY_01.md oraz docs/POSTEP_TOM_I.md. To audyt metadanych i mapowania, **nie** weryfikacja całego 637-stronicowego PDF ani wszystkich rozdziałów.

## Reguły obowiązujące
1. Wstęp historyczny jest chroniony i nie podlega zmianom.
2. O kolejności opracowań decyduje taksonomia, nie numery F ani kolejność powstawania suplementów.
3. Jednostka uznana za ukończoną musi mieć jawny kod taksonomiczny, poziom, minimalną objętość, udokumentowany zakres, wynik kompilacji i dowód rzeczywistej paginacji w docelowym składzie.
4. Minima: I 4, II 11, III 44, IV 111, V 333, VI 1444 stron na punkt; nie liczyć stron pustych, sztucznie dzielonych ani nawigacyjnych.
5. 585/1222 pozostaje wartością historycznego bilansu; suplementów nie doliczać bez integracji z monolitem 0.20.
6. Spis treści finalny dopiero po zamknięciu Tomu I. Propozycja tytułu „Ontologia Liczby i Geometrii” pozostaje niezatwierdzona.

## Pierwsze rozpoznane mapowania (wstępne, wymagają kontroli zawartości)
| Jednostka istniejąca | Kandydat taksonomiczny | Poziom | Minimum | Ocena |
|---|---|---:|---:|---|
| F27.2 — definicja granicy ciągu | E2-06 — ciągi | II | 11 | tematycznie zgodne, NIE potwierdzono pełnego punktu |
| F27.3 — granica i ogony | E2-06 — ciągi | II | 11 | tematycznie zgodne, NIE potwierdzono pełnego punktu |
| F28.1 — iloraz różnicowy | E2-13 — pochodna funkcji | II | 11 | tematycznie zgodne, NIE potwierdzono pełnego punktu |
| F28.2 — ekstrema i optymalizacja | E2-13 — pochodna funkcji / MA-08 — optymalizacja | II / III | 11 / 44 | treść przekrojowa; podzielić według faktycznego poziomu, nie liczyć podwójnie |
| F29.1 — sumy prostokątów i całka (zapowiedziany) | E2-14 — całki | II | 11 | NIE opracowano w tym audycie |

**Ważne:** oznaczenia E2 są autorską mapą dydaktyczną, nie kodami MSC2020. Przypisanie do konkretnego MSC wymaga osobnej weryfikacji.

## Ustalenia wydawnicze
- docs/WYDANIE_20_STATUS.md opisuje wydanie 0.20 jako PDF 864 stron, w tym 80 stron indeksu i 197 stron zachowanego bloku MSC. Pliki binarne nie są opublikowane w repo.
- docs/SPIS_TRESCI_NADRZEDNY.md stwierdza 135 punktów F w wydaniu 0.19, z czego 31 miało spełniać minimum, a 104 wymagały rozbudowy. To **deklaracja wcześniejszego rejestru**, nie wynik ponownego przeliczenia.
- Taksonomia źródłowa rozróżnia 6006 szczegółowych kodów, 534 nagłówki grupowe i 63 kategorie główne. Nie należy utożsamiać tego z liczbą gotowych rozdziałów.

## Rejestr brakujących dowodów
- [ ] Odczytać wszystkie wpisy 6006 kodów i 514 autorskich podtematów; potwierdzić integralność eksportu.
- [ ] Powiązać każdy istniejący punkt F z kodem dydaktycznym i — osobno — MSC, z oceną zakresu treści.
- [ ] Sprawdzić deklarowane 31/135 punktów z rzeczywistymi stronami i dowodami.
- [ ] Odzyskać lub odtworzyć kanoniczne źródła monolitu 0.20 i przeprowadzić skład całego Tomu I.
- [ ] Dopiero po weryfikacji podnieść licznik stron.

## Kryterium dalszej pracy
Najpierw audyt od E0-01 i weryfikacja pokrycia przez istniejące rozdziały. Materiały F27–F28 są kandydatami do wykorzystania w późniejszych punktach, nie dowodem ukończenia E2-06 lub E2-13. Żaden istniejący plik nie został zmieniony w ramach niniejszego audytu.
