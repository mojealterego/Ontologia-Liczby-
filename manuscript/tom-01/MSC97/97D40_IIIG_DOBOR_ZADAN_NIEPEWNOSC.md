# MSC 97D40 — III-G: dobór zadań przy niepewnej skuteczności

**Tom I, poziom III.** Uzupełnienie po częściach III-A–III-F. Modele służą do badania własności decyzji; ich parametry nie są twierdzeniami o skuteczności nauczania.

## Definicje

**D67 (wynik losowy).** Dla zadania $i$ niech $X_i\in[0,1]$ oznacza wynik modelowy, a $\mu_i=\mathbb E X_i$ jego wartość oczekiwaną.

**D68 (próba).** Dla zadania $i$ obserwujemy $n_i\ge1$ niezależnych zmiennych $X_{i,1},\ldots,X_{i,n_i}$ o tym samym rozkładzie co $X_i$.

**D69 (średnia empiryczna).** $\widehat\mu_i=n_i^{-1}\sum_jX_{i,j}$.

**D70 (reguła optymistyczna).** Przy liczbie kandydatów $m\ge1$ i $0<\delta<1$ definiujemy $U_i=\widehat\mu_i+\sqrt{\ln(2m/\delta)/(2n_i)}$.

**D71 (regret prosty).** Dla wybranego zadania $\widehat i$ i najlepszego zadania $i^*$, $r=\mu_{i^*}-\mu_{\widehat i}\ge0$.

**D72 (straty asymetryczne).** Koszt błędnej decyzji może zależeć od zadania i ucznia; nie utożsamiamy maksymalizacji wyniku z minimalizacją szkody.

**D73 (budżet eksploracji).** Całkowita liczba prób wynosi $N=\sum_i n_i$.

**D74 (różnica wartości).** Przy dwóch zadaniach $\Delta=\mu_1-\mu_2$.

## Twierdzenia i dowody

**T77 (nieobciążoność średniej).** Przy D68 $\mathbb E\widehat\mu_i=\mu_i$.

*Dowód.* Liniowość wartości oczekiwanej: $\mathbb E(n_i^{-1}\sum_jX_{i,j})=n_i^{-1}n_i\mu_i=\mu_i$. $\square$

**T78 (nierówność koncentracji).** Dla $t>0$ przy D68:
$$P(|\widehat\mu_i-\mu_i|\ge t)\le2e^{-2n_it^2}.$$

*Dowód.* Jest to nierówność Hoeffdinga dla niezależnych zmiennych ograniczonych w przedziale długości jeden; podstawienie długości przedziałów do jej ogólnej postaci daje wskazany wykładnik. $\square$

**T79 (jednoczesne przedziały).** Z prawdopodobieństwem co najmniej $1-\delta$ dla wszystkich $m$ zadań jednocześnie zachodzi
$$|\widehat\mu_i-\mu_i|\le\sqrt{\ln(2m/\delta)/(2n_i)}.$$

*Dowód.* Dla każdego $i$ podstawienie promienia do T78 daje prawdopodobieństwo przekroczenia nie większe niż $\delta/m$. Nierówność sumy zdarzeń ogranicza prawdopodobieństwo choć jednego przekroczenia przez $\delta$. $\square$

**T80 (ograniczenie regret reguły optymistycznej).** Jeśli $\widehat i$ maksymalizuje $U_i$, to na zdarzeniu T79 zachodzi
$$0\le r\le2\sqrt{\frac{\ln(2m/\delta)}{2n_{\widehat i}}}.$$

*Dowód.* Oznaczmy promień zadania $i$ przez $b_i$. Na zdarzeniu T79 mamy $\mu_{i^*}\le U_{i^*}\le U_{\widehat i}=\widehat\mu_{\widehat i}+b_{\widehat i}\le\mu_{\widehat i}+2b_{\widehat i}$. Odejmujemy $\mu_{\widehat i}$. $\square$

**T81 (ograniczenie przy równych próbach).** Jeśli $n_i=n$ dla wszystkich $i$, to na zdarzeniu T79 $r\le\sqrt{2\ln(2m/\delta)/n}$.

