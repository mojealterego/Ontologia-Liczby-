---
title: "ONTOLOGIA LICZBY — Tom I"
subtitle: "MSC 97C30. Procesy poznawcze i matematyczne modele uczenia się"
author: "Andrzej Mikulski"
date: "2026-11-02"
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Metryka redakcyjna.** MSC2020 **97C30 — Cognitive processes, learning theories (aspects of mathematics education)**; rodzina G, autorski poziom I, źródłowa taksonomia s. 10, minimum cztery strony rzeczywistej treści. Rozdział opisuje ścisłe *modele matematyczne* zależności pojęciowych, obserwacji i zapamiętywania. Model nie jest automatycznie teorią psychologiczną potwierdzoną eksperymentem. W szczególności wynik testu nie jest bezpośrednim pomiarem stanu umysłu, a korelacja nie dowodzi wpływu metody nauczania. Tekst stanowi nowy dodatek; nie zmienia historycznego wstępu ani wcześniejszych rozdziałów.

# 1. Definicje: pojęcia, obserwacje, czas

**D01 (graf wymagań).** Niech $V$ będzie skończonym zbiorem umiejętności. Skierowana krawędź $u\to v$ oznacza, że w *przyjętym modelu dydaktycznym* opanowanie $u$ jest wymagane przed nauką $v$. Zakładamy, że graf $G=(V,E)$ jest acykliczny (DAG). Nie twierdzimy, że każda rzeczywista droga uczenia się jest liniowa.

**D02 (domknięcie wymagań).** Dla $A\subseteq V$ zbiór $\operatorname{Cl}(A)$ zawiera $A$ oraz wszystkie wierzchołki, z których prowadzi skierowana ścieżka do jakiegoś $a\in A$. Ścieżka długości zero dopuszcza $a$ samo. Domknięcie opisuje wymagania *transytywne*, a nie tylko bezpośrednich poprzedników.

**D03 (stan zgodny z wymaganiami).** $M\subseteq V$ jest *stanem dopuszczalnym*, gdy $\operatorname{Cl}(M)=M$. Stan dopuszczalny to ideał porządku częściowego wyznaczonego osiągalnością w DAG. Stan ucznia w praktyce może być niezgodny z takim uproszczeniem, np. dzięki nieformalnej intuicji.

**D04 (porządek nauczania).** Porządek topologiczny jest permutacją $v_1,\ldots,v_n$ zbioru $V$, w której każda krawędź $u\to v$ ma $u$ wcześniej niż $v$.

**D05 (rodzina stanów).** $\mathcal I(G)=\{M\subseteq V:\operatorname{Cl}(M)=M\}$ jest rodziną wszystkich stanów dopuszczalnych.

**D06 (koszt nowych wymagań).** Dla dopuszczalnego $M$ i $v\in V$ definiujemy $c(v\mid M)=|\operatorname{Cl}(\{v\})\setminus M|$. Jest to liczba *nowych węzłów*, nie czas nauki ani jej rzeczywisty wysiłek.

**D07 (obserwacja zadania).** $K\in\{0,1\}$ jest ukrytym stanem opanowania jednej umiejętności w danej chwili, a $R\in\{0,1\}$ obserwowanym wynikiem zadania. $K$ nie jest obserwowany bezpośrednio.

**D08 (parametry testu).** $s=P(R=1\mid K=1)$ jest czułością zadania, a $t=P(R=0\mid K=0)$ swoistością. Zakładamy $0<s,t<1$; te parametry wymagają kalibracji i mogą zależeć od populacji.

**D09 (wiara przed obserwacją).** $p=P(K=1)$, gdzie $0<p<1$, jest prawdopodobieństwem w *określonym modelu*. Iloraz $p/(1-p)$ nazywamy szansą (*odds*).

**D10 (dwustanowy model nauki i zapominania).** W dyskretnym kroku stan $0$ przechodzi do $1$ z prawdopodobieństwem $\ell\in(0,1)$, a stan $1$ do $0$ z prawdopodobieństwem $f\in(0,1)$. Jeśli $p_n=P(K_n=1)$, zakładamy jednorodny łańcuch Markowa. Parametry nie są uniwersalnymi stałymi uczenia się.

