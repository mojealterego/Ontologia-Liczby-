# MSC 97D40 — III-H: przydział zadań i sprawiedliwość proceduralna

**Tom I, poziom III.** Rozszerzenie rozdziału o skończone modele przypisywania uczniom zadań, miejsc i zasobów. Matematyczne kryterium sprawiedliwości jest warunkiem formalnym, a nie dowodem pedagogicznej słuszności konkretnego przydziału.

## 1. Definicje

**D75 (graf dopuszczalności).** Niech $U$ będzie skończonym zbiorem uczniów, $R$ skończonym zbiorem zasobów, a $E\subseteq U\times R$ relacją dopuszczalności przydziału.

**D76 (sąsiedztwo).** Dla $S\subseteq U$ definiujemy $N(S)=\{r\in R:\exists u\in S,\ (u,r)\in E\}$.

**D77 (skojarzenie).** Skojarzenie $M\subseteq E$ to zbiór par, w którym żaden uczeń ani zasób nie występuje więcej niż raz.

**D78 (pełne pokrycie uczniów).** Skojarzenie pokrywa $U$, gdy każdy $u\in U$ należy do dokładnie jednej pary w $M$.

**D79 (deficyt Halla).** Dla $S\subseteq U$ liczba $d(S)=|S|-|N(S)|$ mierzy niedobór odrębnych zasobów dostępnych tej grupie.

**D80 (pojemność).** Funkcja $b:R\to\mathbb Z_{\ge0}$ przypisuje zasobowi maksymalną liczbę uczniów. Przydział pojemnościowy jest funkcją $f:U\to R$, dla której $(u,f(u))\in E$ i $|f^{-1}(\{r\})|\le b(r)$.

**D81 (koszt).** Każdej parze $(u,r)\in E$ przypisujemy koszt $c(u,r)\ge0$; koszt pełnego przydziału wynosi $C(f)=\sum_{u\in U}c(u,f(u))$.

**D82 (koszt wąskiego gardła).** $B(f)=\max_{u\in U}c(u,f(u))$ dla niepustego $U$.

**D83 (alokacja dóbr).** Dla skończonego zbioru jednakowo ocenianych, niepodzielnych dóbr $G$ alokacja $A=(A_1,\ldots,A_n)$ jest partycją $G$ na $n\ge1$ zbiorów.

**D84 (EF1 dla dóbr jednostkowych).** Alokacja jest *wolna od zazdrości po usunięciu jednego dobra* (EF1), jeśli dla każdej pary osób $i,j$ z $A_j\ne\varnothing$ istnieje $g\in A_j$ takie, że $|A_i|\ge|A_j\setminus\{g\}|$; gdy $A_j=\varnothing$, warunek jest automatyczny.

**D85 (alokacja wyrównana).** Alokacja jest wyrównana, gdy $||A_i|-|A_j||\le1$ dla wszystkich $i,j$.

## 2. Twierdzenia z dowodami

**T85 (ograniczenie liczności skojarzenia).** Każde skojarzenie spełnia $|M|\le\min(|U|,|R|)$.

*Dowód.* Odwzorowania przypisujące parze jej pierwszą i drugą współrzędną są różnowartościowe na $M$, więc liczba par nie przewyższa liczby elementów żadnej części grafu. $\square$

**T86 (warunek konieczny Halla).** Jeżeli istnieje skojarzenie pokrywające $U$, to $|N(S)|\ge|S|$ dla każdego $S\subseteq U$.

*Dowód.* Zasoby skojarzone z różnymi uczniami w $S$ są różne i należą do $N(S)$. Istnieje więc iniekcja $S\hookrightarrow N(S)$. $\square$

**T87 (twierdzenie Halla, skończona postać).** Skojarzenie pokrywające $U$ istnieje wtedy i tylko wtedy, gdy $|N(S)|\ge|S|$ dla wszystkich $S\subseteq U$.

