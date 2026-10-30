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


**Weryfikacja odtwarzalna F8.4–F8.5:** dodano `tests/test_f84_f85.py` na `main` (9 testów jednostkowych przykładów). Uruchomienie lokalne: `python -m pytest -q tests/test_f84_f85.py` po skopiowaniu źródeł do repozytorium; przed publikacją pliku testowego równoważny lokalny zestaw dał **9/9 zaliczonych**. Testy nie dowodzą niezależności CH ani pełnej poprawności filozoficznych interpretacji.


## Opracowania F9.1–F9.2 (30 października 2026)

| Punkt | Plik źródłowy na `main` | Nowa zawartość | Stan |
| --- | --- | --- | --- |
| **F9.1 — Co znaczy policzyć?** | `manuscript/tom-01/F09/F9.1_UZUPELNIENIE_LICZENIE_I_LICZEBNOSC.md` | 10 twierdzeń, 12 zadań z rozwiązaniami; bijekcje i niezmienniczość liczebności, sumowanie po włóknach, iloczyn kartezjański, zasada podwójnego liczenia, włączenia i wyłączenia, współczynniki dwumianowe | Źródło zapisane na `main`; osobny podgląd PDF A4, **4 strony**; **brak integracji** z monolitem |
| **F9.2 — Indukcja i rekurencja** | `manuscript/tom-01/F09/F9.2_UZUPELNIENIE_INDUKCJA_I_REKURENCJA.md` | 10 twierdzeń, 12 zadań z rozwiązaniami; twierdzenie o rekurencji, prawa dodawania i mnożenia, silna indukcja, algorytm Euklidesa, niezmienniki Fibonacciego i szybkie potęgowanie | Źródło zapisane na `main`; osobny podgląd PDF A4, **4 strony**; **brak integracji** z monolitem |

**Kontrole lokalne:** 17/17 testów obliczeniowych zaliczonych (`python -m unittest discover -s tests -p test_f91_f92.py -v` w odrębnym katalogu roboczym). Sprawdzono małe skończone przypadki zasad liczenia, kombinatoryki, działań rekurencyjnych, NWD i tożsamości Fibonacciego. Testy te **nie dowodzą poprawności wszystkich twierdzeń matematycznych**.

**Skład:** XeLaTeX/Pandoc, dwa dokumenty A4 po 4 strony, bez wykrytego wychodzenia bloków tekstu poza strony. W obu PDF każda strona ma ponad 2000 wyekstrahowanych znaków. Kontrolne SHA-256 plików podglądowych:
- F9.1: `9bf265a32e2661963aecea6d55a6ba37dbbc4d6554f17754aab34670c7bca992`;
- F9.2: `6b6e22ee19f1b2c86f9ef992882a6c08e6d76262b536310dada2a267ab38c915`.

**Bilans dodatków:** 41 stron wcześniej udokumentowanych od F7.1 do F8.5 + 8 stron nowych podglądów F9.1–F9.2 = **49 stron odrębnych uzupełnień PDF**. Nie jest to objętość scalonego Tomu I. Udokumentowany bilans **585/1222** pozostaje niezmieniony do chwili rzeczywistej integracji i ponownej kompilacji monolitu 0.20.

**Następny punkt do opracowania:** F9.3 „Odliczanie a dowód”. Finalny spis treści wykonać dopiero po całkowitym ukończeniu i finalnym składzie Tomu I.


## Opracowanie F9.3 — „Odliczanie a dowód” (30 października 2026)

- **Źródło na `main`:** `manuscript/tom-01/F09/F9.3_UZUPELNIENIE_ODLICZANIE_A_DOWOD.md`, commit `0206b58f029fd2733202656657b8aeb7472f31af`. Ponowny odczyt przez GitHub potwierdził długość 15 710 znaków i skrót kontrolny FNV-1a UTF-16 `029ea2cb`, zgodny z lokalnym źródłem podglądu.
- **Treść:** dwie definicje (protokół empiryczny i rozróżnienie spełniania/dowodliwości), dziesięć twierdzeń z uzasadnieniami, pięć kontrprzykładów i dwanaście rozwiązanych zadań. Rozróżniono dowód ogólny od próby empirycznej, prawdę w modelu od konsekwencji teorii, zachowanie formuł przez izomorfizm, rozstrzygalność weryfikacji dowodu od rozstrzygalności zdań oraz zakres zupełności `R` względem `Q`.
- **Testy na `main`:** `tests/test_f93.py`, pierwotny commit `e15dd971c2686f78b17624ce4974e619c1f3da25`, poprawka ścieżki źródła `a7adad4a33030f8b8c80005f29e25fb27d89770e`. Lokalnie, w układzie katalogów zgodnym z repozytorium, polecenie `python -m unittest discover -s tests -p test_f93.py -v` zakończyło się wynikiem **12/12 OK**. Testy obejmują skończone modele, przykłady wielomianowe, klasy równoważności i rachunek rekurencyjny. Nie stanowią mechanicznej weryfikacji wszystkich dowodów.
- **Podgląd lokalny:** XeLaTeX przez Pandoc, **4 strony A4** (595,28 × 841,89 pt), odpowiednio 3486, 4259, 4471 i 2995 znaków tekstu wyekstrahowanego. Kontrola PyMuPDF: brak bloków tekstu wychodzących poza bezpieczny obszar 12 pt od krawędzi; oględziny pierwszej i ostatniej strony. SHA-256 podglądu PDF: `3635196a5406e11ce02a8799d54a51b662d851185b6a415752208b174f10db3c`. **PDF jest lokalnym artefaktem podglądu, nie plikiem w repozytorium.**
- **Integracja:** nowy tekst pozostaje osobnym suplementem; **nie scalono** go z monolitem wydania 0.20, którego binarny i źródłowy artefakt nie jest dostępny w repozytorium. Wstęp historyczny i dotychczasowe fragmenty manuskryptu nie były modyfikowane. Nie wykonano niezależnej recenzji matematycznej.
- **Bilans oddzielnych podglądów F7.1–F9.3:** 49 wcześniej udokumentowanych + 4 nowe = **53 strony niescalonych uzupełnień**. Bilans właściwego Tomu I pozostaje **585/1222 według rejestru**, bez doliczania dodatków. Końcowy spis treści nadal odroczony do ukończenia tomu.
- **Następny punkt:** F9.4 „Zadania z rozwiązaniem” (oryginał na s. 140–141). Nie powielać istniejących ćwiczeń; dodać zadania wymagające pełnych dowodów, weryfikacji założeń i przypadków brzegowych.


## Uzupełnienie F9.4 (30 października 2026)

**F9.4 — „Zadania z rozwiązaniem”**, źródło: `manuscript/tom-01/F09/F9.4_UZUPELNIENIE_ZADANIA_Z_DOWODAMI.md` na `main`.

