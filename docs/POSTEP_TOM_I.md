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


## F15.3 — NWD, NWW i zastosowania (30 października 2026)

- Źródło na `main`: `manuscript/tom-01/F15/F15.3_UZUPELNIENIE_KONGRUENCJE_OKRESY.md`; commity `5cc76716b4f85a00c2f8663e49da9621a14eb6e6`, `904afa8c2623d1ecde0c0a0a0b4e41e2319600fd`.
- Zakres: 4 definicje, 8 twierdzeń z dowodami, 5 kontrprzykładów, 12 zadań z rozwiązaniami. Uogólnione CRT, kongruencje liniowe, przesunięte harmonogramy, liczba rozwiązań i okresy wspólne. Nie powtórzono dowodu tożsamości NWD·NWW.
- Testy opublikowane: `tests/test_f153.py`, commit `2bad45efd7b7858ec1b41a3c469e0209b374cd83`; pięć metod sprawdzających skończone zakresy. W tej sesji **nie potwierdzono ich uruchomienia**. Nie oznaczać ich jako zaliczone.
- Kompilacja PDF: **nie wykonana**; środowisko lokalne nie mogło pobrać opublikowanego źródła z raw.githubusercontent.com. Brak zweryfikowanego podglądu i liczby jego stron.
- Suplement pozostaje niescalony z monolitem 0.20. Licznik **585/1222 bez zmian**. Nie modyfikowano wcześniejszych źródeł ani historycznego wstępu. Nie utworzono finalnego spisu treści; nie rozpoczęto Tomu II.


## F15.3 — zakończenie weryfikacji lokalnej i rozwinięcie (31 października 2026)

- **Źródło:** `manuscript/tom-01/F15/F15.3_UZUPELNIENIE_KONGRUENCJE_OKRESY.md`; rozwinięcie T9–T12, D5, K6–K7, Z13–Z16 oraz korekty K3, K7 i warunków brzegowych T3/T8/T12. Commity `62e25b3401b47f15dbd32716db88538714163a1b`, `1b386a413dc41f68817a9ff4d9aafd7d02976e5f`, `2362fd284bfbec113e92a7cb4066561e89e7afa5`. **Łącznie F15.3: 5 definicji, 12 twierdzeń z dowodami, 7 kontrprzykładów, 16 rozwiązanych zadań.**
- **Testy:** `tests/test_f153.py`; commit `57d3d9034f422b31d816e0ab516f09e1fb0c0ba4`; lokalnie `unittest` **10/10 OK**, `pytest` **10/10 passed**. Zweryfikowano zgodność Git blob SHA źródła `1e205a17f0b663dc5416466052f13df7bc0389f9` i testu `9b68f1eb8ece131b3b70b001aa9030b791486bf7` z GitHub.
- **Podgląd:** lokalny Pandoc/XeLaTeX, **3 strony A4**, 2624/3408/2776 znaków; PyMuPDF: 0 słów poza marginesem 9 pt; SHA-256 PDF `e1e5031aa31c586e681d695b9cf9b3cc0581114064120b3da33ca7bcbca18726`. PDF nie został dodany jako binarium na `main`.
- **Dokumentacja dowodowa:** `docs/DOWODY_F15_3_2026-10-31.md`, commit `11093a97400e5672bbc67019c6d0c7f4dcba45d3`.
- **Ograniczenia:** testy potwierdzają skończone przypadki, nie stanowią niezależnej recenzji dowodów; brak potwierdzonego GitHub CI i pełnej regresji repozytorium. Nie odnaleziono jeszcze zweryfikowanego następnego oznaczenia punktu po F15.3; wymaga to odczytu oryginalnego monolitu.
- **Wydanie:** historyczny wstęp i dotychczasowe rozdziały bez ingerencji. Integracja z monolitem 0.20 niewykonana; **585/1222 bez zmian**. Bez końcowego spisu treści i bez Tomu II.


## F16.1 — Ułamek jako iloraz: wysokość i rekonstrukcja modularna (31 października 2026)

- **Źródła odniesienia:** odczytano strony 181–182 bibliotecznego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony, wersja referencyjna, nie monolit 0.20) oraz istniejące `manuscript/tom-01/F14/F14.3_UZUPELNIENIE_KONSTRUKCJA_WYMIERNYCH.md`. Odrębny suplement nie powtarza dowodów konstrukcji ciała \(\mathbb Q\).
- **Gotowy materiał na `main`:** `manuscript/tom-01/F16/F16.1_UZUPELNIENIE_WYSOKOSC_REKONSTRUKCJA.md`, commit `34e34459382a21f4eafac15baafedb87486c485b`, Git blob SHA `a18086183f80e516212f1df33b9f6f4038a8f383`. **5 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań.** Nowe zagadnienia: minimalność mianownika, funkcja wysokości, ograniczenia wysokości sumy i iloczynu, zliczanie funkcją Eulera, warunki i jednoznaczność rekonstrukcji modularnej.
- **Testy na `main`:** `tests/test_f161.py`, commit `cb20e74fbce7012f667b82ee6b8cbdd2a07a6d48`, Git blob SHA `7bdb16f12e8a645dfaa83f094a7711e4dc3e164b`. Lokalnie `unittest` **12/12 OK**, `pytest` **12/12 passed**, `compileall` bez błędów. Skończone testy nie zastępują dowodów.
- **PDF:** lokalny Pandoc/XeLaTeX, **3 strony A4**; długości tekstu 2545/3093/1308 znaków; PyMuPDF: 0 słów poza granicą 9 pt; SHA-256 `4d15e892886b62b09d0e38b5d3b8d5c077efdcbfecc257964c9107fd18d98308`. Podgląd nie jest binarium na GitHub.
- **Dokumentacja dowodowa:** `docs/DOWODY_F16_1_2026-10-31.md`, commity `700c763cd1a912c273df20c5825e2ee970152dbe`, `9a1422d8ffde4ddd328f18574bd2015ed22cdcbc`.
- **Ograniczenia:** brak potwierdzonego GitHub CI (statusy commitu testowego puste), pełnej regresji repozytorium, niezależnej recenzji naukowej oraz kompletnego źródła i binarnego monolitu 0.20. Nie integrowano stron. **585/1222 bez zmian**. Wstęp historyczny i poprzednie rozdziały nienaruszone; nie utworzono końcowego spisu treści ani Tomu II.
- **Kolejny punkt:** F16.2 „Dodawanie i odejmowanie” (referencyjne strony 183–184). Przed rozbudową porównać z F14.3 i F16.1, skupić się na ścisłych algorytmach redukcji liczb pośrednich i weryfikowalnych rachunkach, bez ponownego dowodzenia elementarnego wzoru sumy.


## F16.2 — Dodawanie i odejmowanie: redukcja pośrednia (31 października 2026)

- **Stan na main:** `manuscript/tom-01/F16/F16.2_UZUPELNIENIE_DODAWANIE_REDUKCJA.md`, commit `d733560161697671db28b058b906a36136d64617`. Materiał zawiera 4 definicje, 10 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań. Koncentruje się na NWW mianowników, certyfikacie skracania, ograniczeniu wysokości i rachunku wyłącznie całkowitoliczbowym; nie powtarza konstrukcji ciała wymiernych z F14.3.
- **Testy na main:** `tests/test_f162.py`, commit `5ecfa40b25d5262a350fced4e9c5bf4d3460d160`. Obejmują enumerację sum i różnic, przykłady, wysokość, przemienność i walidację wejścia. **Nie uruchomiono dokładnie tego pliku z repozytorium** z powodu braku pobrania do środowiska lokalnego.
- **Weryfikacja niezależna lokalna:** uruchomiono `/mnt/data/ontologia_f162/verify.py`, 33 489 kombinacji kanonicznych ułamków; wszystkie zgodne z `fractions.Fraction`, podzielnością mianownika przez NWW i granicą wysokości. To nie jest pełny wynik testów repozytorium.
- **PDF:** Pandoc i XeLaTeX są zainstalowane, ale próba pobrania opublikowanego źródła zakończyła się błędem DNS `Could not resolve host: raw.githubusercontent.com`; **kompilacji podglądu nie wykonano**, brak zweryfikowanej liczby stron PDF.
- **Ograniczenia:** brak potwierdzonego CI, niezależnej recenzji, pełnej regresji i integracji z rzeczywistym monolitem 0.20. **585/1222 bez zmian**. Historyczny wstęp i dotychczasowe źródła pozostają nienaruszone. Bez końcowego spisu treści i bez Tomu II.


## F16.3 — Mnożenie i dzielenie: skracanie krzyżowe (31 października 2026)

- **Źródło na main:** `manuscript/tom-01/F16/F16.3_UZUPELNIENIE_MNOZENIE_DZIELENIE.md`, commit `bd89786240deabe9ebc6fe5130c7ce71090f7000`. 4 definicje, 10 twierdzeń z dowodami, 6 kontrprzykładów i 12 zadań rozwiązanych. Zagadnienia: kanoniczne skracanie krzyżowe, zero, kryterium dopuszczalności dzielenia, ograniczenie wysokości i certyfikat iloczynu.
- **Testy opublikowane:** `tests/test_f163.py`, commit `bd79b37726e1129ec3119ef8714daf3e1329abc0`. Pięć metod: enumeracja mnożenia i dzielenia, przykłady, zero, niepoprawne dane. **Uruchomienie dokładnego pliku repozytoryjnego niepotwierdzone**; brak potwierdzonego CI.
- **PDF:** nie skompilowano w tej sesji. Nie ma zweryfikowanego podglądu ani liczby stron.
- **Stan wydawniczy:** brak integracji z rzeczywistym monolitem 0.20, **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały bez zmian. Brak niezależnej recenzji naukowej i pełnej regresji; bez końcowego spisu treści i bez Tomu II.

