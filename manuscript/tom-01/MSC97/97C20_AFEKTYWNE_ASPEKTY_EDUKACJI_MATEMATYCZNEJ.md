---
title: "Ontologia Liczby i Geometrii — Tom I"
subtitle: "MSC 97C20. Emocje, motywacja i rzetelność pomiaru w edukacji matematycznej"
author: "Andrzej Mikulski"
date: "2026-11-02"
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Metryka.** MSC2020 **97C20 — Affective behavior and mathematics education**; rodzina G, poziom autorski I, taksonomia s. 10, minimum 4 strony. Rozdział jest opracowaniem matematycznych podstaw badania emocji i motywacji w edukacji. **Nie utożsamia** modelu matematycznego z empirycznie potwierdzoną teorią psychologiczną. Każde twierdzenie poniżej dotyczy jawnie podanego modelu; wnioskowanie przyczynowe wymaga osobnych założeń badawczych. Materiał historyczny Tomu I pozostaje odrębny i niezmieniony.

# 1. Od obserwacji do zmiennej

**D01 (jednostka badania).** Jednostką jest uczeń lub pojedyncza sesja uczenia się, z jednoznacznym identyfikatorem i czasem obserwacji. Pomiaru z dwóch sesji tej samej osoby nie traktuje się bez uzasadnienia jak dwóch niezależnych osób.

**D02 (wskaźnik afektywny).** Wskaźnik afektywny jest obserwowalną odpowiedzią, np. wyborem jednej z uporządkowanych kategorii deklarowanego napięcia przed zadaniem. Sam wskaźnik nie jest tożsamy z ukrytą emocją.

**D03 (skala porządkowa).** Skala $s_1\prec\cdots\prec s_k$ określa kolejność kategorii, ale nie zakłada równych odległości. Średnia liczb przypisanych kategoriom zależy od kodowania.

**D04 (zmienna binarna).** $Y\in\{0,1\}$ może oznaczać poprawne rozwiązanie ustalonego zadania. Prawdopodobieństwo $p=P(Y=1)$ zależy od populacji, treści zadania i warunków pomiaru.

**D05 (zmienna zakłócająca).** $C$ jest potencjalną zmienną zakłócającą relację między $A$ (np. deklarowanym lękiem) a $Y$, jeśli wpływa na rozkład obu i nie jest uwzględniona w porównaniu. Samo skorelowanie $C$ z $A$ nie dowodzi mechanizmu przyczynowego.

**D06 (brak danych).** $R=1$ oznacza zaobserwowanie odpowiedzi, $R=0$ jej brak. Mechanizm braków jest *całkowicie losowy względem $Y$* w rozpatrywanym modelu, gdy $R$ i $Y$ są niezależne.

**D07 (wyniki potencjalne).** Dla jednostki $i$ symbole $Y_i(1),Y_i(0)$ oznaczają hipotetyczne wyniki odpowiednio z interwencją i bez niej. Różnica $Y_i(1)-Y_i(0)$ jest indywidualnym efektem w modelu, lecz zwykle nie obserwuje się obu wartości.

**D08 (średni efekt).** Dla $N$ jednostek $\tau=N^{-1}\sum_{i=1}^N(Y_i(1)-Y_i(0))$. To wielkość matematyczna, nie automatycznie wynik dowolnego badania.

**D09 (przydział losowy).** W całkowicie losowym przydziale dokładnie $n_1$ spośród $N$ jednostek otrzymuje interwencję, a pozostałe $n_0=N-n_1$ stanowią kontrolę; każdy podzbiór rozmiaru $n_1$ ma to samo prawdopodobieństwo.

**D10 (błąd pomiaru).** Model $X^\ast=X+\varepsilon$ oddziela hipotetyczną wielkość $X$ od jej zaszumionego odczytu. Niezależność $\varepsilon$ od $X,Y$ jest założeniem, a nie własnością wszystkich ankiet.

**D11 (próba i populacja).** Statystyka z próby jest funkcją obserwacji. Przeniesienie jej na inną populację wymaga założeń o doborze próby i porównywalności warunków.