**D11 (retencja).** Funkcja $r_\lambda(t)=e^{-\lambda t}$ dla $t\ge0$ i $\lambda>0$ modeluje prawdopodobieństwo zachowania określonego śladu w czasie $t$ bez powtórki. Nie jest to prawo empiryczne dla każdego ucznia i każdej treści.

**D12 (harmonogram powtórek).** Dla ustalonego horyzontu $T>0$ harmonogram z $n$ przerwami opisują $\Delta_i>0$ i $\sum_{i=1}^n\Delta_i=T$. W modelu resetowania śladu każda powtórka przywraca retencję do $1$.

**D13 (budżet obciążenia).** Zadanie $i$ ma umowny koszt $w_i>0$, a sesja budżet $B>0$. Zbiór zadań $S$ jest dopuszczalny, gdy $\sum_{i\in S}w_i\le B$. Koszty nie są automatycznie mierzalnymi jednostkami neuropsychologicznymi.

**D14 (krzywa odpowiedzi).** $\sigma(x)=1/(1+e^{-x})$; w prostym modelu odpowiedzi $P(R=1\mid\theta,b)=\sigma(\theta-b)$, gdzie $\theta$ jest parametrem kompetencji, a $b$ parametrem trudności. Bez dodatkowych ograniczeń oba parametry mają wspólną nieidentyfikowalną translację.

**D15 (entropia binarna).** Dla $p\in[0,1]$ definiujemy $H(p)=-p\log_2p-(1-p)\log_2(1-p)$, z konwencją $0\log_2 0=0$. Jest to miara niepewności rozkładu Bernoulliego, a nie bezpośrednia miara jakości myślenia.

# 2. Twierdzenia z dowodami

**T01 (własności domknięcia).** Dla $A,B\subseteq V$ zachodzi: $A\subseteq\operatorname{Cl}(A)$; jeśli $A\subseteq B$, to $\operatorname{Cl}(A)\subseteq\operatorname{Cl}(B)$; oraz $\operatorname{Cl}(\operatorname{Cl}(A))=\operatorname{Cl}(A)$.

*Dowód.* Pierwsza inkluzja wynika ze ścieżek długości zero. Każda ścieżka do elementu $A$ jest także ścieżką do elementu $B$ przy $A\subseteq B$. Jeżeli $x$ prowadzi ścieżką do $y\in\operatorname{Cl}(A)$, a $y$ do $a\in A$, konkatenacja ścieżek prowadzi $x$ do $a$. Stąd domknięcie domknięcia nie dodaje węzłów; odwrotna inkluzja wynika z pierwszej własności. $\square$

**T02 (stany tworzą kratę dystrybutywną).** Jeśli $M,N\in\mathcal I(G)$, to $M\cap N$ i $M\cup N$ należą do $\mathcal I(G)$, a operacje przecięcia i sumy zbiorów spełniają prawa rozdzielności.

*Dowód.* Poprzednik dowolnego elementu $M\cap N$ należy jednocześnie do obu stanów; poprzednik elementu $M\cup N$ należy do tego stanu, z którego pochodzi element. Oba zbiory są zatem domknięte. Prawa rozdzielności są standardowymi tożsamościami zbiorowymi. $\square$

**T03 (istnienie kolejności nauczania).** Każdy skończony DAG ma porządek topologiczny.

*Dowód.* W niepustym skończonym DAG istnieje wierzchołek bez krawędzi wchodzących: gdyby każdy miał poprzednika, powtarzając wybór poprzedników w skończonym zbiorze, otrzymalibyśmy cykl. Usuwamy taki wierzchołek i stosujemy indukcję do pozostałego DAG. Wstawienie usuniętego wierzchołka na początek daje wymagany porządek. $\square$

**T04 (najmniejsze rozszerzenie stanu).** Dla $M\in\mathcal I(G)$ i $v\in V$ zbiór $M'=M\cup\operatorname{Cl}(\{v\})$ jest najmniejszym względem inkluzji stanem dopuszczalnym zawierającym $M\cup\{v\}$.

