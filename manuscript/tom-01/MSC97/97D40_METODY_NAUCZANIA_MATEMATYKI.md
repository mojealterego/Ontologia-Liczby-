# MSC 97D40 — Metody nauczania matematyki i techniki pracy w klasie

**Tom I · poziom III MSC2020 · opracowanie matematyczne i metodyczne, wersja częściowa.** Niniejszy tekst jest nowym rozdziałem, nie zastępuje wstępu historycznego ani wcześniejszych rozdziałów F. Twierdzenia dotyczą jawnie zdefiniowanych modeli; nie stanowią bez badań empirycznych dowodów skuteczności metod dydaktycznych.

**Nota redakcyjna (2026-11-02).** Weryfikacja oficjalnego MSC2020 potwierdziła kod 97D40 i poziom III, pominięty wcześniej w lokalnym indeksie taksonomii. Wymagane minimum tego poziomu w projekcie to 44 strony. Obecny materiał nie został jeszcze przyjęty jako pełne opracowanie 44-stronicowe; nie wolno utożsamiać przejścia testów z ukończeniem kategorii.

## 1. Definicje

**D01 (graf wymagań).** Skończony skierowany graf acykliczny $G=(V,E)$ opisuje zależności: $u\to v$ oznacza, że umiejętność $u$ jest warunkiem wstępnym $v$.

**D02 (stan opanowania).** $M\subseteq V$ jest dopuszczalny, gdy z $v\in M$ i $u\to v$ wynika $u\in M$.

**D03 (domknięcie wymagań).** $\mathrm{cl}(S)$ to najmniejszy dopuszczalny zbiór zawierający $S$.

**D04 (zadanie dydaktyczne).** Zadanie $i$ ma koszt czasowy $c_i>0$, wartość modelową $v_i\ge0$ i zbiór wymaganych kompetencji $R_i\subseteq V$.

**D05 (plan lekcji).** Plan to podzbiór zadań $I$ spełniający $\sum_{i\in I}c_i\le B$, gdzie $B$ jest budżetem czasu.

**D06 (pokrycie).** Dla zbioru umiejętności sprawdzanych przez zadanie $C_i\subseteq V$, pokrycie planu to $C(I)=\bigcup_{i\in I}C_i$.

**D07 (zysk krańcowy).** Przy wagach $w_u\ge0$ zysk dołączenia zadania $j$ to $\Delta(j\mid I)=\sum_{u\in C_j\setminus C(I)}w_u$.

**D08 (ocena diagnostyczna).** Test jest funkcją $T:X\to\{0,1\}^m$ przypisującą stanowi ucznia $x$ wektor odpowiedzi; model nie zakłada, że obserwowany wektor identyfikuje $x$.

**D09 (trafność identyfikacyjna).** Test identyfikuje stany z klasy $X_0$, gdy ograniczenie $T|_{X_0}$ jest różnowartościowe.

**D10 (informacja zwrotna).** Reguła informacji zwrotnej jest funkcją $F:\{0,1\}^m\to A$, gdzie $A$ jest zbiorem możliwych interwencji.

**D11 (grupa współpracy).** Podział $P=\{P_1,\ldots,P_k\}$ jest partycją skończonego zbioru uczniów.

**D12 (obciążenie grupy).** Jeśli uczeń $s$ ma modelowy nakład $a_s\ge0$, obciążenie grupy to $L(P_j)=\sum_{s\in P_j}a_s$.

**D13 (miara nierównowagi).** $D(P)=\max_j L(P_j)-\min_j L(P_j)$.

**D14 (wynik znormalizowany).** Dla punktów $r$ z maksymalnej liczby $m>0$ wynik wynosi $q=r/m$; porównywanie $r$ bez uwzględnienia $m$ może być błędne.

**D15 (efekt obserwowany).** Dla wyników przed $x_i$ i po $y_i$ średnia różnica w próbie $n>0$ to $\bar d=n^{-1}\sum_i(y_i-x_i)$; sama ta liczba nie identyfikuje przyczyny zmiany.

## 2. Twierdzenia i dowody

**T01 (istnienie domknięcia).** Dla każdego $S\subseteq V$ istnieje jednoznaczne $\mathrm{cl}(S)$.

*Dowód.* Zbiór $V$ jest dopuszczalny, więc rodzina dopuszczalnych nadzbiorów $S$ jest niepusta. Jej przecięcie jest dopuszczalne: poprzednik każdego węzła należącego do przecięcia należy do każdego z przecinanych zbiorów. Przecięcie jest najmniejszym takim nadzbiorem. Jednoznaczność wynika z minimalności. $\square$