**D12 (aktualizacja bayesowska).** Stan $M\in\{0,1\}$ oznacza w modelu opanowanie określonej umiejętności, a $O$ — obserwację. $P(M=1\mid O)$ jest stopniem niepewności modelu, nie bezpośrednim odczytem stanu umysłu.

**D13 (dwustanowy model przejść).** W kroku czasowym stan 1 przechodzi do 0 z prawdopodobieństwem $a$, a stan 0 do 1 z prawdopodobieństwem $b$, gdzie $0<a,b<1$. Nie przypisuje się tym parametrom znaczenia psychologicznego bez walidacji.

**D14 (ryzyko błędu wielokrotnego).** Gdy analizuje się $m$ hipotez, rodzina zdarzeń fałszywych alarmów to $E_1,\dots,E_m$. Kontrola pojedynczego testu nie oznacza automatycznie kontroli całej rodziny.

**D15 (protokół rzetelności).** Protokół podaje populację, treść zadań, moment pomiaru, operacjonalizację wskaźników, sposób postępowania z brakami, hipotezy i regułę analizy przed interpretacją wyników.

# 2. Twierdzenia, założenia i dowody

**T01 (średnia mieszaniny).** Jeżeli populacja dzieli się na rozłączne grupy $G_1,\dots,G_k$ o liczebnościach $n_j>0$, to średnia zmiennej liczbowej wynosi
\[
\bar y=\sum_{j=1}^k \frac{n_j}{N}\bar y_j,\qquad N=\sum_j n_j.
\]
*Dowód.* Rozbijamy sumę $\sum_{i=1}^N y_i$ na sumy po grupach. Każda suma grupowa to $n_j\bar y_j$. Po podzieleniu przez $N$ otrzymujemy wzór. $\square$

**T02 (brak niezmienniczości średniej skali porządkowej).** Dla co najmniej trzech uporządkowanych kategorii istnieją dwa ściśle rosnące kodowania, które zachowują porządek, ale zmieniają porównanie średnich dwóch grup.
*Dowód.* Grupa A ma kategorie $(s_1,s_3)$, grupa B $(s_2,s_2)$. Dla kodowania $(1,2,3)$ obie średnie wynoszą 2. Dla kodowania $(1,2,100)$ średnia A wynosi 50,5, a B wynosi 2. Oba kodowania zachowują kolejność. $\square$

**T03 (prawo całkowitego prawdopodobieństwa).** Dla rozłącznego podziału $C_1,\dots,C_k$ o dodatnich prawdopodobieństwach:
\[
P(Y=1)=\sum_j P(Y=1\mid C_j)P(C_j).
\]
*Dowód.* Zdarzenia $\{Y=1\}\cap C_j$ są rozłączne i ich suma jest $\{Y=1\}$. Zastosowanie definicji prawdopodobieństwa warunkowego daje wzór. $\square$

**T04 (odwrócenie porównania po agregacji jest możliwe).** Istnieją dwie grupy A, B i dwa poziomy trudności, dla których w każdym poziomie odsetek sukcesów A jest większy, lecz odsetek łączny A jest mniejszy.
*Dowód przez konstrukcję.* Na poziomie łatwym A: $9/10=90\%$, B: $80/100=80\%$; na trudnym A: $20/100=20\%$, B: $1/10=10\%$. Łącznie A: $29/110\approx26,36\%$, B: $81/110\approx73,64\%$. Nierówności wewnątrz poziomów są odwrotne niż nierówność łączna, ponieważ wagi poziomów są różne. $\square$

**T05 (nieobciążoność różnicy średnich w całkowitej randomizacji).** Przy D07–D09, stałych wynikach potencjalnych, braku interferencji między jednostkami i pełnej obserwacji estymator
\[
\widehat\tau=\frac1{n_1}\sum_{i:Z_i=1}Y_i(1)-\frac1{n_0}\sum_{i:Z_i=0}Y_i(0)
\]
spełnia $E_Z[\widehat\tau]=\tau$.
*Dowód.* W losowaniu dokładnie $n_1$ jednostek $P(Z_i=1)=n_1/N$. Z liniowości wartości oczekiwanej pierwszy składnik ma wartość $N^{-1}\sum_iY_i(1)$; analogicznie drugi $N^{-1}\sum_iY_i(0)$. Różnica równa się $\tau$. Nie wymaga to normalności wyników. $\square$

