# ONTOLOGIA LICZBY — kontrola rzeczywistego postępu Tomu I

**Data aktualizacji:** 30 października 2026  
**Gałąź:** `main`  
**Zasada redakcyjna:** finalny spis treści dopiero po kompletnym opracowaniu i zamknięciu Tomu I. Taksonomia służy wyłącznie jako wewnętrzna mapa pracy.

## Punkt odniesienia

- Ostatnie udokumentowane wydanie pełnego monolitu: **0.20**, 864 strony ogółem — według rejestru `docs/WYDANIE_20_STATUS.md`. Oryginalny plik binarny wydania 0.20 **nie jest zapisany w repozytorium**.
- Utrzymywany w rejestrze stan części zasadniczej Tomu I: **585 stron**, niezależnie od 80 stron indeksu i 197 stron archiwalnych opracowań MSC2020.
- Cel: **1222 strony rzeczywistej części merytorycznej**, bez dzielenia rozpoczętego punktu lub dowodu.
- Z rejestru wydania 0.19: **31/135** punktów F spełniało ówczesne wymagania objętościowe, **104/135** wymagały rozwinięcia. Nie jest to wynik recenzji naukowej.

## Nowe prace po wydaniu 0.20

| Punkt | Plik źródłowy | Rezultat | Status w manuskrypcie |
| --- | --- | --- | --- |
| F7.1 — Trzy role zera | `manuscript/tom-01/F07/F7.1_UZUPELNIENIE_FORMALNE.md` | Rozszerzenie dowodowe, przykłady, kontrmodele, 6 zadań z rozwiązaniami; samodzielny podgląd PDF: 5 stron, każda ponad 2000 znaków tekstu wyekstrahowanego | **Nie włączono do monolitu 0.20; bez zaliczenia do bilansu 585/1222** |
| F7.2 — Dlaczego zero mnożone przez liczbę daje zero | `manuscript/tom-01/F07/F7.2_UZUPELNIENIE_ALGEBRAICZNE.md` | Uzupełnienie o pierścienie, moduły, półpierścienie, dzielniki zera i 8 zadań z rozwiązaniami; podgląd PDF: 4 strony, każda ponad 2000 znaków tekstu wyekstrahowanego | **Nie włączono do monolitu 0.20; bez zaliczenia do bilansu 585/1222** |
| F7.3 — Dwa problematyczne zapisy: 0/0 i 0⁰ | `manuscript/tom-01/F07/F7.3_UZUPELNIENIE_TEORIA_OPERACJI.md` | Formalizacja dzielenia częściowego, anihilatory, ciągłość, dowody i 10 rozwiązanych zadań; samodzielny PDF: **5 stron A4**, każda ponad 2000 znaków tekstu | **Nie włączono do monolitu 0.20; bez zaliczenia do bilansu 585/1222** |
| F7.4 — Zero a ujemność | `manuscript/tom-01/F07/F7.4_UZUPELNIENIE_PORZADEK_I_ZNAK.md` | Ciała uporządkowane, stożki dodatnie, metryka, afiniczność, torsja oraz 10 zadań z rozwiązaniami; samodzielny PDF: **5 stron A4**, każda ponad 2000 znaków tekstu | **Nie włączono do monolitu 0.20; bez zaliczenia do bilansu 585/1222** |

Opracowania F7.1–F7.4 zostały złożone do samodzielnych podglądów PDF przy użyciu XeLaTeX. Dla F7.3 i F7.4 wykonano lokalne **36/36 pozytywnych kontroli** obejmujących sprawdzenie przykładów algebraicznych, numerycznych i parametrów składu A4; każda z 10 nowych stron zawiera co najmniej 2000 znaków wyekstrahowanego tekstu. **Testy przykładów nie stanowią dowodu wszystkich twierdzeń, niezależnej recenzji naukowej ani integracyjnego testu z wydaniem 0.20**.

## Reguła zaliczania stron

Strony nowego opracowania można doliczyć do Tomu I **dopiero po** scaleniu z rzeczywistym źródłem ostatniego wydania, usunięciu redakcyjnych powtórzeń, powtórnej kompilacji całego monolitu i sprawdzeniu wynikowych stron. Przed tym etapem licznik części merytorycznej pozostaje **585 (według dokumentacji, bez niezależnego potwierdzenia pliku 0.20)**.

## Następny odcinek pracy

Kolejnymi działaniami merytorycznymi są integracja uzupełnień F7.1–F7.4 z właściwym monolitem po uzyskaniu źródła wydania 0.20 oraz rozwijanie punktów F8.1 i kolejnych według sekwencji manuskryptu. Nie tworzyć finalnego spisu treści, nie przechodzić do Tomu II i nie oznaczać żadnego punktu jako zweryfikowany jedynie na podstawie osiągniętej długości.

## Kontrola uzupełnień F7.3–F7.4 (30.10.2026)

- `F7.3`: 5 stron A4; lokalny SHA-256 podglądu PDF: `671d8820b273020808cb9c59fa89a1141514f1dc847e5528efbd3add0cae1e9d`.
- `F7.4`: 5 stron A4; lokalny SHA-256 podglądu PDF: `42ba9a262ef9aa53ed3b469c368f8565ac38aa8997d3f5ed807235105a9a073b`.
- Łącznie po sesjach F7.1–F7.4: **19 stron osobnych podglądów PDF** (5 + 4 + 5 + 5). **Nie jest to wzrost numeracji stron Tomu I.**
- Zarówno binarny monolit 0.20, jak i wynikowy scalony PDF Tomu I pozostają nieobecne na gałęzi `main`. Nie oznaczać integracji jako wykonanej bez odpowiednich artefaktów.

