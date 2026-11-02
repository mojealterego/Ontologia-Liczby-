# MSC 97D40 — część III-F: próbkowanie, eksperyment dydaktyczny i granice wnioskowania

**Tom I, poziom III.** Nowy suplement matematyczny. Poniższe twierdzenia dotyczą skończonych populacji i jawnie określonych schematów losowania. Nie zastępują oceny etycznej ani walidacji rzeczywistego eksperymentu edukacyjnego.

## Definicje

**D57 (populacja skończona).** Populacja to indeksy $U=\{1,\ldots,N\}$, $N\ge2$, z ustalonymi wartościami $y_i\in\mathbb R$. Średnia populacji wynosi $\mu=N^{-1}\sum_i y_i$.

**D58 (wariancja populacyjna z poprawką).** $S_y^2=(N-1)^{-1}\sum_i(y_i-\mu)^2$.

**D59 (prosta próba losowa bez zwracania).** $S$ jest jednostajnie wybranym $n$-elementowym podzbiorem $U$, gdzie $1\le n\le N$.

**D60 (średnia i suma estymowana).** $\bar y_S=n^{-1}\sum_{i\in S}y_i$ i $\widehat T=N\bar y_S$.

**D61 (wskaźnik włączenia).** $I_i=\mathbf1_{\{i\in S\}}$, $\pi_i=P(I_i=1)$, $\pi_{ij}=P(I_i=I_j=1)$ dla $i\ne j$; przyjmujemy $\pi_{ii}=\pi_i$.

**D62 (estymator Horvitza–Thompsona).** Dla dowolnego schematu losowania z $\pi_i>0$ definiujemy $\widehat T_{\rm HT}=\sum_{i\in S}y_i/\pi_i$.

**D63 (wyniki potencjalne).** Każdy uczestnik ma ustalone dwie wartości $Y_i(1),Y_i(0)$. Efekt jednostkowy to $\tau_i=Y_i(1)-Y_i(0)$, a średni efekt skończonej populacji $\tau=N^{-1}\sum_i\tau_i$.

**D64 (pełna randomizacja).** Dokładnie $n_1$ uczestników, $1\le n_1<N$, otrzymuje wariant $1$; pozostałych $n_0=N-n_1$ wariant $0$. Każdy podzbiór rozmiaru $n_1$ jest jednakowo prawdopodobny.

**D65 (estymator różnicy średnich).** $\widehat\tau=\bar Y_{1,\mathrm{obs}}-\bar Y_{0,\mathrm{obs}}$, gdzie średnie obejmują obserwowane wyniki odpowiednich grup.

**D66 (warunek braku interferencji).** Wynik uczestnika zależy wyłącznie od jego własnego przypisania; nie zmienia się wraz z przypisaniem innych osób. W modelu D63 zakładamy również, że warianty interwencji są jednoznaczne.

## Twierdzenia z dowodami

**T66 (prawdopodobieństwa włączenia).** W prostej próbie losowej $\pi_i=n/N$, a dla $i\ne j$ i $n\ge2$ mamy $\pi_{ij}=n(n-1)/(N(N-1))$.

*Dowód.* Z $\binom Nn$ równolicznych prób $\binom{N-1}{n-1}$ zawiera ustalone $i$, a $\binom{N-2}{n-2}$ zawiera parę $i,j$. Ilorazy współczynników dwumianowych dają wzory. Dla $n=1$ prawdopodobieństwo pary wynosi zero. $\square$

**T67 (nieobciążoność średniej).** $\mathbb E[\bar y_S]=\mu$.

*Dowód.* Zapisujemy $\bar y_S=n^{-1}\sum_i I_i y_i$ i stosujemy liniowość wartości oczekiwanej oraz T66: $\mathbb E\bar y_S=n^{-1}(n/N)\sum_i y_i=\mu$. $\square$

**T68 (wariancja średniej bez zwracania).** Dla D57–D59:
$$\operatorname{Var}(\bar y_S)=\left(1-\frac nN\right)\frac{S_y^2}{n}.$$

*Dowód.* Niech $z_i=y_i-\mu$, zatem $\sum_i z_i=0$. Wariancja $\bar y_S$ to $n^{-2}\mathbb E(\sum_iI_i z_i)^2$. Rozwijając kwadrat, otrzymujemy
$$n^{-2}\left[\frac nN\sum_i z_i^2+\frac{n(n-1)}{N(N-1)}\sum_{i\ne j}z_i z_j\right].$$
Ponieważ $\sum_{i\ne j}z_i z_j=-(\sum_i z_i^2)$, wyrażenie upraszcza się do $(N-n)\sum_i z_i^2/[nN(N-1)]=(1-n/N)S_y^2/n$. $\square$

