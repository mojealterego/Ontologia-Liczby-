# MSC 97D40 — część III-E: rzetelność pomiaru, kalibracja i granice oceniania

**Tom I, poziom III.** Uzupełnienie rozdziału MSC 97D40. Własności poniższych modeli są twierdzeniami matematycznymi; ich zastosowanie do osób wymaga oddzielnej walidacji psychometrycznej i etycznej.

## Definicje

**D47 (model wyniku).** Wynik obserwowany to $Y=\theta+\varepsilon$, gdzie $\theta$ jest ustaloną wielkością modelową, a $\varepsilon$ błędem losowym o skończonej wariancji.

**D48 (nieobciążoność).** Estymator $\widehat\theta$ jest nieobciążony, gdy $\mathbb E[\widehat\theta]=\theta$.

**D49 (błąd średniokwadratowy).** $\operatorname{MSE}(\widehat\theta)=\mathbb E[(\widehat\theta-\theta)^2]$.

**D50 (średnia powtórzeń).** Dla $n\ge1$ pomiarów $Y_i$ przyjmujemy $\overline Y=n^{-1}\sum_iY_i$.

**D51 (błąd skorelowany).** Dla jednakowych wariancji $\operatorname{Var}(\varepsilon_i)=\sigma^2$ i jednakowych kowariancji $\operatorname{Cov}(\varepsilon_i,\varepsilon_j)=\rho\sigma^2$ dla $i\ne j$ parametr $\rho$ opisuje wspólną zależność błędów.

**D52 (próg decyzji).** Reguła $\delta_t(y)=\mathbf1_{\{y\ge t\}}$ klasyfikuje wynik względem progu $t$.

**D53 (próg z marginesem).** Dla $h>0$ decyzja trójwartościowa wynosi: „poniżej”, gdy $y<t-h$; „powyżej”, gdy $y>t+h$; „niepewne” w pozostałych przypadkach.

**D54 (kalibracja przedziałowa).** Dla poziomu $1-\alpha$ procedura $C(Y)$ jest pokrywająca, gdy $P_\theta(\theta\in C(Y))\ge1-\alpha$ dla wszystkich dopuszczalnych $\theta$.

**D55 (błąd ograniczony).** Model deterministyczny zakłada $|\varepsilon|\le e$ dla znanej stałej $e\ge0$.

**D56 (zmiana skali).** Dodatnie przeskalowanie wyniku ma postać $Y'=aY+b$, gdzie $a>0$.

## Twierdzenia i dowody

**T56 (rozkład MSE).** Jeśli $\widehat\theta$ ma skończony drugi moment, to
$$\operatorname{MSE}(\widehat\theta)=\operatorname{Var}(\widehat\theta)+(\mathbb E[\widehat\theta]-\theta)^2.$$

*Dowód.* Piszemy $\widehat\theta-\theta=(\widehat\theta-\mathbb E\widehat\theta)+(\mathbb E\widehat\theta-\theta)$. Po podniesieniu do kwadratu i wzięciu wartości oczekiwanej składnik mieszany znika, ponieważ pierwszy nawias ma średnią zero. $\square$

**T57 (wariancja średniej niezależnych pomiarów).** Jeśli błędy $\varepsilon_i$ są niezależne, mają średnią zero i wariancję $\sigma^2$, to $\overline Y$ jest nieobciążona i $\operatorname{Var}(\overline Y)=\sigma^2/n$.

*Dowód.* Liniowość wartości oczekiwanej daje $\mathbb E\overline Y=\theta$. Wariancja sumy niezależnych składników jest sumą wariancji, zatem $n^{-2}n\sigma^2=\sigma^2/n$. $\square$

**T58 (wariancja średniej skorelowanej).** W modelu D51:
$$\operatorname{Var}(\overline Y)=\frac{\sigma^2}{n}\bigl(1+(n-1)\rho\bigr).$$

*Dowód.* Rozwijamy wariancję sumy jako sumę $n$ wariancji i $n(n-1)$ uporządkowanych kowariancji, po czym dzielimy przez $n^2$. $\square$