**T06 (korelacja a klasyczny niezależny błąd pomiaru).** Jeżeli $X^\ast=X+\varepsilon$, $E\varepsilon=0$, $\varepsilon$ jest niezależny od $(X,Y)$, a wariancje $X,Y$ są dodatnie, to
\[
\operatorname{Corr}(X^\ast,Y)=\operatorname{Corr}(X,Y)
\sqrt{\frac{\operatorname{Var}(X)}{\operatorname{Var}(X)+\operatorname{Var}(\varepsilon)}}.
\]
*Dowód.* Niezależność daje $\operatorname{Cov}(\varepsilon,Y)=0$ i $\operatorname{Cov}(X,\varepsilon)=0$. Zatem kowariancja licznika jest niezmieniona, a wariancja $X^\ast$ to suma wariancji. Podstawiamy do definicji korelacji. $\square$

**T07 (braki niezależne od wyniku).** Jeśli $R$ i $Y$ są niezależne, $P(R=1)>0$ oraz $E|Y|<\infty$, to $E[Y\mid R=1]=E[Y]$.
*Dowód.* Niezależność oznacza, że rozkład warunkowy $Y$ przy $R=1$ jest rozkładem bezwarunkowym. Oba całkowania dają tę samą wartość. $\square$

**T08 (braki zależne od wyniku mogą odwrócić obraz).** Istnieje populacja o odsetku sukcesu $1/2$, dla której odsetek sukcesu wśród zaobserwowanych wynosi $9/10$.
*Dowód.* Niech $P(Y=1)=P(Y=0)=1/2$, $P(R=1\mid Y=1)=9/10$, $P(R=1\mid Y=0)=1/10$. Wtedy $P(Y=1,R=1)=9/20$ i $P(R=1)=1/2$, więc $P(Y=1\mid R=1)=9/10$. $\square$

**T09 (Bayes dla diagnostycznej obserwacji).** Jeśli $P(M=1)=\pi$, $P(O=+\mid M=1)=s$ i $P(O=+\mid M=0)=f$, gdzie $0<\pi<1$ i $s,f>0$, to
\[
P(M=1\mid O=+)=\frac{s\pi}{s\pi+f(1-\pi)}.
\]
*Dowód.* Licznik jest prawdopodobieństwem zdarzenia łącznego; mianownik sumą obu rozłącznych sposobów uzyskania obserwacji dodatniej. $\square$

**T10 (iloraz szans po obserwacji).** Przy założeniach T09 iloraz szans po obserwacji dodatniej jest ilorazem szans przed obserwacją pomnożonym przez $s/f$.
*Dowód.* Dzielimy prawdopodobieństwo z T09 przez jego dopełnienie: $[s\pi]/[f(1-\pi)]$. $\square$

**T11 (dynamika dwustanowego modelu).** Jeśli $p_t=P(M_t=1)$ w modelu D13, to
\[
p_{t+1}=(1-a-b)p_t+b.
\]
Punkt stały jest równy $p_\infty=b/(a+b)$, a
\[
p_t-p_\infty=(1-a-b)^t(p_0-p_\infty).
\]
*Dowód.* Stan 1 w następnym kroku powstaje z pozostania w 1 albo przejścia z 0. Daje to $(1-a)p_t+b(1-p_t)$. Rozwiązujemy równanie punktu stałego i odejmujemy je od rekurencji. Ponieważ $0<a,b<1$, zachodzi $|1-a-b|<1$, więc $p_t\to p_\infty$. $\square$