*Dowód.* Konieczność daje T86. Wystarczalność udowodnimy indukcyjnie względem $|U|$. Dla $U=\varnothing$ bierzemy skojarzenie puste. Załóżmy tezę dla mniejszych zbiorów. Jeżeli istnieje niepusty właściwy $S\subsetneq U$ z $|N(S)|=|S|$, indukcja daje skojarzenie $S$ z $N(S)$. Dla $T\subseteq U\setminus S$ zachodzi $|N(T)\setminus N(S)|\ge|T|$, ponieważ $|N(S\cup T)|=|N(S)|+|N(T)\setminus N(S)|\ge|S|+|T|$. Indukcja daje skojarzenie reszty z zasobami poza $N(S)$; sumujemy skojarzenia. W przeciwnym razie każde niepuste właściwe $S$ spełnia $|N(S)|\ge|S|+1$. Wybieramy dowolnego $u\in U$ i dowolne $r\in N(\{u\})$, które istnieje na mocy warunku Halla. Po usunięciu $u,r$ każdy $T\subseteq U\setminus\{u\}$ traci co najwyżej jednego sąsiada, zatem ma co najmniej $|T|$ sąsiadów. Indukcja daje skojarzenie reszty; dokładamy $(u,r)$. $\square$

**T88 (pojemnościowy warunek Halla).** Pełny przydział pojemnościowy istnieje wtedy i tylko wtedy, gdy dla każdego $S\subseteq U$ zachodzi
$$|S|\le\sum_{r\in N(S)}b(r).$$

*Dowód.* Konieczność: uczniowie z $S$ mogą trafić wyłącznie do $N(S)$, a każdy zasób $r$ obsłuży co najwyżej $b(r)$ osób. Wystarczalność: zastąpmy zasób $r$ przez $b(r)$ rozróżnialnych kopii, połączonych ze wszystkimi dotychczasowymi sąsiadami $r$. Liczba sąsiadów $S$ w grafie kopii wynosi dokładnie $\sum_{r\in N(S)}b(r)$. T87 daje skojarzenie pokrywające uczniów. Po utożsamieniu kopii tego samego zasobu otrzymujemy przydział o zadanych pojemnościach. $\square$

**T89 (globalna granica pojemności).** Jeżeli istnieje pełny przydział pojemnościowy, to $|U|\le\sum_{r\in R}b(r)$.

*Dowód.* W T88 podstawiamy $S=U$ i korzystamy z $N(U)\subseteq R$ oraz nieujemności pojemności. $\square$

**T90 (monotoniczność wykonalności).** Jeżeli przydział jest wykonalny przy pojemnościach $b$, to jest wykonalny przy $b'\ge b$ punktowo.

*Dowód.* Ten sam przydział spełnia nierówności $|f^{-1}(\{r\})|\le b(r)\le b'(r)$. $\square$

**T91 (monotoniczność minimalnego kosztu).** Jeśli pełny przydział istnieje, zwiększenie pojemności lub dodanie dopuszczalnych krawędzi nie może zwiększyć minimalnego kosztu $C(f)$, o ile koszty dotychczasowych krawędzi pozostają niezmienione.

*Dowód.* Zbiór wcześniejszych przydziałów jest podzbiorem nowego zbioru przydziałów. Minimum tej samej funkcji po większym zbiorze nie przewyższa minimum po mniejszym. $\square$

**T92 (dolna granica wąskiego gardła).** Dla każdego pełnego przydziału $f$ zachodzi
$$B(f)\ge\max_{u\in U}\min_{r\in N(\{u\})}c(u,r),$$
gdy $U\ne\varnothing$ i wszystkie indywidualne sąsiedztwa są niepuste.

*Dowód.* Dla każdego $u$ mamy $c(u,f(u))\ge\min_{r\in N(\{u\})}c(u,r)$. Maksimum po $u$ zachowuje nierówność. $\square$

**T93 (liczba pełnych skojarzeń w grafie kompletnym).** Jeżeli $|U|=n\le m=|R|$ i $E=U\times R$, to liczba skojarzeń pokrywających $U$ wynosi $m!/(m-n)!$.