- **Kontynuacja weryfikacji F16.3 (31.10.2026):** lokalna niezależna enumeracja 14 161 kanonicznych przypadków mnożenia zakończona 14 161/14 161 PASS; porównano z `fractions.Fraction`, NWD, podzielność mianownika i granicę wysokości. Dowód: `docs/DOWODY_F16_3_2026-10-31.md`, commit `e763a440a0b235a704607bb74b1f0c471d4aa31c`. Nie jest to uruchomienie dokładnego pliku `tests/test_f163.py`; PDF nadal nieskompilowany, brak integracji 0.20, **585/1222 bez zmian**.


## F16.4 — Błąd reprezentacji: okresowość i certyfikowane granice (31 października 2026)

- **Odczyt oryginału:** strony 187–188 bibliotecznego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony; materiał referencyjny, nie monolit 0.20). Nie powielono istniejącego kryterium skończonego rozwinięcia ani elementarnych granic błędu sumy i iloczynu.
- **Źródło na `main`:** `manuscript/tom-01/F16/F16.4_UZUPELNIENIE_OKRESOWOSC_CERTYFIKATY.md`; commity `2005d82b870729376b4b4df9f7ce4ea44c39586c`, `06fda126dd977a682ff64b940a2875999ec55a7e`. Git blob SHA `262948068c27c8a8a14837c973c9a6e0537e29d4`. **6 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.** Nowe zagadnienia: dokładny przedokres i okres rozwinięć w podstawie B, rząd multiplikatywny, certyfikaty przedziałowe, zaokrąglanie do parzystej, uwarunkowanie odejmowania i bezpieczna granica błędu ilorazu.
- **Testy na `main`:** `tests/test_f164.py`, commity `015491a3214a25b2fb1dc984b7e7f5e7aa566979`, `e38bf51baca8189752e60d07263aef676e387008`, Git blob SHA `89a983fe9b5e5cdbb8a3c7741bf8ae3131d57959`. Uruchomiono dokładnie opublikowany plik: `unittest` **9/9 OK**, `pytest` **9 passed, 8 subtests passed**, `compileall` bez błędów. Porównanie Git blob SHA z lokalnym `git hash-object` potwierdziło identyczność plików.
- **Podgląd PDF:** lokalny Pandoc/XeLaTeX, **3 strony A4**, PyMuPDF: 0 słów poza marginesem 9 pt. SHA-256 `084bfec8c313b66e0690fee87a6550c5d109d3f84ae0717e62fc3257dcb89a4d`. PDF nie został opublikowany binarnie na `main`.
- **Dokumentacja dowodowa:** `docs/DOWODY_F16_4_2026-10-31.md`, commity `a6b04a9a0535606d21ba8a8fdd4306a575fe4a5a`, `1c0e20b9b871a1f7f2b647c59dad6bbf952cac02`.
- **Ograniczenia:** brak potwierdzonego GitHub Actions CI (puste statusy), pełnej regresji repozytorium, niezależnej recenzji naukowej oraz kompletnego źródła i binarnego monolitu 0.20. **585/1222 bez zmian**; historyczny wstęp i poprzednie rozdziały bez ingerencji, bez końcowego spisu treści i bez Tomu II.
- **Kolejny punkt:** F17.1 „Rozszerzenie przez różnice” (referencyjne strony 189–190). Przed rozszerzeniem zbadać wcześniejsze formalne konstrukcje liczb całkowitych, aby nie powielać grupowego dopełnienia; skupić się na osobnych własnościach porządku, pierścienia i uniwersalności.


## F17.1 — Rozszerzenie przez różnice: porządek i uniwersalność (31 października 2026)

