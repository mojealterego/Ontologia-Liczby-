# MSC 97D40 — III-I: modele opanowania, zapominania i planowania powtórek

**Tom I, poziom III.** Rozdział matematyczny dotyczący jawnych, uproszczonych modeli stanów wiedzy. Prawdopodobieństwo opanowania jest parametrem modelu, nie diagnozą konkretnej osoby. Przejścia Markowa, krzywa wykładnicza i aktualizacja bayesowska wymagają niezależnego uzasadnienia empirycznego.

## 1. Definicje

**D86 (stan opanowania).** Zmienna $M_t\in\{0,1\}$ oznacza w chwili $t$ stan modelowy: $0$ — brak opanowania, $1$ — opanowanie.

**D87 (nabywanie i utrzymywanie).** W jednorodnym modelu Markowa $a=P(M_{t+1}=1\mid M_t=0)$ i $r=P(M_{t+1}=1\mid M_t=1)$, gdzie $a,r\in[0,1]$.

**D88 (prawdopodobieństwo opanowania).** $p_t=P(M_t=1)$.

**D89 (operator przejścia).** $F_{a,r}(p)=a+(r-a)p$ dla $p\in[0,1]$.

**D90 (punkt stały).** $p^*$ jest punktem stałym, jeśli $F_{a,r}(p^*)=p^*$.

**D91 (współczynnik pamięci).** $\lambda=r-a\in[-1,1]$.

**D92 (polityka powtórek).** Akcja $u$ określa parę $(a_u,r_u)$, a jej skutek na rozkład stanu wyraża operator $F_{a_u,r_u}$.

**D93 (model zapominania).** Dla $\kappa\ge0$ i odstępu $d\ge0$ przeżycie śladu pamięciowego wynosi $s_\kappa(d)=e^{-\kappa d}$.

**D94 (okres połowiczny).** Przy $\kappa>0$ okres $h$ spełnia $s_\kappa(h)=1/2$.

**D95 (ciąg odstępów).** Harmonogram bez ponownego uczenia to skończony ciąg $(d_1,\ldots,d_k)$ liczb nieujemnych.

**D96 (stan wiedzy z prerekwizytami).** Dla DAG $G=(V,E)$ zbiór $S\subseteq V$ jest domknięty w dół, jeśli $v\in S$ i $(u,v)\in E$ implikuje $u\in S$.

**D97 (frontier nauczania).** $A(S)=\{v\in V\setminus S:\text{ każdy bezpośredni poprzednik }v\text{ należy do }S\}$.

**D98 (ścieżka dopuszczalna).** Ciąg różnych wierzchołków $(v_1,\ldots,v_k)$ jest dopuszczalny od $S_0$, jeśli $v_i\in A(S_0\cup\{v_1,\ldots,v_{i-1}\})$ dla każdego $i$.

**D99 (próba Bernoulliego).** Obserwacje $X_1,\ldots,X_n\in\{0,1\}$ są warunkowo niezależne i identycznie rozłożone przy ustalonym nieznanym $\theta\in(0,1)$: $P(X_i=1\mid\theta)=\theta$.

**D100 (rozkład beta).** Prior $\theta\sim\mathrm{Beta}(\alpha,\beta)$, gdzie $\alpha,\beta>0$, ma gęstość proporcjonalną do $\theta^{\alpha-1}(1-\theta)^{\beta-1}$.

**D101 (liczniki obserwacji).** $s=\sum_iX_i$ oraz $f=n-s$.

**D102 (posterior).** Rozkład warunkowy parametru $\theta$ po obserwacji danych $X_1,\ldots,X_n$.

**D103 (czułość i swoistość).** Dla binarnego stanu $M$ i wyniku $Y$ definiujemy $\mathrm{Se}=P(Y=1\mid M=1)$ i $\mathrm{Sp}=P(Y=0\mid M=0)$.

**D104 (prawdopodobieństwo wyniku dodatniego).** $q(p)=P(Y=1)$, gdy $P(M=1)=p$.

## 2. Twierdzenia i dowody

**T97 (równanie dynamiki).** W modelu D87–D89 zachodzi $p_{t+1}=a+(r-a)p_t$.

*Dowód.* Z prawa całkowitego prawdopodobieństwa $P(M_{t+1}=1)=P(M_t=0)a+P(M_t=1)r=(1-p_t)a+p_tr$. $\square$

**T98 (zamknięta postać iteracji).** Dla $\lambda=r-a$ i $t\ge0$ zachodzi
$$p_t=\lambda^tp_0+a\sum_{j=0}^{t-1}\lambda^j,$$
gdzie suma pusta wynosi $0$.

*Dowód.* Dla $t=0$ teza jest oczywista. Jeśli obowiązuje dla $t$, to $p_{t+1}=a+\lambda p_t=\lambda^{t+1}p_0+a\sum_{j=0}^{t}\lambda^j$. Indukcja kończy dowód. $\square$