- **Materiał:** 12 różnych, pełnych zadań wraz z dowodami, założeniami i kontrolą przypadków: permutacje z jednym punktem stałym, surjekcje, relacje zwrotne i symetryczne, ścieżki kratowe, rozdziały jednostek, trzy zbiory z przecięciami, zasada szufladkowa, niezmiennik parzystości, stopnie grafu, chińskie twierdzenie o resztach, dwumianowe zliczanie z wyróżnionym elementem i tożsamość Pascala.
- **Podgląd lokalny:** samodzielny XeLaTeX/Pandoc PDF, 4 strony A4. Zliczono co najmniej 2000 znaków tekstu na każdej stronie; kontrola PyMuPDF nie wykazała słów wychodzących poza kartę. SHA-256: `a34f402488718a7f44c0b267bf6872ca5a5082bb2695e1de4a735a8192d64c88`.
- **Reprodukowalne testy:** dodano `tests/test_f93_f94.py` na `main` (17 testów przykładów, w tym 12 tematów ćwiczeń F9.4 i przypadki F9.3). Lokalnie odpowiedni zestaw zakończył się **17/17 pozytywnie**. W repozytorium nie wykonano osobnego przebiegu CI/E2E po zapisie. Testy numeryczne nie zastępują niezależnej recenzji matematycznej.
- **Współbieżność:** podczas prac pojawiła się już wersja F9.3 na `main`, ze źródłem i oddzielnymi testami. Nie nadpisano jej równoległym szkicem.
- **Stan:** F9.4 pozostaje oddzielnym uzupełnieniem. Brak scalonego monolitu wydania 0.20 i aktualnej weryfikacji paginacji po integracji. Wstęp historyczny pozostaje nietknięty.

**Bilans oddzielnych podglądów F7.1–F9.4:** 53 strony uprzednio odnotowanych uzupełnień wraz z F9.3 + 4 strony F9.4 = **57 stron niescalonych materiałów redakcyjnych**. Właściwy rejestr Tomu I nadal wykazuje **585/1222 stron**; nie dodawać podglądów do tego bilansu. Finalny spis treści powstaje dopiero po ukończeniu i składzie Tomu I.

**Następny punkt w kolejności manuskryptu:** F10.1 „Liczba a zapis”. Przy opracowywaniu należy sprawdzić zakres istniejących dowodów o pozycyjnych rozwinięciach oraz dodać nowe wyniki bez dublowania tekstu.


## Opracowania F10.1–F10.2 (30 października 2026)

