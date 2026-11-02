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