**T69 (pełny spis).** Dla $n=N$ średnia z próby jest deterministycznie równa $\mu$ i ma wariancję zero.

*Dowód.* Jedynym $N$-elementowym podzbiorem $U$ jest całe $U$. $\square$

**T70 (nieobciążoność estymatora sumy).** $\mathbb E[\widehat T]=\sum_i y_i$.

*Dowód.* Mnożymy obie strony T67 przez $N$. $\square$

**T71 (nieobciążoność Horvitza–Thompsona).** Dla dowolnego schematu z $\pi_i>0$ zachodzi $\mathbb E[\widehat T_{\rm HT}]=\sum_i y_i$.

*Dowód.* $\widehat T_{\rm HT}=\sum_i I_i y_i/\pi_i$, a $\mathbb E I_i=\pi_i$. Liniowość wartości oczekiwanej kończy dowód; niezależność włączeń nie jest potrzebna. $\square$

**T72 (wariancja Horvitza–Thompsona).** Przy definicjach D61–D62:
$$\operatorname{Var}(\widehat T_{\rm HT})=\sum_{i=1}^N\sum_{j=1}^N\frac{\pi_{ij}-\pi_i\pi_j}{\pi_i\pi_j}y_i y_j.$$

*Dowód.* Rozwijamy wariancję sumy wskaźników. $\operatorname{Cov}(I_i,I_j)=\mathbb E(I_iI_j)-\mathbb EI_i\,\mathbb EI_j=\pi_{ij}-\pi_i\pi_j$, również dla $i=j$, gdyż $I_i^2=I_i$. $\square$

**T73 (nieobciążoność efektu randomizacji).** Przy D63–D66 i pełnej randomizacji $\mathbb E[\widehat\tau]=\tau$.

*Dowód.* Każda grupa jest jednostajną próbą ustalonego rozmiaru z populacji odpowiednich wyników potencjalnych. Z T67 wynika $\mathbb E\bar Y_{1,\mathrm{obs}}=\overline{Y(1)}$ i $\mathbb E\bar Y_{0,\mathrm{obs}}=\overline{Y(0)}$. Różnica tych średnich wynosi $\tau$. $\square$

**T74 (wariancja Neymana).** Niech $S_1^2,S_0^2,S_\tau^2$ oznaczają wariancje skończonych populacji z mianownikiem $N-1$ dla $Y_i(1),Y_i(0),\tau_i$. Wtedy
$$\operatorname{Var}(\widehat\tau)=\frac{S_1^2}{n_1}+\frac{S_0^2}{n_0}-\frac{S_\tau^2}{N}.$$

*Dowód.* Dla wskaźników przypisania $Z_i$ mamy
$\widehat\tau=n_1^{-1}\sum_i Z_iY_i(1)-n_0^{-1}\sum_i(1-Z_i)Y_i(0)$.
Z T68 wariancje obu średnich wynoszą $(1-n_1/N)S_1^2/n_1$ i $(1-n_0/N)S_0^2/n_0$. Dla ustalonych tablic $a_i,b_i$ kowariancja ich średnich w rozłącznych grupach wynosi $-S_{ab}/N$, gdzie $S_{ab}=(N-1)^{-1}\sum_i(a_i-\bar a)(b_i-\bar b)$; wynika to z $\operatorname{Cov}(Z_i,1-Z_j)=-\operatorname{Cov}(Z_i,Z_j)$ i prawdopodobieństw T66. Wariancja różnicy zawiera więc $+2S_{10}/N$. Ponieważ $S_\tau^2=S_1^2+S_0^2-2S_{10}$, po zebraniu składników otrzymujemy wzór. $\square$

**T75 (konserwatywne ograniczenie).** W modelu T74:
$$0\le\operatorname{Var}(\widehat\tau)\le S_1^2/n_1+S_0^2/n_0.$$

*Dowód.* Lewa nierówność wynika z definicji wariancji; prawa z T74 i $S_\tau^2\ge0$. $\square$

**T76 (stały efekt).** Jeżeli $\tau_i=c$ dla wszystkich $i$, to $\operatorname{Var}(\widehat\tau)=S_1^2/n_1+S_0^2/n_0$.

*Dowód.* Wtedy $S_\tau^2=0$ i stosujemy T74. $\square$

## Kontrprzykłady

**K35 (próba wygodna).** Jeżeli do próby trafiają wyłącznie uczniowie z wynikiem $10$, podczas gdy połowa populacji ma wynik $0$, średnia próby $10$ nie estymuje bez obciążenia średniej populacji $5$.

