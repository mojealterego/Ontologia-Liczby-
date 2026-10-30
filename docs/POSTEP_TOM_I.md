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
