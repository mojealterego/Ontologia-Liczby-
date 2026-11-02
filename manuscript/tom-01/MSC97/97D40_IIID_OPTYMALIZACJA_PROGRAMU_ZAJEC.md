# MSC 97D40 — Rozszerzenie III-D: optymalizacja programu zajęć i sprawiedliwy dostęp do treści

**Tom I — opracowanie matematyczne.** Kontynuacja D01–D36, T01–T42, K01–K22 i Z01–Z50. Wszystkie wartości zadań i ograniczenia są elementami modelu, nie pomiarami skuteczności dydaktycznej.

## 8.1. Definicje i modele

**D37 (problem plecakowy lekcji).** Dla $n$ zadań, całkowitych kosztów $c_i\in\mathbb N_{>0}$, wartości $v_i\ge0$ i całkowitego budżetu $B\ge0$ szukamy $I\subseteq\{1,\ldots,n\}$ maksymalizującego $\sum_{i\in I}v_i$ przy $\sum_{i\in I}c_i\le B$.

**D38 (stan dynamiczny).** $F_i(b)$ oznacza maksymalną wartość dopuszczalnego wyboru spośród pierwszych $i$ zadań przy budżecie $b\in\{0,\ldots,B\}$.

**D39 (relaksacja ułamkowa).** W relaksacji D37 zmienne $x_i\in\{0,1\}$ zastępujemy przez $0\le x_i\le1$, zachowując $\sum_i c_ix_i\le B$.

**D40 (zadanie zdominowane).** Rozwiązanie $I$ dominuje $J$, gdy $c(I)\le c(J)$ i $v(I)\ge v(J)$, przy co najmniej jednej ostrej nierówności.

**D41 (front Pareto).** Front Pareto to rodzina rozwiązań niezdominowanych w sensie D40.

**D42 (pokrycie programu).** Dla uniwersum kompetencji $U$ i zbiorów $C_i\subseteq U$ definiujemy $C(I)=\bigcup_{i\in I}C_i$.

**D43 (minimalny koszt pełnego pokrycia).** Szukamy $I$ minimalizującego $\sum_{i\in I}c_i$ przy $C(I)=U$; jeśli nie ma takiego wyboru, koszt wynosi $+\infty$.

**D44 (maska pokrycia).** Przy $|U|=m$ identyfikujemy $C(I)$ z maską $M\in\{0,1\}^m$, a sumę zbiorów z bitowym OR.

**D45 (losowy plan niezależny).** Każde zadanie $i$ włączamy niezależnie z prawdopodobieństwem $p_i\in[0,1]$.

**D46 (prawdopodobieństwo objęcia kompetencji).** Dla $u\in U$ niech $q_u=P(u\in C(I))$ w losowym planie D45.

## 8.2. Twierdzenia z dowodami

**T43 (rekurencja plecakowa).** Dla $i\ge1$ zachodzi
$$F_i(b)=\begin{cases}F_{i-1}(b),&c_i>b,\\\max\{F_{i-1}(b),F_{i-1}(b-c_i)+v_i\},&c_i\le b,\end{cases}$$
przy $F_0(b)=0$.

*Dowód.* Każdy wybór albo pomija zadanie $i$ i osiąga najwyżej $F_{i-1}(b)$, albo je zawiera, pozostawiając budżet $b-c_i$ na pierwsze $i-1$ zadań. Oba warianty są osiągalne przez optymalne wybory z podproblemów. Maksimum daje dokładne optimum. $\square$

**T44 (złożoność programowania dynamicznego).** D37 można rozwiązać dokładnie w czasie $O(nB)$ i pamięci $O(B)$, jeśli koszty i budżet są całkowite.

*Dowód.* T43 wyznacza $(n+1)(B+1)$ stanów, każdy w czasie stałym. Dla kolejnych zadań wystarczy tablica $F(b)$ aktualizowana po budżetach malejąco, aby użyć każdego zadania co najwyżej raz. Liczba komórek wynosi $B+1$. Jest to algorytm pseudowielomianowy: $B$ może być wykładniczy względem długości zapisu binarnego. $\square$