**T02 (monotoniczność).** Jeśli $S\subseteq R$, to $\mathrm{cl}(S)\subseteq\mathrm{cl}(R)$.

*Dowód.* $\mathrm{cl}(R)$ jest dopuszczalnym nadzbiorem $S$; minimalność $\mathrm{cl}(S)$ daje tezę. $\square$

**T03 (idempotencja).** $\mathrm{cl}(\mathrm{cl}(S))=\mathrm{cl}(S)$.

*Dowód.* $\mathrm{cl}(S)$ jest już dopuszczalny, zatem jego najmniejszym dopuszczalnym nadzbiorem jest on sam. $\square$

**T04 (łączenie celów).** $\mathrm{cl}(S\cup R)=\mathrm{cl}(S)\cup\mathrm{cl}(R)$.

*Dowód.* Suma dwóch dopuszczalnych zbiorów jest dopuszczalna: poprzednik elementu należącego do jednej składowej należy do tej samej składowej. Suma zawiera $S\cup R$. Z minimalności wynika jedna inkluzja; T02 zastosowane osobno do $S$ i $R$ daje drugą. $\square$

**T05 (kolejność wprowadzania treści).** Każdy skończony DAG ma porządek liniowy, w którym poprzednik występuje przed następnikiem.

*Dowód.* Skończony DAG ma wierzchołek bez krawędzi wchodzących, inaczej cofanie się po poprzednikach doprowadziłoby do powtórzenia wierzchołka i cyklu. Usuwamy taki wierzchołek i stosujemy indukcję po liczbie wierzchołków. $\square$

**T06 (ograniczenie budżetu).** Każdy plan złożony z $k$ zadań o kosztach co najmniej $c_{\min}>0$ spełnia $k\le\lfloor B/c_{\min}\rfloor$.

*Dowód.* $kc_{\min}\le\sum_{i\in I}c_i\le B$. Dzielimy przez $c_{\min}$ i korzystamy z całkowitości $k$. $\square$

**T07 (monotoniczność pokrycia).** $I\subseteq J$ implikuje $C(I)\subseteq C(J)$.

*Dowód.* Suma zbiorów po mniejszej rodzinie indeksów zawiera się w sumie po większej. $\square$

**T08 (malejący zysk krańcowy).** Przy nieujemnych wagach, dla $I\subseteq J$ oraz $j\notin J$ zachodzi $\Delta(j\mid I)\ge\Delta(j\mid J)$.

*Dowód.* Z T07 wynika $C_j\setminus C(I)\supseteq C_j\setminus C(J)$. Sumowanie nieujemnych wag zachowuje nierówność. $\square$

**T09 (ograniczenie wyniku).** Jeśli $0\le r\le m$ i $m>0$, to $0\le q\le1$.

*Dowód.* Dzielimy nierówności przez dodatnie $m$. $\square$

**T10 (brak identyfikowalności).** Jeżeli istnieją $x\ne y$ z $T(x)=T(y)$, to żadna reguła zależna wyłącznie od wyniku $T$ nie rozróżni tych dwóch stanów.

*Dowód.* Dla dowolnej funkcji $F$ mamy $F(T(x))=F(T(y))$. $\square$

**T11 (zachowanie sumy obciążeń).** Dla każdej partycji $P$ zachodzi $\sum_j L(P_j)=\sum_s a_s$.

*Dowód.* Każdy uczeń należy do dokładnie jednego bloku partycji, więc jego składnik występuje w lewej sumie dokładnie raz. $\square$

**T12 (dolne ograniczenie maksimum).** Dla $k$ niepustych grup $\max_jL(P_j)\ge(\sum_s a_s)/k$.

*Dowód.* Maksimum jest nie mniejsze od średniej arytmetycznej $k$ obciążeń. T11 identyfikuje licznik. $\square$

**T13 (dwie grupy).** Jeśli suma obciążeń wynosi $A$, a jedna grupa ma obciążenie $x$, to $D(P)=|2x-A|$.

*Dowód.* Druga grupa ma $A-x$ na mocy T11. Różnica większego i mniejszego z dwóch obciążeń to $|x-(A-x)|$. $\square$

**T14 (nieujemność wariancji różnic).** Dla $d_i=y_i-x_i$ i $n\ge1$ zachodzi $\sum_i(d_i-\bar d)^2\ge0$, a równość występuje wtedy i tylko wtedy, gdy wszystkie $d_i$ są równe.