*Dowód.* Pierwszemu uczniowi można przydzielić $m$ zasobów, drugiemu $m-1$, aż do $m-n+1$. Zasada mnożenia daje iloczyn. $\square$

**T94 (alokacja wyrównana istnieje).** Dla $k=|G|$ i $n\ge1$ istnieje alokacja z licznościami $\lfloor k/n\rfloor$ albo $\lceil k/n\rceil$.

*Dowód.* Dzielimy $k=qn+r$ z $0\le r<n$. Przydzielamy $q+1$ dóbr pierwszym $r$ osobom, a $q$ pozostałym. Łącznie rozdzielamy $r(q+1)+(n-r)q=k$ dóbr. $\square$

**T95 (alokacja wyrównana jest EF1).** W modelu dóbr jednostkowych każda alokacja wyrównana spełnia EF1.

*Dowód.* Dla dowolnych $i,j$ z $A_j\ne\varnothing$ wyrównanie daje $|A_j|\le|A_i|+1$. Po usunięciu dowolnego dobra z $A_j$ pozostaje $|A_j|-1\le|A_i|$. $\square$

**T96 (najmniejsza możliwa nierównowaga liczności).** Dla $k$ dóbr i $n$ osób minimum $\max_i|A_i|-\min_i|A_i|$ wynosi $0$, jeśli $n\mid k$, a w przeciwnym razie $1$.

*Dowód.* T94 konstruuje alokację o nierównowadze co najwyżej $1$, a przy podzielności przez $n$ o nierównowadze $0$. Gdyby przy $n\nmid k$ nierównowaga była $0$, wszystkie $n$ liczności byłyby równe pewnemu całkowitemu $q$, co dawałoby $k=nq$, sprzeczność. $\square$

## 3. Kontrprzykłady

**K45.** Sama nierówność $|R|\ge|U|$ nie wystarcza: dla $U=\{a,b\}$, $R=\{1,2\}$ i $E=\{(a,1),(b,1)\}$ nie istnieje skojarzenie pokrywające $U$.

**K46.** Sama suma pojemności nie wystarcza: $b(1)=2$, $b(2)=1$, ale trzech uczniów może mieć wyłącznie zasób $2$ w sąsiedztwie.

**K47.** Zachłanny przydział może zablokować rozwiązanie: $a$ dopuszcza $1$ i $2$, $b$ wyłącznie $1$. Wybór $a\mapsto1$ uniemożliwia przydział $b$, choć $a\mapsto2$, $b\mapsto1$ jest poprawny.

**K48.** Minimalny koszt całkowity nie oznacza najmniejszego kosztu maksymalnego: wektor kosztów $(0,9)$ ma sumę $9$ i maksimum $9$, a $(5,5)$ sumę $10$ i maksimum $5$.

**K49.** EF1 nie oznacza pełnego braku zazdrości: przy trzech identycznych dobrach alokacja $(2,1)$ jest EF1, ale osoba z jednym dobrem zazdrości osobie z dwoma.

**K50.** Wzrost pojemności nie musi zmniejszyć kosztu optymalnego: jeśli najtańszy przydział był już wykonalny, optimum pozostaje takie samo.

**K51.** Bez założenia jednakowej jednostkowej wartości dóbr samo wyrównanie liczności nie zapewnia EF1: osoba $i$ ma jedno dobro wartości $0$, osoba $j$ dwa dobra wartości $100$ każde; po usunięciu jednego dobra osoba $i$ nadal zazdrości.

**K52.** Dolna granica T92 może być nieosiągalna: dwóch uczniów ma najtańszy wspólny zasób $1$ o koszcie $0$ i alternatywny zasób $2$ o koszcie $10$. Granica wynosi $0$, ale każdemu pełnemu skojarzeniu odpowiada $B(f)=10$.

## 4. Zadania z rozwiązaniami

**Z109.** Dla $|U|=3$ i $|R|=5$ podaj maksymalną liczbę par. **Rozwiązanie:** z T85 najwyżej $3$.