*Dowód.* Na mocy T02 suma dwóch zbiorów domkniętych jest domknięta. Każdy stan dopuszczalny zawierający $v$ zawiera wszystkich jego poprzedników, czyli $\operatorname{Cl}(\{v\})$; z założenia zawiera też $M$. Musi więc zawierać $M'$. $\square$

**T05 (malejący koszt nowych wymagań).** Jeśli $M\subseteq N$ są stanami dopuszczalnymi, to $c(v\mid N)\le c(v\mid M)$ dla każdego $v$.

*Dowód.* $\operatorname{Cl}(\{v\})\setminus N\subseteq\operatorname{Cl}(\{v\})\setminus M$. Zbiory są skończone, więc nierówność ich liczebności daje tezę. $\square$

**T06 (niezgodność cyklu z porządkiem topologicznym).** Jeśli skierowany graf zawiera cykl $v_1\to\cdots\to v_k\to v_1$, to nie istnieje jego porządek topologiczny.

*Dowód.* Porządek musiałby umieścić $v_1$ przed $v_2$, ..., $v_k$ przed $v_1$, co jest sprzeczne z przechodniością ścisłego porządku liniowego. $\square$

**T07 (iloraz szans po odpowiedzi dodatniej).** Przy D07–D09 i $P(R=1)>0$:
\[
\frac{P(K=1\mid R=1)}{P(K=0\mid R=1)}=\frac p{1-p}\frac{s}{1-t}.
\]

*Dowód.* Z definicji prawdopodobieństwa warunkowego licznik i mianownik po prawej stronie reguły Bayesa mają wspólny dzielnik $P(R=1)$, który się skraca. $\square$

**T08 (kiedy sukces podwyższa ocenę opanowania).** Dla $0<p<1$ obserwacja $R=1$ zwiększa posterior $P(K=1\mid R=1)$ ponad $p$ wtedy i tylko wtedy, gdy $s>1-t$.

*Dowód.* Szanse $p/(1-p)$ są ściśle rosnącą funkcją $p$. Na mocy T07 ich iloraz po obserwacji jest mnożony przez $s/(1-t)$, większy od $1$ dokładnie przy wskazanej nierówności. $\square$

**T09 (aktualizacja po niezależnych warunkowo próbach).** Jeśli $R_1,\ldots,R_m$ są warunkowo niezależne przy ustalonym $K$, a każda próba ma parametry $s,t$, to po $m$ sukcesach posterior odds równa się $\frac p{1-p}\big(\frac{s}{1-t}\big)^m$.

*Dowód.* Warunkowa niezależność daje $P(R_1=\cdots=R_m=1\mid K=1)=s^m$ i analogicznie $(1-t)^m$ dla $K=0$. Stosujemy dowód T07 do zdarzenia łącznego. $\square$

**T10 (prognoza odpowiedzi).** Przy D07–D09 $P(R=1)=sp+(1-t)(1-p)$.

*Dowód.* Rozbijamy zdarzenie $\{R=1\}$ na rozłączne części z $K=1$ i $K=0$, a następnie stosujemy wzór na prawdopodobieństwo warunkowe. $\square$

**T11 (punkt stały i zbieżność modelu dwustanowego).** W D10:
\[
p_{n+1}=(1-\ell-f)p_n+\ell,\quad p_*={\ell\over\ell+f},\quad p_n-p_*=(1-\ell-f)^n(p_0-p_*).
\]
Dla $0<\ell,f<1$ zachodzi $p_n\to p_*$.

*Dowód.* Stan opanowany w kolejnym kroku pochodzi z przejścia $0\to1$ lub pozostania $1\to1$, więc $p_{n+1}=\ell(1-p_n)+(1-f)p_n$. Rozwiązanie równania punktu stałego daje $p_*$. Po odjęciu tego równania otrzymujemy rekurencję geometryczną. Ponieważ $-1<1-\ell-f<1$, potęga zbiega do zera. $\square$

**T12 (retencja i czas połowiczny).** Dla $r_\lambda(t)=e^{-\lambda t}$ zachodzi $r_\lambda(t+u)=r_\lambda(t)r_\lambda(u)$ oraz $t_{1/2}=\ln 2/\lambda$.

