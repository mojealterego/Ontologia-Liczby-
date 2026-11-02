---
title: "Ontologia Liczby — Tom I"
subtitle: "E1-09. Statystyka opisowa: dane, miary i weryfikowalne wnioski"
author: "Andrzej Mikulski"
date: "2026-11-02"
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Taksonomia:** E1-09, poziom I, po E1-08. Rozdział rozróżnia populację, próbę, miary położenia i rozproszenia, wizualizację oraz ograniczenia interpretacji. Wszystkie obliczenia przykładów mogą być prowadzone dokładnie na ułamkach. Nie jest to inferencja statystyczna ani deklaracja przyczynowości. **Stan:** materiał niezintegrowany z monolitem 0.20.

# A. Definicje i zakres

**D1 (zbiór danych z krotnościami).** Próbka liczbowa to skończona niepusta lista \(x_1,\ldots,x_n\in\mathbb R\), \(n\ge1\). Powtórzenia są znaczące; kolejność nie zmienia opisanych niżej miar.

**D2 (liczność i częstość).** Dla wartości \(a\), liczność \(N(a)=|\{i:x_i=a\}|\), a częstość względna \(f(a)=N(a)/n\).

**D3 (średnia arytmetyczna).** \(\bar x=\frac1n\sum_{i=1}^n x_i\).

**D4 (mediana).** Po uporządkowaniu \(x_{(1)}\le\cdots\le x_{(n)}\) mediana to \(x_{((n+1)/2)}\) dla nieparzystego \(n\), a dla parzystego \(n\) średnia dwóch środkowych obserwacji.

**D5 (dominanta).** Moda to dowolna wartość o maksymalnej liczności. Może istnieć kilka mod; dla wszystkich wartości występujących jednokrotnie brak wyróżnionej dominanty, choć formalnie każda maksymalizuje liczność.

**D6 (rozstęp).** \(R=\max_i x_i-\min_i x_i\).

**D7 (wariancja populacyjna listy).** \(V=\frac1n\sum_{i=1}^n(x_i-\bar x)^2\); odchylenie standardowe to \(\sigma=\sqrt V\).

**D8 (wariancja z poprawką Bessela).** Dla \(n\ge2\) definiujemy \(s^2=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2\). Nie jest ona tożsama z \(V\); wnioski o nieobciążoności wymagają założeń probabilistycznych.

**D9 (średnia ważona).** Dla \(w_i\ge0\) i \(W=\sum w_i>0\), \(\bar x_w=\frac1W\sum w_ix_i\).

**D10 (kwartyle: jawna konwencja).** Przyjmujemy mediany dolnej i górnej połowy uporządkowanych danych, bez centralnej obserwacji przy nieparzystym \(n\). Dla \(n\ge4\) obie połowy są niepuste; \(Q_1,Q_3\) to ich mediany, a \(IQR=Q_3-Q_1\). Inne podręczniki i programy stosują inne definicje.

**D11 (wartość odstająca według reguły Tukeya).** Obserwacja poza przedziałem \([Q_1-1{,}5\,IQR,Q_3+1{,}5\,IQR]\) jest oznaczana jako potencjalnie odstająca. To heurystyka, nie dowód błędu.

**D12 (tabela liczności).** Zestawienie różnych wartości i ich liczności, których suma wynosi \(n\).

**D13 (średnia z podgrup).** Jeśli rozłączne grupy o licznościach \(n_j\) mają średnie \(\bar x_j\), średnia łączna to \(\sum_j n_j\bar x_j/\sum_j n_j\).

**D14 (błąd agregacji).** Błędem jest stosowanie średniej nieważonej ze średnich podgrup przy różnych licznościach, chyba że szczególne dane przypadkiem dają poprawny wynik.

**D15 (przedstawienie graficzne).** Wykres słupkowy reprezentuje liczności kategorii; histogram przedstawia liczności lub gęstości w przedziałach liczbowych. Przy nierównych szerokościach klas porównywalną wielkością jest pole słupka, nie sama wysokość.

# B. Twierdzenia i dowody

**T1 (suma częstości).** Dla wszystkich różnych wartości \(a\) w danych \(\sum_a N(a)=n\) oraz \(\sum_a f(a)=1\).
*Dowód.* Każda obserwacja należy dokładnie do jednej klasy o swojej wartości. Zliczenie wszystkich klas liczy każdą obserwację raz; dzielimy przez \(n\). \(\square\)