**T45 (monotoniczność budżetu).** Jeśli $B_1\le B_2$, to $\operatorname{OPT}(B_1)\le\operatorname{OPT}(B_2)$.

*Dowód.* Każdy plan dopuszczalny przy $B_1$ jest dopuszczalny przy $B_2$. Maksimum po większym zbiorze nie może być mniejsze. $\square$

**T46 (relaksacja daje górne ograniczenie).** Wartość optimum ułamkowego $R$ jest nie mniejsza niż optimum całkowitoliczbowe $O$.

*Dowód.* Każdy wektor binarny dopuszczalny w D37 spełnia także warunki relaksacji D39, zatem jej zbiór dopuszczalny jest nadzbiorem. $\square$

**T47 (ograniczenie relaksacji przez dwa).** Załóżmy $c_i\le B$ dla wszystkich zadań, $B>0$ i $v_i\ge0$. Wtedy $R\le2O$.

*Dowód.* Uporządkujmy zadania malejąco według $v_i/c_i$. Istnieje optimum relaksacji, które bierze pewien prefiks zadań w całości i co najwyżej jedno dalsze zadanie ułamkowo: wymiana dodatniej masy z mniejszego ilorazu na większy nie zmniejsza wartości. Niech wartość pełnego prefiksu wynosi $P$, a wartość ewentualnego zadania ułamkowego $\alpha v_j$, $0\le\alpha<1$. Prefiks jest dopuszczalnym planem całkowitym, więc $P\le O$. Samo zadanie $j$ jest dopuszczalne na mocy $c_j\le B$, zatem $\alpha v_j\le v_j\le O$. Stąd $R=P+\alpha v_j\le2O$. Gdy nie ma części ułamkowej, $R=O$. $\square$

**T48 (gwarancja połowy optimum).** W warunkach T47 wybór lepszego z dwóch planów: pełnego prefiksu relaksacji albo samego zadania ułamkowego, daje wartość co najmniej $O/2$.

*Dowód.* Z T46 i rozkładu $R=P+\alpha v_j\le P+v_j$ wynika $O\le P+v_j\le2\max(P,v_j)$. Oba kandydaty są dopuszczalne. Jeśli brak zadania ułamkowego, prefiks jest optymalny. $\square$

**T49 (bezpieczne odrzucanie dominowanych planów).** Dla danego budżetu, jeśli $I$ dominuje $J$, to w maksymalizacji wartości można odrzucić $J$ bez zmniejszenia optimum.

*Dowód.* Gdy $J$ jest dopuszczalny, $c(I)\le c(J)\le B$, więc $I$ także jest dopuszczalny i $v(I)\ge v(J)$. Wystarczy zastąpić $J$ przez $I$. $\square$

**T50 (rekurencja kosztu pokrycia).** Niech $G_i(M)$ oznacza minimalny koszt uzyskania dokładnie maski $M$ za pomocą pierwszych $i$ zadań. Wtedy $G_0(0)=0$, $G_0(M)=+\infty$ dla $M\ne0$, a przejścia z każdego stanu $M$ to pominięcie zadania $i$ lub przejście do $M\operatorname{OR}C_i$ za koszt $c_i$.

*Dowód.* Każdy podzbiór pierwszych $i$ zadań jednoznacznie dzieli się na podzbiory zawierające i niezawierające zadania $i$. W pierwszym przypadku maska jest sumą bitową maski poprzedniego wyboru i $C_i$, a koszt rośnie o $c_i$. Indukcja po $i$ daje dokładne minima. $\square$

**T51 (złożoność pokrycia przez maski).** Dla $m=|U|$ i $n$ zadań algorytm T50 działa w czasie $O(n2^m)$ i pamięci $O(2^m)$.

*Dowód.* Istnieje $2^m$ masek. Każde zadanie wykonuje co najwyżej dwa przejścia z każdej maski. Wystarczą dwie warstwy tablic lub kopia tablicy przy każdym zadaniu. $\square$