- **Porównanie z oryginałem:** odczytano strony 189–190 bibliotecznego ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf (764 strony, nie wydanie 0.20) oraz wcześniejszy suplement F12.1. Nie powtórzono konstrukcji grupowego dopełnienia ani istniejącego wzoru na iloczyn klas.
- **Nowe źródło na main:** manuscript/tom-01/F17/F17.1_UZUPELNIENIE_PORZADEK_UNIWERSALNOSC.md; commit [c959e33](https://github.com/mojealterego/Ontologia-Liczby-/commit/c959e33f186344df89a3967e995f5a00a814e46c), Git blob SHA 353cb3cb247f246ba84dbb513a845df7dcd505dd. **5 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań**. Zakres: normalna postać znaku, porządek liniowy i dyskretny, certyfikat porównania, monotoniczność mnożenia, wartość bezwzględna, charakterystyka pierścienia i uniwersalna mapa pierścieniowa.
- **Testy na main:** tests/test_f171.py; commity [658209c](https://github.com/mojealterego/Ontologia-Liczby-/commit/658209c07428c695be9b9bf44f039dfb6567545d), [90d2d1c](https://github.com/mojealterego/Ontologia-Liczby-/commit/90d2d1c0552f4a5273e87aeae4fe61b30fb01ce4), Git blob SHA 0227cd1cfaa31729662dded13afceec99b87a9a0. Lokalnie: unittest **10/10 OK**, pytest **10/10 passed**, compileall bez błędów. Potwierdzono identyczność obu opublikowanych blob SHA z lokalnymi plikami.
- **Podgląd PDF:** lokalny Pandoc/XeLaTeX, kod wyjścia 0; **4 strony A4**, tekst 2813/3540/3354/996 znaków, zero słów poza marginesem bezpieczeństwa 9 pt; SHA-256 4db8e4e6e04f4626a3e4dce519b444680f7870667841308ce4852ea3d029177d. Binarny PDF nie jest opublikowany na main.
- **Dokumentacja dowodowa:** [docs/DOWODY_F17_1_2026-10-31.md](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/docs/DOWODY_F17_1_2026-10-31.md), commit [584209a](https://github.com/mojealterego/Ontologia-Liczby-/commit/584209add10adea5fa8e1d0aa9f529a2c3d2bd25).
- **Niezweryfikowane:** niezależna recenzja matematyczna, formalna mechanizacja dowodów, pełna regresja i GitHub CI (puste commit statuses). **Blokada integracyjna:** brak kompletnego źródła i binarnego monolitu wydania 0.20.
- **Bilans wydawniczy:** cztery strony odrębnego podglądu **nie są stronami monolitu**. Udokumentowany licznik **585/1222 bez zmian**; łączna suma oddzielnych podglądów nadal wymaga deduplikacji wcześniejszych wersji F12.2. Historyczny wstęp i poprzednie rozdziały bez ingerencji. Bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** F17.2 „Działania i znak” (referencyjna strona 191 i dalsze); nie powielać istniejącego dowodu reguły znaków, rozwinąć certyfikaty aksjomatów pierścienia i niezależność reprezentantów.


## F17.2 — Działania i znak (31 października 2026)

- Nowy, niezależny suplement: `manuscript/tom-01/F17/F17.2_UZUPELNIENIE_DZIALANIA_ZNAK.md`, commit `8ff9868631ce6cb6ecddc7129692025da9636617` na `main`.
- 43 numerowane jednostki: 23 bloki definicyjno-dowodowe i kontrmodelowe oraz 20 rozwiązanych zadań. Materiał dotyczy dobrze określonych działań na klasach par, znaków, porządku, dzielników zera, dzielenia z resztą, NWD i uniwersalności Z.
- **Status:** źródło opublikowane; nie uruchomiono w tej sesji kompilacji PDF ani testów matematycznych; nie wykonano niezależnej recenzji. Objętość PDF niezweryfikowana. To suplement, nie gotowy rozdział scalonej księgi.
- **Blokada:** brak rzeczywistego źródła monolitu 0.20; licznik **585/1222 bez zmian**. Wstęp historyczny i istniejące rozdziały nietknięte. Bez końcowego spisu treści i bez Tomu II.

- **Kontynuacja F17.2:** cztery aneksy, w tym dowód dobrze określonego iloczynu w N, dzielenie przez ujemny dzielnik, przypadki NWD oraz 10 dalszych zadań (razem 30). Commit `1ad07240bb5361769534f017a8316bc4bb2e508a` na `main`.
- **Weryfikacja ograniczona:** sześć lokalnych testów pomocniczych przeszło (arytmetyka par, przykłady, reszty, skracanie); nie uruchomiono dokładnego testu z repozytorium. Próba pobrania aktualnego źródła do środowiska PDF zakończyła się błędem sieciowym. Wygenerowany lokalnie jednostronicowy PDF zawierał wyłącznie techniczny nagłówek i **nie jest podglądem manuskryptu**. Nie raportować go jako skompilowanego suplementu.
- **Integracja:** 585/1222 bez zmian; brak źródła monolitu 0.20.

## F17.2 — pogłębienie i kontrole (31 października 2026)

- **Na main:** `manuscript/tom-01/F17/F17.2_PAKIET_WERYFIKACYJNY.md` (6 definicji, 13 twierdzeń z dowodami, 8 kontrprzykładów, 12 zadań rozwiązanych; commit `a8656201c068d5c5b00cd69bed9d49758c0b72f5`); `manuscript/tom-01/F17/F17.2_CERTYFIKATY_C11_C14.md` (4 certyfikaty, commit `b205ebac00fa5b933da2c1f384dd685b5120f167`).
- **Testy na main:** `tests/test_f172_extended.py` (commit `b96c973ef65c4b0c7a6d94f5418381f791c2c288`, blob `f9323365ffa5755d3731d68c02605fb66498aa59`). Lokalna kopia o identycznym Git blob SHA: unittest **12/12 OK**, pytest **12 passed**, compileall OK. Testy skończone, nie zastępują dowodów.
- **Podgląd lokalny:** osobny, **szerszy wariant roboczy** F17.2 (6 definicji, 18 twierdzeń, 10 kontrprzykładów, 24 zadania i 4 certyfikaty) skompilowano do **10 stron A4**, SHA-256 `43f1a7eadb66d62371dc77fa968c21cdfda94b872427ae7d5555cb76a5cac5a6`, bez słów poza bezpiecznym marginesem. **Nie jest to podgląd identyczny z publikowanym pakietem MD**; pełny wariant lokalny nie został zapisany na main i nie jest zintegrowany.
- **Dokumentacja:** `docs/DOWODY_F17_2_2026-10-31.md`, commit `6a1b38c0cb54dcf8d4628a21cd65097ba0794f9d`.
- **Ograniczenia:** brak CI (0 commit statuses), pełnej regresji, formalnej mechanizacji i niezależnej recenzji. Brak rzeczywistego monolitu 0.20 blokuje integrację. Historyczny wstęp i dotychczasowy manuskrypt nienaruszone. **585/1222 bez zmian**; bez finalnego spisu treści i bez Tomu II.


## F17.2 — Kongruencje i CRT (31 października 2026)

- Opublikowano `manuscript/tom-01/F17/F17.2_KONGRUENCJE_CRT_ROZSZERZENIE.md` na `main`, commit `b6790e02af4c31c8544731a11a1fb2710af086bd`.
- Zakres: 5 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań; dobrze określone działania na klasach, jądro redukcji, jednostki, kongruencje liniowe, uogólnione CRT, rząd addytywny i nilpotenty.
- W tej sesji **nie uruchomiono testów ani kompilacji PDF**; brak formalnej recenzji i pełnej regresji. Liczba stron niepotwierdzona.
- Suplement niezintegrowany z monolitem 0.20. **585/1222 bez zmian**. Wstęp historyczny i wcześniejszy manuskrypt nietknięte. Bez finalnego spisu treści i bez Tomu II.


## F17.2 — Struktura iloczynowa, idempotenty i certyfikaty CRT (31 października 2026)

- **Nowe źródło na main:** `manuscript/tom-01/F17/F17.2_IDEMPOTENTY_CRT_CERTYFIKATY.md`, commit `a5e6aedb45bd9ce22af552b5de2d515c272381d8`, Git blob SHA `c0e4857672221023c630761e31ebb50aa546abb9`. **7 definicji, 12 twierdzeń z dowodami, 8 kontrprzykładów, 12 rozwiązanych zadań.** Zakres: certyfikaty Bézouta, rozwiązywalność CRT, projektory ortogonalne, izomorfizm pierścieni, grupa jednostek, funkcja Eulera, idempotenty, nilpotenty i pierwiastki wielomianów. W odróżnieniu od poprzedniego suplementu nacisk na dekompozycję pierścienia i sprawdzalne certyfikaty.
- **Testy na main:** `tests/test_f172_crt_certificates.py`, commit `7d59d73cb125ce97a4d41ddfc8be5f5938e57750`, Git blob SHA `f36a9c066f92509600086542ec9ae6103a2b3b72`. Identyczny blob lokalny potwierdzono `git hash-object`. Wynik: `python -m unittest -q` **9/9 OK**, `python -m pytest -q` **9 passed**, `compileall` OK. Testy obejmują 176 400 kombinacji CRT, wyczerpujące sprawdzanie projektorów, przykłady, idempotenty i nilpotenty dla małych modułów. Kontrole skończone nie zastępują dowodów.
- **Podgląd dokładnie opublikowanego źródła:** lokalny Pandoc/XeLaTeX, FreeSerif, **4 strony A4**, kod wyjścia 0, bez ostrzeżeń o brakujących glifach i bez słów poza marginesem bezpieczeństwa 9 pt. Zweryfikowano identyczność Markdown przez Git blob SHA; PDF SHA-256 `8bc2d583deb2f9b832c30b7beba07088bd93b0bf7be3c4274b297911e5baf179`. PDF pozostaje artefaktem lokalnym, **nie opublikowano binarnego PDF na main**.
- **CI:** dla commitu testów GitHub zwrócił pustą listę commit statuses; brak potwierdzonego uruchomienia CI i pełnej regresji. Brak niezależnej recenzji i formalnej mechanizacji dowodów.
- **Stan wydawniczy:** źródło nie jest zintegrowane z rzeczywistym monolitem 0.20; **585/1222 bez zmian**. Historyczny wstęp i dotychczasowy manuskrypt bez ingerencji. Bez końcowego spisu treści i bez Tomu II.


## F17.2 — Kongruencje wielomianowe i podnoszenie (31 października 2026)

- **Na main:** `manuscript/tom-01/F17/F17.2_PIERWIASTKI_MODULARNE_PODNOSZENIE.md`, commit `e5d963b218463ee807f4f4960231d7371fb121e0`, korekta kontrprzykładu K1 commit `0679d8bebffb6f50bdd6038f8eab94134be3141f`.
- **Zakres:** 5 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań; kongruencje wielomianowe, liniaryzacja, podnoszenie prostych pierwiastków, CRT, wartościowanie i zliczanie pierwiastków.
- **Weryfikacja:** lokalny skrypt Python zaliczył kontrole liczby rozwiązań x²≡0 dla p∈{2,3,5,7}, k=1..5, pierwiastków x²≡1 dla p∈{3,5,7,11}, k=1..4, zliczanie CRT dla czterech par modułów i trzech wielomianów oraz przykłady modulo 49 i 15. To skończone sprawdzenia, bez pełnej regresji i formalnej mechanizacji. Błąd K1 wykryto i poprawiono.
- **PDF:** kompilacja dokładnego opublikowanego źródła nie została wykonana, ponieważ środowisko kontenerowe nie mogło rozwiązać nazwy `raw.githubusercontent.com` (curl exit 6). Nie deklarować podglądu ani liczby stron.
- **Stan wydawniczy:** brak integracji z monolitem 0.20; **585/1222 bez zmian**. Nie zmieniono historycznego wstępu i wcześniejszych rozdziałów; bez końcowego spisu treści i bez Tomu II.


## F17.3 — Porządek i oś liczbowa: geometria dyskretna (31 października 2026)

- **Punkt odniesienia:** biblioteczny `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony), strony 193–194, zawierający oryginalny F17.3. Jest to inne wydanie niż monolit 0.20.
- **Nowe źródło na `main`:** `manuscript/tom-01/F17/F17.3_UZUPELNIENIE_GEOMETRIA_DYSKRETNA.md`, commit `fda869379859c02877dc7a4c778b03262ae50b5e`, normalizacja końca pliku `22fbdc88b97c3ec1986f358bb4a5385a5192c09d`; Git blob SHA `26550d3f252b8db6e92f6b0df960943a55ed733d`.
- **Zakres:** 7 definicji, 26 twierdzeń i wniosków z dowodami, 10 kontrprzykładów i 26 rozwiązanych zadań. Treść rozwija metrykę, geometrię ścieżek, izometrie, rzutowania, topologię dyskretną, zupełność, zwartość, zaokrąglanie i optymalizację dyskretną, nie zastępując F17.1 ani F17.2.
- **Testy na `main`:** `tests/test_f173_discrete_geometry.py`, commit `4653f9299dffab7bdddbd96fde3ae7ad3320b545`, normalizacja końca pliku `dc549492b569de6081926eb9664cd59276a8d25d`; Git blob SHA `a5225d73625d72ffacb6fd30120a2f469f710a3c`. Lokalnie `unittest` **15/15 OK**, `pytest` **15 passed**, `compileall` bez błędów. SHA lokalne i repozytoryjne identyczne.
- **Podgląd PDF:** z dokładnie tego źródła Markdown skompilowano lokalnie Pandoc/XeLaTeX **7 stron A4**; każda zawiera 3053–3440 znaków wyekstrahowanego tekstu; PyMuPDF wykazał 0 słów poza granicą 8 pt. SHA-256 PDF `cd3240131b5e44f83e28f644238054f366744d2fe917f97b8e8d81510d0ebdb3`. PDF nie został opublikowany binarnie na `main`.
- **Dokumentacja dowodowa:** `docs/DOWODY_F17_3_2026-10-31.md`, commit `ea2714142fa01298eb84068d0fd94705554d211a`.
- **Ograniczenia:** kontrole skończone nie zastępują pełnej recenzji matematycznej ani mechanizacji; brak kompletnego źródła monolitu 0.20 uniemożliwia integrację i finalną paginację. **585/1222 bez zmian.** Historyczny wstęp i poprzednie rozdziały bez ingerencji. Bez końcowego spisu treści i bez Tomu II.


## F17.3 — bezpośrednia rozbudowa istniejącego rozdziału (31 października 2026)

- **Nie tworzono kolejnego równoległego suplementu:** rozszerzono istniejący `manuscript/tom-01/F17/F17.3_UZUPELNIENIE_GEOMETRIA_DYSKRETNA.md` o wypukłość porządkową, twierdzenie Helly'ego na osi, odległości od krat arytmetycznych i różnice skończone. Zachowano dotychczasowy tekst. Commit `d49ea956171c0ce240b36b62747b0aec58e54bb4`, blob `aed288a385383e909c66d6dcc7b1e4ee0cec51f6`. Nowa część: **3 definicje, 11 twierdzeń z dowodami, 4 kontrprzykłady, 12 rozwiązanych zadań**; całe F17.3: D1–D10, T1–T37, K1–K14, Z1–Z38.
- **Testy opublikowane na main:** `tests/test_f173_order_convexity.py`, commit `69e97f823b46c2859c75f7e2180f07afbd0397ae`, blob `a0c8f0e9d783870fd8f3aef062bb7660d670d9b1`; lokalnie identyczny blob: `unittest` **11/11 OK**, `pytest` **11 passed**. Testy skończone, bez formalnej mechanizacji.
- **Podgląd dokładnie źródła z main:** Git blob identyczny z lokalnym źródłem; Pandoc/XeLaTeX **9 stron A4**, 11 pt, margines 2,0 cm, wszystkie strony z rzeczywistą treścią, 0 słów poza bezpieczną granicą 8 pt. SHA-256 PDF `52f60a45d73335057162d3d372a8f434216eae6c5d26360f447198085495966d`. PDF tylko lokalny, bez binarnego uploadu na main.
- **Dowody wykonania:** `docs/DOWODY_F17_3_2026-10-31.md`, aktualizacja commit `c4a369350e29791d87b3bc41a56500a86033255a`. Nie przeprowadzono pełnej regresji, GitHub CI ani formalnej recenzji matematycznej.
- **Bilans monolitu 0.20:** **585/1222 bez zmian**. Brak kompletnego źródła monolitu blokuje scalanie; bez ingerencji w historyczny wstęp, bez finalnego spisu treści i bez Tomu II.


## F17.3 — rozbudowa bezpośrednia do 12 stron podglądu (31 października 2026)

- **Plik istniejącego rozdziału rozszerzony bez usuwania wcześniejszej treści:** `manuscript/tom-01/F17/F17.3_UZUPELNIENIE_GEOMETRIA_DYSKRETNA.md`; commit `c1cedc519e8f1aac6fc2e99f42185ee194c670c6`, Git blob `7072d5fdfcaba50b8e5486b1606398b099c3fefe`.
- **Nowe fragmenty:** D11–D14 (centra minimaksowe, koercywność, silna wypukłość, ważone sumy odległości), T38–T48 (pełne dowody), K15–K20 (kontrprzykłady), Z39–Z52 (rozwiązania). Cały punkt: 14 definicji, 48 twierdzeń/wniosków, 20 kontrprzykładów, 52 zadania rozwiązane.
- **Testy repozytoryjne:** `tests/test_f173_centers_convex_paths.py`, commit `0a54df8cfafbbe23957bf8b0e579e9e721d18367`; lokalnie **11/11 unittest**, **11/11 pytest**, compileall OK. Git blob testu `5d70293d4b229059279222396af355ee0632493e`, zgodny z lokalnym.
- **Podgląd:** źródło identyczne z GitHub na podstawie Git blob; Pandoc/XeLaTeX **12 stron A4**, bez pustych stron i bez wykrytych słów poza marginesem bezpieczeństwa 8 pt. PDF SHA-256 `790c6718dc48c346f9606bd1a0dff0ca6862bde60082243ee6780b6b1c66397f`. PDF lokalny, nie w repo.
- **Dowody techniczne:** `docs/DOWODY_F17_3_2026-10-31.md`, aktualizacja commit `881595c06137b137a91b68f4a60575a30172fd6e`. Brak potwierdzonego CI (puste statusy i workflow runs dla commitu testów); brak pełnej regresji i formalnej recenzji.
- **Integracja:** monolit 0.20 nieobecny w repo; **585/1222 bez zmian**. Nie edytowano historycznego wstępu ani poprzednich rozdziałów. Nie tworzono końcowego spisu treści ani Tomu II.


## F17.3 — rozbudowa istniejącego rozdziału o brzeg grafowy i wariację (31 października 2026)

- **Źródło zaktualizowane bez usuwania wcześniejszych fragmentów:** `manuscript/tom-01/F17/F17.3_UZUPELNIENIE_GEOMETRIA_DYSKRETNA.md`. Commit `25bf3ea48b7a806b7cfa3a6da0eed7597fd20079`, normalizacja końca sekcji `89814d0c04aa950f7b4c8b32b05d0aef7552a77e`; Git blob SHA `5df8134803d68e2f28dc67e32ba9126710724bda` identyczny z lokalnym źródłem podglądu.
- **Nowa treść:** 4 definicje D15–D18, 10 twierdzeń z dowodami T49–T58, 6 kontrprzykładów K21–K26 i 10 rozwiązanych zadań Z53–Z62. Całość F17.3: **18 definicji, 58 twierdzeń/wniosków, 26 kontrprzykładów i 62 rozwiązane zadania**. Zakres: brzeg krawędziowy, składowe, wariacja całkowita, nierówność izoperymetryczna, sumowanie przez części i formuła warstwowa.
- **Testy na `main`:** `tests/test_f173_boundary_variation.py`, commit `2956265f9efba6fa77be196d53e1b8c60298d51e`, blob `7f81df19fc194b7ac1f46373a47a804375dd03cc`, identyczny z lokalnym. **11/11 unittest**, **11/11 pytest**, `compileall` OK; kontrole enumeracyjne i deterministyczne losowe, nie formalna mechanizacja.
- **Podgląd źródła identycznego z `main`:** Pandoc/XeLaTeX, A4, 11 pt, margines 20 mm, **15 stron**, wszystkie z tekstem, 0 słów poza bezpieczną granicą 8 pt; PDF SHA-256 `1bd4e73b5c22583e4130a8e011840c48da7bcc508fa3b331e0cda6e085c46b54`. Ostatnia strona częściowo wypełniona. PDF lokalny, nie binarnie opublikowany w repo.
- **Dokumentacja:** `docs/DOWODY_F17_3_2026-10-31.md`, commit `4fdb5dcb81441731c50d4dc587d9bf6bf630b1b2`, korekta formatowania `2e7830f9f87766584bc2feadbab6cea519124b81`.
- **Ograniczenia:** brak pełnej regresji repozytorium, potwierdzonego GitHub CI, formalnej mechanizacji i niezależnej recenzji. Brak źródła monolitu 0.20 uniemożliwia scalanie. **585/1222 bez zmian**. Historyczny wstęp i poprzednie rozdziały nienaruszone; bez finalnego spisu treści i bez Tomu II.


## F17.3 — energia Dirichleta i zadania brzegowe (31 października 2026)

- **Zapis na main:** bezpośrednio rozszerzono istniejący F17.3 (bez nowego równoległego suplementu), commit **9fc8c64cbe8aed20d6fdd335424e071a52906eab**, blob **7642634d347fb3a1bfc0b196f2364e39ddc90cd6**. Dotychczasowy tekst pozostał niezmienionym prefiksem źródła. Nowe sekcje: D19–D24, T59–T71, K27–K33, Z63–Z74 (6 definicji, 13 twierdzeń z dowodami, 7 kontrprzykładów, 12 zadań rozwiązanych).
- **Zakres całego F17.3:** D1–D24, T1–T71 (łącznie z wnioskami), K1–K33, Z1–Z74; pełną numerację sprawdza test. Rozwinięto energię dyskretną, problem Dirichleta, laplasjan, tożsamość i jądro Greena, równanie Poissona oraz ważone minimum energii.
- **Testy na main:** tests/test_f173_dirichlet_green.py, commit **a576588610d800ce2da34cd09596851f55fdf197**, blob **96b7f9c3e30a0ad3ecb906b6fc7ad7eae9ce226c**. Identyczne lokalne źródła: pytest **14/14**, unittest **14/14**, compileall OK; testy na dokładnych ułamkach i skończonych przypadkach, nie formalne dowody.
- **Podgląd całego F17.3:** Pandoc/XeLaTeX, A4, 11 pt, FreeSerif, margines 20 mm, **19 stron**, każda 2019–3681 znaków tekstu, 0 słów poza granicą 8 pt. PDF SHA-256 **afc3f9d7052c9b021c27b7ccf26ca9ac1459dc7ed81640582765420ff18ce978**. PDF lokalny, nie binarnie zapisany na main.
- **Dowody:** docs/DOWODY_F17_3_2026-10-31.md, aktualizacja commit **37f1aac5fd71d45b562b77a73aada8a56b80d2ff**. Dla commitu testów brak statusów GitHub CI. Nie przeprowadzono pełnej regresji ani niezależnej recenzji.
- **Integracja:** brak kompletnego źródła rzeczywistego monolitu 0.20; **585/1222 stron bez zmian**. Wstęp historyczny i inne rozdziały nietknięte. Nie utworzono końcowego spisu treści ani Tomu II.

## F17.3 — widmo laplasjanu i ostra nierówność Poincarégo (31 października 2026)

- **Zmieniono istniejący manuskrypt F17.3 bez tworzenia równoległego suplementu:** manuscript/tom-01/F17/F17.3_UZUPELNIENIE_GEOMETRIA_DYSKRETNA.md, commit b85b24919b87fb32c46fa0ea206eada933edff44, Git blob 7268e7f95df20b9166fc4f4e07f4ce38dc2b9f47. Dotychczasowe źródło o blobie 7642634d347fb3a1bfc0b196f2364e39ddc90cd6 zachowano jako prefiks, dopisując sekcje 19–21.
- **Nowa treść:** 4 definicje D25–D28, 9 twierdzeń T72–T80 z dowodami, 5 kontrprzykładów K34–K38 i 11 rozwiązanych zadań Z75–Z85. Cały F17.3: 28 definicji, 80 twierdzeń/wniosków, 38 kontrprzykładów, 85 zadań. Kontrola numeracji: brak luk i duplikatów.
- **Testy na main:** tests/test_f173_spectrum.py, commit 01f5a8c34f6334c6c4f0ea3830b3428dc3d67f1d, Git blob 5edcabee4e6f475447e0caecbffbdc6e5703291c, zgodny z lokalnym plikiem. Python standard library bez NumPy; pytest **10 passed**, unittest **10 OK**, compileall kod 0.
- **Podgląd dokładnego pełnego źródła F17.3:** Pandoc/XeLaTeX, FreeSerif, A4, 11 pt, margines 20 mm; **22 strony**, bez pustych stron i bez wykrytych słów poza granicą bezpieczeństwa 8 pt. PDF SHA-256 442b4a0f6f845be73d143502b729d0c602554ce348730c344a9c0126e71567c7. Zgodność źródła PDF z main potwierdza Git blob SHA. PDF jest artefaktem lokalnym.
- **Dowody techniczne:** docs/DOWODY_F17_3_2026-10-31.md, commit 85e94242899b131778ead051f7d9d69ad280673f. Brak potwierdzonego GitHub CI (pusta lista statusów), pełnej regresji, mechanizacji i niezależnej recenzji.
- **Blokada integracji:** źródło monolitu 0.20 nieobecne w repo. **585/1222 stron bez zmian**. Historyczny wstęp i pozostałe rozdziały nietknięte. Bez finalnego spisu treści i bez Tomu II.


## F17.3 — dodatniość semigrupy cieplnej, wymuszenie i Euler (31 października 2026)

- **Zapis na `main`:** bezpośrednie rozszerzenie istniejącego `manuscript/tom-01/F17/F17.3_UZUPELNIENIE_GEOMETRIA_DYSKRETNA.md` o sekcje 22–24, bez usunięcia wcześniejszego prefiksu; commity `7f787ae5430f8bea630f9c86210c4d8a38f44f34` oraz `7ee6d8663e416a7b03a29226e29cdcf1ede8c21c`. Końcowy Git blob `2e501f099b5d83deb78adfa7e12706a25c8b7068`.
- **Nowa treść:** D29–D32, T81–T89 (9 twierdzeń z dowodami), K39–K44, Z86–Z97 (12 rozwiązanych zadań). Cały F17.3: **32 definicje, 89 twierdzeń/wniosków, 44 kontrprzykłady, 97 zadań rozwiązanych**. Dodatniość, substochastyczność i symetria jądra cieplnego, zasada porównania, kontrakcja, jawny Euler, wzór Duhamela, wymuszenie i równowaga Greena.
- **Testy na `main`:** `tests/test_f173_heat_semigroup.py`, commit `7d82c6c76088236aba1b7dfae4f6ea70706324c4`, blob `c8bc34e076a9b48d8c7f6e4ab25b6187b7ed02a1`, zgodny z lokalnym. `unittest` **15/15 OK**, `pytest` **15 passed**, `compileall` kod 0. Kontrole skończone, nie formalna mechanizacja.
- **Podgląd całego F17.3:** dokładne źródło z `main` (zgodny Git blob), Pandoc/XeLaTeX, A4, 11 pt, FreeSerif, margines 20 mm, **24 strony**, wszystkie z tekstem, 0 słów poza granicą 8 pt; PDF SHA-256 `aef3db5dc1be9c95c4cab266c5f74b5a9fb00d87aea8e037287ae13e0adf2014`. PDF pozostaje lokalny, nie opublikowano go binarnie na GitHub.
- **Dowody:** `docs/DOWODY_F17_3_CIEPLO_2026-10-31.md`, commit `47ecd7c432ccd19d272a8979398044eefdfc96e6`. Dla commitu testów GitHub zwrócił pustą listę combined statuses; brak potwierdzonego CI, pełnej regresji i niezależnej recenzji.
- **Integracja:** brak kompletnego źródła rzeczywistego monolitu 0.20. **585/1222 stron bez zmian.** Wstęp historyczny i wcześniejsze rozdziały bez ingerencji; bez finalnego spisu treści i bez Tomu II.


## F18.1 — postać kanoniczna, wysokość, medianty i rozwinięcia pozycyjne (31 października 2026)

- **Zbadano oryginał:** biblioteczny ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf, strony 195–197 (wydanie robocze 764 stron, nie monolit 0.20). Kolejny punkt po F17.3 to F18.1 „Konstrukcja ciała Q”. Zamiast kontynuować nadmiernie rozbudowany F17.3, przygotowano nowy materiał do F18.1 bez powtarzania oryginalnej konstrukcji klas par.
- **Zapis na main:** manuscript/tom-01/F18/F18.1_UZUPELNIENIE_STRUKTURALNE_Q.md, commit f6d0cb8704e0bc704538a5275e10f395c4cc9635, Git blob c4991e670b83d1a91cee61f074c841624224962e. Zakres: **8 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań**.
- **Testy na main:** tests/test_f181_rationals.py, commit 22b85c5a9f8165f117308275e05c6de16a9075ee, Git blob 734f39b1005b3535231d204598167cbc44fbc79e. Lokalne unittest **12/12 OK**, pytest **12 passed**, compileall kod 0. Testy skończone nie zastępują dowodów ogólnych.
- **Podgląd źródła identycznego z main:** Pandoc/XeLaTeX, FreeSerif, A4, 11 pt, margines 20 mm; **3 strony** z tekstem, 0 słów poza granicą bezpieczeństwa 8 pt; PDF SHA-256 64455340fc7628b71cdbd059cfc24b9abab6d4e2a1879d86e08a704008c57fe8. PDF lokalny, nie opublikowany binarnie w repo.
- **Dokumentacja dowodowa:** docs/DOWODY_F18_1_2026-10-31.md, commit debf4efb99003f812644a08c21779fdd8a68b3b4.
- **Ograniczenia:** GitHub combined statuses dla commitu testów puste; brak potwierdzonego CI, pełnej regresji i niezależnej recenzji matematycznej. Brak źródła monolitu 0.20 blokuje integrację. **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały nienaruszone; bez finalnego spisu treści i bez Tomu II.

- **Korekta testu F18.1:** usunięto możliwość cichego pominięcia testu numeracji w układzie repozytoryjnym; commit 0b6ec979fb0b2199135541a2711f28c40c508eaa, blob 6dcd9ab0c829c6dd965dc410f27ac76dec509d1e. Po zmianie lokalne unittest 12/12 OK, pytest 12 passed, compileall kod 0. Wcześniejszy blob testu był przejściowy.


## F18.2 — wartość bezwzględna i certyfikowana arytmetyka przedziałowa (31 października 2026)

- **Punkt oryginalny:** F18.2 „Wartość bezwzględna” na stronach 200–201 roboczego 764-stronicowego pliku ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf. To nie jest wydanie 0.20. Oryginał zawiera już definicję modułu, nierówność trójkąta, metrykę i przykład niezupełności Q, dlatego nie powielono tych dowodów.
- **Nowe źródło na main:** manuscript/tom-01/F18/F18.2_UZUPELNIENIE_WARTOSC_BEZWZGLEDNA.md, commit [761fc5a](https://github.com/mojealterego/Ontologia-Liczby-/commit/761fc5a98a697208050d56a9445e9f87fce9a44e), Git blob ac470a78d820f3bce7e017599e58f96b5ed5e2fb. Zawiera **8 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań**. Zakres: odwrócona nierówność trójkąta, warunki równości, błędy liniowe, rzut na przedział, otoczki iloczynów, certyfikaty dzielenia, stabilność odwrotności, jawny wymierny ciąg Cauchy'ego bez granicy wymiernej.
- **Testy na main:** tests/test_f182_absolute_intervals.py, commit [2b0893f](https://github.com/mojealterego/Ontologia-Liczby-/commit/2b0893fdc35567adabd499032967ec4b410b272b), Git blob 6ddb49468b2873b7f4c1f31c8211b81581329afc. Lokalnie **13/13 unittest**, **13 passed pytest**, compileall kod 0; dokładna arytmetyka wymierna i skończone enumeracje. Nie jest to formalna mechanizacja dowodów.
- **PDF:** lokalna kompilacja Pandoc/XeLaTeX z dokładnego źródła opublikowanego na main: **3 strony A4**, tekst odpowiednio 3367, 3234, 2118 znaków, 0 słów poza marginesem bezpieczeństwa 8 pt. SHA-256 PDF 456c77f9662b5e7fd873bd2c7a8db5f692622d752e50cf08e881b1ea86ea3f73. PDF pozostaje artefaktem lokalnym.
- **Dowody techniczne:** docs/DOWODY_F18_2_2026-10-31.md, commit [26e552c](https://github.com/mojealterego/Ontologia-Liczby-/commit/26e552cc870f89ecba04a0e257751ca45c0b839b).
- **Braki:** brak pełnej regresji repozytorium, potwierdzonego GitHub CI, niezależnej recenzji matematycznej i źródłowego monolitu wydania 0.20. Nie zmieniono wcześniejszych rozdziałów ani historycznego wstępu.
- **Integracja:** **nie wykonano**. Stan części merytorycznej Tomu I nadal **585/1222 stron według historycznego rejestru**. Trzy strony osobnego PDF nie powiększają tej liczby. Bez końcowego spisu treści i bez Tomu II.


## F19.1 — kanoniczne rozwinięcia pozycyjne i certyfikaty cyfr (31 października 2026)

- **Oryginał sprawdzony:** F19.1 „Zapis dziesiętny” na stronach 202–203 roboczego, 764-stronicowego pliku ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf. Nie jest to źródło ani binarny monolit 0.20. Istniejące kryterium skończonego zapisu w podstawie 10 pozostawiono bez zmian.
- **Nowy materiał na main:** manuscript/tom-01/F19/F19.1_UZUPELNIENIE_KANONICZNE_CYFRY.md; commit **befb20faa97840e8957f29ca0965717d903d4f52**, Git blob **5f35280e873ace5decf62c89eb68f1446d09dd6c**. Zawiera **7 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań**. Zakres: zachłanny automat reszt, dokładny minimalny przedokres, rząd multiplikatywny, kanoniczność zapisu, cylindry prefiksów, certyfikaty całkowitoliczbowe i zmiana podstawy.
- **Testy na main:** tests/test_f191_base_expansions.py; commit **f404ed2b0013aad1fef8450ea3444c8236f568e1**, Git blob **72a32a66263270533ab72764e7062e45d7afe9be**. Lokalnie **12/12 unittest**, **12/12 pytest**, compileall kod 0. Sprawdzono dokładne przypadki na Fraction, podstawy 2–13, mianowniki do 99 oraz przykłady okresów i niejednoznaczności. Nie przeprowadzono pełnej regresji repozytorium ani mechanizacji wszystkich dowodów.
- **Podgląd lokalny:** Pandoc/XeLaTeX, FreeSerif 11 pt, A4, margines 20 mm, **3 strony**, liczba znaków tekstu 3048, 3132, 2676; PyMuPDF: 0 słów poza granicą 8 pt. SHA-256 PDF **b3b1c1c8e98c5a2986a9ab7883368a607819ab915d26fc127a9f27f1be14e94e**. Git blob źródła podglądu identyczny z odczytanym z main. PDF pozostaje lokalny.
- **Dokumentacja:** docs/DOWODY_F19_1_2026-10-31.md, commit **f63a77c41b5b9bd7ae844d652c33d7c8cee53b29**. GitHub zwrócił puste combined statuses i workflow runs dla commitu testowego; nie potwierdzono CI.
- **Integracja i bilans:** nie wykonano integracji z monolitem 0.20 (brak kompletnego źródła w repozytorium). **585/1222 stron bez zmian**; trzech stron podglądu nie doliczono. Historyczny wstęp i wcześniejsze rozdziały nietknięte. Bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F19.2 „Dlaczego pojawia się okres?” — opracować uzupełnienia wykraczające poza już obecne twierdzenie o automacie reszt i rzędzie multiplikatywnym, bez dublowania dowodów.

- **Korekta definicji F19.1:** commit **77eabb329faf6447d817c4c2b53c5c9c07c7c6b4** doprecyzowuje prefiks pusty i ogranicza definicję przedokresu do rozwinięć ostatecznie okresowych; po korekcie powtórzono 12/12 unittest, 12/12 pytest i kompilację 3-stronicowego PDF. Blob i SHA-256 w powyższej sekcji odpowiadają wersji skorygowanej.


## F19.2 — orbity reszt, symetrie i certyfikaty okresu (31 października 2026)

- **Punkt wyjścia:** odczytano F19.2 „Dlaczego pojawia się okres?” ze stron 204–205 bibliotecznego, 764-stronicowego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` oraz aktualny rejestr. W oryginale istnieją już argument skończonego automatu reszt, rząd multiplikatywny i granica Eulera; nowe uzupełnienie nie powtarza tych dowodów. Wskazano korektę zapisu `1/11=0,(09)` i `1/13=0,(076923)` bez modyfikowania oryginału.
- **Nowy manuskrypt na `main`:** `manuscript/tom-01/F19/F19.2_UZUPELNIENIE_ORBITY_I_OKRESY.md`; commity `f635f0eee3182ddb31bb067734f86c2dc499d94e` i `de4031def9ff3e423458053d6ddadbd9bed7a786`; końcowy Git blob `6bc2f6185a5c6f36962bbb03f16f39633c6be298`. Zawiera **6 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań**. Zakres: orbity reszt, obrót okresu, certyfikaty minimalności, granica Carmichaela, komplementarne połowy, częstość cyfr, rekonstrukcja mianownika oraz dwa kompletne ślady dzielenia.
- **Testy na `main`:** `tests/test_f192_period_orbits.py`, commity `be0882dda135a46dc569423ae2771a3b307307f7` i `8f1b395d4fe7d663990048c21b76134a4d87f9ca`; Git blob `bfd8e25f26f54021b9bca66b0b0a45b1aa10c765`. Lokalnie **15/15 unittest**, **15/15 pytest**, compileall bez błędów. Potwierdzono zgodność blobów z GitHub. Combined statuses puste — **brak potwierdzonego CI**. Testy skończonych przypadków nie zastępują formalnej weryfikacji wszystkich dowodów.
- **Podgląd lokalny:** Pandoc/XeLaTeX, **4 strony A4**, tekst na stronach **3098 / 3233 / 2929 / 2365** znaków; PyMuPDF: **0 słów poza marginesem 8 pt**; SHA-256 PDF `9264e49bbf1a4081194c9186473b7f715d9c381b43ff3e3cefe5deadddcdce27`. PDF nie jest binarium na GitHub.
- **Dowody:** `docs/DOWODY_F19_2_2026-10-31.md`, commit `c183221c207d7fd47fda93bcbc2a940d18b0529b`.
- **Integracja i bilans:** nie wykonano integracji z wydaniem 0.20 (brak kompletnego źródła i binarium w repo). **585/1222 stron bez zmian**; czterech stron podglądu nie doliczono. Historyczny wstęp i poprzednie rozdziały nienaruszone. Nie utworzono finalnego spisu treści ani nie rozpoczęto Tomu II.
- **Następny punkt:** F19.3 „Zaokrąglenie i błąd”; przed opracowaniem porównać z F19.1 i F18.2, aby nie powielać certyfikatów błędów.


## F19.3 — zaokrąglanie do parzystej, stabilność i propagacja błędów (31 października 2026)

- **Oryginał:** odczytano F19.3 „Zaokrąglenie i błąd” na stronach 206–207 bibliotecznego, 764-stronicowego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (nie jest to wydanie 0.20). Porównano F18.2, F19.1 i F19.2; nie powielono ich podstawowych konstrukcji. Rozwinięto regułę ties-to-even, komórki kwantyzacji, certyfikaty stabilności, podwójne zaokrąglenie, uwarunkowanie odejmowania, zewnętrzne otoczki siatkowe i propagację błędu.
- **Manuskrypt zapisany na `main`:** `manuscript/tom-01/F19/F19.3_UZUPELNIENIE_ZAOKRAGLENIE_I_STABILNOSC.md`; commit [aa3f058](https://github.com/mojealterego/Ontologia-Liczby-/commit/aa3f05869c3e46c0c56127d2d49a50d27db11f43), Git blob **f0428cb3f733ca5b3817573e01b735c4ed9d265a**, zgodny z lokalnym źródłem podglądu. **8 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań**.
- **Testy na `main`:** `tests/test_f193_rounding_stability.py`; commit [9a3f420](https://github.com/mojealterego/Ontologia-Liczby-/commit/9a3f4208a386d5ebf26dc259d75a7d6cc11082a2), Git blob **9bfe48bb2a661b9541a4d8719075b11d84167efa**. Lokalne **17/17 unittest**, **17/17 pytest**, `compileall` kod 0; weryfikacja na dokładnych ułamkach i w strukturze repozytorium. Testy skończone nie zastępują dowodów ogólnych.
- **Podgląd:** Pandoc/XeLaTeX, FreeSerif 11 pt, A4, margines 20 mm, **4 strony**, każda zawiera tekst, 0 słów poza marginesem bezpieczeństwa 8 pt; PDF SHA-256 **09da9a07ac3dba923ff26ede5e842ec913acb6922b3b376eade4a6aa9a5d69dd**. PDF lokalny, nie binarnie opublikowany na GitHub.
- **Dokumentacja dowodowa:** `docs/DOWODY_F19_3_2026-10-31.md`, commit [c08edd1](https://github.com/mojealterego/Ontologia-Liczby-/commit/c08edd10baa180dd9779b1663c8c086be6761035).
- **Niezweryfikowane:** puste GitHub combined statuses, brak potwierdzonego CI, pełnej regresji repozytorium, formalnej mechanizacji i niezależnej recenzji. Brak kompletnego źródła rzeczywistego monolitu 0.20 blokuje integrację.
- **Bilans:** **585/1222 stron bez zmian**; czterech stron podglądu nie doliczono. Historyczny wstęp i poprzednie rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II. Następny punkt należy wybrać po ponownym odczycie aktualnego rejestru i roboczego manuskryptu.


## F20.1 — proporcje, dodatnie klasy skalowania i stabilność ilorazu (31 października 2026)

- **Oryginał:** po F19.3 następny punkt to F20.1 „Stosunek i proporcja”, strony 208–209 roboczego 764-stronicowego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` z biblioteki. Roboczy PDF nie jest monolitem wydania 0.20. Nie powielono istniejących przykładów podziału 240 w stosunku 3:5 ani podstawowego dowodu mnożenia krzyżowego bez dodania warunków.
- **Manuskrypt na `main`:** `manuscript/tom-01/F20/F20.1_UZUPELNIENIE_STRUKTURALNE_PROPORCJE.md`, commit [0ec3d2b](https://github.com/mojealterego/Ontologia-Liczby-/commit/0ec3d2bb77b61fd9f5bf928ceb099beb14a40804), Git blob `87ee2d385ecfc76e5a65b36f538acf8256f43f24`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań**. Klasy dodatniego skalowania, wyznacznik, rząd jeden, podziały sum, łańcuchy proporcji, barycentra, jednorodność, mieszanie mas i dokładna perturbacja ilorazu.
- **Testy na `main`:** `tests/test_f201_ratios_proportions.py`, commit [556c3d8](https://github.com/mojealterego/Ontologia-Liczby-/commit/556c3d805caa0c5570db53413004eb93a035df01), blob `8f2a96a2b00794b9cc893ce01477224cd4c8771c`. Lokalne `unittest` **12/12 OK**, `pytest` **12 passed**, `compileall` kod 0; arytmetyka dokładna `fractions.Fraction`. Zgodność lokalnych blobów źródła i testów z GitHub potwierdzona. Nie jest to formalna mechanizacja wszystkich dowodów.
- **Podgląd lokalny:** Pandoc/XeLaTeX, FreeSerif, 11 pt, A4, margines 20 mm; **3 strony**, tekst 3085 / 2834 / 3336 znaków, 0 słów poza granicą bezpieczeństwa 8 pt. SHA-256 PDF `2eec17e94f5ad4dccd6e2b0668f71f8e2b35fba8ae7d27537041c4c0363e6083`. PDF nie jest binarium na GitHub.
- **Dokumentacja dowodowa:** `docs/DOWODY_F20_1_2026-10-31.md`, commit [add10df](https://github.com/mojealterego/Ontologia-Liczby-/commit/add10df64406d6d8150c2448f8d9effc0f90bb32), blob `dc9c45d0b9e50c9ec7549a0e11dee1a575926fd6`.
- **Niezweryfikowane:** brak niezależnej recenzji matematycznej, mechanizacji, pełnej regresji repozytorium i potwierdzonego przebiegu CI.
- **Integracja:** brak kompletnego źródła monolitu 0.20; nie scalono. **585/1222 stron bez zmian**, 3 stron podglądu nie doliczono. Historyczny wstęp, poprzednie rozdziały i roboczy PDF nie były modyfikowane. Bez finalnego spisu treści i bez Tomu II.
- **Następny punkt w kolejności roboczego manuskryptu:** F20.2 „Procent jako ułamek o mianowniku 100” (strony 210–211). Wymaga rozbudowy ponad już istniejące wzory składania zmian procentowych.


## F20.2 — struktura zmian procentowych, agregacja i stabilność (31 października 2026)

- **Punkt źródłowy:** F20.2 „Procent jako ułamek o mianowniku 100”, strony 210–211 bibliotecznego, 764-stronicowego roboczego ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf (nie monolit 0.20). Oryginał zawiera już podstawowe mnożniki, procent składany, punkty procentowe i zadanie odwrotne; uzupełnienie rozwija formalne założenia i nowe wyniki, bez edycji oryginału.
- **Źródło na main:** manuscript/tom-01/F20/F20.2_UZUPELNIENIE_ZMIANY_PROCENTOWE.md, commit [db09590](https://github.com/mojealterego/Ontologia-Liczby-/commit/db09590ece9c3ea78ba238e9bc744aea08b25616), Git blob c00506e03073e3f7d466b80fb3d5548abc0c76ca. Zawiera **8 definicji D1–D8, 11 twierdzeń T1–T11 z dowodami, 6 kontrprzykładów K1–K6 i 12 rozwiązanych zadań Z1–Z12**. Zakres: grupa dodatnich zmian procentowych, stopa odwrotna, składanie, agregacja ważona, zmiana podstawy indeksu, rozróżnienie punktów procentowych, niezmienniczość kolejności i certyfikowana stabilność.
- **Testy na main:** tests/test_f202_percent_changes.py, commit [3bf6283](https://github.com/mojealterego/Ontologia-Liczby-/commit/3bf628381ba228a59a5a3b565d3eb4ce0799b4e3), Git blob d706bcfad6bc2e78162dc43a70bc0a7ad7a96589. Lokalne **17/17 unittest**, **17/17 pytest**, compileall kod 0. Kontrole używają dokładnej arytmetyki Fraction; lokalne bloby i bloby z main identyczne. GitHub combined statuses i workflow runs dla commitu testowego są puste; **nie potwierdzono CI**.
- **Podgląd lokalny:** Pandoc/XeLaTeX, FreeSerif 11 pt, A4, margines 20 mm, **3 strony**, tekst odpowiednio 3094 / 2882 / 2564 znaków; PyMuPDF: 0 słów poza granicą bezpieczeństwa 8 pt; SHA-256 PDF a44efa49b2c45ba0a71ce1cd8f9631a8ca7770f747caaf997c870959de0f6d6c. Pierwszą i ostatnią stronę obejrzano. PDF nie jest binarium na GitHub.
- **Dokumentacja dowodowa:** docs/DOWODY_F20_2_2026-10-31.md, commity [52f6354](https://github.com/mojealterego/Ontologia-Liczby-/commit/52f635465d49bb57b049071d617e6faf0b487b44) i [cdff829](https://github.com/mojealterego/Ontologia-Liczby-/commit/cdff829d392d8eeefa64773d7bd93a9422289aa3).
- **Niezweryfikowane:** brak pełnej regresji repozytorium, mechanizacji dowodów, niezależnej recenzji matematycznej i integracji z rzeczywistym wydaniem 0.20.
- **Bilans:** **585/1222 stron bez zmian**; trzech stron podglądu nie doliczono. Historyczny wstęp i wcześniejsze rozdziały nietknięte. Bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** F20.3 „Skala i wymiar” na stronach 212–213 roboczego manuskryptu; rozwinąć precyzyjne twierdzenia o analizie wymiarowej, przekształceniach jednostek i propagacji błędów, bez dublowania obecnych przykładów mapowych.

- **Korekty po przeglądzie:** T8 zawężono do udziałów [0,1], commit [4741598](https://github.com/mojealterego/Ontologia-Liczby-/commit/4741598054c816816e3f8f7732d53362bf0c3091); w teście K4 usunięto float, commit [0c8d4f9](https://github.com/mojealterego/Ontologia-Liczby-/commit/0c8d4f9d59b4fe6b14009ba23b80ecc56a45b2ea). Po zmianach ponowiono pełne lokalne 17/17 unittest, 17/17 pytest, compileall i kompilację PDF. Bloby i SHA-256 powyżej dotyczą stanu końcowego.


## F20.3 — struktura wymiarów, niezmienniki i certyfikaty błędów (31 października 2026)

- **Źródło oryginalne:** F20.3 „Skala i wymiar”, strony 212–213 bibliotecznego, 764-stronicowego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf`; nie jest to źródło wydania 0.20. W oryginale istnieją już przykłady mapowe, 72 km/h, skalowanie długości/pola/objętości i wstępna propagacja błędów. Nie powielono ich jako nowych dowodów.
- **Manuskrypt na `main`:** `manuscript/tom-01/F20/F20.3_UZUPELNIENIE_ANALIZA_WYMIAROWA.md`, commit [f0d76c6](https://github.com/mojealterego/Ontologia-Liczby-/commit/f0d76c6510d2aef3a5261171ebdc1fce51491b3c), Git blob `e827daa9014ce48e09703df1d4ab3a0aa8160897`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań**. Model wymiarów `Z^3`, typowane działania, konwersje jednostek, skale afiniczne, miara geometryczna, dokładna propagacja błędu potęg, przedziały i bezwymiarowe niezmienniki macierzy wymiarów.
- **Testy na `main`:** `tests/test_f203_dimensions.py`, commit [c8c6a3e](https://github.com/mojealterego/Ontologia-Liczby-/commit/c8c6a3e052b72db9d54bd51a6fbdff4f194330ff), Git blob `56f644250d2b5b4b273a837a3eb60eb006a4303b`. Lokalnie **20/20 unittest OK**, **20/20 pytest passed**, `compileall` kod 0. Weryfikacja skończonych przypadków `Fraction`, nie formalny dowód wszystkich twierdzeń. Ponowny odczyt obu źródeł z GitHub potwierdził zgodność Git blob z lokalnym `git hash-object`.
- **PDF:** lokalna kompilacja Pandoc/XeLaTeX, FreeSerif 11 pt, A4, margines 20 mm, **3 strony**, tekst odpowiednio **3199 / 2787 / 2252** znaków; PyMuPDF: **0 słów poza granicą 8 pt**. SHA-256 `ee6870b44bc3b02a980af6f432ab64fbbc32118e2d01ea9fa0eb4d84bfc73a2a`. PDF pozostaje artefaktem lokalnym, nie plikiem binarnym w repozytorium.
- **Dokumentacja dowodowa:** `docs/DOWODY_F20_3_2026-10-31.md`, commit [3105de3](https://github.com/mojealterego/Ontologia-Liczby-/commit/3105de3bac78a326fc672e919835baa5564246a5).
- **CI:** combined statuses oraz workflow runs dla commitu testowego zwróciły puste listy; brak potwierdzonego CI. Brak pełnej regresji repozytorium, formalnej mechanizacji i niezależnej recenzji matematycznej.
- **Integracja:** brak kompletnego źródła rzeczywistego monolitu 0.20. **585/1222 stron bez zmian**; 3 stron podglądu nie doliczono. Historyczny wstęp i wcześniejsze rozdziały nienaruszone. Nie utworzono końcowego spisu treści i nie rozpoczęto Tomu II.
- **Następny punkt:** F21.1 „Potęgowanie” (strona 214 roboczego manuskryptu, sprawdzona po zakończeniu F20.3). Nie powielać istniejących dowodów praw potęgowania; zweryfikować zakres dla monoidów nieprzemiennych, wykładników ujemnych i wymiernych.


## F21.1 — struktury potęg, kryteria dziedziny i certyfikaty wymierności (31 października 2026)

- **Weryfikacja oryginału:** strony 214–218 bibliotecznego, 764-stronicowego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf`. Zastane definicje i przykłady potęgowania nie zostały nadpisane; roboczy PDF nie jest monolitem wydania 0.20.
- **Nowy manuskrypt na `main`:** `manuscript/tom-01/F21/F21.1_UZUPELNIENIE_STRUKTURY_POTEG.md`, commit [41f5fde](https://github.com/mojealterego/Ontologia-Liczby-/commit/41f5fde82fc390a596dc54a5965ef1590fe63de5), Git blob `68d4fb9498db7b94a9ca74f9ad7061f3634816c4`. Zawiera **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów i 12 zadań rozwiązanych**. Zakres: morfizmy potęgowe, jednostki monoidu, komutowanie, sprzężenia, rząd elementu, redukcja modularna, ujemne podstawy, wartościowania pierwsze, kryterium wymierności potęg i Frobenius w charakterystyce pierwszej.
- **Testy na `main`:** `tests/test_f211_power_structures.py`, commit [82ec10b](https://github.com/mojealterego/Ontologia-Liczby-/commit/82ec10baff6aa5f7b706bcd8d6da343290ad8e4a), Git blob `f345a99a276c352a46fabe9d8175598969cc91ea`. Lokalnie **24/24 unittest OK**, **24/24 pytest passed**, `compileall` kod 0; testy używają dokładnej arytmetyki `Fraction` i obejmują m.in. 36 par odwracalnych macierzy 2×2 nad F₂. Bloby lokalne i ponownie odczytane z GitHub są identyczne.
- **Podgląd lokalny:** Pandoc/XeLaTeX, FreeSerif 11 pt, A4, margines 16 mm; **3 strony**, tekst wyekstrahowany odpowiednio **3511 / 3333 / 2976** znaków, **0 słów poza granicą 8 pt** według PyMuPDF. SHA-256 PDF `67a317d7edcf4cf49dec1d0835926ca6463540e4cee92ac02eb6d46a1f917804`. PDF nie jest binarium w repozytorium.
- **Dokumentacja dowodowa:** `docs/DOWODY_F21_1_2026-10-31.md`, commit [78535f7](https://github.com/mojealterego/Ontologia-Liczby-/commit/78535f789c1a7fe579201574dc84aec3e4853aed).
- **Kontrola zmian:** od HEAD `e7db2335` do commitu testowego dodano tylko nowe pliki manuskryptu i testów; historyczny wstęp oraz wcześniejsze rozdziały nie były modyfikowane. Combined statuses i workflow runs GitHub dla commitu testowego są puste — **brak potwierdzonego CI**.
- **Niezweryfikowane:** brak pełnej regresji repozytorium, formalnej mechanizacji dowodów, niezależnej recenzji matematycznej i integracji z rzeczywistym źródłem monolitu 0.20.
- **Bilans:** **585/1222 stron bez zmian**; 3 strony podglądu nie zostały doliczone. Nie utworzono końcowego spisu treści ani nie rozpoczęto Tomu II.
- **Następny punkt:** F21.2 „Pierwiastek”, zaczynający się na stronie 218 roboczego manuskryptu. Przed rozbudową porównać z już obecnym dowodem niewymierności pierwiastka z 2, istnieniem pierwiastków w R i pułapkami dziedziny, aby uniknąć duplikacji.


## F21.2 — certyfikowane pierwiastki, normy i oszacowania (31 października 2026)

- **Oryginał:** F21.2 „Pierwiastek” na stronach 219–223 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony, **nie** wydanie 0.20). Porównano definicję, niewymierność √2, istnienie, pierwotną nierówność Höldera, Newtona i zadania; niczego z oryginału nie nadpisano.
- **Źródło na `main`:** `manuscript/tom-01/F21/F21.2_UZUPELNIENIE_CERTYFIKOWANE_PIERWIASTKI.md`. Utworzenie [`97f7ba6`](https://github.com/mojealterego/Ontologia-Liczby-/commit/97f7ba6883ee671e0b2bda29043b06162d381f94); korekta uwzględniająca oryginalną nierówność Höldera [`dee9c0c`](https://github.com/mojealterego/Ontologia-Liczby-/commit/dee9c0c92f75c72e16b81be3e923ef4243911666). Końcowy Git blob `fa06573833207b5f468cbea6d18601ea11e5ecf2`. **8 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań**. Zakres: kwadraty wymierne, rozkład bezkwadratowy, `isqrt`, bisekcja z certyfikatem, dokładna różnica pierwiastków, ostrość stałej Höldera, Lipschitz na przedziałach dodatnich, Newton z dokładną resztą, norma ciała kwadratowego i dokładne cyfry dziesiętne.
- **Testy na `main`:** `tests/test_f212_certified_roots.py`, commit [`55abac9`](https://github.com/mojealterego/Ontologia-Liczby-/commit/55abac9dfa76a4aefa49977ff8d033d0272a8186), Git blob `ddb58ba3c72a73047e766992e5f1a76f1799d2a4`. Lokalnie **24/24 unittest OK**, **24/24 pytest passed**, `compileall` kod 0. Ponowny odczyt obu plików z GitHub potwierdził identyczne bloby jak lokalne `git hash-object`. Testy przypadków nie zastępują formalnych dowodów.
- **Podgląd lokalny:** Pandoc/XeLaTeX, A4, FreeSerif 11 pt, margines 19 mm; **4 strony**, wyekstrahowano **2527 / 2986 / 2916 / 2298** znaków, **0 słów poza granicą 8 pt**. SHA-256 PDF `c555b9c0ecd82ee1826f970734d61f34001806d5677eb1e774ef2e316d42e95d`. PDF jest artefaktem lokalnym, nie plikiem binarnym w repozytorium.
- **Dowody wykonania:** `docs/DOWODY_F21_2_2026-10-31.md`, commit [`4994063`](https://github.com/mojealterego/Ontologia-Liczby-/commit/499406339344a05bc0a2c499d7a1f57274ea6cbf).
- **Niezweryfikowane:** brak pełnej regresji repozytorium, niezależnej recenzji, mechanizacji wszystkich dowodów i testu integracyjnego wydania 0.20. Combined statuses dla commitu testowego: 0; PR-filtered workflow runs: 0; **brak potwierdzonego CI**.
- **Integracja i bilans:** brak rzeczywistego źródła i binarnego monolitu **0.20**. **585/1222 stron bez zmian**, czterech stron podglądu nie doliczono. Historyczny wstęp i poprzednie rozdziały nienaruszone. Nie utworzono końcowego spisu treści ani nie rozpoczęto Tomu II.
- **Następny punkt:** sprawdzić F21.3 „Logarytm” w roboczym manuskrypcie, porównać z już istniejącymi prawami logarytmów i rozwinąć tylko brakujące wyniki.


## F21.3 — wymierne certyfikaty logarytmów (31 października 2026)

- **Kontrola źródła:** odczytano F21.3 „Logarytm” na stronach 224–229 bibliotecznego, 764-stronicowego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (nie monolitu wydania 0.20). Oryginał obejmuje już prawa logarytmów, izomorfizm grup, pochodną, całkę, logarytm zespolony, szereg ln(1+u), zastosowania i zadania. Nowy tekst nie powiela ich jako własnych wyników.
- **Manuskrypt na `main`:** `manuscript/tom-01/F21/F21.3_UZUPELNIENIE_CERTYFIKATY_LOGARYTMOW.md`, commit [0ec2a77](https://github.com/mojealterego/Ontologia-Liczby-/commit/0ec2a771e9dd14646b53c1a91f9e37480f711e64), Git blob `cd98f5112ab4c04e79b4721515248ad7245d147b`. **7 definicji, 11 twierdzeń z dowodami, 6 kontrprzykładów i 12 zadań rozwiązanych.** Kryterium wymierności przez wartościowania, dokładne porównania, symetryczny szereg z certyfikowaną resztą, redukcja dwójkowa, przedziałowy iloraz i log-sum-exp.
- **Testy na `main`:** `tests/test_f213_certified_logarithms.py`, końcowy commit [a8e683d](https://github.com/mojealterego/Ontologia-Liczby-/commit/a8e683da601cdf7b9b65bd9df04833eb8c22b79b), Git blob `64d2e51725af4147779db71458fdb309b8a7b3fb`. Lokalnie **24/24 unittest OK, 24/24 pytest passed, compileall kod 0**. Ponowny odczyt GitHub potwierdził identyczność blobów z lokalnymi `git hash-object`.
- **Podgląd PDF:** Pandoc/XeLaTeX, A4, FreeSerif 11 pt, margines 19 mm, **4 strony**, tekst 2484 / 2296 / 2569 / 2609 znaków, 0 słów poza granicą 8 pt. SHA-256 `7f6751531fae6dbd1a61928ca94ee1ec19f50933e26fb050a566113dd1e865b0`. PDF lokalny, nie zapisany binarnie na GitHub.
- **Protokół dowodowy:** `docs/DOWODY_F21_3_2026-10-31.md`, commit [6eaae79](https://github.com/mojealterego/Ontologia-Liczby-/commit/6eaae7989eafef317bf8b2b67a89774e1557bad7).
- **Niezweryfikowane:** brak pełnej regresji repozytorium, formalnej mechanizacji wszystkich dowodów i niezależnej recenzji matematycznej. Combined statuses GitHub i powiązane workflow runs dla commitu testowego są puste: **brak potwierdzonego CI**.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**; czterech stron podglądu nie doliczono. Historyczny wstęp, poprzednie rozdziały i oryginalny PDF nietknięte. Nie utworzono finalnego spisu treści ani nie rozpoczęto Tomu II.
- **Następny etap:** zweryfikować kolejny rzeczywisty punkt F21.4 lub F22.1 według oryginalnego manuskryptu i rozwijać wyłącznie brakujące rezultaty.