**T12 (monotoniczność funkcji logistycznej).** Funkcja $\sigma(x)=1/(1+e^{-x})$ jest ściśle rosnąca na $\mathbb R$ i $\sigma(-x)=1-\sigma(x)$.
*Dowód.* Różniczkowanie daje $\sigma'(x)=e^{-x}/(1+e^{-x})^2>0$. Równość symetrii wynika z przekształcenia ułamków. $\square$

**T13 (nierówność sumy zdarzeń).** Dla dowolnych zdarzeń $E_1,\dots,E_m$:
\[
P\!\left(\bigcup_{j=1}^m E_j\right)\le\sum_{j=1}^mP(E_j).
\]
*Dowód.* Wskaźnik unii nie przekracza sumy wskaźników zdarzeń. Bierzemy wartości oczekiwane. Niezależność nie jest potrzebna. $\square$

**T14 (kontrola rodziny testów).** Jeśli każdy z $m$ testów ma prawdopodobieństwo fałszywego alarmu co najwyżej $\alpha/m$, to prawdopodobieństwo przynajmniej jednego fałszywego alarmu jest nie większe niż $\alpha$.
*Dowód.* Stosujemy T13 do zdarzeń fałszywych alarmów. $\square$

**T15 (wariancja średniej niezależnych prób).** Dla niezależnych zmiennych Bernoulliego $Y_1,\dots,Y_n$ o wspólnym parametrze $p$:
\[
E\bar Y=p,\quad \operatorname{Var}(\bar Y)=\frac{p(1-p)}n\le\frac1{4n}.
\]
*Dowód.* Wartość oczekiwana sumy jest sumą wartości oczekiwanych; niezależność pozwala zsumować wariancje $p(1-p)$. Nierówność wynika z $p(1-p)=1/4-(p-1/2)^2$. $\square$

**T16 (granica prawdopodobieństwa dużego błędu).** W warunkach T15 dla $\varepsilon>0$:
\[
P(|\bar Y-p|\ge\varepsilon)\le\frac1{4n\varepsilon^2}.
\]
*Dowód.* Z nierówności Czebyszewa otrzymujemy ograniczenie $\operatorname{Var}(\bar Y)/\varepsilon^2$ i stosujemy T15. Nie jest to przedział ufności uzyskany bezwarunkowo dla każdej procedury doboru uczniów. $\square$

# 3. Kontrprzykłady: czego dane nie uprawniają do twierdzenia

**K01.** Wysoki wynik ankiety „lubię matematykę” nie implikuje poprawnego rozwiązania równania; wskaźnik afektywny i kompetencja są różnymi zmiennymi.

**K02.** Średnie 2,5 i 3 na skali porządkowej nie mają stałej interpretacji odległości bez założenia metrycznego; T02 pokazuje zależność od kodowania.

**K03.** Dodatnia korelacja między zainteresowaniem a wynikiem nie dowodzi, że zwiększenie zainteresowania wywoła wzrost wyniku: oba mogą zależeć od wcześniejszej wiedzy.

**K04.** W próbie bez losowego przydziału grupa z dodatkowymi zajęciami może mieć wyższy wynik już przed zajęciami; różnica końcowa nie identyfikuje automatycznie efektu.

**K05.** Dwie osoby mogą rozwiązać tę samą liczbę zadań, ale różne zadania. Porównanie sum bez ustalenia trudności może być mylące.

**K06.** W T04 każdy poziom trudności faworyzuje A, a agregacja B; ignorowanie struktury poziomów prowadzi do sprzecznej interpretacji.

**K07.** Jeśli osoby z niepowodzeniem częściej opuszczają pomiar, średnia wśród obecnych może rosnąć mimo niezmienionych kompetencji; zob. T08.

**K08.** Niezerowy błąd pomiaru może osłabiać korelację (T06), ale zależny od wyniku błąd może ją również sztucznie zwiększać. T06 nie stosuje się bez niezależności.

**K09.** Wysoka trafność pojedynczej odpowiedzi nie oznacza pewnego „opanowania” umiejętności; posterior w T09 zależy także od prioru i częstości fałszywie dodatnich odpowiedzi.