*Dowód.* Każdy kwadrat jest nieujemny; suma zeruje się dokładnie wtedy, gdy zerują się wszystkie składniki. $\square$

**T15 (niezmienniczość średniej różnicy na wspólne przesunięcie).** Jeśli do każdego $x_i$ i $y_i$ dodamy tę samą stałą $a$, to $\bar d$ się nie zmieni.

*Dowód.* $(y_i+a)-(x_i+a)=y_i-x_i$ dla każdego $i$. $\square$

**T16 (ograniczenie zysku z pokrycia).** Jeśli $W=\sum_{u\in V}w_u$, to dla każdego planu $I$ zachodzi $0\le\sum_{u\in C(I)}w_u\le W$.

*Dowód.* $C(I)\subseteq V$ i wszystkie wagi są nieujemne. $\square$

## 3. Kontrprzykłady

**K01.** Bez acykliczności nie istnieje porządek z T05: graf $a\to b\to a$ jest cyklem.

**K02.** Nie wolno utożsamiać czasu z wartością: zadanie o koszcie 10 może mieć wartość 1, a zadanie o koszcie 2 — wartość 9.

**K03.** Zachłanny wybór najwyższej wartości może być nieoptymalny: przy $B=10$ zadania $(c,v)=(6,9),(5,8),(5,8)$; wybór dwóch ostatnich daje 16 zamiast 9.

**K04.** Liczba zadań nie jest pokryciem: dziesięć zadań sprawdzających tę samą umiejętność pokrywa jeden element $V$.

**K05.** Zwiększenie liczby grup nie musi zmniejszać $D(P)$: obciążenia $(10,0)$ mają nierównowagę 10, a podział na trzy grupy $(10,0,0)$ także 10.

**K06.** Średnia poprawa nie dowodzi przyczynowości: identyczny wzrost w dwóch grupach może wynikać z czynnika zewnętrznego.

**K07.** Test jednego pytania z odpowiedzią 0 lub 1 nie identyfikuje trzech odmiennych stanów: zasada szufladkowa.

**K08.** Wynik surowy 8 punktów nie jest lepszy od 7 bez znajomości maksimum: $8/20<7/10$.

**K09.** Dla wag ujemnych T08 nie musi zachodzić: przy $w_u=-1$ i $C_j=\{u\}$, $C(I)=\varnothing$, $C(J)=\{u\}$, zyski wynoszą odpowiednio $-1$ i $0$.

**K10.** Bez warunku $c_{\min}>0$ ograniczenie T06 zawodzi: dowolnie wiele zadań zerokosztowych mieści się w budżecie.

## 4. Zadania rozwiązane

**Z01.** Graf $a\to b\to c$: $\mathrm{cl}(\{c\})=\{a,b,c\}$, ponieważ $c$ wymaga $b$, a $b$ wymaga $a$.

**Z02.** Graf $a\to b$, $a\to c$: $\mathrm{cl}(\{b,c\})=\{a,b,c\}$.

**Z03.** Dla grafu Z02 poprawny porządek to $(a,b,c)$; również $(a,c,b)$.

**Z04.** Przy $B=45$ minut i $c_{\min}=8$ minut T06 daje najwyżej $\lfloor45/8\rfloor=5$ zadań.

**Z05.** Koszty $(10,15,25)$, budżet 30: zadania 1 i 2 kosztują 25, więc tworzą plan dopuszczalny.

**Z06.** Pokrycia $C_1=\{a,b\}$, $C_2=\{b,c\}$: $C(\{1,2\})=\{a,b,c\}$.

**Z07.** Dla wag $(w_a,w_b,w_c)=(2,3,5)$ i Z06 zysk dołączenia zadania 2 po zadaniu 1 wynosi $w_c=5$.

**Z08.** Dla tych samych wag zysk zadania 2 bez wcześniejszych zadań wynosi $w_b+w_c=8$.

**Z09.** Wynik 18 z 24 to $q=18/24=3/4$.

**Z10.** Wynik 9 z 10 i 16 z 20: pierwszy to $0{,}9$, drugi $0{,}8$.

**Z11.** Test $T$ daje tę samą odpowiedź dla stanów $x$ i $y$. Wówczas każda deterministyczna reguła informacji zwrotnej $F\circ T$ daje tę samą interwencję.

**Z12.** Obciążenia uczniów $(2,3,5)$, grupy $\{2,3\}$ i $\{5\}$: obciążenia wynoszą $(5,5)$, więc $D=0$.