**T2 (średnia w przedziale).** \(\min_i x_i\le\bar x\le\max_i x_i\).
*Dowód.* Dla każdego \(i\), \(m\le x_i\le M\). Sumując i dzieląc przez dodatnie \(n\), otrzymujemy nierówności. \(\square\)

**T3 (zerowa suma odchyleń).** \(\sum_i(x_i-\bar x)=0\).
*Dowód.* \(\sum_i x_i-n\bar x=n\bar x-n\bar x=0\). \(\square\)

**T4 (średnia minimalizuje kwadraty).** Dla dowolnego \(a\in\mathbb R\):
\[
\sum_i(x_i-a)^2=\sum_i(x_i-\bar x)^2+n(a-\bar x)^2.
\]
Wobec tego jedynym minimum sumy kwadratów jest \(a=\bar x\).
*Dowód.* Podstaw \(x_i-a=(x_i-\bar x)+(\bar x-a)\), rozwiń kwadraty i zastosuj T3, aby wyzerować wyraz mieszany. \(\square\)

**T5 (nieujemność wariancji).** \(V\ge0\), przy czym \(V=0\) wtedy i tylko wtedy, gdy wszystkie obserwacje są równe.
*Dowód.* Każdy kwadrat odchylenia jest nieujemny; suma wynosi zero dokładnie wtedy, gdy każdy składnik jest zerem. \(\square\)

**T6 (wzór obliczeniowy na wariancję).**
\[
V=\frac1n\sum_i x_i^2-\bar x^2.
\]
*Dowód.* Rozwijamy \((x_i-\bar x)^2=x_i^2-2x_i\bar x+\bar x^2\), sumujemy i używamy \(\sum_i x_i=n\bar x\). \(\square\)

**T7 (przesunięcie danych).** Po zastąpieniu każdego \(x_i\) przez \(x_i+c\) średnia i mediana rosną o \(c\), a wariancja, odchylenie i rozstęp nie zmieniają się.
*Dowód.* Średnia nowa to \(\bar x+c\); porządek danych jest zachowany, więc mediana przesuwa się o \(c\). Odchylenia od nowej średniej pozostają \(x_i-\bar x\), a różnica maksimum i minimum pozostaje taka sama. \(\square\)

**T8 (skalowanie danych).** Po zastąpieniu \(x_i\) przez \(a x_i\), średnia zmienia się na \(a\bar x\), wariancja na \(a^2V\), odchylenie na \(|a|\sigma\), rozstęp na \(|a|R\).
*Dowód.* Liniowość sumy daje średnią; odchylenia stają się \(a(x_i-\bar x)\), więc ich kwadraty mnożą się przez \(a^2\). Rozstęp i odchylenie wynikają z wartości bezwzględnej. \(\square\)

**T9 (średnia ważona w otoczce).** Dla wag z D9, \(\min x_i\le\bar x_w\le\max x_i\).
*Dowód.* Mnożymy nierówności \(m\le x_i\le M\) przez \(w_i\ge0\), sumujemy i dzielimy przez \(W>0\). \(\square\)

**T10 (łączenie grup).** Dla rozłącznych grup o licznościach \(n_1,n_2>0\):
\[
\bar x=\frac{n_1\bar x_1+n_2\bar x_2}{n_1+n_2}.
\]
*Dowód.* Suma obserwacji w każdej grupie wynosi \(n_j\bar x_j\). Dzielimy sumę obu grup przez łączną liczność. \(\square\)

**T11 (mediana minimalizuje sumę modułów).** Każda mediana uporządkowanej listy minimalizuje \(F(a)=\sum_i|x_i-a|\). Dla parzystego \(n\) wszystkie \(a\) między dwiema środkowymi obserwacjami minimalizują \(F\).
*Dowód.* Parujemy najmniejszą i największą obserwację, drugą najmniejszą i drugą największą itd. Dla pary \(u\le v\), nierówność trójkąta daje \(|u-a|+|v-a|\ge v-u\), z równością dokładnie dla \(a\in[u,v]\). Przecięcie przedziałów dla wszystkich par to przedział między dwiema środkowymi obserwacjami; przy nieparzystym \(n\) dodatkowy składnik \(|x_{((n+1)/2)}-a|\) wymusza środkową obserwację. \(\square\)

