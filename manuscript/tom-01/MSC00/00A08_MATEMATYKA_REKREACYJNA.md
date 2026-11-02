---
title: "Ontologia Liczby — Tom I"
subtitle: "MSC 00A08. Matematyka rekreacyjna: od zagadki do twierdzenia"
author: "Andrzej Mikulski"
date: "2026-11-02"
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Pozycja źródłowa:** MSC2020 00A08 — *Recreational mathematics*, rodzina A, poziom autorski I, strona 9 taksonomii, minimum 4 strony opracowania. Ten tekst jest nowym rozdziałem Tomu I, nie zmianą istniejącego wstępu historycznego ani rozdziałów E0/E1/F. Po E1-11 stanowi pierwszy nieopracowany wpis indeksu poziomu I. Matematyka rekreacyjna jest tu traktowana jako dziedzina stawiania i dowodzenia twierdzeń, nie katalog odpowiedzi bez uzasadnienia.

# 1. Od zabawy do problemu formalnego

**D01 (stan).** Stanem zagadki nazywamy element ustalonego zbioru $S$. Opis stanu musi zawierać wszystkie informacje potrzebne do określenia dopuszczalnych ruchów.

**D02 (ruch i osiągalność).** Relacja $R\subseteq S\times S$ określa legalny ruch. Stan $t$ jest osiągalny ze stanu $s$, gdy istnieje skończony ciąg $s=s_0,s_1,\ldots,s_k=t$ z $s_i R s_{i+1}$. Dopuszczamy $k=0$.

**D03 (niezmiennik).** Funkcja $I:S\to A$ jest niezmiennikiem, jeżeli $sRt$ pociąga $I(s)=I(t)$. Jej wartości mogą być liczbami, klasami reszt, kolorami albo obiektami kombinatorycznymi.

**D04 (półniezmiennik).** Funkcja $P:S\to\mathbb Z$ jest półniezmiennikiem malejącym, gdy $sRt$ implikuje $P(t)\le P(s)$; jest ściśle malejąca, gdy zawsze zachodzi nierówność ostra. Służy także do dowodzenia zakończenia gry.

**D05 (kolorowanie szachownicowe).** Komórka planszy o współrzędnych całkowitych $(i,j)$ ma kolor określony parzystością $i+j$. Sąsiednie komórki mają różne kolory.

**D06 (domino).** Domino jest parą komórek sąsiadujących bokiem. Pokrycie domino jest rodziną rozłącznych domino, której suma komórek jest całą rozpatrywaną planszą.

**D07 (graf).** Graf prosty nieskierowany $G=(V,E)$ ma zbiór wierzchołków $V$ i zbiór dwuelementowych podzbiorów $V$ jako krawędzi. Stopień $d(v)$ to liczba krawędzi incydentnych z $v$.

**D08 (droga Eulera).** Droga Eulera przechodzi przez każdą krawędź dokładnie raz. Cykl Eulera jest drogą Eulera zamkniętą; wierzchołki mogą się powtarzać.

**D09 (dwudzielność).** Graf jest dwudzielny, jeśli $V=A\cup B$, $A\cap B=\varnothing$ i każda krawędź ma końce w różnych częściach.

**D10 (gra bezstronna).** Gra jest skończona, bezstronna i o normalnej konwencji wygranej, jeżeli obaj gracze mają identyczne dostępne ruchy, nie ma nieskończonych rozgrywek, a gracz bez ruchu przegrywa. Nie dopuszczamy losowości.

**D11 (pozycja wygrywająca).** Pozycja jest wygrywająca, jeśli gracz rozpoczynający może wymusić zwycięstwo; przegrywająca, jeśli każdy legalny ruch oddaje przeciwnikowi pozycję wygrywającą. Stan terminalny jest przegrywający.