**Z13.** Dla dwóch grup o łącznym obciążeniu 20 i obciążeniu pierwszej 7, T13 daje $D=|14-20|=6$.

**Z14.** Przy $A=21$ i dwóch grupach T12 wymusza maksymalne obciążenie co najmniej $10{,}5$.

**Z15.** Wyniki przed $(2,4,6)$ i po $(4,5,9)$: różnice $(2,1,3)$, więc $\bar d=2$.

**Z16.** W Z15 dodanie 10 do każdego wyniku przed i po nie zmienia $\bar d=2$.

**Z17.** Dla różnic $(1,1,1)$ suma kwadratów odchyleń od średniej wynosi zero.

**Z18.** Dla różnic $(1,2,3)$ średnia wynosi 2, a suma kwadratów odchyleń $1+0+1=2$.

**Z19.** Przy $V=\{a,b,c\}$ i wagach $(1,2,3)$ dowolne pokrycie ma wagę co najwyżej $W=6$.

**Z20.** Dla zadań o kosztach $(6,5,5)$ i wartościach $(9,8,8)$, budżet 10, plan $\{2,3\}$ ma wartość 16 i jest lepszy od $\{1\}$ o wartości 9.

## 5. Interpretacja i granice naukowe

Graf wymagań jest hipotezą modelową, a nie automatycznie prawdziwym opisem rozwoju ucznia. Zadania mogą sprawdzać wiele kompetencji jednocześnie, a pojedyncza odpowiedź może mieć wiele przyczyn. Pokrycie, zysk i optymalizacja czasu są obliczeniowymi narzędziami projektowania zajęć, nie zamiennikami badań skuteczności. W szczególności średnia różnica przed–po nie pozwala wykluczyć efektów dojrzewania, selekcji, powtarzania testu ani zdarzeń zewnętrznych. Przy interpretacji empirycznej potrzebny jest projekt badawczy z właściwą grupą porównawczą, miarami niepewności i kontrolą błędów.

**Literatura kontekstowa:** G. Pólya, *How to Solve It* (1945); J. Bruner, *The Process of Education* (1960); L. S. Vygotsky, *Mind in Society* (1978); P. Black, D. Wiliam, *Assessment and Classroom Learning* (1998). Pozycje wskazują tradycje dydaktyczne; nie dowodzą poprawności dowolnego modelu przyjętego w tym rozdziale.


## 6. Rozszerzenie III-A: optymalizacja pokrycia i granice diagnozy

Poniższe twierdzenia rozwijają D04–D10. W odróżnieniu od zaleceń dydaktycznych są formalnymi własnościami skończonych modeli. **Nie stanowią dowodu skuteczności konkretnej interwencji edukacyjnej.**

**D16 (ważona funkcja pokrycia).** Dla rodziny zadań indeksowanych zbiorem skończonym $N$ i wag $w_u\ge 0$ określamy
$$f(I)=\sum_{u\in\bigcup_{i\in I}C_i}w_u,\qquad I\subseteq N.$$
Przyjmujemy $f(\varnothing)=0$.

**D17 (zachłanny plan kardynalny).** Dla całkowitego $1\le k\le |N|$ algorytm zaczyna od $G_0=\varnothing$ i w kroku $t$ wybiera zadanie $j\notin G_t$ o największym $f(G_t\cup\{j\})-f(G_t)$, po czym definiuje $G_{t+1}=G_t\cup\{j\}$. W razie remisów dopuszczalny jest dowolny deterministyczny wybór.

**D18 (optimum kardynalne).** $O$ jest optymalne dla budżetu liczby zadań $k$, gdy $|O|\le k$ i $f(O)=\max_{|I|\le k}f(I)$. Maksimum istnieje, ponieważ $N$ jest skończony.

**D19 (deterministyczny test binarny).** Dla skończonej klasy stanów $X$ test $T:X\to\{0,1\}^m$ ma $m$ pytań. Nie utożsamiamy $m$ z liczbą niezależnych informacji w przypadku odpowiedzi skorelowanych.

**T17 (normalizacja i monotoniczność).** Funkcja $f$ spełnia $f(\varnothing)=0$ oraz $I\subseteq J\implies f(I)\le f(J)$.

*Dowód.* Pierwsza równość wynika z pustej sumy. Zawieranie $I\subseteq J$ implikuje $C(I)\subseteq C(J)$, a wszystkie wagi są nieujemne. $\square$

