# ONTOLOGIA LICZBY — kontrola rzeczywistego postępu Tomu I

**Data aktualizacji:** 2 listopada 2026  
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
- **Następny etap (potwierdzony odczytem strony 230):** F22.1 „Litera jako zmienna” w rozdziale „Algebra: symbole, wyrażenia i tożsamości”. Oryginał ma już rozróżnienie zmiennych wolnych i związanych, ewaluację wielomianu oraz warunki przekształceń równań; rozwinąć brakujące wyniki bez ich powielania.


## F22.1 — zmienne, wielomiany formalne i semantyka podstawienia (1 listopada 2026)

- **Weryfikacja oryginału:** strony 230–234 bibliotecznego, 764-stronicowego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (nie jest to monolit wydania 0.20). W oryginale już istnieją zmienne wolne i związane, różnica kwadratów, ewaluacja wielomianu, zasada tożsamości nad nieskończonym podzbiorem ciała, analiza parametru `a` oraz ostrzeżenia o skracaniu przez zero; nowy suplement nie nadpisuje tych treści.
- **Nowy manuskrypt na `main`:** `manuscript/tom-01/F22/F22.1_UZUPELNIENIE_SEMANTYKA_ZMIENNYCH.md`; commit [2dc37c4](https://github.com/mojealterego/Ontologia-Liczby-/commit/2dc37c46c8f0d174a9f525fb3c3aac787133bce2), korekta [df156a8](https://github.com/mojealterego/Ontologia-Liczby-/commit/df156a8a8afca11d55be7f245cae8cd90a5ed699), końcowy Git blob `89ff8d696b177d267ffc8958871236b82e34cab2`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.** Zakres: uniwersalność ewaluacji, jądro `(X-a)`, liczba pierwiastków, funkcje wielomianowe nad ciałami skończonymi, interpolacja Lagrange'a, podstawienie bez przechwycenia, równoważność równań i pochodna formalna.
- **Testy na `main`:** `tests/test_f221_variables_polynomials.py`; commit [61c6a08](https://github.com/mojealterego/Ontologia-Liczby-/commit/61c6a080931bfc25daaf5fe15422d2091f1892b1), Git blob `014eccf5a01ab0ebc0e4888131c12e1e3ca800d1`. Lokalnie **20/20 unittest OK**, **20/20 pytest passed**, `compileall` kod 0. Ponowny odczyt z GitHub potwierdził zgodność Git blob z lokalnym `git hash-object`. Skończone testy nie są formalnym dowodem wszystkich twierdzeń.
- **PDF lokalny:** Pandoc/XeLaTeX, A4, FreeSerif 10 pt, margines 16 mm; **3 strony**; tekst wyekstrahowany **3419 / 4393 / 2862** znaków; **0 słów poza granicą 8 pt**. SHA-256 PDF `2af09fd1ce9e41ee16be58b931071146616753088a5cd4b3b73615b90b1aa4a1`. Podgląd nie jest binarium zapisanym w repozytorium.
- **Dokumentacja wykonania:** `docs/DOWODY_F22_1_2026-11-01.md`; commit [ef5ed9e](https://github.com/mojealterego/Ontologia-Liczby-/commit/ef5ed9eea9c375b6c6f4862b7af461156a63bbfc), korekta [82652c9](https://github.com/mojealterego/Ontologia-Liczby-/commit/82652c9ff82438a8f3140ed710c22b7d084bab99).
- **Niezweryfikowane:** brak pełnej regresji całego repozytorium, mechanizacji wszystkich dowodów i niezależnej recenzji. GitHub combined statuses: 0; PR-filtered workflow runs: 0 — **brak potwierdzonego CI**.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**; 3 stron nowego podglądu nie doliczono. Historyczny wstęp i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F22.2 „Upraszczanie i dziedzina” od strony 235 roboczego oryginału. W źródle już są usuwalne osobliwości i warunki skracania; rozwinąć teorię bez ich powielania.


## F22.2 — dziedziny składniowe i certyfikaty przekształceń (1 listopada 2026)

- **Oryginał:** strony 235–239 bibliotecznego, 764-stronicowego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (nie wydanie 0.20). Zastane: skracanie z wyłączeniami, usuwalne i nieusuwalne osobliwości, równania wymierne, pierwiastki i powtarzalne zadania. Nie modyfikowano oryginału.
- **Manuskrypt na `main`:** `manuscript/tom-01/F22/F22.2_UZUPELNIENIE_DZIEDZINY_I_CERTYFIKATY.md`; commit [3bf10bd](https://github.com/mojealterego/Ontologia-Liczby-/commit/3bf10bdfac1083cb180786acb02e769888860c3a), Git blob `4727c5fc14b98ee924c29ac02404c42c9131345d`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 zadań rozwiązanych.** Zakres: funkcje częściowe, certyfikaty wyłączeń, normalizacja i jej jednoznaczność, rzędy zer, równoważność strzeżona, rozwiązania równań wymiernych, analiza znaków.
- **Testy na `main`:** `tests/test_f222_domains.py`; commit [4423f89](https://github.com/mojealterego/Ontologia-Liczby-/commit/4423f89e7d88a7345e2138567c92598b3deab73c), Git blob `a52870d096f4cf705d776654ed0232d8f7211ed4`. Lokalnie **20/20 unittest OK**, **20/20 pytest passed**, `compileall` kod 0. Odczytane z GitHub bloby zgodne z lokalnymi `git hash-object`. Testy przypadków nie zastępują recenzji matematycznej.
- **Podgląd lokalny:** Pandoc/XeLaTeX, FreeSerif 10 pt, A4, margines 17 mm; **3 strony**, tekst **3498 / 3721 / 1545** znaków; **0 słów poza marginesem 8 pt**. SHA-256 PDF `9b2c222e110d07ab7bdd00f48fa778462182ab6d5b44edf94e3d984de4625775`. PDF nie został opublikowany binarnie w repozytorium.
- **Protokół dowodowy:** `docs/DOWODY_F22_2_2026-11-01.md`; commit [d3c16f7](https://github.com/mojealterego/Ontologia-Liczby-/commit/d3c16f741dee689f9be10e94d64866c59df0ab21).
- **Niezweryfikowane:** brak pełnej regresji repozytorium, niezależnej recenzji i mechanizacji wszystkich dowodów; GitHub combined statuses 0, PR-filtered workflow runs 0, więc **CI niepotwierdzone**.
- **Blokada:** brak kompletnego źródła i binarnego monolitu 0.20. **585/1222 stron bez zmian**, trzech stron podglądu nie doliczono. Historyczny wstęp i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F22.3 „Przykład rozkładu” — zbadać oryginał przed dalszym opracowaniem.


## F22.3 — pierwotność wielomianów i certyfikaty rozkładu (1 listopada 2026)

- **Oryginał:** odczytano strony 240–244 bibliotecznego, 764-stronicowego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (nie monolit wydania 0.20). W oryginale są już wzory Viète’a, pierwiastki wymierne, twierdzenie o reszcie, krotności, rozkłady kwadratowe i 24 zadania. Nowy suplement nie nadpisuje ani nie przedstawia ich jako nowych.
- **Manuskrypt na `main`:** `manuscript/tom-01/F22/F22.3_UZUPELNIENIE_ROZKLAD_CERTYFIKATY.md`; utworzenie [49ae618](https://github.com/mojealterego/Ontologia-Liczby-/commit/49ae61804a9d99d5f9c68ce310394e01fbf4b78e), korekta [face7ac](https://github.com/mojealterego/Ontologia-Liczby-/commit/face7ace294acabd75e8a4c2a7ab97d27d719232), Git blob `90450a7b4ac0ee091309b7fca9ed98ecf1ccd511`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań**. Tematy: lemat Gaussa, redukcja modulo p, Eisenstein, NWD z pochodną, charakterystyka p, część liniowa i certyfikaty Bézouta.
- **Testy na `main`:** `tests/test_f223_factor_certificates.py`, commit [361b6c1](https://github.com/mojealterego/Ontologia-Liczby-/commit/361b6c1df1a92340a35bdad0dd9b63f4940026ff), Git blob `567a171ac77ed69be61beb6700712e4f03927841`. Lokalnie **24/24 unittest OK**, **24/24 pytest passed**, `compileall` kod 0; SymPy 1.14.0 i dokładne operacje na wielomianach. Bloby lokalne zgodne z ponownie odczytanymi z GitHub. Testy skończonych przykładów nie stanowią mechanizacji dowodów.
- **Podgląd lokalny:** Pandoc/XeLaTeX, A4, FreeSerif 10 pt, margines 18 mm, **3 strony**; PyMuPDF: 0 słów poza granicą bezpieczeństwa 8 pt. SHA-256 PDF `4e1a3aa21cc98740a43a5f821892f7a5f8e3310d0e5126d2b5cc0a32ad560689`. PDF lokalny, nie zapisany binarnie w repozytorium.
- **Dokumentacja dowodowa:** `docs/DOWODY_F22_3_2026-11-01.md`, commit [0523d2e](https://github.com/mojealterego/Ontologia-Liczby-/commit/0523d2ebe103733c0dc5ae3705415803c624b898).
- **Niezweryfikowane:** brak pełnej regresji repozytorium, niezależnej recenzji matematycznej i mechanizacji wszystkich dowodów. GitHub combined statuses i powiązane workflow runs dla commitu testowego puste — **CI niepotwierdzone**.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu 0.20. **585/1222 stron bez zmian**; 3 stron podglądu nie doliczono. Historyczny wstęp, wcześniejsze rozdziały i oryginalny PDF nietknięte; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F23.1 „Równanie liniowe”; sprawdzić oryginalne ujęcie przed dalszym rozwinięciem.


## F23.1 — włókna przekształceń, kongruencje i certyfikaty (1 listopada 2026)

- **Oryginał:** F23.1 „Równanie liniowe”, strony 245–249 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony; **nie** monolit wydania 0.20). Istniejące przypadki nad ciałem, równoważność przekształceń, parametry, nierówności i 24 zadania nie zostały powielone ani nadpisane.
- **Manuskrypt na `main`:** `manuscript/tom-01/F23/F23.1_UZUPELNIENIE_WLOKNA_I_KONGRUENCJE.md`, commit [2db4b77](https://github.com/mojealterego/Ontologia-Liczby-/commit/2db4b770c456f67651d3c6aaba0ef19af42aef62), Git blob `3d5a855de3d8f28dd11173be4f35811bf023e806`. **8 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.** Zakres: anihilator i włókno, osiągalność w pierścieniach, kongruencje liniowe, certyfikaty Bézouta, CRT, błąd wsteczny i stabilność.
- **Testy na `main`:** `tests/test_f231_linear_fibers.py`, commit [26baee0](https://github.com/mojealterego/Ontologia-Liczby-/commit/26baee0f20c15201470caa58d8d17c8399014042), Git blob `d92b43054326cb43a39ddd6b32dbd4243f575680`. Lokalnie **26/26 unittest OK**, **26/26 pytest passed**, `compileall` kod 0. Obejmują dokładne `Fraction`, pełne małe przestrzenie reszt i certyfikaty. Ponowny odczyt z GitHub potwierdził identyczność blobów z lokalnym `git hash-object`.
- **Podgląd lokalny:** Pandoc/XeLaTeX, FreeSerif 11 pt, A4, margines 18 mm, **3 strony**, tekst **3115 / 2966 / 2461** znaków, **0 słów poza granicą 8 pt**. SHA-256 PDF `d8f4cb767c4b09adfe31ad9419dc1eec2f4b031da629bd4e8f659fec6ae741b0`. PDF lokalny, nie opublikowany binarnie na GitHub.
- **Protokół dowodowy:** `docs/DOWODY_F23_1_2026-11-01.md`, commit [3e6d927](https://github.com/mojealterego/Ontologia-Liczby-/commit/3e6d9274ca5a871d6b0dc48f90e97a84751954c0).
- **Niezweryfikowane:** brak pełnej regresji repozytorium i mechanizacji wszystkich dowodów. GitHub combined statuses dla commitu testowego: pusta lista — **CI niepotwierdzone**. Lokalne testy nie zastępują dowodów ogólnych.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**, 3 stron podglądu nie doliczono. Historyczny wstęp i poprzednie rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F23.2 „Równanie kwadratowe” od strony 250 roboczego manuskryptu. Najpierw porównać z istniejącymi dowodami wyróżnika, Viète’a i przypadków zdegenerowanych.


## F23.2 — ślad, charakterystyka 2 i podnoszenie modularne (1 listopada 2026)

- **Oryginał:** zweryfikowano strony 250–259 bibliotecznego 764-stronicowego ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf, który nie jest monolitem wydania 0.20. Oryginał ma już klasyczny wzór kwadratowy, Viète’a, pierwiastki zespolone, elementy arytmetyki modularnej i bisekcji. Nie modyfikowano oryginału ani wstępu historycznego.
- **Manuskrypt na main:** manuscript/tom-01/F23/F23.2_UZUPELNIENIE_CIALA_SKONCZONE_I_LIFTING.md; commit [92f0422](https://github.com/mojealterego/Ontologia-Liczby-/commit/92f0422461dfe2f6ce469afa5eb75f12579b14cd); Git blob 0438fdc808a7f622b8fa0a07a1cebea9b7d9cdb0. **6 definicji, 11 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.** Nowe rozszerzenie: ślad i Artin–Schreier w charakterystyce 2, rozdzielność, Hensel dla prostych pierwiastków, certyfikaty przedziałowe.
- **Testy na main:** tests/test_f232_quadratic_certificates.py; commit [9e27522](https://github.com/mojealterego/Ontologia-Liczby-/commit/9e275229c6880c05160bf0ca7080e14f74dfab54); Git blob 34c9cd9a60a0d416cc28535a302348c9ad2d210f. Lokalnie **24/24 unittest OK, 24/24 pytest passed, compileall kod 0**; porównanie Git blob z lokalnym git hash-object potwierdziło zgodność.
- **PDF lokalny:** Pandoc/XeLaTeX, FreeSerif 10 pt, A4, margines 18 mm; **3 strony**, tekst 4259 / 3931 / 2318 znaków, **0 słów poza granicą 8 pt**. SHA-256 PDF 99e2a7a4b7db75e8d858386a3843160d6a951acda40a2ec53382acaaec462e46. PDF nie został opublikowany jako binarium na GitHub.
- **Protokół dowodowy:** docs/DOWODY_F23_2_2026-11-01.md; commit [a8c810d](https://github.com/mojealterego/Ontologia-Liczby-/commit/a8c810d958535dc44f886e780e09bc1cf5ec826c).
- **Niezweryfikowane:** brak pełnej regresji repozytorium, niezależnej recenzji matematycznej i formalnej mechanizacji dowodów. GitHub combined status dla commitu testowego: pending, 0 statusów; Actions workflow runs: 0 — **brak potwierdzonego CI**.
- **Blokada integracji:** brak źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**, trzech stron podglądu nie doliczono. Historyczny wstęp i poprzednie rozdziały nietknięte; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** sprawdzić F23.3 w rzeczywistym roboczym manuskrypcie przed opracowaniem, nie powielać wyników już obecnych w F23.2.


## F23.3 — certyfikaty nierówności i izolacja pierwiastków (1 listopada 2026)

- **Oryginał:** sprawdzono strony **260–269** bibliotecznego roboczego ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf (764 strony, nie wydanie 0.20). Oryginał ma już tabele znaków, nierówności klasyczne, argumenty pochodnej i ogólną ideę certyfikatu. Nowe rozszerzenie skupia się na dokładnym Hornerze przedziałowym, ciągu Sturma i izolacji pierwiastków. F23.4 zaczyna się na stronie 270.
- **Manuskrypt na main:** manuscript/tom-01/F23/F23.3_UZUPELNIENIE_CERTYFIKATY_NIEROWNOSCI.md, commit [18396a1](https://github.com/mojealterego/Ontologia-Liczby-/commit/18396a1dce4b5f653bd8efba32f048d81f12e898), korekta [efeaabe](https://github.com/mojealterego/Ontologia-Liczby-/commit/efeaabe41f3c467f062026e9d2a8b2f19c6373ed); blob ed77e7c3806d6a95283f13efb0c0c3cbe326249e. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.**
- **Testy na main:** tests/test_f233_inequality_certificates.py, commit [1c3d10b](https://github.com/mojealterego/Ontologia-Liczby-/commit/1c3d10b115fffd82e8cffbbd991cef6fd0ef3872), blob 9a4b6686d645722b88f0d4a7f44cf259eaf4866f. W lokalnym odpowiedniku: **26/26 unittest OK, 26/26 pytest passed, compileall kod 0**. Nie potwierdzono bajtowej identyczności lokalnego testu z plikiem main.
- **PDF:** lokalny Pandoc/XeLaTeX, A4, 10 pt, margines 18 mm, **3 strony**, tekst 3872/4703/1661 znaków, 0 słów poza marginesem 8 pt. SHA-256 3d0aab49f012168845bc278e12b044c99d432bbdbd406f16312eba04633bf6b8. Podgląd pochodzi z rozszerzonej lokalnej redakcji, **nie z dokładnego blobu main**; kompilacja opublikowanego źródła nadal wymaga odtworzenia.
- **Protokół:** docs/DOWODY_F23_3_2026-11-01.md, commit [54bc00e](https://github.com/mojealterego/Ontologia-Liczby-/commit/54bc00eab13487a995c3152616851aa4b88edae7). Nie potwierdzono zielonego GitHub CI, pełnej regresji, formalnej mechanizacji ani niezależnej recenzji matematycznej.
- **Bilans:** brak rzeczywistego źródła i binarnego monolitu 0.20. **585/1222 stron bez zmian**, bez doliczania 3 stron podglądu. Historyczny wstęp i poprzednie rozdziały nienaruszone; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F23.4 „Układ dwóch równań”, od strony 270 roboczego manuskryptu; przed uzupełnieniem sprawdzić już istniejące eliminację Gaussa, jądro, rząd i rozkład LU.


## F23.4 — układy całkowitoliczbowe i certyfikaty Smitha (1 listopada 2026)

- **Oryginał:** odczytano s. 270–279 bibliotecznego roboczego ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf (764 strony, nie monolit wydania 0.20). Wcześniej opisano już eliminację Gaussa, Cramera, rząd, jądro, LU/QR, Schura i uwarunkowanie; nowe opracowanie rozpatruje całkowitoliczbowe zbiory rozwiązań.
- **Manuskrypt na main:** manuscript/tom-01/F23/F23.4_UZUPELNIENIE_UKLADY_CALKOWITOLICZBOWE.md, commit [549b25c](https://github.com/mojealterego/Ontologia-Liczby-/commit/549b25cf7e0f840c64cbc7e94199011231ea97f7), Git blob 267cbd8c7961f6bb6f72a7d277aac031aed57aca. **8 definicji, 11 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań.** Zakres: postać Smitha 2×2, kryteria podzielności, kraty, przypadek rzędu jeden, certyfikaty modularne, mianowniki wymiernych rozwiązań.
- **Testy na main:** tests/test_f234_integer_systems.py, commit [864dec2](https://github.com/mojealterego/Ontologia-Liczby-/commit/864dec22bb6570976b6173db5a434c3bd5f30a06), Git blob 70ab6a75f5d03284026f519c91bd7fdf083ec12f. Lokalnie **29/29 unittest OK, 29/29 pytest passed, compileall kod 0**; weryfikacja 625 macierzy 2×2 względem SymPy Smith normal form. Bajtowa zgodność źródeł z main potwierdzona Git blob SHA.
- **PDF lokalny:** Pandoc/XeLaTeX z dokładnego opublikowanego źródła; **3 strony A4** (595,28 × 841,89 pt), 3957 / 4218 / 1148 znaków, 0 słów poza marginesem bezpieczeństwa 8 pt. SHA-256 PDF 33cf3f6e44d71749b64758e626285752235c43beb26e0ac460037a2b93533a64. PDF nie został opublikowany binarnie w repozytorium.
- **Protokół dowodowy:** docs/DOWODY_F23_4_2026-11-01.md, commit [3e12ada](https://github.com/mojealterego/Ontologia-Liczby-/commit/3e12adae87fa297cd39abd66fb665552ed9ce3df).
- **Niezweryfikowane:** brak pełnej regresji repozytorium i formalnej mechanizacji wszystkich dowodów; GitHub combined statuses 0 i Actions runs dla commitu testowego 0, więc **CI niepotwierdzone**.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**; 3 stron podglądu nie doliczono. Historyczny wstęp, wcześniejsze rozdziały i oryginalny PDF niezmienione; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F24.1 „Odcinek i kąt” od strony 280 roboczego manuskryptu, po sprawdzeniu istniejącego ujęcia Pitagorasa, Talesa, podobieństwa i pomiaru.

## F24.1 — dokładne predykaty geometrii płaskiej (1 listopada 2026)

- **Oryginał:** odczytano s. 280–284 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony; nie monolit wydania 0.20). Są tam już Pitagoras, Tales, podobieństwo, cosinusy, kąty wpisane i 24 zadania; suplement nie powiela ich wyprowadzeń.
- **Manuskrypt na `main`:** `manuscript/tom-01/F24/F24.1_UZUPELNIENIE_PREDYKATY_GEOMETRII.md`; commit [161f71e](https://github.com/mojealterego/Ontologia-Liczby-/commit/161f71e0a48431211133a7021e80d8e8ec56acf2), Git blob `4c44516145d9e1210f63eae346b54dadaefdc7a0`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.** Zakres: orientacja, tożsamość Grama, dokładne rzuty, przecięcia odcinków, środek okręgu opisanego.
- **Testy na `main`:** `tests/test_f241_geometry_predicates.py`; commit [9a3586a](https://github.com/mojealterego/Ontologia-Liczby-/commit/9a3586a87337a8840ec90f75b7962a8b61bc9b4b), Git blob `c468e3ffb821a8b60f153e54f4acee38c0cf3039`. Lokalnie **30/30 unittest OK, 30/30 pytest passed, compileall kod 0**; Git blob identyczny z lokalnym `git hash-object`.
- **Podgląd lokalny:** Pandoc/XeLaTeX z dokładnego opublikowanego źródła, A4, 10 pt, margines 18 mm; **3 strony**, 0 słów poza granicą 8 pt. SHA-256 PDF `86389836cecae9148e9baf4b69637b5840d1393fe3c7cdf48cf07829e82696fb`. PDF nie został zapisany binarnie na GitHub.
- **Protokół:** `docs/DOWODY_F24_1_2026-11-01.md`; commit [ed1c11d](https://github.com/mojealterego/Ontologia-Liczby-/commit/ed1c11dfe8aa9537e8dd6285f7a6029befb15237).
- **Niezweryfikowane:** brak pełnej regresji, formalnej mechanizacji dowodów i niezależnej recenzji; brak potwierdzonego CI (combined statuses 0, PR-filtered workflow runs 0).
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**, trzech stron podglądu nie doliczono. Historyczny wstęp i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F24.2 „Pola figur”, od s. 285 roboczego manuskryptu; najpierw porównać z już istniejącymi Heronem, wzorem sznurowadła i determinantem.



## F24.2 — certyfikaty pól, wielokąty kratowe i obszary z otworami (1 listopada 2026)

- **Oryginał:** odczytano s. 285–289 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony; nie monolit 0.20). Są już Heron, wzór sznurowadła, skala pola, całka zorientowana i 24 zadania; ich treści nie nadpisano.
- **Manuskrypt na `main`:** `manuscript/tom-01/F24/F24.2_UZUPELNIENIE_CERTYFIKATY_POLA_I_SIATKA.md`; commit [2cc9fff](https://github.com/mojealterego/Ontologia-Liczby-/commit/2cc9fffd987858e03b484c8e7a9b15870128ab70), Git blob `1012bcbc9ec213bc1c1c5716844b9152e214d54c`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.** Zakres: dokładna orientacja, brzegi kratowe, Pick, otwory, transformacje unimodularne, certyfikowane błędy współrzędnych.
- **Testy na `main`:** `tests/test_f242_area_certificates.py`; commit [8d3957f](https://github.com/mojealterego/Ontologia-Liczby-/commit/8d3957ffaf401aa200c5297618ea9f8450aed5ca), Git blob `448b400d00aa5c236263ba6b2d9f241b07f0d476`. **35/35 unittest OK, 35/35 pytest passed, compileall kod 0**. Regresja lokalna F24.1 + F24.2: **65/65 passed**. Bloby obu plików potwierdzono ponownym odczytem GitHub i lokalnym `git hash-object`.
- **PDF lokalny:** Pandoc/XeLaTeX z bajtowo identycznego źródła `main`; **3 strony A4**, 4847 / 4447 / 1248 znaków, 0 słów poza marginesem 8 pt; SHA-256 `aa37d74c36e19529ab91f21654ec64b78caff5766fb1dcd1141f85131797edc4`. PDF nie został opublikowany binarnie na GitHub.
- **Dowody techniczne:** `docs/DOWODY_F24_2_2026-11-01.md`, commit [805e62c](https://github.com/mojealterego/Ontologia-Liczby-/commit/805e62cd929da69afea8bdbd09e67bf8646373a2).
- **Niezweryfikowane:** brak pełnej regresji repozytorium, mechanizacji wszystkich dowodów i niezależnej recenzji matematycznej; combined statuses 0 i PR-filtered workflow runs 0 dla commitu testowego, więc **CI niepotwierdzone**.
- **Blokada:** brak kompletnego źródła i binarnego monolitu 0.20. **585/1222 stron bez zmian**, 3 stron podglądu nie doliczono. Historyczny wstęp i wcześniejsze rozdziały nietknięte; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** F24.3 „Objętości i skala”, od s. 290 roboczego manuskryptu; przed rozbudową sprawdzić istniejące wzory walca, kuli i prawo skali.


## F24.3 — objętości i skala, certyfikaty wyznacznikowe (1 listopada 2026)

- **Weryfikacja źródła:** odczytano s. 290–294 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony, nie wydanie 0.20). Oryginał zawiera już bryły elementarne, Cavalieriego, skale oraz 24 zadania o walcach i stożkach. Nie nadpisano go.
- **Manuskrypt na `main`:** `manuscript/tom-01/F24/F24.3_UZUPELNIENIE_CERTYFIKATY_OBJETOSCI.md`, commit [add460c](https://github.com/mojealterego/Ontologia-Liczby-/commit/add460cc54a733b5301379c49eb11591fcc23627), Git blob `00cc87dc27494d2907a41784fa14f24b77fa7d87`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.** Zakres: miara objętości, determinanty, triangulacja czworościanami, przekształcenia afiniczne, przekroje, ścięte ostrosłupy, elipsoidy i certyfikaty błędów.
- **Testy na `main`:** `tests/test_f243_volume_certificates.py`, commit [369efad](https://github.com/mojealterego/Ontologia-Liczby-/commit/369efad8f5845735c2ec5274bfec814d00776816), Git blob `712c00a003828c522a3487f02ff5cfa2297e4600`. **37/37 unittest OK, 37/37 pytest passed, compileall kod 0**. Lokalna regresja F24.1–F24.3: **102/102 passed**. Oba bloby zweryfikowano ponownym odczytem i lokalnym `git hash-object`.
- **PDF lokalny:** Pandoc/XeLaTeX z bajtowo identycznego źródła `main`; **3 strony A4**, 3062 / 3145 / 2482 znaków, 0 słów poza marginesem 8 pt; SHA-256 `3bcb8d93733545d357c7e4f2e062e2cf5a57f3310623f71ae4608ffdb36504b6`. PDF nie został zapisany binarnie na GitHub.
- **Protokół dowodowy:** `docs/DOWODY_F24_3_2026-11-01.md`, commit [cd40420](https://github.com/mojealterego/Ontologia-Liczby-/commit/cd40420679b10cf61114e2ecaed5b201e31f1245), Git blob `6a45dcbbd24328957bd808f16c99a8a1f5cceaed`.
- **Niezweryfikowane:** brak pełnej regresji całego repozytorium, mechanizacji wszystkich dowodów i niezależnej recenzji matematycznej; 0 combined statuses i 0 PR-filtered workflow runs dla commitu testowego, dlatego **CI niepotwierdzone**.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**; trzech stron podglądu nie doliczono. Historyczny wstęp i wcześniejsze rozdziały nietknięte; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** po weryfikacji roboczego manuskryptu opracować F25.1, bez powtarzania istniejących dowodów.


## F25.1 — moduły Cauchy’ego, certyfikaty przedziałowe i uniwersalność uzupełnienia (1 listopada 2026)

- **Oryginał:** przeczytano strony 295–299 bibliotecznego roboczego ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf (764 strony, nie monolit wydania 0.20). Wcześniej opisano już niewymierność pierwiastka z 2, Newtona, przekroje Dedekinda, klasy Cauchy’ego, gęstość i działania na klasach. Suplement nie nadpisuje oryginału ani historycznego wstępu.
- **Manuskrypt na main:** manuscript/tom-01/F25/F25.1_UZUPELNIENIE_MODULY_I_CERTYFIKATY.md, commit [b3c45bb](https://github.com/mojealterego/Ontologia-Liczby-/commit/b3c45bbd0150a3d5aa4cdde68263bad597a7b7d0), Git blob a2017a7accdf6ff9e680f04289c1224134cc2d54. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań.** Zakres: ilościowe moduły Cauchy’ego, szybkie podciągi, bisekcja i reszty, zagnieżdżone certyfikaty, mnożenie i odwrotność, znaki, diagonalizacja, uniwersalność uzupełnienia.
- **Testy na main:** tests/test_f251_cauchy_certificates.py, commit [ced39e3](https://github.com/mojealterego/Ontologia-Liczby-/commit/ced39e3e452334eefd58dbe8e3b601e2013f0b8c), Git blob ece8cf3cba8e6e7abe8904186dfd827bf021d3cb. Lokalnie **40/40 unittest OK, 40/40 pytest passed, compileall kod 0**. Regresja lokalna F24.1–F24.3 + F25.1: **142/142 pytest passed**. Ponowny odczyt GitHub potwierdził identyczność blobów z lokalnym git hash-object.
- **Podgląd PDF lokalny:** Pandoc/XeLaTeX z identycznego źródła main, **3 strony A4**, 10 pt FreeSerif, margines 18 mm; PyMuPDF: **0 słów poza marginesem bezpieczeństwa 8 pt**; SHA-256 7f405d70638c3c7ebee4de0996433bb127637f9f3b119b121b223e15e9255f53. PDF nie zapisano binarnie w repozytorium.
- **Protokół:** docs/DOWODY_F25_1_2026-11-01.md, commit [41016d5](https://github.com/mojealterego/Ontologia-Liczby-/commit/41016d55e8234d9b3fb0c2373a8acfb4db55ed75).
- **Niezweryfikowane:** brak pełnej regresji repozytorium i formalnej mechanizacji twierdzeń; combined statuses 0, PR-filtered workflow runs 0 dla commitu testowego — **CI niepotwierdzone**. Testy skończonych instancji nie dowodzą ogólnych kwantyfikatorów.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu 0.20. **585/1222 stron bez zmian**, trzech stron podglądu nie doliczono. Historyczny wstęp i poprzednie rozdziały nienaruszone; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** F25.2 „Zupełność i supremum”, po porównaniu z istniejącym oryginałem; nie powielać definicji Cauchy’ego i standardowych dowodów.

## F25.2 — certyfikowane kresy i optymalizacja przedziałowa (1 listopada 2026)

- **Źródło porównawcze:** strony 300–304 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony, nie monolit 0.20). Oryginał zawiera już supremum, Archimedesa, przedziały zagnieżdżone, Bolzana–Weierstrassa, bisekcję i pierwiastki. Bez zmian w oryginale i historycznym wstępie.
- **Nowy manuskrypt na `main`:** `manuscript/tom-01/F25/F25.2_UZUPELNIENIE_KRESY_CERTYFIKATY_OPTYMALIZACJI.md`; commity [7878241](https://github.com/mojealterego/Ontologia-Liczby-/commit/78782411c9251ff37e9c08b236cc82c51f5cb600), [22432e3](https://github.com/mojealterego/Ontologia-Liczby-/commit/22432e302ae3e3f4153e4f95e779929e82bb60bd), Git blob `b79d398cc3b1c34ac59fefb4b8faaf8ef193d233`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.**
- **Testy na `main`:** `tests/test_f252_supremum_certificates.py`; commit [e691e4b](https://github.com/mojealterego/Ontologia-Liczby-/commit/e691e4b53f1935c4b0e469a79ce5356815de80f9), Git blob `96c58a10a45864f233af9ccff0c1688ea832d0e7`. Lokalnie **40/40 unittest OK, 40/40 pytest passed, compileall kod 0**; regresja F24.1–F24.3 + F25.1–F25.2: **182/182 pytest passed**. Bloby manuskryptu i testów identyczne lokalnie i na GitHub.
- **Podgląd PDF:** lokalny Pandoc/XeLaTeX z dokładnego źródła `main`, **3 strony A4**, 10 pt FreeSerif, margines 18 mm, PyMuPDF: **0 słów poza marginesem bezpieczeństwa 8 pt**; SHA-256 `beda71de294759dd2fdf7ca071df254a54458bd3ceabc80156a3e1142a336bf2`. PDF nie opublikowano binarnie na GitHub.
- **Protokół:** `docs/DOWODY_F25_2_2026-11-01.md`, commit [8a42b54](https://github.com/mojealterego/Ontologia-Liczby-/commit/8a42b5497444877bdc97a2047326505461893685).
- **Niezweryfikowane:** pełna regresja całego repozytorium, formalna mechanizacja twierdzeń, niezależna recenzja matematyczna. GitHub combined statuses 0, PR-filtered workflow runs 0 — **CI niepotwierdzone**.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu 0.20. **585/1222 stron bez zmian**; trzech stron podglądu nie doliczono. Bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F25.3 po odczycie istniejącego oryginału, bez powielania wyników.


## F25.3 — dokładne certyfikaty odległości i pokrycia (1 listopada 2026)

- **Źródło porównawcze:** strony 305–309 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony; nie jest wydaniem 0.20). Istniejące definicje topologiczne, zwartość i spójność nie zostały powtórzone ani zmodyfikowane.
- **Manuskrypt na `main`:** `manuscript/tom-01/F25/F25.3_UZUPELNIENIE_CERTYFIKATY_ODLEGLOSCI.md`; commit [5836d02](https://github.com/mojealterego/Ontologia-Liczby-/commit/5836d021b3ec69e7964dd32631c345d7709394d6); Git blob `0db4bd68103b979ce971e214a549a4f47e12a558`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.** Tematy: dokładna normalizacja sum przedziałów, rzut, dylatacja, erozja, promień niepokrycia, certyfikaty pokrycia i stabilność Hausdorffa.
- **Testy na `main`:** `tests/test_f253_interval_distance_certificates.py`; commit [44084a3](https://github.com/mojealterego/Ontologia-Liczby-/commit/44084a3edc586c82067b58edba9f69c08d0e95ef); Git blob `2b43409e23fe21602d2405e364bd479041d9825a`. Lokalnie **28/28 unittest OK, 28/28 pytest passed**, regresja lokalna F24.1–F25.3 **210/210 passed**, `compileall` kod 0. Git blob zgodny z lokalnym `git hash-object`.
- **PDF lokalny:** Pandoc/XeLaTeX z bajtowo identycznego źródła `main`; **3 strony A4**, FreeSerif 10 pt, margines 18 mm; PyMuPDF: **0 słów poza marginesem 8 pt**; SHA-256 `77c921e4d0df8d5d6cd62d3048175b4b765ded15ca22e3ae354e6805a8541b14`. PDF nie opublikowano binarnie w repozytorium.
- **Protokół:** `docs/DOWODY_F25_3_2026-11-01.md`, commit [b02cfc9](https://github.com/mojealterego/Ontologia-Liczby-/commit/b02cfc9890c286e641e3dd68d1db294bc6fb8e17).
- **Niezweryfikowane:** pełna regresja całego repozytorium, formalna mechanizacja dowodów i niezależna recenzja matematyczna. GitHub: 0 combined statuses i 0 workflow runs dla commitu testowego; **CI niepotwierdzone**.
- **Blokada integracji:** brak źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**, trzech stron podglądu nie doliczono. Historyczny wstęp i poprzednie rozdziały nietknięte; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** F26.1 „Dziedzina, przeciwdziedzina i obraz” po weryfikacji oryginału roboczego; nie dublować gotowych definicji.


## F26.1 — włókna, nasycenie i faktoryzacja funkcji (1 listopada 2026)

- **Oryginał:** zweryfikowano s. 311–315 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony, **nie** wydanie 0.20). Istniejące definicje funkcji, dziedziny, przeciwdziedziny, obrazu, przeciwobrazu, iniekcji, surjekcji i bijekcji oraz 24 ćwiczenia nie zostały nadpisane ani powtórzone. F26.2 zaczyna się na s. 316.
- **Manuskrypt na `main`:** `manuscript/tom-01/F26/F26.1_UZUPELNIENIE_WLOKNA_I_FAKTORYZACJA.md`, commity [cf9ff22](https://github.com/mojealterego/Ontologia-Liczby-/commit/cf9ff22e16583e30cb0488a9e6d932192f9c99a1) i [17c937a](https://github.com/mojealterego/Ontologia-Liczby-/commit/17c937ab97aa8a72b2c99728500d7a3e6e62a77b), Git blob `74927ca60e5d43b86984d0b5c4d6b16e6c956e22`. **8 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.** Zakres: włókna, nasycenie, iloraz, sprzężenie obrazu z przeciwobrazem, faktoryzacja, certyfikaty liczności i kolizji.
- **Testy na `main`:** `tests/test_f261_fibers_factorization.py`, commit [2f428de](https://github.com/mojealterego/Ontologia-Liczby-/commit/2f428de02ba1c20600526b11c3e0340dfd24abb5), Git blob `e39e005d0b9a10d67327864d3560d2431374445c`. Lokalnie **25/25 unittest OK, 25/25 pytest passed, compileall kod 0**. Regresja F24.1–F26.1 na siedmiu dostępnych plikach: **235/235 pytest passed**. Bloby obu plików identyczne lokalnie i na GitHub.
- **PDF lokalny:** Pandoc/XeLaTeX z dokładnego źródła `main`, **3 strony A4**, FreeSerif 11 pt, margines 20 mm, tekst 2661 / 3154 / 2627 znaków, PyMuPDF: **0 słów poza marginesem 8 pt**; SHA-256 `d49fbf36cddb896ba3b460b92bf7e7e814360577ad350aead1cb99b2078e659b`. PDF nie opublikowano binarnie na GitHub.
- **Protokół:** `docs/DOWODY_F26_1_2026-11-01.md`, commit [157af75](https://github.com/mojealterego/Ontologia-Liczby-/commit/157af759680123d8d4f787bc0f6444b61fd052ea).
- **Niezweryfikowane:** pełna regresja całego repozytorium, mechanizacja wszystkich dowodów i niezależna recenzja matematyczna. GitHub combined statuses dla commitu testowego: 0; **CI niepotwierdzone**.
- **Blokada integracji:** brak źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**; 3 stron podglądu nie doliczono. Historyczny wstęp i poprzednie rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F26.2 „Funkcja liniowa i kwadratowa” od s. 316 roboczego manuskryptu. Odróżniać funkcję afiniczną od liniowej w sensie algebry; nie powielać istniejących wyprowadzeń postaci kanonicznej i monotoniczności.


## F26.2 — certyfikaty odporności funkcji kwadratowych (1 listopada 2026)

- **Źródło porównawcze:** odczytano s. 316–324 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony; **nie** wydanie 0.20). F26.3 zaczyna się na s. 325. Nie powielono istniejącej postaci kanonicznej, monotoniczności, regresji wprowadzającej ani błędu cięciwy.
- **Manuskrypt na `main`:** `manuscript/tom-01/F26/F26.2_UZUPELNIENIE_CERTYFIKATY_KWADRATOWE.md`; commity [0d85932](https://github.com/mojealterego/Ontologia-Liczby-/commit/0d859322697911821b30e88b48a4017b65ed9e35), [bcffe64](https://github.com/mojealterego/Ontologia-Liczby-/commit/bcffe6454d4afa796efdfa5d104738126d50f62f); Git blob `51c081c7ef9d6999542b67887804bbf71df2680d`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań**. Zakres: obwiednie współczynników, odporne znaki, marginesy, stabilność ekstremów, optimum całkowitoliczbowe, izolacja pierwiastków, certyfikat Bernsteina i dokładna regresja.
- **Testy na `main`:** `tests/test_f262_quadratic_robustness.py`; commit [bd6c10d](https://github.com/mojealterego/Ontologia-Liczby-/commit/bd6c10d75c2f7e895de59c975b2b17e0d39f1670); Git blob `d2bbb10254c40478bf464b681db54c62663cbfcc`. Lokalnie **35/35 unittest OK, 35/35 pytest passed**, `compileall` kod 0; regresja dostępnych ośmiu modułów F24.1–F26.2: **270/270 pytest passed**. Poprawiono wykryty testem przypadek wielomianu stałego przed publikacją.
- **PDF lokalny:** Pandoc/XeLaTeX z bajtowo identycznego źródła `main`, **3 strony A4**, FreeSerif 10 pt, margines 20 mm; tekst 3362 / 3745 / 2216 znaków; PyMuPDF: **0 słów poza marginesem 8 pt**; SHA-256 `8c8b4d3d32eda364f60d8875ebe60b0495c16cba534840dffd531d5f0efee150`. PDF nie jest binarnym plikiem w repozytorium.
- **Protokół dowodowy:** `docs/DOWODY_F26_2_2026-11-01.md`, commit [0d944ad](https://github.com/mojealterego/Ontologia-Liczby-/commit/0d944adf53bb090f32d334759e57a89f71544c09).
- **Niezweryfikowane:** pełna regresja całego repozytorium, mechanizacja wszystkich dowodów, niezależna recenzja. GitHub combined statuses: 0; PR-filtered workflow runs: 0; **CI niepotwierdzone**.
- **Blokada integracji:** brak źródła i binarnego monolitu 0.20. **585/1222 stron bez zmian**; 3 stron podglądu nie doliczono. Historyczny wstęp i poprzednie rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F26.3 „Złożenie i odwrotność”, od s. 325 roboczego manuskryptu; sprawdzić oryginalne warunki dziedzin i typowania przed rozszerzeniem.


## F26.3 — funkcje częściowe, ścisłe dziedziny i odwracalność (1 listopada 2026)

- **Oryginał:** zbadano strony 325–329 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony, nie wydanie 0.20); F27.1 zaczyna się na s. 330. W oryginale są już podstawy składania, odwrotności, przeciwobrazów, funkcji ułamkowo-liniowych i 24 zadania; nie powielono tych treści.
- **Manuskrypt na `main`:** `manuscript/tom-01/F26/F26.3_UZUPELNIENIE_FUNKCJE_CZESCIOWE_I_ODWRACALNOSC.md`; commity [111d0d4](https://github.com/mojealterego/Ontologia-Liczby-/commit/111d0d408423d25279dbb5966d7aeb50d343d476), [a6a1514](https://github.com/mojealterego/Ontologia-Liczby-/commit/a6a151492ca582b8b0c69d5847fff3b931f9479a); Git blob `fb89d44d22a9c4e7c8d86a8e7a9bfdf09705adf7`. **9 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.**
- **Testy na `main`:** `tests/test_f263_partial_composition.py`; commit [c63641a](https://github.com/mojealterego/Ontologia-Liczby-/commit/c63641a2ac11a7a002dfa1d79bb3293a401c91e6); Git blob `731fa57410a9e79c27a296b0da92df9d07280825`. Lokalnie **31/31 unittest OK, 31/31 pytest passed**, `compileall` bez błędów. Regresja dziewięciu dostępnych modułów F24.1–F26.3: **301/301 pytest passed**. Bloby zgodne z lokalnym `git hash-object`.
- **PDF lokalny:** Pandoc/XeLaTeX, **3 strony A4**, FreeSerif 10 pt, margines 18 mm; tekst 3400 / 4080 / 2800 znaków, **0 słów poza marginesem 8 pt**. SHA-256 `d00e51195df49054d92899d1af325fe4655781430962ab3b4b31c8662a0402e2`. Podgląd nie został dodany binarnie do repozytorium.
- **Protokół dowodowy:** `docs/DOWODY_F26_3_2026-11-01.md`, commit [c3b0dda](https://github.com/mojealterego/Ontologia-Liczby-/commit/c3b0ddae4fc33074c0ab02f47633c9eb9388aedc).
- **Niezweryfikowane:** pełna regresja repozytorium i formalna mechanizacja twierdzeń. GitHub: 0 statusów CI i 0 PR-filtered workflow runs dla commitu testowego — **CI niepotwierdzone**.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**; 3 stron podglądu nie doliczono. Historyczny wstęp i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F27.1 „Ciąg jako funkcja” od strony 330 roboczego manuskryptu; przed opracowaniem porównać istniejące wyniki o ciągach i zbieżności.


## F27.1 — certyfikaty iteracji i stabilności (1 listopada 2026)

- **Oryginał:** odczytano strony 330–334 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony; nie monolit 0.20). Istniejące definicje ciągu, sumy geometryczne, monotoniczność, rekurencje i 24 zadania pozostawiono bez zmian.
- **Manuskrypt na `main`:** `manuscript/tom-01/F27/F27.1_UZUPELNIENIE_CERTYFIKATY_ITERACJI.md`; commity [40847b1](https://github.com/mojealterego/Ontologia-Liczby-/commit/40847b19f9e02d5a041f4adca458d19ced164ee8), [f2a488b](https://github.com/mojealterego/Ontologia-Liczby-/commit/f2a488b3a5319d688def483f10ee38c37e5ae681), Git blob `6e81c9e0de06caa0433f01735d63509962700d9c`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań**; certyfikaty zbieżności, propagacja błędu, kontrakcje i stabilność.
- **Testy na `main`:** `tests/test_f271_iteration_certificates.py`, commit [3415052](https://github.com/mojealterego/Ontologia-Liczby-/commit/3415052d21b9b03915cce10ba5c4fd9e6d7d3397), Git blob `7314269e7a25b2d134fa1b5148144f47bc6d02b4`. Lokalnie **36/36 unittest OK, 36/36 pytest passed, compileall bez błędów**. Regresja dziesięciu lokalnych modułów F24.1–F27.1: **337/337 pytest passed**. Testy nie zastępują formalnych dowodów.
- **PDF lokalny:** Pandoc/XeLaTeX, **3 strony A4**, FreeSerif 10 pt, margines 18 mm; 2870 / 3554 / 1627 znaków, PyMuPDF: **0 słów poza marginesem bezpieczeństwa 8 pt**. SHA-256 `7664f651c983dbacc96b381fc66533c0efd7bb2b34ac2fe1e10248adfa0fd6ee`. PDF nie opublikowano binarnie w repozytorium.
- **Protokół:** `docs/DOWODY_F27_1_2026-11-01.md`, commit [e15773f](https://github.com/mojealterego/Ontologia-Liczby-/commit/e15773f24f2e524bbb23d28c1743d6b11e676cb1).
- **Niezweryfikowane:** pełna regresja repozytorium, mechanizacja dowodów, niezależna recenzja. GitHub: 0 statusów CI, 0 przebiegów Actions dla commitu testowego — **CI niepotwierdzone**.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**; 3 stron podglądu nie doliczono. Historyczny wstęp i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F27.2 „Definicja granicy” od strony 334 roboczego manuskryptu; sprawdzić istniejące dowody epsilon–N i dodać wyniki niepowtarzające oryginału.

## F27.2 — świadkowie ε–N i metastabilność (1 listopada 2026)

- **Oryginał:** odczytano s. 335–340 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony; **nie** monolit wydania 0.20). F27.3 zaczyna się na s. 341. Nie powielono definicji ε–N, jednoznaczności granicy, twierdzeń o Cauchym, podciągach i limsup/liminf.
- **Manuskrypt na `main`:** `manuscript/tom-01/F27/F27.2_UZUPELNIENIE_SWIADKOWIE_GRANIC.md`; commity [f28d508](https://github.com/mojealterego/Ontologia-Liczby-/commit/f28d508eeb29f035fdeb95829ee5197ad3b4ab35), [c36e643](https://github.com/mojealterego/Ontologia-Liczby-/commit/c36e6435484a0bf74269c7e49352edd51b6d821e); Git blob `7f7f4c55e33baa65a2d7bd4980412d3047eb00ea`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.**
- **Testy na `main`:** `tests/test_f272_limit_witnesses.py`; commity [c41f6e2](https://github.com/mojealterego/Ontologia-Liczby-/commit/c41f6e2a6d45a919a56079c1ca346bef6473b07d), [590f250](https://github.com/mojealterego/Ontologia-Liczby-/commit/590f2503f1e31c97a4bacae9c2028a8818fcd2a4); Git blob `8f7f63008531cb9b0d80ce4409228183c3e21542`. Lokalnie **30/30 unittest OK**; regresja 11 dostępnych modułów F24.1–F27.2: **367/367 pytest passed**; `compileall` bez błędów. Bloby źródła i testów identyczne z lokalnym `git hash-object`.
- **Podgląd PDF:** Pandoc/XeLaTeX z identycznego źródła `main`, **3 strony A4**, FreeSerif 10 pt, margines 18 mm; 3375 / 3450 / 2199 znaków; PyMuPDF: **0 słów poza marginesem 8 pt**; SHA-256 `dbc09dae2adf00768070d446f4fc53102dd34a8546eecd0924f665acbf762074`. PDF jest lokalny, nie opublikowany binarnie w repozytorium.
- **Protokół:** `docs/DOWODY_F27_2_2026-11-01.md`, commit [b3821ba](https://github.com/mojealterego/Ontologia-Liczby-/commit/b3821baf406437c8aa163e7a2afc17c2922ec42e).
- **Niezweryfikowane:** pełna regresja repozytorium, mechanizacja wszystkich dowodów, niezależna recenzja; GitHub combined statuses 0, PR-filtered workflow runs 0 dla commitu testowego, więc **CI niepotwierdzone**.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**, trzech stron podglądu nie doliczono. Historyczny wstęp i wcześniejsze rozdziały nienaruszone; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** F27.3 „Granica nie jest ostatnim wyrazem” od s. 341 roboczego manuskryptu; nie powielać gotowych przykładów i zadań.

## F27.3 — ogony, nieosiąganie i certyfikaty sum (1 listopada 2026)

- **Oryginał:** odczytano s. 341–345 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony, **nie** wydanie 0.20); F28.1 zaczyna się na s. 346. Nie modyfikowano oryginału ani historycznego wstępu.
- **Manuskrypt na `main`:** `manuscript/tom-01/F27/F27.3_UZUPELNIENIE_OGONY_I_NIEOSIAGANIE_GRANICY.md`; commit [59e5a04](https://github.com/mojealterego/Ontologia-Liczby-/commit/59e5a0437c0f2c37d6f14641f52a69496d175065); Git blob `6325cc4d4438f36380566139ba0408a22ba21178`. **8 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.** Zakres: błąd ogona, nieosiągana granica, certyfikaty przedziałowe, reszty szeregów, punkty skupienia, granice iterowane.
- **Testy na `main`:** `tests/test_f273_tails_nonattainment.py`; commit [80474b5](https://github.com/mojealterego/Ontologia-Liczby-/commit/80474b549389da47adbc01269feee71f800a2592); Git blob `107874cc759cce9ce82175e606ecf2a66fa84397`. Lokalnie **41/41 unittest OK, 41/41 pytest passed, 24 podtesty**; regresja 11 dostępnych modułów F24.2–F27.3 **378/378 pytest passed**, `compileall` kod 0. Pierwszy przebieg regresji 377/378 wykrył brak pliku źródłowego F27.1 w zestawie, po skopiowaniu niezmienionego pliku i ponowieniu 378/378.
- **Errata źródłowa:** `docs/ERRATA_F27_3_2026-11-01.md`; commit [d090255](https://github.com/mojealterego/Ontologia-Liczby-/commit/d090255e4392b6cc3a7f4e7a269790d0f515ec9d). **19 błędnych wyników w 24 zadaniach** na s. 343–344; poprawne odpowiedzi i dokładne testy wymierne zapisano osobno, bez ingerencji w historyczne strony.
- **Podgląd PDF lokalny:** Pandoc/XeLaTeX z bajtowo identycznego źródła `main`; **3 strony A4**, FreeSerif 10 pt, margines 18 mm, PyMuPDF: **0 słów poza marginesem bezpieczeństwa 8 pt**; SHA-256 `2cfca11955d6a5cf93324c0a70e2bf6705937cff14ec77d5eeee333c8edff519`. PDF nie został opublikowany binarnie w repozytorium.
- **Protokół:** `docs/DOWODY_F27_3_2026-11-01.md`, commit [54aea51](https://github.com/mojealterego/Ontologia-Liczby-/commit/54aea5134ba48c37d45b899da3f9e1629d603354). Git blob SHA trzech źródeł i protokołu zgodny z lokalnym `git hash-object`.
- **Niezweryfikowane:** pełna regresja repozytorium, formalna mechanizacja twierdzeń, niezależna recenzja matematyczna. GitHub dla commitu testowego: **0 statusów i 0 workflow runs** w zapytaniu `head_sha`; **zielone CI niepotwierdzone**.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu 0.20. **585/1222 stron bez zmian**, 3 stron podglądu nie doliczono. Historyczny wstęp i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F28.1 „Iloraz różnicowy” od s. 346 roboczego manuskryptu; najpierw zweryfikować oryginalne dowody różniczkowania, następnie rozwijać nowe certyfikaty i przykłady bez dublowania podstaw.


## F28.1 — certyfikaty ilorazu różnicowego i błędów numerycznych (1 listopada 2026)

- **Oryginał:** odczytano s. 346–351 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony, **nie** wydanie 0.20); F28.1 obejmuje s. 346–350, F28.2 zaczyna się na s. 351. Nie powielono definicji pochodnej, reguł różniczkowania, Taylora ani wprowadzenia do ilorazu centralnego.
- **Manuskrypt na `main`:** `manuscript/tom-01/F28/F28.1_UZUPELNIENIE_CERTYFIKATY_ILORAZOW.md`; commit [acfedbf](https://github.com/mojealterego/Ontologia-Liczby-/commit/acfedbf2d83151dfa784b9d86e68a41dfbc768e3), Git blob `55eaa6ae56fd388364c012666f84af1b26150620`. **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań.** Opracowano ścisłe błędy ilorazów, ekstrapolację Richardsona, nierówności siecznych wypukłych i nieidentyfikowalność pochodnej ze skończonych pomiarów.
- **Testy na `main`:** `tests/test_f281_difference_quotients.py`, commit [d8cb5cd](https://github.com/mojealterego/Ontologia-Liczby-/commit/d8cb5cd7c3ce912d1d5c160261c3bb7d859dbf8d), Git blob `d94dcbcb72702fabee8f868780bd1cee98ff2e4f`. Lokalnie **33/33 unittest OK, 33/33 pytest passed**, `compileall` bez błędów. Regresja 11 plików dostępnych lokalnie (F24.3–F28.1, bez części wcześniejszych plików): **376 passed, 24 subtests passed**. Git blob obu plików zgodny z lokalnym `git hash-object`.
- **PDF lokalny:** Pandoc/XeLaTeX z bajtowo identycznego źródła `main`, **3 strony A4**, FreeSerif 10 pt, margines 18 mm; 4030 / 3659 / 1554 znaków; PyMuPDF **0 słów poza marginesem 8 pt**; SHA-256 `bd6065ade0662a481674cb361145a9894980dd1125f5ab86af8229eed758de28`. PDF nie opublikowano binarnie w repozytorium.
- **Protokół:** `docs/DOWODY_F28_1_2026-11-01.md`, commit [c9e8f99](https://github.com/mojealterego/Ontologia-Liczby-/commit/c9e8f99b679006fccf1c313b17f96e0b9caf402e).
- **Niezweryfikowane:** pełna regresja całego repozytorium, formalna mechanizacja twierdzeń, niezależna recenzja. GitHub dla commitu testowego: 0 combined statuses i 0 PR-filtered workflow runs — **zielone CI niepotwierdzone**.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu 0.20. **585/1222 stron bez zmian**; 3 stron podglądu F28.1 nie doliczono. Historyczny wstęp i poprzednie rozdziały nietknięte; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** F28.2 „Ekstrema i optymalizacja”, od s. 351 roboczego manuskryptu; sprawdzić wcześniejsze dowody Fermata i kryterium drugiej pochodnej przed opracowaniem nowych certyfikatów.


## F28.2 — certyfikaty globalności i lokalizacji minimizatora (1 listopada 2026)

- **Oryginał:** zbadano s. 351–355 bibliotecznego roboczego `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT.pdf` (764 strony; **nie** monolit 0.20). Istniejące Fermat, kryterium drugiej pochodnej, Weierstrass, brzegi, AM–GM i 24 zadania nie zostały powielone ani zmienione.
- **Manuskrypt na `main`:** `manuscript/tom-01/F28/F28.2_UZUPELNIENIE_CERTYFIKATY_OPTYMALIZACJI.md`, Git blob `9d0ae453289815c3bd698eb9ff51527b4f7a168a`; **8 definicji, 12 twierdzeń z dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań**. Globalne obwiednie krzywizny, residuum rzutowe, przedziały znaku, bisekcja, dolne granice, bezpieczne odrzucanie, odporność na błąd gradientu.
- **Testy na `main`:** `tests/test_f282_global_optimality.py`, Git blob `5b2a51788b11cf7ea08b940a1d6ddc5dbb82ffeb`. Lokalnie **45/45 unittest OK, 45/45 pytest passed**, `compileall` kod 0. Regresja 11 dostępnych lokalnie modułów F25.1–F28.2: **384 passed, 24 subtests passed**; nie jest to pełna regresja repozytorium.
- **PDF lokalny:** Pandoc/XeLaTeX z bajtowo identycznego źródła `main`; **3 strony A4**, FreeSerif, margines 18 mm; PyMuPDF **0 słów poza marginesem 8 pt**. SHA-256 `2346721a96450942f572c7e850e8ceea2078dfc0218b0bbc150018c0e7a63d58`. PDF nie dodano binarnie do repozytorium.
- **Commity:** [f261101](https://github.com/mojealterego/Ontologia-Liczby-/commit/f2611013362872bb0300e55d2f90091ec1969f44), [7994f87](https://github.com/mojealterego/Ontologia-Liczby-/commit/7994f87bc6fb6a09251c69f046808d1cc591315f), [5fef808](https://github.com/mojealterego/Ontologia-Liczby-/commit/5fef808b3cea5164edaa792ae9ccafe0450bbc5e), [0498530](https://github.com/mojealterego/Ontologia-Liczby-/commit/049853013735ff92f09b213cf5ca301457fe2115), [194fa8c](https://github.com/mojealterego/Ontologia-Liczby-/commit/194fa8cdec0955ba7e2cd15a058310d582e766ab), [2655fbb](https://github.com/mojealterego/Ontologia-Liczby-/commit/2655fbbe3156154ed5727ca1e3e73b05d29ce785).
- **Protokół dowodowy:** `docs/DOWODY_F28_2_2026-11-01.md`, commit [18fdedb](https://github.com/mojealterego/Ontologia-Liczby-/commit/18fdedbc640b069b61965984c1a71f9a082de622); Git blob `667ffa37cd700de5178e5949b3bbf70ab5cb2ae2`.
- **Niezweryfikowane:** pełna regresja 67 plików testowych repozytorium, formalna mechanizacja dowodów, niezależna recenzja. GitHub: 0 combined statuses i 0 workflow runs w sprawdzonym zakresie; **CI niepotwierdzone**.
- **Blokada integracji:** brak kompletnego źródła i binarnego monolitu wydania 0.20. **585/1222 stron bez zmian**, trzech stron podglądu nie doliczono. Historyczny wstęp i poprzednie rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** F29.1 „Od sum prostokątów do całki”, od s. 356 roboczego manuskryptu; najpierw zweryfikować definicje całkowalności i istniejące przykłady.


## Korekta metody redakcyjnej — audyt taksonomiczny (1 listopada 2026)

- Utworzono `docs/AUDYT_ZGODNOSCI_TAKSONOMICZNEJ_2026-11-01.md`, commit `180104ab6aecf7d99a4bf8234121979ef9134189`.
- Zidentyfikowano wstępne mapowania F27.2/F27.3 → E2-06, F28.1 → E2-13, F28.2 → E2-13/MA-08; są to kandydatury, nie dowody ukończenia punktów.
- Przywrócono priorytet kolejności E0-01 → dalsze punkty według taksonomii; nie zaliczać suplementów jako gotowych jednostek bez audytu treści i rzeczywistej paginacji.
- Bilans **585/1222 bez zmian**; historyczny wstęp bez zmian; nie utworzono finalnego spisu treści ani Tomu II.

## E0-01 — Klasyfikacja i relacje, poziom I (1 listopada 2026)

- **Kolejność taksonomiczna:** rozpoczęto od E0-01, nie od kolejnego numeru F. W repo nie odnaleziono wcześniej samodzielnej monografii E0-01. Wykorzystano istniejące F9.1 jako kontekst, bez modyfikacji wcześniejszych tekstów.
- **Źródło na main:** `manuscript/tom-01/E0/E0-01_KLASYFIKACJA_I_RELACJE.md`, commit `af0a52275acd8d725003330a2c19fe0364b51051`, rozszerzenie `08a19b5a3ed0fe62f3e9a1a6bc9deb537fc9c12e`; 10 definicji, 12 twierdzeń, 6 kontrprzykładów i 36 rozwiązanych zadań.
- **Testy:** `tests/test_e001_classification_relations.py`, commit `7a546a8bd4985f261fd3f3b5381857a534823519`; 12 testów modelowych. Lokalny analog 12/12 OK; wykonanie dokładnego pliku przez GitHub CI niepotwierdzone.
- **Automatyzacja:** `.github/workflows/tom1-e001.yml`, commit `f3b39c3cf6375fa35d2a9600eb334fdff0c03f9b`, kompiluje PDF ze źródła main po uruchomieniu workflow. Zielony CI i wynikowy PDF z tego workflow pozostają **niepotwierdzone**.
- **Lokalny podgląd:** rozbudowany wariant lokalny E0-01, 9 stron A4, Pandoc/XeLaTeX, 0 słów poza marginesem 8 pt; **wariant nie jest bajtowo identyczny z treścią na main**, dlatego nie potwierdza jej paginacji. SHA-256 PDF: `a3dab65f9521ecd42a44cac963e0ebcc59acabf976e87384af48e8c5d2af07b8`.
- **Protokół:** `docs/DOWODY_E0_01_2026-11-01.md`, commit `e8c85083203459180a50ed833df4647b25ffd675`.
- **Otwarte:** kompilacja i kontrola wymaganych stron *dokładnej wersji repozytoryjnej*, kontrola ścisłości, integracja z monolitem 0.20. Punkt E0-01 ma status **opracowany źródłowo, nieodebrany wydawniczo**.
- **Bilans:** **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze punkty nienaruszone. Bez finalnego spisu treści i bez Tomu II.


## E0-02 — Liczby naturalne: liczebność, zapis pozycyjny, porównania i oszacowania (1 listopada 2026)

- **Kolejność:** po E0-01, według taksonomii poziomu I; przegląd istniejących F8.2, F10.1, F10.2 wykazał pokrewne, bardziej zaawansowane treści, których nie nadpisano. Nie stwierdzono wcześniejszego samodzielnego opracowania E0-02.
- **Manuskrypt na main:** manuscript/tom-01/E0/E0-02_LICZBY_NATURALNE.md, commit [9fb18f1](https://github.com/mojealterego/Ontologia-Liczby-/commit/9fb18f1887fe922a0ec6d27edb4763f4e6e1f19c), blob e2bddfad59a45d540eca9af30eacbf731031803f; 9 definicji, 14 twierdzeń z dowodami, 6 kontrprzykładów, 36 rozwiązanych zadań i 4 problemy syntetyczne z rozwiązaniami.
- **Testy:** tests/test_e002_natural_numbers.py, commit [5a1547f](https://github.com/mojealterego/Ontologia-Liczby-/commit/5a1547f216d7b1f1bcb2e17603dc0a797d1f0a28), blob 52f1ed1667747acf3b9d2d36ba5781e8da0a760b. W lokalnym, nieidentycznym bajtowo odpowiedniku wykonano **26/26 unittest OK**. Wykonanie dokładnego pliku GitHub przez CI pozostaje niepotwierdzone.
- **Skład:** .github/workflows/tom1-e002.yml, commit [95a2311](https://github.com/mojealterego/Ontologia-Liczby-/commit/95a231194810fad6157bc88d79b298a9029ffeea), blob 0136afdb7af930f82ce7a56e5ba15bb4d7e114bc; workflow przewiduje XeLaTeX/Pandoc, kontrolę niepustych stron i publikację artefaktu PDF. Wynik workflow i liczba stron **niepotwierdzone**; 0 PR-filtered runs i 0 combined statuses nie są dowodem braku uruchomienia push workflow.
- **Protokół:** docs/DOWODY_E0_02_2026-11-01.md, commit [9cc1e63](https://github.com/mojealterego/Ontologia-Liczby-/commit/9cc1e632ab54f796f55aee16766c1284cf696230).
- **Status:** E0-02 opracowany źródłowo, **nieodebrany wydawniczo**. Bez zweryfikowanego PDF nie potwierdzono minimalnych 4 stron teorii i 4 stron ćwiczeń. Brak kompletnego źródła monolitu 0.20 blokuje integrację.
- **Bilans:** **585/1222 stron bez zmian**. Historyczny wstęp i wszystkie wcześniejsze rozdziały bez ingerencji; bez końcowego spisu treści i bez Tomu II. Kolejny punkt E0-03 „Działania arytmetyczne”.

- **E0-02 — korekta składu:** podział części A/B i bramka 4+4 stron: commit [09bc142](https://github.com/mojealterego/Ontologia-Liczby-/commit/09bc1426bd4ead828139912457011954794a49e9), [f902122](https://github.com/mojealterego/Ontologia-Liczby-/commit/f902122f1fd2471016e3263e667a0a7dc313255c); aktualizacja protokołu [8355e19](https://github.com/mojealterego/Ontologia-Liczby-/commit/8355e19b2db0009a8c9f42128b2455ef77dec577). Niepotwierdzona kompilacja PDF i objętość — nie doliczać stron.

- **E0-02 — dowód:** pełna indukcja w Twierdzeniu 1 (niezależność liczebności od kolejności), commit [e85d27d](https://github.com/mojealterego/Ontologia-Liczby-/commit/e85d27db5dcb3aa32a1ec0e3c36296fd81b18964), protokół [32b9398](https://github.com/mojealterego/Ontologia-Liczby-/commit/32b93983d0a1ddd992bd0a7cc31392c0d9a05934). PDF i integracja nadal otwarte.


## E0-03 — Działania arytmetyczne (1 listopada 2026)

- **Taksonomia:** E0-03, poziom I; zgodnie z kolejnością po E0-02. Wykorzystano odniesienie do wcześniejszego F10.2, bez ingerencji w jego zawartość.
- **Manuskrypt:** `manuscript/tom-01/E0/E0-03_DZIALANIA_ARYTMETYCZNE.md`, commit [98c1281](https://github.com/mojealterego/Ontologia-Liczby-/commit/98c12812851e1d0c7bf79499efe93ee7665892ea), Git blob `bba766b06eb953cd10c2fe4e62e3b787f1ff6138`; 10 definicji, 15 twierdzeń z dowodami, 6 kontrprzykładów, 40 rozwiązanych ćwiczeń, 4 rozwiązane problemy syntetyczne.
- **Testy:** `tests/test_e003_arithmetic.py`, commit [2fc8771](https://github.com/mojealterego/Ontologia-Liczby-/commit/2fc8771f1500b46fc5b1eb736d9876153ddd387b); plik testowy zapisany, **nie uruchomiony w Pythonie** w tej sesji. Wykonano niezależne sprawdzenie 600 par (dzielna 0–49, dzielnik 1–12) w JS, 0 błędów; sprawdzono zdalny tekst: 10 definicji, 15 twierdzeń, 40 ćwiczeń i 4 problemy.
- **Niepotwierdzone:** wymagane minimum stron teorii i ćwiczeń w składzie PDF, wynik CI, pełna regresja, formalna weryfikacja wszystkich dowodów. Nie kompilowano PDF w tej sesji; brak lokalnego silnika składu w dostępnym środowisku.
- **Bilans:** **585/1222 bez zmian** do integracji z rzeczywistym monolitem 0.20. Wstęp historyczny i poprzednie rozdziały nienaruszone; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** E0-04 — Pomiar; przed napisaniem sprawdzić istniejące rozdziały o jednostkach, skali, długości, masie, polu i czasie.


## E0-04 — Pomiar (1 listopada 2026)

- **Zapis na main:** manuskrypt [c4af8d9](https://github.com/mojealterego/Ontologia-Liczby-/commit/c4af8d93b9d0fae402b867fa947035202eb5ff83), testy [05cebe0](https://github.com/mojealterego/Ontologia-Liczby-/commit/05cebe0ad5d0be92fb2a7ff8d92e9d35d66070dc), workflow PDF [aaf4398](https://github.com/mojealterego/Ontologia-Liczby-/commit/aaf43986739ee927bda0dc9f61481aa502a52449), protokół [86aa1a4](https://github.com/mojealterego/Ontologia-Liczby-/commit/86aa1a487064fb809af1e970f47132e2d87a748f).
- **Dokładny manuskrypt GitHub:** 11 definicji, 16 twierdzeń z dowodami, 7 kontrprzykładów, 40 rozwiązanych ćwiczeń i 4 problemy przekrojowe. Wszystkie trzy pliki źródłowe ponownie odczytano z main.
- **Kontrole wykonane:** 8/8 testów Python w lokalnym równoważnym wariancie; lokalnie wygenerowany i sprawdzony dwustronicowy PDF jest wyłącznie podglądem fragmentów, nie kompilacją dokładnego manuskryptu.
- **Niepotwierdzone:** CI i jego pełny PDF, minimum 4 stron teorii i 4 stron ćwiczeń, kompletna weryfikacja matematyczna, integracja z monolitem 0.20. Szczegóły w docs/DOWODY_E0_04_2026-11-01.md.
- **Bilans:** **585/1222 stron bez zmian**. Wstęp historyczny i poprzednie rozdziały bez ingerencji; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** E0-05 — Figury i przestrzeń; przed opracowaniem wykonać kontrolę już istniejącej geometrii.

- **E0-04 — kontrola duplikacji:** porównano F13.2 (prostokąty i siatki) oraz F20.3 (skala, wymiary, niepewność); dopisano do E0-04 odsyłacze zamiast przepisywania zaawansowanych treści, commit [66c9d99](https://github.com/mojealterego/Ontologia-Liczby-/commit/66c9d9948de4d457553948434a52cd9cb792795c), zaktualizowano protokół [e034624](https://github.com/mojealterego/Ontologia-Liczby-/commit/e034624d6f8e67271c3b0f0cce4c7838e8296144). Bilans stron bez zmian.


## E0-05 — Figury i przestrzeń (2 listopada 2026)

- **Opracowano na main:** [E0-05 — Figury i przestrzeń](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/manuscript/tom-01/E0/E0-05_FIGURY_I_PRZESTRZEN.md), commit [91d8654](https://github.com/mojealterego/Ontologia-Liczby-/commit/91d8654061e0b453ca93b5c53d6a8686bfcf508a); 15 definicji, 16 twierdzeń z 16 dowodami, 9 kontrprzykładów, 40 ćwiczeń i 4 problemy przekrojowe z rozwiązaniami. Ponownie odczytano źródło z main, Git blob 94863575d4040b9bf7e16a4e56bdd166c31db01a.
- **Wykorzystanie wcześniejszych treści:** skontrolowano F13.2 (siatki prostokątne), F17.3 (geometria dyskretna) i E0-04 (pomiar); rozdziały pozostawiono bez zmian, a E0-05 ograniczono do geometrii elementarnej, symetrii, orientacji i brył.
- **Testy:** [test_e005_geometry.py](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/tests/test_e005_geometry.py), commit [750acc4](https://github.com/mojealterego/Ontologia-Liczby-/commit/750acc4aad010a36324cccf003adf2d614c2e075). Lokalnie wykonano **9/9 unittest OK** na równoważnej kopii, bez potwierdzenia identyczności bajtowej z repozytorium.
- **PDF:** lokalnie skompilowano przez Pandoc/XeLaTeX **2-stronicowy podgląd A4 wybranych fragmentów**; nie jest to pełna kompilacja manuskryptu GitHub. [Workflow E0-05](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/.github/workflows/tom1-e005.yml) przewiduje kompilację dokładnego źródła i osobną bramkę 4 stron teorii + 4 stron ćwiczeń; wynik CI **niepotwierdzony**. Workflow: commity [f234729](https://github.com/mojealterego/Ontologia-Liczby-/commit/f234729fc7afb82e2003693a0ea10b0792fb83ad) i [7166724](https://github.com/mojealterego/Ontologia-Liczby-/commit/7166724aa3f18ab52cf673903969ea2ecdb5faff).
- **Dowody i ograniczenia:** [docs/DOWODY_E0_05_2026-11-02.md](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/docs/DOWODY_E0_05_2026-11-02.md), commit [fa33ec7](https://github.com/mojealterego/Ontologia-Liczby-/commit/fa33ec7ea52acb5620526ef6c392c4ad707b2948).
- **Status:** opracowanie źródłowe zapisane; pełna paginacja, minimalna objętość i integracja z monolitem 0.20 nadal niepotwierdzone. **585/1222 bez zmian**. Wstęp historyczny i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt taksonomii:** E1-01 — Ułamki i liczby wymierne, po kontroli materiałów już istniejących.


## E1-01 — Ułamki i liczby wymierne (2 listopada 2026)

- **Taksonomia:** E1-01, poziom I; po E0-05. Opracowano ułamki, proporcje, liczby dziesiętne, procenty, stosunki oraz błędy przybliżeń. Sprawdzono F14.3, F10.1 i F19.1; zachowano je bez zmian.
- **Dokładne źródło na main:** [E1-01](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/manuscript/tom-01/E1/E1-01_ULAMKI_I_LICZBY_WYMIERNE.md), finalny commit [49b1dcb](https://github.com/mojealterego/Ontologia-Liczby-/commit/49b1dcb1078299fbe0cae047d2668f9f15040fda), Git blob `5839e75196b47a6ab76bfe7b028d17aeac28234e`; 14 definicji, 21 twierdzeń z 21 dowodami, 12 kontrprzykładów, 60 zadań i 8 problemów z rozwiązaniami.
- **Testy:** [test_e101_rationals.py](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/tests/test_e101_rationals.py), commit [8e1ff69](https://github.com/mojealterego/Ontologia-Liczby-/commit/8e1ff6983eab4094028848abaf35fec6c396e25a); wykonano lokalnie **8/8 unittest OK** na pliku bajtowo identycznym z GitHub (blob `f582ab8a0dc1b2ba2abb348989e13c6778b32d09`).
- **Skład:** Pandoc/XeLaTeX skompilował dokładne źródło z GitHub do **9-stronicowego A4 PDF**; 5 stron teorii (ostatnia częściowa), 4 strony zadań (ostatnia częściowa), brak pustych stron; lokalna bramka `pdftotext` zaliczona. PDF jest podglądem samodzielnym, **nie** integracją z monolitem 0.20. [Workflow CI](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/.github/workflows/tom1-e101.yml) zapisany na main, **wynik CI niepotwierdzony**.
- **Dowody:** [docs/DOWODY_E1_01_2026-11-02.md](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/docs/DOWODY_E1_01_2026-11-02.md), commit [c379ed1](https://github.com/mojealterego/Ontologia-Liczby-/commit/c379ed10d9f151ea4b76982c66545a1d21c74115). Podano SHA-256 lokalnego PDF i źródła, Git blob oraz ograniczenia.
- **Status:** opracowanie źródłowe i lokalna kompilacja **potwierdzone**; CI, pełna recenzja matematyczna i integracja globalna **otwarte**. **585/1222 stron bez zmian**. Wstęp historyczny i wcześniejsze rozdziały nietknięte; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** E1-02 — Podzielność; sprawdzić istniejące dowody NWD/NWW i algorytmu Euklidesa.


## E1-02 — Podzielność (2 listopada 2026)

- **Taksonomia:** E1-02, poziom I, liczby pierwsze, NWD, NWW, rozkład na czynniki; kolejność po E1-01. Zbadano istniejące F15.1 i F15.2 przed napisaniem rozdziału, bez ich nadpisania.
- **Manuskrypt:** [E1-02_PODZIELNOSC.md](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/manuscript/tom-01/E1/E1-02_PODZIELNOSC.md), Git blob `9d1863788c36fb6b7c9a98da2509c8c861b85e60`, **25 450 znaków**. Zawiera 13 definicji, 23 twierdzenia z dowodami, 9 kontrprzykładów, 56 rozwiązanych zadań oraz 8 rozwiązanych problemów syntetycznych. Commity: [5941514](https://github.com/mojealterego/Ontologia-Liczby-/commit/5941514bba15c68d8ccb6e6a943f12ffe6f39198), [0a4363c](https://github.com/mojealterego/Ontologia-Liczby-/commit/0a4363c4610df1bbac6062c11bf71b3e40a77771), [7a57797](https://github.com/mojealterego/Ontologia-Liczby-/commit/7a5779788db1d25250cddaf3592efe53872aec05).
- **Testy:** [tests/test_e102_divisibility.py](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/tests/test_e102_divisibility.py), commit [9249aed](https://github.com/mojealterego/Ontologia-Liczby-/commit/9249aed2725ad59919a2650102c98605d50afc75). **8/8 lokalnie OK** na pliku bajtowo identycznym z repo (lokalny git hash-object = Git blob `110945c403c3a672450b5dec830468df7c3655e7`).
- **Skład:** [workflow tom1-e102.yml](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/.github/workflows/tom1-e102.yml), commit [d9bd685](https://github.com/mojealterego/Ontologia-Liczby-/commit/d9bd685d0cda064d8d9a353c131bf0a9d5f20d2b). Lokalnie Pandoc/XeLaTeX: **2 niepuste strony A4 tylko z wybranych fragmentów** (PDF SHA-256 `29ffc36a86e291eba4863e8ae37668fdcad4e3da0c7678c9b5e98ed4b8a46250`). **Nie** skompilowano pełnego repozytoryjnego źródła; objętość i CI niepotwierdzone.
- **Protokół:** [DOWODY_E1_02_2026-11-02.md](https://github.com/mojealterego/Ontologia-Liczby-/blob/main/docs/DOWODY_E1_02_2026-11-02.md), commit [892d987](https://github.com/mojealterego/Ontologia-Liczby-/commit/892d98753c09957b6cbd76bc22eb26bdc0ec7477).
- **Status:** opracowanie źródłowe i dokładny plik testów potwierdzone; pełny PDF, paginacja, CI i integracja niepotwierdzone. **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały nienaruszone; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** E1-03 — Potęgi i pierwiastki; najpierw sprawdzić istniejące F21.1 i powiązane materiały.


## E1-03 — Potęgi i pierwiastki (2 listopada 2026)

- **Taksonomia:** E1-03, poziom II; rozdział po E1-02, z odniesieniem do istniejącego F21.1, którego nie zmieniono.
- **Manuskrypt:** [`manuscript/tom-01/E1/E1-03_POTEGI_I_PIERWIASTKI.md`](../manuscript/tom-01/E1/E1-03_POTEGI_I_PIERWIASTKI.md), commit [1f9efa4](https://github.com/mojealterego/Ontologia-Liczby-/commit/1f9efa4668cfead40b1a4590792c292e086a6b36), Git blob `b69d3f4bd6c5e6efd439d570d64a72e218adb597`; odczyt z main potwierdził 16059 znaków, 11 definicji, 19 twierdzeń z dowodami, 60 rozwiązanych zadań i 4 problemy przekrojowe.
- **Testy:** [`tests/test_e103_powers_roots.py`](../tests/test_e103_powers_roots.py), commit [84f43ff](https://github.com/mojealterego/Ontologia-Liczby-/commit/84f43ffcc01c21885ca5bde009f56bfe0f2a4e8f). **Nie uruchomiono** jeszcze dokładnego pliku testów w Pythonie; nie potwierdzono CI.
- **Skład:** nie skompilowano pełnego PDF E1-03; próba pobrania dokładnego źródła do środowiska składu przez raw.githubusercontent.com zakończyła się błędem sieci (HTTP 000). Minimum 11 stron i wymagania ćwiczeniowe pozostają niepotwierdzone.
- **Status:** źródło zapisane i odczytane z main; nieodebrane wydawniczo. Historyczny wstęp i wcześniejsze rozdziały nienaruszone. Bez końcowego spisu treści i bez Tomu II. **585/1222 stron bez zmian** do integracji z rzeczywistym monolitem 0.20.


## E1-04 — Algebra elementarna (2 listopada 2026; etap źródłowy)

- **Taksonomia:** E1-04, **poziom I**, minimum **4 rzeczywiste strony** według `taxonomy/TEKST_ZRODLOWY_01.md`, s. 9/637. **Sprostowanie E1-03:** wcześniejszy zapis „poziom II / 11 stron” był nieprawidłowy; E1-03 również należy do poziomu I, minimum 4 strony. Poprawka klasyfikacji E1-03: [e9c5c61](https://github.com/mojealterego/Ontologia-Liczby-/commit/e9c5c6159c9b03633d228d7c03eae94d666f00b9).
- **Kontrola wcześniejszej treści:** sprawdzono F22.1 (semantyka zmiennych, wielomiany formalne) i F7.2 (aksjomatyka zera); nie zmieniono wcześniejszych rozdziałów ani historycznego wstępu.
- **Manuskrypt:** [E1-04_ALGEBRA_ELEMENTARNA.md](../manuscript/tom-01/E1/E1-04_ALGEBRA_ELEMENTARNA.md), commit [8199328](https://github.com/mojealterego/Ontologia-Liczby-/commit/81993282417bae3adc3b3e7cc75fe99549bbfe6f), Git blob `ff331e5085ae5632d62a061816e8d7a7ba35f983`; odczyt z main: 14 454 znaków, 12 definicji, 19 twierdzeń z dowodami, 10 kontrprzykładów, 40 rozwiązanych zadań i 4 problemy.
- **Testy:** [test_e104_elementary_algebra.py](../tests/test_e104_elementary_algebra.py), commit [ddbd836](https://github.com/mojealterego/Ontologia-Liczby-/commit/ddbd8368796947c180206b0db9380ba63ed7d788); lokalny `git hash-object` zgodny z blobem GitHub `f3bc7dd0fd2c80e784a4fc6ffbec27c03b18276d`. Wykonano **9/9 OK** E1-04.
- **Naprawa regresji E1-03:** lokalny test ujawnił 1 błąd porównania zmiennoprzecinkowego (`27**(2/3)=8.999999999999998`). Zmieniono asercje na `assertAlmostEqual`, commit [717178e](https://github.com/mojealterego/Ontologia-Liczby-/commit/717178e2cee72c566a75bd61ef2b21e852b32921). Po poprawce **8/8 OK** E1-03, razem **17/17 lokalnych testów OK**; oba lokalne pliki testowe są bajtowo identyczne z wersjami GitHub.
- **PDF:** lokalny podgląd *wybranych fragmentów*, Pandoc/XeLaTeX, **2 niepuste strony A4**, SHA-256 `e28040ad2bd89befa464906657b5cb4e86cc110353449b165def3eb7ecae12c8`. Nie jest pełnym składem źródła. [Workflow pełnego źródła E1-04](../.github/workflows/tom1-e104.yml), commit [260ede5](https://github.com/mojealterego/Ontologia-Liczby-/commit/260ede51590dfce96ff69d517e3ba9f6aa76ed5b), zapisany; jego wynik CI, pełna paginacja i odbiór minimum 4 stron **niepotwierdzone**.
- **Dowody:** [DOWODY_E1_04_2026-11-02.md](DOWODY_E1_04_2026-11-02.md), commit [6c4a7ff](https://github.com/mojealterego/Ontologia-Liczby-/commit/6c4a7ff2e1b69a17b3a322307f164875651d1bf5).
- **Stan kanoniczny:** **585/1222 stron bez zmian** do rzeczywistej integracji z monolitem 0.20. Bez końcowego spisu treści i bez Tomu II. **Następny punkt E1-05 — Równania liniowe**.


## Dyrektywa wydawnicza — 2026-11-02: limit rozmiaru tomów

- **Nie obowiązuje sztywne 1222 stron na tom.** Tom może liczyć mniej stron, jeżeli jego zawartość jest kompletna i spełnia wymagania merytoryczne oraz redakcyjne. Dawne `585/1222` jest wyłącznie historycznym wskaźnikiem wcześniejszego planu, nie aktualnym kryterium ukończenia.
- **Twardy limit artefaktu:** każdy końcowy PDF pojedynczego tomu musi mieć rozmiar **ściśle mniejszy niż 99 MB** (konserwatywnie przyjmować 99 000 000 bajtów jako górny próg, a test odbiorczy wymaga `size < 99000000`).
- Kontrola rozmiaru następuje po ostatecznym składzie, osadzeniu fontów, grafik i optymalizacji. Preferować tekst i wzory wektorowe; obrazy kompresować z zachowaniem czytelności. Gdy optymalizacja nie wystarcza, dzielić materiał na logiczne tomy bez pomijania treści.
- Liczba stron w nowych materiałach pozostaje niezaliczona do kanonicznego Tomu I przed rzeczywistą integracją z monolitem 0.20. Wstęp historyczny pozostaje bez zmian; nie tworzyć końcowego spisu treści przed ukończeniem Tomu I.


## E1-05 — Równania liniowe (2 listopada 2026)

- **Kolejność taksonomiczna:** po E1-04, przed E1-06. Poziom I. Sprawdzono istniejące F12.3 dotyczące odwracalności; pozostaje bez zmian.
- **Źródło:** [E1-05_ROWNANIA_LINIOWE.md](../manuscript/tom-01/E1/E1-05_ROWNANIA_LINIOWE.md), commit [ac19245](https://github.com/mojealterego/Ontologia-Liczby-/commit/ac19245fd64c80988362f8ab16208b8c678d3ab2), Git blob `d7250bad5058cd3ae6b4b9c089c2ebb3db043cc8`. Zweryfikowano ponownym odczytem: 19 523 znaki, 10 definicji, 18 twierdzeń z dowodami, 12 kontrprzykładów, 60 rozwiązanych zadań, 4 problemy syntetyczne.
- **Testy:** [test_e105_linear_equations.py](../tests/test_e105_linear_equations.py), commit [5fe7a69](https://github.com/mojealterego/Ontologia-Liczby-/commit/5fe7a69f4b7badf53dab47a1b3010503531cd20c). **11/11 OK** lokalnie; Git blob testu zgodny z lokalnym `git hash-object` (`597c65ac09d92b88f80b9553feb45285b42c9f69`).
- **PDF:** lokalnie skompilowany ReportLab **podgląd fragmentów**, 4 niepuste strony A4, 51 943 bajty, SHA-256 `aa7236de1f0816bb4b1face95a4a44690f0c1a4509441fc19255c519920c2b17`. **Nie** jest to pełny skład dokładnego źródła. Workflow [tom1-e105.yml](../.github/workflows/tom1-e105.yml), commit [65e7b4b](https://github.com/mojealterego/Ontologia-Liczby-/commit/65e7b4bb6d6f32fb4bd357ba097daa8addfbaffa), kompiluje pełne źródło i wymusza PDF <99 000 000 bajtów; wynik CI i pełna paginacja niepotwierdzone.
- **Protokół:** [DOWODY_E1_05_2026-11-02.md](DOWODY_E1_05_2026-11-02.md), commit [283e039](https://github.com/mojealterego/Ontologia-Liczby-/commit/283e039687217dc89ce63ecd84d31ac3143e135c).
- **Stan kanoniczny:** 585 stron w historycznym bilansie, bez doliczania E1-05 do monolitu 0.20. **1222 nie jest już wymaganym celem**, a limit końcowego PDF to <99 MB. Historyczny wstęp i wcześniejsze rozdziały zachowane; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** E1-06 — Planimetria; przed rozbudową sprawdzić istniejące rozdziały geometrii.


## E1-06 i E1-07 — Planimetria oraz Stereometria (2 listopada 2026)

**Znaczący przyrost źródłowy:** dwa następujące po sobie punkty taksonomii poziomu I, bez ingerencji w historyczny wstęp i wcześniejsze rozdziały.

- **E1-06 Planimetria:** [manuskrypt](../manuscript/tom-01/E1/E1-06_PLANIMETRIA.md), commit [63fe49d](https://github.com/mojealterego/Ontologia-Liczby-/commit/63fe49d80ea7f1613eb03abe6ba2010b54a52395), Git blob `f093c53b4a37402093f9341b10d192d4e94d1495`. 19 172 znaków, 15 definicji, 20 twierdzeń z dowodami, 9 kontrprzykładów, 50 rozwiązanych zadań i 6 problemów.
- **E1-07 Stereometria:** [manuskrypt](../manuscript/tom-01/E1/E1-07_STEREOMETRIA.md), commit [cf0bf95](https://github.com/mojealterego/Ontologia-Liczby-/commit/cf0bf95112f6cebb1a1a156d883ffb86e08425ee), Git blob `480fa5f5fc9ec2bfe87f88dc8bfe192f0aa06f24`. 18 498 znaków, 15 definicji, 18 twierdzeń z dowodami, 9 kontrprzykładów, 50 rozwiązanych zadań i 6 problemów.
- **Testy:** [E1-06](../tests/test_e106_planimetry.py), [E1-07](../tests/test_e107_stereometry.py). **25/25 lokalnie OK** na plikach o blob SHA zgodnych z GitHub; w E1-06 naprawiono dokładność obliczeń testu kątów (commit [3602c74](https://github.com/mojealterego/Ontologia-Liczby-/commit/3602c740e6bb8d34789385913bad7a1cae531ed2)).
- **PDF:** dwa lokalnie skompilowane i wyrenderowane podglądy wybranych fragmentów, po **2 strony A4** (E1-06: 43 493 bajty; E1-07: 42 733 bajty). Nie są pełnym składem manuskryptów. [Workflow](../.github/workflows/tom1-e106-e107.yml), commit [fa45060](https://github.com/mojealterego/Ontologia-Liczby-/commit/fa4506021f21ea07d98aca7c89b901512f9ca78d), kompiluje dokładne źródła i sprawdza **<99 000 000 bajtów**, lecz wynik CI pozostaje niepotwierdzony.
- **Protokół dowodowy:** [DOWODY_E1_06_E1_07_2026-11-02.md](DOWODY_E1_06_E1_07_2026-11-02.md), commit [92d30ca](https://github.com/mojealterego/Ontologia-Liczby-/commit/92d30caadb32ebc6cd6eabdd0fafbf3ef110b9ef).
- **Odbiór:** pełna paginacja, formalny przegląd wszystkich dowodów, zielony CI i integracja z monolitem 0.20 pozostają otwarte. **Historyczne 585 stron bez zmian; 1222 nie jest już wymaganym celem.** Wstęp i wcześniejsze rozdziały nienaruszone, bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** E1-08 — Geometria współrzędnych.

## 2026-11-02 — E1-08 Geometria współrzędnych i E1-09 Statystyka opisowa

- **Stan źródeł:** [E1-08](../manuscript/tom-01/E1/E1-08_GEOMETRIA_WSPOLRZEDNYCH.md) (commit [3a7f8f3](https://github.com/mojealterego/Ontologia-Liczby-/commit/3a7f8f30fafeb956e063c96c4eaca26134b50a26), blob `8ddf6828cb4a90de95e19d3fe3b1b33a32e7ac22`, 14 416 znaków) i [E1-09](../manuscript/tom-01/E1/E1-09_STATYSTYKA_OPISOWA.md) (commit [257374c](https://github.com/mojealterego/Ontologia-Liczby-/commit/257374c6ae99a77aa97846db43167bde9e6d8eb9), blob `105ac6b134f72e037f8058a38541b7534a926cf7`, 14 806 znaków) **zapisane i ponownie odczytane z `main`**.
- **Opracowanie:** E1-08: 14 definicji, 16 twierdzeń z dowodami, 10 kontrprzykładów, 36 rozwiązanych zadań i 3 problemy. E1-09: 15 definicji, 16 twierdzeń z dowodami, 10 kontrprzykładów, 36 rozwiązanych zadań i 3 problemy. Razem 32 twierdzenia i 78 rozwiązanych zadań/problemów. Rozdziały uzupełniają E0-05, E1-06, E1-07 i F24.1 bez ingerencji w wcześniejsze teksty.
- **Testy:** [E1-08](../tests/test_e108_coordinates.py), [E1-09](../tests/test_e109_statistics.py): **25/25 lokalnie OK**; lokalne `git hash-object` obu plików zgodne z GitHub blob (`d798f008fa52fa5fa08fa5a714d1a206d8aaa203`, `1c5556208c864525e6dd3a5a6f19d77478375430`). Dodatkowo **20/20** niezależnych testów własności.
- **Podglądy PDF:** Pandoc/XeLaTeX: 2 × 2 strony A4 z wybranych fragmentów, odpowiednio 43 075 i 41 473 bajty, SHA-256 `48ff238c1f918d365cb6419f4d05834651d83eefcab72fe96379df80bc649402` oraz `6a185c7799d78e6ed9aba241b69af679244a019beeff1a3ab151ff3632935dc1`. **Nie są pełnym składem** dokładnych źródeł.
- **CI:** [workflow](../.github/workflows/tom1-e108-e109.yml) zapisany na `main`, po korektach parsera matematycznego i formatu A4 (ostatni commit [b7b0d5a](https://github.com/mojealterego/Ontologia-Liczby-/commit/b7b0d5a12f67dab2e2cb4b79a46fc0c6cf8372da)). Kompilacja pełnych źródeł, sprawdzenie minimum 4 stron, tekstu w PDF i limitu `< 99 000 000` bajtów **zaprojektowane, ale wynik CI niepotwierdzony**.
- **Dowody:** [protokół E1-08/E1-09](DOWODY_E1_08_E1_09_2026-11-02.md), commit [e29dc7c](https://github.com/mojealterego/Ontologia-Liczby-/commit/e29dc7cc6f7b969fbdd10bec35a4c3c616afb9d2).
- **Blokady:** brak potwierdzonego zielonego CI, pełnego składu dokładnego źródła, formalnej recenzji wszystkich dowodów i integracji z monolitem 0.20. Historycznie zintegrowane **585 stron bez zmian**; 1222 nie jest już progiem wymaganym. Nie zmieniono wstępu historycznego, nie utworzono finalnego spisu treści i nie rozpoczęto Tomu II.
- **Następny punkt:** E1-10 — Prawdopodobieństwo elementarne.


## 2026-11-02 — E1-10 Prawdopodobieństwo elementarne i naprawa CI

- **Źródło:** [E1-10](../manuscript/tom-01/E1/E1-10_PRAWDOPODOBIENSTWO_ELEMENTARNE.md), commit [c08c9a3](https://github.com/mojealterego/Ontologia-Liczby-/commit/c08c9a3378cf329e083f9071763295f6d71628bd), Git blob `b7241e9c7c6708d7231881c44bc9f2c0d071b8f8`. Ponowny odczyt z `main`: 17 133 znaki, **16 definicji, 20 twierdzeń z dowodami, 12 kontrprzykładów, 52 rozwiązane zadania, 5 problemów przekrojowych**. Materiał E1-10 poziomu I, po E1-09; bez ingerencji w wcześniejsze teksty.
- **Testy:** [test_e110_probability.py](../tests/test_e110_probability.py), końcowy blob `29f4504fb41b8e5777ca3e775f60e5957fe26795`, poprawka [a19ffbe](https://github.com/mojealterego/Ontologia-Liczby-/commit/a19ffbe89ec8b1495df951dd6c97d56dd6a6db65). **12/12 lokalnie OK**, identyczny `git hash-object` uruchomionego pliku i GitHub; wyczerpująca enumeracja zdarzeń i próbek, arytmetyka dokładna `Fraction`.
- **PDF lokalny:** Pandoc/XeLaTeX, **3 strony A4**, 60 896 bajtów, SHA-256 `94e040892ed4db19b786bbdc256df8032078b592354f0a2a6b14b442562b74b4`. Wyłącznie podgląd wybranych fragmentów, **nie pełny skład**.
- **CI:** [workflow E1-10](../.github/workflows/tom1-e110.yml) zapisany; sprawdza pełne źródło, minimum 4 strony, obecność tekstu, rozmiar <99 000 000 bajtów i SHA-256. Poprzednie CI E1-08/E1-09 [#41395104462](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41395104462) rzeczywiście zawiodło przez brak `lmodern.sty`. Zapisano poprawkę instalacji `lmodern` na `main` w siedmiu workflow (E1-01, E1-02, E1-04, E1-05, E1-06/E1-07, E1-08/E1-09, E1-10). **Wyniki nowych przebiegów niepotwierdzone w chwili zapisu tego wpisu**.
- **Protokół:** [DOWODY_E1_10_2026-11-02.md](DOWODY_E1_10_2026-11-02.md), commit [9674b99](https://github.com/mojealterego/Ontologia-Liczby-/commit/9674b990a68f67224216b4d9a63b78c5b183e743).
- **Stan odbioru:** pełny skład i formalna recenzja wszystkich dowodów, zielone CI oraz integracja z monolitem 0.20 pozostają otwarte. **585 stron bez zmian**; 1222 stron nie jest już wymaganym celem. Każdy finalny tom PDF musi mieć mniej niż 99 MB (technicznie <99 000 000 bajtów). Historyczny wstęp bez ingerencji; bez finalnego spisu treści i bez Tomu II.
- **Następny punkt:** E1-11 — Modelowanie.


## Aneks dowodowy: potwierdzone GitHub Actions i pełny PDF (2026-11-02)

- **Zielony CI E1-10:** [przebieg 41400277877](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400277877), `success` na commit `51c53cc691e46470115e07c5d846969c570561d9`. Wykonano dokładny repozytoryjny plik testów: **12/12 OK**; wykonano kompilację **całego** źródła z `main` przez Pandoc/XeLaTeX.
- **Pełny PDF E1-10:** **7 stron A4**, **74 142 bajty**, SHA-256 `514252e11b2677acc85168f644e8e6f428f0b73cee12e8eea85a3674357603c2`. SHA-256 wejściowego Markdown: `f39450e586fbc530e2f8b5660424ec8fac25d93243581de4c523ff7b79156459`. [Artefakt GitHub Actions](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400277877) `tom1-e110-complete-pdf` (ID 13120248942). ZIP pobrano i rozpakowano lokalnie; SHA-256 rozpakowanego PDF zgodne z logiem CI, `pdfinfo` wskazuje A4 i 7 stron; `pdftotext` potwierdza obecność końcowego Problem P5. Każda strona zawiera ponad 1600 znaków wyekstrahowanego tekstu.
- **Wynik:** E1-10 ma potwierdzoną kompilację pełnego źródła i spełnia techniczny limit 99 MB. **Nie oznacza to jeszcze integracji z monolitem 0.20 ani pełnej recenzji wszystkich dowodów.**
- **Dodatkowa naprawa procesu:** [E1-08/E1-09, przebieg 41400284879](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400284879), `success`, 25/25 testów, dwa pełne PDF A4 po 6 stron (70 837 i 70 877 bajtów). Wcześniejsza blokada `lmodern.sty` usunięta w tych workflow. [E1-01, przebieg 41400317753](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400317753) również zakończył się `success`.


## Aneks końcowy tej tury — wszystkie E1-01–E1-10 mają zielone CI (2026-11-02)

- **E1-03:** dodano brakujący [workflow](../.github/workflows/tom1-e103.yml), commit [83346ab](https://github.com/mojealterego/Ontologia-Liczby-/commit/83346ab67f5865426fe6f18967385132ca8b4074); [przebieg 41401029789](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41401029789) `success`: **8/8 testów**, pełny PDF **7 stron A4, 74 898 B**, SHA-256 `a572670345cf6d42b8b9bb3092b7780893c77463512ed988d2bae16f2bba3cc5`.
- **E1-04:** [przebieg 41400610631](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400610631) `success`: **9/9 testów**, pełny PDF **5 stron A4, 62 945 B**, SHA-256 `88cd2e3cea3e2ad57d448c629bd26914ac90765d2d4527ecad019251c8f909c8`.
- **E1-01:** [przebieg 41400317753](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41400317753) `success`: **8/8 testów**, pełny PDF **9 stron A4, 80 446 B**, SHA-256 `871c7e974f609139e16e8f4508cf44d7b114133fd21b0f434b1ecf10e8dd4cc9`.
- **Wszystkie E1-01 do E1-10:** każdy z dziesięciu rozdziałów ma w tej turze **potwierdzony zielony przebieg GitHub Actions**, testy i kompletny osobny PDF A4. Z artefaktów pobrano wszystkie dziesięć PDF, sprawdzono `pdfinfo`, `pdftotext`, SHA-256 i brak pustych stron; łącznie **71 stron w osobnych plikach**, NIE w kanonicznym monolicie. Opracowano lokalny pakiet ZIP z 10 PDF i manifestem SHA-256 (702 955 B), bez publikowania finalnego Tomu I.
- **Ograniczenie:** wynik zielonego CI potwierdza kompilację i testy arytmetyczne, lecz nie formalną recenzję każdego dowodu ani integrację z monolitem 0.20. **Historyczne 585 stron bez zmian.** Nie tworzono końcowego spisu treści ani Tomu II.


## E1-11 — Modelowanie matematyczne: ukończony samodzielny rozdział źródłowy (2026-11-02)

- **Podstawa:** taksonomia poziomu I: E1-11 po E1-10, minimum 4 strony. Rozdział E1-11 jest ostatnim punktem edukacyjnej sekwencji E1, **nie** ostatnim punktem Tomu I.
- **Manuskrypt:** [E1-11 Modelowanie](../manuscript/tom-01/E1/E1-11_MODELOWANIE.md), commit [e93157b](https://github.com/mojealterego/Ontologia-Liczby-/commit/e93157babc7c2f09cf8f4aab15a76dcd360ae6dc), 21 717 znaków, Git blob cb5e2945c555e62a1485ad3d04134efa6f2cf93a. **18 definicji, 22 twierdzenia z dowodami, 12 kontrprzykładów, 52 zadania z rozwiązaniami i 5 problemów przekrojowych z rozwiązaniami.** Źródło ponownie odczytane z main.
- **Testy:** [20 testów dokładnej arytmetyki](../tests/test_e111_modeling.py), commit [ac00da0](https://github.com/mojealterego/Ontologia-Liczby-/commit/ac00da098e41cdc1f605037350c908ec5d953aab); GitHub Actions **20/20 OK**. Dodatkowo niezależne lokalne kontrole wybranych własności **13/13 OK**.
- **Workflow:** [tom1-e111.yml](../.github/workflows/tom1-e111.yml), commit [e6d0c63](https://github.com/mojealterego/Ontologia-Liczby-/commit/e6d0c63b72e7117e1b4ad37e442c84f830728696); [przebieg 41407934161](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41407934161) **success**. Pełny osobny PDF ze źródła repo: **8 niepustych stron A4, 83 012 B**, SHA-256 2806d4e9e55956b1e892472f084adcba9e2a9cfd9da646b230c36ff1ae71c379. Źródło SHA-256 f45678b3be1797618d36f18fa09040925cfe4e038a2878d533f7b829a91700bd. Artefakt Actions ID 13124262500. PDF pobrany i sprawdzony lokalnie, w tym podgląd wizualny stron 1 i 8.
- **Protokół:** [DOWODY_E1_11_2026-11-02.md](DOWODY_E1_11_2026-11-02.md), końcowy commit [9d3dce7](https://github.com/mojealterego/Ontologia-Liczby-/commit/9d3dce737bc898241bad53c833a4bbb649b2f49b).
- **Granica odbioru:** zielone CI i testy rachunkowe nie zastępują formalnego przeglądu wszystkich dowodów; brak integracji z kanonicznym monolitem 0.20. **Historyczne 585 stron bez zmian**, dawny cel 1222 stron nieobowiązkowy, końcowy PDF każdego tomu musi mieć mniej niż 99 000 000 B. Wstęp historyczny i wcześniejsze rozdziały bez ingerencji. Bez końcowego spisu treści i bez Tomu II.


## MSC 00A08 — Matematyka rekreacyjna i scalony korpus roboczy książki (2026-11-02)

- **Źródło kolejności:** po ukończeniu E1-11 następnym nieopracowanym wpisem indeksu poziomu I jest **00A08 — Recreational mathematics** (rodzina A, MSC2020, s. 9 źródłowej taksonomii, minimum 4 strony). Wstęp historyczny i wcześniejsze rozdziały bez ingerencji.
- **Nowy rozdział na main:** [00A08 — Matematyka rekreacyjna](../manuscript/tom-01/MSC00/00A08_MATEMATYKA_REKREACYJNA.md), commit [e1a51d3](https://github.com/mojealterego/Ontologia-Liczby-/commit/e1a51d38de2f00bf87018655ecdf93ce6b16f116), korekta ścisłości dowodu T12 commit [dc0b373](https://github.com/mojealterego/Ontologia-Liczby-/commit/dc0b373b2133b14aaaa27108055a3d177ba61b4b). **12 definicji, 20 twierdzeń z dowodami, 10 kontrprzykładów, 24 rozwiązane zadania.**
- **Testy na main:** [tests/test_msc00a08_recreation.py](../tests/test_msc00a08_recreation.py), commit [ee8922d](https://github.com/mojealterego/Ontologia-Liczby-/commit/ee8922d01680e8c3bff4c4bc2818985ead4a7dee), 20 testów do uruchomienia w CI. **Lokalnie** niezależne kontrole wybranych twierdzeń: **12/12 OK** (w tym 32 768 kolorowań K6); nie jest to potwierdzenie uruchomienia dokładnego pliku z main. [Workflow PDF i testów](../.github/workflows/tom1-msc00a08.yml), commit [55930e9](https://github.com/mojealterego/Ontologia-Liczby-/commit/55930e9dd7dc4f77627ad848495a33441126f546). Zielony wynik CI i pełny PDF 00A08 **jeszcze niepotwierdzone**.
- **Praca nad właściwą książką:** dodano [scripts/assemble_tom1.py](../scripts/assemble_tom1.py) (commit [90340f9](https://github.com/mojealterego/Ontologia-Liczby-/commit/90340f9bf51eb881755d3cf66d70c20a6cfb3942)), [11 testów scalania](../tests/test_assemble_tom1.py) (commit [bebc091](https://github.com/mojealterego/Ontologia-Liczby-/commit/bebc091e2e0a75595a579c366fc0cfbc792f04a9)), [stronę tytułową korpusu](TOM_I_KORPUS_ROBOCZY.md) (commit [f0c45ab](https://github.com/mojealterego/Ontologia-Liczby-/commit/f0c45abc62e25f0c989ecc81f2e6546e81971afa)) i [workflow łączący 17 rozdziałów E0/E1/00A08 w jeden PDF](../.github/workflows/tom1-book-working.yml) (commit [b151a87](https://github.com/mojealterego/Ontologia-Liczby-/commit/b151a87c5d0257314a2f6ff49cb53323f5d24aad)).
- **Rzeczywisty scalony PDF lokalny:** połączono pełne PDF E1-01–E1-11 z nową stroną tytułową w **jeden dokument 80 stron A4, 937 612 bajtów**, SHA-256 **c4a691a0e49d3fb222ed7c9f1f0848e7485cba52971631705b43aa160f628f19**. Sprawdzono manifest SHA-256 dziesięciu rozdziałów, SHA E1-11, pdfinfo, pdftotext oraz obrazy pierwszej i ostatniej strony; **0 pustych stron i 0 słów poza obszarem stron**. Okładka robocza: obsydian i złoto. **To korpus roboczy bez oryginalnego wstępu i bez bloku F; nie jest kanonicznym Tomem I ani plikiem PDF na GitHub.** Nowy workflow ma wytworzyć pełniejszy 17-rozdziałowy korpus, ale jego wykonanie pozostaje niepotwierdzone.
- **Blokada integracji 0.20:** wydanie 0.20 ma według dokumentacji 864 strony, SHA-256 ea888d112cc255856c03cead7428d4f817ad2c692d0e6e6d61f46ae17738dd43. Brak binarnego oryginału na main. Biblioteczny roboczy monolit 764 stron nie jest zamiennikiem, a próba autoryzowanej materializacji zakończyła się odmową. Skrypt odrzuca pliki z niezgodnym SHA, a po dostarczeniu oryginału będzie kontrolować 33 strony wstępu.
- **Pełny protokół:** [DOWODY_MSC00A08_KORPUS_TOM_I_2026-11-02.md](DOWODY_MSC00A08_KORPUS_TOM_I_2026-11-02.md), commit [38a9735](https://github.com/mojealterego/Ontologia-Liczby-/commit/38a97357808a29c5ba4d85031fb1b0c4c6edcd57), aktualizacja finalnej sumy SHA-256 [5a17aaf](https://github.com/mojealterego/Ontologia-Liczby-/commit/5a17aaf1d103bf7d8d1552b70abaa85a040b84a3).
- **Bilans kanoniczny:** historyczne **585 stron bez zmian**. 1222 strony nie są obowiązkowe; finalny PDF tomu musi mieć **<99 000 000 bajtów**. Bez końcowego spisu treści i bez Tomu II.
- **Następny punkt taksonomii:** 00A09 — Popularization of mathematics.


## MSC 00A09 — Popularyzacja matematyki; rozbudowa ciągłej książki (2026-11-02)

- **Źródłowa kolejność:** po 00A08 występuje 00A09 (*Popularization of mathematics*), rodzina A, poziom I, strona 9 taksonomii, minimum 4 strony. Odczytano rejestr na main przed zmianami (blob 4a7433c812f304d81f8443d1f5ace34cc6514ce7); nowy plik przed utworzeniem nie istniał.
- **Manuskrypt zapisany na main:** [00A09 — Popularyzacja matematyki](../manuscript/tom-01/MSC00/00A09_POPULARYZACJA_MATEMATYKI.md), commit [23086e16](https://github.com/mojealterego/Ontologia-Liczby-/commit/23086e16ae8c241a5bc414d63f8629f6d607ebc0), **14 definicji, 14 twierdzeń z dowodami, 10 kontrprzykładów, 18 zadań rozwiązanych**. Tematy: logika komunikatów, procenty, jednostki, skale wykresów, Bayes, paradoks agregacji, niepewność i odtwarzalność.
- **Testy:** [tests/test_msc00a09_popularization.py](../tests/test_msc00a09_popularization.py), commit [878f06c3](https://github.com/mojealterego/Ontologia-Liczby-/commit/878f06c305be65b2a27e6a25eef191c30ab7c606), korekta [db2bf511](https://github.com/mojealterego/Ontologia-Liczby-/commit/db2bf511ee8aabfe9275c5c7baf9c1687c862455); dokładny lokalny plik o identycznym Git blob SHA bc0b7c312ec74e08444ed1eac9e04a93875fb8a7: **unittest 18/18 OK**, compileall OK; dodatkowo **15/15** niezależnych kontroli rachunkowych. Testy skończone nie są pełną recenzją dowodów.
- **Skład PDF:** lokalny **2-stronicowy podgląd wybranych fragmentów** (49 887 B, SHA-256 3c5e2481e61ad80497b189a9a0f7775f46362d768af73778b2ecbf50b21fc8ed); kontrola tekstu, renderów i marginesów OK. **Nie jest to pełny PDF rozdziału.** [Workflow 00A09](../.github/workflows/tom1-msc00a09.yml), commit [153acfe5](https://github.com/mojealterego/Ontologia-Liczby-/commit/153acfe56dd3463a3e953ef272806b005ebf409a), ma kompilować pełny plik i wymagać >=4 stron; **wynik CI niepotwierdzony**.
- **Książka ciągła:** [workflow roboczego Tomu I](../.github/workflows/tom1-book-working.yml) rozszerzono na **18 rozdziałów** (5 E0 + 11 E1 + 00A08 + 00A09), commit [639c8fbe](https://github.com/mojealterego/Ontologia-Liczby-/commit/639c8fbee74f579a46ff1f3619b6b07d3c389b3c). Nie potwierdzono jeszcze nowego artefaktu 18-rozdziałowego; wcześniejszy PDF E1 liczący 80 stron pozostaje osobnym roboczym korpusem.
- **Pełny protokół:** [DOWODY_MSC00A09_2026-11-02.md](DOWODY_MSC00A09_2026-11-02.md), commit [055b0669](https://github.com/mojealterego/Ontologia-Liczby-/commit/055b066943914965f640ec0df9f88883833fe437).
- **Kanoniczny bilans:** **585 stron bez zmian**, brak integracji z oryginałem 0.20 (864 strony, binarium nieobecne na main). Cel 1222 nieobowiązkowy; końcowy PDF musi mieć <99 000 000 B. Wstęp historyczny i wcześniejsze rozdziały bez ingerencji; bez końcowego spisu treści i bez Tomu II.
- **Następny punkt:** 97C20 — *Affective behavior and mathematics education*, poziom I, strona 10 taksonomii.


## MSC 97C20 — Afektywne aspekty edukacji matematycznej (2026-11-02)

- **Taksonomia:** 97C20, rodzina G, autorski poziom I, s. 10, minimum 4 strony. Pozycja następuje po 00A09; kolejną pozycją jest **97C30 — procesy poznawcze i teorie uczenia się**.
- **Na main:** [pełny manuskrypt 97C20](../manuscript/tom-01/MSC97/97C20_AFEKTYWNE_ASPEKTY_EDUKACJI_MATEMATYCZNEJ.md), commit [1385e5b](https://github.com/mojealterego/Ontologia-Liczby-/commit/1385e5bb8260ab0fa7cf664d56017def1de223fb), blob `c7d21304bb8c151d6eba608464e4e8fe18b7b46f`: **15 definicji, 16 twierdzeń z dowodami, 10 kontrprzykładów, 20 zadań rozwiązanych**, 17 096 znaków.
- **Testy:** [test_msc97c20_affective.py](../tests/test_msc97c20_affective.py), commit [98fdc93](https://github.com/mojealterego/Ontologia-Liczby-/commit/98fdc9372f752eb640f84bea2bcd9938172deff3). Lokalny plik ma identyczny Git blob SHA `522b042a37c43365b222d3f7a1e0202c5a5ded2a`; **unittest 20/20 OK**, compileall OK. Kontrole skończone nie zastępują formalnej recenzji dowodów.
- **Podgląd PDF:** lokalnie skompilowano **2 strony A4 wybranych fragmentów** przez Pandoc/XeLaTeX, **53 801 B**, SHA-256 `92d34fdc4e34ca9cf48a30a257384185533ffdc02015f2e2f3e0fc1edc95afb1`; tekst niepusty, 0 słów poza obszarem bezpieczeństwa 10 pt. To nie jest pełny skład źródła.
- **CI/PDF pełnego rozdziału:** [workflow 97C20](../.github/workflows/tom1-msc97c20.yml), commit [3186198](https://github.com/mojealterego/Ontologia-Liczby-/commit/31861987adc74c527b1c94e242e7a1026178c694), zapisany. **Zielony przebieg i pełny PDF niepotwierdzone.**
- **Ciągła książka:** [workflow korpusu](../.github/workflows/tom1-book-working.yml) rozszerzono na **19 rozdziałów** (5 E0, 11 E1, 00A08, 00A09, 97C20), commit [4543e9a](https://github.com/mojealterego/Ontologia-Liczby-/commit/4543e9ac3d26b9b1a8dd5f1a0661f845c9daa653). [Metryka korpusu](TOM_I_KORPUS_ROBOCZY.md) poprawiona, commit [97edf94](https://github.com/mojealterego/Ontologia-Liczby-/commit/97edf94a38f8f5405cba4b74fd3d8b6496accfb8). **Nie potwierdzono wykonania nowego składu 19 rozdziałów**.
- **Dowody:** [DOWODY_MSC97C20_2026-11-02.md](DOWODY_MSC97C20_2026-11-02.md), commit [7a0f082](https://github.com/mojealterego/Ontologia-Liczby-/commit/7a0f082f792bf85262d904b716a8f42d9968d5c1).
- **Bilans kanoniczny:** 585 stron bez zmian, 1222 nieobowiązkowe, PDF finalnego tomu <99 000 000 B. Brak binarnego 0.20 (864 strony wg dokumentacji) na main; wstęp historyczny i poprzednie rozdziały bez ingerencji. Bez końcowego spisu treści i bez Tomu II.


## Potwierdzony ciągły PDF Tomu I — 19 rozdziałów i kontrola granic (2026-11-02)

- **MSC 97C20, zielony CI:** [GitHub Actions 41428891204](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41428891204), **20/20 testów**, pełny PDF **6 stron A4, 78 953 B**, SHA-256 `412940731109a0972fd453fd3d95631bc0cbed446568865196cc74a11492f056`. Artefakt ID `13133866318` pobrany i zweryfikowany.
- **Rzeczywista scalona książka robocza:** [GitHub Actions 41428942141](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41428942141), **success**; 19 pełnych rozdziałów, **134 strony A4, 1 633 129 B**, SHA-256 `1f87d9c33bcbd537e15009612738a1cf3c3a6c84a8063a28be829f520dc0dbb2`, artefakt ID `13133371880`, 0 pustych stron. W tym wydaniu **brak** oryginalnego wstępu i kanonicznego monolitu 0.20, dlatego nie jest to ukończony Tom I.
- **Kontrola druku:** w pierwszym 134-stronicowym składzie stwierdzono dwa minimalne przekroczenia granic stron (s. 15 i 31). Dodano [scripts/pdf_bounds.py](../scripts/pdf_bounds.py), commit [0a05bf9](https://github.com/mojealterego/Ontologia-Liczby-/commit/0a05bf9472f69e3714eb1f8dc9c6deb0d69b7a1f), oraz integrację preflight w workflow, commit [b69267b](https://github.com/mojealterego/Ontologia-Liczby-/commit/b69267b9fddef27bbd1b167329a3d1e0d08b0293). Lokalnie na kopii pełnego PDF poprawiono **2/2 strony**, po poprawce 0 przekroczeń i 134 niepuste strony. Nowy CI [41429743116](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41429743116) uruchomiony; status końcowy do potwierdzenia.
- **Protokół:** [DOWODY_MSC97C20_2026-11-02.md](DOWODY_MSC97C20_2026-11-02.md), aneks CI commit [79b1a3a](https://github.com/mojealterego/Ontologia-Liczby-/commit/79b1a3a33763c82f0138eb41250fc6f596ecd1bc).
- **Bilans kanoniczny:** historyczne **585 stron bez zmian**, dawny cel 1222 nieobowiązkowy, limit końcowego PDF <99 000 000 B. Wstęp historyczny i poprzednie rozdziały bez ingerencji; nie tworzono końcowego spisu treści ani Tomu II.


## Zamknięcie kontroli składu 19-rozdziałowego (2026-11-02)

- **Nowy zielony CI po korekcie overflow:** [run 41429743116](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41429743116), commit [b69267b](https://github.com/mojealterego/Ontologia-Liczby-/commit/b69267b9fddef27bbd1b167329a3d1e0d08b0293), `assemble` success.
- **Poprawiony pełny korpus roboczy:** **134 strony A4, 19 rozdziałów, 1 656 878 bajtów**, SHA-256 `36ae4449b2e559fe114cf516e96b6e410b19816836a2361f61cf74d01d25f74b`, artefakt CI ID **13133089212**. Plik pobrano, sprawdzono manifest i SHA-256, 0 pustych stron i **0 słów poza granicami bezpieczeństwa 5 pt**. Pierwsza i ostatnia strona obejrzane wizualnie.
- **Protokół:** [DOWODY_MSC97C20_2026-11-02.md](DOWODY_MSC97C20_2026-11-02.md), aneks odbiorczy commit [215970a](https://github.com/mojealterego/Ontologia-Liczby-/commit/215970addbf6490aadd4a8fa88e5b6c94a8323aa).
- **Granica odbioru:** jest to realna książka robocza, lecz **bez kanonicznego monolitu 0.20 i oryginalnego wstępu historycznego**. Zintegrowane historyczne **585 stron bez zmian**; 1222 nieobowiązkowe; finalny PDF tomu <99 000 000 B. Bez końcowego spisu treści i bez Tomu II.


## MSC 97C30 — Procesy poznawcze i modele uczenia się; integracja z dostarczonym monolitem (2026-11-02)

- **Źródło:** MSC2020 97C30, poziom autorski I, strona 10 taksonomii, minimum 4 strony. Po wcześniejszym 97C20 następny punkt; kolejny w indeksie: **97D40**. Przed zmianami odczytano bieżący rejestr (blob 80ae8e08072e843d0bf2ea7203673ce7244452da).
- **Nowy manuskrypt na main:** [97C30](../manuscript/tom-01/MSC97/97C30_PROCESY_POZNAWCZE_I_TEORIE_UCZENIA.md), commit [0d03fb7](https://github.com/mojealterego/Ontologia-Liczby-/commit/0d03fb719cec4a47005d3280030dfa5cf8a50b87), blob a466a83b9c694d7434bd39daa32384a856e527e7, **15 definicji, 16 twierdzeń z dowodami, 10 kontrprzykładów, 20 rozwiązanych zadań**.
- **Testy:** [28 testów](../tests/test_msc97c30_cognition.py), commit [ec2f4be](https://github.com/mojealterego/Ontologia-Liczby-/commit/ec2f4be3f2a4716cee992c91820af05db772f02e), blob 81f5cb9b4b438042ad977a5ee929f01a952816a0. **Lokalnie 28/28 OK**, dokładnie ten sam blob co na main. [GitHub Actions 41438424204](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41438424204) **success**, w logach 28/28 OK i kompilacja pełnego rozdziału. Artefakt CI ID 13137857119.
- **Pełny podgląd PDF:** Pandoc/XeLaTeX, **6 stron A4, 79 679 B**, SHA-256 d1342701ca10f9d0a4003dab99ca563e18c2e4516474fc0f971cd8f87d7cc7c9. Źródło SHA-256 cc63fa0d81f77b7fc5d95b6cb21e7453c52372c1bbde5012e98cfee62f46b04a. Wszystkie strony zawierają tekst; kontrola znaczników T16, K10, Z20 i wizualna kontrola strony 1.
- **Ciągły korpus:** [workflow](../.github/workflows/tom1-book-working.yml) rozszerzony do **20 rozdziałów**, commit [5fdc33e](https://github.com/mojealterego/Ontologia-Liczby-/commit/5fdc33e1b6e5f22846301fd2f6a94ac7c2939a0f). Nowy CI [41438448699](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41438448699) uruchomiony; wynik końcowy w chwili aktualizacji **niepotwierdzony**.
- **Właściwa książka z dostarczonej kopii:** otrzymany monolit 629 stron, SHA-256 cd2e5e9ef0adefc3344ff8a7a1bcaa4befd2e1b85b4a711a36c3a0c179cb1309. Lokalnie złożono **641-stronicowy niekanoniczny podgląd**: niezmienione 629 stron + 6 stron pełnego 97C20 + 6 stron pełnego 97C30; **8 098 355 B**, SHA-256 57cb34ce2b432def6b65a000a45d83570f1e8ce949332c83cab3fa7f4c894dcb. Zweryfikowano zgodność tekstu wszystkich 629 stron, identyczność renderów stron 1, 2, 33, 34, 629 oraz zachowanie 585 zakładek i 4 odsyłaczy PDF. [Reprodukcyjny skrypt](../scripts/assemble_supplied_monolith.py), commit [6073ef7](https://github.com/mojealterego/Ontologia-Liczby-/commit/6073ef7f09d21bf1d085cfbafb15fae9240b91f2).
- **Granica kanoniczna:** otrzymany monolit 629 stron **nie jest** oryginałem wydania 0.20, które dokumentacja opisuje jako 864 strony i SHA-256 ea888d112cc255856c03cead7428d4f817ad2c692d0e6e6d61f46ae17738dd43. Podgląd 641 stron nie oznacza integracji 0.20 ani ukończenia Tomu I. Historyczne **585 stron bez zmian**; dawny cel 1222 stron nieobowiązkowy; finalny PDF <99 000 000 B. Oryginalny wstęp i poprzednie strony pozostają nienaruszone; bez końcowego spisu treści i bez Tomu II.
- **Pełny protokół:** [DOWODY_MSC97C30_INTEGRACJA_2026-11-02.md](DOWODY_MSC97C30_INTEGRACJA_2026-11-02.md). Otwarte: formalna recenzja wszystkich dowodów, walidacja empiryczna modeli oraz kanoniczna integracja 0.20.


### Odbiór CI MSC 97C30 i korpusu 20 rozdziałów (2026-11-02)

- [MSC 97C30, run 41438424204](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41438424204) **success**: **28/28 testów**, pełny PDF ze źródła main, artefakt ID 13137857119.
- [Ciągły korpus, run 41438448699](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41438448699) **success**: **20 rozdziałów, 140 stron A4, 1 743 342 B**, artefakt ID 13137322247, **97/97 testów** (11 + 20 + 18 + 20 + 28). To **niekanoniczny** korpus E0/E1/MSC bez historycznego wstępu.
- Niezależny lokalny **641-stronicowy podgląd** z dostarczonego monolitu 629 stron i dwóch suplementów 97C20/97C30 zachowuje wszystkie oryginalne strony, ale **nie jest wydaniem 0.20**. Historyczne 585 stron bez zmian. Szczegóły w [protokole](DOWODY_MSC97C30_INTEGRACJA_2026-11-02.md).


## MSC 97D40 — Metody nauczania matematyki (2026-11-02)

- **Nowy rozdział na main:** [97D40](../manuscript/tom-01/MSC97/97D40_METODY_NAUCZANIA_MATEMATYKI.md), commit [569e303f](https://github.com/mojealterego/Ontologia-Liczby-/commit/569e303f9c4ebd08e5fd8bfa8f6d1e767118ed23). Zawartość: 15 definicji, 16 twierdzeń z dowodami, 10 kontrprzykładów, 20 rozwiązanych zadań. Modelowe twierdzenia matematyczne nie są empirycznym dowodem skuteczności pedagogicznej.
- **Testy zapisane na main:** [test_msc97d40_teaching.py](../tests/test_msc97d40_teaching.py), commit [08f87d8e](https://github.com/mojealterego/Ontologia-Liczby-/commit/08f87d8e9540a9245eb2c8133532db368625b5c0), 17 przypadków unittest; **uruchomienie CI i pełnego testu tego pliku niepotwierdzone na etapie tego wpisu**.
- **Stan integracji:** źródłowy monolit 629 stron (SHA-256 cd2e5e9ef0adefc3344ff8a7a1bcaa4befd2e1b85b4a711a36c3a0c179cb1309) pozostaje odrębny od kanonicznego wydania 0.20 (864 strony według dokumentacji). Nie doliczono stron do historycznego bilansu 585; nie ingerowano w historyczny wstęp i dotychczasowy materiał. Nie tworzono końcowego spisu treści ani Tomu II.
- **Otwarte:** pełna kompilacja nowego rozdziału, testy CI, recenzja dowodów i docelowa integracja z 0.20. Limit końcowego PDF: rozmiar <99 000 000 B.


## MSC 97D40 — rozszerzenie poziomu III i weryfikacja (2026-11-02)

- **Weryfikacja klasyfikacji:** oficjalny MSC2020 zawiera **97D40 Mathematics teaching methods and classroom techniques** (s. 118); lokalny indeks `taxonomy/index/MSC_LEVEL_III.tsv` pomijał ten wpis. Uzupełniono go na `main` w commicie [785807ff](https://github.com/mojealterego/Ontologia-Liczby-/commit/785807ff3058dbcdd93b54b74acc4d4ab446926d). Rozdział poprawiono z poziomu I na **III**, commit [cc04cd30](https://github.com/mojealterego/Ontologia-Liczby-/commit/cc04cd303142c6eb5b3de21469acedb7ef3eb6ec); **minimum 44 stron nieosiągnięte — status częściowy**.
- **Nowa treść:** [97D40, rozszerzenie III-A](../manuscript/tom-01/MSC97/97D40_METODY_NAUCZANIA_MATEMATYKI.md), commit [0f0f53ec](https://github.com/mojealterego/Ontologia-Liczby-/commit/0f0f53ec02a15a88e96c4ada611690627f6e85ec). Dodano D16–D19, T17–T24 z dowodami, K11–K14 i Z21–Z30. Materiał wcześniejszy pozostał zachowany.
- **Testy:** bazowe **17/17 lokalnie OK** na pliku o Git blob SHA-1 `d669beb6d57ac20ac3359cc4fe0aef38495aa6d8`; rozszerzenie [test_msc97d40_advanced.py](../tests/test_msc97d40_advanced.py), commit [6cd33c17](https://github.com/mojealterego/Ontologia-Liczby-/commit/6cd33c17aec53a0ba0c77d24361b84c3b8b1ab8c); niezależnie **3436/3436 kontroli matematycznych lokalnie OK**. Odbiór pełnego CI w chwili wpisu **niepotwierdzony**.
- **CI i książka:** [workflow korpusu](../.github/workflows/tom1-book-working.yml) uwzględnia **21 rozdziałów**, a [workflow rozdziału](../.github/workflows/tom1-msc97d40.yml) kompiluje pełny PDF 97D40. Lokalnie utworzono **2-stronicowy podgląd rozszerzenia**, dołączony do zachowanego 641-stronicowego podglądu z oryginalnego monolitu 629 stron; wynik **643 strony, 8 149 313 B**, SHA-256 `3d10e3dcc6650c120272e1e5c6a2e0e31a2fce4a787fcd26742820a5984b2868`. Zweryfikowano 629/629 oryginalnych stron tekstowo, 5 próbek renderu, 4 odsyłacze, 589 zakładek.
- **Protokół:** [DOWODY_MSC97D40_ROZSZERZENIE_IIIA_2026-11-02.md](DOWODY_MSC97D40_ROZSZERZENIE_IIIA_2026-11-02.md), commit [f315ba5f](https://github.com/mojealterego/Ontologia-Liczby-/commit/f315ba5f8be0ed767762e40e826ffefb50d7c4a3).
- **Granica:** 643-stronicowy podgląd nie jest wydaniem 0.20 (dokumentacja: 864 strony). Historyczne **585 stron bez zmian**, bez końcowego spisu treści i bez Tomu II; finalny PDF <99 000 000 B. Pełny odbiór poziomu III, CI i formalna recenzja pozostają otwarte.


### Odbiór pełnego MSC 97D40 i integracja książki (2026-11-02)

- **27/27 testów lokalnie OK** na dokładnych blobach testów z `main` (17 bazowych i 10 rozszerzonych). [CI 97D40 run 41445051738](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41445051738) **success**, pełny rozdział **6 stron, 83 793 B**, SHA-256 `6f5392d53c5f6ef0ad6c45584a58295629108edb214f40ba97170d78d54be20a`, artefakt 13141781622.
- **Książka robocza z rzeczywistym monolitem:** do poprzednich 641 stron dołączono pełny 6-stronicowy PDF 97D40 z CI, wynik **647 stron, 8 187 625 B**, SHA-256 `d6bc2d8b3964b05ac598f8541d79f38b1ba967fd0178784b9866cce4e07288d7`. Sprawdzono zgodność tekstową 629/629 oryginalnych stron, 641/641 stron poprzedniej integracji, 6/6 stron nowego rozdziału, 5 renderów, 589 zakładek i 4 odsyłaczy. **Niekanoniczne 0.20**; 585 stron bez zmian.
- **CI 21-rozdziałowego korpusu:** [run 41445046049](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41445046049) **failure** z powodu jednego słowa poza marginesem 5 pt po scaleniu 146 stron; testy zakończyły się sukcesem. Poprawka workflow [601c8bdf](https://github.com/mojealterego/Ontologia-Liczby-/commit/601c8bdf7600f7f69f8030c342179b9ac0580aa9) dodaje `--repair` i ponowną walidację; nowy wynik wymaga potwierdzenia.
- Pełny protokół: [DOWODY_MSC97D40_ROZSZERZENIE_IIIA_2026-11-02.md](DOWODY_MSC97D40_ROZSZERZENIE_IIIA_2026-11-02.md), aneks commit [a63599d6](https://github.com/mojealterego/Ontologia-Liczby-/commit/a63599d6e9dfe072acfd5c79e0c3a1860bae5f2a).

- **Korekta liczby testów w CI:** run 41445051738 wykonał 17 bazowych testów (sukces kompilacji pełnego PDF); **10 dodatkowych testów** potwierdzono lokalnie na dokładnym blobie, ale w tym przebiegu nie były uruchomione. Poprawiono workflow rozdziału w commicie [568e303e](https://github.com/mojealterego/Ontologia-Liczby-/commit/568e303ece25e3a52f75c91ef8edbbf49e700b8d), aby następny CI uruchamiał **27/27**. Zielony wynik po poprawce niepotwierdzony na etapie tego wpisu.


## MSC 97D40 — rozszerzenie III-B, diagnoza adaptacyjna (2026-11-02)

- **Zapis na main:** [rozdział MSC 97D40](../manuscript/tom-01/MSC97/97D40_METODY_NAUCZANIA_MATEMATYKI.md), commit [67794720](https://github.com/mojealterego/Ontologia-Liczby-/commit/677947201bf12aa22725a6de099110940aa38d14). Rozszerzenie D20–D27, T25–T32 (dowody), K15–K18, Z31–Z40. Materiał wcześniejszy pozostawiono bez zmian. Nadal nieosiągnięte minimum 44 stron poziomu III.
- **Testy zapisane na main:** [test_msc97d40_information.py](../tests/test_msc97d40_information.py), commit [1a8e7aa5](https://github.com/mojealterego/Ontologia-Liczby-/commit/1a8e7aa502a735eaec7783022a2897a1715870b1), 7 przypadków unittest. Niezależnie lokalnie wykonano 1153 kontrole liczbowe (64 rozkłady i 1089 modeli obserwacji), wszystkie zaliczone. **Nie potwierdzono jeszcze uruchomienia nowego pliku unittest w CI.**
- **Podgląd PDF lokalny:** kompilacja 1 strony wybranych dowodów i złączenie z wcześniejszą 647-stronicową książką roboczą; **648 stron, 8 022 407 bajtów**, SHA-256 `adf6bd686f42dfc4fea577cb597e70f0c3430fcc0e2fd161602d7324413bd62c`. Podgląd **nie obejmuje pełnego nowego rozszerzenia** i nie jest wydaniem 0.20. Nie zastępuje wcześniej skompilowanych stron ani historycznego wstępu.
- **Otwarte:** pełny PDF aktualnego MSC 97D40, zielony CI z nowymi testami, recenzja wszystkich dowodów, osiągnięcie 44 stron oraz kanoniczna integracja z binarnym wydaniem 0.20 (864 strony według dokumentacji). Historyczne 585 stron bez zmian; 1222 stron nieobowiązkowe; końcowy PDF <99 000 000 B. Bez końcowego spisu treści i bez Tomu II.


## MSC 97D40 — III-C i pełny roboczy PDF 653 stron (2026-11-02)

- **Zapis treści na main:** [MSC 97D40](../manuscript/tom-01/MSC97/97D40_METODY_NAUCZANIA_MATEMATYKI.md), III-C commit [f500ebce](https://github.com/mojealterego/Ontologia-Liczby-/commit/f500ebcebfc96510759758bf5eda0792ad6b3d63) oraz korekta D35/K21 commit [39e10a5b](https://github.com/mojealterego/Ontologia-Liczby-/commit/39e10a5b9a1e2ecaae1c996a78f2cbc2a7529074). III-C zawiera 9 nowych definicji D28–D36, 10 twierdzeń T33–T42 z dowodami, 4 kontrprzykłady K19–K22 i 10 rozwiązanych zadań Z41–Z50.
- **Testy:** [III-C](../tests/test_msc97d40_uncertainty.py), commit [1754c644](https://github.com/mojealterego/Ontologia-Liczby-/commit/1754c644a4d1897b65b74a8e2346a70759b361b2); [III-B](../tests/test_msc97d40_information.py), commit [1a8e7aa5](https://github.com/mojealterego/Ontologia-Liczby-/commit/1a8e7aa502a735eaec7783022a2897a1715870b1). Lokalnie **17/17 unittest OK**, z potwierdzeniem identyczności Git blob SHA-1 obu plików z main. CI rozdziału i korpusu zaktualizowano, ale **nowego zielonego przebiegu Actions jeszcze nie potwierdzono**.
- **PDF pełnego roboczego rozdziału:** poprzednie 6 stron + pełne III-B 3 strony + pełne III-C 3 strony = **12 stron**, SHA-256 5db5484dc39192b09e9edf6f0589bcc3cf6ec4fa4338aa6185d4560aa4b00e26. Nowe sekcje skompilowano lokalnie przez Pandoc/XeLaTeX; zero słów poza marginesem 5 pt. Nie jest to bezpośrednia kompilacja całego dokładnego HEAD Markdown z main.
- **Scalony Tom I, podgląd niekanoniczny:** **653 strony, 8 312 064 bajty**, SHA-256 3302fae91920547116b0c537d0000f535d7bd6b7a022c71cdfc1606bc8819955; 629 stron oryginału + 6 stron 97C20 + 6 stron 97C30 + 12 stron 97D40. Zachowano tekstowo wszystkie oryginalne 629 stron i wszystkie 647 stron poprzedniego podglądu; 5 próbek renderów, 4 odsyłacze, 589 zakładek. Pierwsza strona jest graficzną okładką bez tekstu. Użyto pypdf 5.9.0.
- **Skrypt integracyjny:** [assemble_supplied_monolith.py](../scripts/assemble_supplied_monolith.py) obsługuje teraz 3 suplementy; commit [20918fb5](https://github.com/mojealterego/Ontologia-Liczby-/commit/20918fb548ed5a608ea2aece7a445a70f1e8fabd). Lokalnie sprawdzono równoważną operację pypdf; wykonania dokładnego zaktualizowanego pliku skryptu z main nie potwierdzono.
- **Protokół:** [DOWODY_MSC97D40_IIIC_2026-11-02.md](DOWODY_MSC97D40_IIIC_2026-11-02.md), commit [5aa37985](https://github.com/mojealterego/Ontologia-Liczby-/commit/5aa379851a44440eb8f9dcd4bf90e4d528e4e5db).
- **Granice:** 97D40 to poziom III z minimum **44 stron**; 12 stron oznacza **status częściowy**. Brak binarnego monolitu 0.20 (dokumentacja: 864 strony) blokuje kanoniczną integrację. **Historyczne 585 stron bez zmian**, 1222 nieobowiązkowe, limit PDF <99 000 000 B. Nie zmieniono historycznego wstępu, nie utworzono końcowego spisu treści, nie rozpoczęto Tomu II.


## MSC 97D40 — III-D, optymalizacja programu zajęć; podgląd 657 stron (2026-11-02)

- **Treść zapisana na main:** [MSC 97D40 III-D](../manuscript/tom-01/MSC97/97D40_IIID_OPTYMALIZACJA_PROGRAMU_ZAJEC.md), commit [b874688b](https://github.com/mojealterego/Ontologia-Liczby-/commit/b874688b736dc6bfccdf01b170a70c52dc7105ca). Nowe D37–D46 (10 definicji), T43–T55 (13 twierdzeń z dowodami), K23–K28 (6 kontrprzykładów), Z51–Z64 (14 rozwiązanych zadań). Nie nadpisano wcześniejszych rozdziałów.
- **Testy:** [test_msc97d40_optimization.py](../tests/test_msc97d40_optimization.py), commit [6f7d022e](https://github.com/mojealterego/Ontologia-Liczby-/commit/6f7d022e3c78565cc112291c8e612526d42db494), **8/8 lokalnie OK**; lokalny blob SHA-1 9aa7105a0782b2ec5350a3be91d2045900a0c093 jest identyczny z main. Sprawdzono exhaustive 0/1 knapsack vs brute force, minimum pokrycia, relaksację ułamkową i prawdopodobieństwa.
- **Workflow:** [tom1-msc97d40.yml](../.github/workflows/tom1-msc97d40.yml), commit [7d5ed1fe](https://github.com/mojealterego/Ontologia-Liczby-/commit/7d5ed1fed25b63dcf1798ea3ada4c27b4486b6e9), kompiluje główny manuskrypt 97D40 wraz z nową częścią III-D i uruchamia nowy plik testów. **Zielony CI po zmianie niepotwierdzony**.
- **Kompilacja lokalna:** pełny tekst nowego III-D — **4 strony A4**, 0 słów poza marginesem 5 pt; 12 wcześniejszych stron III-A–C + 4 nowe = **16 stron** roboczego rozdziału. Nie jest to jeszcze jednolita kompilacja całego HEAD Markdown.
- **Książka robocza:** z monolitu 629 stron + 6 stron 97C20 + 6 stron 97C30 + 16 stron 97D40 złożono **657 stron, 8 383 427 B**, SHA-256 `974f492e55db92b99aabc5ec1cfa3a2659c5bc1b1e62befefbf4ec9aa25a020a`. Zweryfikowano 629/629 stron tekstowo, rendery 1/2/33/34/629, 585/585 zakładek źródła, 4/4 odsyłacze. Limit PDF <99 000 000 B spełniony.
- **Protokół:** [DOWODY_MSC97D40_IIID_2026-11-02.md](DOWODY_MSC97D40_IIID_2026-11-02.md), commit [d7c07890](https://github.com/mojealterego/Ontologia-Liczby-/commit/d7c0789058774b8ba655e1823764ccbd57a4495e).
- **Nadal otwarte:** poziom III wymaga minimum 44 stron, obecnie 16; pełna recenzja matematyczna; CI; kanoniczny monolit 0.20 (864 strony, nieobecny w dostarczonym pliku). Historyczne **585 stron bez zmian**; brak końcowego spisu treści i brak Tomu II.


## MSC 97D40 — część III-E, rzetelność pomiaru (2026-11-02)

- **Nowy manuskrypt na main:** [97D40 III-E](../manuscript/tom-01/MSC97/97D40_IIIE_RZETELNOSC_POMIARU.md), commit [93faaa30](https://github.com/mojealterego/Ontologia-Liczby-/commit/93faaa30d413d9254a580aaee2dfb5b78a0f3724). Dodano D47–D56 (10 definicji), T56–T65 (10 twierdzeń z dowodami), K29–K34 (6 kontrprzykładów), Z65–Z80 (16 zadań z rozwiązaniami). Nie nadpisano wcześniejszych rozdziałów.
- **Testy:** [test_msc97d40_measurement.py](../tests/test_msc97d40_measurement.py), commit [b331e6da](https://github.com/mojealterego/Ontologia-Liczby-/commit/b331e6dad3ef9495d1277df31499b85788512deb). Lokalnie wykonano 6608 niezależnych kontroli liczbowych korelacji, progów i przeskalowania; wszystkie zaliczone. **Nie potwierdzono jeszcze wykonania pełnego unittest z repo ani zielonego GitHub Actions po zmianie.**
- **CI:** [workflow](../.github/workflows/tom1-msc97d40.yml) rozszerzony o plik III-E i testy pomiarowe, commit [66f50450](https://github.com/mojealterego/Ontologia-Liczby-/commit/66f50450f7b7ff662f2c5173aefd3ac1b88d1421). Pełna kompilacja dokładnego HEAD na GitHub Actions oczekuje na potwierdzenie.
- **Podgląd lokalny:** ReportLab wygenerował **1 stronę wybranych twierdzeń** III-E, następnie PyMuPDF dołączył ją do wcześniejszego 647-stronicowego PDF roboczego; wynik **648 stron, 8 043 200 B**, SHA-256 `90a711a7063cc4203eb56a0c2f4e4ff530f23205e1a3f404031721d9b05bc087`. Sprawdzono zgodność tekstową wszystkich 647 wcześniejszych stron oraz wizualnie nową stronę. **To podgląd wybranych twierdzeń, nie pełna kompilacja III-E, i nie jest wydaniem 0.20.**
- **Otwarte:** pełna kompilacja wszystkich części MSC 97D40, odbiór CI, minimum 44 stron poziomu III, recenzja dowodów i kanoniczna integracja z binarnym wydaniem 0.20. Historyczne **585 stron bez zmian**, 1222 nieobowiązkowe, PDF końcowy <99 000 000 B. Wstęp historyczny i poprzednie rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.


## MSC 97D40 — część III-F i odbiór CI pełnego rozdziału (2026-11-02)

- **Manuskrypt na main:** [97D40 III-F — losowanie i wnioskowanie](../manuscript/tom-01/MSC97/97D40_IIIF_LOSOWANIE_I_WNIOSKOWANIE.md), commit [b080141a](https://github.com/mojealterego/Ontologia-Liczby-/commit/b080141a30f37408934aba6eb2ca4c4526765927): D57–D66 (10 definicji), T66–T76 (11 twierdzeń z dowodami), K35–K40 (6 kontrprzykładów), Z81–Z96 (16 zadań rozwiązanych). Nie zmieniono wcześniejszych rozdziałów.
- **Testy:** [test_msc97d40_sampling.py](../tests/test_msc97d40_sampling.py), commit [e6dbd26a](https://github.com/mojealterego/Ontologia-Liczby-/commit/e6dbd26a561cbcaadc5945f1c5252187ab087a2e), **6/6 lokalnie OK**; enumeracja schematów losowania, estymatora HT i wariancji Neymana. Poprawiono tautologiczny test MSE w [test_msc97d40_measurement.py](../tests/test_msc97d40_measurement.py), commit [1c55d8dc](https://github.com/mojealterego/Ontologia-Liczby-/commit/1c55d8dc613ccb9ae863f04bbe5e3dee4a809b08).
- **CI pełnego rozdziału:** [GitHub Actions run 41474366935](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41474366935) **success**, **66/66 testów**, pełna kompilacja z czterech źródeł, 13 znaczników tekstu potwierdzonych. [Workflow](../.github/workflows/tom1-msc97d40.yml) po zmianach [083a8870](https://github.com/mojealterego/Ontologia-Liczby-/commit/083a8870588a296779dfd0a8e01313f36683682c) i [9b3cd213](https://github.com/mojealterego/Ontologia-Liczby-/commit/9b3cd21309241d0f7a93a752e4c5b091ad707565). Artefakt CI ID **13157635325**.
- **Pełny PDF MSC 97D40:** **19 stron A4, 153 890 B**, SHA-256 `8e8940ab95a178e6f0c212c3c55e5f6842ed7880fe3531dad8e4066ff5aae634`; pobrano i zweryfikowano ZIP z CI. **Nadal nieosiągnięte 44 strony** poziomu III.
- **Scalony Tom I — podgląd:** **660 stron, 8 088 173 B**, SHA-256 `1e31fa92a4f3d09d7c99fa0464198ffd405e577a5910961db9d978e532f34a44`: 629 stron dostarczonego monolitu + 6 MSC 97C20 + 6 MSC 97C30 + **19 pełnego MSC 97D40**. Kontrola: 641/641 wcześniejszych stron zgodnych tekstowo, 19/19 stron pełnego rozdziału zgodnych tekstowo, 588/588 zakładek, 4/4 odsyłacze, 0 słów poza marginesem 5 pt na nowych stronach.
- **Protokół:** [DOWODY_MSC97D40_IIIF_2026-11-02.md](DOWODY_MSC97D40_IIIF_2026-11-02.md), aneks odbiorczy commit [e118823a](https://github.com/mojealterego/Ontologia-Liczby-/commit/e118823a33bc42e7caaa53b99842686de35983a3).
- **Granice:** podgląd 660 stron nie jest kanonicznym 0.20 (według dokumentacji 864 strony; brak jego pliku binarnego). Historyczne **585 stron bez zmian**, 1222 stron nieobowiązkowe, limit PDF <99 000 000 B. Nie zmieniono wstępu historycznego, nie tworzono końcowego spisu treści ani Tomu II. Otwarte: minimum 44 stron dla MSC 97D40, recenzja formalna i integracja z prawdziwym monolitem 0.20.


## MSC 97D40 — część III-G, dobór zadań przy niepewności (2026-11-02)

- **Manuskrypt na main:** [97D40 III-G](../manuscript/tom-01/MSC97/97D40_IIIG_DOBOR_ZADAN_NIEPEWNOSC.md), commit [12acf04e](https://github.com/mojealterego/Ontologia-Liczby-/commit/12acf04e811a1015c8297da7a8ba40c795ac9799). D67–D74, T77–T84 z dowodami, K41–K44, Z97–Z108. Nie nadpisano wcześniejszych rozdziałów.
- **Testy na main:** [test_msc97d40_selection.py](../tests/test_msc97d40_selection.py), commit poprawionej stałej numerycznej [b269f156](https://github.com/mojealterego/Ontologia-Liczby-/commit/b269f156d1c99ebf6f5455a62af4787203520a45). Niezależne lokalne obliczenia: **2280/2280 kontroli** promieni ufności i granic regret OK. **Uruchomienie całego nowego pliku unittest i wynik GitHub Actions niepotwierdzone.**
- **Workflow:** [tom1-msc97d40.yml](../.github/workflows/tom1-msc97d40.yml), commit [7383b286](https://github.com/mojealterego/Ontologia-Liczby-/commit/7383b2860a599c9e41651e5fa8b798bdcc59b9cc), uwzględnia III-G w Pandoc i nowe testy. Odbiór zielonego CI wymaga osobnego potwierdzenia.
- **Lokalny podgląd:** ReportLab wygenerował **1 stronę wybranych twierdzeń III-G** (SHA-256 `5bfc557e2879703ae1c8443c044d94f6b92ee4fb5005aa050838cbfe7962a6f9`), dołączoną do istniejącego 660-stronicowego roboczego PDF; wynik **661 stron, 8 089 948 B**, SHA-256 `b45cd8b63b77495cbdf59b1da10bed903c4cfd53c526097abadd4ee15779753a`. **Nie jest to pełna kompilacja aktualnego rozdziału ani kanoniczny monolit 0.20.**
- **Otwarte:** minimum 44 stron poziomu III, pełny CI i skład aktualnego HEAD, recenzja dowodów, dostęp do rzeczywistego binarnego monolitu 0.20. Historyczne **585 stron bez zmian**, 1222 nieobowiązkowe, limit PDF <99 000 000 B. Bez zmian w historycznym wstępie, bez końcowego spisu treści, bez Tomu II.


## MSC 97D40 — część III-H, przydział zadań i sprawiedliwość (2026-11-02)

- **Wykonano i zapisano na main:** [III-H](../manuscript/tom-01/MSC97/97D40_IIIH_PRZYDZIAL_I_SPRAWIEDLIWOSC.md), commit [dcf8b86a](https://github.com/mojealterego/Ontologia-Liczby-/commit/dcf8b86a0a6406d4ccc888b34b67dc11d62f2c0a). Dodano **11 definicji (D75–D85), 12 twierdzeń z dowodami (T85–T96), 8 kontrprzykładów (K45–K52) i 20 zadań z rozwiązaniami (Z109–Z128)**. Wcześniejsze rozdziały i wstęp historyczny nie zostały zmienione.
- **Testy na main:** [test_msc97d40_matching.py](../tests/test_msc97d40_matching.py), commit [fd8c5cd7](https://github.com/mojealterego/Ontologia-Liczby-/commit/fd8c5cd7ea3c641b078aa77fc9d58144bb818eca). Lokalnie **9/9 testów III-H**, a łącznie z dostępnymi III-F i III-G **22/22**. Wyczerpująca enumeracja małych grafów i przydziałów pojemnościowych; nie jest to pełny test wszystkich plików repozytorium.
- **Workflow:** [tom1-msc97d40.yml](../.github/workflows/tom1-msc97d40.yml), commit [1b683a9f](https://github.com/mojealterego/Ontologia-Liczby-/commit/1b683a9f4c27c362f083e01fb02233db63a8228e), uruchamia nowe testy i włącza III-H do pełnej kompilacji Pandoc. **Zielony wynik nowego przebiegu GitHub Actions niepotwierdzony.**
- **Lokalne PDF:** podgląd wybranych dowodów III-H **2 strony, 59 618 B**, SHA-256 `4ed5ba8540fd57aa209de7c732a4578682a62b6f4170e90533552937f6e407f8`. Scalony podgląd roboczy Tomu I **663 strony, 8 067 235 B**, SHA-256 `0488748f4c92149b38af4766c589136d49a3ed45a13d4cec6e9b02411cf81ff1`; tekst **661/661** poprzednich stron zgodny, zachowano **589 zakładek i 4/4** odsyłacze. **To nie jest pełny skład III-H ani kanoniczny monolit 0.20.**
- **Dowody szczegółowe:** [DOWODY_MSC97D40_IIIH_2026-11-02.md](DOWODY_MSC97D40_IIIH_2026-11-02.md), commit [139b3660](https://github.com/mojealterego/Ontologia-Liczby-/commit/139b3660b89742a5555b26d6a64f94e4127e76a5).
- **Otwarte:** pełny CI i skład całego aktualnego MSC 97D40, minimum **44 stron** poziomu III, formalna recenzja matematyczna oraz dostęp do binarnego wydania **0.20**. Historyczne **585 stron bez zmian**, 1222 nieobowiązkowe, PDF końcowy <99 000 000 B. Bez końcowego spisu treści i bez Tomu II.


## MSC 97D40 — część III-I, modele opanowania i powtórek (2026-11-02)

- **Nowy pełny suplement na `main`:** [III-I](../manuscript/tom-01/MSC97/97D40_IIII_MODELE_OPANOWANIA_I_POWTOREK.md), commit [b3d95194](https://github.com/mojealterego/Ontologia-Liczby-/commit/b3d951949b8136ff352ca5afb8d901684cd6be8b). D86–D104 (19 definicji), T97–T116 (20 twierdzeń z dowodami), K53–K60 (8 kontrprzykładów), Z129–Z144 (16 rozwiązanych zadań). Zachowano wszystkie wcześniejsze rozdziały.
- **Testy:** [test_msc97d40_mastery.py](../tests/test_msc97d40_mastery.py), commit [5af2c8a8](https://github.com/mojealterego/Ontologia-Liczby-/commit/5af2c8a889805706d82b91e01605188fe96ecaab). Lokalnie **14/14 unittest OK**; porównano dokładną zawartość pliku testowego i manuskryptu z `main` za pomocą liczby znaków i FNV-1a UTF-16. **CI po zmianie niepotwierdzone**.
- **Workflow:** [tom1-msc97d40.yml](../.github/workflows/tom1-msc97d40.yml), commit [27864844](https://github.com/mojealterego/Ontologia-Liczby-/commit/2786484496e819c8ecc23278b09001e9b4d75a89), uwzględnia nowe testy i źródło III-I.
- **Pełny podgląd III-I:** **4 strony A4, 69 837 B**, SHA-256 `ae0d59c361c973f275db93c5b2175e77b4d2ef53b56d79095465ca2084033d5a`; Pandoc/XeLaTeX, tekstowe znaczniki D104/T116/K60/Z144 i kontrola marginesów wszystkich czterech stron OK. Wizualnie skontrolowano strony 1 i 4.
- **Roboczy Tom I:** **667 stron, 8 139 550 B**, SHA-256 `79aa2fa6cc5fd13e3a0950e87dde2728855672e2f36d770eb44780327c78a08f`: 663 wcześniejsze strony robocze + 4 pełne strony III-I. Kontrola: tekst **663/663** wcześniejszych stron i **4/4** nowych zgodny, **4/4** odsyłacze, **589/589** wcześniejszych zakładek zachowanych (łącznie 590). **Nie jest to pełna kompilacja aktualnego MSC 97D40 ani wydanie 0.20.**
- **Protokół dowodowy:** [DOWODY_MSC97D40_IIII_2026-11-02.md](DOWODY_MSC97D40_IIII_2026-11-02.md), commit [dcece442](https://github.com/mojealterego/Ontologia-Liczby-/commit/dcece442b43cba7fb015ae14601b7012ed6b9a2a).
- **Otwarte:** 44 strony poziomu III, pełny zielony CI na aktualnym HEAD, pełny skład wszystkich części MSC 97D40, formalna recenzja, właściwy binarny monolit 0.20 (864 strony według rejestru). Historyczne **585 stron bez zmian**; PDF końcowy <99 000 000 B; bez końcowego spisu treści i bez Tomu II.


## Suplement F13.4 — 2 listopada 2026

- Dodano `manuscript/tom-01/F13/F13.4_SUPLEMENT_SPLOT_MOMENTY.md` na `main`, commit `737f826fc348a2c32b8f6a6d2e7d752493bd3f38`.
- Materiał: 2 definicje, 4 twierdzenia z dowodami, 3 kontrprzykłady, 4 zadania rozwiązane. Splot skończony, masa, pierwszy moment, łączność i ograniczenia kontroli sumy.
- Testy automatyczne i kompilacja PDF suplementu nie zostały wykonane. Bez integracji z monolitem 0.20; bilans 585/1222 bez zmian.
- Historyczny wstęp i wcześniejszy manuskrypt bez zmian. Bez końcowego spisu treści i bez Tomu II.


### Weryfikacja F13.4 — 2 listopada 2026

- Dodano `tests/test_f134.py` na `main`, commit `2af44f3bec79c696fb9a7f00fd51adb058fa9b2d`.
- Lokalny zestaw 5 testów jednostkowych: **5/5 OK** (masa splotu, pierwszy moment, łączność, przykłady i kontrprzykłady).
- Wygenerowano lokalny **2-stronicowy podgląd kontrolny** PDF A4, 24 941 B, SHA-256 `b2c5839607080ebf120f9e20e4c13a6a5df83ebe7facc678d36a5c829a1bf7f0`. Podgląd jest redakcyjnym streszczeniem suplementu, nie pełnym składem źródła i nie jest zapisany w repozytorium.
- Nie potwierdzono CI, formalnego dowodzenia ani integracji z monolitem 0.20. Historyczny bilans 585/1222 bez zmian.


## F13.4-B — drugi moment, wielomiany tworzące i przesunięcia (2026-11-02)

- **Manuskrypt rozszerzony na main:** [F13.4](../manuscript/tom-01/F13/F13.4_SUPLEMENT_SPLOT_MOMENTY.md), commit [7adaea51](https://github.com/mojealterego/Ontologia-Liczby-/commit/7adaea51128ac2cf55ea0eaea92e68db438f7651). Dodano D3–D6, T5–T10 (dowody), K4–K6, Z5–Z9. Poprzednia treść i historyczny wstęp nietknięte. **Uwaga:** przyrost to 4 definicje, 6 twierdzeń, 3 kontrprzykłady i 5 zadań.
- **Testy:** [test_f134.py](../tests/test_f134.py) rozbudowano o drugi moment, pochodne formalne, przesunięcia i niejednoznaczność momentów, commit [6d1488fe](https://github.com/mojealterego/Ontologia-Liczby-/commit/6d1488fec5c95241174c4d205d06d9ec68289077). Lokalnie niezależna enumeracja **1521/1521** przypadków T5 OK; **pełny zestaw unittest w repo nie został w tym przebiegu wykonany**.
- **CI:** nowy [workflow F13.4](../.github/workflows/tom1-f134.yml), commit [17d7d28d](https://github.com/mojealterego/Ontologia-Liczby-/commit/17d7d28d4576273b3c6a2b07e8ddc9411aff64d2), uruchamia unittest i kompiluje pełny suplement Pandoc/XeLaTeX z kontrolą znaczników i sum SHA-256. **Zielony przebieg CI niepotwierdzony; pełny PDF nie został jeszcze pobrany ani lokalnie zweryfikowany.**
- **Otwarte:** zielony CI, odbiór pełnego PDF, formalna recenzja matematyczna, integracja z rzeczywistym binarnym monolitem 0.20. Historyczny bilans **585/1222 bez zmian**; nie tworzono końcowego spisu treści ani Tomu II.

 
## F14.4 — ułamki łańcuchowe i certyfikaty Euklidesa (2 listopada 2026)

- **Źródło na main:** [F14.4](../manuscript/tom-01/F14/F14.4_ULAMKI_LANCUCHOWE_I_CERTYFIKATY.md), commit [d8c16832](https://github.com/mojealterego/Ontologia-Liczby-/commit/d8c16832937b5ac2b7e6a0ed284b962f9695d49c). Suplement uzupełnia F14.3 bez powtarzania istniejącego dowodu własności mediantu; zawiera **6 definicji D1–D6, 9 twierdzeń T1–T9 z dowodami, 5 kontrprzykładów K1–K5 i 10 rozwiązanych zadań Z1–Z10**. Zachowano wcześniejszą treść i wstęp historyczny.
- **Testy na main:** [test_f144.py](../tests/test_f144.py), commit [43798d50](https://github.com/mojealterego/Ontologia-Liczby-/commit/43798d50ec9109a4bd970a575e7975dbd49cbfeb). Lokalnie python -m unittest -v test_f144.py: **9/9 OK**, z enumeracją dokładnych ułamków fractions.Fraction, wyznaczników unimodularnych, znaków błędów, oszacowań, wzrostu mianowników, niezmiennika NWD i przykładów. Porównanie pełnych źródeł z main: długość/FNV-1a UTF-16 manuskryptu **11269 / 806d642c**, testów **4838 / 58f50ad7**, zgodne z lokalnymi plikami.
- **Pełny podgląd PDF:** Pandoc/XeLaTeX z tego samego źródła, **5 stron A4**, **57 264 B**, SHA-256 **9a1fe35cc03f17aecbfe077cd5d5c709e931c705514e81070376e0faac843bc6**. Liczba znaków wyekstrahowanych ze stron: 1606, 2348, 1913, 2295, 1711; 0 bloków poza bezpiecznym obszarem 8 pt. Obejrzano render pierwszej i ostatniej strony. PDF jest lokalnym artefaktem, nie plikiem GitHub.
- **CI:** [workflow F14.4](../.github/workflows/tom1-f144.yml), commity [d1f283bf](https://github.com/mojealterego/Ontologia-Liczby-/commit/d1f283bf30c1d432604fc5e29251ce09918b166f) i [8e1657d7](https://github.com/mojealterego/Ontologia-Liczby-/commit/8e1657d7b43a7421aca94adb49f9522d0f205e71), uruchamia testy i buduje kompletny suplement PDF. **Zielony przebieg na HEAD wymaga osobnego potwierdzenia**; testy lokalne nie dowodzą formalnie wszystkich twierdzeń.
- **Integracja:** brak oryginalnego binarnego monolitu wydania 0.20; suplementu **nie doliczono** do historycznego bilansu **585/1222**. Nie utworzono końcowego spisu treści i nie rozpoczęto Tomu II. Docelowy PDF Tomu I pozostaje ograniczony do **<99 MB**.

- **Rozszerzenie testów F14.4:** commit [4491409a](https://github.com/mojealterego/Ontologia-Liczby-/commit/4491409a90ee4792806aa4358cd8ad0480247265) dodaje kontrolę tożsamości ogona T4 i odległości sąsiednich zbieżników T7; ponowny lokalny przebieg **9/9 OK**. Pełny PDF źródła bez zmian.

- **Diagnostyka CI F14.4:** uruchomienie [41501125500](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41501125500) zakończyło się błędem podczas XeLaTeX, mimo pozytywnych testów matematycznych. Log: brak metryki czcionki Zapf Dingbats pzdr.tfm. W commicie [f5c14828](https://github.com/mojealterego/Ontologia-Liczby-/commit/f5c1482868d86c6b62df47e949b9cd754be23b8a) do instalacji zależności CI dodano texlive-fonts-recommended. Lokalnie ponownie skompilowano pełny PDF przy ustawieniach workflow (DejaVu Serif, A4) i zweryfikowano znaczniki D1, D6, T1, T9, K1, K5, Z1, Z10. **Zielony przebieg CI po poprawce nie został jeszcze potwierdzony**.

- **Odbiór etapowy CI po poprawce:** przebieg [41501440744](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41501440744), commit f5c14828: kroki **Exact rational tests**, **Install PDF toolchain** i **Build and inspect complete F14.4 PDF** mają status success; na chwilę odczytu krok publikacji artefaktu pozostaje in_progress, a wynik całego workflow nie jest jeszcze ustalony. Nie oznaczać tego przebiegu jako zielonego przed statusem completed/success.

- **Zamknięcie CI F14.4 (potwierdzone):** [GitHub Actions run 41501440744](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41501440744) dla przypiętego SHA **f5c1482868d86c6b62df47e949b9cd754be23b8a** zakończył się **completed/success**. Wszystkie kroki (testy, instalacja, kompilacja pełnego PDF, kontrola A4 i znaczników, upload) mają status success. Artefakt **tom1-f144-full-supplement**, GitHub artifact ID **13168668005**, 64 456 B, nieprzeterminowany. To dowód poprawnego wykonania workflow dla wskazanego SHA, a nie formalnej recenzji twierdzeń ani integracji monolitu 0.20. Kolejne commity aktualizujące wyłącznie rejestr postępu nie były osobno objęte workflow ograniczonym filtrami ścieżek.

## F13.4-C — kontrola granicy momentów (2026-11-02)

- Zaktualizowano `tests/test_f134_higher.py` na `main`: commit `eef81dc9e1505192c6e5e46d8b3439567bb0493e`. Dodano test granicy znikania momentów konstrukcji dwumianowej dla n=1..8. Plik testowy jest objęty workflow `tom1-f134.yml`.
- Lokalny, szerszy zestaw kontrolny `/mnt/data/f134_work/test_f134_higher.py` uruchomiono przez `python -m unittest -v`: **4/4 OK**. Jest to oddzielny plik lokalny; nie oznacza potwierdzenia wyniku GitHub Actions.
- Poprawiono instalację czcionek TeX w workflow F13.4: commit `8b627f39187374bb482b81fffc9544d34189f666`. Zielony przebieg CI po tej poprawce i pełny PDF nadal wymagają weryfikacji.
- Historyczne 585 stron bez zmian. Brak integracji z kanonicznym monolitem 0.20; bez końcowego spisu treści i bez Tomu II.

## F13.4-D — rekonstrukcja z momentów silniowych (2026-11-02)

- Rozszerzono manuskrypt na `main`: commit `8a3bf2f69fef4a3f76e6dfe74328e70cbcc5b37c`, definicja D11, twierdzenia T17–T19 z dowodami, kontrprzykład K10, zadania Z16–Z18.
- Dodano `tests/test_f134_reconstruction.py`, commit `641c1190266e1cf6c2c21b1c32460af47813d1ee`. Lokalnie **3/3 testy OK**, w tym pełna enumeracja **3905/3905** ciągów długości 1–5, współczynniki -2..2, rekonstrukcja dokładna `fractions.Fraction`. Z testami wyższych momentów łącznie **7/7 OK**.
- Workflow F13.4 rozszerzono o test rekonstrukcji i kontrolę znaczników T19/K10/Z18: commit `d4f10a182134cb59948ce916a35d8a69954168bc`. Zielony CI i pełny PDF z aktualnego źródła **niepotwierdzone**.
- Historyczne 585 stron bez zmian. Integracja z binarnym monolitem 0.20 pozostaje otwarta; bez końcowego spisu treści i Tomu II.

## F13.4 — korekta statusu i T19 (2026-11-02)

- Commit `c7b49e4e9a240b0a302bee73ab1fcf66991db92c` precyzuje historyczny status pierwszej wersji suplementu i oddziela dokładność algebraiczną od nieudowodnionej stabilności numerycznej T19.
- Lokalny zestaw `test_f134_higher.py` + `test_f134_reconstruction.py` uruchomiony ponownie: **7/7 unittest OK**; testy lokalne są szersze niż obecne testy zapisane w repozytorium.
- **Otwarte:** pełny PDF z bieżącego manuskryptu, potwierdzony GitHub Actions `completed/success` dla aktualnego SHA, formalna recenzja matematyczna i integracja z monolitem 0.20. Bilans historyczny 585 stron bez zmian; bez Tomu II.


## F28.2-B — niegładka optymalizacja wypukła (2 listopada 2026)

- **Nowy materiał na `main`:** [F28.2-B](../manuscript/tom-01/F28/F28.2B_NIEGLADKA_OPTYMALIZACJA.md), commit [d96cafad](https://github.com/mojealterego/Ontologia-Liczby-/commit/d96cafad9348ddbf8c42cca09b86dc5fdd08d4e6). Opracowano **7 definicji, 9 twierdzeń z dowodami, 7 kontrprzykładów, 12 zadań z rozwiązaniami**. Uzupełnia istniejący F28.2, nie zastępuje wcześniejszego tekstu.
- **Testy na `main`:** [test_f282b_nonsmooth.py](../tests/test_f282b_nonsmooth.py), commit [41060641](https://github.com/mojealterego/Ontologia-Liczby-/commit/41060641dfa5c163affb2c5351cda924a8065eb6). Lokalnie **7/7 unittest OK**, dokładne `fractions.Fraction`, testy stacjonarności, stabilności, projekcji, luki optymalności i przypadków brzegowych.
- **Pełny lokalny podgląd PDF:** Pandoc/XeLaTeX, **4 strony A4**, **66 973 B**, SHA-256 `373f9feff38f091dd35b958292f66b354c830c866c4f4a299bc478a4e4e80985`. Tekst stron: 2559, 3084, 3218, 1449 znaków; 0 bloków poza marginesem 7 pt; render wszystkich stron skontrolowany. PDF nie jest binarnym monolitem 0.20 i nie jest w repo.
- **CI:** [workflow F28.2-B](../.github/workflows/tom1-f282b.yml), commit [432f7e5f](https://github.com/mojealterego/Ontologia-Liczby-/commit/432f7e5f6892e8d750a5e78e60db44a4dc6f75a2); pierwszy [run 41511707149](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41511707149) początkowo `queued`. **Nie oznaczać CI jako zielonego przed potwierdzeniem `completed/success`.**
- **Dowody i ograniczenia:** [DOWODY_F28_2B_2026-11-02.md](DOWODY_F28_2B_2026-11-02.md), commit [45fa7f17](https://github.com/mojealterego/Ontologia-Liczby-/commit/45fa7f173b56ca2ca21a960e900a2792427033e8). Brak formalnej mechanizacji i pełnego testu całego repozytorium; brak integracji z monolitem 0.20. **Historyczne 585/1222 bez zmian**; historyczny wstęp bez zmian, bez końcowego spisu treści i bez Tomu II.


### Odbiór CI i korekta A4 dla F28.2-B (2 listopada 2026)

- [GitHub Actions run 41511707149](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41511707149), przypięty commit `432f7e5f6892e8d750a5e78e60db44a4dc6f75a2`: **completed/success**. Wszystkie kroki: checkout, testy exact rational, instalacja narzędzi, kompilacja pełnego PDF, inspekcja A4 i znaczników, publikacja artefaktu — **success**. Artefakt `tom1-f282b-full-supplement`, ID `13172699887`, 67 116 B, nieprzeterminowany. To potwierdzenie procesu CI dla wskazanego SHA, nie formalny dowód twierdzeń.
- W lokalnym przeglądzie wykryto, że pierwszy podgląd (SHA `afeac05b...`) był w formacie **US Letter**, mimo omyłkowego opisu A4. Wykonano rzeczywistą ponowną kompilację z `-V papersize=a4`; nowy PDF ma **4 strony A4**, **66 973 B**, SHA-256 `373f9feff38f091dd35b958292f66b354c830c866c4f4a299bc478a4e4e80985`. Każda strona bez bloków poza marginesem 7 pt. Zaktualizowano [protokół dowodowy](DOWODY_F28_2B_2026-11-02.md), commit [860ed957](https://github.com/mojealterego/Ontologia-Liczby-/commit/860ed957edbad475909851cff9f8d61b97b9baaf).
- Monolit 0.20 nadal niedostępny; **585/1222 bez zmian**, historyczny wstęp bez zmian, bez końcowego spisu treści i bez Tomu II.


## F28.2-C — dualność wypukła i certyfikaty prymalno-dualne (2 listopada 2026)

- **Manuskrypt na main:** [F28.2-C](../manuscript/tom-01/F28/F28.2C_DUALNOSC_I_CERTYFIKATY.md), commit [da8665a6](https://github.com/mojealterego/Ontologia-Liczby-/commit/da8665a60aa95b038bb2a8b09c6221da62d98847). Osobny suplement do F28.2 i F28.2-B: **7 definicji, 9 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań**. Dotyczy dualności wypukłej, dokładnej luki, certyfikatów położenia i słabej dualności przedziałowej.
- **Testy na main:** [test_f282c_duality.py](../tests/test_f282c_duality.py), commit [e0da37e2](https://github.com/mojealterego/Ontologia-Liczby-/commit/e0da37e24618e028ecd5fcb198d89c43afdf12a9). Lokalnie **7/7 unittest OK**, 612 kombinacji parametrów, dokładne fractions.Fraction. Testy nie stanowią formalnej mechanizacji dowodów.
- **Pełny lokalny PDF:** Pandoc/XeLaTeX, **4 strony A4**, **60 466 B**, SHA-256 a6963f9796b4c91e51f0fd9ec790c77ea7b7b83140f93563c4570703dc308027. Każda strona 595,28 × 841,89 pt; liczby znaków: 1512, 2094, 2155, 2106; 0 bloków poza 6 pt; komplet D1–D7/T1–T9/K1–K6/Z1–Z12. Źródło PDF i źródło na main zgodne (9155 jednostek UTF-16, FNV-1a e974907d).
- **Workflow na main:** [tom1-f282c.yml](../.github/workflows/tom1-f282c.yml), commit [a83a6399](https://github.com/mojealterego/Ontologia-Liczby-/commit/a83a63996ef192dab572fef4cbe133418d45a6ea). [Run 41519792887](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41519792887) uruchomiony; pierwszy odczyt potwierdził sukces testów, lecz cały workflow był jeszcze in_progress. Nie oznaczać zielonego CI przed completed/success.
- **Protokół:** [DOWODY_F28_2C_2026-11-02.md](DOWODY_F28_2C_2026-11-02.md), commit [405d1954](https://github.com/mojealterego/Ontologia-Liczby-/commit/405d19546979a0f633913237b9b7b535b5c5b055).
- **Integracja:** brak oryginalnego binarnego monolitu 0.20; **585/1222 bez zmian**. Historyczny wstęp i wcześniejszy manuskrypt nietknięte. Bez końcowego spisu treści i bez Tomu II.


### Zamknięcie CI F28.2-C — potwierdzone (2 listopada 2026)

- [GitHub Actions run 41519792887](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41519792887), commit a83a63996ef192dab572fef4cbe133418d45a6ea: **completed/success**.
- Testy wymierne, instalacja zależności, kompilacja pełnego PDF, kontrola A4 i znaczników oraz publikacja artefaktu: wszystkie kroki **success**.
- Artefakt: **tom1-f282c-full-supplement**, ID **13177925067**, 60 579 B, nieprzeterminowany.
- Zaktualizowany [protokół dowodowy](DOWODY_F28_2C_2026-11-02.md), commit [9238c49d](https://github.com/mojealterego/Ontologia-Liczby-/commit/9238c49d8f85710441b1787a65dcd9752dff13a5).
- To potwierdzenie testów i składu dla wskazanego SHA, **nie** formalna mechanizacja dowodów ani integracja monolitu 0.20. Historyczne **585/1222 bez zmian**, bez finalnego spisu treści i Tomu II.


## F28.2-D — iteracje proksymalne i certyfikaty zbieżności (2 listopada 2026)

- **Manuskrypt na main:** [F28.2-D](../manuscript/tom-01/F28/F28.2D_ITERACJE_PROKSYMALNE.md), commit [ef28a8b5](https://github.com/mojealterego/Ontologia-Liczby-/commit/ef28a8b5411784187c04757839855005484be764). Osobny suplement do F28.2, F28.2-B i F28.2-C: **8 definicji, 10 twierdzeń z dowodami, 7 kontrprzykładów i 12 zadań z rozwiązaniami**. Wyniki dotyczą rozdzielnego problemu wielowymiarowego z dodatnią krzywizną diagonalną, proksymalnego progowania, kontrakcji, certyfikatu a posteriori i optymalnego kroku.
- **Testy na main:** [test_f282d_proximal.py](../tests/test_f282d_proximal.py) (commit [7dda2178](https://github.com/mojealterego/Ontologia-Liczby-/commit/7dda21787a25e70525703fdc161efd346b942e42)) i [test_f282d_certificates.py](../tests/test_f282d_certificates.py) (commit [20c05e59](https://github.com/mojealterego/Ontologia-Liczby-/commit/20c05e599599a9299f9e3c14dd964459be386d8b)). Lokalnie **14/14 unittest OK**, dokładne `fractions.Fraction`; powtórzono układ uruchomienia z katalogu nadrzędnego `tests`. Git blob SHA wszystkich trzech plików źródłowych/testowych z GitHub zgadza się z lokalnym `git hash-object`.
- **Pełny lokalny podgląd PDF:** Pandoc/XeLaTeX, **5 stron A4**, **59 310 B**, SHA-256 `3712a0791a8c4668a23bde01a518873738bff43437c901a6aab9030bec0bd477`. Kontrola PyMuPDF: **0** bloków tekstu poza obszarem 5 pt, komplet znaczników D1–D8, T1–T10, K1–K7, Z1–Z12; render stron 1 i 5 skontrolowany. Nie jest to monolit 0.20 ani binarium w repozytorium.
- **Workflow:** [tom1-f282d.yml](../.github/workflows/tom1-f282d.yml), końcowy commit konfiguracji [08c60a5a](https://github.com/mojealterego/Ontologia-Liczby-/commit/08c60a5a68315e362817d473e14d07e34167d0c3). [Run 41528949712](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41528949712) był `in_progress` przy zapisie tego wpisu; **nie oznaczać CI jako zielonego bez osobnego potwierdzenia**.
- **Protokół dowodowy:** [DOWODY_F28_2D_2026-11-02.md](DOWODY_F28_2D_2026-11-02.md), korekta formatowania commit [48dbfae3](https://github.com/mojealterego/Ontologia-Liczby-/commit/48dbfae3c16a76c05a6ebe0008b1c43882e63a82).
- **Otwarte:** niezależna recenzja matematyczna, mechanizacja dowodów, pełny lokalny zestaw testów całego repozytorium, oryginalny binarny monolit 0.20 i integracja. Historyczne **585/1222 stron bez zmian**; historyczny wstęp i wcześniejszy tekst nietknięte; bez końcowego spisu treści i bez Tomu II.


### Odbiór CI F28.2-D — potwierdzony (2 listopada 2026)

- [GitHub Actions run 41528949712](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41528949712), przypięty commit `08c60a5a68315e362817d473e14d07e34167d0c3`: **completed/success**. Wszystkie kroki, w tym **14 testów**, pełny skład PDF, kontrola A4/znaczników i publikacja artefaktu — **success**.
- Artefakt `tom1-f282d-full-supplement`, ID `13181935223`, 68 068 B, `expired=false`.
- Protokół [DOWODY_F28_2D_2026-11-02.md](DOWODY_F28_2D_2026-11-02.md) uzupełniony w commicie [165fb3ad](https://github.com/mojealterego/Ontologia-Liczby-/commit/165fb3adf7eb237980ce13f66d425a6d1397bd8f).
- Zielony CI potwierdza proces testowania i kompilacji **dla wskazanego SHA**, nie formalny dowód matematyczny. Bez monolitu 0.20 brak kanonicznej integracji; **585/1222 bez zmian**, bez końcowego spisu treści i Tomu II.


## F28.2-E — niedokładne iteracje proksymalne i certyfikaty błędu (2 listopada 2026)

- **Źródło na `main`:** [F28.2-E](../manuscript/tom-01/F28/F28.2E_NIEDOKLADNE_ITERACJE_I_CERTYFIKATY.md), commit [`93d804d4`](https://github.com/mojealterego/Ontologia-Liczby-/commit/93d804d402f8b69ef002a5dfa7982fe54b90aa6d). Osobny suplement po F28.2-D, zawierający **8 definicji, 10 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań**. Tematy: iteracje z błędem, certyfikaty residuum, ostre oszacowania błędu, zbieżność przy zanikających zaburzeniach i bezpieczne zatrzymywanie.
- **Testy na `main`:** [test_f282e_inexact.py](../tests/test_f282e_inexact.py), commit [`87a04404`](https://github.com/mojealterego/Ontologia-Liczby-/commit/87a04404d365a8d6523a7817b8b75c6c36026ee5). Lokalnie **18/18 unittest OK**, `fractions.Fraction`; Git blob SHA źródła i testów zgodne z lokalnym `git hash-object`.
- **Lokalny pełny podgląd PDF:** Pandoc/XeLaTeX, **4 strony A4, 63 440 B**, SHA-256 `f5f8fbe9ccf6c79c502af9999620fe586cdb67f59557de59430bd2933c842f48`; wszystkie znaczniki D1–D8, T1–T10, K1–K6, Z1–Z12 obecne; 0 bloków poza 6 pt. PDF nie jest binarnym monolitem 0.20 i nie jest zapisany w repozytorium.
- **CI:** [tom1-f282e.yml](../.github/workflows/tom1-f282e.yml), commit [`ac4b88fb`](https://github.com/mojealterego/Ontologia-Liczby-/commit/ac4b88fbc3ab9af797601ef5880d9a66b99fe926). [GitHub Actions run 41537770449](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41537770449) uruchomiony dla tego SHA. W ostatnim odczycie testy w CI zakończyły się sukcesem, instalacja zależności była `in_progress`. **Nie oznaczać pełnego CI jako `success` przed osobnym potwierdzeniem.**
- **Protokół dowodowy:** [DOWODY_F28_2E_2026-11-02.md](DOWODY_F28_2E_2026-11-02.md), ostatni commit redakcyjny [`509efb43`](https://github.com/mojealterego/Ontologia-Liczby-/commit/509efb439883117c4939cf5aef4e6641a254e322).
- **Otwarte:** mechanizacja dowodów, niezależna recenzja, pełny lokalny zestaw testów całego repozytorium, oryginalny monolit 0.20 i integracja. **Historyczne 585/1222 stron bez zmian.** Wstęp historyczny i wcześniejszy manuskrypt nietknięte. Bez końcowego spisu treści i bez Tomu II.


### Odbiór CI F28.2-E — potwierdzony (2 listopada 2026)

- [GitHub Actions run 41537770449](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41537770449), przypięty SHA `ac4b88fbc3ab9af797601ef5880d9a66b99fe926`: **completed/success**.
- Testy dokładne, instalacja narzędzi, pełny skład PDF, kontrola A4/znaczników i publikacja artefaktu — wszystkie kroki **success**.
- Artefakt `tom1-f282e-full-supplement`, ID `13185162442`, 63 487 B, `expired=false`.
- Protokół uzupełniony w commicie [`39aa7a92`](https://github.com/mojealterego/Ontologia-Liczby-/commit/39aa7a9225a7350295e0e3cd9490320ae3b9c15e). CI nie stanowi formalnego dowodu matematycznego. Monolit 0.20 nadal niezweryfikowany; **585/1222 bez zmian**, bez końcowego spisu treści i bez Tomu II.


### F28.2-F — Metoda gradientu (3 listopada 2026)

- Nowy plik `manuscript/tom-01/F28/F28.2F_METODA_GRADIENTU_I_CERTYFIKATY.md`, commit `03cfb738357f4e4c363e763f39f4f3c8df4c73bf`: 5 definicji, 6 twierdzeń z dowodami, 5 kontrprzykładów, 12 rozwiązanych zadań. Nie zmieniano F28.2–F28.2-E ani wstępu historycznego.
- Testy repozytoryjne `tests/test_f282f_gradient.py`, commit `0803ee95f833b05d82d828c465a72514e4ca83a4`. Lokalnie wykonano 8/8 testów na odrębnym, szerszym zestawie; testów wersji opublikowanej na GitHub jeszcze nie uruchomiono. Nie deklarować zielonego CI.
- Lokalny podgląd PDF A4: 2 strony, 64 325 B, kompilacja Pandoc/XeLaTeX. **Uwaga:** podgląd sporządzono z pełniejszego lokalnego wariantu tekstu; nie stanowi on dowodu bajtowej zgodności z krótszym plikiem opublikowanym na main. Pełny skład pliku GitHub wymaga osobnej kompilacji.
- Nie ma integracji z monolitem 0.20 ani niezależnej recenzji matematycznej. Kanoniczny licznik **585/1222** pozostaje bez zmian. Bez końcowego spisu treści i bez Tomu II.


### F28.2-G — Rzutowana metoda gradientu (3 listopada 2026)

- **Nowy manuskrypt:** [F28.2-G](../manuscript/tom-01/F28/F28.2G_RZUTOWANA_METODA_GRADIENTU.md), commit [88810356](https://github.com/mojealterego/Ontologia-Liczby-/commit/888103565aa6afe7c4d5649f4ee6205abb75f840). 7 definicji, 10 twierdzeń z dowodami, 7 kontrprzykładów, 16 rozwiązanych zadań; rzut metryczny, nierówności wariacyjne, metoda rzutowanego gradientu, tempo O(1/N), certyfikaty residuum.
- **Testy:** [test_f282g_projected_gradient.py](../tests/test_f282g_projected_gradient.py), commit [f232eeab](https://github.com/mojealterego/Ontologia-Liczby-/commit/f232eeab6a4fd3d1b0d828ae6703bb3eee593526). **Lokalnie 21/21 unittest OK**, dokładna arytmetyka Fraction; dodatkowo 8/8 lokalnych testów F28.2-F. SHA blob źródła 3985d2cc2e42a629f5a85b7f2facbfbb5f184cb0 i testów 5ff8fa151c40b9658a7529355ece5674b06cee04 potwierdzone lokalnym git hash-object.
- **Podgląd PDF:** skompilowany dokładnie ze źródła odpowiadającego SHA blob, Pandoc/XeLaTeX; **4 strony A4, 67 800 B**, SHA-256 babc55be65c81d68bc896661584a665e0132db7f6776b1d6bf310a26753045e2. pdfinfo A4, pdftotext D1–D7/T1–T10/K1–K7/Z1–Z16 kompletne, wizualna kontrola stron 1 i 4. PDF lokalny, nie monolit.
- **CI:** [tom1-f282g.yml](../.github/workflows/tom1-f282g.yml), commit [7be358d1](https://github.com/mojealterego/Ontologia-Liczby-/commit/7be358d11d75a75d22e634ea41fcd0dfec6eeccd); [uruchomienie 41547061512](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41547061512) przy pierwszej kontroli **in_progress**, nie deklarować zielonego wyniku bez odczytu.
- **Dowody:** [DOWODY_F28_2G_2026-11-03.md](DOWODY_F28_2G_2026-11-03.md), commit [fabee1ce](https://github.com/mojealterego/Ontologia-Liczby-/commit/fabee1ceb8ad79c7ed0ad01a377becd421c30199).
- **Otwarte:** pełny lokalny test suite, mechanizacja dowodów, niezależna recenzja, oryginalny monolit 0.20 i integracja. Nie zmieniano wstępu ani wcześniejszych rozdziałów. **585/1222 bez zmian**; bez końcowego spisu treści i bez Tomu II.


### Odbiór CI F28.2-G — potwierdzony (3 listopada 2026)

- [Run 41547061512](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41547061512), SHA `7be358d11d75a75d22e634ea41fcd0dfec6eeccd`: **completed/success**; wszystkie kroki testów, instalacji narzędzi, składu A4, walidacji i publikacji artefaktu zakończone `success`.
- Artefakt `tom1-f282g-full-supplement`, ID `13189805286`, 67 897 B, `expired=false`.
- Protokół dowodowy uzupełniony commitem [42b4510b](https://github.com/mojealterego/Ontologia-Liczby-/commit/42b4510bd05a7d96f4697ce2369d287a677bc3b5).
- Zielony CI nie zastępuje formalnej mechanizacji twierdzeń ani integracji z oryginalnym monolitem 0.20. **585/1222** bez zmian; bez końcowego spisu treści i Tomu II.


### F28.2-H — Projekcje naprzemienne (3 listopada 2026)

- **Rozwinięcie manuskryptu:** [F28.2H](../manuscript/tom-01/F28/F28.2H_PROJEKCJE_NAPRZEMIENNE_I_CERTYFIKATY.md), commit [b507d1a7](https://github.com/mojealterego/Ontologia-Liczby-/commit/b507d1a739d1d1b493ea41001a7c436830660ad9). 7 definicji, 10 twierdzeń z pisemnymi dowodami, 7 kontrprzykładów i 14 rozwiązanych zadań. Tematy: rzuty naprzemienne, spadek Fejéra, suma residuów, zbieżność w skończonym wymiarze, dokładne tempo dla prostych i warunek błędu.
- **Testy:** [test_f282h_alternating_projections.py](../tests/test_f282h_alternating_projections.py), commit [6a40a9b9](https://github.com/mojealterego/Ontologia-Liczby-/commit/6a40a9b9e935812d4f91ca4c885c24f8585f95e2). Lokalnie **19/19 unittest OK**, Fraction. Manuskrypt i testy odczytane ponownie z GitHub; ich SHA Git blob zgadzają się z lokalnymi git hash-object.
- **Pełny lokalny PDF:** Pandoc/XeLaTeX, **3 strony A4, 65 218 B**, SHA-256 b6618164e9471c106788d28d49a62269ca2a0b11b0efc569f646b0bdc7981f3c. Źródło PDF jest bajtowo zgodne z opublikowanym manuskryptem. Kontrola tekstu: D1–D7, T1–T10, K1–K7, Z1–Z14; bez bloków poza obszarem bezpiecznym.
- **CI:** [tom1-f282h.yml](../.github/workflows/tom1-f282h.yml), commit [28d69c4c](https://github.com/mojealterego/Ontologia-Liczby-/commit/28d69c4c9a61d08ebac66755cc7f3dd415dbf177); [run 41553387551](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41553387551) początkowo in_progress. Wymaga potwierdzenia końcowego statusu.
- **Protokół:** [DOWODY_F28_2H_2026-11-03.md](DOWODY_F28_2H_2026-11-03.md), commit [d66f78fa](https://github.com/mojealterego/Ontologia-Liczby-/commit/d66f78fabc66cde5023b912d6f95066fb078788a).
- **Otwarte:** mechanizacja dowodów, niezależna recenzja, pełny lokalny zestaw testów całego repozytorium, monolit 0.20 i integracja. Historyczne **585/1222 bez zmian**. Wstęp historyczny i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.


### Odbiór CI F28.2-H — potwierdzony (3 listopada 2026)

- [Run 41553387551](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41553387551), SHA 28d69c4c9a61d08ebac66755cc7f3dd415dbf177: **completed/success**. Testy, instalacja narzędzi, skład PDF A4, kontrola znaczników i publikacja artefaktu — wszystkie kroki success.
- Artefakt tom1-f282h-full-supplement, ID 13192823251, 65 348 B, expired=false.
- Uaktualniony [protokół F28.2-H](DOWODY_F28_2H_2026-11-03.md), commit [1a733cc8](https://github.com/mojealterego/Ontologia-Liczby-/commit/1a733cc866eb03aa0f7ccae3cae6fde619f3045d).
- Nadal otwarte: niezależna recenzja, mechanizacja dowodów, pełny lokalny test suite repozytorium i integracja z oryginalnym monolitem 0.20. **585/1222 bez zmian**. Nie modyfikowano wstępu historycznego, nie utworzono końcowego spisu treści ani Tomu II.


### F28.2-I — Projekcje naprzemienne i liniowa regularność (3 listopada 2026)

- **Manuskrypt zapisany na `main`:** `manuscript/tom-01/F28/F28.2I_PROJEKCJE_REGULARNOSC_I_CERTYFIKATY.md`, commit `b48023913da6b7fbb564eede33e5116916161445`: 6 definicji, 8 twierdzeń z pisemnymi dowodami, 6 kontrprzykładów, 12 rozwiązanych zadań. Założenia globalnej regularności i punktu początkowego w A jawnie ograniczają T5–T6.
- **Testy na `main`:** `tests/test_f282i_projections.py`, commit `eb197e61525bd8b565adb19765b74e0f299bcc6c`. **Lokalnie wykonano 4/4 testy w osobnym skrypcie kontrolnym** (projekcje przedziałowe, oszacowania wymierne, nieekspansywność w siatce). Nie potwierdzono uruchomienia testu opublikowanego na GitHub ani CI.
- **Podgląd lokalny:** `F28_2I_PODGLAD_KONTROLNY.pdf`, ReportLab, 1 strona A4, 25 272 B; poprawna kontrola rozmiaru strony i ekstrakcji tekstu. **Jest skrótem kontrolnym, nie pełnym składem manuskryptu z repo.**
- **Niezweryfikowane:** pełny suite repo, CI, formalizacja dowodów, niezależna recenzja, pełny skład z opublikowanego źródła.
- **Blokada:** brak oryginalnego monolitu 0.20 do integracji. **585/1222 bez zmian**, wstęp historyczny nietknięty, bez końcowego spisu treści i bez Tomu II.


### F28.2-J — Zbieżność projekcji w Rⁿ i perturbacje (3 listopada 2026)

- **Manuskrypt:** `manuscript/tom-01/F28/F28.2J_ZBIEZNOSC_PROJEKCJI_I_BLEDY.md`, commit pierwotny `36d558dbd7ab28c1dda5c2ecb702f26ae2c60d28`, korekta kontrprzykładu K5 `6e0283a3fe65d310facc0678e13db28317457833`. Zawiera 6 definicji, 8 twierdzeń z dowodami, 6 kontrprzykładów i 12 zadań z rozwiązaniami. Dowód zbieżności wykorzystuje skończony wymiar, domkniętość, wypukłość i niepuste przecięcie.
- **Testy na `main`:** `tests/test_f282j_convergence.py`, commit `4269fc1034d8dc68fc4cf2a28f7fc42ad5750995`. Lokalnie uruchomiono **5/5** testów pokrywających projekcje przedziałowe, nierówność pitagorejską, nieekspansywność i sumę geometryczną (plik lokalny `test_f282j.py`); ponadto **4/4** testy lokalne poprzedniego F28.2-I. Testów z pliku GitHub F28.2-J ani pełnego CI nie uruchomiono; nie deklarować zielonego CI.
- **PDF:** `/mnt/data/ONTOLOGIA_F28_2J_PODGLAD.pdf`, ReportLab, 1 strona A4, 24 669 bajtów, skontrolowany rozmiar strony przez PyMuPDF. Jest to **skrót redakcyjny**, nie pełny skład pliku źródłowego z GitHub.
- **Niezweryfikowane:** formalna mechanizacja dowodów, pełny PDF źródła repo, niezależna recenzja, pełne testy repo i GitHub Actions.
- **Blokada:** brak potwierdzonej integracji z oryginalnym monolitem 0.20. Licznik **585/1222** pozostaje bez zmian. Historyczny wstęp i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.


### F28.2-K — Projekcje z błędami sumowalnymi (3 listopada 2026)

- **Manuskrypt na `main`:** `manuscript/tom-01/F28/F28.2K_PROJEKCJE_ZABURZENIA_SUMOWALNE.md`, commit `a7b8883146ae0be318f6e0853d6866df7d8603ee`. 6 definicji, 9 twierdzeń z pisemnymi dowodami, 6 kontrprzykładów, 12 zadań z rozwiązaniami. Zachowano rozróżnienie między zbieżnością odległości (T5) a zbieżnością iteratów przy dodatkowej kontrakcji (T8).
- **Testy na `main`:** `tests/test_f282k_perturbations.py`, commit `5f359200af46470fe200d79ff497e13afcce67a8`. W osobnym lokalnym skrypcie wykonano **34/34 sprawdzeń arytmetyki dokładnej**; nie uruchomiono jeszcze opublikowanego pliku testowego ani całego CI. Nie deklarować zielonego CI.
- **Lokalny PDF:** `F28_2K_PODGLAD_KONTROLNY.pdf`, ReportLab, **1 strona A4, 2161 B**. Jest to **streszczenie kontrolne**, nie pełny skład źródła GitHub. Brak potwierdzenia kompletnego PDF.
- **Otwarte:** formalizacja dowodów, pełna kompilacja manuskryptu, pełne testy repozytorium, CI, niezależna recenzja. Brak integracji z oryginalnym monolitem 0.20; **585/1222 bez zmian**. Wstęp historyczny i poprzednie rozdziały bez ingerencji. Bez końcowego spisu treści i bez Tomu II.


### F28.2-L — Kontrakcje z zaburzeniami (3 listopada 2026)

- **Manuskrypt `main`:** `manuscript/tom-01/F28/F28.2L_KONTRAKCJE_ZABURZENIA_I_CERTYFIKATY.md`, commit `dcff7fd630a7478aef39ab7048f9166691980c06`: 6 definicji, 8 twierdzeń z dowodami, 6 kontrprzykładów i 12 rozwiązanych zadań. Udowodniono m.in. certyfikat resztowy, ostrość oszacowania i zbieżność przy zanikających zaburzeniach kontrakcji.
- **Testy `main`:** `tests/test_f282l_contractions.py`, commit `5d2951d926a3084dfcdebd5b48a70546dd0d2df5`. Lokalny skrypt o równoważnych przypadkach: **6/6 unittest OK** (Fraction). Nie uruchomiono pobranego pliku GitHub ani całego zestawu CI.
- **Podgląd PDF:** `F28_2L_PODGLAD_KONTROLNY.pdf`, ReportLab, 1 strona A4, 24 350 B; weryfikacja przez PyMuPDF. Jest to **podgląd selektywny**, nie pełny skład opublikowanego manuskryptu.
- **Otwarte:** pełny skład z repo, testy CI, niezależna recenzja, mechanizacja dowodów. Brak monolitu 0.20 do integracji; **585/1222 bez zmian**. Nie zmieniano wstępu historycznego ani wcześniejszych rozdziałów; bez końcowego spisu treści i Tomu II.


### F28.2-M — Certyfikaty a posteriori dla iteracji niedokładnych (3 listopada 2026)

- **Manuskrypt na `main`:** `manuscript/tom-01/F28/F28.2M_CERTYFIKATY_A_POSTERIORI.md`, commit `4c31db34fa3a9a1303e19ba353fe5f51a8478206`, korekta dowodu ostrości T7 commit `db046799bf3c1c7fda081323646c4227e595587a`. 6 definicji, 8 twierdzeń z dowodami, 6 kontrprzykładów, 12 zadań rozwiązanych. Dwustronny certyfikat resztowy uwzględnia certyfikowany błąd operatora δ.
- **Testy zapisane na `main`:** `tests/test_f282m_certificates.py`, commit `7bb0498fdb857bc5d2eff393f68bc8cb2c8de9ca`; testy Fraction ostrości i przykładów. **Nie uruchomiono testów**: lokalne środowiska `container.exec` i `python.exec` zwracały `ConnectionError` podczas tej sesji. Nie deklarować wyniku testów ani CI.
- **PDF:** **nie skompilowano** z powodu niedostępności środowiska wykonawczego; nie ma zweryfikowanego nowego pliku do pobrania. Wymagany ponowny przebieg testów i kompilacja pełnego źródła.
- **Otwarte:** uruchomienie testów, CI, pełny skład PDF, mechanizacja i niezależna recenzja. Brak integracji z monolitem 0.20; **585/1222 bez zmian**. Wstęp historyczny i wcześniejsze rozdziały bez ingerencji, bez końcowego spisu treści i Tomu II.


### Weryfikacja uzupełniająca F28.2-M — 3 listopada 2026

- Przywrócono działanie lokalnego środowiska Python 3.13.5. Odtworzono lokalnie treść pięciu testów odczytanych z `tests/test_f282m_certificates.py` (GitHub `main`) i wykonano `python -m unittest discover -s /mnt/data/ontologia_f282m_verified -p 'test_*.py' -v`: **5/5 OK**. Lokalna kopia testu: SHA-256 `ed5895c7b457dd1b4393a2787dca3623e017b4f56c1d3849f49bcd6e8407bc03`. Nie jest to uruchomienie CI ani test całego repozytorium.
- Utworzono **kontrolny PDF** ReportLab `/mnt/data/ontologia_f282m_verified/F28_2M_CERTYFIKATY_PODGLAD.pdf`: **1 strona A4, 25 072 B**, SHA-256 `3a46c9ef6724a631dd1f9e01c1b4143ea6b235d15ba77e635561216a99d1f9aa`. Kontrola PyMuPDF: tekst 1472 znaków, ostatni blok tekstu kończy się na y=741.2 pt przy wysokości strony 841.9 pt. **PDF zawiera wybrane wyniki, nie jest pełnym składem manuskryptu**.
- Weryfikacja manuskryptu źródłowego: ponowny odczyt F28.2-M z `main`; poprzedni tekst i wstęp historyczny bez zmian. Pozostają otwarte: pełny skład PDF z opublikowanego źródła, pełny CI, formalna i niezależna recenzja, integracja z oryginalnym monolitem 0.20. **585/1222 bez zmian**, bez końcowego spisu treści i Tomu II.


### F28.2-N — Kontrakcje ze zmienną dokładnością (3 listopada 2026)

- **Nowy suplement na `main`:** `manuscript/tom-01/F28/F28.2N_HARMONOGRAM_DOKLADNOSCI.md`, commit `f2c24baa1087dc091ddbfa4b7968518f263bfd17`. Zawiera 6 definicji, 9 twierdzeń z pisemnymi dowodami, 6 kontrprzykładów i 12 zadań z rozwiązaniami. Główne wyniki: rekurencja budżetu błędów, granice dla geometrycznego harmonogramu dokładności, przypadek rezonansowy q=s, kryteria a posteriori i zbieżność przy błędach zanikających.
- **Testy na `main`:** `tests/test_f282n_accuracy.py`, commit `1b849013457d5c854af9c7ca17b74d37a57198e4`. Lokalnie wykonano `python -m unittest discover -s /mnt/data/ontologia_f282n -p 'test_*.py' -v`: **6/6 OK**, arytmetyka dokładna `fractions.Fraction`, sprawdzanie przypadków q≠s, q=s, ostrości i przykładów. Testowano lokalną kopię kodu o tej samej treści; nie wykonano GitHub Actions ani pełnego suite.
- **PDF:** `/mnt/data/ontologia_f282n/F28_2N_PODGLAD.pdf`, ReportLab, **1 strona A4, 25 214 B**, SHA-256 `fd209b19a79de0d7ef17b4609c0a5b1f671f128c1160ea5c49a306f646757025`. Zweryfikowano format przez PyMuPDF i wyrenderowano obraz strony. Jest to **podgląd selektywny**, nie pełny skład manuskryptu z repo. Próba bezpośredniego pobrania surowego pliku przez curl nie powiodła się (DNS), odczyt repo i zapis przez connector GitHub działają.
- **Niezweryfikowane:** pełna kompilacja z kanonicznego źródła, pełny CI, niezależna recenzja, formalizacja dowodów. Brak oryginalnego monolitu 0.20 do integracji. **585/1222 bez zmian**. Historyczny wstęp i poprzednie rozdziały bez ingerencji, bez końcowego spisu treści i bez Tomu II.


### F28.2-O — Zmienne kontrakcje i certyfikaty błędu (3 listopada 2026)

- **Manuskrypt zapisany na `main`:** `manuscript/tom-01/F28/F28.2O_ZMIENNE_KONTRAKCJE.md`, commit `022760d15e73e5134a99c560bce34d799cb518f3`. Opracowano 7 definicji, 8 twierdzeń z dowodami, 7 kontrprzykładów i 14 rozwiązanych zadań. Kluczowe wyniki: propagacja błędów dla zmiennych współczynników, jawny wzór z iloczynami, certyfikat a posteriori, zbieżność przy jednostajnej kontrakcji oraz przy sumowalnych zaburzeniach i zaniku iloczynów. Zaznaczono konieczność wspólnego punktu stałego.
- **Testy zapisane na `main`:** `tests/test_f282o_variable_contractions.py`, commit `a6a8d0970425d2d3a2fa5b3c233fa6f84c753f6b`. Siedem metod unittest z arytmetyką Fraction, sprawdzających zadania Z1–Z4, Z6–Z7, ostrość i certyfikat resztowy. **Nie wykonano testów** w tej sesji; kontener wykonawczy zwrócił `redis.exceptions.ConnectionError`. Nie deklarować 7/7 OK ani zielonego CI.
- **PDF:** próba dostępu do środowiska kompilacji i instrukcji PDF przez `container.exec` zakończyła się `ConnectionError`; **brak nowego skompilowanego podglądu F28.2-O**. Należy wrócić do pełnej kompilacji i kontroli matematycznej.
- **Otwarte:** uruchomienie testów z repo, PDF, CI, formalna mechanizacja i niezależna recenzja, integracja z oryginalnym monolitem 0.20. **585/1222 bez zmian**; wstęp historyczny i wcześniejsze rozdziały bez ingerencji; bez końcowego spisu treści i Tomu II.


### F28.2-O — wykonanie testów i przygotowanie CI (3 listopada 2026)

- Odczytano z `main` manuskrypt F28.2-O oraz `tests/test_f282o_variable_contractions.py`. Odtworzono bajtowo treść testów w lokalnym pliku `test_f282o.py` i wykonano `python -m unittest discover -s /mnt/data/ontologia_f282o -p test_f282o.py -v`: **7/7 testów OK**, Python 3.13.5, Fraction. Nie jest to jeszcze wykonanie testów na runnerze GitHub.
- Dodano workflow `.github/workflows/tom1-f282o.yml`, commit `eebf81715bf096a4a6236d510f709e275ed91fb9`: uruchamia test repozytoryjny, instaluje Pandoc/XeLaTeX, kompiluje **pełny** PDF A4 ze źródła `main`, kontroluje znaczniki D1–D7/T1–T8/K1–K7/Z1–Z14, limit 99 MB i publikuje artefakt. **Status wykonania workflow niepotwierdzony**; nie deklarować zielonego CI ani pełnego PDF bez artefaktu.
- Lokalnie wygenerowano selektywny PDF kontrolny `F28_2O_PODGLAD_KONTROLNY.pdf` (ReportLab, **1 strona A4, 23 849 B**, kontrola PyMuPDF). To **nie jest** pełny skład manuskryptu.
- Pozostaje odbiór CI, weryfikacja pełnego PDF, recenzja dowodów i integracja z oryginalnym monolitem 0.20. **585/1222 bez zmian**; nie zmieniano wstępu ani wcześniejszych rozdziałów, nie utworzono końcowego spisu treści ani Tomu II.


### F28.2-P — Ruchome punkty stałe i certyfikaty śledzenia (3 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2P_RUCHOME_PUNKTY_STALE.md`, commit `2b7800c9b84033cf76bf79d1fdcf44ab550c36ac`. Osiem twierdzeń z dowodami, siedem definicji, cztery kontrprzykłady i osiem rozwiązanych zadań. Rozróżniono śledzenie ruchomego punktu stałego od zbieżności do nieruchomego celu.
- **Testy na main:** `tests/test_f282p_tracking.py`, commit `a366e00478cf1052d1730de86b07f5b5c2fc6e62`. Lokalnie wykonano **8/8 unittest OK**, Python 3.13.5, arytmetyka `fractions.Fraction`. Nie uruchomiono pełnego zestawu repo ani CI.
- **Pełny podgląd lokalny:** Pandoc/XeLaTeX z pełnego lokalnego źródła F28.2-P: `F28_2P_PELNY_PODGLAD.pdf`, **2 strony A4, 47 013 B**, SHA-256 `3cbc922a905b8bd8be13fec960363a087567b42621a55cb5e98327aef803fcb8`. Kontrola `pdfinfo` potwierdziła format i rozmiar. PDF nie jest zintegrowany z monolitem; nie jest artefaktem GitHub CI.
- **Otwarte:** niezależna recenzja, formalna mechanizacja, pełne CI i integracja z oryginalnym monolitem 0.20. **585/1222 bez zmian**. Wstęp historyczny i wcześniejsze rozdziały nietknięte, bez końcowego spisu treści i bez Tomu II.


### F28.2-Q — Obserwowalny dryf operatora (3 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2Q_OBSERWOWALNY_DRYF_OPERATORA.md`, commit `ac01b5284065102d400a2d6c3431122066a7e0ba`: 5 definicji, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Lokalny certyfikat dryfu wykorzystuje różnicę operatorów w punkcie stałym; globalny certyfikat wymaga udowodnionego supremum.
- **Testy na main:** `tests/test_f282q_operator_drift.py`, commit `03051cbe31e09b00fcbd4fe13ac244ae3371984d`. Lokalny skrypt o tych samych 7 przypadkach: `python -m unittest discover -s /mnt/data/ontologia_f282q -p 'test_*.py' -v` — **7/7 OK** (Fraction). Nie uruchomiono pobranego pliku testów ani CI.
- **PDF:** `/mnt/data/ontologia_f282q/F28_2Q_PODGLAD.pdf`, Pandoc/XeLaTeX, 1 strona A4, 34 179 B, SHA-256 `f41472e27b1e96d936c3e3364c93be7faac9cfa8d098bd56f6713c34993fa4e0`. **Podgląd wyciągu**, nie pełny skład źródła GitHub; środowisko kontenera nie mogło pobrać raw GitHub (błąd DNS).
- **Otwarte:** pełny PDF z kanonicznego manuskryptu, pełny test suite, CI, niezależna recenzja, mechanizacja dowodów oraz integracja z rzeczywistym monolitem 0.20. **585/1222 bez zmian**; historyczny wstęp i poprzednie rozdziały nietknięte, bez końcowego spisu treści i bez Tomu II.


### F28.2-R — Lokalne certyfikaty dryfu punktów stałych (3 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2R_LOKALNE_CERTYFIKATY_DRYFU.md`, commit początkowy `36883c5675233da3665060a5db6db2c98aac0095`, korekta kontrprzykładu K1 `7847d3ec979fd459e57c37998b33d62a829295cf`. 6 definicji, 7 twierdzeń z dowodami, 5 kontrprzykładów i 8 rozwiązanych zadań. T1 ogranicza dryf celu przez lokalną zmianę operatora w starym punkcie stałym; T5 wymaga jednostajnej kontrakcji.
- **Testy na main:** `tests/test_f282r_drift.py`, commit `ebb3bae1e93b6aef1d9d6b3962b49689119d1491`. Wykonano lokalny skrypt z dziewięcioma równoważnymi testami Fraction: **9/9 OK** (Python unittest). Nie uruchomiono jeszcze opublikowanego pliku z GitHub ani pełnego CI.
- **PDF:** `/mnt/data/ontologia_f282r/F28_2R_PODGLAD_KONTROLNY.pdf`, ReportLab, **1 strona A4**, SHA-256 `732314a2278c1b5f704f11ebb5c7905524be580323b4cadd56920cb3d05b65d4`. Sprawdzono w PyMuPDF i wyrenderowano stronę. **Wyciąg kontrolny, nie pełny skład kanonicznego manuskryptu**. Próba git ls-remote z kontenera nie powiodła się z powodu błędu DNS.
- **Otwarte:** niezależna recenzja dowodów, testy uruchomione bezpośrednio z repo, zielony CI, pełny skład PDF i integracja z rzeczywistym monolitem 0.20. **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały niezmienione, bez końcowego spisu treści i bez Tomu II.


### F28.2-S — Obliczalne certyfikaty dryfu (3 listopada 2026)

- **Manuskrypt zapisany na `main`:** `manuscript/tom-01/F28/F28.2S_OBLICZALNE_CERTYFIKATY_DRYFU.md`, commit `bf1d6299bca6c6644dde2bb5dd892f8dba7b4b16`. 6 definicji, 8 twierdzeń z dowodami, 5 kontrprzykładów, 10 zadań rozwiązanych. Nowy certyfikat uwzględnia resztę przybliżonego starego punktu stałego i niedokładną ewaluację operatora.
- **Testy na `main`:** `tests/test_f282s_computable_drift.py`, commit `9311730269a069aa4c7fdc9e910fd7479985fef8`. Lokalnie wykonano 9/9 testów Python unittest w pliku `/mnt/data/ontologia_s/test_f282s.py`, w tym 144 dokładne przypadki parametryczne `Fraction`. Lokalny skrypt ma równoważną logikę, lecz nie jest pobranym plikiem z GitHub. Nie zweryfikowano CI.
- **PDF:** `/mnt/data/ontologia_s/F28_2S_PELNY_PODGLAD.pdf`, Pandoc/XeLaTeX, **2 strony A4, 48 653 bajty**, SHA-256 `afedbd34ecb8128214d827ee991a5d018998bbd9a23a6deed366d6fbfc979fb4`. Powstał z **lokalnej rozszerzonej wersji redakcyjnej** F28.2-S; nie jest binarnym składem dokładnej wersji źródłowej z GitHub. `pdfinfo` potwierdził rozmiar A4.
- **Otwarte:** pełny skład kanonicznego pliku GitHub, uruchomienie testów bezpośrednio z repo, CI, niezależna recenzja i mechanizacja dowodów. Kontener nie rozwiązuje DNS `github.com`, ale connector GitHub umożliwił rzeczywisty zapis na `main`. Brak integracji z oryginalnym monolitem 0.20; **585/1222 bez zmian**. Wstęp historyczny i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.


### F28.2-T — Dwuresztowe certyfikaty dryfu (3 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2T_DWURESZTOWE_CERTYFIKATY_DRYFU.md`, commit `8a5f326ce588ba0c1cc7738257f3384e00876dbc`; korekta rachunków przykładów K3/Z9: `636fdfa0a4ef9dfa0677c30a376ebb4445e44543`. 7 definicji, 8 twierdzeń z dowodami, 6 przykładów granicznych/kontrprzykładów, 10 rozwiązanych zadań. Certyfikat łączy dwie reszty z dwiema kierunkowymi granicami lokalnego porównania operatorów.
- **Testy na main:** `tests/test_f282t_two_residual_drift.py`, commit `566dd73bd1aadd90061cc825177642d5322c0c67`. 7 metod unittest z arytmetyką dokładną Fraction, w tym rodziny parametryczne. **Nie wykonano**: lokalny Python i kontener zgłosiły `ConnectionError`; brak dowodu zielonego CI. Nie przypisywać statusu PASS.
- **PDF:** nie wygenerowano ani nie zweryfikowano: środowisko kontenera niedostępne. Pełna kompilacja i niezależna recenzja pozostają otwarte.
- **Ograniczenia:** poprzednie rozdziały i wstęp historyczny bez ingerencji; monolit 0.20 niezintegrowany; **585/1222 bez zmian**; bez końcowego spisu treści i Tomu II.


### F28.2-U — Certyfikaty kumulacji zaburzeń (3 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2U_CERTYFIKATY_KUMULACJI_ZABURZEN.md`, commit `bb27d1f5d990fde0079157720c7effcf4e6634d7`. 6 definicji, 8 twierdzeń z dowodami, 5 kontrprzykładów i 8 rozwiązanych zadań. Wcześniejsze źródła i historyczny wstęp pozostawiono nietknięte.
- **Testy na main:** `tests/test_f282u_trajectory_certificates.py`, commit `204658ae60ac6de074841fed9114108c7e993c2e`. Lokalny skrypt z równoważnymi dziewięcioma metodami `unittest` zakończył się wynikiem **9/9 OK** (Python 3.13.5, Fraction); nie wykonano jeszcze pliku pobranego z GitHub ani pełnego CI.
- **Podgląd PDF:** `/mnt/data/ontologia_u/F28_2U_PELNY_PODGLAD.pdf`, Pandoc/XeLaTeX, **2 strony A4, 54 089 bajtów**, SHA-256 `aa47f3348d5589ae5ee9a32cac38cbcf4875e10caa952610e5bc0a7f1ecbd9fd`. PDF powstał z lokalnej pełniejszej wersji redakcyjnej, nie z dokładnych bajtów manuskryptu zapisanych na GitHub; pełny kanoniczny skład pozostaje do wykonania.
- **Otwarte:** zielony CI, pełna niezależna recenzja, mechanizacja dowodów, integracja z rzeczywistym monolitem 0.20. **585/1222 bez zmian**. Nie sporządzono końcowego spisu treści ani nie rozpoczęto Tomu II.


### F28.2-V — Certyfikaty zaburzeń z opóźnioną obserwacją (3 listopada 2026)

- **Manuskrypt na `main`:** `manuscript/tom-01/F28/F28.2V_CERTYFIKATY_OPOZNIONYCH_OBSERWACJI.md`, commit `d71173e5f80d260a30511e425f00b64471552da2`. 6 definicji, 8 twierdzeń z dowodami, 5 kontrprzykładów, 10 rozwiązanych zadań. Rozszerzenie F28.2-U o pomiary opóźnione, minimum wielu certyfikatów i stabilność granic błędu.
- **Testy na `main`:** `tests/test_f282v_delayed_observations.py`, commit `f4e59aa712c77c1d13ed1eb63ab32cbef0d3b4df`, 8 metod unittest z arytmetyką `Fraction`. **Nie wykonano opublikowanego pliku testowego** — kontener nie rozwiązuje DNS `raw.githubusercontent.com`. Wykonano **2/2 lokalne testy równoważnego fragmentu**: przykłady Z2/Z6/Z8 i 48 kombinacji ostrości T8; oba OK. Nie utożsamiać tego z wynikiem ośmiu testów repo.
- **PDF:** lokalny **wyciąg kontrolny**, nie pełny skład źródła GitHub: `/mnt/data/ontologia_v/F28_2V_PODGLAD.pdf`, Pandoc/XeLaTeX, **1 strona A4, 29 956 bajtów**, SHA-256 `6c4e7c383511fd5d88d9c74c3d33a09ad3efae392ba60d01b366de7d9f342cec`.
- **Otwarte:** uruchomienie oryginalnych 8 metod testowych, pełny CI, niezależna recenzja i mechanizacja dowodów, kanoniczny pełny PDF, integracja z rzeczywistym monolitem 0.20. **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały bez ingerencji; bez końcowego spisu treści i bez Tomu II.


### F28.2-W — Certyfikaty a posteriori dla obserwacji z błędem (3 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2W_CERTYFIKATY_A_POSTERIORI.md`, commit `20975e0f239fc3ad2f128a7c34ed78bba003a45d`. Zawiera 4 definicje, 8 twierdzeń z dowodami, 5 kontrprzykładów oraz 10 zadań z rozwiązaniami. Wynik główny: dla kontrakcji q i przybliżonej obserwacji w operatora Ty z błędem η, odległość od punktu stałego jest w przedziale [max(0,r−η)/(1+q),(r+η)/(1−q)], gdzie r=d(y,w).
- **Testy na main:** `tests/test_f282w_noisy_residuals.py`, commit `85e40a5f480b310407f506e03e529ea76af45cbe`. Lokalnie wykonano 10/10 testów analogicznego pliku `/mnt/data/ontologia_w/test_f282w.py`, Python unittest/Fraction. Plik lokalny i opublikowany nie są bajtowo identyczne; testy opublikowanego pliku oraz CI nie zostały wykonane.
- **PDF:** `/mnt/data/ontologia_w/F28_2W_PODGLAD_KONTROLNY.pdf`, Pandoc/XeLaTeX, 1 strona A4, 35 741 B, SHA-256 `0d6ed9d8006b14906b8e510c218208ade4e58e9ac14fb0c5c1734d8a6f30a2ca`. **To skrócony podgląd kontrolny, nie pełny skład źródła z GitHub.** Kontener nie rozwiązuje DNS raw.githubusercontent.com.
- **Otwarte:** pełny PDF dokładnego źródła repozytorium, uruchomienie opublikowanego testu, pełne CI, niezależna recenzja matematyczna i integracja z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały bez ingerencji. **585/1222 bez zmian**, bez końcowego spisu treści i bez Tomu II.


### F28.2-X — Certyfikaty niepewności kalibracji (3 listopada 2026)

- **Manuskrypt na `main`:** `manuscript/tom-01/F28/F28.2X_CERTYFIKATY_NIEPEWNOSCI_KALIBRACJI.md`, commit `e88e58b6ddd50bf3c01e4bd94d60a7434d1afbd3`. 3 definicje, 7 twierdzeń z dowodami, 5 kontrprzykładów i 8 zadań rozwiązanych. Przedział błędu dla niepewnego współczynnika kontrakcji, wielokrotne pomiary, ostrość, stabilność kalibracji i rekurencja zaburzeń.
- **Testy zapisane na `main`:** `tests/test_f282x_calibration.py`, commit `4eb33f746466aeef41729c3dcf96fc29f0cbd1dc`, 10 metod `unittest` w arytmetyce `Fraction`. **Brak potwierdzonego uruchomienia**: lokalny kontener jest niedostępny; nie przypisywać statusu PASS ani zielonego CI.
- **PDF:** **nie skompilowano** — środowisko kontenera zwróciło błąd usługi; brak potwierdzonego podglądu. Nie należy podawać liczby stron nowego suplementu.
- **Otwarte:** wykonanie testów repozytorium, kompilacja PDF, niezależna recenzja dowodów, CI i integracja z rzeczywistym monolitem 0.20. Historyczny wstęp i poprzednie rozdziały pozostawiono bez zmian. **585/1222 bez zmian**. Bez końcowego spisu treści i bez Tomu II.


### F28.2-Y — Certyfikaty złożenia kontrakcji (3 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2Y_CERTYFIKATY_ZLOZEN_KONTRAKCJI.md`, commit `877452bc771ef5c92b94c32bf8e7db5493a8a80f`. Cztery definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i cztery zadania rozwiązane. Rozróżnia punkt stały cyklu od punktów stałych jego składników; uwzględnia ważone błędy obliczeniowe.
- **Testy na main:** `tests/test_f282y_composition.py`, commit `5e8c7bad1d5fcb5f05a2f1715e6fdf9e237e5851`. Sześć metod unittest, w tym 36 przypadków parametrycznych Fraction. Status wykonania należy potwierdzić niezależnie od samego zapisu kodu.
- **Otwarte:** integracja z rzeczywistym monolitem 0.20, pełny CI i niezależna recenzja. **585/1222 bez zmian**. Nie zmieniono historycznego wstępu, wcześniejszych rozdziałów ani nie utworzono końcowego spisu treści; bez Tomu II.

- **Weryfikacja lokalna wykonana:** odtworzono kod sześciu metod testowych w `/mnt/data/ontologia_y/test_f282y.py` i uruchomiono `python -m unittest discover -s /mnt/data/ontologia_y -p 'test_*.py' -v`: **6/6 OK**, w tym 36 przypadków parametrycznych. Nie jest to uruchomienie pliku pobranego z GitHub ani zielony CI. Lokalny podgląd kontrolny `F28_2Y_PODGLAD_KONTROLNY.pdf` (ReportLab, 1 strona A4, 24 157 bajtów, pdfinfo) zawiera wyciąg wyników, nie pełne źródło. Kontener nie rozwiązuje DNS github.com; kanoniczna kompilacja pozostaje otwarta.


### F28.2-Z — Cykliczne orbity i certyfikaty fazowe (3 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2Z_CYKLICZNE_ORBITY_FAZOWE.md`, commit `18a8b57adf9cbdc0621dd6e4132d38d2d89077bf`. Cztery definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady, sześć zadań rozwiązanych. Wynik: jednoznaczna orbita fazowa oraz ostre certyfikaty `C_i=B_i/(1-Q)` dla reszt cyklicznych.
- **Testy na main:** `tests/test_f282z_phase_orbits.py`, commit `1725b0667fdfe37027d106ff68e22e4a2a3c1f8e`. Lokalnie uruchomiono **5/5 OK** w równoważnym skrypcie `/mnt/data/ontologia_z/test_f282z.py`, w tym 400 kombinacji parametrów w arytmetyce dokładnej `Fraction`. Nie jest to uruchomienie opublikowanego pliku ani pełnego CI.
- **PDF:** lokalny wyciąg `/mnt/data/ontologia_z/F28_2Z_PODGLAD_KONTROLNY.pdf`, ReportLab, 1 strona A4, 2236 B, sprawdzony przez `pdfinfo`. Nie jest pełnym składem opublikowanego źródła.
- **Otwarte:** wykonanie opublikowanych testów, CI, pełna kompilacja kanonicznego źródła, niezależna recenzja, formalizacja oraz integracja z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały nietknięte. **585/1222 bez zmian**, bez końcowego spisu treści i bez Tomu II.


### F28.2-AA — Stabilność orbit fazowych przy perturbacji operatorów (3 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AA_STABILNOSC_ORBIT_PERTURBACJE.md`, commit `ee2b32b52f898166ef653bad31e82e2ba072574a`. Cztery definicje, siedem twierdzeń z dowodami, cztery kontrprzykłady i sześć zadań rozwiązanych. Lokalny dryf operatorów mierzony na orbicie odniesienia; ostre oszacowanie fazowe `e_i <= B_i/(1-Q)`, nie wymagające globalnej normy różnicy operatorów.
- **Testy na main:** `tests/test_f282aa_phase_perturbations.py`, commit `f15398ad1005f7026ef5e2f442020d7b62e89fec`. Lokalnie wykonano 6/6 testów równoważnego pliku w `/mnt/data/ontologia_aa/test_f282aa.py`, w tym 64 kombinacje parametrów i 28 przykładów braku jednostajnej kontrakcji; arytmetyka dokładna `Fraction`. Nie jest to wykonanie bajtowo identycznego pliku z GitHub.
- **PDF:** lokalny podgląd redakcyjny `/mnt/data/ontologia_aa/F28_2AA_PODGLAD.pdf`, Pandoc/XeLaTeX, 2 strony A4; SHA-256 `a283ebe1c3b6d74f76cdace900e2323fa41121c3987a4a155f9e850b53dbb471`. Podgląd wykonano z lokalnego, obszerniejszego opracowania; nie jest składem dokładnie opublikowanego źródła.
- **Otwarte:** testy uruchomione bezpośrednio z repozytorium, GitHub Actions, niezależna recenzja i formalizacja dowodów, kanoniczny skład, integracja z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały bez zmian. **585/1222 bez zmian**; bez końcowego spisu treści i bez Tomu II.


### F28.2-AB — Stabilność cykli przy przejściowej ekspansji (3 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AB_STABILNOSC_PRZEJSCIOWA_EKSPANSJA.md`, commit `a5a153ee41c5a61a6aea0d533336fbdfcb19149e`. Cztery definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady, sześć rozwiązanych zadań. Nowy warunek: iloczyn stałych Lipschitza pełnego cyklu Q<1, mimo dopuszczalnej ekspansji pojedynczych faz.
- **Testy na main:** `tests/test_f282ab_transient_expansion.py`, commit `8bbf4723703766459b65a329cfff90fa68b517e0`. Lokalnie wykonano **6/6** testów równoważnego pliku `/mnt/data/ontologia_ab/test_f282ab.py` w arytmetyce dokładnej Fraction; nie wykonano bajtowo identycznego pliku pobranego z GitHub ani pełnego CI.
- **PDF lokalny:** `/mnt/data/ontologia_ab/F28_2AB.pdf`, Pandoc/XeLaTeX, **2 strony A4, 55 712 B**, SHA-256 `504c28354a07aca127f8435026d77d9be74f5e521fb3e523df5abfe12c8a335d`. Powstał z lokalnej pełniejszej redakcji, nie z bajtowo identycznego źródła repo.
- **Otwarte:** niezależna recenzja, uruchomienie opublikowanego testu, GitHub Actions, kanoniczna kompilacja i integracja z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały nietknięte. **585/1222 bez zmian**, bez końcowego spisu treści i bez Tomu II.


### F28.2-AC — Certyfikaty fazowe z reszt pomiarowych (3 listopada 2026)

- Źródło: `manuscript/tom-01/F28/F28.2AC_CERTYFIKATY_FAZOWE_Z_RESZT_POMIAROWYCH.md`, commit `16c4b395409132f0a83bf816e46fc3a37a01d9f7`; 4 definicje, 6 twierdzeń z dowodami, 5 kontrprzykładów i 8 rozwiązanych zadań.
- Testy: `tests/test_f282ac_phase_residuals.py`, commit `677ca9d58ba723f6fe4e8e5299e61e7318be36a7`; sześć metod unittest, w tym 25 przypadków parametrycznych w arytmetyce Fraction. Sam zapis testów nie oznacza ich wykonania.
- Kluczowy warunek: iloczyn stałych Lipschitza całego cyklu Q<1; certyfikat fazowy B_i/(1−Q) uwzględnia niepewność obserwacji.
- Brak integracji z rzeczywistym monolitem 0.20; licznik **585/1222 bez zmian**. Wstęp historyczny i wcześniejsze rozdziały niezmienione; nie tworzono końcowego spisu treści ani Tomu II.


### F28.2-AD — Certyfikaty przedziałowe i optymalizacja budżetu (3 listopada 2026)

- **Źródło na main:** `manuscript/tom-01/F28/F28.2AD_CERTYFIKATY_PRZEDZIALOWE_OPTYMALIZACJA.md`, commit `62eb0504e40691fadeb900101e4b3b0f064a0211`. Cztery definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady, sześć rozwiązanych zadań. Kontynuacja F28.2-AC: reszty przedziałowe, dolne nierówności między fazami, monotoniczność certyfikatu, optymalny przydział ograniczonego budżetu redukcji reszt oraz ostrość.
- **Testy na main:** `tests/test_f282ad_interval_budget.py`, commit `df9fecdba09cbf05715ca228eacf528436ccbe9b`, pięć metod unittest z arytmetyką `Fraction`. **Lokalnie wykonano 5/5 OK** na skrypcie o analogicznej treści `/mnt/data/ontologia_ad/test_f282ad.py`, w tym 64 pary parametrów; nie jest to uruchomienie bajtowo identycznego pliku pobranego z repozytorium. Polecenie repo: `python -m unittest discover -s tests -p 'test_f282ad_interval_budget.py' -v`.
- **PDF:** lokalny wyciąg kontrolny `/mnt/data/ontologia_ad/F28_2AD_PODGLAD_KONTROLNY.pdf` (ReportLab), 1 strona A4, 24 493 bajty, parametry sprawdzone przez `pdfinfo`. **Nie jest to pełny skład opublikowanego źródła**.
- **Niezweryfikowane:** pełne CI, mechaniczna formalizacja dowodów, niezależna recenzja, wykonanie testów bezpośrednio z checkout repozytorium, kanoniczny pełny PDF.
- **Integracja:** nie scalono z rzeczywistym monolitem 0.20. Wstęp historyczny i wcześniejsze rozdziały nie były zmieniane. **585/1222 bez zmian**, bez końcowego spisu treści i bez Tomu II.


### F28.2-AE — Minimax jednoczesnej kontroli wielu faz (3 listopada 2026)

- **Źródło na main:** `manuscript/tom-01/F28/F28.2AE_MINIMAKS_WIELU_FAZ.md`, commit `81b35236a6ca24e3561f544d130f63082270793c`. Cztery definicje, siedem twierdzeń z dowodami, cztery kontrprzykłady i sześć zadań rozwiązanych. Rozszerzenie F28.2-AD z pojedynczej fazy na minimaks wielu faz, równoważność programowi liniowemu, wypukłość wartości budżetowej, wymianę przy dominacji i dolne oszacowanie przez mieszankę faz.
- **Testy na main:** `tests/test_f282ae_minimax.py`, commit `7dd406721779466e789df627a015c0d0a0eebe52`; siedem metod `unittest` w arytmetyce dokładnej `Fraction`. Sam zapis nie stanowi potwierdzenia wykonania ani CI.
- **Granice:** nie przeprowadzono integracji z rzeczywistym monolitem 0.20 ani niezależnej recenzji matematycznej. Wstęp historyczny i wcześniejsze rozdziały nie były edytowane. Bilans **585/1222** bez zmian; nie tworzyć końcowego spisu treści ani Tomu II.


### F28.2-AF — Dualne certyfikaty optymalności minimaksowej (3 listopada 2026)

- **Manuskrypt:** `manuscript/tom-01/F28/F28.2AF_DUALNE_CERTYFIKATY_MINIMAKSU.md`, commit `0147beafc4c0a9f66f4b8fd6d21d9ea5ca2f5a20`. Trzy definicje, pięć twierdzeń z dowodami (w tym silna dualność oparta na klasycznym twierdzeniu LP), cztery kontrprzykłady i sześć zadań z rozwiązaniami.
- **Testy na main:** `tests/test_f282af_dual_minimax.py`, commit `7792bb2884a30d1706d4cab0c2701724ce75e410`; sześć metod `unittest` w arytmetyce dokładnej `Fraction`. **Nie wykonano pobranego pliku testowego:** kontener nie rozwiązuje DNS raw.githubusercontent.com. Lokalnie sprawdzono osobno pięć wartości symetrycznego przykładu wymiernego (5/5); nie jest to wynik 6/6 opublikowanych testów.
- **PDF:** lokalny skrócony podgląd kontrolny `/mnt/data/ontologia_af/F28_2AF_PODGLAD_KONTROLNY.pdf`, ReportLab, jedna strona A4; nie jest pełnym składem źródła GitHub.
- **Otwarte:** pełna kompilacja opublikowanego manuskryptu, uruchomienie wszystkich testów repozytorium i CI, niezależna recenzja dowodów, integracja z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały nie były edytowane. **585/1222 bez zmian**. Bez finalnego spisu treści i bez Tomu II.


### F28.2-AG — Wrażliwość minimaksu na budżet (4 listopada 2026)

- Manuskrypt: `manuscript/tom-01/F28/F28.2AG_WRAZLIWOSC_BUDZETU.md`, commit `88a25455f7a437aa4c7caa0a5bf5a12b75e0301e`; 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Wyniki: monotoniczność, wypukłość, odcinkowa afiniczność, dualne proste wspierające, oszacowanie Lipschitza.
- Testy: `tests/test_f282ag_budget_sensitivity.py`, commit `362246d8e61a134ec4a361d02e04656c095067e6`; 5 metod `unittest` w arytmetyce `Fraction`. Nie przypisywać statusu PASS bez wykonania opublikowanego pliku.
- Bez zmian w poprzednich rozdziałach i wstępie historycznym. Nie scalono z monolitem 0.20. Bilans **585/1222** bez zmian. Nie utworzono końcowego spisu treści ani Tomu II.


### F28.2-AH — Odporny minimaks scenariuszowy (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AH_ODPORNY_MINIMAKS_SCENARIUSZE.md`, commit `a29ad1c6bb65fc9e1207e5dc0728852903239aa5`. Trzy definicje, sześć twierdzeń z dowodami, pięć kontrprzykładów, osiem zadań rozwiązanych. Skończone scenariusze, dokładna linearyzacja LP, rozróżnienie decyzji odpornej i adaptacyjnej, granica Lipschitza, dualny certyfikat mieszanki scenariuszy.
- **Testy na main:** `tests/test_f282ah_robust_scenarios.py`, commit `105577a48ab6755ef7391fed17c6a74f85b225ff`. Lokalny skrypt o tej samej treści logicznej uruchomiono: `python -m unittest discover -s /mnt/data/ontologia_ah -p 'test_*.py' -v`, **8/8 OK**. Sprawdzono m.in. 121 par wypukłości i 231 par nierówności Lipschitza w arytmetyce `Fraction`. **Nie wykonano bezpośrednio pobranego pliku repozytorium ani pełnego CI.**
- **PDF:** lokalny wyciąg kontrolny `/mnt/data/ontologia_ah/F28_2AH_PODGLAD.pdf`, Pandoc/XeLaTeX, **1 strona A4**, **40 362 B**, SHA-256 `105fe72aabbd56d03da6b1275376b167d21c7e6b9bdb63b697eb17a353ac9660`. **To nie pełny skład opublikowanego źródła**.
- **Granice:** nie wykonano niezależnej recenzji wszystkich dowodów, formalizacji w asystencie dowodowym, GitHub Actions ani integracji z rzeczywistym monolitem 0.20. Kontener nie rozwiązuje DNS github.com; dostęp do źródeł uzyskano przez autoryzowany konektor GitHub. Wstęp historyczny i wcześniejsze rozdziały nie zostały edytowane.
- **Bilans:** **585/1222 bez zmian** do czasu scalania i rzeczywistej paginacji monolitu 0.20. Nie utworzono końcowego spisu treści ani Tomu II.


### F28.2-AI — Ryzyko ogonowe i CVaR (4 listopada 2026)

- **Źródło na main:** `manuscript/tom-01/F28/F28.2AI_SCENARIUSZE_LOSOWE_CVAR.md`, commit `6d455cc5aa5bb54140464eeb97eb9e9f70d7f2a9`. Trzy definicje (VaR, CVaR, kontrola ryzyka), pięć twierdzeń z dowodami, cztery kontrprzykłady, osiem zadań rozwiązanych. Wyniki obejmują dokładną linearyzację CVaR, dualną otoczkę prawdopodobieństw, granicę najgorszego przypadku, wypukłość budżetową i stabilność względem błędów scenariuszy.
- **Testy na main:** `tests/test_f282ai_cvar.py`, commit `3ddc260c828518b38557974cc81fa76b1fc75c0d`. Osiem metod unittest z arytmetyką `Fraction`; ich opublikowany plik nie został jeszcze wykonany z checkout GitHub. Osobny lokalny skrypt sprawdzający osiem analogicznych własności dał **8/8 OK**, co nie jest formalną weryfikacją dowodów ani wynikiem CI.
- **Status:** brak integracji z rzeczywistym monolitem 0.20, pełnej kompilacji kanonicznej i niezależnej recenzji. Historyczny wstęp i wcześniejsze rozdziały pozostawiono bez zmian. **585/1222 bez zmian**. Bez końcowego spisu treści i bez Tomu II.


### F28.2-AJ — Odporność CVaR na błędy rozkładu (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AJ_ODPORNOSC_CVAR_ROZKLADY.md`, commit `9e75ce59092c4418ce4a2f8e3dd52d585947261d`. Cztery definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Nowe wyniki: oszacowanie TV z czynnikiem `1/(1-alpha)`, jego ostrość, certyfikat dla kuli niepewności rozkładu i stabilność łączna.
- **Testy na main:** `tests/test_f282aj_cvar_distribution.py`, commit `5d58c3894e6b37e3a7fe58d027a6ec901059fccc`. Siedem metod `unittest`, arytmetyka dokładna `Fraction`. **Nie potwierdzono wykonania testów:** środowisko kontenera zwróciło błąd usługi. Brak podstaw do deklaracji PASS i zielonego CI.
- **PDF:** nie skompilowano z powodu błędu usługi kontenera. Kanoniczny podgląd i niezależna recenzja pozostają otwarte.
- **Ograniczenia:** wcześniejsze rozdziały i historyczny wstęp nieedytowane; brak integracji z rzeczywistym monolitem 0.20; **585/1222 bez zmian**; bez końcowego spisu treści i bez Tomu II.


### F28.2-AK — CVaR i certyfikaty transportowe (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AK_CVAR_TRANSPORT_CERTYFIKATY.md`, commit `f2a3c645885e551ee219d7d0e946235d8f466198`. Cztery definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Rozwinięto F28.2-AJ o odległość transportową Wassersteina-1, certyfikat błędu CVaR, ostrość współczynnika i wypukłość ryzyka decyzyjnego.
- **Testy zapisane na main:** `tests/test_f282ak_transport_cvar.py`, commit `97c6e2d812b9e6e41a4159de5e1d3b9aa547b01e`; sześć metod `unittest` opartych na `Fraction`. **Nie wykonano bajtowo identycznego pliku repozytorium**: lokalny kontener nie rozwiązuje DNS `raw.githubusercontent.com`. Lokalnie wykonano 5/5 testów analogicznego skryptu `/mnt/data/ontologia_ak/test_local.py`, w tym 324 porównania transportowe, wszystkie OK. Nie oznaczać opublikowanych testów ani CI jako PASS.
- **PDF:** `/mnt/data/ontologia_ak/F28_2AK_PODGLAD.pdf`; Pandoc/XeLaTeX, 1 strona A4, SHA-256 `fff521ea9977ab8ca2fdd3e48fc24ba857e7333529900943c9a8002cc6e4e535`. To wyciąg kontrolny, **nie** kompilacja pełnego manuskryptu pobranego z GitHub.
- **Otwarte:** wykonanie dokładnie opublikowanych testów, GitHub Actions, niezależna recenzja wszystkich dowodów, kanoniczna kompilacja pełnego źródła, integracja z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały bez ingerencji. **585/1222 bez zmian**. Bez końcowego spisu treści i bez Tomu II.


### F28.2-AL — Dokładna odporna CVaR na dwóch scenariuszach (4 listopada 2026)

- **Źródło na main:** `manuscript/tom-01/F28/F28.2AL_DOKLADNA_ODPORNA_CVAR_DWA_SCENARIUSZE.md`; commit `f2a75b8a994903e461f4b358450794614cd1fee9`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Zamknięta formuła odpornego CVaR dla dokładnie dwóch scenariuszy, promień nasycenia i ostrość transportowego współczynnika.
- **Testy na main:** `tests/test_f282al_exact_two_scenario_cvar.py`; commit `98c48381124f0cf3dc159f4adcc97af67db47ca6`. Osiem metod `unittest` w arytmetyce `Fraction`. Lokalny skrypt z tymi samymi ośmioma przypadkami testowymi zakończył się **8/8 OK**; nie wykonano jeszcze bajtowo identycznego pliku pobranego z repozytorium.
- **Podgląd lokalny:** `/mnt/data/ontologia_al/F28_2AL.pdf`, Pandoc/XeLaTeX, 2 strony A4, kompilacja poprawna. Jest to pełniejsza lokalna redakcja, **nie** kompilacja bajtowo identycznego źródła opublikowanego na GitHub. Weryfikacja typograficzna wymaga ponownego składu z opublikowanego pliku.
- **Niezweryfikowane:** pełne CI, niezależna recenzja dowodów, wykonanie testów dokładnie z checkout, kanoniczna kompilacja i integracja z rzeczywistym monolitem 0.20.
- **Bilans:** **585/1222 bez zmian**; wcześniejsze rozdziały i wstęp historyczny nieedytowane. Bez końcowego spisu treści i bez Tomu II.


### F28.2-AM — Przedziałowa niepewność masy i odwrotne certyfikaty CVaR (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AM_PRZEDZIALOWA_NIEPEWNOSC_CVAR.md`, commit `09e3bac54acb9eb5c14a80a190cbbdf540869543`. Cztery definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Przedziałowa otoczka transportowa, dokładne krańce CVaR, odwrotny promień osiągnięcia progu, promień bezpieczeństwa oraz oszacowanie Lipschitza.
- **Testy zapisane na main:** `tests/test_f282am_interval_transport_cvar.py`, commit `5ccf7fd420079768fb135d4a05262f2007b6c5b8`; sześć metod `unittest`, dokładna arytmetyka `Fraction`. **Nie wykonano testów:** kontener i Python zwracają błąd usługi. Brak podstaw do statusu PASS i do deklaracji zielonego CI.
- **PDF:** nie skompilowano, ponieważ kontener/Python są niedostępne (błąd usługi). Pełny skład i niezależna recenzja matematyczna pozostają otwarte.
- **Integracja:** bez rzeczywistego monolitu 0.20; **585/1222 bez zmian**. Wstęp historyczny i wcześniejsze rozdziały nieedytowane. Bez końcowego spisu treści i bez Tomu II.


### F28.2-AN — Certyfikaty progowe CVaR przy przedziałowej niepewności masy (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AN_CERTYFIKATY_PROGOWE_CVAR.md`, commit `7d28acedcfdf220b07504c047e299a90ddaf59d6`. Cztery definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady, sześć rozwiązanych zadań. Dokładna otoczka mas, warunek bezpieczeństwa progu i najmniejszy promień osiągnięcia.
- **Testy na main:** `tests/test_f282an_thresholds.py`, commit `2d04f0a0130d4ddf1b7dbf5fb86153179b1eb4c1`. Siedem metod unittest w arytmetyce Fraction; **lokalnie uruchomiono 7/7 OK na analogicznym pliku**, obejmującym 255 punktów kontrolnych granic (15 przedziałów × 17 punktów). Nie jest to wykonanie pobranego z GitHub pliku ani pełnego CI.
- **PDF lokalny:** `/mnt/data/ontologia_an/F28_2AN_PODGLAD.pdf`, Pandoc/XeLaTeX, 2 strony A4; skompilowany z lokalnej redakcji o tym samym zakresie matematycznym, ale nie z bajtowo identycznego pliku opublikowanego na GitHub.
- **Otwarte:** niezależna recenzja, kanoniczna kompilacja opublikowanego źródła, pełny GitHub Actions, integracja z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały nie były edytowane. **585/1222 bez zmian**; bez końcowego spisu treści i bez Tomu II.


### F28.2-AO — Ścisłe przekroczenie CVaR i margines bezpieczeństwa (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AO_SCISLE_PRZEKROCZENIE_CVAR.md`, commit `ea75b45ccd7c6c7e7e4692a5e25a6bbc9c492810`. Cztery definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady, sześć rozwiązanych zadań. Rozróżniono osiągnięcie progu `C=τ` i ścisłe przekroczenie `C>τ`, otwarty brzeg zbioru promieni naruszenia, ciągły margines bezpieczeństwa i certyfikaty błędu numerycznego.
- **Testy na main:** `tests/test_f282ao_strict_cvar.py`, commit `fb969ab2f872f3a8364293cdf5cd70b465d82572`. Osiem metod `unittest` opartych na dokładnej arytmetyce `Fraction`. **Lokalnie przed publikacją uruchomiono odpowiadający logicznie plik: 8/8 OK**; brak potwierdzenia uruchomienia bajtowo identycznego pliku z checkout GitHub i brak potwierdzenia GitHub Actions.
- **Podgląd:** lokalny `/mnt/data/ontologia_ao/F28_2AO_PODGLAD.pdf`, Pandoc/XeLaTeX, 2 strony A4. PDF jest kompilacją lokalnej wersji redakcyjnej, **nie** opublikowanego bajtowo identycznego źródła.
- **Otwarte:** niezależna recenzja wszystkich dowodów, kanoniczna kompilacja opublikowanego manuskryptu, pełny CI i integracja z rzeczywistym monolitem 0.20. Wstęp historyczny i wcześniejsze rozdziały nieedytowane. **585/1222 bez zmian**. Bez finalnego spisu treści i bez Tomu II.


### F28.2-AP — Wrażliwość CVaR na poziom ufności (4 listopada 2026)

- **Źródło na main:** `manuscript/tom-01/F28/F28.2AP_WRAZLIWOSC_CVAR_POZIOM_UFNOSCI.md`, commit `2d1a790ee8c77cb40fbc136daa1bf2f50da6df47`. Cztery definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Profil R(α), punkt nasycenia, dokładny zbiór dopuszczalnych poziomów, stabilność wspólna masy i poziomu ufności.
- **Testy na main:** `tests/test_f282ap_confidence_cvar.py`, commit `83f289ea6f9fe88483abd8114a0b2e97078cf2b0`. Sześć metod unittest w arytmetyce dokładnej Fraction. **Lokalnie wykonano 6/6 OK** na pliku o tej samej treści logicznej; nie wykonano bajtowo identycznego pliku pobranego z repozytorium ani GitHub Actions.
- **Podgląd:** lokalny `/mnt/data/ontologia_ap/F28_2AP_PODGLAD.pdf`, Pandoc/XeLaTeX, 2 strony A4. PDF z pełniejszej lokalnej redakcji, **nie** z bajtowo identycznego pliku opublikowanego na GitHub.
- **Niezweryfikowane:** niezależna recenzja wszystkich dowodów, pełny CI, kanoniczna kompilacja opublikowanego źródła i integracja z rzeczywistym monolitem 0.20. Wstęp historyczny i wcześniejsze rozdziały nieedytowane. **585/1222 bez zmian**; bez końcowego spisu treści i bez Tomu II.


### F28.2-AQ — Kwantyle krytyczne i odwrotna kalibracja CVaR (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AQ_ODWROTNA_KALIBRACJA_CVAR.md`, commit `0cbe67c3290eb36e993baa543353176afc58205b`. Trzy definicje, pięć twierdzeń z dowodami, cztery kontrprzykłady, sześć zadań rozwiązanych. Klasyfikacja profilu, dokładny zbiór bezpiecznych poziomów, odwrotna kalibracja masy, stabilność i próg minimalny.
- **Testy na main:** `tests/test_f282aq_inverse_cvar.py`, commit `4309b9e8e8d8185ccd2d1b5ea7d6e8af044c1664`, sześć metod `unittest`. Lokalnie wykonano **1100** dokładnych porównań wymiernych w oddzielnym skrypcie `/mnt/data/ontologia_aq/check.py` — PASS. **Nie jest to wykonanie bajtowo identycznego pliku repozytorium ani pełnego CI.**
- **PDF:** lokalny kontrolny wyciąg `/mnt/data/ontologia_aq/F28_2AQ_PODGLAD.pdf`, Pandoc/XeLaTeX, 1 strona A4; nie jest kanonicznym składem pełnego opublikowanego źródła.
- **Niezweryfikowane:** uruchomienie opublikowanych sześciu testów z checkout, GitHub Actions, niezależna recenzja dowodów, kanoniczny skład i integracja z monolitem 0.20.
- **Bilans:** **585/1222 bez zmian** do integracji z rzeczywistym monolitem 0.20; historyczny wstęp i wcześniejsze rozdziały nieedytowane; bez finalnego spisu treści i bez Tomu II.


### F28.2-AR — Dokładna CVaR dla trzech scenariuszy (4 listopada 2026)

- **Źródło na main:** `manuscript/tom-01/F28/F28.2AR_CVAR_TRZY_SCENARIUSZE.md`, commit `1ed461d98480755523f735d05faba1187556640b`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć zadań z rozwiązaniami. Wyprowadzono dokładną trzygałęziową formułę ogona dla trzech uporządkowanych strat, monotoniczność, certyfikat progu oraz stabilność względem perturbacji strat.
- **Testy zapisane na main:** `tests/test_f282ar_three_scenario_cvar.py`, commit `e15848207f01284e7dd6f615be0b69e89e3b6060`, pięć metod `unittest` w arytmetyce `Fraction`. **Nie uruchomiono bajtowo identycznego pliku z repozytorium**: lokalne pobranie `raw.githubusercontent.com` zakończyło się błędem DNS. Lokalnie uruchomiono oddzielny skrypt `/mnt/data/check_ar.py`: **3/3 grupy OK**, w tym 900 porównań wzoru zamkniętego i algorytmu ogonowego. Wynik lokalny nie jest wynikiem testów repozytorium ani GitHub Actions.
- **PDF kontrolny:** lokalny `/mnt/data/F28_2AR_PODGLAD.pdf`, Pandoc/XeLaTeX, **1 strona A4**. Jest to wyciąg, nie pełna kompilacja kanonicznego źródła opublikowanego na GitHub.
- **Niezweryfikowane:** opublikowany test uruchomiony z checkout, pełne CI, niezależna recenzja dowodów, pełny skład źródła oraz integracja z rzeczywistym monolitem 0.20.
- **Bilans:** **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały nie były edytowane; bez końcowego spisu treści i bez Tomu II.


### F28.2-AS — CVaR dla n scenariuszy: porządkowanie i remisy (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AS_CVAR_N_SCENARIUSZY.md`, commit `4710f988ceb67ffd1bb8c28b3596ea6e9385e33e`. Cztery definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć zadań rozwiązanych. Uogólniono F28.2-AR na skończone n, remisy strat i masy zerowe; podano certyfikat progowy i złożoność algorytmu.
- **Testy na main:** `tests/test_f282as_n_scenario_cvar.py`, commit `f0f49b741cfdfbf5ddc4b8f2f8a57e6635870bf0`. Sześć metod unittest; arytmetyka Fraction, enumeracja scenariuszy, porównanie zachłannej reprezentacji z minimalizacją primal. **Lokalnie uruchomiono oddzielny logicznie równoważny skrypt**: 6/6 OK. **Nie uruchomiono bajtowo identycznego pliku pobranego z GitHub; CI niezweryfikowane.**
- **Podgląd lokalny:** `/mnt/data/ontologia_as/F28_2AS_PODGLAD.pdf`, ReportLab, 1 strona A4, 24 136 B. Jest to wyciąg kontrolny, **nie pełny skład kanonicznego źródła**.
- **Otwarte:** uruchomienie dokładnego testu z checkout, GitHub Actions, niezależna recenzja wszystkich dowodów, pełny skład i integracja z rzeczywistym monolitem 0.20.
- **Bilans:** **585/1222 bez zmian**. Wstęp historyczny i wcześniejsze rozdziały nieedytowane; bez końcowego spisu treści i bez Tomu II.


### F28.2-AT — Dokładna odporność CVaR na przedziałowe błędy strat (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AT_ODPORNOSC_PRZEDZIALOWA_STRAT.md`, commit `74fb982d7f4dee5c40d74b892e073d85760454e9`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Dokładne ekstrema CVaR w prostokątnym zbiorze niepewności strat, certyfikat progowy, stabilność w normie maksimum i ważonej normie L1, niezmienniczość remisów.
- **Testy na main:** `tests/test_f282at_interval_loss_cvar.py`, commit `98e9e244dec466502a216d32145c5b27fab81a17`, sześć metod unittest opartych na Fraction. Lokalnie uruchomiono **6/6 OK na oddzielnym logicznie równoważnym skrypcie** `/mnt/data/ontologia_at/test.py`, w tym 225 skończonych przypadków monotoniczności. **Nie jest to wykonanie bajtowo identycznego testu opublikowanego na GitHub ani wynik GitHub Actions.**
- **Podgląd lokalny:** `/mnt/data/ontologia_at/F28_2AT_PODGLAD.pdf`, ReportLab, 1 strona A4, 24 871 bajtów, SHA-256 `eb53a6a1361977ea8e7e1f95701986a944d46b0f22054dc213ac478e7a6705a1`. Wyciąg kontrolny, nie kanoniczna kompilacja pełnego opublikowanego manuskryptu.
- **Niezweryfikowane:** niezależna recenzja wszystkich dowodów, uruchomienie opublikowanego testu z checkout, pełny GitHub Actions, kanoniczny skład całego źródła i integracja z rzeczywistym monolitem 0.20.
- **Bilans:** **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały nieedytowane; bez końcowego spisu treści i bez Tomu II.


### F28.2-AU — Spójność CVaR i granice addytywności (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AU_SPOJNOSC_CVAR.md`, commit `3b6726ce9d3dab1471d89616704211cdcd4dabf3`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć zadań rozwiązanych. Wykazano reprezentację dualną, monotoniczność, translację, dodatnią jednorodność, subaddytywność, warunek równości i stabilność.
- **Testy na main:** `tests/test_f282au_coherence_cvar.py`, commit `4f04474901cf34ec3e5da519e1ce7165b581f2d5`. Sześć metod unittest w arytmetyce Fraction. **Lokalnie uruchomiono oddzielny logicznie równoważny skrypt:** `python -m unittest discover -s /mnt/data/ontologia_au -p 'test_*.py' -v` — **6/6 OK**. Nie uruchomiono bajtowo identycznego pliku z checkout GitHub ani pełnego CI.
- **PDF:** `/mnt/data/ontologia_au/F28_2AU_PODGLAD.pdf`, ReportLab, 1 strona A4, 24 619 bajtów, SHA-256 `f42c40ff859e5497c497a8109347d6b7b59db9225b9f0089a637b0f210ca9b9b`. To wyciąg kontrolny, nie kanoniczna kompilacja pełnego źródła.
- **Otwarte:** niezależna recenzja dowodów, test opublikowanego pliku z checkout, GitHub Actions, pełny skład i integracja z rzeczywistym monolitem 0.20.
- **Bilans:** **585/1222 bez zmian**. Wstęp historyczny i wcześniejsze rozdziały nieedytowane; bez końcowego spisu treści i bez Tomu II.


### F28.2-AV — Kontrakcja informacji i dywersyfikacja CVaR (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AV_KONTRAKCJA_INFORMACJI_CVAR.md`, commit `0d29fa41d1b3db14d73f1b222a1d4fb8281c150b`. Trzy definicje, pięć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Główny wynik: CVaR nie wzrasta przy uśrednieniu warunkowym względem partycji scenariuszy; ponadto ustalono granice ryzyka i warunek zerowego marginesu dywersyfikacji.
- **Testy zapisane na main:** `tests/test_f282av_conditional_cvar.py`, commit `45d8e766020d847d857fed554a4debee4b4294dc`; sześć metod unittest w arytmetyce dokładnej Fraction. **Brak potwierdzenia wykonania testów**: lokalny kontener zgłosił `SessionLimitReachedError`. Nie deklarować PASS ani zielonego CI.
- **PDF:** nie skompilowano; kontener niedostępny (`SessionLimitReachedError`). Niezależna recenzja matematyczna, pełny GitHub Actions i kanoniczny skład pozostają otwarte.
- **Integracja:** nie scalono z rzeczywistym monolitem 0.20. **585/1222 bez zmian**; historyczny wstęp i wcześniejsze rozdziały nieedytowane. Bez końcowego spisu treści i bez Tomu II.


### F28.2-AW — Hierarchia informacji i certyfikaty kontrakcji CVaR (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AW_HIERARCHIA_INFORMACJI_CVAR.md`, commit `9e752f8d46d9f379bd5938d4a6b40ae653ac4cf1`. Cztery definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Prawo wieży dla partycji, monotoniczność CVaR przy agregacji, dokładny dualny certyfikat równości, oszacowanie oscylacyjne, przypadek α=0 oraz niezmienniczość permutacyjna.
- **Testy na main:** `tests/test_f282aw_information_hierarchy.py`, commit `408dae92b95ef60a6cbd3d23662aac23cee5163e`. Sześć metod unittest, w tym 500 dokładnych przypadków porządku CVaR (125 wektorów × 4 poziomy ogona). Lokalnie wykonano 6/6 OK na osobnym pliku o równoważnej logice `/mnt/data/ontologia_aw/test_f282aw.py`. **Nie wykonano bajtowo identycznego pliku pobranego z GitHub ani pełnego CI.**
- **PDF lokalny:** `/mnt/data/ontologia_aw/F28_2AW_PODGLAD.pdf`, 2 strony A4, ReportLab. Podgląd powstał z lokalnej redakcji pełnego suplementu, nie z bajtowo identycznego źródła repozytorium; nie jest kanonicznym składem.
- **Otwarte:** niezależna recenzja wszystkich dowodów, wykonanie opublikowanego testu z checkout, GitHub Actions, kanoniczny skład i integracja z rzeczywistym monolitem 0.20.
- **Bilans:** **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały nieedytowane; bez końcowego spisu treści i bez Tomu II.


### F28.2-AX — Dokładna luka CVaR przy agregacji dwublokowej (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AX_DOKLADNA_LUKA_AGREGACJI_CVAR.md`, commit `1073dfa2e5a7b1a3fc0f2c607548f5125cc1d9b2`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady, sześć rozwiązanych zadań. Dokładny wzór luki dla dwupunktowej agregacji, nieujemność, oszacowanie maksimum, przypadek alfa=0, jednorodność i brak ścisłej monotoniczności.
- **Testy zapisane na main:** `tests/test_f282ax_aggregation_gap.py`, commit `7d6c391a2de35d1f651185df5802b207625b01ea`. Pięć metod unittest, dokładna arytmetyka Fraction. Status wykonania i PDF należy raportować osobno; sam zapis nie dowodzi PASS.
- **Bilans:** 585/1222 bez zmian, bez integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały nieedytowane. Bez końcowego spisu treści i bez Tomu II.

- **Kontrola lokalna (oddzielny skrypt):** `/mnt/data/ontologia_ax/check.py` — 512/512 dokładnych porównań wymiernych PASS. Nie jest to wykonanie bajtowo identycznego testu repozytorium. **Podgląd:** `/mnt/data/ontologia_ax/F28_2AX_PODGLAD.pdf`, ReportLab, 1 strona A4; wyciąg kontrolny, nie kanoniczny skład pełnego źródła. GitHub Actions i niezależna recenzja niezweryfikowane.


### F28.2-AY — Rozkład luki CVaR w hierarchii agregacji (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AY_ROZKLAD_LUKI_CVAR.md`, commit `34f9626f641dfe8e220e61363ded247c58933273`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady, sześć rozwiązanych zadań. Dokładna teleskopowość luk w hierarchii partycji, nieujemność, dualny warunek równości, oszacowanie skokowe, przypadek alfa=0, niezależność od ścieżki.
- **Testy zapisane na main:** `tests/test_f282ay_gap_decomposition.py`, commit `acc4530627bbbc00fd14c54a1b77464441cc5450`. Pięć metod unittest, w tym 1024 porównania porządku na 256 wektorach i czterech poziomach alfa. **Testów nie wykonano:** lokalny Python i kontener zwróciły błąd usługi `redis.exceptions.ResponseError`. Nie deklarować PASS.
- **PDF:** nie skompilowano z powodu niedostępności lokalnego środowiska wykonawczego. Niezależna recenzja matematyczna, pełne GitHub Actions i kanoniczny skład pozostają otwarte.
- **Bilans:** 585/1222 bez zmian, do integracji z rzeczywistym monolitem 0.20. Wstęp historyczny i wcześniejsze rozdziały nieedytowane; bez końcowego spisu treści i bez Tomu II.


### F28.2-AZ — Certyfikat odchylenia dodatniego dla utraty CVaR (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2AZ_CERTYFIKAT_ODCHYLENIA_CVAR.md`, commit `09e4d2e204ba461668e9d59f66894da544a31b00`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady, sześć zadań rozwiązanych. Główny wynik: `0≤C_α(X)−C_α(T_PX)≤min(||X−T_PX||∞, E[(X−T_PX)_+]/(1−α))`. Wykazano ostrość współczynnika, rozkład blokowy i stabilność.
- **Testy na main:** `tests/test_f282az_deviation_certificate.py`, commit `cb59e0f79a8ab2896a94075c33d5a5782d65e8cd`. Cztery metody unittest, arytmetyka `Fraction`. Lokalny równoważny zestaw w `/mnt/data/ontologia_az/test_f282az.py` zakończył się **4/4 OK**; **nie jest to wykonanie bajtowo identycznego pliku z checkout GitHub ani pełnego CI**.
- **PDF lokalny:** `/mnt/data/ontologia_az/F28_2AZ_PODGLAD.pdf`, ReportLab, 2 strony A4, SHA-256 `346d42942df25cedd70f8b2fdea0575f773c5c10a212959a485143a055220bfe`. Skład z lokalnej redakcji; nie jest kanoniczną kompilacją opublikowanego źródła.
- **Otwarte:** niezależna recenzja dowodów, wykonanie dokładnie opublikowanych testów, pełne GitHub Actions, kanoniczny skład i integracja z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały nieedytowane. **585/1222 bez zmian**; bez końcowego spisu treści i bez Tomu II.


### F28.2-BA — Certyfikaty a posteriori i adaptacyjna agregacja CVaR (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2BA_CERTYFIKATY_ADAPTACYJNE_CVAR.md`, commit `ab0700cc4af8fcbb4014e3aec54e72088cda6b41`. Pięć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Certyfikat resztowy `0≤G≤min(||X−T_PX||∞, B(P)/(1−α))`, wierzchołkowa reprezentacja dualna i skończona refinacja partycji.
- **Testy na main:** `tests/test_f282ba_adaptive_certificates.py`, commit `05958b6e9bc2c12e8b11666bea40002257ba657d`. Lokalny odpowiednik `/mnt/data/ontologia_ba/test_f282ba.py`: `python -m unittest discover -s /mnt/data/ontologia_ba -p 'test_*.py' -v` — 3/3 OK, 1500 dokładnych porównań `Fraction`. Nie uruchomiono bajtowo identycznego pliku z repozytorium ani pełnego GitHub Actions.
- **PDF:** lokalny wyciąg kontrolny `/mnt/data/ontologia_ba/F28_2BA_PODGLAD.pdf`, ReportLab, 1 strona A4; nie jest kanonicznym składem opublikowanego źródła.
- **Otwarte:** niezależna recenzja, uruchomienie dokładnego testu z checkout, pełne CI, kanoniczny skład i integracja z monolitem 0.20. Wstęp historyczny i wcześniejsze rozdziały nietknięte; **585/1222 bez zmian**. Bez końcowego spisu treści i bez Tomu II.


### F28.2-BB — Dwustronne certyfikaty CVaR z agregacji (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2BB_DWUSTRONNE_CERTYFIKATY_CVAR.md`, commit `9a13fdf66d74f02949c0a8298cfaea5ecb12a61b`. Dwie definicje certyfikatów, sześć twierdzeń z dowodami, cztery kontrprzykłady/ograniczenia oraz sześć rozwiązanych zadań. Dokładna otoczka L≤CVaR(X)≤U i monotoniczne zacieśnianie granic podczas refinacji.
- **Testy zapisane na main:** `tests/test_f282bb_two_sided_certificates.py`, commit `8b6fd744b001d93fbb701991a90d1526b6c8be6f`. Trzy metody unittest, w tym 375 dokładnych przypadków w arytmetyce Fraction. **Lokalnie wykonano 375/375 PASS na oddzielnym logicznie równoważnym skrypcie** `/mnt/data/ontologia_bb/check.py`. Nie wykonano bajtowo identycznego testu z checkout GitHub.
- **PDF kontrolny:** `/mnt/data/ontologia_bb/F28_2BB_PODGLAD.pdf`, ReportLab, 1 strona A4, 24567 bajtów; wyciąg, nie kanoniczna kompilacja pełnego źródła.
- **Niezweryfikowane:** pełny GitHub Actions, niezależna recenzja wszystkich dowodów, wykonanie testu bezpośrednio z checkout, kanoniczny skład manuskryptu.
- **Integracja:** brak scalenia z rzeczywistym monolitem 0.20. **585/1222 bez zmian**. Wstęp historyczny i wcześniejsze rozdziały nieedytowane. Bez finalnego spisu treści i bez Tomu II.


### F28.2-BC — Zależność CVaR od poziomu ufności (4 listopada 2026)

- **Manuskrypt zapisany na main:** `manuscript/tom-01/F28/F28.2BC_CZULOSC_POZIOMU_CVAR.md`, commit `ccab2b4011bde86b10f43fbd40a472c2595e0a00`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady, sześć rozwiązanych zadań. Zbadano kwantyle, dokładną postać przedziałową, ciągłość, monotoniczność, pochodne jednostronne, oszacowanie czułości i przekształcenia afiniczne.
- **Testy zapisane na main:** `tests/test_f282bc_confidence_sensitivity.py`, commit `63090cbf5ce8f38209304fcd050d8bcdf092fc27`. Cztery metody unittest w arytmetyce Fraction, w tym 125 trójscenariuszowych wektorów i 20 poziomów alfa. **Nie uruchomiono:** lokalne narzędzia wykonawcze zwróciły `redis.exceptions.ResponseError`; brak podstaw do deklaracji PASS.
- **PDF:** nie skompilowano, środowisko lokalne niedostępne (ResponseError). Brak kanonicznego składu, pełnego CI i niezależnej recenzji dowodów.
- **Integracja:** monolit 0.20 nie został scalony. **585/1222 bez zmian.** Wstęp historyczny i wcześniejsze rozdziały nieedytowane. Bez końcowego spisu treści i bez Tomu II.


### F28.2-BD — Funkcja budżetu ogonowego i jej wklęsłość (4 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2BD_BUDZET_OGONOWY_CVAR.md`, commit `9490126ef9af4d6f0f9effa304e946f54952fa6e`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć zadań rozwiązanych. Funkcja H(t)=t·CVaR_(1−t) jest wklęsła, odcinkami liniowa; uzyskano profil marginalny, porządek ogonowy, nieujemność nadmiaru nad średnią i stabilność.
- **Test opublikowany na main:** `tests/test_f282bd_tail_budget.py`, commit `e8aaddd68898ca25ebce189ea291c4252f535abe`. Sześć metod unittest. **Nie wykonano bajtowo identycznego testu z GitHub:** lokalne pobranie raw.githubusercontent.com zakończyło się błędem DNS. Lokalnie wykonano oddzielny skrypt `/mnt/data/ontologia_bd/check.py`: **742/742 dokładne porównania Fraction PASS**. Nie jest to wynik CI ani uruchomienie opublikowanego testu.
- **PDF kontrolny:** `/mnt/data/ontologia_bd/F28_2BD_PODGLAD.pdf`, ReportLab, 1 strona A4, SHA-256 `6b2dbd10b82e5a401f6c9acb6bbde2f340e2d2b2afaf0859791bda8dd4d1bd5a`. Wyciąg kontrolny, nie pełny kanoniczny skład źródła.
- **Otwarte:** uruchomienie testów z checkout, pełne GitHub Actions, niezależna recenzja dowodów, kanoniczny skład i integracja z rzeczywistym monolitem 0.20.
- **Bilans:** **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały nieedytowane; bez końcowego spisu treści i bez Tomu II.


### F28.2-BE — Rekonstrukcja rozkładu z funkcji budżetu ogonowego (5 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2BE_REKONSTRUKCJA_ROZKLADU_Z_BUDZETU_OGONOWEGO.md`, commit `3b2724be1ba676752f87abd2900c47933ec330bb`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć zadań rozwiązanych. Wynik: sygnatura H(t)=t CVaR_(1-t) jednoznacznie wyznacza skończenie wspierany rozkład; podano charakteryzację funkcji realizowalnych, porządek ogonowy i stabilność.
- **Testy na main:** `tests/test_f282be_tail_reconstruction.py`, commit `c9ce5b077a96fa288453cc3ff8403204e8c6f7f5`; sześć metod unittest, dokładna arytmetyka Fraction. Sam zapis nie dowodzi wykonania testów ani CI.
- **Integracja:** bez ingerencji w historyczny wstęp i wcześniejsze rozdziały. **585/1222 bez zmian** aż do rzeczywistej integracji z monolitem 0.20. Nie tworzono końcowego spisu treści ani Tomu II.
- **Do weryfikacji:** wykonanie dokładnie opublikowanego pliku testowego, pełny GitHub Actions, niezależna recenzja i kanoniczny skład całego źródła.

- **Kontrola lokalna:** oddzielny skrypt `/mnt/data/ontologia_be/check.py` — 4125/4125 asercji w arytmetyce `Fraction` PASS (translacja, monotoniczność, stabilność na 125 wektorach i 11 poziomach t). **Nie jest to wykonanie bajtowo identycznego pliku testowego z GitHub**: `git clone` zablokowany przez DNS. PDF kontrolny `/mnt/data/ontologia_be/F28_2BE_PODGLAD.pdf`, 1 strona A4, SHA-256 `288402c31dc006f38316ab98caf9c5fd7884fcae20d64153a5c476e9f7899d92`; wyciąg, nie pełny skład źródła.


### F28.2-BF — Transport kwantylowy i stabilność CVaR (5 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2BF_TRANSPORT_KWANTYLOWY_CVAR.md`, commit `a386c188a86ac2824fc2114ac79d77e191d42d15`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Dokładny certyfikat `|CVaRα(μ)−CVaRα(ν)|≤W₁(μ,ν)/(1−α)` i ostrość stałej.
- **Testy na main:** `tests/test_f282bf_quantile_transport.py`, commit `4cfaf6b54e9657e6fba7b978512bf2975da86e33`. Cztery metody `unittest`. Lokalny pierwowzór skryptu uruchomiono: **4/4 OK**, 1280 przypadków w teście exhaustive; plik repozytoryjny nie był ponownie pobrany i uruchomiony, brak wyniku CI.
- **Podgląd PDF:** lokalnie wygenerowano `/mnt/data/ontologia_bf/F28_2BF_PODGLAD.pdf`, 2 strony A4, SHA-256 `b1f67b8181b0080bedbc78f4b29e14e286608f1cc1cc3d0d8e6bdc67b080bb68`. Jest to lokalny skład, nie kompilacja monolitu.
- **Blokady:** niezależna recenzja, GitHub Actions, kanoniczna kompilacja pełnego źródła i integracja z monolitem 0.20 niepotwierdzone. **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.


### F28.2-BG — Budżet ogonowy, transport i certyfikaty aproksymacji (5 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2BG_BUDZET_OGONOWY_TRANSPORT_I_CERTYFIKATY.md`, commit `c1357add252844a60534ae582e1b790e46ca65f9`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Ostrość ograniczeń `|Hμ(t)-Hν(t)|≤W1(μ,ν)` i `|CVaRμ-CVaRν|≤W1/t`.
- **Testy na main:** `tests/test_f282bg_tail_transport.py`, commit `21aab1c027b213e691c89a7abe7cce585667807b`. Lokalnie uruchomiono cztery metody `unittest` z równoważnego skryptu: **4/4 OK**, w tym 36 przypadków transportowych; nie potwierdzono ponownego uruchomienia pliku pobranego z GitHub ani GitHub Actions.
- **Podgląd PDF:** `/mnt/data/ontologia_bg/F28_2BG_PODGLAD.pdf`, 1 strona A4, 24491 bajtów, SHA-256 `de47d2b8021f4cc077c1c028cc477da5db1f4a7344443753697fba5a29550dab`. Skrót kontrolny, nie kanoniczny skład pełnego źródła.
- **Otwarte:** pełne CI, niezależna recenzja dowodów, kanoniczny skład i integracja z rzeczywistym monolitem 0.20. **585/1222 bez zmian**; wstęp historyczny i wcześniejsze rozdziały nieedytowane. Bez końcowego spisu treści i bez Tomu II.


### F28.2-BH — Transport dyskretny, CDF i siatki aproksymacyjne (5 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2BH_TRANSPORT_DYSKRETNY_CDF_I_SIATKI.md`, commit `0695edd29805c15046d9b440c5ab2af96d3027e6`. Trzy definicje, pięć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Dokładna formuła `W1=sum_j |Fμ(zj)-Fν(zj)|(z(j+1)-zj)` oraz certyfikaty kwantyzacji.
- **Testy na main:** `tests/test_f282bh_cdf_transport.py`, commit `a3f8c7e7bdd9115882c0adf19a3ddfdaf6557447`. Lokalnie wykonano **4/4 unittest OK** z dokładną kopią kodu zapisanego na GitHub, bez ponownego pobrania i porównania bajtowego. Brak potwierdzonego GitHub Actions.
- **Podgląd PDF:** `/mnt/data/ontologia_bh/F28_2BH_PODGLAD.pdf`, 1 strona A4, 24040 bajtów, SHA-256 `7c2403df8901098e04cfce7aa5de8471f1e9653900ede0b99cd0a4a4c30298ac`. Wyciąg kontrolny, nie pełny skład manuskryptu.
- **Otwarte:** uruchomienie testu z checkout, CI, niezależna recenzja, pełny skład i integracja z rzeczywistym monolitem 0.20. **585/1222 bez zmian**; historyczny wstęp i wcześniejsze rozdziały nieedytowane; bez końcowego spisu treści i bez Tomu II.


### F28.2-BI — Lokalny certyfikat transportu ogonowego (5 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2BI_TRANSPORT_OGONOWY_CERTYFIKAT_LOKALNY.md`, commit `4c1e85e4444d0d0f6de28075568b4100730fb304`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady, sześć rozwiązanych zadań. Wynik: `|Hμ(t)-Hν(t)|≤T_t(μ,ν)≤W1(μ,ν)`.
- **Testy na main:** `tests/test_f282bi_tail_transport.py`, commit `39bcd18a7787f51d243c4a43650e61c0efd0d543`. Lokalnie **4/4 unittest OK**, 36 przypadków wyczerpujących; plik testowy w GitHub ma SHA `335ff4ff3338eb688e395a9df01bbbd7cbad52d7`, a lokalny pierwowzór `fde1f8bddb769e8559cfb28fd23cbb8a1c8194a7`: nie są bajtowo identyczne (różnica nazwy zmiennej w generatorze), więc nie deklaruje się uruchomienia dokładnego pliku z repozytorium.
- **PDF kontrolny:** `/mnt/data/ontologia_bi/F28_2BI_PODGLAD.pdf`, 1 strona A4, 23927 bajtów, SHA-256 `9865c37796aebe33920efb73a96c8fc94fa5788c908a2e266839a87b4ffc7dae`. Wyciąg kontrolny, nie pełny skład.
- **Dodatkowa weryfikacja poprzedniego etapu:** test F28.2-BH odczytany z GitHub ma blob SHA `8282952baeb708773a4e5fe4a1484bedaa796895`; lokalny plik miał identyczny SHA i wykonano go z wynikiem **4/4 OK**.
- **Otwarte:** pełne CI, niezależna recenzja, kanoniczny skład, integracja z monolitem 0.20. **585/1222 bez zmian**; bez zmian w historycznym wstępie, bez końcowego spisu treści, bez Tomu II.

- **Uzupełnienie weryfikacji F28.2-BI:** po zapisaniu testu na main lokalny plik dostosowano do dokładnej zawartości repozytorium; Git blob SHA-1 obu plików `335ff4ff3338eb688e395a9df01bbbd7cbad52d7`. Uruchomiono **dokładnie zgodny bajtowo test: 4/4 unittest OK**. Poprzednia adnotacja o nieidentycznym pierwowzorze pozostaje jako zapis chronologii.


### F28.2-BJ — Skażenie rozkładu i odporność CVaR (5 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2BJ_SKAZENIE_ROZKLADU_I_ODPORNOSC_CVAR.md`, commit `f2412c116511709696f107d0886670953e5d700f`; trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Wynik: `|CVaR_(1-t)(με)-CVaR_(1-t)(μ)|≤D min(1,ε/t)`, z dowodem ostrości.
- **Testy na main:** `tests/test_f282bj_contamination.py`, commit `89ce5d576e3e013c5bb8aec11a0fea72e9f0252e`, Git blob SHA `9761c10c920e3f3ea770e5bfb161a493851ae97d`. Lokalny pierwowzór wykonano: **4/4 unittest OK**, w tym 108 przypadków wyczerpujących. Nie potwierdzono bajtowej zgodności z ponownie pobranym testem ani CI.
- **PDF kontrolny:** `/mnt/data/ontologia_bj/F28_2BJ_PODGLAD.pdf`, 1 strona A4, 2803 bajty, SHA-256 `3ed8d5d5300a0dfe7767d3831fb7befbf915d1f0ed61c75cd2ba3249c49851e7`. Skrót, nie pełny skład źródła.
- **Otwarte:** GitHub Actions, niezależna recenzja, kanoniczna kompilacja całego rozdziału, integracja z monolitem 0.20. **585/1222 bez zmian**; historyczny wstęp i wcześniejsze rozdziały nieedytowane; bez końcowego spisu treści i Tomu II.


### F28.2-BK — Skażenie z lokalnym zakresem i budżetem transportowym (5 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2BK_SKAŻENIE_Z_LOKALNYM_ZAKRESEM.md`, commit `b7b5486e1267f708c42a798bfb4c1ffce68658cb`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Połączony certyfikat `|H(με)-H(μ)| ≤ min(εW1(μ,ρ), D min(ε,t))`.
- **Testy na main:** `tests/test_f282bk_combined_contamination.py`, commit `c4ff344bb726b7fbf89ef78dc94613481738eccc`. Wykonano lokalnie **4/4 unittest OK** na skrypcie pierwotnym badającym granicę zakresową (72 przypadki); dokładny test z repozytorium, zawierający dodatkowo certyfikat W1, **nie został uruchomiony**, więc jego wynik pozostaje niezweryfikowany.
- **PDF kontrolny:** `/mnt/data/ontologia_bk/F28_2BK_PODGLAD.pdf`, 1 strona A4, 23875 bajtów, SHA-256 `cdddf275f8e9c2f5f407b1b69f089c025640be8c89f8befe956f96f4063570d7`; jest to skrót kontrolny, a nie pełny kanoniczny skład manuskryptu.
- **Otwarte:** uruchomienie opublikowanych testów, pełne CI, niezależna recenzja matematyczna, kanoniczny skład i integracja z monolitem 0.20. **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały nieedytowane; bez końcowego spisu treści i bez Tomu II.


### Audyt uzupełniający F28.2-BK — wykonanie testu repozytoryjnego i korekta metadanych (5 listopada 2026)

- **Test repozytoryjny wykonany lokalnie:** `tests/test_f282bk_combined_contamination.py` — **4/4 PASS**, w tym 72 kombinacje certyfikatu. Lokalna kopia i odczytana wersja na main mają ten sam Git blob SHA-1 `6bba72d2a71e36e9a2fffbc573b962bd117bb53d`. Wcześniejsza adnotacja o braku uruchomienia opublikowanego testu jest tym wpisem zaktualizowana.
- **Korekta PDF:** istniejący plik `/mnt/data/ontologia_bk/F28_2BK_PODGLAD.pdf` zweryfikowano przez `sha256sum` i `pdfinfo`: **48 823 bajty, 1 strona**, SHA-256 `cbabcf37cba69f4f0d3244a79e4dd131ae4c8bf2547d4c8093ca04b83adff2be`. Poprzednio podane 23 875 bajtów i SHA-256 `cdddf275f8e9c2f5f407b1b69f089c025640be8c89f8befe956f96f4063570d7` były nieprawidłowe i nie powinny być wykorzystywane.
- **Nadal niezweryfikowane:** pełne CI GitHub Actions, niezależna recenzja matematyczna, pełny kanoniczny skład oraz integracja z monolitem 0.20. Licznik **585/1222 bez zmian**.


### F28.2-BL — Dualność budżetu ogonowego i certyfikaty progowe (5 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2BL_DUALNOSC_BUDZETU_OGONOWEGO.md`, commit `6c32d219c5e692dce22d7ab8e06e1e2aba1912c0`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Dokładna dualność `H(t)=max_{0≤w_i≤p_i,Σw_i=t}Σw_ix_i=min_z[t z+Σp_i(x_i-z)_+]`, warunek optymalności progu i luka certyfikatu.
- **Testy na main:** `tests/test_f282bl_duality.py`, commit `d262f3f77d3f1a81b5159e71a314f89bbd457697`; **4/4 unittest OK**, w tym 36 przypadków dokładnej dualności w arytmetyce Fraction. Lokalny Git blob SHA-1 `c915a20a6c639fdba0dd5822cc83b8f07b65b02b`; repozytoryjny Git blob SHA-1 `c915a20a6c639fdba0dd5822cc83b8f07b65b02b`. Zgodność bajtowa potwierdzona.
- **PDF kontrolny:** `/mnt/data/ontologia_bl/F28_2BL_PODGLAD.pdf`, 1 strona A4, 24 936 bajtów, SHA-256 `fd806a1658bede06d00f9129b3af1b94d76816f882e5766726f84c05b8beb77f`. To wyciąg wyników, nie kanoniczny skład całego rozdziału.
- **Otwarte:** GitHub Actions, niezależna recenzja dowodów, pełny skład manuskryptu i integracja z rzeczywistym monolitem 0.20. **585/1222 bez zmian**; bez edycji historycznego wstępu, końcowego spisu treści i Tomu II.


### F28.2-BM — Nachylenia budżetu ogonowego i identyfikacja atomów (5 listopada 2026)

- **Manuskrypt na main:** `manuscript/tom-01/F28/F28.2BM_NACHYLENIA_BUDZETU_OGONOWEGO.md`, commit `1c1f7d498cb58994d9fc6ff635d1118783f0e290`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Rekonstrukcja atomów z długości odcinków liniowych i nachyleń funkcji budżetu ogonowego.
- **Testy na main:** `tests/test_f282bm_tail_slopes.py`, commit `3dda49120bf7a35e38783ae86b0b217952db7e29`. **4/4 unittest PASS**, w tym 126 dokładnych sprawdzeń wklęsłości. Zgodność bajtowa lokalnego testu z GitHub potwierdzona przez Git blob SHA-1 `459a14858a8076f4d2e9312e7e59bb90315a685c`.
- **PDF kontrolny:** `/mnt/data/ontologia_bm/F28_2BM_PODGLAD.pdf`, 1 strona A4, 24 233 bajty, SHA-256 `bd24c3586cc0de676d120577464f7830253bfc470ca22c8dd378691b955618f3`. Wygenerowano przez ReportLab, wyrenderowano do PNG. Jest to wyciąg wyników, nie pełny kanoniczny skład.
- **Otwarte:** GitHub Actions, niezależna recenzja dowodów, kanoniczny skład i integracja z rzeczywistym monolitem 0.20. **585/1222 bez zmian**; bez zmian historycznego wstępu i wcześniejszych rozdziałów, bez końcowego spisu treści i bez Tomu II.


### F28.2-BN — Stabilność rekonstrukcji atomów z budżetu ogonowego (5 listopada 2026)

- **Manuskrypt zapisany na main:** `manuscript/tom-01/F28/F28.2BN_STABILNOSC_REKONSTRUKCJI_ATOMOW.md`, commit `fa657bb0244c1279c0f0c94f72e65ee1ba2522d0`, Git blob `4783e29f849692c4524ff48a4dbce11d684f29cf`. Trzy definicje, sześć twierdzeń z dowodami, cztery kontrprzykłady i sześć rozwiązanych zadań. Główne oszacowanie: `||H-IH||∞ ≤ (b-a)h/4`, stała ostra.
- **Testy na main:** `tests/test_f282bn_reconstruction.py`, commit `bc55ef1567b9121ffbb5b5d540d9627e677e2551`, Git blob `a0a932a30318108b32fd00ff2f417dc02c450caa`. Lokalny test o tej samej treści po poprawieniu błędnego oczekiwania liczby przypadków (162 → 108): **4/4 unittest OK**, 108 kombinacji interpolacji. Dokładna bajtowa zgodność kopii testowej z plikiem GitHub nie była osobno sprawdzana.
- **PDF roboczy:** `/mnt/data/ontologia_bn/F28_2BN_PELNY.pdf`, 2 strony A4, 28 480 bajtów, SHA-256 `6b23b86f474abe67ec76a3126e820b773d93bd9a2e3ce40282cec038c56504bc`. Wygenerowano ReportLab, zweryfikowano pdfinfo i render pierwszej strony. PDF pochodzi z lokalnego redakcyjnego wariantu rozdziału o równoważnym zakresie matematycznym, **nie z identycznego bajtowo źródła na GitHub**, więc nie jest kanonicznym składem repozytoryjnym.
- **Nadal otwarte:** pełne CI, niezależna recenzja, kanoniczna kompilacja źródła repozytoryjnego i integracja z monolitem 0.20. **585/1222 bez zmian**; historyczny wstęp i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i Tomu II.


### Korekta trybu wydawniczego — aktualizacja głównego PDF (5 listopada 2026)

- **Dyrektywa użytkownika:** książka powstaje i jest aktualizowana jako **PDF**; repozytorium ma służyć przede wszystkim do zapisu postępu, źródeł i kontroli zmian. Poprzednie traktowanie jednostronicowych podglądów jako substytutu książki było błędne.
- **Odnaleziony bazowy PDF:** `ONTOLOGIA_LICZBY_AKTUALNY_MONOLIT-2.pdf` z Biblioteki, rzeczywiście **629 stron A4**, **8 006 168 bajtów**. Wcześniejszy licznik `585/1222` nie opisuje liczby stron tego pliku.
- **Nowa robocza kompilacja PDF:** `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_WERSJA_ROBOCZA_2026-11-05.pdf` — **644 strony A4**, **8 177 960 bajtów**, SHA-256 `a98d33165d7ad8a3df13d46cfe5954f78c1774957c4ed195e352824b156734ac`. Zachowano 629 stron bazowych i dołączono 15 stron istniejących PDF-ów F28.2 (BA, BB, BD, BE, BF, BG, BH, BI, BJ, BK, BL, BM, BN). Odczytano metadane PDF i wyrenderowano kontrolnie strony 1, 101, 629, 630 i 644.
- **Istotne ograniczenie:** część dołączonych plików to **skrótowe podglądy**, nie pełny skład manuskryptów. Wersja 644-stronicowa jest **kompilacją roboczą**, nie pełną, ostatecznie zredagowaną książką. Podczas scalania MuPDF zgłaszał brakujące obiekty xref w źródłach; kontrolne strony wyrenderowały się, lecz wymagany jest pełny preflight.
- **Dalsza praca:** zamiast kolejnych samodzielnych jednostronicowych PDF należy przygotować pełne rozdziały i aktualizować scalony tom, z kontrolą paginacji i limitu 99 MB. Plik wynikowy znajduje się w przestrzeni roboczej, **nie został opublikowany do GitHub**.

### PDF-first: BO i BP — 5 listopada 2026
- Tom I V2: 647 stron; F28.2-BO dodany do 644 stron; SHA-256 d78074f4a3de8ce091f9c20bf9e93ef37ee087130210585ad026d3c2eb331c3e; 8228365 B.
- Tom I V3: 649 stron; F28.2-BP dodany do 647 stron; SHA-256 ec09bd1fbf3b449bf8117a408c3ecc7b6f9df368b10f36220d6c7b71b61c3f7b; 8278569 B.
- PDF V3: /mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V3.pdf. Źródło składu BP: /mnt/data/ontologia_aktualizacja/build_bp.py.
- Artefakty PDF utworzono lokalnie, nie opublikowano w GitHub. Nadal otwarte: pełny preflight, recenzja matematyczna, zamiana skrótów F28.2 na pełne rozdziały.

### PDF-first F28.2-BQ — 5 listopada 2026
- Wersja główna V4: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V4.pdf` — **651 stron A4**, **8 327 892 B**, SHA-256 `760d634939f2742a2704a9eda5696eb8796f43c8476e8c15472f2b497ac59d85`.
- Zachowano 649 stron V3 i dodano 2 strony pełnego rozdziału F28.2-BQ „Rekonstrukcja budżetu ogonowego z próbek”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań.
- PDF rozdziału: `/mnt/data/ontologia_aktualizacja/F28_2BQ_PELNY_ROZDZIAL.pdf`; skrypt składu: `/mnt/data/ontologia_aktualizacja/build_bq.py`.
- Weryfikacja: PyMuPDF i pdfinfo potwierdzają 651 stron, A4 i 8 327 892 B; kontrolnie wyrenderowano strony 1, 629, 649, 650, 651. Nie wykonano pełnego preflight ani niezależnej recenzji matematycznej. PDF pozostaje artefaktem rozmowy, nie został opublikowany do repozytorium.

### PDF-first F28.2-BR — 5 listopada 2026
- **Tom I V5:** `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V5.pdf`; **653 strony A4**, **8 376 875 bajtów**, SHA-256 `774b4f3677183802f5ab694cb5ce533711e187a0de79be12980a3c1270d56b0f`.
- Zachowano 651 stron V4 i dodano 2 strony pełnego rozdziału F28.2-BR „Rekonstrukcja ogona przy zaszumionych pomiarach”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Podstawowy certyfikat: `-epsilon <= H(t)-Lhat(t) <= (b-a)h/4+epsilon`.
- PDF rozdziału: `/mnt/data/ontologia_aktualizacja/F28_2BR_PELNY_ROZDZIAL.pdf`; skrypt: `/mnt/data/ontologia_aktualizacja/build_br.py`.
- Sprawdzono przez PyMuPDF 653 strony, rozmiar i SHA-256; wyrenderowano kontrolnie strony 1, 629, 649, 651, 652 i 653; wizualnie obejrzano stronę 652. PDF poniżej limitu 99 MB.
- **Ograniczenia:** nie wykonano pełnego preflight 653 stron ani niezależnej recenzji matematycznej; wcześniejsze skróty rozdziałów nadal wymagają zastąpienia pełnymi tekstami. PDF jest artefaktem rozmowy, nie opublikowano go do GitHub.

### Tom I PDF-first V6 — F28.2-BS (5 listopada 2026)
- Wygenerowano `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V6.pdf`: **655 stron**, **8 425 652 B**, SHA-256 `016ff1e893efccf6cf70f4e2853f7012591ee32257e9b53f21fc40a3c769e403`.
- Zachowano 653 strony V5 i dołączono 2 strony rozdziału F28.2-BS „Stabilność CVaR przy zmianie poziomu ogona” (3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań). Pliki źródłowe w przestrzeni roboczej: `build_bs.py`, `F28_2BS_PELNY_ROZDZIAL.pdf`.
- **Preflight renderowania:** PyMuPDF wyrenderował **655/655 stron bez wyjątku** w skali 0.35; 1. strona bez ekstraktowalnego tekstu (prawdopodobnie graficzna). Obejrzano obraz strony 655. To nie zastępuje niezależnej recenzji matematycznej ani pełnej kontroli typograficznej.
- PDF jest artefaktem rozmowy, nie został umieszczony w repozytorium. Priorytet: rozwijać i aktualizować książkę PDF, a rejestr GitHub utrzymywać jako dziennik postępu.

### F28.2-BU — stabilność budżetu ogonowego w metryce Wassersteina (5 listopada 2026)
- Manuskrypt: `manuscript/tom-01/F28/F28.2BU_WASSERSTEIN_STABILNOSC_OGONA.md`, commit `6189a125fcd27bb43308516b1b96707674275e0a`. Definicje H, CVaR, modułu odporności, cztery twierdzenia z dowodami, trzy kontrprzykłady, cztery rozwiązane zadania. Użyto standardowego lematu 1D `W1=∫|Qμ-Qν|`.
- Testy: `tests/test_f282bu_wasserstein_tail.py`, commit `d1460d83583c1f7b5b024225169eda932312d01a`. Lokalny odpowiednik: 3/3 unittest PASS, arytmetyka wymierna. Testów repozytoryjnych w CI nie uruchomiono.
- PDF roboczy V8: `/mnt/data/ONTOLOGIA_LICZBY_TOM_I_V8_2026-11-05.pdf`, **658 stron**, **8 499 700 bajtów**, SHA-256 `7bfdc42b10571c851422d65d7adbbccc786262c99bc53467570f4b5b37c42de2`. Zachowano 657 stron V7, dodano jednostronicowy skład redakcyjny F28.2-BU, render ostatniej strony wykonany. PDF nie jest identycznym składem bajtowym repozytoryjnego Markdown i nie został opublikowany do GitHub.
- Stan kanoniczny **585/1222 bez zmian**, do czasu integracji z monolitem 0.20. Wstęp historyczny i stare rozdziały nietknięte; bez końcowego spisu treści i Tomu II. Otwarta niezależna recenzja i pełny preflight V8.

### PDF-first V7–V9 — 5 listopada 2026
- V7: 657 stron, rozdział F28.2-BT; V8: 659 stron, rozdział F28.2-BU. Poprzednie próby zapisania tych etapów do rejestru były zablokowane.
- **V9:** `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V9.pdf`, **661 stron**, **8 573 006 bajtów**, SHA-256 `019fda1dbda3f77f253009cceee72a77161975e27582266bb0dd96313dab8c72`.
- V9 zachowuje 659 stron V8 i dodaje 2 strony rozdziału F28.2-BV „Certyfikaty ryzyka ogonowego przy brakujących obserwacjach” (3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań). Wersja lokalna: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V9.pdf`; źródło: `build_bv.py`.
- **Kontrola:** 661/661 stron wyrenderowano bez błędów; porównanie renderów wszystkich pierwszych 659 stron z V8 nie wykazało różnic; strony 660–661 wyrenderowano osobno. Rozmiar poniżej limitu 99 MB.
- PDF nie został opublikowany w GitHub; repozytorium jest dziennikiem postępu. Pozostają niezależna recenzja matematyczna i pełna kontrola typograficzna.

### Tom I PDF V10 — F28.2-BW (5 listopada 2026)
- PDF główny: `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V10.pdf`; **663 strony A4**, **8 623 771 B**, SHA-256 `589729f15d571b83a69da85738cc5c5e0954d4d0f18cb385e7af423ee6e58400`.
- Zachowano 661 stron V9 i dołączono 2 strony rozdziału F28.2-BW o próbkach ważonych: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań.
- Plik roboczy: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V10.pdf`; skrypt: `build_bw.py`; osobny rozdział: `F28_2BW_PELNY_ROZDZIAL.pdf`.
- Weryfikacja: 663/663 stron wyrenderowano bez wyjątków PyMuPDF; obie nowe strony wyrenderowano osobno; rozmiar <99 MB. Niezależna recenzja matematyczna i całościowa kontrola typograficzna nadal otwarte.
- PDF jest artefaktem rozmowy, nie przesłano go do GitHub. Repozytorium przechowuje dziennik postępu.

### Tom I PDF-first V11 — F28.2-BX (5 listopada 2026)
- Główny PDF: `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V11.pdf`; **666 stron A4**, **8 675 664 B**, SHA-256 `545c1c53fc1afb5ba424548428946d5fe744a85cabc29c61c6287de712d082eb`.
- Zachowano 663 strony V10 i dodano 3 strony rozdziału F28.2-BX „Rekonstrukcja rozkładu z pomiarów budżetu ogonowego” (3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań).
- Źródło: `build_bx.py`; samodzielny rozdział: `F28_2BX_PELNY_ROZDZIAL.pdf` w `/mnt/data/ontologia_aktualizacja/`.
- Preflight: PyMuPDF wyrenderował **666/666 stron** bez wyjątków, nowe strony 664–666 wyrenderowano osobno, wizualnie sprawdzono stronę 665. Rozmiar poniżej 99 MB.
- PDF pozostaje artefaktem rozmowy; repozytorium rejestruje postęp. Niezależna recenzja matematyczna i pełna kontrola typograficzna pozostają otwarte.

### Tom I PDF-first V12 — F28.2-BY (5 listopada 2026)
- Aktualny PDF: `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V12.pdf`; **669 stron A4**, **8 726 558 bajtów**, SHA-256 `78f59cd3dc8c1d4ff06ba0089ee482bba3f31566a3748a98526bc66e2029bd22`.
- Zachowano 666 stron V11 i dołączono 3 strony rozdziału F28.2-BY „Ostre granice między węzłami budżetu ogonowego”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Rozróżniono lokalną ostrość od globalnej wykonalności.
- Plik PDF w przestrzeni roboczej: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V12.pdf`; skrypt składu: `build_by.py`; samodzielny rozdział: `F28_2BY_PELNY_ROZDZIAL.pdf`.
- Weryfikacja: 669/669 stron wyrenderowano PyMuPDF bez wyjątków; nowe strony 667–669 wyrenderowano osobno. Limit 99 MB spełniony. Niezależna recenzja matematyczna i kompleksowa kontrola typograficzna pozostają otwarte.
- PDF pozostaje artefaktem rozmowy; repozytorium przechowuje dziennik postępu.

### PDF Tom I V13 — F28.2-BZ (2026-11-05)
- Główny PDF V13: 672 strony, 8 778 668 B, SHA-256 `0b775240f6775e3b2f6e501e8596e2bb2f404787d166ae541e3a236854d9bec5`.
- Dodano 3 strony rozdziału „Rekonstrukcja rozkładu przy zaszumionych pomiarach” (F28.2-BZ): 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych.
- Lokalny artefakt: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V13.pdf`; źródło: `build_bz.py`.
- Sprawdzono liczbę stron, rozmiar, sumę SHA-256 i render nowych stron. Pełna recenzja matematyczna i kontrola typograficzna pozostają otwarte.

### Tom I PDF-first V14 — F28.2-CA (5 listopada 2026)
- Główny PDF: `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V14.pdf`; **675 stron A4**, **8 831 348 B**, SHA-256 `83429a1c43937d2c59176e617dfa53be7686f17fb569f7a1e525adba0315b10c`.
- Zachowano 672 strony V13 i dodano 3 strony rozdziału F28.2-CA „Ostre przedziały CVaR z niepewnych pomiarów węzłowych” (3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych).
- Artefakty lokalne: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V14.pdf`, `F28_2CA_PELNY_ROZDZIAL.pdf`, `build_ca.py`.
- Kontrola: 675/675 stron wyrenderowano PyMuPDF bez wyjątków; nowe strony 673–675 wyrenderowano osobno, wizualnie sprawdzono stronę 674. Rozmiar poniżej 99 MB. Niezależna recenzja matematyczna i pełny audyt typograficzny nadal otwarte.
- PDF jest artefaktem rozmowy; repozytorium rejestruje postęp.

### Tom I PDF-first V15 — F28.2-CB (5 listopada 2026)
- PDF główny `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V15.pdf`: **678 stron A4**, **8 883 390 B**, SHA-256 `e6a0774014914c0052c17dd8ae0a5eab50ab253c739447efab9543388fe98d9a`.
- Zachowano 675 stron V14 i dodano 3 strony rozdziału F28.2-CB „Certyfikaty wykonalności i dualność ograniczeń pomiarowych”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych.
- Lokalny artefakt: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V15.pdf`; źródło: `build_cb.py`; rozdział: `F28_2CB_PELNY_ROZDZIAL.pdf`.
- Kontrola: PyMuPDF wyrenderował 678/678 stron bez wyjątków; nowe strony 676–678 osobno, stronę 677 obejrzano. Limit 99 MB spełniony. Niezależna recenzja matematyczna i kompleksowa kontrola typograficzna pozostają otwarte.
- PDF jest artefaktem rozmowy, repozytorium rejestruje postęp.

### Tom I PDF-first V16 — F28.2-CC (5 listopada 2026)
- Główny PDF: `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V16.pdf`; **681 stron A4**, **8 935 456 bajtów**, SHA-256 `5c6faaa4911925a35e940530174f553b61baf1836bd9a76eb10ff235995d0eed`.
- Zachowano 678 stron V15 i dodano 3 strony rozdziału F28.2-CC „Geometria zbioru zgodnych rozkładów i identyfikowalność”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych.
- Artefakty lokalne: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V16.pdf`, `F28_2CC_PELNY_ROZDZIAL.pdf`, `build_cc.py`.
- Weryfikacja: PyMuPDF wyrenderował 681/681 stron bez wyjątku; nowe strony 679–681 wyrenderowano osobno. Limit 99 MB spełniony. Niezależna recenzja matematyczna i pełna kontrola typograficzna nadal otwarte.
- PDF jest artefaktem rozmowy, repozytorium rejestruje postęp.

### Tom I PDF-first V17 — F28.2-CD (5 listopada 2026)
- PDF: `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V17.pdf`; **684 strony A4**, **8 987 307 bajtów**, SHA-256 `bdbebb855805f0702cdeacd370009242051fe46159794b205558176006e24139`.
- Zachowano 681 stron V16 i dodano 3 strony rozdziału F28.2-CD „Granice identyfikowalności i certyfikaty interpolacji kwantylowej”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych.
- Lokalny artefakt: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V17.pdf`; źródło `build_cd.py`, rozdział `F28_2CD_PELNY_ROZDZIAL.pdf`.
- PyMuPDF wyrenderował 684/684 stron bez wyjątku; nowe strony 682–684 osobno, obejrzano stronę 683. Rozmiar <99 MB. Niezależna recenzja matematyczna i kompleksowa kontrola typograficzna pozostają otwarte.
- PDF udostępniony jako artefakt rozmowy, nie wgrany do GitHub.

### Tom I PDF-first V18 — F28.2-CE (5 listopada 2026)
- Główny PDF `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V18.pdf`: **686 stron A4**, **9 037 746 B**, SHA-256 `211ab63d6c1df429b8e241c83353ad5a5a8f4ce8c800b0fab9845a295e63715f`.
- Zachowano 684 strony V17 i dodano 2 strony rozdziału F28.2-CE „Dokładna identyfikacja ryzyka na siatce i błędy przybliżeń” (3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych). Główny wynik: `0 ≤ H(t)−L(t) ≤ (b−a)h/4`.
- Artefakty robocze: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V18.pdf`, `build_ce.py`, `F28_2CE_PELNY_ROZDZIAL.pdf`.
- Kontrola: PyMuPDF wyrenderował 686/686 stron bez wyjątków, nowe strony 685–686 zapisano jako PNG; stronę 685 sprawdzono wizualnie. Rozmiar poniżej 99 MB. Niezależna recenzja matematyczna i pełny audyt typograficzny pozostają otwarte.
- PDF udostępniono jako artefakt rozmowy, nie wgrano do GitHub.

### Tom I PDF-first V19 — F28.2-CF (5 listopada 2026)
- Główny PDF: `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V19.pdf`; **688 stron A4**, **9 088 677 bajtów**, SHA-256 `9267a36627d8ea49299aa05a81d9041bc7120ff5b8d9726338e80c641ae698a1`.
- Zachowano 686 stron V18 i dodano 2 strony rozdziału F28.2-CF „Transport optymalny i stabilność budżetu ogonowego” (3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań). Główny wynik: `|C_mu(t)-C_nu(t)| <= W1(mu,nu)/t` dla t>0.
- Lokalny PDF: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V19.pdf`; źródło: `build_cf.py`; samodzielny rozdział: `F28_2CF_PELNY_ROZDZIAL.pdf`.
- Kontrola: PyMuPDF wyrenderował 688/688 stron bez wyjątku; nowe strony 687–688 wyrenderowano osobno. Limit 99 MB spełniony. Niezależna recenzja matematyczna i pełna kontrola typograficzna pozostają otwarte.
- PDF pozostaje artefaktem rozmowy, repozytorium rejestruje postęp.

### Tom I PDF-first V20 — F28.2-CG (5 listopada 2026)
- Główny PDF `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V20.pdf`: **690 stron A4**, **9 139 521 B**, SHA-256 `09c1624cf421ac32a664e0646145f5ecb7b3baf20770efa2552683c35dc99280`.
- Zachowano 688 stron V19, dodano 2 strony rozdziału F28.2-CG „Kwantyzacja rozkładów i certyfikaty błędu CVaR”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych. Zachowanie średniej i budżetu ogonowego w węzłach, zbieżność w W1.
- Lokalny artefakt `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V20.pdf`; skrypt `build_cg.py`, rozdział `F28_2CG_PELNY_ROZDZIAL.pdf`.
- Kontrola: 690/690 stron wyrenderowano PyMuPDF bez wyjątków; nowe strony 689–690 wyrenderowano osobno, stronę 689 obejrzano. Limit 99 MB spełniony. Niezależna recenzja matematyczna i pełna kontrola typograficzna pozostają otwarte.
- PDF pozostaje artefaktem rozmowy, repozytorium rejestruje postęp.

### Tom I PDF-first V21 — F28.2-CH (5 listopada 2026)
- Główny PDF `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V21.pdf`: **693 strony A4**, **9 190 016 B**, SHA-256 `0bb557b8c5078f4c05703bddf97fd502a487ceff7f3b5bd4cfd7c46114ca6fcd`.
- Zachowano 690 stron V20 i dodano 3 strony rozdziału F28.2-CH „Porządek wypukły i dominacja budżetów ogonowych”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych.
- Lokalny artefakt `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V21.pdf`; skrypt `build_ch.py`, rozdział `F28_2CH_PELNY_ROZDZIAL.pdf`.
- Kontrola: PyMuPDF wyrenderował 693/693 stron bez wyjątku; nowe strony 691–693 zapisano jako PNG. Limit 99 MB spełniony. Niezależna recenzja matematyczna i pełna kontrola typograficzna pozostają otwarte.
- PDF jest artefaktem rozmowy, repozytorium rejestruje postęp.

### Tom I PDF-first V22 — F28.2-CI (5 listopada 2026)
- Główny PDF: `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V22.pdf`; **696 stron A4**, **9 240 745 B**, SHA-256 `deaf494fdab3e459b4ebe2b95c460c024366383b17e2d154899cc2b357675408`.
- Zachowano 693 strony V21 i dodano 3 strony rozdziału F28.2-CI „Funkcja stop-loss: odzyskiwanie rozkładu i stabilność”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych.
- Artefakty lokalne: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V22.pdf`, `build_ci.py`, `F28_2CI_PELNY_ROZDZIAL.pdf`.
- Weryfikacja: 696/696 stron wyrenderowano PyMuPDF bez wyjątków; nowe strony 694–696 wyrenderowano osobno, wizualnie sprawdzono stronę 695. Limit 99 MB spełniony. Niezależna recenzja matematyczna i całościowa kontrola typograficzna pozostają otwarte.
- PDF udostępniony jako artefakt rozmowy, nie wgrany do GitHub.

### Tom I PDF-first V23 — F28.2-CJ (5 listopada 2026)
- Główny PDF: `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V23.pdf`; **698 stron A4**, **9 290 211 B**, SHA-256 `737c9c06759fadeb57afc7c5e198679d8d5c97b50d5620dee144edb9844d91ec`.
- Zachowano 696 stron V22 i dodano 2 strony rozdziału F28.2-CJ „Odtwarzanie rozkładu z dyskretnych cen stop-loss”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych. Udowodniono m.in. warunki zgodności nachyleń i błąd interpolacji ≤h/4.
- Artefakty: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V23.pdf`, `build_cj.py`, `F28_2CJ_PELNY_ROZDZIAL.pdf`.
- Kontrola: PyMuPDF wyrenderował 698/698 stron bez wyjątków; nowe strony 697–698 wyrenderowano osobno, stronę 697 sprawdzono wizualnie. Limit 99 MB spełniony. Niezależna recenzja matematyczna i pełny audyt typograficzny pozostają otwarte.
- PDF jest artefaktem rozmowy, repozytorium rejestruje postęp.

### Tom I PDF-first V24 — F28.2-CK (5 listopada 2026)
- Główny PDF: `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V24.pdf`; **701 stron A4**, **9 341 478 B**, SHA-256 `e0c18fb325633c99cb3a61a330bc131502485a599ba1cce5ec2f480b38972bf9`.
- Zachowano 698 stron V23 i dodano 3 strony rozdziału F28.2-CK „Przedziałowe ceny stop-loss i certyfikaty zgodności”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Uwzględniono test wykonalności, konstrukcję atomową i oszacowanie błędu interpolacji.
- Artefakty: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V24.pdf`, `build_ck.py`, `F28_2CK_PELNY_ROZDZIAL.pdf`.
- Weryfikacja: PyMuPDF wyrenderował 701/701 stron bez wyjątków; nowe strony 699–701 wyrenderowano osobno; stronę 700 sprawdzono wizualnie. Limit 99 MB spełniony. Niezależna recenzja matematyczna i pełna kontrola typograficzna pozostają otwarte.
- PDF jest artefaktem rozmowy, repozytorium rejestruje postęp.

### Tom I PDF-first V25 — F28.2-CL (5 listopada 2026)
- Główny PDF `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V25.pdf`: **703 strony A4**, **9 391 640 B**, SHA-256 `d9032de5da004c3a39e46566e6878855c8275d38b920189e20fb3296b65c1aac`.
- Zachowano 701 stron V24 i dodano 2 strony rozdziału F28.2-CL „Minimalna korekta sprzecznych cen stop-loss”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań.
- Artefakty: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V25.pdf`, `build_cl.py`, `F28_2CL_PELNY_ROZDZIAL.pdf`.
- Kontrola: 703/703 stron wyrenderowano PyMuPDF bez wyjątków; nowe strony 702–703 wyrenderowano osobno, stronę 703 sprawdzono wizualnie. Limit 99 MB spełniony. Niezależna recenzja matematyczna i pełny audyt typograficzny pozostają otwarte.
- PDF jest artefaktem rozmowy; repozytorium rejestruje postęp.

### Tom I PDF-first V26 — F28.2-CM (5 listopada 2026)
- PDF `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V26.pdf`: **706 stron A4**, **9 442 288 B**, SHA-256 `72baa25712ac14b595085f43e70936e21d9a33981ababfb649f437dd07a4c3d7`.
- Zachowano 703 strony V25 i dodano 3 strony rozdziału F28.2-CM „Stabilność funkcji stop-loss i certyfikaty transportowe”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań.
- Artefakty lokalne: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V26.pdf`, `build_cm.py`, `F28_2CM_PELNY_ROZDZIAL.pdf`.
- Weryfikacja: PyMuPDF wyrenderował 706/706 stron bez wyjątków; trzy nowe strony zapisano jako PNG, stronę 705 obejrzano wizualnie. Limit 99 MB spełniony. Niezależna recenzja matematyczna i całościowa kontrola typograficzna nadal otwarte.
- PDF pozostaje artefaktem rozmowy, repozytorium rejestruje postęp.

### Tom I PDF-first V27 — F28.2-CN (5 listopada 2026)
- PDF: `ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V27.pdf`, **709 stron A4**, **9 493 086 B**, SHA-256 `93255cc9394a1849cc11624775f9009a24debd3dce4a891794e042a215ef7350`.
- Zachowano 706 stron V26 i dodano 3 strony rozdziału F28.2-CN „Ostre ograniczenia funkcji stop-loss przy znanym nośniku”: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady i 6 zadań rozwiązanych. Omówiono bariery Jensena i siecznej, kryterium węzłowe i ostry błąd interpolacji h/4.
- Pliki robocze: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V27.pdf`, `build_cn.py`, `F28_2CN_PELNY_ROZDZIAL.pdf`.
- Kontrola: 709/709 stron wyrenderowano PyMuPDF bez wyjątku; nowe strony 707–709 zapisano jako PNG. Limit 99 MB spełniony. Niezależna recenzja matematyczna i pełna kontrola typograficzna pozostają otwarte.
- PDF jest artefaktem rozmowy, repozytorium rejestruje postęp.

### Tom I — F28.2-BW: ostre bariery budżetu ogonowego (5 listopada 2026)
- **Na `main`**: `manuscript/tom-i/F28_2BW.md` (commit `50c00d340a74dba76d79475559ef9fb614af921a`), `tests/test_f28_2bw.py` (commit `44768b190a47787ca7a30d1bf5202bc74b387f5f`). Materiał: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań.
- **Test lokalny**: 4830 przypadków dla rozkładów dwupunktowych w dokładnej arytmetyce wymiernej, PASS. Testuje `tm ≤ H(t) ≤ min(tb,m−(1−t)a)` i przykłady rozróżniające rozkłady. Nie stanowi niezależnej recenzji wszystkich dowodów.
- **Podgląd lokalny**: `/mnt/data/ontologia_run3/F28_2BW_PODGLAD.pdf`, 2 strony, 49 124 bajty, SHA-256 `1826ea27cfa5f1e1ea43fd592223dabb363cc6a066f4d6207d2dd92716996dc9`; wszystkie strony otwarte i wyrenderowane w PyMuPDF. Nie wgrano binarnego PDF do repozytorium.
- **Status**: bez integracji z rzeczywistym monolitem 0.20; kanoniczny licznik **585/1222 bez zmian**. Nie zmieniono historycznego wstępu, nie utworzono końcowego spisu treści, nie rozpoczęto Tomu II. Niezależna recenzja, pełne CI i integracja monolitu pozostają otwarte.

### Tom I — F28.2-BX: dyskretna wklęsłość i rekonstrukcja atomowa (5 listopada 2026)
- **Zapisano na `main`** manuskrypt `manuscript/tom-i/F28_2BX.md` (commit `22af57eff393386115a8ca60ba372fe8ed0fa5bc`), 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady i 6 zadań rozwiązanych; test `tests/test_f28_2bx.py` (commit `bdb85b2c623a01b06fb8b386dbb7b6ec8c34f741`).
- **Lokalny test matematyczny**: 55 080 kontroli w dokładnej arytmetyce wymiernej (Python, PASS); zweryfikowano monotoniczność nachyleń, średnią, rekonstrukcję węzłów i nierówność `0≤H−L≤(b−a)h/4` na siatce. Nie zastępuje to niezależnej recenzji dowodów.
- **Podgląd lokalny**: `/mnt/data/ontologia_bx/F28_2BX_PODGLAD.pdf` (2 strony A4, 28 103 B, SHA-256 `ad344c22c2cd4f60cfa73389577462a96b6837503588a39bf62e15d285b9ac6d`); obie strony wyrenderowano przez PyMuPDF. Podgląd PDF i lokalny wariant źródła nie są identyczne bajtowo z plikiem manuskryptu GitHub; binarnego PDF nie wgrano do repo.
- **Stan kanoniczny**: 585/1222 bez zmian — brak integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i dotychczasowe rozdziały niezmienione. Nie przygotowano końcowego spisu treści ani Tomu II. Pełne CI, niezależna recenzja matematyczna i audyt typograficzny nadal otwarte.

### Tom I — F28.2-BY: identyfikowalność atomów z budżetu ogonowego (5 listopada 2026)
- **Na `main`:** `manuscript/tom-i/F28_2BY.md` (commit `03aa6d9af48278a9cfbbe7f3e831df4276a8bdb9`), `tests/test_f28_2by.py` (commit `bf10c4e5622b55fb97498ceb1916ff6fd3ccaf81`). 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Wykazano związek maksymalnych odcinków afinicznych H z masami atomów i niestabilność detekcji atomu w W1.
- **Test lokalny:** `python test_f28_2by.py` — PASS, **4992 kontrole** w dokładnej arytmetyce wymiernej; sprawdzono monotoniczność, wklęsłość i nachylenia bloków atomowych. `python -m py_compile` — PASS. Nie stanowi niezależnej recenzji matematycznej.
- **Lokalny podgląd:** `/mnt/data/ontologia_by/F28_2BY_PODGLAD.pdf` — **2 strony A4**, **49 836 B**, SHA-256 `299dd2cbd692d7d5aebd5f422bad6e29b9819af914e94d3f5046b3f34c203bea`; obie strony wyrenderowane przez PyMuPDF. Podgląd opiera się na bardziej szczegółowym lokalnym wariancie tekstu i nie jest wierną kompilacją repozytoryjnego Markdown; zapis PDF do repo nie nastąpił.
- **Stan kanoniczny:** **585/1222 bez zmian**. Brak integracji z rzeczywistym monolitem 0.20; historyczny wstęp bez zmian, brak końcowego spisu treści i Tomu II. Otwarte: pełne CI, niezależna recenzja, audyt typograficzny i integracja.

### Tom I — F28.2-BZ: jednostronne pochodne i certyfikaty kwantylowe (5 listopada 2026)
- **Zapisane na `main`:** `manuscript/tom-i/F28_2BZ.md` (commit `3783fd2131a6027d85d4fea4752864153e4c9b7f`), `tests/test_f28_2bz.py` (commit `e94cef1edaba6d2ea6bcf319e1f251fef3558dd2`). Pięć twierdzeń z dowodami, trzy definicje, cztery kontrprzykłady i sześć rozwiązanych zadań.
- **Test lokalny:** Python, `fractions.Fraction`, PASS — 411 asercji dokładnych, obejmujących sieczne funkcji wklęsłej, jawne pochodne i granice błędu szumowego. Testy nie są niezależną recenzją dowodów ani pełnym CI.
- **Podgląd lokalny:** `/mnt/data/ontologia_bz/F28_2BZ_PODGLAD.pdf` — 2 strony A4, 6165 bajtów, SHA-256 `5392d8ead2111f1d4bb8da53c39a8b0cfb7c18b6098336f15c2c8748f4e09b9d`. Obie strony wyrenderowano PyMuPDF. PDF z rozszerzonego wariantu źródła lokalnego, nie jest wierną kompilacją repozytoryjnego Markdown; nie wgrano PDF do repo.
- **Status:** licznik kanoniczny **585/1222 bez zmian** — nie integrowano z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały niezmienione; bez końcowego spisu treści i Tomu II. Otwarte: integracja monolitu, pełne CI, niezależna recenzja matematyczna i audyt typograficzny.

### Tom I — F28.2-DO: kwantyle i budżet górnego ogona (5 listopada 2026)
- **Zapis na main:** `manuscript/tom-i/F28_2DO.md` — commit początkowy `efd2f9f16ee83bf7c3ca70948e1d985d457176a8`, korekta nieuzasadnionego T4 i zastąpienie go poprawnym twierdzeniem — commit `9f85b27d9aae1a6c4649d50d66ca6866a8648259`; `tests/test_f28_2do.py` — commit `0d004bad3215366e1faae76ecb317ddaf4ac167a`.
- **Zakres:** 3 definicje, 4 twierdzenia z dowodami, 3 kontrprzykłady i 4 zadania rozwiązane. Odtwarzanie kwantyla z pochodnej H, tożsamość W1 dla pochodnych, oszacowanie W1 dla interpolacji siatkowej, niejednoznaczność pomiarów krańcowych.
- **Test wykonany lokalnie:** niezależny skrypt `/mnt/data/ontologia_do/check.py` — PASS, 37 dokładnych asercji na liczbach wymiernych. Test repozytoryjny `tests/test_f28_2do.py` zapisano, ale jego uruchomienie w CI **niepotwierdzone**.
- **Podgląd PDF:** `/mnt/data/ontologia_do/F28_2DO_PODGLAD.pdf` — 1 strona A4, 25 596 B, SHA-256 `9b0e5d6dacabbed77df4f49a517984f155f837ca2831b69be70a4197e6bfb201`; render PyMuPDF PASS. Podgląd jest skróconą lokalną redakcją, nie wierną kompilacją repozytoryjnego Markdown; nie zapisano binarnego PDF w repo.
- **Status:** kanoniczne **585/1222 bez zmian**. Brak integracji z monolitem 0.20, historyczny wstęp bez ingerencji, bez końcowego spisu treści i bez Tomu II. Pełne CI, niezależna recenzja i weryfikacja integracyjna pozostają otwarte.


### Tom I — F28.2-DP: rekonstrukcja kwantylowa i ostry błąd transportowy (5 listopada 2026)
- **Zapisane na main:** `manuscript/tom-i/F28_2DP.md` — commit `0a41fa785be9d52df7ce917216867c96c46a3a66`; `tests/test_f28_2dp.py` — commit `23245d6e4b9ec76337082fbde73b9a5cfb828966`.
- **Zakres:** 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Ostre oszacowanie `W1(μ,μ_P)≤(b−a)h/2` i stabilność na błędy średnich komórkowych.
- **Test lokalny:** Python `fractions.Fraction`, PASS, 758 asercji w wariancie roboczym (test repozytoryjny zawiera podzbiór tych kontroli; jego wykonanie w CI niepotwierdzone). Uwaga: wariant roboczy zawiera dodatkowe kontrole monotoniczności; kod testu repozytoryjnego zapisano osobno.
- **Podgląd lokalny:** `/mnt/data/ontologia_dp/F28_2DP_PODGLAD.pdf` — 2 strony A4, 29 766 B, render PyMuPDF 2/2 PASS. Podgląd wygenerowany z pełniejszej lokalnej redakcji, nie jest wierną kompilacją pliku z repozytorium. Binarnego PDF nie wgrano do GitHub.
- **Stan kanoniczny:** 585/1222 bez zmian; brak integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i dotychczasowe rozdziały niezmienione; nie utworzono końcowego spisu treści ani Tomu II. Otwarte: pełne CI, niezależna recenzja matematyczna i audyt typograficzny.

### Aktualizacja PDF Tom I — V28 i V29 (2026-11-05)
- V28: 711 stron, 9 542 773 B; F28.2-CO „Spready stop-loss i identyfikacja masy w przedziałach”; SHA-256 `f3a0c3709210dd6ddf7bc8b0e62c628b54eb4d9a96bd8c7de4dba90d9f243c04`.
- V29: 713 stron, 9 593 065 B; F28.2-CP „Stabilna rekonstrukcja dystrybuanty z zaszumionych cen stop-loss”; SHA-256 `0dff942bf32ca95de0a912c1129f8432d1cdffa926e0092f5218cfd912a032d4`.
- Główny PDF V29: `/mnt/data/ontologia_aktualizacja/ONTOLOGIA_LICZBY_TOM_I_AKTUALIZACJA_2026-11-05_V29.pdf`. Zachowano 711 stron V28 i dołączono dwie strony F28.2-CP. Test PyMuPDF: 713/713 stron bez błędów; strona 713 obejrzana. Limit 99 MB spełniony.
- To zapis lokalnej redakcji PDF; nie potwierdza umieszczenia binarnego PDF w repozytorium ani zastąpienia odrębnego monolitu repozytoryjnego. Niezależna recenzja matematyczna i audyt typograficzny nadal otwarte.

### Tom I — F28.2-DQ: kwantylowa aproksymacja komórkowa (2026-11-05)
- **Zapis na main:** `manuscript/tom-i/F28_2DQ.md` commit `8fdbf3c855ac10757b0b661412c8a3cd1bf8d8cf`; `tests/test_f28_2dq.py` commit `bff6f0ee856c09a30303a38340063c709f754616`.
- **Zakres:** 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych. Oszacowanie `W1(μ,μ_P)≤ΣΔᵢdᵢ/2≤(b−a)h/2`, ostrość, zachowanie średniej, stabilność szumowa, test funkcji Lipschitza.
- **Lokalne sprawdzenie:** `python test_f28_2dq.py` PASS (501 kontroli raportowanych przez skrypt); `python -m py_compile` PASS. Testy algebraiczne nie stanowią pełnej weryfikacji dowodów.
- **PDF lokalny:** `/mnt/data/ontologia_dq/F28_2DQ_PODGLAD.pdf`, 2 strony A4, 29204 B, SHA-256 `7edc10447ae5e5cf83c2df9fa23cf5074b536a17da09a5136618c0684da29b86`; PyMuPDF wyrenderował 2/2 stron. PDF pochodzi z lokalnego, nieidentycznego bajtowo wariantu manuskryptu; nie jest kompilacją GitHub 1:1 ani nie został wgrany do repozytorium.
- **Stan kanoniczny:** 585/1222 bez zmian. Brak integracji z monolitem 0.20. Historyczny wstęp i dotychczasowe rozdziały bez zmian. Brak końcowego spisu treści i Tomu II. Otwarte: pełne CI, niezależna recenzja matematyczna, audyt typograficzny.

### Tom I — F28.2-DR: kwantyzacja kwantylowa w metryce kwadratowej (2026-11-05)
- **Zapis na main:** `manuscript/tom-i/F28_2DR.md`, commit `26d5f76219d0d2aa08ec2b76651c45b76f169cb4`; `tests/test_f28_2dr.py`, commit `92bfc48115981aac230585c77c8dddb2d880d1f0`.
- **Zakres:** 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych. Tożsamość `W₂²=ΣEᵢ`, certyfikat `W₂²≤ΣΔᵢdᵢ²/4≤h(b−a)²/4`, zachowanie średniej, dekompozycja drugiego momentu i stabilność przy monotonicznych zakłóceniach.
- **Weryfikacja lokalna:** `python test_f28_2dr.py` — PASS, 5350 dokładnych asercji wymiernych. Nie oznacza to formalnej weryfikacji wszystkich dowodów ani wykonania CI.
- **Podgląd lokalny:** `/mnt/data/ontologia_dr/F28_2DR_PODGLAD.pdf`; 2 strony A4, 29 380 B, SHA-256 `8d170b5cfb517d4bb07b036156ef9b8bd2db7cdad90ef7c4d365d252f78915e8`; render PyMuPDF 2/2. Lokalny wariant redakcyjny PDF nie jest wierną kompilacją GitHub 1:1 i nie został wgrany do repozytorium.
- **Stan kanoniczny:** 585/1222 bez zmian, ponieważ brak integracji z rzeczywistym monolitem 0.20. Historyczny wstęp nietknięty; brak końcowego spisu treści i Tomu II. Otwarte: pełne CI, niezależna recenzja matematyczna, integracja i audyt typograficzny.

### Tom I — F28.2-DS: hierarchia metryk transportowych (2026-11-05)
- Na gałęzi main: `manuscript/tom-i/F28_2DS.md`, commit `a88bce2abf1e37ce6eda6de0ac8d770b221516ad`; `tests/test_f28_2ds.py`, commit `052cf27241fd234f6a8dbdca5fc1dfe86567aae7`.
- Zakres: 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Wyniki: W₁≤W₂, W₂²≤D W₁, certyfikat kwantyzacji W₂²≤hD²/4, kontrakcja uśredniania komórkowego.
- Weryfikacja lokalna: 1109 asercji w dokładnej arytmetyce wymiernej PASS; kompilacja testu Python PASS. Nie wykonano niezależnej recenzji ani pełnego CI.
- Brak integracji z rzeczywistym monolitem 0.20: licznik kanoniczny 585/1222 bez zmian. Historyczny wstęp i dotychczasowe rozdziały niezmienione; brak końcowego spisu treści i Tomu II.


### Tom I — F28.2-DT: kwantyzacja medianowa W1 (2026-11-05)
- **Zapis na main:** `manuscript/tom-i/F28_2DT.md` — commit `805cbbd77a2985884c6288ead79e0677891e8550`; `tests/test_f28_2dt.py` — commit `ddc92d2fc48c02cfbe46476d4f87da5b8fef49eb`.
- **Zakres:** 3 definicje, 4 twierdzenia z dowodami, 4 kontrprzykłady i 6 rozwiązanych zadań. Mediana komórkowa minimalizuje błąd L1; ostry certyfikat `W1 ≤ (1/2) Σ Δ_i d_i ≤ h(b-a)/2`; stabilność dla normy supremum i kontrprzykład nieciągłości operatora próbkowania w L1.
- **Test lokalny:** `python test_f28_2dt.py` — PASS, **78 164** asercje w arytmetyce wymiernej (test enumeracyjny na dyskretnych niemalejących kwantylach). Pełne CI i niezależna recenzja dowodów niepotwierdzone.
- **Podgląd lokalny:** `/mnt/data/ontologia_dt/F28_2DT_PODGLAD.pdf`, 1 strona A4, SHA-256 `8f75e4ab6ffa7ce1a0ed6d991098055b84093321eb1a09d31c51242138f16bf6`, render PyMuPDF PASS. To skrócony podgląd, **nie** wierna kompilacja repozytoryjnego manuskryptu; binarny PDF nie został umieszczony w repozytorium.
- **Stan kanoniczny:** **585/1222 bez zmian**, bez integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsza treść niezmienione. Bez końcowego spisu treści i Tomu II.


### Tom I — F28.2-DU: projekcje kwantylowe na zagnieżdżonych partycjach (2026-11-05)
- **Na main:** `manuscript/tom-i/F28_2DU.md` commit `efd8a2060950a890545cdb21dc71f1848a1324bb`; `tests/test_f28_2du.py` commit `8913da7eca34c4e8149ff63b10db04b09b70236c`.
- **Zakres:** 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych. Dokładny bilans Pitagorasa dla W2 przy zagnieżdżonych partycjach, monotoniczność błędu, certyfikat zbieżności i dekompozycja wariancji.
- **Weryfikacja:** test regresyjny zapisano w repozytorium; jego wykonanie w CI i pełna kompilacja PDF **niepotwierdzone**. Materiał wymaga niezależnej recenzji matematycznej.
- **Kanoniczny licznik:** 585/1222 bez zmian; bez integracji z rzeczywistym monolitem 0.20, bez ingerencji w historyczny wstęp, bez końcowego spisu treści i bez Tomu II.


### Tom I — F28.2-DV: dokładny zysk adaptacyjnego rozszczepienia (2026-11-05)
- **Zapis na main:** `manuscript/tom-i/F28_2DV.md` — commit `ebac4b9abe8d03e3e19c0f9cf4cba10afc2d7acb`; `tests/test_f28_2dv.py` — commit `3f77d785e9f0572df1fa99bb7b88bf90ad308796`.
- **Zakres:** 2 definicje, 4 twierdzenia z dowodami, 4 kontrprzykłady i 6 rozwiązanych zadań. Zysk rozszczepienia `G=(w_L*w_R/(w_L+w_R))*(m_L-m_R)^2`, dokładny spadek W2², ostra bariera i optymalność pojedynczego kroku.
- **Weryfikacja lokalna:** Python fractions.Fraction — PASS, 2100 dokładnych asercji dla niemalejących sześciopunktowych kwantyli; py_compile PASS. Pełne CI i niezależna recenzja niepotwierdzone.
- **Podgląd PDF:** `/mnt/data/ontologia_dv/F28_2DV_PODGLAD.pdf`, 1 strona A4, SHA-256 `9b6ac3b813f283da2d1657099ab61595bd6a6fd6b94cd233f79210f3172c78a1`, render PyMuPDF PASS. To skrócona redakcja lokalna, nie wierna kompilacja GitHub 1:1; binarny PDF nie jest zapisany w repozytorium.
- **Stan kanoniczny:** 585/1222 bez zmian, brak integracji z monolitem 0.20. Nie zmieniono historycznego wstępu ani wcześniejszych rozdziałów, nie utworzono końcowego spisu treści ani Tomu II.


### Tom I — F28.2-DW: certyfikat zatrzymania adaptacyjnej kwantyzacji (2026-11-05)
- **Na main:** `manuscript/tom-i/F28_2DW.md` — commit `8ea0ad8babf26bb96d2438191fec993e0cd7994b`; `tests/test_f28_2dw.py` — commit `16c8a54a72ca5ba690c22f73c99ff9877910074c`.
- **Zakres:** 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Dokładny certyfikat błędu W₂²≤Σw_I(B_I−A_I)²/4, formuła zysku rozszczepienia, bezpieczne zatrzymanie i zbieżność przy drobniejącej siatce.
- **Weryfikacja:** niezależny lokalny skrypt Python z `fractions.Fraction` wykonał 420 kontroli tożsamości zysku i 84 kontrole certyfikatu — PASS. Test zapisany na main zawiera również kontrolę przypadku liniowego; wykonanie tego pliku w GitHub Actions niepotwierdzone. Testy nie zastępują recenzji matematycznej.
- **Integracja:** brak dostępu do rzeczywistego monolitu 0.20; licznik **585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały bez ingerencji. Bez końcowego spisu treści i bez Tomu II.


### Tom I — F28.2-DX: zbieżność certyfikatów dyadycznych (2026-11-05)
- **Zapis na main:** `manuscript/tom-i/F28_2DX.md` commit `5a292c97f476f43541621662fb59e555bbea736c`; `tests/test_f28_2dx.py` commit początkowy `7ad42b7e3144509b5621697b255a3cec215d3d6b`, poprawka formuły testu `a5c819faac21f9b818d6fa513111e86206cde558`.
- **Zakres:** 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Zbieżność dyadycznych projekcji kwantylowych, bilans energii, ograniczenia zakresowe i stabilność.
- **Weryfikacja lokalna:** 826 asercji w dokładnej arytmetyce wymiernej (lokalny odpowiednik testu), PASS. Pierwsza wersja testu miała niepoprawną formułę dla poziomu refinacji i została poprawiona w osobnym commicie. CI i niezależna recenzja matematyczna niepotwierdzone.
- **PDF:** lokalny skrócony podgląd `/mnt/data/ontologia_dx/F28_2DX_PODGLAD.pdf`, 1 strona A4, 25 661 B, SHA-256 `93aeeb859886ac4597abacb865dec7b3f9eaf80f30791f55e4879a6f2123afec`, render PyMuPDF PASS. Nie jest to pełna kompilacja Markdown ani integracja monolitu.
- **Stan kanoniczny:** 585/1222 bez zmian; monolit 0.20 nie został zmodyfikowany. Historyczny wstęp i wcześniejsze rozdziały bez ingerencji. Bez końcowego spisu treści i bez Tomu II.


### Tom I — F28.2-DY: dwustronne certyfikaty błędu kwantyzacji (2026-11-05)
- **Na main:** `manuscript/tom-i/F28_2DY.md`, commit `75de05e755bf13af4ff9431ff79a6813f394bc7c`; `tests/test_f28_2dy.py`, commit `dfc482e5d72eae35d7311f6d2af6ea1d39a7afaa`.
- **Zawartość:** 3 definicje, 6 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Wynik: `B_P <= E_P = W2²(mu,mu_P) <= C_P`, gdzie `B_P=E_P-E_R` jest mierzalnym zyskiem refinacji. Wykazano, że nie istnieje dodatnie uniwersalne dolne oszacowanie `E_P >= c C_P`.
- **Weryfikacja lokalna:** niezależnie od pliku GitHub uruchomiono odpowiednik enumeracyjnego testu w `fractions.Fraction`: **790 przypadków, 1580 dokładnych asercji PASS**. Nie uruchomiono bezpośrednio pobranego testu z repozytorium (brak DNS do raw.githubusercontent.com), a GitHub Actions CI niepotwierdzone.
- **Podgląd PDF:** lokalny skrót redakcyjny `/mnt/data/ontologia_dy/F28_2DY_PODGLAD.pdf`, 1 strona A4, 2984 B, SHA-256 `5d621be1d5f6b52a33119e2632038dc046572d9f3c036aa8e65adb2e2947a881`. Poprawnie otwarty i wyrenderowany w PyMuPDF. **Nie jest wierną kompilacją pełnego manuskryptu** i nie został umieszczony na GitHub.
- **Ograniczenia:** niezależna recenzja matematyczna, pełne CI, wierna kompilacja źródła i integracja z rzeczywistym monolitem 0.20 nadal otwarte. Historyczny wstęp i wcześniejsza treść niezmienione; bez końcowego spisu treści i bez Tomu II. Kanoniczny licznik **585/1222 bez zmian**.


### Tom I — F28.2-DZ: certyfikaty a posteriori z hierarchii projekcji (2026-11-05)
- **Zapis na main:** `manuscript/tom-i/F28_2DZ.md` — commit `8f29d176794a471e8c7f069e8fe9b3918556b113`, korekta zapisu wykładników `bbe57768f0e605d20d1afcb8208f6c2e02d249c3`; `tests/test_f28_2dz.py` — commit `c540f4455ed7b4f484ec0fd487932153d2752d02`.
- **Zakres:** 4 twierdzenia z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych. Dokładny ogon energii E(P_n)=Σ_{k≥n}D_k, przedziałowy certyfikat po skończonej refinacji, niemożność oszacowania reszty przez pojedynczy przyrost.
- **Weryfikacja:** przygotowano test w arytmetyce wymiernej; jego wykonanie lokalne i CI **niepotwierdzone** z powodu błędu narzędzia wykonawczego. Kompilacja PDF **nieprzeprowadzona** z tej samej przyczyny. Nie przypisywać statusu PASS.
- **Stan:** kanoniczny licznik 585/1222 bez zmian; brak integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały niezmienione. Bez końcowego spisu treści i bez Tomu II. Otwarta niezależna recenzja matematyczna.


### Tom I — F28.2-EA: zachłanna refinacja kwantylowa (2026-11-05)
- **Zapis na main:** `manuscript/tom-i/F28_2EA.md` commit `dd7b3db6adc3a8ee2692010b5e5c05f0aa32e30e`, korekta kontrprzykładu `1398eb1c52fa08d14209b22f44ec84119f5b95a3`; `tests/test_f28_2ea.py` commit `bb30da3575f9c91ce23bdb9614a9f296a285bffb`.
- **Zakres:** 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Lokalna optymalność maksymalnego zysku, skończona terminacja, ograniczenie zakresowe, rekurencja dynamicznego programowania oraz jawny kontrprzykład globalnej optymalności zachłannej dla `(0,0,1,2,4)`: `2/15 > 1/10`.
- **Weryfikacja lokalna:** niezależny skrypt `/mnt/data/ontologia_ea/test_f28_2ea.py` — **PASS, 4527 asercji** w dokładnej arytmetyce wymiernej. Test zapisany w GitHub obejmuje również kontrprzykład; jego uruchomienie w GitHub Actions niepotwierdzone.
- **Podgląd PDF:** lokalny `/mnt/data/ontologia_ea/F28_2EA_PODGLAD.pdf`, 1 strona A4, 24516 B, SHA-256 `4c9c129dc1c69b51861371d2137c7b3b923fc6a2ac5e1a5daebac1393c2b4419`, otwarcie i render PyMuPDF PASS. Jest to **skrócony podgląd**, nie wierna kompilacja całego manuskryptu i nie został umieszczony w repo.
- **Stan:** kanoniczne **585/1222 bez zmian**; brak integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały niezmienione. Bez końcowego spisu treści i bez Tomu II. Pełne CI, niezależna recenzja i audyt typograficzny nadal otwarte.


### Tom I — F28.2-EB: dokładne programowanie dynamiczne kwantyzacji (2026-11-05)
- **Na main:** `manuscript/tom-i/F28_2EB.md`, commit `d277ba0aab6a8249d9fe0722d165bda620577d02`; `tests/test_f28_2eb.py`, commit `5cb4e51bcb6631c504a18b78feeb293b4120d722`.
- **Zakres:** definicja kosztu, 5 twierdzeń z dowodami, 4 kontrprzykłady i 6 rozwiązanych zadań. Dokładna rekurencja optimum globalnego dla kolejnych komórek, koszt z sum prefiksowych, monotoniczność i złożoność O(kn²).
- **Lokalna weryfikacja:** odpowiednik testu wykonano w Pythonie z fractions.Fraction: PASS, 2180 dokładnych asercji; py_compile PASS. Wykonanie testu repozytoryjnego w CI niepotwierdzone.
- **PDF:** lokalny podgląd pełnego zakresu redakcyjnego `/mnt/data/ontologia_eb/F28_2EB_PODGLAD.pdf`, 2 strony A4, SHA-256 `733fa75175ddff354f5f33e1f83640dd59ed629348fd153538f85048b5424389`, otwarcie i render PyMuPDF PASS. PDF przygotowano z lokalnego wariantu, nie jest wierną kompilacją bajtową manuskryptu GitHub.
- **Stan:** 585/1222 bez zmian; brak integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsza treść niezmienione. Bez końcowego spisu treści i Tomu II. CI, niezależna recenzja i audyt typograficzny otwarte.


### Tom I — F28.2-EC: nierówność Monge'a i monotoniczność cięć (2026-11-05)
- **Manuskrypt na main:** `manuscript/tom-i/F28_2EC.md`, commit `01c8cb99cff10f1a2e5eb7ad6ea3c4a9a100d19f`.
- **Test na main:** `tests/test_f28_2ec.py`, commit `e8e937e0809cd0d20add002ebce1d747ea1384cc`.
- **Zakres:** 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady i 6 zadań z rozwiązaniami. Ważony koszt przedziału, wariacyjność średniej, wzór złączenia, nierówność Monge'a, monotoniczność najmniejszego minimalizatora w dynamicznym programowaniu i bezpieczne zawężanie zakresu poszukiwań.
- **Lokalna kontrola niezależna:** `/mnt/data/ontologia_ec/check.py`, dokładna arytmetyka `fractions.Fraction`: **5726 kontroli PASS**; obejmuje Monge'a, monotoniczność punktów cięcia i porównanie optimum DP z pełną enumeracją dla małych uporządkowanych próbek. **Nie jest to wykonanie pobranego pliku testowego z GitHub ani niezależna recenzja dowodów.**
- **Podgląd lokalny PDF:** `/mnt/data/ontologia_ec/F28_2EC_PODGLAD.pdf`, 2 strony A4, 25381 bajtów, SHA-256 `595a0ac71ad04818b4eb261f605a147e426166987de729b9f837b4a0eff42f4e`, otwarcie i render PyMuPDF poprawne. To **skrócona redakcja**, nie wierna kompilacja całego manuskryptu GitHub.
- **Ograniczenia:** CI GitHub niepotwierdzone; brak niezależnej recenzji matematycznej; brak integracji z rzeczywistym monolitem 0.20. Wcześniejsza treść i historyczny wstęp nietknięte. **Kanoniczny licznik 585/1222 bez zmian**, bez końcowego spisu treści i bez Tomu II.


### Tom I — F28.2-ED: algorytm dziel i zwyciężaj (2026-11-05)
- **Manuskrypt na main:** `manuscript/tom-i/F28_2ED.md`, commit `2beae7d99b9d39a8bb0692e6329b460097753404`.
- **Test na main:** `tests/test_f28_2ed.py`, commit `ada6e99f1a7f7fabd9507b0e74c7371f550500ca`.
- **Zakres:** 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady i 6 zadań z rozwiązaniami. Rekurencja Bellmana, nierówność Monge'a, monotoniczność najmniejszego minimalizatora, algorytm dziel i zwyciężaj O(kn log n).
- **Weryfikacja lokalna:** wykonano `python /mnt/data/ontologia_ed/test_f28_2ed.py`: PASS, 49 003 dokładne asercje wymierne; `python -m py_compile`: PASS. Skrypt lokalny jest równoważny treści testu zapisanego na GitHub, ale nie został pobrany z GitHub; GitHub Actions CI niepotwierdzone.
- **PDF:** lokalny skrócony podgląd `/mnt/data/ontologia_ed/F28_2ED_PODGLAD.pdf`, 1 strona A4, 24 138 bajtów, SHA-256 `394601033e1ab3db375b5d806b12c12d9b489c2a0d8593d68b6a466cdb67beb4`. PyMuPDF otwarcie i render 1/1 PASS. To nie jest wierna kompilacja całego manuskryptu; nie zapisano PDF na GitHub.
- **Otwarte:** niezależna recenzja dowodów, pełne CI, integracja z rzeczywistym monolitem 0.20 i audyt typograficzny. Historyczny wstęp i wcześniejsze rozdziały niezmienione. **Kanoniczny licznik 585/1222 bez zmian**; bez końcowego spisu treści i bez Tomu II.


### Tom I — F28.2-EE: audyt algorytmu dziel i zwyciężaj (2026-11-06)
- **Na main:** `manuscript/tom-i/F28_2EE.md`, commit `ea83800a54ea900432f16cf5ad92a4af87f949a6`; `tests/test_f28_2ee.py`, commit `8a393bb43525e4f3215d816649bde76167a318d5`.
- **Zakres:** 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych. Koszt blokowy, rekonstrukcja świadka, kryterium różnicowe, niezmienniczość afiniczna i granice testowania.
- **Lokalna weryfikacja:** `python -m py_compile /mnt/data/ontologia_ee/check.py` PASS; `python /mnt/data/ontologia_ee/check.py` PASS: **77 328 asercji wymiernych**, porównanie referencyjnego DP i przyspieszonego divide-and-conquer, kontrola dopuszczalności i kosztu świadka. Jest to **lokalny odpowiednik**, nie uruchomienie pobranego z GitHub `tests/test_f28_2ee.py` (DNS raw.githubusercontent.com niedostępny). GitHub Actions CI niepotwierdzone.
- **Podgląd PDF:** `/mnt/data/ontologia_ee/F28_2EE_PODGLAD.pdf`, 1 strona A4, SHA-256 `86b8931f71b0371dbac90d74b5123e59cfb125f0fea278a70e3a31a34e933585`; otwarcie i render PyMuPDF PASS. Skrócona redakcja, nie wierna kompilacja pełnego manuskryptu GitHub; PDF nie jest zapisany w repozytorium.
- **Stan:** 585/1222 bez zmian; brak integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały niezmienione. Bez końcowego spisu treści i bez Tomu II. Niezależna recenzja matematyczna i pełne CI pozostają otwarte.


### Tom I — F28.2-EF: stabilność podziałów i certyfikat luki (2026-11-06)
- Na main: `manuscript/tom-i/F28_2EF.md` commit `e1302690eb3d5643b881133248ca0aa4af3aab1b`; `tests/test_f28_2ef.py` commit `7dabb3a261c0557e972b41567ad609745292f6ec`.
- Zakres: 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady i 6 rozwiązanych zadań. Jednostajny certyfikat `|E_y(P)-E_x(P)| <= 4WRδ+4Wδ²`, stabilność optimum i wystarczający warunek zachowania cięcia `γ>2K`.
- Weryfikacja lokalna: skrypt Python fractions.Fraction PASS, 17 841 dokładnych asercji; py_compile PASS. Wykonanie repozytoryjnego testu w CI niepotwierdzone.
- Podgląd lokalny: `/mnt/data/ontologia_ef/F28_2EF_PODGLAD.pdf`, 2 strony A4, SHA-256 `a57fb9bda675d0691b2373fad00d840d3f82c70b5a3786b59ff8676b5732d71a`, render 2/2. To lokalna redakcja, nie bajtowo wierna kompilacja GitHub.
- Kanoniczny licznik **585/1222 bez zmian**; bez integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejszy manuskrypt bez zmian. Bez końcowego spisu treści i bez Tomu II. CI i niezależna recenzja pozostają otwarte.


### Tom I — F28.2-EG: ostre certyfikaty stabilności ważonej (2026-11-06)
- **Zapis na main:** `manuscript/tom-i/F28_2EG.md`, commit `bdf56c55ae47cd1f91714391411f97ed4b376496`; `tests/test_f28_2eg.py`, commit `f97bc3db3b6917551a4d5d2905041382f1ba1528`.
- **Zakres:** definicje kosztu i luki, 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Ostry certyfikat `|sqrt(E_x(P))-sqrt(E_y(P))| <= ||x-y||_w`, stabilność pierwiastka optimum oraz kryterium zachowania jednoznacznego cięcia `gamma>2d(2||x||_w+d)`.
- **Weryfikacja lokalna:** niezależny odpowiednik testu w `/mnt/data/ontologia_eg/verify.py` — 44 352 dokładne kontrole wymierne PASS, `py_compile` PASS. **Nie jest to wykonanie pliku pobranego z repozytorium** (DNS raw.githubusercontent.com niedostępny); GitHub Actions CI niepotwierdzone.
- **Podgląd PDF:** `/mnt/data/ontologia_eg/F28_2EG_PODGLAD.pdf`, 1 strona A4, SHA-256 `052a2d7ab260677cc923d31701a1941f9aa8312f23e3a5b06e2e77b69649428a`; PyMuPDF otwarcie i render PASS. Skrócony podgląd, nie pełna kompilacja repozytoryjnego manuskryptu.
- **Stan:** 585/1222 bez zmian, brak integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsze rozdziały niezmienione; bez końcowego spisu treści i Tomu II. Pełne CI i niezależna recenzja otwarte.


### Tom I — F28.2-EH: parowe certyfikaty stabilności (2026-11-06)
- **Manuskrypt na main:** `manuscript/tom-i/F28_2EH.md`, commit finalnej treści `d84bceee769a13b5acaebeb1a5fbd9a9be74ac86` (poprzedni commit `45e78ebade52b6c673cfe2ccfc84510218d3b5f2` zawierał wyłącznie tymczasową treść, zastąpioną w całości).
- **Test na main:** `tests/test_f28_2eh.py`, commit `5dcc63d445bd044cc624fdd8481fc657028eb6cd`.
- **Zakres:** 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych. Dokładna tożsamość perturbacyjna różnicy kosztów, norma różnicy rzutów ≤1, parowy certyfikat zachowania jednoznacznego optimum i konieczne oraz wystarczające kryterium dla konkretnego zaburzenia.
- **Weryfikacja lokalna:** `python /mnt/data/ontologia_eh/test_f28_2eh.py` — PASS, **20 414** dokładnych asercji wymiernych; `python -m py_compile` PASS. Jest to lokalny odpowiednik testu na GitHub, a nie wykonanie pliku pobranego z repozytorium. Pierwsza próba z szerszą enumeracją przekroczyła limit czasu; zakres ograniczono do n=3,4.
- **PDF:** lokalny `/mnt/data/ontologia_eh/F28_2EH.pdf`, 2 strony A4, wygenerowany z lokalnego Markdown przez ReportLab; nie jest wiernym typograficznie renderem matematycznym (wzory pozostają zapisem tekstowym). Plik nie został umieszczony na GitHub.
- **Ograniczenia:** pełne GitHub Actions CI i niezależna recenzja matematyczna niepotwierdzone. Nie integrowano z rzeczywistym monolitem 0.20; **licznik 585/1222 bez zmian**. Historyczny wstęp i wcześniejsze rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.


### Tom I — F28.2-EI: kierunkowe promienie stabilności (2026-11-06)
- **Manuskrypt na main:** `manuscript/tom-i/F28_2EI.md`, commit `05ce2566be991bde84b33233c54455374a6fc0f9`.
- **Test na main:** `tests/test_f28_2ei.py`, commit `b50410c3ad57982eb3d9516cb8c0d86bc75c4330`.
- **Zakres:** 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Dokładna kwadratowa tożsamość luki wzdłuż kierunku, pierwszy punkt remisu, stabilność ścisłego optimum, niezmienniczość afiniczna i dolny certyfikat promienia.
- **Lokalne testy:** niezależnie przygotowany `/mnt/data/ontologia_ei/test_f28_2ei.py` — PASS, 137700 dokładnych tożsamości wymiernych i 3 kontrole brzegowe; `py_compile` PASS. Test repozytoryjny nie został uruchomiony z pobranego GitHub pliku, GitHub Actions CI niepotwierdzone.
- **PDF:** lokalny `/mnt/data/ontologia_ei/F28_2EI_PODGLAD.pdf`, 2 strony A4, SHA-256 `17cee86ce85852bbf8bfe8fd8065d45cc36f8e5ab270f0a7f98633e35134ee81`; render 2/2 PASS. Jest to podgląd z lokalnego pełnego wariantu, a nie wierna kompilacja pliku GitHub.
- **Stan:** 585/1222 bez zmian; brak integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsza treść niezmienione; bez końcowego spisu treści i bez Tomu II. Niezależna recenzja matematyczna oraz CI nadal otwarte.


### Tom I — F28.2-EJ: promień zgodności porządku i pierwszy remis (2026-11-06)
- **Na main:** `manuscript/tom-i/F28_2EJ.md` commit `da83a8d841b22570775a8baf532b1593793e0e77`, poprawka przykładu `cca580f668806a87c6130320a5710ca79ade2a6b`; `tests/test_f28_2ej.py` commit `a2caff185cd49ab126eeb572f2ba446ce78f9390`.
- **Zakres:** 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych. Dokładna bariera zachowania uporządkowania x+th oraz pierwszy remis konkurencyjnego podziału, z rozróżnieniem remisu i granicy porządku.
- **Weryfikacja lokalna:** niezależny odpowiednik testu `/mnt/data/ontologia_ej/check.py`: PASS, 49 815 dokładnych asercji wymiernych, `py_compile` PASS. To nie jest wykonanie pliku pobranego z GitHub; CI niepotwierdzone.
- **PDF:** lokalny skrócony podgląd `/mnt/data/ontologia_ej/F28_2EJ_PODGLAD.pdf`, 1 strona A4, SHA-256 `32147c6906a5d7e9e8addd18d236207ca2518f4151447ff720e2d88062a21948`; otwarcie i render PyMuPDF PASS. Nie jest wierną kompilacją całego manuskryptu.
- **Stan:** 585/1222 bez zmian, brak integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsza treść bez zmian; bez końcowego spisu treści i Tomu II. Niezależna recenzja matematyczna oraz pełne CI otwarte.


### Tom I — F28.2-EK: komórki stabilności i wielokrotne remisy (2026-11-06)
- **Manuskrypt na main:** `manuscript/tom-i/F28_2EK.md`, commit `8c9d9a97242da13b5c613e130f9a1760998c2c2a`.
- **Test na main:** `tests/test_f28_2ek.py`, commit `b0ac9f888b78b12b6b09a56c3525e44b0aa45950`.
- **Zakres:** definicje zbioru aktywnego, punktu przełączenia i remisu stycznego; 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 rozwiązanych zadań. Klasyfikacja kandydatów na przełączenia przez pierwiastki różnic kwadratowych kosztów.
- **Weryfikacja lokalna:** `python -m py_compile` PASS; niezależny lokalny skrypt `/mnt/data/ontologia_ek/test_f28_2ek.py` PASS — 55 728 dokładnych tożsamości wymiernych. To nie jest uruchomienie pobranego pliku repozytoryjnego. GitHub Actions CI i niezależna recenzja matematyczna niepotwierdzone.
- **PDF:** lokalny skrócony podgląd `/mnt/data/ontologia_ek/F28_2EK_PODGLAD.pdf`, 1 strona, SHA-256 `ae4ac81285a58d64c9bc66554ec6412b7f4b14718b4d35aeb26da88ad98d4e0f`; PyMuPDF otwarcie i render PASS. Nie jest wierną kompilacją pełnego manuskryptu; nie zapisano go na GitHub.
- **Stan:** kanoniczne 585/1222 bez zmian; brak integracji z rzeczywistym monolitem 0.20. Historyczny wstęp i wcześniejsza treść niezmienione; bez końcowego spisu treści i bez Tomu II.


### Tom I — F28.2-EL: wieloparametrowe komórki stabilności (2026-11-06)
- **Manuskrypt na main:** `manuscript/tom-i/F28_2EL.md`, commit `15a1a235b9adbe92ed35b93ec8556cc3bfd4c8a5`.
- **Test na main:** `tests/test_f28_2el.py`, commit `285bbcadfe1a8d573ea83890d28e6857faf526a4`.
- **Zakres:** 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady, 6 zadań rozwiązanych. Wieloparametrowe kwadratowe koszty, półalgebraiczne komórki optimum, certyfikat kuli, kandydaci na przełączenia na prostych i wielościan zachowania porządku. Pierwszy kontrprzykład dotyczy abstrakcyjnych funkcji kosztu, nie konkretnych podziałów.
- **Weryfikacja lokalna:** `python /mnt/data/ontologia_el/test_f28_2el.py` PASS, **277830 dokładnych tożsamości wymiernych** dla n=2..4; `python -m py_compile` PASS. Jest to lokalny odpowiednik, a nie uruchomienie pliku pobranego z GitHub. GitHub Actions CI niepotwierdzone.
- **PDF:** lokalny `/mnt/data/ontologia_el/F28_2EL_PODGLAD.pdf`, **2 strony A4**, 49444 B, SHA-256 `89b923c71fddefe6bcc2170a76c117e76c041f0dabc1fb3a974e32eb79425e20`; otwarcie i render 2/2 PASS. Podgląd z lokalnego manuskryptu, nie wierna kompilacja typograficzna tekstu na GitHub; PDF nie został zapisany na GitHub.
- **Blokady:** niezależna recenzja matematyczna, pełne CI, integracja z rzeczywistym monolitem 0.20 i audyt typograficzny nadal otwarte. Historyczny wstęp i wcześniejsze rozdziały niezmienione. **Kanoniczny licznik 585/1222 bez zmian**; bez końcowego spisu treści i bez Tomu II.


### Tom I — F28.2-EM: geometria rzutów i kierunki obojętne (2026-11-06)
- Manuskrypt: `manuscript/tom-i/F28_2EM.md`, commit `b71307ef1d99183d92cf93fa0f61322f0469ea43`.
- Test: `tests/test_f28_2em.py`, commit `345e35b3c502d85a6cbc58e5cac11f710b9dd2eb`.
- Zakres: 3 definicje, 5 twierdzeń z dowodami, 4 kontrprzykłady i 6 rozwiązanych zadań. Rzuty ważone, jądro i rząd, półokreśloność macierzy Grama, symetria translacji.
- Testy lokalne / CI / PDF: status niepotwierdzony na etapie zapisu; wymagają odrębnej weryfikacji. Brak integracji z monolitem 0.20; licznik 585/1222 bez zmian. Historyczny wstęp i poprzednie rozdziały nietknięte; bez końcowego spisu treści i bez Tomu II.