**T12 (wpływ jednej obserwacji na średnią).** Gdy wartość \(x_k\) zastępujemy \(x_k+\delta\), średnia wzrasta o \(\delta/n\).
*Dowód.* Suma wzrasta o \(\delta\), a liczność pozostaje \(n\). \(\square\)

**T13 (nierówność dla rozstępu i wariancji).** Jeśli wszystkie \(x_i\in[m,M]\), to \(V\le(M-m)^2/4\).
*Dowód.* Z \((x_i-m)(M-x_i)\ge0\) wynika \(x_i^2\le(m+M)x_i-mM\). Uśrednienie i T6 dają \(V\le(m+M)\bar x-mM-\bar x^2=(M-\bar x)(\bar x-m)\). Dla nieujemnych \(u=M-\bar x,v=\bar x-m\) mamy \(uv\le((u+v)/2)^2=(M-m)^2/4\). \(\square\)

**T14 (nierówność Czebyszewa dla skończonej listy).** Dla \(t>0\) i \(V\) z D7, udział obserwacji z \(|x_i-\bar x|\ge t\) nie przekracza \(V/t^2\).
*Dowód.* Niech \(k\) oznacza liczbę takich obserwacji. Suma kwadratów odchyleń jest co najmniej \(kt^2\). Zatem \(nV\ge kt^2\), czyli \(k/n\le V/t^2\). \(\square\)

**T15 (łączna wariancja dwóch grup).** Dla rozłącznych grup \(G_1,G_2\) o średnich \(\mu_j\), wariancjach populacyjnych \(V_j\), licznościach \(n_j\) i wspólnej średniej \(\mu\):
\[
V=\frac{n_1(V_1+(\mu_1-\mu)^2)+n_2(V_2+(\mu_2-\mu)^2)}{n_1+n_2}.
\]
*Dowód.* W każdej grupie rozwijamy \(x-\mu=(x-\mu_j)+(\mu_j-\mu)\); wyraz mieszany sumuje się do zera na mocy T3 zastosowanego do grupy. Sumujemy obie grupy i dzielimy przez całkowitą liczność. \(\square\)

**T16 (średnia nie determinuje rozproszenia).** Dwie listy mogą mieć tę samą średnią, a różne wariancje.
*Dowód przez konstrukcję.* Listy \((0,2)\) i \((1,1)\) mają średnią \(1\), lecz wariancje odpowiednio \(1\) i \(0\). \(\square\)

# C. Kontrprzykłady interpretacyjne

**K1.** Średnia \(1,1,1,9\) wynosi \(3\), ale żaden element listy nie jest równy \(3\).

**K2.** Mediana \(1,2,100\) to \(2\), a średnia \(103/3\); nie należy ich utożsamiać.

**K3.** Listy \(1,2,3\) i \(1,1,4\) mają tę samą średnią \(2\), lecz różne rozstępy i wariancje.

**K4.** Średnia dwóch średnich grup liczności \(1\) i \(9\) nie jest zwykle średnią całej próby: grupy \((100)\) oraz dziewięć zer dają \(10\), nie \(50\).

**K5.** Histogram o klasach różnej szerokości nie może być interpretowany tylko przez wysokości słupków, jeśli wysokości przedstawiają gęstości.

**K6.** Wartość odstająca według IQR nie jest automatycznie pomyłką pomiaru; może być poprawną, rzadką obserwacją.

**K7.** \(s^2\) nie istnieje dla \(n=1\) z definicji D8, mimo że \(V=0\) jest wtedy określone.

**K8.** Nie każda lista ma jedną dominantę: \(1,1,2,2\) ma dwie wartości modalne.

**K9.** Z dodatniej korelacji dwóch cech nie wynika związek przyczynowy; ukryta zmienna może wpływać na obie.

**K10.** Średnia arytmetyczna nie musi być dobrą miarą „typowej” wartości przy silnej asymetrii, np. \(1,1,1,1000\).

# D. Zadania z pełnymi rozwiązaniami
**Zadanie 1.** Wyznacz średnią 2,4,6,8.

*Rozwiązanie.* \((2+4+6+8)/4=5\).

**Zadanie 2.** Wyznacz medianę 8,1,4.

*Rozwiązanie.* Po uporządkowaniu \(1,4,8\), mediana to \(4\).

**Zadanie 3.** Wyznacz medianę 7,1,9,3.