**K10.** Mała wartość $p$ dla jednej z 40 analiz nie świadczy sama przez się o kontroli ryzyka fałszywego odkrycia w całej rodzinie; zob. T14.

# 4. Zadania z pełnymi rozwiązaniami

**Z01.** W grupie 12 uczniów średnia liczba poprawnych odpowiedzi wynosi 6, a w grupie 18 uczniów 8. Wyznacz średnią łączną.  
*Rozwiązanie.* $(12\cdot6+18\cdot8)/30=216/30=7,2$.

**Z02.** Dla kategorii niski, średni, wysoki porównaj A=(niski,wysoki), B=(średni,średni) przy kodowaniu $(1,2,3)$ i $(1,2,100)$.  
*Rozwiązanie.* Pierwsze kodowanie: średnie $2$ i $2$; drugie: $50,5$ i $2$. Nie wolno uznać średniej porządkowej za niezmienniczą.

**Z03.** Poziom łatwy występuje z prawdopodobieństwem $0,7$, a trudny z $0,3$. Sukcesy warunkowe wynoszą odpowiednio $0,8$ i $0,2$.  
*Rozwiązanie.* $P(Y=1)=0,7\cdot0,8+0,3\cdot0,2=0,62$.

**Z04.** Zweryfikuj agregację z T04.  
*Rozwiązanie.* A ma 29 sukcesów w 110 próbach, B 81 w 110; $29/110<81/110$, mimo $9/10>80/100$ i $20/100>1/10$.

**Z05.** W całkowitej randomizacji $N=40$, $n_1=10$. Jakie jest prawdopodobieństwo przydziału ustalonego ucznia do interwencji?  
*Rozwiązanie.* $n_1/N=10/40=1/4$. Nie oznacza to, że każdy konkretny podzbiór 10 uczniów jest równie prawdopodobny przy dowolnej metodzie przydziału.

**Z06.** Jeśli dla każdego ucznia $Y_i(1)=Y_i(0)+2$, jaki jest $\tau$?  
*Rozwiązanie.* $\tau=N^{-1}\sum_i2=2$. W modelu z wynikami binarnymi taki przykład nie byłby dopuszczalny; tutaj wyniki są liczbowe.

**Z07.** Dla $\operatorname{Var}(X)=9$ i $\operatorname{Var}(\varepsilon)=7$ oblicz współczynnik osłabienia korelacji w T06.  
*Rozwiązanie.* $\sqrt{9/(9+7)}=3/4$. Korelacja pierwotna $0,8$ staje się $0,6$, jeśli wszystkie założenia T06 są spełnione.

**Z08.** W modelu T08 policz odsetek sukcesów wśród obserwowanych.  
*Rozwiązanie.* $\frac{(1/2)(9/10)}{(1/2)(9/10)+(1/2)(1/10)}=9/10$.

**Z09.** Prior opanowania $\pi=0,3$, czułość obserwacji $s=0,8$, fałszywie dodatni odsetek $f=0,2$. Oblicz posterior.  
*Rozwiązanie.* $(0,8\cdot0,3)/(0,8\cdot0,3+0,2\cdot0,7)=0,24/0,38=12/19$.

**Z10.** Oblicz iloraz szans po dodatniej obserwacji z Z09.  
*Rozwiązanie.* Prior odds $3/7$, iloraz wiarygodności $s/f=4$, posterior odds $12/7$, zgodnie z $(12/19)/(7/19)=12/7$.

**Z11.** W modelu D13 przy $a=0,2$, $b=0,3$ i $p_0=0,4$ oblicz $p_1$ oraz $p_\infty$.  
*Rozwiązanie.* $p_1=0,5\cdot0,4+0,3=0,5$; $p_\infty=0,3/0,5=0,6$.

**Z12.** Dla danych Z11 wyznacz $p_3$.  
*Rozwiązanie.* $p_3=0,6+0,5^3(0,4-0,6)=0,575$.

**Z13.** Wykaż, że $\sigma(0)=1/2$ oraz $\sigma(2)>1/2$.  
*Rozwiązanie.* $\sigma(0)=1/(1+1)=1/2$. Z monotoniczności T12 i $2>0$ wynika druga nierówność.