**T18 (submodularność).** Dla $A\subseteq B\subseteq N$ i $j\notin B$:
$$f(A\cup\{j\})-f(A)\ \ge\ f(B\cup\{j\})-f(B).$$

*Dowód.* Nowe elementy pokrywane po dodaniu $j$ to odpowiednio $C_j\setminus C(A)$ oraz $C_j\setminus C(B)$. Drugi zbiór zawiera się w pierwszym. Wagi są nieujemne, więc jego suma nie jest większa. $\square$

**T19 (oszacowanie postępu algorytmu zachłannego).** Niech $O$ będzie optimum z D18. Dla każdego $0\le t<k$:
$$f(G_{t+1})-f(G_t)\ge \frac{f(O)-f(G_t)}{k}.$$

*Dowód.* Z monotoniczności $f(O)\le f(O\cup G_t)$. Dodawanie elementów $O\setminus G_t$ po kolei i zastosowanie T18 daje
$$f(O\cup G_t)-f(G_t)\le\sum_{j\in O\setminus G_t}[f(G_t\cup\{j\})-f(G_t)].$$
W sumie jest co najwyżej $k$ nieujemnych składników, więc co najmniej jeden z nich jest nie mniejszy niż $(f(O)-f(G_t))/k$, o ile różnica jest dodatnia. Jeśli różnica nie jest dodatnia, teza wynika z nieujemności zysku. Algorytm wybiera największy dostępny zysk, co kończy dowód. $\square$

**T20 (gwarancja zachłanna).** Po $k$ krokach:
$$f(G_k)\ge\left(1-\left(1-\frac1k\right)^k\right)f(O)\ge(1-e^{-1})f(O).$$

*Dowód.* Niech $r_t=f(O)-f(G_t)$. Z T19 mamy $r_{t+1}\le(1-1/k)r_t$. Ponieważ $f(G_0)=0$, $r_0=f(O)$, a więc $r_k\le(1-1/k)^k f(O)$. Stąd pierwsza nierówność. Druga wynika z $1-x\le e^{-x}$ dla $x\ge0$, zastosowanej do $x=1/k$. $\square$

**T21 (dolna granica długości diagnozy).** Jeśli deterministyczny test $T:X\to\{0,1\}^m$ identyfikuje wszystkie $n=|X|\ge1$ stany, to
$$2^m\ge n,\qquad m\ge\lceil\log_2 n\rceil.$$

*Dowód.* Różnowartościowość $T$ wymaga co najmniej $n$ różnych wektorów odpowiedzi. W zbiorze $\{0,1\}^m$ istnieje dokładnie $2^m$ takich wektorów. Logarytmujemy dodatnie liczby. $\square$

**T22 (osiągalność granicy kodowej).** Dla dowolnego $n\ge1$ istnieje abstrakcyjny test deterministyczny identyfikujący $n$ stanów przy $m=\lceil\log_2 n\rceil$ pytaniach binarnych.

*Dowód.* Numerujemy stany od $0$ do $n-1$ i przypisujemy im różne zapisy binarne o długości $m$ (z zerami wiodącymi). Ponieważ $n\le2^m$, kodowanie jest różnowartościowe. Konstrukcja nie gwarantuje istnienia pedagogicznie sensownych pytań realizujących każdy bit. $\square$

**T23 (oczekiwana wartość pokrycia).** Jeśli $Y_u$ jest wskaźnikiem losowym zdarzenia, że umiejętność $u$ została rzeczywiście pokryta, a $p_u=P(Y_u=1)$, to dla skończonego $V$:
$$\mathbb E\!\left[\sum_{u\in V}w_uY_u\right]=\sum_{u\in V}w_up_u.$$

*Dowód.* Liniowość wartości oczekiwanej i $\mathbb E[Y_u]=p_u$. Nie jest potrzebna niezależność zmiennych $Y_u$. $\square$

**T24 (ograniczenie oczekiwanego pokrycia).** Dla $0\le p_u\le1$ i $w_u\ge0$:
$$0\le\sum_{u\in V}w_up_u\le\sum_{u\in V}w_u.$$

*Dowód.* Każdy składnik $w_up_u$ leży w przedziale $[0,w_u]$; sumujemy nierówności. $\square$

### Kontrprzykłady do rozszerzenia

**K11 (zachłanność nie zawsze optymalna).** Dla $k=2$, równych wag i pokryć $C_A=\{1,2,3,4\}$, $C_B=\{1,2,5\}$, $C_C=\{3,4,6\}$ zachłanny wybiera najpierw $A$ (wartość $4$), a potem $B$ lub $C$ (łącznie $5$). Optimum $\{B,C\}$ pokrywa wszystkie $6$ elementów.