**T59 (dopuszczalna korelacja równowymiarowa).** Dla $n\ge2$ i $\sigma^2>0$ wspólna korelacja D51 musi spełniać $-1/(n-1)\le\rho\le1$.

*Dowód.* Macierz korelacji ma postać $(1-\rho)I+\rho J$. Na podprzestrzeni prostopadłej do wektora jedynek ma wartość własną $1-\rho$, a na tym wektorze $1+(n-1)\rho$. Dodatnia półokreśloność obu wartości własnych daje tezę. $\square$

**T60 (nierówność Czebyszewa dla średniej).** Przy założeniach T57, dla $h>0$:
$$P(|\overline Y-\theta|\ge h)\le\frac{\sigma^2}{nh^2}.$$

*Dowód.* Stosujemy nierówność Markowa do nieujemnej zmiennej $(\overline Y-\theta)^2$, której wartość oczekiwana z T57 wynosi $\sigma^2/n$. $\square$

**T61 (przedział pokrycia bez założenia normalności).** Przy T57 i $0<\alpha<1$ przedział
$$C(\overline Y)=\left[\overline Y-\frac{\sigma}{\sqrt{n\alpha}},\,\overline Y+\frac{\sigma}{\sqrt{n\alpha}}\right]$$
ma pokrycie co najmniej $1-\alpha$, o ile $\sigma$ jest znane.

*Dowód.* W T60 podstawiamy $h=\sigma/\sqrt{n\alpha}$ dla $\sigma>0$. Gdy $\sigma=0$, średnia jest równa $\theta$ prawie na pewno i przedział zdegenerowany ma pokrycie $1$. $\square$

**T62 (stabilność klasyfikacji przy błędzie ograniczonym).** W modelu D55, jeśli $\theta<t-e$, to $\delta_t(Y)=0$, a jeśli $\theta\ge t+e$, to $\delta_t(Y)=1$.

*Dowód.* W pierwszym przypadku $Y\le\theta+e<t$. W drugim $Y\ge\theta-e\ge t$. $\square$

**T63 (niezmienniczość progu przy zmianie skali).** Dla $a>0$, $Y'=aY+b$ i $t'=at+b$ zachodzi $\delta_{t'}(Y')=\delta_t(Y)$.

*Dowód.* Nierówności $aY+b\ge at+b$ i $Y\ge t$ są równoważne, ponieważ $a>0$. $\square$

**T64 (niepewność przy progu).** Jeśli $|\varepsilon|\le e$ i $|Y-t|>e$, to znak $Y-t$ jest zgodny ze znakiem $\theta-t$.

*Dowód.* Z $|\theta-Y|\le e$ wynika: jeśli $Y>t+e$, to $\theta\ge Y-e>t$; jeśli $Y<t-e$, to $\theta\le Y+e<t$. $\square$

**T65 (minimalna liczba pomiarów dla granicy Czebyszewa).** Przy T57, $\sigma>0$, $h>0$ i $0<\alpha<1$ wystarczy $n\ge\lceil\sigma^2/(\alpha h^2)\rceil$, aby $P(|\overline Y-\theta|\ge h)\le\alpha$.

*Dowód.* Podstawiamy ograniczenie na $n$ do prawej strony T60. $\square$

## Kontrprzykłady

**K29.** Nieobciążoność nie oznacza małego MSE: estymator $\theta+Z$ z $\mathbb EZ=0$, $\operatorname{Var}Z=10^6$ jest nieobciążony, lecz ma MSE $10^6$.

**K30.** Powtarzanie tego samego skorelowanego pomiaru nie musi redukować wariancji: przy $\rho=1$ T58 daje $\operatorname{Var}(\overline Y)=\sigma^2$ dla każdego $n$.

**K31.** Bez znajomości $\sigma$ nie wolno przedstawiać przedziału T61 jako gwarantowanego: dowolnie niedoszacowana wariancja może prowadzić do niedostatecznego pokrycia.