**Z14.** Dla 20 hipotez i rodzinnego poziomu błędu $\alpha=0,05$ podaj próg Bonferroniego.  
*Rozwiązanie.* $\alpha/20=0,0025$. Z T14 wynika ograniczenie prawdopodobieństwa co najmniej jednego fałszywego alarmu do 0,05.

**Z15.** Dla $n=100$ niezależnych odpowiedzi Bernoulliego z $p=1/2$ oblicz wariancję średniej.  
*Rozwiązanie.* $(1/2)(1/2)/100=1/400=0,0025$.

**Z16.** W warunkach T15, $n=400$, $\varepsilon=0,1$. Podaj granicę z T16.  
*Rozwiązanie.* $1/(4\cdot400\cdot0,1^2)=1/16=0,0625$. To konserwatywne ograniczenie, nie dokładne prawdopodobieństwo.

**Z17.** Uczeń ma prawdopodobieństwa poprawnej odpowiedzi $0,4$, $0,7$, $0,9$ na trzy różne zadania. Oblicz oczekiwaną liczbę sukcesów bez założenia niezależności.  
*Rozwiązanie.* Dla wskaźników $Y_j$ zachodzi $E(Y_1+Y_2+Y_3)=0,4+0,7+0,9=2$. Liniowość oczekiwania nie wymaga niezależności.

**Z18.** Dwie sesje tej samej osoby dały odpowiedzi 0 i 1. Czy wolno z T15 wywnioskować wariancję średniej równą $p(1-p)/2$?  
*Rozwiązanie.* Nie bez dodatkowego założenia niezależności. Jeśli odpowiedzi są doskonale zależne, wariancja średniej może być większa niż przy niezależności.

**Z19.** W grupie 60 uczniów 24 deklaruje wysoki stres, a 36 niski. Wśród pierwszych 12 uzyskało sukces, wśród drugich 27. Oblicz sukces łączny i warunkowy.  
*Rozwiązanie.* Łącznie $39/60=0,65$. Warunkowo: $12/24=0,5$ i $27/36=0,75$. Same odsetki nie rozstrzygają kierunku przyczynowości.

**Z20.** Zaprojektuj minimalny protokół badania wpływu dobrowolnego treningu matematycznego na wynik testu.  
*Rozwiązanie.* Z góry definiujemy populację, wynik i termin pomiaru; przydzielamy uczestników losowo do oferty treningu lub kontroli; rejestrujemy brakujące wyniki i odstępstwa; analizujemy różnicę średnich według przydziału (intention-to-treat). Estymandem jest efekt **oferty** treningu, a nie bez dodatkowych założeń efekt faktycznego uczestnictwa. Przed publikacją podajemy niepewność, liczbę uczestników i ograniczenia.

# 5. Zakres ważności i źródła

Wyniki T01–T16 są twierdzeniami rachunku prawdopodobieństwa, algebry i podstaw wnioskowania statystycznego **przy wskazanych założeniach**. Nie są dowodami, że konkretny program motywacyjny działa. Modele D12–D13 służą pokazaniu struktury wnioskowania o nieobserwowalnym stanie; nie zastępują walidacji psychometrycznej. Skale porządkowe, efekty selekcji, zależności między sesjami i wielokrotne testowanie wymagają osobnego raportowania.

**Literatura do dalszej weryfikacji:** S. S. Stevens, *On the Theory of Scales of Measurement*, Science 103 (1946), 677–680; D. B. Rubin, *Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies*, Journal of Educational Psychology 66 (1974), 688–701; Y. Benjamini, Y. Hochberg, *Controlling the False Discovery Rate*, JRSS B 57 (1995), 289–300; R. S. Baker, A. T. Corbett, V. Aleven, *More Accurate Student Modeling through Contextual Estimation of Slip and Guess Probabilities in Bayesian Knowledge Tracing*, ITS 2008. Bibliografia jest wskazówką naukową; nie oznacza przeprowadzenia przeglądu systematycznego.