**T52 (dolne ograniczenie liczby zadań).** Jeżeli każde $C_i$ zawiera co najwyżej $r>0$ kompetencji, a $|U|=m$, każdy plan pełnego pokrycia zawiera co najmniej $\lceil m/r\rceil$ zadań.

*Dowód.* Dla planu $I$ zachodzi $m=|C(I)|\le\sum_{i\in I}|C_i|\le r|I|$. Dzielimy przez $r$ i zaokrąglamy w górę. $\square$

**T53 (dokładne prawdopodobieństwo pokrycia).** W D45 dla dowolnego $u\in U$:
$$q_u=1-\prod_{i:u\in C_i}(1-p_i),$$
przy konwencji, że iloczyn pusty wynosi $1$.

*Dowód.* Kompetencja $u$ pozostaje nieobjęta dokładnie wtedy, gdy nie wybrano żadnego zadania ją zawierającego. Niezależność wyborów pozwala pomnożyć prawdopodobieństwa niewybrania. Bierzemy dopełnienie. $\square$

**T54 (ograniczenie wykładnicze braku pokrycia).** Dla każdego $u\in U$ zachodzi
$$P(u\notin C(I))\le\exp\!\left(-\sum_{i:u\in C_i}p_i\right).$$

*Dowód.* Z T53 prawdopodobieństwo nieobjęcia to iloczyn $(1-p_i)$. Dla $p_i\in[0,1]$ mamy $1-p_i\le e^{-p_i}$. Mnożąc nierówności otrzymujemy tezę. $\square$

**T55 (wartość oczekiwana losowego pokrycia).** Dla wag $w_u\ge0$:
$$\mathbb E\left[\sum_{u\in C(I)}w_u\right]=\sum_{u\in U}w_u\left(1-\prod_{i:u\in C_i}(1-p_i)\right).$$

*Dowód.* Wprowadzamy wskaźnik $Y_u=\mathbf1_{\{u\in C(I)\}}$ i korzystamy z liniowości wartości oczekiwanej oraz T53. Nie jest potrzebna niezależność wskaźników $Y_u$. $\square$

## 8.3. Kontrprzykłady

**K23 (zachłanność względem wartości).** Przy budżecie $10$ i zadaniach $(c,v)=(6,9),(5,8),(5,8)$ wybór zadania o największej wartości daje $9$, podczas gdy wybór dwóch pozostałych daje $16$.

**K24 (koszt całkowity a zapis binarny).** Algorytm $O(nB)$ nie jest ogólnie wielomianowy względem długości wejścia: liczba $B=2^k$ ma $k+1$ bitów, lecz wymaga $2^k+1$ stanów budżetu.

**K25 (dominacja pojedynczych zadań nie wystarcza).** Dwa zadania o pokryciach $\{a\}$ i $\{b\}$ mogą razem pokrywać $\{a,b\}$; usunięcie jednego z nich na podstawie samej liczby pokrytych kompetencji może zniszczyć jedyny pełny plan.

**K26 (ułamkowa lekcja nie jest lekcją).** Przy $B=3$ i dwóch zadaniach, każde o koszcie $2$ i wartości $3$, relaksacja może wybrać jedno zadanie w całości i połowę drugiego (wartość $4{,}5$), ale model całkowitoliczbowy dopuszcza co najwyżej jedno zadanie (wartość $3$).

**K27 (brak niezależności).** Jeżeli dwa zadania są zawsze wybierane wspólnie z prawdopodobieństwem $1/2$, to prawdopodobieństwo objęcia kompetencji występującej w obu wynosi $1/2$, a nie $1-(1-1/2)^2=3/4$.

**K28 (optymalizacja modelu a jakość nauczania).** Plan maksymalizujący zadane $v_i$ może być pedagogicznie słaby, jeśli wartości błędnie opisują transfer wiedzy, zmęczenie lub potrzeby uczniów. Dowód optymalności nie waliduje parametrów.

## 8.4. Zadania z rozwiązaniami