*Dowód.* Pierwsza tożsamość wynika z prawa dodawania wykładników. Równanie $e^{-\lambda t}=1/2$ po zlogarytmowaniu daje drugą. $\square$

**T13 (równe przerwy w modelu resetowania).** Przy D12 największa przerwa spełnia $\max_i\Delta_i\ge T/n$. W modelu resetowania, gdy jakość harmonogramu to najmniejsza retencja bezpośrednio przed powtórką, równe przerwy $\Delta_i=T/n$ maksymalizują tę najniższą retencję.

*Dowód.* Gdyby wszystkie przerwy były mniejsze od $T/n$, ich suma byłaby mniejsza od $T$. Najniższa retencja jest równa $e^{-\lambda\max_i\Delta_i}$, ponieważ wykładnik jest funkcją malejącą długości przerwy. Minimalna możliwa wartość maksimum przerw wynosi $T/n$ i jest osiągana przy równych przerwach. $\square$

**T14 (monotoniczność wykonalności obciążenia).** Jeżeli $S$ jest wykonalne w D13, to każdy $A\subseteq S$ jest wykonalny. Nie wynika z tego optymalność zachłannego wyboru zadań według największej pojedynczej wartości.

*Dowód.* Wszystkie koszty są dodatnie, więc $\sum_{i\in A}w_i\le\sum_{i\in S}w_i\le B$. Druga część zostanie obalona przez konkretny kontrprzykład K09. $\square$

**T15 (symetria i maksymalna pochodna funkcji logistycznej).** Dla $x\in\mathbb R$ zachodzi $\sigma(-x)=1-\sigma(x)$ i $0<\sigma'(x)=\sigma(x)(1-\sigma(x))\le1/4$.

*Dowód.* Przekształcenie $1/(1+e^x)=1-1/(1+e^{-x})$ daje symetrię. Różniczkowanie daje wzór na pochodną. Dla $q\in(0,1)$ mamy $q(1-q)=1/4-(q-1/2)^2\le1/4$, z równością przy $x=0$. $\square$

**T16 (granice entropii binarnej).** Dla $p\in[0,1]$ zachodzi $0\le H(p)\le1$ bit; maksimum występuje tylko przy $p=1/2$, a minimum przy $p\in\{0,1\}$.

*Dowód.* Każdy składnik $-q\log_2q$ jest nieujemny dla $q\in[0,1]$. Dla $0<p<1$ mamy $H'(p)=\log_2((1-p)/p)$ i $H''(p)=-1/(p(1-p)\ln2)<0$. Jedyny punkt krytyczny to $p=1/2$, gdzie $H=1$. W końcach, na mocy przyjętej konwencji, $H=0$. $\square$

# 3. Kontrprzykłady i granice stosowalności

**K01 (cykl wymagań).** Krawędzie $a\to b$ i $b\to a$ uniemożliwiają porządek topologiczny. Model wymagający DAG musi wykrywać i odrzucać taki graf, a nie arbitralnie ukrywać cykl.

**K02 (poprzednik pośredni).** Dla $a\to b\to c$ bezpośrednim poprzednikiem $c$ jest $b$, ale $\operatorname{Cl}(\{c\})=\{a,b,c\}$. Sprawdzanie tylko krawędzi bezpośrednich pomija $a$.

**K03 (stan niedomknięty).** Dla $a\to b$ zbiór $\{b\}$ nie jest stanem dopuszczalnym; sam wynik zadania dotyczącego $b$ nie gwarantuje opanowania $a$.

**K04 (wielość poprawnych kolejności).** Dla dwóch niezależnych węzłów $a,b$ zarówno $(a,b)$, jak i $(b,a)$ jest porządkiem topologicznym. Graf nie wymusza jednej ścieżki uczenia się.

**K05 (graf nie jest przyczynowością).** Krawędź $a\to b$ w modelu dydaktycznym nie dowodzi, że nauczanie $a$ przyczynowo zwiększa wynik w $b$; wymagany byłby odpowiedni projekt badawczy.