**T99 (jedyny punkt stały).** Jeśli $(a,r)\ne(0,1)$, to operator $F_{a,r}$ ma dokładnie jeden punkt stały
$$p^*=\frac{a}{1-r+a}\in[0,1].$$

*Dowód.* Równanie $p=a+(r-a)p$ daje $(1-r+a)p=a$. Mianownik jest dodatni poza parą $(0,1)$; ponadto $0\le a\le1-r+a$, więc $p^*\in[0,1]$. $\square$

**T100 (zbieżność do stanu stacjonarnego).** Jeśli $|\lambda|<1$, to $p_t=p^*+\lambda^t(p_0-p^*)$ oraz $p_t\to p^*$.

*Dowód.* Odejmujemy od T97 równanie $p^*=a+\lambda p^*$, otrzymując $p_{t+1}-p^*=\lambda(p_t-p^*)$. Indukcja daje postać zamkniętą, a $\lambda^t\to0$. $\square$

**T101 (dwa przypadki brzegowe).** Jeśli $(a,r)=(0,1)$, to $p_t=p_0$ dla wszystkich $t$. Jeśli $(a,r)=(1,0)$, to $p_{t+1}=1-p_t$, a dla $p_0\ne1/2$ ciąg nie ma granicy.

*Dowód.* W pierwszym przypadku $F(p)=p$. W drugim $F(p)=1-p$ i $F(F(p))=p$, zatem kolejne wyrazy naprzemiennie przyjmują $p_0$ i $1-p_0$. $\square$

**T102 (stabilność różnicy warunków początkowych).** Dla dwóch ciągów z tymi samymi $a,r$ zachodzi $|p_t-q_t|=|\lambda|^t|p_0-q_0|$.

*Dowód.* Różnica równań T97 daje $p_{t+1}-q_{t+1}=\lambda(p_t-q_t)$; iterujemy i bierzemy moduł. $\square$

**T103 (dominacja działania).** Jeżeli $a_1\ge a_0$ i $r_1\ge r_0$, to $F_{a_1,r_1}(p)\ge F_{a_0,r_0}(p)$ dla każdego $p\in[0,1]$.

*Dowód.* Różnica wynosi $(1-p)(a_1-a_0)+p(r_1-r_0)$, czyli sumę składników nieujemnych. $\square$

**T104 (wrażliwość na parametry).** Dla każdego $p\in[0,1]$:
$$|F_{a_1,r_1}(p)-F_{a_0,r_0}(p)|\le\max(|a_1-a_0|,|r_1-r_0|).$$

*Dowód.* Stosujemy nierówność trójkąta do $(1-p)(a_1-a_0)+p(r_1-r_0)$ i fakt $(1-p)+p=1$. $\square$

**T105 (akumulacja zaburzeń).** Jeśli $|r_1-a_1|\le c<1$, $|F_1(p)-F_0(p)|\le\varepsilon$ dla wszystkich $p$, a ciągi $p_{t+1}=F_1(p_t)$ i $q_{t+1}=F_0(q_t)$ startują z $p_0=q_0$, to
$$|p_t-q_t|\le\varepsilon\frac{1-c^t}{1-c}.$$

*Dowód.* $d_{t+1}\le|F_1(p_t)-F_1(q_t)|+|F_1(q_t)-F_0(q_t)|\le cd_t+\varepsilon$. Z $d_0=0$ i indukcji otrzymujemy sumę geometryczną. $\square$

**T106 (prawo składania zapominania).** Dla $\kappa,d,e\ge0$ zachodzi $s_\kappa(d+e)=s_\kappa(d)s_\kappa(e)$.

*Dowód.* $e^{-\kappa(d+e)}=e^{-\kappa d}e^{-\kappa e}$. $\square$

**T107 (monotoniczność i okres połowiczny).** Dla $\kappa>0$ funkcja $s_\kappa$ jest ściśle malejąca, a jedyny okres połowiczny wynosi $h=\ln2/\kappa$.

*Dowód.* Pochodna $s_\kappa'(d)=-\kappa e^{-\kappa d}<0$. Rozwiązanie $e^{-\kappa h}=1/2$ daje $\kappa h=\ln2$. $\square$

**T108 (niezmienniczość podziału czasu bez powtórek).** Dla harmonogramu D95 iloczyn retencji $\prod_{j=1}^ks_\kappa(d_j)$ zależy tylko od sumy $D=\sum_jd_j$ i wynosi $e^{-\kappa D}$.

*Dowód.* Wielokrotnie stosujemy T106. $\square$

**T109 (zachowanie domknięcia prerekwizytów).** Jeśli $S$ jest domknięty w dół i $v\in A(S)$, to $S\cup\{v\}$ jest domknięty w dół.