| Punkt | Źródło na gałęzi \`main\` | Treść uzupełnienia | Lokalna weryfikacja | Integracja |
| --- | --- | --- | --- | --- |
| F10.1 — Liczba a zapis | \`manuscript/tom-01/F10/F10.1_UZUPELNIENIE_REPREZENTACJE.md\` | 9 twierdzeń z dowodami, 12 zadań z rozwiązaniami. Schemat Hornera, kanonizacja zapisów, liczba słów stałoszerokościowych, kryterium rozwinięcia skończonego i okresowego, kod uzupełnień do dwóch | PDF XeLaTeX 4 strony rzeczywistego A4; tekst na kolejnych stronach: 2457, 3356, 3445, 2632 znaków; brak wykrytego wychodzenia słów poza kartę | Nie scalono z monolitem 0.20 |
| F10.2 — Przeniesienie w dodawaniu | \`manuscript/tom-01/F10/F10.2_UZUPELNIENIE_PRZENIESIENIA.md\` | 10 twierdzeń z dowodami, 12 zadań z rozwiązaniami. Niezmienniki prefiksowe, przeniesienie i pożyczka, przepełnienie, przeniesienie wieloskładnikowe i normalizacja iloczynu | PDF XeLaTeX 4 strony A4; tekst na stronach: 2120, 3487, 3120, 2185 znaków; brak wykrytego wychodzenia słów poza kartę | Nie scalono z monolitem 0.20 |

- **Testy:** lokalnie wykonano 16/16 testów w pliku \`tests/test_f10.py\` (odtwarzalny zestaw zapisany również na \`main\`). Sprawdzono tysiące przykładów konwersji oraz pełne małe przestrzenie wejść dla dodawania/odejmowania kolumnowego. Testy numeryczne nie są formalnym dowodem wszystkich twierdzeń. Brak potwierdzonego osobnego uruchomienia CI po commicie.
- **Kontrola PDF (SHA-256):** F10.1 — \`558227d089e8c76b76938244aeddae8b6c52da0af9a91a33f61b7d042c6c1982\`; F10.2 — \`6135435b0a6c35d36b5724898731431ea9626c36fe8ca3eef581ee92e375f54b\`.
- **Stan materiałów:** 57 stron oddzielnych uzupełnień F7.1–F9.4 + 8 stron F10.1–F10.2 = **65 stron odrębnych PDF**. Nie jest to wzrost objętości scalonej księgi.
- **Bilans Tomu I:** dotychczasowe **585/1222 stron wyłącznie według rejestru**, bez integracji i nowego przeliczenia wydania 0.20. Nie tworzyć finalnego spisu treści przed ukończeniem Tomu I; nie modyfikować historycznego wstępu.

**Następna jednostka źródłowa:** F10.3 „System sześćdziesiątkowy i zero”. Należy rozdzielić współczesny model matematyczny zapisu bazowego od tez o historii notacji babilońskiej oraz zweryfikować wszystkie przykłady konwersji i arytmetyki ułamków.


## Opracowanie F10.3 (30 października 2026)

**F10.3 — „System sześćdziesiątkowy i zero”** zapisano w \`manuscript/tom-01/F10/F10.3_UZUPELNIENIE_SZEŚĆDZIESIĄTKOWY_ZERO.md\` na gałęzi \`main\`.

- **Treść:** 8 twierdzeń z dowodami, 12 zadań z rozwiązaniami. Pozycje zerowe, algorytm Hornera, kryterium skończonego rozwinięcia ułamków, minimalna liczba miejsc, okresy i ich długość w przypadkach względnej pierwszości, przeniesienia oraz rozróżnienie czasu trwania i wskazań zegara.
- **Ostrożność historyczna:** odróżniono nowoczesny model pozycyjny od faktycznych znaków klinowych; źródła historyczne: MacTutor oraz F. Cajori, *A History of Mathematical Notations*. Bez przypisywania współczesnych separatorów wszystkim tabliczkom i bez deklaracji własnej weryfikacji paleograficznej.
- **Podgląd:** XeLaTeX/Pandoc, 4 strony A4; wyekstrahowano odpowiednio 2511, 3667, 3533, 2378 znaków; brak słów wychodzących poza obszar strony; SHA-256 PDF: \`1fd2dfb4e765fbcb4641b95af0b2874d7bcd48cf2ccbe802297c23723ad5ef1e\`.
- **Testy:** 8 nowych lokalnych kontroli zakończonych pomyślnie; odtwarzalne w \`tests/test_f103.py\` na \`main\`. Łącznie z F10.1–F10.2 wykonano lokalnie **24/24 testy pozytywne**; nie uruchomiono osobnego potwierdzonego przebiegu GitHub CI na opublikowanych testach. Testy liczbowe nie zastępują formalnych dowodów ani oceny źródeł historycznych.
- **Bilans dodatków F7.1–F10.3:** 65 stron wcześniejszych, oddzielnych podglądów + 4 strony F10.3 = **69 stron niescalonych materiałów**. Nie zmienia to dotychczasowego, niezweryfikowanego niezależnie bilansu 585/1222 stron monolitu 0.20.

**Następny punkt:** ustalić dokładny nagłówek F10.4 i jego istniejące dowody przed opracowaniem. Końcowy spis treści dopiero po ukończeniu i finalnym składzie Tomu I. Nie modyfikować historycznego wstępu.


## Opracowanie F11.1 (30 października 2026)

**F11.1 — „Dodawanie przez rekurencję: struktura i uniwersalność”**. Dodano uzupełnienie bez nadpisywania istniejących stron 148–149, historycznego wstępu ani innych rozdziałów.

- **Źródło na main:** `manuscript/tom-01/F11/F11.1_UZUPELNIENIE_MONOID.md`; commit utworzenia [`a70af9b`](https://github.com/mojealterego/Ontologia-Liczby-/commit/a70af9be9f9ac2ba2b58ae28f945090b4f602197), poprawka łamania wzoru [`f1fd5df`](https://github.com/mojealterego/Ontologia-Liczby-/commit/f1fd5df13d496269ce925bb0ac0bfe7d97c7c2bb).
- **Zakres:** 4 definicje, 9 twierdzeń z dowodami, 5 kontrprzykładów i 12 zadań z rozwiązaniami. Uniwersalność `(N,+,0)` jako monoidu generowanego przez jeden element, iteracja w dowolnym monoidzie, endomorfizmy, skończone sumy, algebraiczny porządek, częściowe odejmowanie, grupy cykliczne. Nie powielono dowodów łączności i skracania z oryginalnego F11.1.
- **Testy:** `tests/test_f111.py`, commit [`65c6242`](https://github.com/mojealterego/Ontologia-Liczby-/commit/65c62422e6264d2f984f72bdd416811e49c66f20). Lokalnie wykonano **12/12 testów pozytywnych** poleceniem `python -m unittest discover -s /mnt/data/ontologia_run2 -p test_f111.py -v` (po checkout repozytorium odpowiednio `python -m unittest discover -s tests -p test_f111.py -v`); dodatkowo ponownie wykonano lokalne testy F10.1–F10.3 **24/24 pozytywne**. Kontrole skończonych przypadków nie zastępują dowodów ogólnych.
- **PDF podglądowy:** lokalny Pandoc + XeLaTeX, 4 strony rzeczywistego A4, 12 pt, marginesy 24 mm; brak słów poza granicą kart według PyMuPDF; SHA-256 `c4239bcba97e84ddef10d1797606a7834be760b4ae2aafe3861ffadccee62254`. Pomocnicza kontrola parytetu źródła lokalnego i ponownie odczytanego z GitHub: długość 8297 znaków, FNV-1a 32 `2d9068a5` (kontrola niesłużąca jako kryptograficzny dowód integralności). PDF nie jest opublikowany jako plik binarny na GitHubie.
- **Regresja rozszerzona:** lokalne uruchomienie `python -m pytest -q` na 10 dostępnych plikach testowych F8.1–F8.5, F9.1–F9.4, F10.1–F10.3 oraz F11.1: **114/114 testów pozytywnych** (czas 1,07 s). To wynik lokalnego zestawu z katalogów roboczych, nie przebieg CI na GitHubie ani dowód poprawności wszystkich twierdzeń.
- **Stan:** F11.1 jest uzupełnieniem oddzielnym, niescalonym z monolitem 0.20. Wcześniej wykazano **69 stron** podglądów F7.1–F10.3; obecne 4 strony dają **73 strony odrębnych podglądów**, nieobjęte numeracją księgi. Bilans **585/1222** pozostaje bez zmian.
- **Blokady:** brak źródłowego i binarnego monolitu wydania 0.20 w repozytorium; brak potwierdzonego CI po commicie; brak niezależnej recenzji matematycznej. Nie wolno deklarować integracji, pełnej certyfikacji dowodów ani wzrostu paginacji.
- **Następny punkt:** F11.2 „Przemienność i jej znaczenie” (oryginał na s. 150–151). Najpierw sprawdzić istniejące argumenty, nie dublować dowodu przemienności.

Końcowy spis treści pozostaje odroczony do całkowitego ukończenia i finalnego składu Tomu I; nie przechodzić do Tomu II.


## Opracowanie F11.2 (30 października 2026)

**F11.2 — „Przemienność i jej znaczenie: od permutacji do struktur wolnych”.** Rozwinięcie pierwotnych stron 150–151 bez zastępowania wcześniejszej treści, historycznego wstępu i dowodu przemienności w arytmetyce Peana.

- **Źródło na `main`:** `manuscript/tom-01/F11/F11.2_UZUPELNIENIE_PRZEMIENNOSC.md`; commit utworzenia [`90b5a0e`](https://github.com/mojealterego/Ontologia-Liczby-/commit/90b5a0ef9925a122d71ccf0e44fc20391bf95422). Potwierdzony ponowny odczyt z GitHub: blob SHA `ae7daad9e0f75d0863162ed5eb815dd88ea3dd25`, długość 10 913 znaków, FNV-1a UTF-16 `f85a7f37` zgodne z lokalnym źródłem.
- **Zawartość:** 5 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań. Zagadnienia: centrum monoidu, przemienność lokalna i globalna, monoid skończonych wielozbiorów, jego własność uniwersalna, symetria sumy rozłącznej, skracanie, abelianizacja monoidu oraz grupowanie po włóknach funkcji. Oddzielono łączność, przemienność i skracalność.
- **Testy na `main`:** `tests/test_f112.py`; commit [`f9fcbfa`](https://github.com/mojealterego/Ontologia-Liczby-/commit/f9fcbfab7eb8d022bc083280dd1561291fb99a31). Ponowny odczyt: blob SHA `1e77e0ad1d6eb96dbd271eba45b46eea70f31a3f`, 4551 znaków, FNV-1a UTF-16 `c719d8bc` zgodne z lokalnym testem. Lokalnie: `python -m unittest discover -s tests -p test_f112.py -v` — **16/16 pozytywnych**. Dodatkowo wykonano dostępny lokalny zestaw F9.1–F9.2: **17/17 pozytywnych**. Nie uruchomiono pełnej regresji całego repozytorium ani nie potwierdzono GitHub CI.
- **Podgląd PDF:** lokalnie Pandoc + XeLaTeX, 4 strony rzeczywistego A4, 11 pt, margines 23 mm. Ekstrakcja tekstu: odpowiednio 2471, 2421, 2160, 2213 znaków. PyMuPDF: zero słów poza granicą 16 pt od krawędzi na każdej stronie; oględziny pierwszej i ostatniej strony. SHA-256 lokalnego PDF: `dbedd3aa99d67a4e35fa8c4855edd84bf5f2fe542443711f6d23fb3d1e9919f8`. **PDF nie jest plikiem binarnym opublikowanym na GitHubie.**
- **Bilans:** 73 uprzednio udokumentowane strony oddzielnych podglądów + 4 strony F11.2 = **77 stron niescalonych materiałów**. Właściwy licznik Tomu I pozostaje **585/1222 wyłącznie według wcześniejszego rejestru**; nie doliczać stron przed integracją z rzeczywistym monolitem 0.20.
- **Ograniczenia:** lokalne testy przykładów nie są formalną weryfikacją wszystkich twierdzeń; brak niezależnej recenzji naukowej, potwierdzonego CI oraz źródłowego i binarnego monolitu 0.20. Nie wolno deklarować integracji ani zmiany numeracji księgi.
- **Następny punkt do opracowania:** F11.3 „Przykłady i kontrola” (oryginał na stronach 152–153). Najpierw sprawdzić istniejące przykłady i nie powielać ich; wprowadzić nowe metody walidacji sum i formalne oszacowania.

Końcowy spis treści wykonać dopiero po ukończeniu i finalnym składzie Tomu I. Nie przechodzić do Tomu II.


## F11.3 — kontrola sum (30 października 2026)

- Źródło: `manuscript/tom-01/F11/F11.3_UZUPELNIENIE_KONTROLA_SUM.md`, commit `48e0d45be21dd51fad7a68ad0d32dee7c9a7f17b` na `main`.
- Zakres: 3 definicje, 8 twierdzeń z dowodami, 4 kontrprzykłady i 12 rozwiązanych zadań. Certyfikaty prefiksowe, niezmiennik pętli, podział na bloki, kontrola modularna, CRT przy modułach względnie pierwszych, dokładna rekonstrukcja przy ograniczeniu błędu oraz oszacowanie błędów sumowania.
- Status: tekst źródłowy zapisany; brak potwierdzonej recenzji formalnej, wykonania testów i kompilacji PDF w tej sesji. Nie twierdzić, że są zaliczone.
- Brak integracji z monolitem 0.20; licznik 585/1222 bez zmian. Dotychczasowe 77 stron odrębnych podglądów nie obejmuje F11.3. Wstęp historyczny i poprzednie materiały niezmienione. Bez finalnego spisu treści i bez Tomu II.


## Domknięcie kontroli F11.3 i nowe uzupełnienie F12.1 (30 października 2026)

### F11.3 — rozszerzenie i weryfikacja techniczna

- **Zachowano dotychczasowy tekst** manuscript/tom-01/F11/F11.3_UZUPELNIENIE_KONTROLA_SUM.md i wyłącznie dopisano część o certyfikatach przedziałowych, sumach kontrolnych z wagami, wykrywaniu transpozycji, monotoniczności prefiksów oraz błędach względnych. Commit rozszerzenia: [8fc9bc0](https://github.com/mojealterego/Ontologia-Liczby-/commit/8fc9bc0ea6fb80a7e9907dc4208e38e3dab57c45); końcowy blob źródła: 51f9307a8904361c5c57f4527b0814f7f4fa4ab6.
- **Bilans treści całego uzupełnienia:** 5 definicji (D1–D5), 14 twierdzeń z dowodami (T1–T14), 8 kontrprzykładów (K1–K8) i 20 rozwiązanych zadań (Z1–Z20). Zapisane źródło jest odrębne od pierwotnych stron 152–153.
- **Testy:** tests/test_f113.py (8 testów; wcześniejszy commit cb1320b6c0b3d7b1e9f85bda675975c28e2a1ff3) oraz tests/test_f113_extended.py (6 testów; commit [78924ab](https://github.com/mojealterego/Ontologia-Liczby-/commit/78924abe0bed157ceb36ff911892443c69caef89)). Oba pliki odtworzono lokalnie z identycznością Git blob SHA i wykonano: **14/14 OK**. Sprawdzono m.in. przypadki skończone dla wag modulo liczb pierwszych, granic przedziałów i prefiksów.
- **Podgląd PDF:** lokalna kompilacja Pandoc/XeLaTeX: **4 strony A4**; 1949, 2223, 2627, 1708 znaków wyekstrahowanego tekstu. PyMuPDF: 0 słów poza obszarem 15 pt od krawędzi. SHA-256 PDF: a76515e9e2a818d49772dbfe99456364d99b662a29dcd327c138eeb5e349addc. PDF pozostaje artefaktem lokalnym, nie binarium na GitHubie.

### F12.1 — odejmowanie częściowe i dopełnienie grupowe

- **Nowe źródło:** manuscript/tom-01/F12/F12.1_UZUPELNIENIE_GRUPOWE.md, commit [f8a23d6](https://github.com/mojealterego/Ontologia-Liczby-/commit/f8a23d68c20a7e3e2595c62b4995705a2b4ca5cc); Git blob SHA 9ef241c13a168ba220424294826121f063911ed7, zgodny z lokalnym plikiem użytym do kompilacji PDF.
- **Zakres:** 5 definicji, 10 twierdzeń z dowodami, 7 kontrprzykładów i 12 rozwiązanych zadań. Operacja częściowa w N, relacja formalnych różnic, konstrukcja Z, dobrze określone działania, porządek grupowy, własność uniwersalna dopełnienia grupowego, teleskopowanie i znaczenie skracalności monoidu. Suplement do oryginalnych stron 154–155 bez ich nadpisywania.
- **Testy:** tests/test_f121.py, commit [63c0591](https://github.com/mojealterego/Ontologia-Liczby-/commit/63c059113e5cd4df19fa23dc325ecbf06f681c50), Git blob SHA 1b4bd8142de78162c0de6c9652b007bad32320f9. W lokalnym odtworzeniu identycznym bajtowo z plikiem opublikowanym: **12/12 OK**. Kontrole obejmują skończone modele relacji równoważności, działań na klasach, porządku i przedłużenia homomorfizmów do grup cyklicznych.
- **Podgląd PDF:** Pandoc/XeLaTeX, **4 strony A4**; 2554, 2420, 2108, 2715 znaków tekstu. PyMuPDF: 0 słów poza obszarem 15 pt. SHA-256: cd1314d773e79a51dfe112a59c5651add18388e6fec7cf4fd0a1fc2e77fd22f8.

### Bilans i ograniczenia

- Łącznie w bieżącym lokalnym uruchomieniu: **26/26 testów pozytywnych** (14 F11.3 + 12 F12.1); dwa osobne podglądy PDF, po 4 strony A4. Potwierdzono zgodność Git blob SHA plików źródłowych i testowych z plikami lokalnymi.
- Wcześniejsze **77 stron** osobnych podglądów F7.1–F11.2 + **4 strony F11.3** + **4 strony F12.1** = **85 stron odrębnych materiałów PDF**, niebędących częścią zintegrowanej księgi.
- **Licznik właściwego monolitu pozostaje 585/1222 wyłącznie według wcześniejszej dokumentacji.** Nie ma w repozytorium kompletnego źródła ani binarnego wydania 0.20; integracji i nowej paginacji nie wykonano.
- Nie uruchomiono potwierdzonego GitHub Actions CI i nie wykonano niezależnej recenzji wszystkich twierdzeń. Testy skończonych przypadków nie zastępują dowodów ogólnych.
- Historyczny wstęp, pierwotne strony manuskryptu i pozostałe suplementy pozostają nietknięte. Bez końcowego spisu treści; bez przejścia do Tomu II.
- **Następny punkt merytoryczny:** F12.2 „Pożyczanie w zapisie dziesiętnym” (pierwotne strony 156–157). Rozszerzyć formalny niezmiennik pożyczki i przypadki graniczne bez powtarzania przykładów już zawartych w oryginale.

## F12.2 — pożyczanie pozycyjne: wykonanie i kontrola (30 października 2026)

- **Zapisane źródło na `main`:** `manuscript/tom-01/F12/F12.2_UZUPELNIENIE_POZYCZANIE.md`, commit [b5e547e](https://github.com/mojealterego/Ontologia-Liczby-/commit/b5e547e6ba5ecb21af387eb0daa73cadd9ef6673), blob SHA `e80506e99a847319a8a5fe47abedf05a1c609a07`. Samodzielny suplement do oryginalnych stron 156–157: **6 definicji, 16 twierdzeń z dowodami, 9 kontrprzykładów, 24 rozwiązane zadania**. Niezmiennik prefiksowy, pożyczka końcowa, certyfikaty, dopełnienie cyfrowe, kongruencje, łańcuch równych cyfr, analiza kosztu.
- **Korekta formalna F12.2:** D2 dopuszcza także $A<B$, a T7 interpretuje wynik jako $A-B=R_n-c_nb^n$; commit [a9fa84e](https://github.com/mojealterego/Ontologia-Liczby-/commit/a9fa84e70d67e6087ba05c8f9a0c6934e0590f08). Zaktualizowano i ponownie skompilowano lokalny PDF.
- **Zapisane testy:** `tests/test_f122.py`, commit [d4863e4](https://github.com/mojealterego/Ontologia-Liczby-/commit/d4863e430e4ef24961228e68b821ec157117dc2a), blob SHA `d4622b3aa4cf6a345adf5f493384d1f6ed99ae99`. Lokalne wykonanie: **12/12 OK**; wyczerpujące pary dla podstaw 2, 3 i 10 oraz kontrola certyfikatów i przypadków granicznych.
- **Regresja:** lokalne pliki `test_f113.py`, `test_f113_extended.py`, `test_f121.py` sprawdzone względem Git blob SHA aktualnego `main`: **26/26 OK**. Łącznie **38/38 testów lokalnych OK**. Bez potwierdzonego przebiegu GitHub Actions CI i bez formalnej recenzji wszystkich dowodów.
- **Podgląd:** Pandoc + XeLaTeX, kod wyjścia 0, **4 strony rzeczywistego A4** (595,28 × 841,89 pt), 10 pt, margines 20 mm; PyMuPDF: **0 słów poza granicą 16 pt**. SHA-256 lokalnego PDF: `6a1af2172e74c5a919d1635162aa69448bf374e70b798a75ebf04e8654d3253f`. Poprzedni podgląd Letter/2 strony został zastąpiony poprawnym A4/4 strony. PDF jest lokalny, nie został zapisany jako binarium w repozytorium.
- **Dowody szczegółowe:** [docs/DOWODY_F12_2_2026-10-30.md](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/docs/DOWODY_F12_2_2026-10-30.md), commit [e9235db](https://github.com/mojealterego/Ontologia-Liczby-/commit/e9235db03ad238db41488d93fb790d9b8acaddf8).
- **Bilans odrębnych podglądów:** 85 stron wcześniej udokumentowanych + 4 strony F12.2 = **89 stron materiałów niescalonych**. **Monolit pozostaje 585/1222 wyłącznie według historycznego rejestru**, bez aktualizacji paginacji.
- **Blokada integracyjna:** w repozytorium brak kompletnego źródła i binarnego monolitu wydania 0.20. Nie naruszono historycznego wstępu, pierwotnych stron 156–157 ani wcześniejszych materiałów. Nie tworzono końcowego spisu treści; nie przechodzono do Tomu II.
- **Kolejny punkt:** F12.3 „Zadanie odwrotne” (oryginalna strona 158); najpierw porównać z istniejącym omówieniem równań i uniknąć powtarzania dowodów z F12.1.


## Opracowania F12.2–F12.3 (30 października 2026)

| Punkt | Źródło na `main` | Rezultat i weryfikacja | Integracja |
| --- | --- | --- | --- |
| F12.2 — Pożyczanie w zapisie dziesiętnym | `manuscript/tom-01/F12/F12.2_UZUPELNIENIE_NIEZMIENNIKI_POZYCYJNE.md` | Niezmiennik prefiksu `A_j-B_j=C_j-u_j β^j`, odejmowanie przez dopełnienie, przypadki graniczne zera, arytmetyka stałej szerokości i błąd numeryczny; 11 twierdzeń/lematów/wniosków, 12 zadań z rozwiązaniami; podgląd **4 strony A4** | Niescalony z monolitem 0.20 |
| F12.3 — Zadanie odwrotne | `manuscript/tom-01/F12/F12.3_UZUPELNIENIE_RÓWNANIA_ODWROTNE.md` | Translacje grupowe, kryterium podzielności w Z, kongruencje liniowe, diofantyczne równania dwóch niewiadomych i teleskopowanie różnic; 12 oznaczonych twierdzeń/lematów/wniosków, 12 zadań z rozwiązaniami; podgląd **4 strony A4** | Niescalony z monolitem 0.20 |

**Kod i testy odtwarzalne:** `tools/arithmetic.py`, `tests/test_f122_f123.py`; uruchomienie lokalne z katalogu repozytorium: `python -m unittest discover -s tests -p 'test_f122_f123.py' -v`. Podczas tej sesji **14/14 testów pozytywnych**, w tym wyczerpująca weryfikacja małych przypadków, 2500 losowo odtwarzalnych par, NWD i parametrów równań diofantycznych. GitHub Actions/CI nie zostało potwierdzone; testy nie zastępują dowodów ogólnych ani niezależnej recenzji naukowej.

**Skład:** dwa podglądy XeLaTeX po 4 strony A4, każda strona z tekstem, bez słów wychodzących poza margines bezpieczeństwa 12 pt; sprawdzono wyrenderowane strony pierwszą i końcową. PDF-y są artefaktami lokalnymi; repozytorium przechowuje ich źródła. Do **85 stron** wcześniejszych osobnych podglądów doszło **8 stron F12.2–F12.3**, co daje **93 strony odrębnych materiałów niescalonych**, jeżeli w międzyczasie nie pojawiły się dalsze pakiety.

**Bilans pełnego monolitu Tomu I pozostaje 585/1222 wyłącznie według rejestru 0.20**; pełne źródło i binarny monolit wydania 0.20 nadal nie zostały dostarczone do integracji. Nie modyfikować historycznego wstępu, nie uznawać dodatków za strony monolitu i nie sporządzać końcowego spisu treści do zamknięcia Tomu I.

**Następny punkt według oryginalnego manuskryptu:** F13.1 „Definicja i tabliczka mnożenia” (s. 160–161 wydania referencyjnego 0.18).


## F13.1 — Definicja i tabliczka mnożenia: certyfikacja (30 października 2026)

- **Nowe źródło na main:** manuscript/tom-01/F13/F13.1_UZUPELNIENIE_TABLICA_I_CERTYFIKACJA.md. Utworzenie: [4e3fd0e](https://github.com/mojealterego/Ontologia-Liczby-/commit/4e3fd0e72b2643ad43421b7f2a1618a7405bf0de); korekta odtwarzalnego marginesu A4: [1abd9b6](https://github.com/mojealterego/Ontologia-Liczby-/commit/1abd9b66c9096a7b704870a100f8e7725a2e7047). Git blob źródła: e0446f2ad519b0516c8e563fedd5f15253326624, zgodny z lokalnym git hash-object.
- **Zakres:** 6 definicji, 14 oznaczonych twierdzeń/wniosków z dowodami, 8 kontrprzykładów, 12 zadań z rozwiązaniami. Własność uniwersalna funkcji addytywnych, kompletny certyfikat lokalny tablicy, monotoniczność, skracanie, podzielność, sumy kontrolne, okresy modulo i niewystarczalność kontroli wyłącznie przez symetrię lub sumę. Oryginalny F13.1 (strony 160–161 dostępnego manuskryptu) zawiera już definicję rekurencyjną, rozdzielność i łączność; ich podstawowych dowodów nie dublowano.
- **Testy na main:** tests/test_f131.py, commit [6e11a16](https://github.com/mojealterego/Ontologia-Liczby-/commit/6e11a16a57a6fd681ba490bcf45484dfe087318d); Git blob ce1c524313a0561253acd7646f06e5a732ad096e zgodny z lokalnym. Lokalnie **15/15 OK**; z referencyjnymi testami F12.2–F12.3 **29/29 OK**. Nie jest to uruchomienie CI ani mechaniczny dowód wszystkich twierdzeń.
- **Podgląd:** lokalnie Pandoc + XeLaTeX, **4 strony A4** przy 10 pt i marginesie 19 mm, odpowiednio 2635, 2999, 3441, 3399 znaków tekstu; PyMuPDF: 0 słów poza obszarem 14 pt od krawędzi. SHA-256 PDF: 2dbe68be941f50276657eee70beaf2d0cce7b111b6fd312f9486c9ba5146726b. PDF nie jest binarium opublikowanym w repo.
- **Dokumentacja dowodowa:** docs/DOWODY_F13_1_2026-10-30.md, commit [0ed0a2d](https://github.com/mojealterego/Ontologia-Liczby-/commit/0ed0a2dde50336678768c0726d43fe4fb43864e4).
- **Uwaga o monolicie:** odnaleziony w Bibliotece plik ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf ma **764 strony**, więc nie jest tożsamy z opisanym w docs/WYDANIE_20_STATUS.md wydaniem 0.20 (864 strony). Jego surowe bajty nie były dostępne do materializacji. W repo nadal brak źródła i binarnego monolitu 0.20. **585/1222 bez zmian**, bez integracji i ponownej paginacji.
- **Uwaga o sumie podglądów:** w repo są dwie wersje suplementu F12.2; rejestr wykazuje historycznie 93 strony niescalonych podglądów, lecz ich łączna liczba wymaga rozstrzygnięcia duplikacji. Nowe 4 strony F13.1 są osobnym podglądem, nie stronami monolitu.
- **Ograniczenia:** brak niezależnej recenzji wszystkich dowodów i potwierdzonego GitHub CI. Historyczny wstęp i wcześniejsze rozdziały niezmienione; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F13.2 „Model prostokątny”, oryginalne strony 162–163; przed rozszerzeniem odróżnić model kombinatoryczny od miary geometrycznej i nie powielać istniejących przykładów.


## F13.2 — Model prostokątny: enumeracja i certyfikaty (30 października 2026)

- **Nowe źródło na main:** manuscript/tom-01/F13/F13.2_UZUPELNIENIE_PROSTOKATY.md; commit [7dd880d](https://github.com/mojealterego/Ontologia-Liczby-/commit/7dd880d23d22ab945be6a8ab01e6ac8cb809040e), Git blob 16100a6c803bec3d88aabfeec94e47a3f02ccab9. Ponowny odczyt GitHub i lokalny git hash-object wykazały identyczność bajtową.
- **Zakres:** 5 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań. Oryginalne F13.2 (s. 162–163 referencyjnego wydania 0.18) już zawiera bijekcję kartezjańską, rozdzielność, podwójne liczenie i odróżnienie pola od liczebności. Suplement nie powtarza tych argumentów: rozwija enumerację podprostokątów, ich łączną powierzchnię kombinatoryczną, graf sąsiedztwa, dwudzielność, certyfikaty prefiksów i kryterium minorów.
- **Testy:** tests/test_f132.py; commit [25fb7c1](https://github.com/mojealterego/Ontologia-Liczby-/commit/25fb7c1bf54152c2f42817e4e81d34f41de95081), Git blob ec7216035f0b0943bccdaa5e117dec7399ba4dbc. Lokalnie 12/12 OK (unittest, testy wyczerpujące małych siatek i F_3); źródło testów identyczne bajtowo z plikiem na main.
- **Podgląd:** Pandoc + XeLaTeX, **4 strony A4**, tekst na stronach: 2204, 2344, 2506, 2172 znaków; PyMuPDF: zero słów poza granicą 12 pt; oględziny renderów stron 1 i 4. SHA-256 lokalnego PDF: 0f1dd4012ae65bc99d5727099e983fb16d600f8802880f9d7fb6b106846333e2. PDF nie jest opublikowanym binarium repozytorium.
- **Dokumentacja odtwarzalna:** docs/DOWODY_F13_2_2026-10-30.md; commit [837e005](https://github.com/mojealterego/Ontologia-Liczby-/commit/837e005d0627f5593513679f99f1163ba9b4e956).
- **Bilans:** wcześniejsza liczba 93 niescalonych stron podglądów i 4 strony F13.1 były historycznie dokumentowane z zastrzeżeniem duplikacji F12.2. F13.2 dodaje kolejne 4 strony odrębnego podglądu; **nie ogłaszamy nowego definitywnego sumarycznego bilansu** przed deduplikacją. Monolit Tomu I pozostaje **585/1222 według rejestru 0.20**, bez doliczania suplementów.
- **Granice weryfikacji:** brak potwierdzonego CI na GitHubie, niezależnej recenzji wszystkich dowodów oraz kompletnego źródła i binarnego monolitu 0.20. Nie wykonano integracji. Historyczny wstęp i wcześniejsza treść pozostają bez zmian; bez finalnego spisu treści, bez Tomu II.
- **Następny punkt:** F13.3 „Algorytm pisemny” (oryginalne strony 164–165). Należy rozszerzać niezmienniki splotu i przeniesień bez powielania już istniejących przykładów.


## F13.3 — Algorytm pisemny: formalna normalizacja (30 października 2026)

- **Źródło:** `manuscript/tom-01/F13/F13.3_UZUPELNIENIE_SPLOT_I_PRZENIESIENIA.md`; uzupełnienie oryginalnych stron 164–165 wydania referencyjnego 0.18. Oryginału ani historycznego wstępu nie modyfikowano.
- **Zakres:** 4 definicje, 12 twierdzeń z dowodami i 12 rozwiązanych zadań; splot cyfr, indukcyjny niezmiennik prefiksów, normalizacja przeniesień, długość iloczynu, koszt klasyczny, tożsamość Karatsuby, arytmetyka modularna i wykrywanie błędów cyfr.
- **Kod referencyjny:** `tools/long_multiply.py`; typowany, jawny ślad iloczynu i przeniesień; nie jest implementacją stałoczasową ani biblioteką kryptograficzną.
- **Testy:** `tests/test_f133.py`; **14/14 lokalnie pozytywnych** (`python -m unittest discover -s tests -p 'test_f133.py' -v` w katalogu roboczym); obejmują m.in. małe przypadki wyczerpujące, testy losowe 256-bitowych liczb, przeniesienia, przepełnienie i walidację danych. Testy obliczeniowe nie zastępują recenzji wszystkich dowodów.
- **Podgląd PDF:** 5 stron A4, po **2069 / 2849 / 3058 / 3921 / 2502** znaki wyekstrahowanego tekstu; brak słów poza obszarem strony według PyMuPDF (margines bezpieczeństwa 10 pt). Lokalny SHA-256: `3c2d643343c619f2b697b63ad737ae8898079fd916932b1d915eb1f983476695`. PDF lokalny, niewłączony do repozytorium ani monolitu.
- **Integracja:** niewykonana — nadal brak źródła i binarnego monolitu wydania 0.20. **585/1222** stron właściwego tomu pozostaje liczbą wyłącznie dokumentacyjną; nie doliczać pięciu stron podglądu. Wcześniejszy łączny licznik podglądów nadal wymaga deduplikacji F12.2. Finalny spis treści dopiero po ukończeniu Tomu I.
- **Kolejny punkt:** po F13.3 przejść do F14.1 zgodnie z kolejnością oryginalnego manuskryptu, po odczytaniu oryginału i weryfikacji wcześniejszych uzupełnień.


## F14.1 — Dzielenie z resztą: prefiksy i certyfikaty (30 października 2026)

- **Oryginał zweryfikowany:** F14.1 „Dzielenie z resztą”, strony 166–167 w 764-stronicowym referencyjnym pliku `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf`. Plik ten nie jest potwierdzonym monolitem 0.20 (w rejestrze 0.20 opisano 864 strony). Istniejący dowód twierdzenia o dzieleniu, przykłady i historyczny wstęp pozostawiono bez zmian.
- **Nowe źródło na `main`:** `manuscript/tom-01/F14/F14.1_UZUPELNIENIE_PREFIKSY_CERTYFIKATY.md`, commit [23cfb4d](https://github.com/mojealterego/Ontologia-Liczby-/commit/23cfb4dbbce080648491df64ab4e820541b24a94), Git blob `d5f8b8a1df59b2ce2c3bc64a79f7af61e2c8b017`. 5 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów i 12 zadań z rozwiązaniami. Nowy zakres: niezmiennik prefiksowy, certyfikat kroków, kontrola modularna, sklejanie bloków, sufiksy, okresowość i obsługa znaków.
- **Kod i testy:** `tools/long_divide.py` (commit [31757d3](https://github.com/mojealterego/Ontologia-Liczby-/commit/31757d322fd6ad514ad8cdd1d2651346719430f1)); `tests/test_f141.py` (commity [ce4ab36](https://github.com/mojealterego/Ontologia-Liczby-/commit/ce4ab36a936d35fd5cd1f7e1faac9a545bcf95d8), [b37562e](https://github.com/mojealterego/Ontologia-Liczby-/commit/b37562edbef6e1995d7bcc50f086088fa8a0fb95)). Ponowny odczyt z GitHub potwierdził blob SHA plików. W lokalnym odtworzeniu układu repozytorium `unittest` **12/12 OK**, `pytest` **12/12 passed**, `compileall` bez błędów. Nie jest to przebieg GitHub CI.
- **Podgląd lokalny:** Pandoc/XeLaTeX, **3 strony A4**; tekst na stronach **2604 / 3455 / 3236** znaków, zero słów poza granicą 9 pt według PyMuPDF; SHA-256 PDF `572114eb41a3e8cd319d40a941f57ca8e46d173405c5275e77879923ed1ab924`. PDF nie jest binarium na `main`.
- **Dowody wykonania:** `docs/DOWODY_F14_1_2026-10-30.md`, commit [4375c68](https://github.com/mojealterego/Ontologia-Liczby-/commit/4375c686d13b58237373b32b10b3591b7bec5ae4).
- **Bilans:** 3 strony nowego, oddzielnego podglądu; historyczna suma podglądów nadal wymaga deduplikacji F12.2, dlatego nie deklaruje się definitywnego łącznego wyniku. **585/1222 stron monolitu Tomu I bez zmian** — brak źródłowego i binarnego wydania 0.20, integracji i ponownej paginacji.
- **Niezweryfikowane:** niezależna recenzja naukowa wszystkich twierdzeń, GitHub Actions CI oraz integracja monolitu. Wstęp historyczny i wcześniejsze rozdziały nietknięte. Bez finalnego spisu treści i bez Tomu II.
- **Kolejny punkt:** F14.2 „Dlaczego nie dzielimy przez zero?” — najpierw porównać z gotowym F7.3 i oryginalnymi stronami 168–169, nie powielać definicji ani istniejących kontrprzykładów.


## F14.2 — Dzielenie przez zero: dziedziny, lokalizacja i totalizacja (30 października 2026)

- **Oryginał:** przeczytano strony 168–169 referencyjnego 764-stronicowego pliku ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf. Zawierały już brak odwrotności zera, równanie 0x=a, niedozwolone skracanie, granice i uwagi o strukturach rozszerzonych. Przed opracowaniem porównano również F7.3 i F14.1. Nie zmieniano oryginału ani historycznego wstępu.
- **Nowy materiał na main:** manuscript/tom-01/F14/F14.2_UZUPELNIENIE_DZIEDZINY_LOKALIZACJA.md; commit [5088e45](https://github.com/mojealterego/Ontologia-Liczby-/commit/5088e45d3409d3c95e35fc0ceef8a379036d2b5c), Git blob SHA d2a15786fcc1c69f337449aa43c497c75d5a5f9b. **6 definicji, 12 twierdzeń z dowodami, 8 kontrprzykładów i 12 zadań z rozwiązaniami.** Zakres: ścisła dziedzina wyrażeń, równość częściowa, warunkowe przekształcenia, lokalizacja i jej własność uniwersalna, totalizacja zerowa, arytmetyka ciał skończonych oraz błąd zaburzonego mianownika.
- **Testy:** tests/test_f142.py, commity [3075837](https://github.com/mojealterego/Ontologia-Liczby-/commit/307583776747de40d841e7d33ce9036e304c69a8) i [6a46817](https://github.com/mojealterego/Ontologia-Liczby-/commit/6a468172ae162b3deaeb88f2c11d75987a8b6ce9), końcowy Git blob SHA 622c376bdcec85ce8d8a848c7d6e3a6e4adef08c. Lokalnie: unittest **16/16 OK**, pytest **16/16 passed**, compileall bez błędów. Testy obejmują skończone przypadki, nie są formalnym dowodem wszystkich twierdzeń.
- **Podgląd PDF:** lokalna kompilacja Pandoc/XeLaTeX, **4 strony A4**, tekst 2777 / 3469 / 2458 / 1638 znaków. PyMuPDF: zero słów poza obszarem 9 pt od krawędzi; renderowanie i kontrola wizualna stron. SHA-256 lokalnego PDF: f55509e6d5b886af80f7b4eb8cc67920f02e5b13e968f150214cf18cf7ab8788. PDF nie jest binarium opublikowanym na main.
- **Dokumentacja dowodowa:** docs/DOWODY_F14_2_2026-10-30.md, commit [5771dfd](https://github.com/mojealterego/Ontologia-Liczby-/commit/5771dfd177390b17ef589d2c23836946e51a9dab).
- **Niezweryfikowane:** niezależna recenzja wszystkich dowodów, pełna regresja repozytorium i GitHub Actions CI. Statusy dla commitu testowego nie zawierały wyników. Brak kompletnego źródła i binarnego monolitu wydania 0.20 uniemożliwia integrację i nową paginację.
- **Bilans:** cztery nowe strony są odrębnym podglądem, **nie zwiększają 585/1222**. Nie podawać definitywnej sumy odrębnych podglądów bez deduplikacji F12.2. Nie tworzyć finalnego spisu treści ani Tomu II.
- **Następny punkt:** F14.3 „Ułamki jako wynik dzielenia” (oryginał od strony 170). Najpierw sprawdzić istniejące konstrukcje i dowody, następnie rozszerzać bez powtórzeń.


## F14.3–F15.1 — konstrukcja wymiernych i podzielność (30 października 2026)

| Punkt | Plik na `main` | Odrębny rezultat | Kontrola i ograniczenia |
| --- | --- | --- | --- |
| F14.3 — Ułamki jako wynik dzielenia | `manuscript/tom-01/F14/F14.3_UZUPELNIENIE_KONSTRUKCJA_WYMIERNYCH.md` | 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań. Konstrukcja ciała \(\mathbb Q\), niezależność reprezentantów, własność uniwersalna, porządek, gęstość, mediant Fareya i oszacowania przybliżeń. Git commit `eef7f999ec2a257e1a38a72e8dce26cedd753841`, odczyt treści potwierdzony. | Lokalny Pandoc/XeLaTeX: **4 strony A4**, 2404 / 3231 / 2574 / 3123 znaki tekstu; kontrola PyMuPDF bez przekroczeń 9 pt. PDF SHA-256: `fe8dbaec0a9ddf67692994238d7c1e3f9b4e1012ab8afdc76e867925bb415b49`. |
| F15.1 — Podzielność | `manuscript/tom-01/F15/F15.1_UZUPELNIENIE_IDEALY_I_WARTOSCIOWANIA.md` | 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań. Porządek podzielności, ideały główne, NWD/NWW, rozkład na pierwsze, wartościowania, CRT, sumowanie bloków cyfr. Git commit `93545160570c374edd2c75897c0f2a8305523bdb`, odczyt treści potwierdzony. | Lokalny Pandoc/XeLaTeX: **4 strony A4**, 2465 / 2916 / 2664 / 3050 znaków tekstu; kontrola PyMuPDF bez przekroczeń 9 pt. PDF SHA-256: `c249b421304625f1daeaf9d36b3f38849972c04c787e36968e8517fcf333c20a`. |

**Testy reprodukowalne:** `tests/test_f143.py` (commit `f7b3f52647669374a36fde569363c5bda6a6027f`) i `tests/test_f151.py` (commit `8a2b67e9443458e6f7a4ce5f04159d44cc26d800`). Lokalnie `python -m pytest -q` dla tych dwóch plików: **24/24 passed**, wyłącznie przypadki skończone i kontrola rachunków. **Nie uruchomiono potwierdzonego GitHub Actions CI** i nie przeprowadzono niezależnej recenzji naukowej wszystkich dowodów.

**Integracja i bilans:** osiem stron kolejnych samodzielnych podglądów PDF **nie jest częścią scalonego monolitu**. Historyczna suma podglądów wymaga deduplikacji dwóch wersji F12.2, dlatego nie deklarujemy nowej sumy całkowitej. Udokumentowany bilans części zasadniczej Tomu I pozostaje **585/1222**, wyłącznie według rejestru wydania 0.20, którego pełnych źródeł i binarnego PDF w repozytorium nadal brakuje. Wstęp historyczny oraz istniejące rozdziały pozostawiono bez zmian. Bez końcowego spisu treści i bez przejścia do Tomu II.

**Następny punkt:** F15.2 „Algorytm Euklidesa” — przed pisaniem porównać z oryginalnymi stronami 174–176 i z gotowymi dowodami NWD/Bézouta w F15.1; rozwinąć odrębne własności, np. granice złożoności i certyfikaty obliczeń, bez powtarzania źródeł.


## F15.2 — Algorytm Euklidesa: certyfikaty i złożoność (30 października 2026)

- **Odczyt źródeł:** bieżący rejestr, F15.1 oraz referencyjny plik biblioteczny `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf`, strony 174–176. Oryginał zawiera już niezmienniczość NWD, zakończenie, Bézouta, algorytm rozszerzony, wzmiankę o złożoności logarytmicznej i odwrotnościach modularnych. Nowy suplement koncentruje się na certyfikatach, macierzach unimodularnych, formalnej kontroli śladów, granicach liczby kroków i argumentach ze znakami.
- **Źródło na `main`:** `manuscript/tom-01/F15/F15.2_UZUPELNIENIE_EUKLIDES_CERTYFIKATY.md`. Utworzenie `efbd1dfb4909ef1cdbed2802f790310259e360fe`, korekta eliminująca powtórzenia `58f725d6b653849bd3c5e094a24b24ea5505ec53`, certyfikat macierzowy `7faade3b84295cedc92eaeb6515b8d8eb64ee1b3`. **5 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów/granic, 12 zadań rozwiązanych.**
- **Testy na `main`:** `tests/test_f152.py`, commit utworzenia `0074623a5d8d760cb5cde9b96a0f23bcefffed90`, ostatni merytoryczny commit `5d091ffff39c6d6362395db65b0525fb5766b5f5`. Lokalnie końcowy zestaw `unittest` **15/15 OK** i `pytest` **15/15 passed**. Wyczerpujące małe zakresy, certyfikaty Bézouta, determinanty, ślady, granica logarytmiczna i 250 pseudolosowych dużych par. Pomocnicza zgodność źródeł GitHub/lokalnych: długość/FNV-1a UTF-16: źródło **9257 / 7c599c8b**, test **4940 / 640cac31**.
- **Podgląd PDF:** Pandoc/XeLaTeX, **3 strony A4**, odpowiednio **2325 / 3084 / 2710** znaków tekstu; PyMuPDF: 0 słów poza marginesem 9 pt; SHA-256 lokalnego PDF `b2ab35fe1faf6456773136c46990cffa0cc98918e6948fa247b18099abca5eb9`. Binarny PDF nie jest opublikowany na `main`.
- **Dowody wykonania:** `docs/DOWODY_F15_2_2026-10-30.md`, końcowy commit `a6d1e562f3532f73f0358128cf2903ac4797e50d`.
- **Ograniczenia:** brak potwierdzonego GitHub Actions CI, niezależnej recenzji naukowej i integracji z rzeczywistym monolitem 0.20. Wersja biblioteczna 764 strony nie jest tożsama z wydaniem 0.20 (864 strony według rejestru). Historyczny wstęp i istniejące rozdziały nietknięte. Podgląd **nie zwiększa 585/1222**; nie ustalono łącznej liczby niescalonych stron z powodu wcześniejszej duplikacji F12.2.
- **Następny punkt:** F15.3 „NWD, NWW i zastosowania” (referencyjna strona 179). Porównać z F15.1 i istniejącym F15.3; rozwijać zastosowania bez powtarzania dowodu `gcd·lcm=|ab|`. Bez końcowego spisu treści i bez Tomu II.