*Rozwiązanie.* Po uporządkowaniu \(1,3,7,9\), mediana \((3+7)/2=5\).

**Zadanie 4.** Wyznacz dominantę 2,3,3,4,4,4.

*Rozwiązanie.* Liczność \(4\) jest największa, zatem moda \(4\).

**Zadanie 5.** Wyznacz wszystkie mody 1,1,2,2,3.

*Rozwiązanie.* Wartości \(1\) i \(2\) mają liczność \(2\), obie są modami.

**Zadanie 6.** Oblicz rozstęp 2,9,4,7.

*Rozwiązanie.* \(R=9-2=7\).

**Zadanie 7.** Zbuduj liczności dla 1,2,2,3,3,3.

*Rozwiązanie.* \(N(1)=1,N(2)=2,N(3)=3\), suma \(6\).

**Zadanie 8.** Wyznacz częstość względną wartości 3 z poprzedniego zadania.

*Rozwiązanie.* \(f(3)=3/6=1/2\).

**Zadanie 9.** Wyznacz wariancję populacyjną listy 1,3.

*Rozwiązanie.* Średnia \(2\), kwadraty odchyleń \(1,1\); \(V=(1+1)/2=1\).

**Zadanie 10.** Wyznacz odchylenie standardowe listy 1,3.

*Rozwiązanie.* \(\sigma=\sqrt1=1\).

**Zadanie 11.** Wyznacz wariancję populacyjną listy 2,2,2.

*Rozwiązanie.* Wszystkie odchylenia są zerowe, więc \(V=0\).

**Zadanie 12.** Wyznacz wariancję z poprawką Bessela dla 1,3.

*Rozwiązanie.* \(s^2=(1+1)/(2-1)=2\).

**Zadanie 13.** Czy dla listy jednoelementowej 7 istnieje wariancja z poprawką Bessela?

*Rozwiązanie.* Nie, mianownik \(n-1=0\); wariancja populacyjna wynosi \(0\).

**Zadanie 14.** Po dodaniu 10 do 1,3,5 znajdź nową średnią.

*Rozwiązanie.* Pierwotna średnia \(3\); nowa \(13\).

**Zadanie 15.** Po pomnożeniu 1,3 przez 4 oblicz nową wariancję.

*Rozwiązanie.* Pierwotna wariancja \(1\); nowa \(4^2\cdot1=16\).

**Zadanie 16.** Oblicz średnią ważoną ocen 3 (waga 1), 5 (waga 3).

*Rozwiązanie.* \((3\cdot1+5\cdot3)/4=18/4=9/2\).

**Zadanie 17.** Dwie grupy: 2 osoby średnia 8, 3 osoby średnia 3. Wyznacz średnią łączną.

*Rozwiązanie.* \((2\cdot8+3\cdot3)/5=25/5=5\).

**Zadanie 18.** Dane 1,2,3,4,5. Oblicz kwartyle przy przyjętej konwencji.

*Rozwiązanie.* Po wyłączeniu mediany \(3\), dolna połowa \(1,2\) ma medianę \(3/2\), górna \(4,5\) ma medianę \(9/2\).

**Zadanie 19.** Dla poprzedniej listy oblicz IQR.

*Rozwiązanie.* \(9/2-3/2=3\).

**Zadanie 20.** Dla danych 1,2,3,4,5 podaj granice Tukeya.

*Rozwiązanie.* \(Q_1-1{,}5IQR=1{,}5-4{,}5=-3\), \(Q_3+4{,}5=9\).

**Zadanie 21.** Wyznacz średnią 1,1,1,9.

*Rozwiązanie.* Suma \(12\), liczność \(4\), średnia \(3\).

**Zadanie 22.** Wyznacz medianę 1,1,1,9.

*Rozwiązanie.* Środkowe wartości to \(1,1\), więc mediana \(1\).

**Zadanie 23.** Oblicz sumę odchyleń od średniej listy 1,2,6.

*Rozwiązanie.* Średnia \(3\), suma \((-2)+(-1)+3=0\).

**Zadanie 24.** Wyznacz średnią listy 0,2 i porównaj z listą 1,1.

*Rozwiązanie.* Obie mają średnią \(1\), ale wariancje \(1\) i \(0\).

**Zadanie 25.** Wyznacz nową średnią, gdy w liście pięciu obserwacji jedną zwiększono o 20.