**K32.** Przy $a<0$ T63 jest fałszywe: dla $a=-1$, $b=t=0$, $Y=1$ otrzymujemy $\delta_0(Y)=1$, ale $\delta_0(-Y)=0$.

**K33.** Sama odległość $|Y-t|\le e$ nie przesądza o prawdziwej klasie: przy $Y=t$ i $e>0$ zgodne z pomiarem są $\theta=t-e$ i $\theta=t+e$.

**K34.** Dla $n=3$ i $\rho=-0{,}9$ rzekoma macierz korelacji D51 ma wartość własną $1+2\rho=-0{,}8$ i nie może być macierzą kowariancji.

## Zadania rozwiązane

**Z65.** Estymator o wariancji $4$ i obciążeniu $3$. **Rozwiązanie:** T56 daje MSE $=4+3^2=13$.

**Z66.** $n=16$, $\sigma^2=9$, pomiary niezależne. **Rozwiązanie:** $\operatorname{Var}(\overline Y)=9/16$.

**Z67.** $n=4$, $\sigma^2=9$, $\rho=1/3$. **Rozwiązanie:** T58 daje $(9/4)(1+3/3)=9/2$.

**Z68.** $n=5$, $\rho=-1/4$. **Rozwiązanie:** jest to dolna granica T59; wariancja średniej w modelu wynosi zero.

**Z69.** $n=100$, $\sigma=2$, $h=1$. **Rozwiązanie:** T60 daje prawdopodobieństwo co najwyżej $4/(100\cdot1)=0{,}04$.

**Z70.** $n=100$, $\sigma=2$, $\alpha=0{,}05$. **Rozwiązanie:** promień T61 to $2/\sqrt5\approx0{,}8944$.

**Z71.** $\sigma^2=4$, $h=1$, $\alpha=0{,}05$. **Rozwiązanie:** T65 wymaga $n\ge\lceil4/0{,}05\rceil=80$.

**Z72.** $t=50$, $e=3$, $\theta=46$. **Rozwiązanie:** ponieważ $46<47$, klasyfikacja jest na pewno poniżej progu.

**Z73.** $t=50$, $e=3$, $\theta=53$. **Rozwiązanie:** $\theta\ge t+e$, więc klasyfikacja $\delta_t(Y)=1$.

**Z74.** $t=50$, $e=3$, $Y=55$. **Rozwiązanie:** $Y>53$, więc $\theta>50$ niezależnie od dopuszczalnego błędu.

**Z75.** $Y=7$, $t=5$, $a=2$, $b=3$. **Rozwiązanie:** $Y'=17$, $t'=13$; obie reguły zwracają $1$.

**Z76.** $Y=4$, $t=5$, $a=2$, $b=3$. **Rozwiązanie:** $Y'=11$, $t'=13$; obie reguły zwracają $0$.

**Z77.** $n=3$, $\rho=-1/2$. **Rozwiązanie:** to dopuszczalna granica dolna T59.

**Z78.** $n=3$, $\rho=-3/4$. **Rozwiązanie:** $-3/4<-1/2$, więc nie istnieje taka macierz korelacji równokorelacyjnej.

**Z79.** $n=4$, $\sigma^2=1$, $\rho=0$. **Rozwiązanie:** T58 daje $1/4$.

**Z80.** $n=4$, $\sigma^2=1$, $\rho=1$. **Rozwiązanie:** T58 daje $1$; powtarzanie idealnie zależnego pomiaru nie zwiększa precyzji.

## Granice weryfikacji

Powyższe twierdzenia są ścisłe wyłącznie w jawnie opisanych modelach. Wynik ucznia nie jest sam z siebie addytywnym pomiarem jednej stałej zdolności. Zależność błędów, trafność konstruktu, warunki przeprowadzania testu i wpływ interwencji muszą być badane empirycznie. Nie należy stosować tych wzorów do automatycznych decyzji o uczniach bez niezależnej walidacji i nadzoru człowieka.