## Opracowanie F8.1 (30 października 2026)

- Źródło: `manuscript/tom-01/F08/F8.1_UZUPELNIENIE_FORMALNE.md`.
- Nieskończoność potencjalna i aktualna: aksjomat nieskończoności ZF, sklejanie prefiksów, diagonalizacja Cantora, lemat Königa, zbieżność i oszacowania błędów.
- Wynik źródłowy: 8 twierdzeń, 12 zadań z rozwiązaniami; lokalny podgląd 5 stron A4, każda ponad 2000 znaków wyekstrahowanego tekstu; 7 lokalnych testów zakończonych wynikiem pozytywnym.
- Brak integracji z monolitem 0.20 i niezależnej recenzji matematycznej. 5 stron **nie doliczono** do deklarowanych 585/1222 stron Tomu I.
- Łącznie z F7.1–F7.4: 24 strony odrębnych podglądów (5+4+5+5+5). Nie są to jeszcze strony scalonej księgi.
- Spis treści zostanie wykonany dopiero po całkowitym ukończeniu Tomu I.


## Opracowania F8.2–F8.3 (30 października 2026)

| Punkt | Plik źródłowy na `main` | Zawartość | Dowody techniczne | Stan integracji |
| --- | --- | --- | --- | --- |
| F8.2 — Zbiory przeliczalne | `manuscript/tom-01/F08/F8.2_UZUPELNIENIE_PRZELICZALNOSC.md` | 9 twierdzeń, 12 zadań rozwiązanych; konstrukcje bijekcji, liczby wymierne, kodowanie par, granice aksjomatu wyboru | 6 testów lokalnych zaliczonych; skorygowano formalne kodowanie par `(z⁻¹(p), q−1)`; po ponownym składzie 4 strony A4, tekst na każdej stronie > 2000 znaków | Nie scalono z monolitem 0.20 |
| F8.3 — Przekątna Cantora | `manuscript/tom-01/F08/F8.3_UZUPELNIENIE_DIAGONALIZACJA.md` | 9 twierdzeń, 12 zadań rozwiązanych; lemat diagonalny, kod trójkowy, przekroje wymierne, równoliczność przestrzeni funkcji, granice obliczalności | 10 testów lokalnych zaliczonych; kompilacja XeLaTeX, 4 strony A4; każda > 2000 znaków tekstu, blokom tekstowym nie brakuje obszaru strony | Nie scalono z monolitem 0.20 |

**Lokalna kontrola tej partii:** 16/16 testów pozytywnych; testy numeryczne i strukturalne nie zastępują matematycznej recenzji wszystkich dowodów. Formatowanie i końcowy przydział stron mogą się zmienić po integracji. Licznik monolitu pozostaje **585/1222 według rejestru, bez niezależnego odczytu binarnego wydania 0.20**. Nie dodawać stron dodatków do tego bilansu i nie generować końcowego spisu treści przed ukończeniem Tomu I.

**Następny punkt:** F8.4 „Hipoteza continuum i niezależność” — weryfikować rozróżnienie ZF/ZFC, niezależność względną i zakres twierdzeń Gödla–Cohena, bez powtarzania gotowego fragmentu.


## Opracowania F8.4–F8.5 (30 października 2026)

| Punkt | Ścieżka źródłowa | Wynik merytoryczny | Testy lokalne | Integracja |
| --- | --- | --- | --- | --- |
| F8.4 — Hipoteza continuum i niezależność | `manuscript/tom-01/F08/F8.4_UZUPELNIENIE_NIEZALEZNOSC.md` | 7 twierdzeń z rozróżnieniem wyników własnych i literaturowych; 12 zadań z rozwiązaniami; ZFC, konstruktybilność, forcing, granice niezależności | Podgląd PDF A4: **4 strony**; 5/5 testów przykładów; każda strona powyżej 2000 znaków, bez przekroczeń marginesów | **Niescalony** z monolitem 0.20 |
| F8.5 — Znaczenie ontologiczne | `manuscript/tom-01/F08/F8.5_UZUPELNIENIE_MODELE_ONTOLOGIA.md` | 11 twierdzeń/lematów, 12 zadań z rozwiązaniami; izomorfizmy, PA pierwszego i drugiego rzędu, paradoks Skolema, formalna rekurencja i status ontologiczny | Podgląd PDF A4: **5 stron**; 4/4 testów przykładów; każda strona powyżej 2000 znaków, bez przekroczeń marginesów | **Niescalony** z monolitem 0.20 |

**Przegląd ograniczeń:** testy lokalne są testami przykładów i składu, nie dowodzą twierdzeń o niezależności CH ani całkowitej poprawności wywodów z teorii modeli. Formalna recenzja naukowa i test integracyjny monolitu 0.20 **nie zostały wykonane**. Źródła zapisano bez modyfikacji wstępu historycznego.

**Rejestr materiału niezintegrowanego F7.1–F8.5:** 41 stron oddzielnych PDF (5+4+5+5+5+4+4+4+5), bez zaliczenia do fizycznej numeracji Tomu I. Obowiązujący udokumentowany bilans Tomu I pozostaje **585/1222**, ponieważ brak źródła i binarnego monolitu wydania 0.20 w repozytorium. Finalny spis treści sporządzić dopiero po ukończeniu tomu.