*Rozwiązanie.* Średnia wzrasta o \(20/5=4\).

**Zadanie 26.** Podaj przedział, w którym leży średnia danych 7,9,11.

*Rozwiązanie.* Z T2: w \([7,11]\); dokładnie \(\bar x=9\).

**Zadanie 27.** Sprawdź, czy dla listy 0,2 nierówność wariancyjna z T13 jest ostra.

*Rozwiązanie.* \(m=0,M=2,V=1=(M-m)^2/4\); zachodzi równość.

**Zadanie 28.** Dla listy 1,3,5 oblicz średnią i wariancję.

*Rozwiązanie.* \(\bar x=3\), \(V=(4+0+4)/3=8/3\).

**Zadanie 29.** Dla listy 1,3,5 wyznacz odsetek wartości w odległości co najmniej 2 od średniej.

*Rozwiązanie.* Dwie z trzech wartości: \(2/3\).

**Zadanie 30.** Wykaż, że średnia 10 liczb równych 7 wynosi 7.

*Rozwiązanie.* Suma \(70\), dzieląc przez \(10\) otrzymujemy \(7\).

**Zadanie 31.** Oblicz średnią liczb 1,2,3,4,5,6.

*Rozwiązanie.* Suma \(21\), więc \(\bar x=21/6=7/2\).

**Zadanie 32.** Oblicz wariancję populacyjną listy -1,1.

*Rozwiązanie.* Średnia \(0\), wariancja \((1+1)/2=1\).

**Zadanie 33.** Oblicz wariancję listy 2,4,6.

*Rozwiązanie.* Średnia \(4\), wariancja \((4+0+4)/3=8/3\).

**Zadanie 34.** Czy w liście 1,2,2,3 występuje jedna dominanta?

*Rozwiązanie.* Tak, wartość \(2\) ma największą liczność \(2\).

**Zadanie 35.** Zmień jednostkę z metrów na centymetry: jak zmienia się wariancja?

*Rozwiązanie.* Każda wartość mnoży się przez \(100\); wariancja przez \(100^2=10000\).

**Zadanie 36.** Porównaj średnie grup (100) i (0,0,0,0,0,0,0,0,0).

*Rozwiązanie.* Średnia pierwszej \(100\), drugiej \(0\), a łączna \((100+0)/10=10\).

# E. Problemy i komentarz metodologiczny

**Problem 1 (dwie metody).** Dla danych \(1,2,3,4\) oblicz wariancję bezpośrednio i wzorem T6.

*Rozwiązanie.* Średnia \(5/2\). Kwadraty odchyleń: \(9/4,1/4,1/4,9/4\), suma \(5\), więc \(V=5/4\). Alternatywnie \(\frac{1+4+9+16}{4}-(5/2)^2=30/4-25/4=5/4\).

**Problem 2 (łączenie wariancji).** Grupa A ma dane \(0,2\), grupa B dane \(4,6\). Oblicz średnią i wariancję łączną za pomocą T15.

*Rozwiązanie.* Każda grupa ma wariancję \(1\), średnie \(1\) i \(5\), a wspólna średnia wynosi \(3\). Wariancja łączna to \([2(1+4)+2(1+4)]/4=5\). Bezpośrednio odchylenia \(-3,-1,1,3\) mają kwadraty \(9,1,1,9\); średnia \(20/4=5\).

**Problem 3 (dane i wniosek).** Wyniki pięciu pomiarów wynoszą \(4,4,4,4,20\). Oblicz średnią, medianę i wskaż ograniczenie interpretacji.

*Rozwiązanie.* Średnia \(36/5=7{,}2\), mediana \(4\). Średnia reaguje na pojedynczą dużą wartość; bez kontekstu pomiaru nie wolno usuwać wartości \(20\) ani nazywać jej błędem.

**Granice odbioru.** Twierdzenia o wariancji dotyczą *opisowej wariancji listy*, nie estymacji parametrów populacji na podstawie losowej próby. Reguła kwartylowa jest konwencją redakcyjną, a granice Tukeya heurystyką. Testy liczbowe nie są formalnym dowodem wszystkich twierdzeń. Bez integracji z monolitem 0.20 nie zwiększamy historycznych 585 stron. Cel 1222 stron nie obowiązuje, końcowy PDF tomu ma mieć mniej niż 99 000 000 bajtów. Nie zmieniono wstępu historycznego.