**Z51.** Dla zadań $(c,v)=(2,3),(3,4)$ i $B=3$ wyznacz optimum. **Rozwiązanie:** dopuszczalne są wybory pusty, pierwszy i drugi; oba naraz kosztują $5$. Optimum to drugie zadanie o wartości $4$.

**Z52.** Dla danych Z51 i $B=5$ oblicz optimum. **Rozwiązanie:** oba zadania kosztują $5$ i dają $3+4=7$, co jest największą możliwą wartością.

**Z53.** Dla jednego zadania $(c,v)=(4,7)$ i $B=3$ oblicz $F_1(3)$. **Rozwiązanie:** $c>B$, więc z T43 mamy $F_1(3)=F_0(3)=0$.

**Z54.** Dla jednego zadania $(4,7)$ i $B=4$ oblicz $F_1(4)$. **Rozwiązanie:** $\max(0,0+7)=7$.

**Z55.** Przy $B=10$, $(c,v)=(6,9),(5,8),(5,8)$ wskaż rozwiązanie lepsze od zachłannego. **Rozwiązanie:** zadania drugie i trzecie mają koszt $10$ i wartość $16$.

**Z56.** Dla $O=15$ i $R=18$ sprawdź T46–T47. **Rozwiązanie:** $15\le18\le30$, więc obie granice są spełnione.

**Z57.** Uniwersum $U=\{a,b,c\}$, zadania $C_1=\{a,b\}$, $C_2=\{b,c\}$, oba o koszcie $2$. **Rozwiązanie:** pełne pokrycie wymaga obu zadań i kosztuje $4$.

**Z58.** W Z57 wyznacz dolne ograniczenie liczby zadań z T52. **Rozwiązanie:** $m=3$, $r=2$, zatem potrzeba co najmniej $\lceil3/2\rceil=2$ zadań.

**Z59.** Przy trzech kompetencjach maski $C_1=011_2$ i $C_2=110_2$ dają sumę. **Rozwiązanie:** $011_2\operatorname{OR}110_2=111_2$.

**Z60.** Jedna kompetencja występuje w dwóch niezależnie losowanych zadaniach o $p_1=1/2$ i $p_2=1/3$. **Rozwiązanie:** $q=1-(1/2)(2/3)=2/3$.

**Z61.** Dla Z60 oblicz granicę T54. **Rozwiązanie:** $P(\text{brak})=1/3\le e^{-5/6}\approx0{,}4346$.

**Z62.** Dla dwóch kompetencji o wagach $2,5$ i prawdopodobieństwach pokrycia $1/2,4/5$ oblicz wartość oczekiwaną. **Rozwiązanie:** $2(1/2)+5(4/5)=5$.

**Z63.** Zadanie $A$ kosztuje $4$ i daje wartość $6$, a $B$ kosztuje $5$ i daje wartość $5$. Czy $A$ dominuje $B$? **Rozwiązanie:** tak, bo $4<5$ i $6>5$.

**Z64.** Dla $n=20$, $B=100$ podaj liczbę stanów tablicy $F_i(b)$. **Rozwiązanie:** $(n+1)(B+1)=21\cdot101=2121$ stanów; implementacja dwuwarstwowa przechowuje $101$ wartości na warstwę.

## 8.5. Granice modelu i kontrola poprawności

Dowody dotyczą skończonych problemów optymalizacyjnych. D44–D51 nie zastępują psychometrii ani badań przyczynowych. Zmienna $x_i=1$ oznacza wybór zadania, nie gwarantowane nabycie umiejętności. Przed wdrożeniem planu do pracy z uczniami należy empirycznie ocenić koszt, wartość, trafność zbiorów $C_i$, dostępność zadań i wpływ na grupy o różnych potrzebach. Pseudowielomianowe $O(nB)$ nie daje gwarancji skalowalności dla dowolnego binarnego kodowania kosztów. W T47–T48 nie wolno pominąć warunku $c_i\le B$; zadania przekraczające budżet należy odrzucić przed relaksacją.