**K12 (iloraz zysku do kosztu nie wystarcza).** Budżet czasu $B\ge3$; zadanie $A$ kosztuje $B$ i ma wartość $B$, zadanie $C$ kosztuje $1$ i ma wartość $1+\varepsilon$ dla $\varepsilon>0$. Zachłanny algorytm wybierający największe $v_i/c_i$ zaczyna od $C$, po czym nie może wybrać $A$. Jego wartość wynosi $1+\varepsilon$, a optimum dla $B>1+\varepsilon$ ma wartość $B$. Iloraz wyników dąży do zera przy $B\to\infty$.

**K13 (granica informacyjna nie gwarantuje sensowności pytań).** Dla $n=4$ dwa abstrakcyjne bity wystarczają do zakodowania stanów, ale jeśli oba pytania mają identyczną odpowiedź dla dwóch stanów, rzeczywisty test nie jest różnowartościowy.

**K14 (niezależność nie jest konieczna dla T23).** Niech $Y_a=Y_b$ będzie tą samą zmienną Bernoulliego z parametrem $1/2$, a $w_a=w_b=1$. Zmienne są doskonale zależne, lecz oczekiwana suma nadal wynosi $1$.

### Zadania rozwiązane do rozszerzenia

**Z21.** Dla $C_1=\{a,b\}$, $C_2=\{b,c\}$ i wag $w_a=2,w_b=3,w_c=5$ oblicz $f(\{1,2\})$. **Rozwiązanie:** pokrycie to $\{a,b,c\}$, zatem $f=2+3+5=10$.

**Z22.** W Z21 oblicz zysk dołączenia zadania $2$ po zadaniu $1$. **Rozwiązanie:** nowa jest tylko umiejętność $c$, więc zysk wynosi $5$.

**Z23.** Dla $k=2$ oblicz współczynnik gwarancji T20. **Rozwiązanie:** $1-(1-1/2)^2=3/4$.

**Z24.** Dla $k=3$ oblicz współczynnik gwarancji T20. **Rozwiązanie:** $1-(2/3)^3=19/27$.

**Z25.** Ile binarnych pytań potrzeba do rozróżnienia $9$ stanów w modelu T21? **Rozwiązanie:** $m\ge\lceil\log_2 9\rceil=4$, ponieważ $2^3=8<9\le16=2^4$.

**Z26.** Zakoduj cztery stany dwoma bitami. **Rozwiązanie:** przypisz kolejno $00,01,10,11$; każdy stan ma unikatowy wektor.

**Z27.** Dla dwóch umiejętności o wagach $2$ i $5$, z prawdopodobieństwami pokrycia $1/2$ i $4/5$, oblicz oczekiwane pokrycie. **Rozwiązanie:** $2\cdot(1/2)+5\cdot(4/5)=1+4=5$.

**Z28.** Wykaż, że w K11 wynik zachłanny jest gorszy od optimum. **Rozwiązanie:** $f(\{A,B\})=f(\{A,C\})=5$, natomiast $f(\{B,C\})=6$.

**Z29.** Dla $k=1$ sprawdź T20. **Rozwiązanie:** współczynnik wynosi $1-(1-1)^1=1$, co odpowiada wyborowi najlepszego pojedynczego zadania.

**Z30.** W K12 przy $B=100$, $\varepsilon=0{,}1$ oblicz iloraz wartości zachłannej do optymalnej. **Rozwiązanie:** $(1{,}1)/100=0{,}011$.

**Granica walidacji rozszerzenia III-A.** Dowody T17–T24 są argumentami skończonej matematyki dyskretnej. T20 dotyczy ograniczenia liczby zadań, **nie** ogólnego ograniczenia czasowego; K12 pokazuje, dlaczego tych warunków nie można utożsamiać. Rzeczywista diagnoza wymaga badania jakości pytań, błędów pomiaru, etyki i trafności interwencji.


## 6. Rozszerzenie III-B: diagnoza adaptacyjna i niezawodność oceniania

**D20 (drzewo diagnostyczne).** Skończone binarne drzewo decyzyjne przypisuje węzłom wewnętrznym pytania o odpowiedziach $0,1$, a liściom rozpoznane stany. Długość ścieżki do liścia jest liczbą zadanych pytań.

**D21 (test bezbłędny).** Test adaptacyjny jest bezbłędny na $X$, jeśli różnym stanom przypisuje różne liście; dla $x\in X$ oznaczmy liczbę pytań przez $\ell(x)$.