**K06 (sukces przy niskim prawdopodobieństwie opanowania).** Dla $p=1/100$, $s=9/10$, $t=9/10$ pojedynczy sukces daje posterior $1/12\approx0{,}0833$, a nie $90\%$. Bazowa częstość ma znaczenie.

**K07 (zależne odpowiedzi).** Dwa identycznie skopiowane wyniki tego samego zadania nie są dwiema warunkowo niezależnymi obserwacjami. Podwojenie ilorazu wiarygodności byłoby nieuprawnione.

**K08 (nieidentyfikowalność skali).** W D14 pary $(\theta,b)=(2,1)$ i $(102,101)$ dają to samo $P(R=1)=\sigma(1)$. Sam pojedynczy wynik nie identyfikuje obu parametrów.

**K09 (zachłanność zawodzi).** Budżet $B=10$, zadania: $A$ ma koszt $6$ i wartość $9$, $B$ i $C$ mają koszt $5$ i wartość $8$ każde. Wybór zadania o największej pojedynczej wartości daje $A$ i wartość $9$, podczas gdy $\{B,C\}$ ma wartość $16$.

**K10 (retencja i psychologia).** Z T13 nie wynika, że równe odstępy są optymalne w realnej nauce: jeśli powtórki zmieniają $\lambda$, istnieje zmęczenie albo skuteczność zależy od trudności, założenie resetowania przestaje obowiązywać.

# 4. Zadania z pełnymi rozwiązaniami

**Z01.** W grafie $a\to b$, $a\to c$, $b\to d$, $c\to d$ wyznacz $\operatorname{Cl}(\{d\})$. **Rozwiązanie:** poprzednikami $d$ są $b,c$, a obu poprzedza $a$. Zatem domknięcie to $\{a,b,c,d\}$.

**Z02.** Ile stanów dopuszczalnych ma łańcuch $a\to b\to c$? **Rozwiązanie:** są to $\varnothing,\{a\},\{a,b\},\{a,b,c\}$, więc dokładnie $4$.

**Z03.** Podaj kolejność topologiczną grafu z Z01. **Rozwiązanie:** $(a,b,c,d)$, gdyż każda krawędź biegnie od elementu wcześniejszego do późniejszego; również $(a,c,b,d)$ jest poprawna.

**Z04.** W grafie z Z01 uczeń ma stan $M=\{a,b\}$. Ile nowych węzłów wymaga $d$? **Rozwiązanie:** $\operatorname{Cl}(\{d\})\setminus M=\{c,d\}$, więc $c(d\mid M)=2$.

**Z05.** Dla $M=\{a,b\}$ i $N=\{a,c\}$ w grafie z Z01 oblicz sumę i przecięcie. **Rozwiązanie:** $M\cup N=\{a,b,c\}$ i $M\cap N=\{a\}$. Oba są domknięte.

**Z06.** Przy $p=1/4$, $s=4/5$, $t=9/10$ oblicz $P(K=1\mid R=1)$. **Rozwiązanie:** $sp=1/5$, $(1-t)(1-p)=3/40$, więc wynik to $(1/5)/(11/40)=8/11$.

**Z07.** Dla parametrów z Z06 oblicz $P(K=1\mid R=0)$. **Rozwiązanie:** $(1-s)p=1/20$, $t(1-p)=27/40$, więc wynik to $(1/20)/(29/40)=2/29$.

**Z08.** Wyznacz posterior odds po sukcesie z Z06. **Rozwiązanie:** prior odds $=1/3$, iloraz wiarygodności $=(4/5)/(1/10)=8$, więc posterior odds $=8/3$ i posterior $=8/11$.

**Z09.** Przy dwóch warunkowo niezależnych sukcesach z parametrami Z06 oblicz posterior. **Rozwiązanie:** posterior odds $=(1/3)\cdot8^2=64/3$, zatem posterior $=64/67$.

**Z10.** Oblicz prawdopodobieństwo sukcesu w Z06 przed obserwacją. **Rozwiązanie:** $sp+(1-t)(1-p)=1/5+3/40=11/40$.