**Z110.** Dla $U=\{a,b\}$, $N(\{a\})=N(\{b\})=\{1\}$ oceń wykonalność. **Rozwiązanie:** $|N(U)|=1<2$, więc nie ma pełnego skojarzenia.

**Z111.** Dla $a\sim\{1,2\}$, $b\sim\{1\}$ znajdź skojarzenie. **Rozwiązanie:** $\{(a,2),(b,1)\}$.

**Z112.** Trzy osoby mogą korzystać wyłącznie z zasobu $r$ o $b(r)=2$. **Rozwiązanie:** dla $S=U$ nierówność T88 wymaga $3\le2$, więc przydział jest niemożliwy.

**Z113.** Zasoby mają pojemności $b(1)=2$, $b(2)=1$; wszyscy trzej uczniowie dopuszczają oba. **Rozwiązanie:** dwóch przydzielamy do $1$, jednego do $2$.

**Z114.** Dla $n=3,m=5$ policz pełne skojarzenia grafu kompletnego. **Rozwiązanie:** $5\cdot4\cdot3=60$.

**Z115.** Dla $n=4,m=4$ policz pełne skojarzenia. **Rozwiązanie:** $4!=24$.

**Z116.** Rozdziel $11$ dóbr między $4$ osoby wyrównanie. **Rozwiązanie:** liczności $(3,3,3,2)$.

**Z117.** Minimalna nierównowaga dla $12$ dóbr i $4$ osób. **Rozwiązanie:** $0$, alokacja $(3,3,3,3)$.

**Z118.** Minimalna nierównowaga dla $13$ dóbr i $4$ osób. **Rozwiązanie:** $1$, np. $(4,3,3,3)$.

**Z119.** Czy alokacja $(3,2,2)$ jest EF1 przy dobrach jednostkowych? **Rozwiązanie:** tak, różnice liczności nie przekraczają $1$ (T95).

**Z120.** Czy alokacja $(4,1,1)$ jest EF1 przy dobrach jednostkowych? **Rozwiązanie:** nie, osoba z jednym dobrem po usunięciu jednego dobra z pakietu czterech nadal porównuje $1<3$.

**Z121.** Dla kosztów przypisanych $(2,4,6)$ policz koszt całkowity. **Rozwiązanie:** $C=12$.

**Z122.** Dla tych samych kosztów policz wąskie gardło. **Rozwiązanie:** $B=6$.

**Z123.** Dla $U=\{a,b\}$, kosztów $c(a,1)=0$, $c(a,2)=10$, $c(b,1)=0$, $c(b,2)=10$ oblicz minimalne wąskie gardło. **Rozwiązanie:** $10$, bo jeden uczeń musi otrzymać zasób $2$.

**Z124.** W Z123 oblicz granicę T92. **Rozwiązanie:** $0$, ponieważ każdy uczeń indywidualnie ma zasób o koszcie $0$.

**Z125.** Czy podniesienie $b(1)$ z $1$ do $2$ może unieważnić wcześniej dopuszczalny przydział? **Rozwiązanie:** nie, z T90.

**Z126.** Dla $U=\varnothing$ i dowolnego $R$ znajdź skojarzenie pokrywające $U$. **Rozwiązanie:** zbiór pusty.

**Z127.** Dla $k=2,n=5$ podaj wyrównaną alokację. **Rozwiązanie:** $(1,1,0,0,0)$.

**Z128.** Dla $k=0,n=3$ oblicz minimalną nierównowagę. **Rozwiązanie:** $0$, alokacja $(0,0,0)$.

## 5. Granice interpretacji

Dopuszczalność krawędzi i koszt nie powinny być wyznaczane na podstawie nieuprawnionych lub dyskryminujących założeń. Kryterium EF1 opisuje jedynie szczególny model dóbr jednostkowych; rzeczywista równość szans wymaga analizy potrzeb, dostępności, skutków interwencji i nadzoru człowieka. Matematyczny dowód istnienia przydziału nie dowodzi jego skuteczności dydaktycznej.