**D22 (rozkład stanów).** Wektor $p=(p_x)_{x\in X}$ spełnia $p_x>0$ oraz $\sum_xp_x=1$. Średnia liczba pytań to $L=\sum_xp_x\ell(x)$.

**D23 (entropia diagnozy).** $H(p)=-\sum_xp_x\log_2p_x$ bitów.

**D24 (koszt pomyłki).** Dla decyzji $a\in A$, stanu $x\in X$ i funkcji strat $\lambda(a,x)\ge0$ ryzyko decyzji przy rozkładzie $p$ to $R(a;p)=\sum_xp_x\lambda(a,x)$.

**D25 (reguła Bayesa).** Dla skończonego $A$ decyzja $a^*(p)$ minimalizuje $R(a;p)$.

**D26 (informacja zwrotna z obserwacji).** Dla wyniku $Y=y$ o dodatnim prawdopodobieństwie aktualizujemy $p_x^{(y)}=P(X=x\mid Y=y)$.

**D27 (straty po informacji).** Ryzyko z informacją to $\sum_yP(Y=y)\min_aR(a;p^{(y)})$; bez informacji $\min_aR(a;p)$.

**T25 (nierówność Krafta).** Długości liści bezbłędnego binarnego drzewa diagnostycznego spełniają $\sum_{x\in X}2^{-\ell(x)}\le1$.

*Dowód.* Każdy liść na głębokości $\ell$ wyznacza cylinder nieskończonych ciągów binarnych o mierze $2^{-\ell}$ w miarze uczciwych niezależnych bitów. Cylindry różnych liści są rozłączne, gdyż żaden liść nie jest przodkiem innego liścia. Suma ich miar nie przekracza $1$. $\square$

**T26 (dolna granica średniej długości diagnozy).** Każde bezbłędne drzewo spełnia $L\ge H(p)$.

*Dowód.* Niech $K=\sum_x2^{-\ell(x)}\le1$ z T25 i $q_x=2^{-\ell(x)}/K$. Z nieujemności dywergencji $D(p\Vert q)=\sum_xp_x\log_2(p_x/q_x)\ge0$ otrzymujemy
$$0\le -H(p)+L+\log_2K.$$
Ponieważ $\log_2K\le0$, mamy $L\ge H(p)-\log_2K\ge H(p)$. Nieujemność dywergencji wynika z $\ln t\le t-1$ po podstawieniu $t=q_x/p_x$ i zsumowaniu. $\square$

**T27 (konstrukcja bliska optimum).** Jeśli wolno zadawać dowolne abstrakcyjne pytania binarne o stan, istnieje bezbłędny test o średniej liczbie pytań $L<H(p)+1$ dla co najmniej dwóch stanów.

*Dowód.* Dla każdego stanu wybieramy długość $\ell_x=\lceil-\log_2p_x\rceil$. Wtedy $\sum_x2^{-\ell_x}\le\sum_xp_x=1$. Z twierdzenia Krafta–McMillana o kodach prefiksowych istnieje binarne drzewo z liśćmi o tych długościach. Ponieważ $\ell_x<-\log_2p_x+1$, po pomnożeniu przez $p_x$ i zsumowaniu mamy $L<H(p)+1$. Konstrukcja jest abstrakcyjna: nie gwarantuje, że pytania odpowiadają sensownym zadaniom szkolnym. $\square$

**T28 (informacja nie zwiększa optymalnego ryzyka).** Dla skończonych $X,A,Y$ zachodzi
$$\sum_yP(Y=y)\min_aR(a;p^{(y)})\le\min_aR(a;p).$$

*Dowód.* Niech $a_0$ minimalizuje ryzyko bez obserwacji. Dla każdego $y$ minimum ryzyka warunkowego nie przewyższa ryzyka decyzji $a_0$. Po zważeniu przez $P(Y=y)$ i zsumowaniu prawa całkowitego prawdopodobieństwa otrzymujemy $\sum_yP(Y=y)R(a_0;p^{(y)})=R(a_0;p)$. $\square$

**T29 (nieujemność wartości informacji).** Definiując $V=\min_aR(a;p)-\sum_yP(Y=y)\min_aR(a;p^{(y)})$, otrzymujemy $V\ge0$.

*Dowód.* Bezpośrednio z T28. $\square$

**T30 (diagnostyka bez informacji).** Jeśli $X$ i $Y$ są niezależne, to $V=0$.