*Dowód.* Każdy poprzednik elementu z $S$ należy do $S$. Każdy bezpośredni poprzednik $v$ należy do $S$ z definicji $A(S)$, a z domknięcia $S$ także wszyscy dalsi poprzednicy. $\square$

**T110 (istnienie pełnej ścieżki).** W skończonym DAG, dla dowolnego domkniętego $S_0$, istnieje dopuszczalna ścieżka zawierająca każdy wierzchołek $V\setminus S_0$ dokładnie raz.

*Dowód.* Jeśli $V\setminus S$ jest niepuste, graf indukowany na nim ma wierzchołek bez poprzedników w tym podgrafie, bo inaczej zawierałby cykl. Wszystkie jego poprzedniki należą do $S$, więc leży w $A(S)$. Dodajemy go, zachowując domknięcie dzięki T109, i powtarzamy skończoną liczbę razy. $\square$

**T111 (aktualizacja beta–Bernoulli).** W modelu D99–D102 posterior ma rozkład $\mathrm{Beta}(\alpha+s,\beta+f)$.

*Dowód.* Wiarygodność próby wynosi $\theta^s(1-\theta)^f$. Mnożymy ją przez gęstość prior proporcjonalną do $\theta^{\alpha-1}(1-\theta)^{\beta-1}$ i normalizujemy. Otrzymujemy gęstość beta o parametrach $\alpha+s,\beta+f$. $\square$

**T112 (średnia posterior i predykcja).** Przy T111:
$$\mathbb E[\theta\mid X_1,\ldots,X_n]=P(X_{n+1}=1\mid X_1,\ldots,X_n)=\frac{\alpha+s}{\alpha+\beta+n}.$$

*Dowód.* Średnia rozkładu $\mathrm{Beta}(A,B)$ wynosi $A/(A+B)$, co wynika z tożsamości $B(A+1,B)=A\,B(A,B)/(A+B)$ dla funkcji beta. Warunkowo względem $\theta$ następna próba ma prawdopodobieństwo sukcesu $\theta$; prawo iterowanego oczekiwania daje drugi człon. $\square$

**T113 (wygładzanie średniej).** Przy $n>0$ średnia posterior jest kombinacją wypukłą średniej prior $\alpha/(\alpha+\beta)$ i średniej próby $s/n$:
$$\frac{\alpha+s}{\alpha+\beta+n}=\frac{\alpha+\beta}{\alpha+\beta+n}\frac{\alpha}{\alpha+\beta}+\frac n{\alpha+\beta+n}\frac sn.$$

*Dowód.* Po sprowadzeniu do wspólnego mianownika licznik wynosi $\alpha+s$; wagi są nieujemne i sumują się do $1$. $\square$

**T114 (posterior przy braku obserwacji).** Dla $n=0$ posterior jest równy prior.

*Dowód.* Wiarygodność pustej próby jest stałą $1$, więc aktualizacja Bayesa nie zmienia gęstości. $\square$

**T115 (wpływ niedoskonałego testu).** Przy D103–D104:
$$q(p)=\mathrm{Se}\,p+(1-\mathrm{Sp})(1-p).$$

*Dowód.* Rozbijamy zdarzenie $Y=1$ według rozłącznych stanów $M=1$ i $M=0$ i stosujemy prawo całkowitego prawdopodobieństwa. $\square$

**T116 (identyfikowalność stanu z częstości dodatnich wyników).** Jeśli $\mathrm{Se}+\mathrm{Sp}\ne1$ i obie charakterystyki testu są znane, to
$$p=\frac{q+\mathrm{Sp}-1}{\mathrm{Se}+\mathrm{Sp}-1}.$$
Jeżeli $\mathrm{Se}+\mathrm{Sp}=1$, to $q(p)$ jest stałe i nie identyfikuje $p$.

*Dowód.* T115 daje $q=(\mathrm{Se}+\mathrm{Sp}-1)p+1-\mathrm{Sp}$. Dla niezerowego współczynnika przy $p$ rozwiązujemy równanie liniowe; dla zerowego $q$ nie zależy od $p$. $\square$

## 3. Kontrprzykłady

**K53.** Nie każdy model ma jeden stan stacjonarny: przy $a=0,r=1$ wszystkie $p\in[0,1]$ są punktami stałymi.

**K54.** Zbieżność nie jest automatyczna: przy $a=1,r=0$ i $p_0=0$ otrzymujemy $0,1,0,1,\ldots$.

**K55.** Większa szansa nabycia nie gwarantuje dominacji działania, gdy retencja spada: przy $a_1=1,r_1=0$, $a_0=0,r_0=1$ i $p=1$ działanie 1 daje $0$, a działanie 0 daje $1$.