**D12 (liczba Grundy'ego).** Dla skończonej gry bezstronnej $g(s)=\operatorname{mex}\{g(t):sRt\}$, gdzie $\operatorname{mex}$ jest najmniejszą nieujemną liczbą całkowitą nieobecną w zbiorze. Rekurencja jest dobrze określona przy braku nieskończonych rozgrywek.

# 2. Niezmienniki, kolorowanie i konstrukcje

**T01 (zasada niezmiennika).** Jeżeli $I$ jest niezmiennikiem, a $I(s)\ne I(t)$, to $t$ nie jest osiągalny z $s$.

*Dowód.* Wzdłuż dowolnego legalnego ciągu $s_0Rs_1R\cdots Rs_k$ zachodzi $I(s_0)=I(s_1)=\cdots=I(s_k)$ przez przechodniość równości. Sprzeczność z $I(s)\ne I(t)$. $\square$

**T02 (przeszkoda szachownicowa).** Każda plansza pokrywalna domino ma tyle samo komórek obu kolorów.

*Dowód.* Każde domino pokrywa jedną komórkę o parzystym i jedną o nieparzystym $i+j$. Sumując po rozłącznych domino, otrzymujemy równe liczności. $\square$

**T03 (szachownica z usuniętymi przeciwległymi rogami).** Z planszy $8\times8$ usuńmy dwa przeciwległe narożniki. Pozostałych 62 komórek nie da się pokryć domino.

*Dowód.* Narożniki $(1,1)$ i $(8,8)$ mają parzyste sumy współrzędnych, więc ten sam kolor. Początkowo było po 32 komórki obu kolorów, po usunięciu zostaje 30 i 32. Przeczy to T02. $\square$

**T04 (niezmiennik modularny).** Niech $w:S\to\mathbb Z$ i $m\ge2$. Jeśli każdy ruch zmienia $w$ o wielokrotność $m$, to reszta $w(s)\bmod m$ jest niezmiennikiem.

*Dowód.* Z warunku $m\mid(w(t)-w(s))$ wynika $w(t)\equiv w(s)\pmod m$. Stosujemy T01. $\square$

**T05 (ściśle malejąca miara kończy rozgrywkę).** Jeśli istnieje $P:S\to\mathbb N_0$, która w każdym ruchu ściśle maleje, to z pozycji $s$ można wykonać najwyżej $P(s)$ ruchów.

*Dowód.* Każdy ruch zmniejsza wartość całkowitą nieujemną co najmniej o 1. Po $P(s)+1$ ruchach wartość musiałaby być ujemna. $\square$

**T06 (obwód polimina).** Dla figury z $n$ jednostkowych kwadratów, w której $e$ par boków kwadratów jest wspólnych, obwód wynosi $4n-2e$.

*Dowód.* Suma obwodów osobnych kwadratów wynosi $4n$. Każdy wspólny bok jest w tej sumie policzony dwukrotnie, a nie należy do brzegu figury. Odejmujemy $2e$. $\square$

**T07 (liczba pokryć prostokąta $2\times n$).** Jeśli $a_n$ oznacza liczbę pokryć prostokąta $2\times n$ domino, to $a_0=a_1=1$ i dla $n\ge2$ zachodzi $a_n=a_{n-1}+a_{n-2}$.

*Dowód.* Lewa skrajna kolumna jest albo pokryta jednym pionowym domino (pozostaje $2\times(n-1)$), albo dwoma poziomymi (pozostaje $2\times(n-2)$). Przypadki są rozłączne i wyczerpujące. $\square$

# 3. Grafy i trasy

**T08 (lemat o uściskach dłoni).** W każdym skończonym grafie nieskierowanym $\sum_{v\in V}d(v)=2|E|$.

*Dowód.* Każda krawędź ma dwa końce i wnosi po 1 do stopnia każdego końca. $\square$

**T09 (parzystość liczby wierzchołków nieparzystych).** W każdym skończonym grafie liczba wierzchołków nieparzystego stopnia jest parzysta.

*Dowód.* T08 daje parzystą sumę stopni. Jej parzystość równa się parzystości liczby składników nieparzystych. $\square$

**T10 (kryterium cyklu Eulera).** Skończony graf, w którym wszystkie wierzchołki o dodatnim stopniu leżą w jednej składowej, ma cykl Eulera wtedy i tylko wtedy, gdy wszystkie stopnie są parzyste.

*Dowód.* W cyklu Eulera każde wejście do wierzchołka jest sparowane z wyjściem, więc stopnie są parzyste. Odwrotnie, rozpoczynamy marsz po niewykorzystanych krawędziach. W wierzchołku różnym od początkowego nie można utknąć: po każdej wykorzystanej krawędzi wejściowej liczba pozostałych incydentnych krawędzi jest nieparzysta, więc dodatnia. Marsz wraca do początku, tworząc cykl. Jeżeli pozostają krawędzie, spójność części z dodatnimi stopniami zapewnia wierzchołek aktualnego cyklu incydentny z niewykorzystaną krawędzią; budujemy tam kolejny cykl i wplatamy go w poprzedni. Powtarzamy skończenie wiele razy. $\square$

**T11 (kryterium otwartej drogi Eulera).** W grafie o jednej składowej zawierającej wszystkie krawędzie istnieje otwarta droga Eulera wtedy i tylko wtedy, gdy dokładnie dwa wierzchołki mają nieparzysty stopień.

*Dowód.* W otwartej drodze tylko początek i koniec mają niesparowane odpowiednio wyjście i wejście. Odwrotnie, dodajemy krawędź między dwoma wierzchołkami nieparzystymi, co czyni wszystkie stopnie parzystymi. Z T10 otrzymujemy cykl Eulera, a usunięcie dodanej krawędzi daje żądaną drogę. Gdy krawędź już istniała, rozumowanie przeprowadzamy na multigrafie pomocniczym; końcowa droga korzysta wyłącznie z pierwotnych krawędzi. $\square$

**T12 (charakterystyka grafów dwudzielnych).** Skończony graf jest dwudzielny wtedy i tylko wtedy, gdy nie ma cyklu nieparzystej długości.

*Dowód.* W grafie dwudzielnym kolejne wierzchołki cyklu zmieniają część, więc powrót do początku wymaga parzystej liczby krawędzi. Odwrotnie, w każdej składowej wybierzmy korzeń i podzielmy wierzchołki według parzystości odległości od korzenia. Wybieramy drzewo najkrótszych ścieżek (BFS). Gdyby krawędź łączyła wierzchołki tej samej parzystości, dwie jednoznaczne ścieżki drzewa od ich najniższego wspólnego przodka, wraz z tą krawędzią, tworzyłyby cykl nieparzysty. Sprzeczność. $\square$

**T13 (wzór Eulera dla grafów płaskich).** Dla spójnego grafu narysowanego na płaszczyźnie bez przecięć krawędzi poza wierzchołkami zachodzi $V-E+F=2$, gdzie $F$ obejmuje także obszar nieograniczony.

*Dowód.* Dla drzewa $E=V-1$ i $F=1$, więc wzór zachodzi. Jeśli graf zawiera cykl, usuwamy krawędź leżącą na tym cyklu. Spójność zostaje zachowana, a dwa sąsiednie obszary łączą się w jeden: $E$ i $F$ zmniejszają się o 1, $V$ się nie zmienia. Indukcja po liczbie krawędzi prowadzi do drzewa. $\square$

# 4. Gry deterministyczne

**T14 (kryterium Grundy'ego).** W skończonej grze bezstronnej o normalnej konwencji pozycja $s$ jest przegrywająca dokładnie wtedy, gdy $g(s)=0$.

*Dowód.* Indukcja po maksymalnej długości gry. Dla stanu terminalnego $\operatorname{mex}(\varnothing)=0$ i brak ruchu oznacza porażkę. Dla pozostałych stanów $g(s)=0$ oznacza, że żadna pozycja następna nie ma wartości 0; z indukcji wszystkie są wygrywające. Gdy $g(s)>0$, definicja $\operatorname{mex}$ zapewnia istnienie ruchu do wartości 0, czyli do pozycji przegrywającej. $\square$

**T15 (odejmowanie jednej lub dwóch zapałek).** W grze z $n$ zapałkami, gdzie wolno zabrać 1 lub 2, pozycja jest przegrywająca dokładnie dla $n\equiv0\pmod3$.

*Dowód.* Dla $n=0$ brak ruchu. Z wielokrotności 3 każdy ruch prowadzi do reszty 1 lub 2. Z każdej innej reszty istnieje ruch do wielokrotności 3 (odpowiednio 1 albo 2). Indukcja po $n$ kończy dowód. $\square$

**T16 (odejmowanie jednej lub trzech zapałek).** W grze, w której wolno zabrać 1 lub 3, przegrywające są dokładnie pozycje z parzystą liczbą zapałek.

*Dowód.* Każdy legalny ruch zmienia parzystość. Z dodatniej liczby nieparzystej można zabrać 1 i przejść do parzystej; z parzystej każdy ruch, o ile istnieje, prowadzi do nieparzystej. Stan 0 jest przegrywający. Indukcja. $\square$

**T17 (wieże Hanoi).** Minimalna liczba ruchów do przeniesienia $n$ krążków z jednego słupka na drugi przy trzech słupkach i zakazie kładzenia większego na mniejszym wynosi $H_n=2^n-1$.

*Dowód.* Przed pierwszym przeniesieniem największego krążka trzeba przenieść wszystkie $n-1$ mniejszych na słupek pomocniczy, co wymaga co najmniej $H_{n-1}$ ruchów. Po przeniesieniu największego trzeba przenieść mniejsze na niego, ponownie co najmniej $H_{n-1}$ ruchów. Konstrukcja rekurencyjna osiąga $H_n=2H_{n-1}+1$ z $H_0=0$. Indukcja daje $2^n-1$. $\square$

**T18 (problem Józefa, eliminacja co drugiego).** Numerując osoby od 1 do $n$ i eliminując co drugą, począwszy od osoby 2, ocalały numer wynosi $J(n)=2\ell+1$, gdy $n=2^m+\ell$ i $0\le\ell<2^m$.

*Dowód.* Przy parzystym $2k$ pierwsza runda usuwa wszystkie numery parzyste; problem na $k$ pozostałych osobach po przeskalowaniu daje $J(2k)=2J(k)-1$. Przy nieparzystym $2k+1$ po usunięciu numerów parzystych następnym usuniętym jest numer 1; cykliczna renumeracja pozostałych daje $J(2k+1)=2J(k)+1$. Z $J(1)=1$ i obu rekurencji przez indukcję po $n$ otrzymujemy wskazany wzór. $\square$

# 5. Zliczanie, barwienie i granice informacji

**T19 (sześć osób).** W każdej grupie sześciu osób istnieją trzy osoby wzajemnie się znające albo trzy osoby wzajemnie sobie nieznane, zakładając symetryczną relację znajomości.

*Dowód.* Wybieramy osobę $A$. Spośród pięciu pozostałych co najmniej trzy są w jednej kategorii: znane $A$ albo nieznane $A$. W pierwszym przypadku, jeśli dwie z tej trójki się znają, tworzą z $A$ trójkę znajomych; jeśli żadna para się nie zna, ta trójka jest wzajemnie nieznana. Drugi przypadek jest symetryczny. $\square$

**T20 (dolne ograniczenie liczby ważeń).** Jeżeli doświadczenie rozróżnia $N$ możliwych stanów, a każde ważenie na wadze szalkowej daje najwyżej trzy wyniki (lewa cięższa, równowaga, prawa cięższa), to algorytm gwarantujący identyfikację stanu potrzebuje w najgorszym przypadku co najmniej $\lceil\log_3N\rceil$ ważeń.

*Dowód.* Adaptacyjna procedura z najwyżej $k$ ważeniami jest drzewem decyzyjnym o rozgałęzieniu najwyżej 3 i ma co najwyżej $3^k$ liści. Rozróżnienie $N$ stanów wymaga co najmniej $N$ różnych liści, więc $3^k\ge N$. Jest to warunek konieczny, nie gwarancja osiągalności tej liczby ważeń. $\square$

# 6. Kontrprzykłady: konieczność nie oznacza wystarczalności

**K01.** Równa liczba pól czarnych i białych nie wystarcza do pokrycia domino: plansza składająca się z dwóch niesąsiadujących pól różnych kolorów ma bilans $1:1$, ale nie ma legalnego domino.

**K02.** Zgodność reszt modulo 2 nie gwarantuje osiągalności: jeśli jedynym ruchem na $\mathbb Z$ jest dodanie lub odjęcie 4, to ze stanu 0 nie osiągniemy stanu 2, mimo że oba są parzyste.

**K03.** Parzysta suma stopni nie gwarantuje cyklu Eulera: ścieżka z trzema wierzchołkami ma stopnie $(1,2,1)$ i sumę 4.

**K04.** Istnienie drogi Eulera nie oznacza istnienia cyklu Eulera: pojedyncza krawędź ma drogę Eulera, ale oba końce mają stopień nieparzysty.

**K05.** Brak trójkątów nie oznacza dwudzielności: cykl o pięciu krawędziach nie ma trójkąta, lecz jest cyklem nieparzystym.

**K06.** W grupie pięciu osób twierdzenie T19 nie musi zachodzić: relację znajomości tworzącą pięciokąt oznaczamy na czerwono, a wszystkie pozostałe pary na niebiesko. Zarówno pięciokąt, jak i jego dopełnienie są bez trójkątów.

**K07.** Odpowiedź 6 ruchów dla trzech krążków Hanoi jest niemożliwa: T17 daje dolne ograniczenie 7, niezależnie od intuicyjnego planu ruchów.

**K08.** W grze z odejmowaniem $\{1,2\}$ nie wystarcza reguła „zawsze zabierz 2”: przy $n=4$ ruch do $n=2$ oddaje przeciwnikowi pozycję wygrywającą, a zabranie 1 daje $n=3$, pozycję przegrywającą.

**K09.** Zgadnięty wzór na podstawie wielu prób nie jest dowodem: $n^2+n+41$ jest pierwsza dla $n=0,\ldots,39$, ale dla $n=40$ wynosi $41^2$.

**K10.** Warunek $V-E+F=2$ nie jest samodzielnym certyfikatem planarności abstrakcyjnego grafu: dla grafu $K_{3,3}$ formalne podstawienie $V=6,E=9,F=5$ spełnia równanie, choć graf nie ma osadzenia płaskiego. Wielkość $F$ ma sens jako liczba obszarów dopiero dla konkretnego osadzenia.

# 7. Zadania rozwiązane

**Z01.** Czy można pokryć domino planszę $6\times6$ bez dwóch rogów na jednej przekątnej? **Rozwiązanie.** Rogi mają ten sam kolor, więc zostaje 16 pól jednego koloru i 18 drugiego. T02 wyklucza pokrycie.

**Z02.** Oblicz liczbę pokryć $2\times5$. **Rozwiązanie.** Rekurencja T07 daje $a_0=1,a_1=1,a_2=2,a_3=3,a_4=5,a_5=8$.

**Z03.** Oblicz obwód prostokąta z pięciu kwadratów w jednym rzędzie. **Rozwiązanie.** $n=5$, wspólnych boków $e=4$, więc $4n-2e=20-8=12$.

**Z04.** Wyznacz obwód litery L z trzech jednostkowych kwadratów. **Rozwiązanie.** Dwa wspólne boki dają $4\cdot3-2\cdot2=8$.

**Z05.** Czy graf o stopniach $(3,3,2,2)$ może istnieć? **Rozwiązanie.** Tak: cykl czterech wierzchołków z jedną przekątną ma właśnie takie stopnie. Suma wynosi 10, czyli pięć krawędzi.

**Z06.** Czy graf o stopniach $(3,2,2)$ istnieje? **Rozwiązanie.** Nie: suma stopni wynosi 7, co przeczy T08.

**Z07.** Czy prosty cykl pięciokątny ma cykl Eulera? **Rozwiązanie.** Tak: jest spójny, a każdy wierzchołek ma stopień 2; obchodzimy pięć krawędzi.

**Z08.** Czy ścieżka na czterech wierzchołkach ma drogę Eulera? **Rozwiązanie.** Tak, dwa końce mają stopień 1, a dwa wewnętrzne stopień 2; drogą jest cała ścieżka.

**Z09.** Wyznacz $V-E+F$ dla osadzonego kwadratu z przekątną. **Rozwiązanie.** $V=4,E=5,F=3$ (dwa obszary wewnętrzne i zewnętrzny), więc $4-5+3=2$.

**Z10.** Czy cykl długości 7 jest dwudzielny? **Rozwiązanie.** Nie, bo sam jest cyklem nieparzystym (T12).

**Z11.** Czy drzewo jest dwudzielne? **Rozwiązanie.** Tak: nie zawiera żadnych cykli, zatem również nieparzystych (T12).

**Z12.** Kto wygrywa przy 12 zapałkach i ruchach 1 albo 2? **Rozwiązanie.** Pozycja 12 jest przegrywająca (T15), więc przy bezbłędnej grze wygrywa drugi gracz.

**Z13.** Jaki pierwszy ruch wykonać przy 14 zapałkach i ruchach 1 albo 2? **Rozwiązanie.** Zabieramy 2, pozostawiając 12, wielokrotność 3.

**Z14.** Kto wygrywa przy 19 zapałkach i ruchach 1 albo 3? **Rozwiązanie.** Pierwszy gracz zabiera 1, pozostawiając parzyste 18 (T16).

**Z15.** Ile ruchów wymaga Hanoi dla czterech krążków? **Rozwiązanie.** $2^4-1=15$.

**Z16.** Dla ilu krążków minimalna liczba ruchów Hanoi wynosi 31? **Rozwiązanie.** $2^n-1=31$, więc $2^n=32$ i $n=5$.

**Z17.** Kto pozostanie w problemie Józefa dla $n=10$? **Rozwiązanie.** $10=8+2$, więc $J(10)=2\cdot2+1=5$.

**Z18.** Wyznacz $J(13)$. **Rozwiązanie.** $13=8+5$, zatem $J(13)=11$.

**Z19.** Jaka jest minimalna liczba ważeń dla 27 rozróżnialnych stanów przy najwyżej trzech wynikach każdego ważenia? **Rozwiązanie.** $3^2<27=3^3$, zatem co najmniej 3; osiągalność zależy od dopuszczalnych ważeń.

**Z20.** Ile ważeń potrzeba co najmniej do rozróżnienia 82 stanów? **Rozwiązanie.** $3^4=81<82\le243=3^5$, więc co najmniej 5.

**Z21.** W grupie siedmiu osób czy zawsze istnieje trójka wzajemnie znana lub nieznana? **Rozwiązanie.** Tak: wybieramy dowolne sześć osób i stosujemy T19.

**Z22.** Podaj kolorowanie krawędzi $K_5$ bez jednobarwnego trójkąta. **Rozwiązanie.** Krawędzie cyklu $1-2-3-4-5-1$ kolorujemy na czerwono, pozostałe na niebiesko; oba podgrafy są cyklami długości 5.

**Z23.** Uzasadnij, że zamknięta trasa skoczka szachowego nie może odwiedzić dokładnie raz wszystkich pól planszy $5\times5$. **Rozwiązanie.** Każdy ruch skoczka zmienia kolor pola, więc zamknięta trasa ma parzystą liczbę ruchów, podczas gdy odwiedzenie 25 pól w cyklu wymaga 25 ruchów.

**Z24.** Pokaż niezmiennik ruchu $(x,y)\mapsto(x+2,y-2)$ dla całkowitych współrzędnych. **Rozwiązanie.** Suma $x+y$ pozostaje stała; osobno parzystość każdej współrzędnej także się nie zmienia. Ze stanu $(0,0)$ nie osiągniemy $(1,-1)$, mimo równej sumy.

# 8. Granice metody i bibliografia

Niezmiennik dostarcza zwykle warunku koniecznego osiągalności, a nie algorytmu konstrukcji. Kolorowanie zależy od reguł ruchu, a rozumowanie probabilistyczne wymaga jawnego modelu losowego. Liczba Grundy'ego dotyczy skończonych gier bezstronnych przy normalnej konwencji, nie dowolnych gier strategicznych. Wzór Eulera wymaga rzeczywistego osadzenia płaskiego. Zadania rekreacyjne stają się twierdzeniami dopiero po sformułowaniu hipotez i dowodu.

**Literatura do dalszej lektury:** M. Gardner, *Mathematical Puzzles and Diversions* (1959); R. J. Wilson, *Introduction to Graph Theory* (wydania różne); J. H. Conway, *On Numbers and Games* (1976); E. R. Berlekamp, J. H. Conway, R. K. Guy, *Winning Ways for Your Mathematical Plays* (1982); F. Harary, *Graph Theory* (1969). Literatura stanowi kontekst; wszystkie dowody w rozdziale zapisano autonomicznie.

**Status wydawniczy:** materiał źródłowy gotowy do odrębnej recenzji. Nie zintegrowano go z kanonicznym monolitem 0.20; historyczny licznik 585 stron bez zmian. Nie tworzono końcowego spisu treści ani Tomu II.