*Dowód.* Dla każdego $y$ z dodatnim prawdopodobieństwem posterior $p^{(y)}=p$, więc wszystkie minima w T29 są równe. $\square$

**T31 (decyzja przy stracie zero–jeden).** Jeśli $A=X$ i $\lambda(a,x)=\mathbf 1_{\{a\ne x\}}$, reguła Bayesa wybiera dowolny stan o największym $p_x$, a minimalne ryzyko wynosi $1-\max_xp_x$.

*Dowód.* $R(a;p)=\sum_{x\ne a}p_x=1-p_a$. Minimalizacja jest równoważna maksymalizacji $p_a$. $\square$

**T32 (dokładna diagnoza usuwa stratę klasyfikacyjną).** Przy stracie zero–jeden i obserwacji $Y=X$ ryzyko z informacją wynosi $0$, a wartość informacji wynosi $1-\max_xp_x$.

*Dowód.* Po obserwacji $y$ posterior przypisuje prawdopodobieństwo $1$ stanowi $y$. Wybór $a=y$ ma stratę zerową; wynik wynika z T31. $\square$

### Kontrprzykłady i granice

**K15.** Granica entropijna nie gwarantuje dopuszczalności pedagogicznej pytań: przy dwóch stanach identycznie odpowiadających na każde dostępne pytanie nie istnieje bezbłędny test, choć $H(p)\le1$.

**K16.** Obserwacja może nie mieć wartości: przy niezależnych $X$ i $Y$ otrzymujemy $V=0$, nawet gdy wynik $Y$ ma wysoką entropię.

**K17.** Więcej informacji nie oznacza zawsze poprawy każdej indywidualnej decyzji: T28 dotyczy *średniego optymalnego ryzyka*, nie wyniku każdego ucznia.

**K18.** Dla strat asymetrycznych wybór najczęstszego stanu nie musi minimalizować ryzyka: przy $P(X=1)=0{,}4$, koszt fałszywego alarmu $1$ i koszt przeoczenia $10$, decyzja „1” ma ryzyko $0{,}6$, a decyzja „0” ma ryzyko $4$.

### Zadania z rozwiązaniami

**Z31.** Cztery stany o równych prawdopodobieństwach. **Rozwiązanie:** $H=2$ bity; drzewo o czterech liściach na głębokości $2$ daje $L=2$.

**Z32.** Dwa stany o prawdopodobieństwach $1/2,1/2$. **Rozwiązanie:** $H=1$ i jedno pytanie binarne wystarcza.

**Z33.** Długości liści $(1,2,2)$. **Rozwiązanie:** suma Krafta wynosi $1/2+1/4+1/4=1$.

**Z34.** Długości $(1,1,2)$. **Rozwiązanie:** suma Krafta wynosi $1/2+1/2+1/4=5/4>1$; takie długości nie tworzą bezbłędnego drzewa.

**Z35.** Rozkład $(1/2,1/4,1/4)$ i długości $(1,2,2)$. **Rozwiązanie:** $L=1/2+1/2+1/2=3/2$; entropia także wynosi $3/2$.

**Z36.** Dwa stany o prawdopodobieństwach $0{,}8$ i $0{,}2$ przy stracie zero–jeden. **Rozwiązanie:** wybieramy stan pierwszy, ryzyko $0{,}2$.

**Z37.** W Z36 obserwacja ujawnia stan bezbłędnie. **Rozwiązanie:** ryzyko po obserwacji $0$, wartość informacji $0{,}2$.

**Z38.** Przy $p=(1/3,1/3,1/3)$ i stracie zero–jeden. **Rozwiązanie:** minimalne ryzyko $1-1/3=2/3$.

**Z39.** Przy $X\perp Y$ i dowolnej skończonej funkcji strat. **Rozwiązanie:** posterior równy prior, zatem wartość informacji $V=0$.

**Z40.** Przy $P(X=1)=0{,}4$, stracie przeoczenia $10$ i fałszywego alarmu $1$. **Rozwiązanie:** przewidywanie „1” daje $0{,}6$, przewidywanie „0” daje $4$, więc optymalna jest decyzja „1”.

**Granica zastosowania.** T25–T32 opisują modele informacji i decyzji. Użycie ich do rzeczywistych uczniów wymaga osobnej oceny rzetelności testów, ochrony danych, uczciwości pomiaru i skutków błędnych decyzji. Twierdzenie o istnieniu kodu prefiksowego nie dowodzi istnienia odpowiedniego zestawu pytań dydaktycznych.