**K56.** Sama liczba powtórek nie zmienia retencji w modelu bez ponownego uczenia D93: przy tej samej sumie odstępów T108 daje ten sam iloczyn.

**K57.** Wykładnicze zapominanie nie jest uniwersalnym prawem psychologicznym: funkcja $s(d)=1/(1+d)$ nie spełnia T106, gdyż $s(2)=1/3\ne1/4=s(1)^2$.

**K58.** Przy cyklicznych prerekwizytach $a\to b\to a$ zbiór $A(\varnothing)$ jest pusty; T110 wymaga DAG.

**K59.** Posterior T111 jest niewłaściwy dla danych silnie zależnych, jeśli błędnie uznamy wielokrotne kopie tej samej odpowiedzi za niezależne próby.

**K60.** Przy $\mathrm{Se}=\mathrm{Sp}=1/2$ każdy $p$ daje $q=1/2$; z samej częstości wyników dodatnich nie można odzyskać $p$.

## 4. Zadania rozwiązane

**Z129.** $a=0{,}2$, $r=0{,}9$, $p_0=0{,}4$. **Rozwiązanie:** $p_1=0{,}2+0{,}7\cdot0{,}4=0{,}48$.

**Z130.** Dla Z129 oblicz punkt stały. **Rozwiązanie:** $p^*=0{,}2/(1-0{,}9+0{,}2)=2/3$.

**Z131.** Dla Z129 oblicz $p_2$. **Rozwiązanie:** $p_2=0{,}2+0{,}7\cdot0{,}48=0{,}536$.

**Z132.** $a=r=0{,}6$. **Rozwiązanie:** $\lambda=0$, więc po jednym kroku $p_1=0{,}6$ niezależnie od $p_0$.

**Z133.** $a=0,r=1$. **Rozwiązanie:** $F(p)=p$, zatem dowolny stan początkowy pozostaje niezmieniony.

**Z134.** $a=1,r=0,p_0=0{,}3$. **Rozwiązanie:** $p_1=0{,}7$, $p_2=0{,}3$.

**Z135.** $\kappa=\ln2/7$. **Rozwiązanie:** okres połowiczny wynosi $7$ jednostek czasu.

**Z136.** $\kappa=\ln2/7$, odstęp $14$. **Rozwiązanie:** $s_\kappa(14)=e^{-2\ln2}=1/4$.

**Z137.** Odstępy $(2,3,5)$ przy $\kappa=0{,}1$. **Rozwiązanie:** iloczyn retencji wynosi $e^{-0{,}1(2+3+5)}=e^{-1}$.

**Z138.** DAG $a\to c$, $b\to c$, $c\to d$, $S=\{a,b\}$. **Rozwiązanie:** $A(S)=\{c\}$, następnie $A(\{a,b,c\})=\{d\}$.

**Z139.** Prior $\mathrm{Beta}(2,3)$, obserwacje: trzy sukcesy i jedna porażka. **Rozwiązanie:** posterior $\mathrm{Beta}(5,4)$.

**Z140.** Dla Z139 oblicz średnią posterior. **Rozwiązanie:** $5/(5+4)=5/9$.

**Z141.** Prior $\mathrm{Beta}(1,1)$, zero obserwacji. **Rozwiązanie:** posterior pozostaje $\mathrm{Beta}(1,1)$.

**Z142.** $\mathrm{Se}=0{,}9$, $\mathrm{Sp}=0{,}8$, $p=0{,}6$. **Rozwiązanie:** $q=0{,}9\cdot0{,}6+0{,}2\cdot0{,}4=0{,}62$.

**Z143.** Przy $\mathrm{Se}=0{,}9$, $\mathrm{Sp}=0{,}8$, $q=0{,}62$ wyznacz $p$. **Rozwiązanie:** $p=(0{,}62+0{,}8-1)/(0{,}9+0{,}8-1)=0{,}42/0{,}7=0{,}6$.

**Z144.** Dwa modele mają te same $a,r$, lecz $p_0=0{,}2$ i $q_0=0{,}8$, przy $|r-a|=1/2$. **Rozwiązanie:** po trzech krokach odległość wynosi $(1/2)^3\cdot0{,}6=0{,}075$.

## 5. Granice interpretacji

Parametry $a,r,\kappa,\mathrm{Se},\mathrm{Sp}$ muszą zostać oszacowane w odpowiednio zaprojektowanych badaniach, a nie arbitralnie przypisane uczniowi. Rzeczywista wiedza nie jest binarna; wpływają na nią kontekst, zmęczenie, stres i wcześniejsze doświadczenia. W szczególności powtarzanie tego samego pytania nie tworzy niezależnych obserwacji Bernoulliego, a średnia posterior nie jest automatycznie oceną zdolności. Formalny harmonogram powtórek jest hipotezą planistyczną, nie rekomendacją pedagogiczną bez walidacji.