**Z11.** Dla $\ell=1/5$, $f=1/10$ wyznacz punkt stały. **Rozwiązanie:** $p_*=(1/5)/(3/10)=2/3$.

**Z12.** Dla $p_0=1/3$ oraz parametrów Z11 wyznacz $p_1$. **Rozwiązanie:** $p_1=(7/10)(1/3)+1/5=13/30$.

**Z13.** Wyznacz $p_2$ z Z12. **Rozwiązanie:** $p_2=(7/10)(13/30)+1/5=151/300$.

**Z14.** Dla $\lambda=\ln 2/4$ oblicz retencję po $8$ jednostkach czasu. **Rozwiązanie:** $r_\lambda(8)=e^{-2\ln2}=1/4$.

**Z15.** Rozłóż horyzont $T=12$ na $n=3$ przerwy minimalizujące najdłuższą przerwę. **Rozwiązanie:** przerwy $(4,4,4)$ dają maksimum $4$, a T13 dowodzi, że mniejsze maksimum jest niemożliwe.

**Z16.** Budżet $10$, koszty $6,5,4$. Czy można wybrać pierwsze i trzecie zadanie? **Rozwiązanie:** $6+4=10\le10$, zatem tak; wszystkich trzech nie można, bo suma wynosi $15$.

**Z17.** Znajdź lepszy zestaw od zachłannego w K09. **Rozwiązanie:** $\{B,C\}$ kosztuje $5+5=10$ i daje $8+8=16>9$.

**Z18.** Dla $\theta=b$ oblicz szansę sukcesu w D14. **Rozwiązanie:** $\sigma(\theta-b)=\sigma(0)=1/2$.

**Z19.** Dla $\theta-b=\ln3$ oblicz szansę sukcesu. **Rozwiązanie:** $\sigma(\ln3)=1/(1+1/3)=3/4$.

**Z20.** Oblicz entropię przy $p=1/2$ oraz $p=1$. **Rozwiązanie:** $H(1/2)=-(1/2)(-1)-(1/2)(-1)=1$ bit; $H(1)=0$ bit według konwencji granicznej.

# 5. Ograniczenia i protokół walidacji

W modelu grafowym należy najpierw jawnie uzasadnić krawędzie wymagań, a następnie testować, czy wybrane zależności przewidują trudności uczniów poza próbą, na której je zbudowano. Poprawność algorytmu domknięcia nie dowodzi poprawności pedagogicznego wyboru krawędzi. W modelu Bayesa parametry $p,s,t$ powinny być estymowane lub kalibrowane, a nie dobierane dla uzyskania oczekiwanej diagnozy. T09 wymaga niezależności warunkowej; powtórne podanie tego samego zadania może ją naruszać. W modelu Markowa stałość $\ell,f$ jest silnym uproszczeniem: interwencje, przerwy i rodzaj zadań mogą je zmieniać. Model wykładniczej retencji nie powinien zastępować danych z odroczonych pomiarów.

**Granica dowodowa.** T01–T16 są twierdzeniami o podanych strukturach matematycznych. Z01–Z20 są przykładami rachunkowymi, a testy komputerowe sprawdzają tylko skończony zestaw przypadków. Żadne z nich samo nie dowodzi, że opisany mechanizm jest przyczynową teorią uczenia się u ludzi. Taki wniosek wymaga osobnej metodologii empirycznej, oceny błędu pomiaru, kontroli doboru próby i replikacji.

**Literatura orientacyjna.** B. Bloom (1968), *Learning for Mastery*; A. Newell, H. Simon (1972), *Human Problem Solving*; J. R. Anderson, A. T. Corbett, K. R. Koedinger, R. Pelletier (1995), *Cognitive Tutors: Lessons Learned*; A. T. Corbett, J. R. Anderson (1995), *Knowledge Tracing: Modeling the Acquisition of Procedural Knowledge*; J. Sweller (1988), *Cognitive Load During Problem Solving*; R. Bjork, E. Bjork (1992), *A New Theory of Disuse and an Old Theory of Stimulus Fluctuation*. Pozycje te są kontekstem historycznym modeli, nie dowodem ich uniwersalnej poprawności.