**K36 (zwracanie).** Przy losowaniu ze zwracaniem prawdopodobieństwa wspólnego włączenia są inne; zastosowanie T68 bez poprawki schematu może zaniżyć lub zawyżyć wariancję.

**K37 (zerowa inkluzja).** Jeśli $\pi_i=0$ dla pewnego $i$ z $y_i\ne0$, wzór HT nie jest określony, a całkowitej sumy nie da się nieobciążenie oszacować tym estymatorem.

**K38 (interferencja).** Gdy wynik ucznia zależy od tego, czy jego kolega otrzymał interwencję, zapis $Y_i(z_i)$ nie obejmuje wszystkich możliwych wyników; T73 nie uzasadnia wówczas efektu przyjętego modelu.

**K39 (heterogeniczne efekty).** Przy $Y(0)=(0,0)$ i $Y(1)=(0,2)$ efekty to $(0,2)$, więc $S_\tau^2=2>0$; pominięcie składnika $-S_\tau^2/N$ w T74 nie daje równości.

**K40 (losowanie nie naprawia błędu pomiaru).** Jeśli w grupie interwencji wynik rejestrowany jest z systematycznym dodatkiem $5$, różnica średnich obserwowanych wyników może być obciążona względem efektu rzeczywistego mimo poprawnej randomizacji.

## Zadania z rozwiązaniami

**Z81.** $N=10,n=4$. **Rozwiązanie:** $\pi_i=4/10=0{,}4$.

**Z82.** $N=10,n=4$, $i\ne j$. **Rozwiązanie:** $\pi_{ij}=4\cdot3/(10\cdot9)=2/15$.

**Z83.** Populacja $(1,3,5)$, $n=2$. **Rozwiązanie:** $\mu=3$, trzy średnie prób wynoszą $2,3,4$, ich średnia wynosi $3$.

**Z84.** Dla Z83 oblicz $S_y^2$. **Rozwiązanie:** $[(1-3)^2+0+(5-3)^2]/(3-1)=4$.

**Z85.** Dla Z83 oblicz wariancję średniej. **Rozwiązanie:** $(1-2/3)\cdot4/2=2/3$.

**Z86.** $N=100,n=20,S_y^2=25$. **Rozwiązanie:** wariancja średniej wynosi $(1-0{,}2)\cdot25/20=1$.

**Z87.** $N=100,n=100$. **Rozwiązanie:** wariancja średniej wynosi $0$.

**Z88.** Dla $N=10$ i $\bar y_S=7$ estymowana suma to $\widehat T=70$.

**Z89.** W próbie z $\pi_1=1/2,\pi_2=1/4$ obserwujemy $y_1=3,y_2=2$. **Rozwiązanie:** $\widehat T_{\rm HT}=3/(1/2)+2/(1/4)=14$.

**Z90.** $N=4,n_1=n_0=2$, $Y(0)=(0,0,0,0)$, $Y(1)=(1,1,1,1)$. **Rozwiązanie:** $\widehat\tau=1$ dla każdego przypisania, więc wariancja $0$.

**Z91.** $Y(0)=(1,2,3,4)$, $Y(1)=(2,3,4,5)$. **Rozwiązanie:** $\tau_i=1$ i $\tau=1$.

**Z92.** Dla Z91 i $n_1=n_0=2$, $S_1^2=S_0^2=5/3$. **Rozwiązanie:** T74 daje wariancję $(5/3)/2+(5/3)/2=5/3$.

**Z93.** $N=4$, $Y(0)=(0,0,0,0)$, $Y(1)=(0,0,2,2)$. **Rozwiązanie:** $\tau=1$.

**Z94.** Dla Z93 $S_1^2=S_\tau^2=4/3$, $S_0^2=0$, $n_1=n_0=2$. **Rozwiązanie:** T74 daje $(4/3)/2-(4/3)/4=1/3$.

**Z95.** Dla Z93 możliwe średnie wyników leczonych wynoszą $0,1,2$ z prawdopodobieństwami odpowiednio $1/6,4/6,1/6$. **Rozwiązanie:** wariancja wynosi $(1/6)(0-1)^2+(1/6)(2-1)^2=1/3$.

**Z96.** $S_1^2=4,S_0^2=9,n_1=10,n_0=15$. **Rozwiązanie:** T75 daje górne ograniczenie $4/10+9/15=1$.

**Granica dowodowa.** T73–T76 wymagają poprawnej randomizacji, braku interferencji, spójnego pomiaru i stabilnych wyników potencjalnych. Związek przyczynowy w modelu losowym nie jest automatycznie przenoszalny na inną populację lub inną metodę dydaktyczną.