*Dowód.* T80 i równość liczności prób dają $2\sqrt{\ln(2m/\delta)/(2n)}=\sqrt{2\ln(2m/\delta)/n}$. $\square$

**T82 (budżet równych prób).** Przy $n_i=n$ dla $m$ zadań, $N=mn$.

*Dowód.* Sumujemy $m$ identycznych składników w D73. $\square$

**T83 (nieujemność regret).** Dla każdego wyboru $\widehat i$ zachodzi $0\le r\le1$.

*Dowód.* $\mu_{i^*}$ jest maksimum średnich, a wszystkie $\mu_i\in[0,1]$ z D67. $\square$

**T84 (stabilność wyboru przy znanej luce).** Przy dwóch zadaniach i $\Delta>0$, jeśli $|\widehat\mu_1-\mu_1|<\Delta/2$ i $|\widehat\mu_2-\mu_2|<\Delta/2$, to $\widehat\mu_1>\widehat\mu_2$.

*Dowód.* $\widehat\mu_1>\mu_1-\Delta/2=\mu_2+\Delta/2>\widehat\mu_2$. $\square$

## Kontrprzykłady

**K41.** Bez niezależności T78 nie obowiązuje w tej postaci: jeśli wszystkie próby są tą samą zmienną Bernoulliego $(1/2)$, średnia nie koncentruje się wraz ze wzrostem $n$.

**K42.** Najwyższa średnia nie gwarantuje bezpieczeństwa: dwa zadania mogą mieć tę samą średnią, ale różne ryzyko rzadkiego niepożądanego wyniku.

**K43.** Reguła maksymalizująca $\widehat\mu_i$ może wybrać gorsze zadanie przy małej próbie; błąd estymacji nie znika deterministycznie.

**K44.** Więcej obserwacji z jednej grupy nie zastępuje reprezentatywności: przy systematycznym doborze próby $\widehat\mu_i$ może nie estymować średniej populacyjnej.

## Zadania rozwiązane

**Z97.** $X=(0,1,1,0)$: $\widehat\mu=1/2$.

**Z98.** Dla $m=2$, $\delta=0{,}1$, $n=100$ promień wynosi $\sqrt{\ln40/200}\approx0{,}1358$.

**Z99.** Przy $\widehat\mu=0{,}6$ i promieniu $0{,}1$, $U=0{,}7$.

**Z100.** Dla średnich $(0{,}7,0{,}5)$ i wyboru drugiego zadania, $r=0{,}2$.

**Z101.** Dla średnich $(0{,}7,0{,}5)$ i wyboru pierwszego zadania, $r=0$.

**Z102.** Dla $m=4$, $n=25$, budżet $N=100$.

**Z103.** Dla $m=5$ i promieni z T79, każdy indywidualny błąd ma prawdopodobieństwo przekroczenia co najwyżej $\delta/5$.

**Z104.** Dla $\Delta=0{,}2$ błędy obu średnich mniejsze niż $0{,}1$ zapewniają poprawny wybór w T84.

**Z105.** Przy $n=200$ i $m=2$, $\delta=0{,}1$, granica T81 wynosi $\sqrt{2\ln40/200}\approx0{,}1921$.

**Z106.** Dla $n=100$ i $m=2$ promień T79 jest mniejszy niż przy $n=25$ dokładnie dwukrotnie, ponieważ promień jest proporcjonalny do $1/\sqrt n$.

**Z107.** Dla $X_i\in[0,1]$ dowolna średnia empiryczna również należy do $[0,1]$, gdyż jest kombinacją wypukłą obserwacji.

**Z108.** Dla $m=3$ i $\delta=0{,}06$ ryzyko przekroczenia pojedynczego przedziału jest nie większe niż $0{,}02$, a któregokolwiek nie większe niż $0{,}06$.

## Zastrzeżenie metodologiczne

Twierdzenia T77–T84 wymagają określonych warunków losowania i ograniczoności zmiennych. W zastosowaniach edukacyjnych niezależność obserwacji, reprezentatywność i znaczenie skali wyników wymagają odrębnego uzasadnienia. Optymalizacja średniego wyniku nie zastępuje oceny ryzyka, dostępności ani sprawiedliwości oceniania.
