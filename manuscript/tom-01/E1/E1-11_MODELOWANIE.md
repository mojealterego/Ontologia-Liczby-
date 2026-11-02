---
title: "Ontologia Liczby — Tom I"
subtitle: "E1-11. Modelowanie matematyczne: od danych i założeń do sprawdzalnych przewidywań"
author: "Andrzej Mikulski"
date: "2026-11-02"
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Pozycja taksonomiczna:** E1-11, poziom I, minimum źródłowe 4 strony. Ten rozdział zamyka edukacyjną sekwencję E1 w roboczej mapie taksonomii, ale **nie** oznacza ukończenia Tomu I. Stanowi niezależny materiał do późniejszej integracji z rzeczywistym monolitem 0.20. Nie zastępuje ani nie modyfikuje historycznego wstępu, E1-01–E1-10 i istniejących rozdziałów F. Modele są jawnie uproszczone; wynik matematyczny nie jest automatycznie prawdą o świecie.

# A. Język modelowania i zasady poprawności

**D1 (układ rzeczywisty i model).** Układ rzeczywisty to przedmiot obserwacji; model matematyczny to zespół zmiennych, założeń, równań i ograniczeń służących do opisu wybranych cech układu. Model nie jest tożsamy z układem.

**D2 (wielkość i jednostka).** Wielkość mierzalna jest parą wartości liczbowej i jednostki. Dodawanie wymaga zgodnych wymiarów; mnożenie i dzielenie jednostek podlega odpowiednim regułom algebraicznym.

**D3 (zmienna i parametr).** Zmienna jest argumentem mogącym przyjmować wartości z określonej dziedziny. Parametr pozostaje ustalony w obrębie jednego zastosowania modelu, ale może zmieniać się między zastosowaniami.

**D4 (dziedzina fizyczna).** Dziedzina fizyczna jest podzbiorem dziedziny algebraicznej spełniającym ograniczenia rzeczywiste: np. czas nieujemny, liczba osób całkowita, masa nieujemna.

**D5 (założenie modelowe).** Założenie jest jawnym uproszczeniem, którego nie wyprowadza się z samej matematyki, np. stała prędkość, brak strat lub niezmienna cena.

**D6 (model proporcjonalny).** Model proporcjonalności prostej ma postać $y=kx$, gdzie $k$ jest stałym współczynnikiem, a dziedzina i jednostki są jawne.

**D7 (model afiniczny).** Model liniowy z wyrazem wolnym ma postać $y=ax+b$. W szkolnym języku nazywa się go często liniowym, choć jako odwzorowanie liniowe w sensie algebry liniowej jest liniowy tylko przy $b=0$.

**D8 (model odwrotnej proporcjonalności).** Dla $x\ne0$ model ma postać $y=k/x$; stałość iloczynu $xy=k$ jest jego cechą rozpoznawczą.

**D9 (obserwacja i reszta).** Dla obserwacji $(x_i,y_i)$ i przewidywania $\widehat y_i=f(x_i)$ reszta to $r_i=y_i-\widehat y_i$. Reszta jest różnicą wartości, nie dowodem błędu pomiarowego ani przyczynowości.

**D10 (kalibracja).** Kalibracja polega na wyznaczeniu parametrów modelu na podstawie danych i ustalonego kryterium dopasowania.

**D11 (walidacja).** Walidacja sprawdza model na danych lub warunkach nieużytych do kalibracji, z podaniem kryterium akceptacji.

**D12 (interpolacja i ekstrapolacja).** Interpolacja przewiduje wartości pomiędzy obserwowanymi argumentami; ekstrapolacja poza ich zakresem wymaga dodatkowego uzasadnienia.

**D13 (niepewność przedziałowa).** Zapis $x\in[L,U]$ wyraża, że rzeczywista wartość znajduje się w podanym przedziale przy przyjętych założeniach. Nie przypisuje sam przez się prawdopodobieństwa.

**D14 (identyfikowalność).** Parametr jest identyfikowalny z danych w zadanej klasie modeli, gdy nie istnieją dwa różne jego dopuszczalne zestawy dające identyczne obserwacje.

**D15 (błąd bezwzględny i względny).** Dla wartości rzeczywistej $y$ i przybliżenia $\widehat y$ błąd bezwzględny to $|y-\widehat y|$, a względny to $|y-\widehat y|/|y|$ wyłącznie przy $y\ne0$.

**D16 (model dyskretny).** Model dyskretny określa wartości w krokach $n\in\mathbb N_0$, np. $x_{n+1}=qx_n+c$, z podanym stanem początkowym.

**D17 (model deterministyczny).** Przy ustalonych parametrach i warunkach początkowych model deterministyczny przypisuje każdemu dopuszczalnemu argumentowi jedno przewidywanie; nie oznacza to, że świat jest deterministyczny.

**D18 (analiza wrażliwości).** Analiza wrażliwości bada zmianę wyniku pod wpływem zmiany danych lub parametrów, przy zachowaniu określonych założeń.

# B. Twierdzenia i dowody

**T1 (jednoznaczna kalibracja afiniczna).** Dla dwóch punktów $(x_1,y_1)$, $(x_2,y_2)$ o $x_1\ne x_2$ istnieje dokładnie jeden model $y=ax+b$ przechodzący przez oba punkty, przy czym
$$a=\frac{y_2-y_1}{x_2-x_1},\qquad b=y_1-ax_1.$$

*Dowód.* Odejmując równania $y_1=ax_1+b$ i $y_2=ax_2+b$, otrzymujemy $y_2-y_1=a(x_2-x_1)$, więc $a$ jest wyznaczone jednoznacznie. Pierwsze równanie wyznacza $b$. Podstawienie potwierdza oba punkty. $\square$

**T2 (kryterium proporcjonalności).** Model afiniczny $f(x)=ax+b$ jest proporcjonalny w sensie $f(x)=kx$ na dziedzinie zawierającej co najmniej dwie różne liczby wtedy i tylko wtedy, gdy $b=0$.

*Dowód.* Jeśli $b=0$, bierzemy $k=a$. Jeśli $ax+b=kx$ dla dwóch różnych argumentów, odejmowanie równań daje $a=k$, a więc $b=0$. $\square$

**T3 (iloraz w modelu proporcjonalnym).** Dla $y=kx$ i $x\ne0$ zachodzi $y/x=k$. Odwrotnie, stały iloraz $y/x=k$ dla wszystkich niezerowych $x$ w dziedzinie wyznacza ten model.

*Dowód.* Dzielenie pierwszej równości przez $x$ i mnożenie drugiej przez $x$. $\square$

**T4 (iloczyn w odwrotnej proporcjonalności).** Dla $x\ne0$ równość $y=k/x$ jest równoważna $xy=k$.

*Dowód.* Mnożymy obie strony przez $x$ lub dzielimy przez niezerowe $x$. $\square$

**T5 (średnia mieszaniny).** Jeśli łączymy dwie jednorodne partie o dodatnich masach $m_1,m_2$ i stężeniach ułamkowych $c_1,c_2$, bez reakcji i strat substancji, to stężenie mieszaniny wynosi
$$c=\frac{m_1c_1+m_2c_2}{m_1+m_2}.$$

*Dowód.* Masy substancji w partiach wynoszą $m_1c_1$ i $m_2c_2$; po zsumowaniu dzielimy masę substancji przez całkowitą masę mieszaniny. $\square$

**T6 (ograniczenie mieszaniny).** W warunkach T5 zachodzi $\min(c_1,c_2)\le c\le\max(c_1,c_2)$.

*Dowód.* Wagi $w_i=m_i/(m_1+m_2)$ są nieujemne i sumują się do 1. Zatem $c=w_1c_1+w_2c_2$ jest kombinacją wypukłą dwóch liczb. $\square$

**T7 (droga przy stałej prędkości).** Przy stałej prędkości $v\ge0$ i czasie $t\ge0$ droga wynosi $s=vt$; dla $v>0$ czas pokonania drogi $s$ wynosi $t=s/v$.

*Dowód.* Pierwsza zależność jest przyjętą definicją modelu stałej prędkości, druga wynika algebraicznie przez dzielenie przez $v>0$. Nie jest to twierdzenie o ruchu przy zmiennej prędkości. $\square$

**T8 (zmiana jednostki prędkości).** Liczba opisująca tę samą prędkość w $\mathrm{m/s}$ jest równa liczbie w $\mathrm{km/h}$ podzielonej przez $3{,}6$.

*Dowód.* $1\,\mathrm{km/h}=1000\,\mathrm m/3600\,\mathrm s=(1/3{,}6)\,\mathrm{m/s}$. $\square$

**T9 (próg rentowności).** Jeśli koszt $K(q)=F+cq$ i przychód $R(q)=pq$ dla $q\ge0$, przy $p>c$, to zysk $R(q)-K(q)$ jest nieujemny wtedy i tylko wtedy, gdy $q\ge F/(p-c)$.

*Dowód.* $R-K=(p-c)q-F$. Dzielimy nierówność $(p-c)q\ge F$ przez dodatnie $p-c$. Jeśli $q$ oznacza liczbę sztuk, minimalną dopuszczalną liczbą jest sufit progu. $\square$

**T10 (monotoniczność modelu afinicznego).** Dla $x_2>x_1$, znak $f(x_2)-f(x_1)$ jest znakiem współczynnika $a$ modelu $f(x)=ax+b$.

*Dowód.* $f(x_2)-f(x_1)=a(x_2-x_1)$, a drugi czynnik jest dodatni. $\square$

**T11 (propagacja błędu w modelu afinicznym).** Jeśli $|x-\widehat x|\le\varepsilon$ i $f(x)=ax+b$, to $|f(x)-f(\widehat x)|\le |a|\varepsilon$.

*Dowód.* Różnica to $a(x-\widehat x)$; po wzięciu modułu stosujemy założone ograniczenie. $\square$

**T12 (przedział prognozy przy dodatnim nachyleniu).** Jeśli $a\ge0$ i $x\in[L,U]$, to $ax+b\in[aL+b,aU+b]$.

*Dowód.* Pomnożenie $L\le x\le U$ przez $a\ge0$ i dodanie $b$ zachowuje kierunki nierówności. $\square$

**T13 (średnia minimalizuje sumę kwadratów).** Dla danych $y_1,\ldots,y_n$ ($n\ge1$) jedyną liczbą minimalizującą $\sum_i(y_i-c)^2$ jest średnia $\bar y=(\sum_i y_i)/n$.

*Dowód.* Po rozwinięciu wokół $\bar y$ mamy $\sum_i(y_i-c)^2=\sum_i(y_i-\bar y)^2+n(c-\bar y)^2$, bo $\sum_i(y_i-\bar y)=0$. Drugi składnik jest nieujemny i znika wyłącznie przy $c=\bar y$. $\square$

**T14 (nachylenie metody najmniejszych kwadratów).** Jeśli $n\ge2$ i nie wszystkie $x_i$ są równe, to jedyne parametry minimalizujące
$$S(a,b)=\sum_{i=1}^n(y_i-ax_i-b)^2$$
są dane przez
$$a=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}{\sum_i(x_i-\bar x)^2},\qquad b=\bar y-a\bar x.$$

*Dowód.* Dla ustalonego $a$ zastosowanie T13 do liczb $y_i-ax_i$ daje $b=\bar y-a\bar x$. Po podstawieniu i oznaczeniu $u_i=x_i-\bar x$, $v_i=y_i-\bar y$ mamy $S(a)=\sum_i(v_i-au_i)^2$. Uzupełnienie kwadratu:
$$S(a)=\sum_i v_i^2-\frac{(\sum_i u_iv_i)^2}{\sum_i u_i^2}+\Big(\sum_i u_i^2\Big)\Big(a-\frac{\sum_i u_iv_i}{\sum_i u_i^2}\Big)^2.$$
Ponieważ mianownik jest dodatni, minimum jest jedyne i występuje dla wskazanego $a$. $\square$

**T15 (zerowa suma reszt regresji z wyrazem wolnym).** Dla parametrów z T14 zachodzi $\sum_i r_i=0$.

*Dowód.* $\sum_i r_i=\sum_i y_i-a\sum_i x_i-nb=n(\bar y-a\bar x-b)=0$. $\square$

**T16 (ortogonalność reszt).** Dla parametrów z T14 zachodzi $\sum_i x_i r_i=0$.

*Dowód.* Z warunku minimalizacji kwadratu w dowodzie T14 otrzymujemy $\sum_i(x_i-\bar x)r_i=0$. Ponieważ $\sum_i r_i=0$ na mocy T15, po rozwinięciu otrzymujemy $\sum_i x_i r_i=0$. $\square$

**T17 (model wzrostu geometrycznego).** Jeśli $x_0>0$ i $x_{n+1}=qx_n$ dla $q>0$, to $x_n=x_0q^n$.

*Dowód.* Dla $n=0$ równość jest oczywista. Z założenia indukcyjnego $x_{n+1}=q x_0q^n=x_0q^{n+1}$. $\square$

**T18 (suma stałych przyrostów).** Jeśli $x_{n+1}=x_n+d$, to $x_n=x_0+nd$.

*Dowód.* Indukcja po $n$: krok $x_{n+1}=x_0+nd+d=x_0+(n+1)d$. $\square$

**T19 (granica błędu sumy).** Jeśli $|x-\widehat x|\le\varepsilon_x$ i $|y-\widehat y|\le\varepsilon_y$, to $|(x+y)-(\widehat x+\widehat y)|\le\varepsilon_x+\varepsilon_y$.

*Dowód.* Nierówność trójkąta dla $(x-\widehat x)+(y-\widehat y)$. $\square$

**T20 (nieidentyfikowalność modelu bez ograniczenia klasy).** Dla skończonych różnych argumentów $x_1,\ldots,x_n$ i dowolnego wielomianu $p$ przechodzącego przez dane $(x_i,y_i)$ istnieje nieskończenie wiele wielomianów dających te same obserwacje.

*Dowód.* Dla dowolnego $c\in\mathbb R$ wielomian $p_c(x)=p(x)+c\prod_{i=1}^n(x-x_i)$ spełnia $p_c(x_i)=p(x_i)=y_i$. Różne $c$ dają różne wielomiany. $\square$

**T21 (zachowanie bilansu).** Jeśli stan zasobu $M_n$ zmienia się wyłącznie o dopływ $I_n$ i odpływ $O_n$ w kroku $n$, to $M_{n+1}=M_n+I_n-O_n$, a po $N$ krokach
$$M_N=M_0+\sum_{n=0}^{N-1}I_n-\sum_{n=0}^{N-1}O_n.$$

*Dowód.* Sumujemy równania dla kolejnych kroków; wyrazy pośrednie $M_1,\ldots,M_{N-1}$ redukują się teleskopowo. $\square$

**T22 (jednostki współczynników).** Jeśli $y=ax+b$, gdzie $x$ i $y$ mają odpowiednio wymiary $[X]$ i $[Y]$, to $[a]=[Y]/[X]$ i $[b]=[Y]$.

*Dowód.* Każdy składnik sumy $ax+b$ musi mieć wymiar $[Y]$; z $[a][X]=[Y]$ otrzymujemy wynik. $\square$

# C. Kontrprzykłady i pułapki

**K1.** Dwa punkty $(0,0)$ i $(1,1)$ pasują zarówno do $y=x$, jak i do $y=x^2$; zgodność z dwoma obserwacjami nie dowodzi prawa liniowego.

**K2.** Model $y=2x+5$ nie jest proporcjonalnością prostą: dla $x=0$ otrzymujemy $y=5$, nie 0.

**K3.** Dla $y=10/x$ podstawienie $x=0$ jest niedozwolone; dziedzina nie może być pominięta.

**K4.** Średnia prędkość na dwóch odcinkach tej samej długości przejechanych z prędkościami 30 i 60 km/h wynosi 40 km/h, a nie 45 km/h: czasy dla drogi $d$ to $d/30$ i $d/60$, więc $2d/(d/30+d/60)=40$.

**K5.** Cena $100$ zł po podwyżce o 20% i obniżce o 20% wynosi $96$ zł, nie $100$ zł: $100\cdot1{,}2\cdot0{,}8=96$.

**K6.** Z korelacji między sprzedażą lodów i liczbą kąpieli nie wynika, że lody powodują kąpiele; temperatura może wpływać na obie zmienne.

**K7.** Model kosztu $K(q)=50+3q$ nie daje sensownej prognozy dla $q=-10$ sztuk mimo algebraicznej możliwości podstawienia.

**K8.** Dopasowanie wielomianu stopnia 9 do 10 punktów nie gwarantuje dobrych prognoz poza zakresem danych.

**K9.** Przy danych $(1,2)$ i $(1,5)$ nie istnieje funkcja $y=f(x)$ przechodząca przez oba punkty: ten sam argument nie może mieć dwóch wartości.

**K10.** Przy $x=0$ błąd względny względem $x$ jest niezdefiniowany; nawet gdy błąd bezwzględny wynosi 0.

**K11.** Przy $m_1=m_2$ i stężeniach 10% i 30% wynik to 20%; przy nierównych masach średnia arytmetyczna 20% na ogół nie jest poprawna.

**K12.** Prognoza wzrostu liczby mieszkańców $x_n=100(1{,}1)^n$ nie może być bezrefleksyjnie stosowana w nieskończoność; ograniczenia zasobów mogą złamać założenie stałego tempa.

# D. Zadania rozwiązane — podstawy i kalibracja

**Z1.** Cena 4 jednakowych zeszytów to 28 zł. Model i cena 9 zeszytów? *Rozwiązanie:* $C(q)=7q$ zł, więc $C(9)=63$ zł.

**Z2.** Taksówka pobiera 8 zł opłaty początkowej i 3 zł/km. Cena 12 km? *Rozwiązanie:* $C(d)=8+3d$, $C(12)=44$ zł.

**Z3.** Dla punktów $(1,5)$ i $(4,14)$ wyznacz $y=ax+b$. *Rozwiązanie:* $a=(14-5)/(4-1)=3$, $b=5-3=2$, zatem $y=3x+2$.

**Z4.** Model $y=5x-7$. Dla jakiego $x$ wartość wynosi 18? *Rozwiązanie:* $5x-7=18$, $x=5$.

**Z5.** Czy punkty $(1,3),(2,6),(3,9)$ są zgodne z proporcjonalnością prostą? *Rozwiązanie:* Wszystkie ilorazy $y/x$ wynoszą 3, więc tak: $y=3x$.

**Z6.** Czy punkty $(1,4),(2,7),(3,10)$ są proporcjonalne? *Rozwiązanie:* Nie; pasują do modelu afinicznego $y=3x+1$, którego wyraz wolny jest niezerowy.

**Z7.** Sześciu pracowników kończy zadanie w 10 godzin. Ilu godzin potrzeba 15 jednakowo wydajnym pracownikom przy doskonałej podzielności pracy? *Rozwiązanie:* $6\cdot10=60$ roboczogodzin, więc $60/15=4$ godziny.

**Z8.** Prędkość 72 km/h wyraź w m/s. *Rozwiązanie:* $72/3{,}6=20$ m/s.

**Z9.** Samochód jedzie 90 km/h przez 2,5 h. Droga? *Rozwiązanie:* $s=90\cdot2{,}5=225$ km.

**Z10.** Dystans 150 km, stała prędkość 75 km/h. Czas? *Rozwiązanie:* $t=150/75=2$ h.

**Z11.** Stały koszt 400 zł, koszt jednostkowy 12 zł, cena 20 zł. Minimalna liczba całych sztuk do braku straty? *Rozwiązanie:* $(20-12)q\ge400$, więc $q\ge50$.

**Z12.** W warunkach Z11 zysk przy 80 sztukach? *Rozwiązanie:* $(20-12)80-400=240$ zł.

**Z13.** Masa 2 kg roztworu 10% i 3 kg roztworu 20%. Stężenie? *Rozwiązanie:* $(2\cdot0{,}10+3\cdot0{,}20)/5=0{,}16$, czyli 16%.

**Z14.** Zmieszaj 1 kg roztworu 30% z 4 kg roztworu 5%. Stężenie? *Rozwiązanie:* $(0{,}30+0{,}20)/5=0{,}10$, czyli 10%.

**Z15.** W zbiorniku jest 40 l, dopływ 5 l/min, odpływ 2 l/min. Ile po 12 minutach? *Rozwiązanie:* $40+(5-2)\cdot12=76$ l, przy założeniu stałych przepływów.

**Z16.** W zbiorniku 70 l, wypływa 4 l/min, brak dopływu. Kiedy będzie pusty? *Rozwiązanie:* $70/4=17{,}5$ min; model ważny do chwili opróżnienia.

# E. Zadania rozwiązane — skale, dane i błędy

**Z17.** Mapa ma skalę 1:25000. Odległość 8 cm na mapie odpowiada ilu kilometrom? *Rozwiązanie:* $8\cdot25000=200000$ cm = 2 km.

**Z18.** Model długości $y=2x+3$; $x\in[4,5]$. Podaj zakres $y$. *Rozwiązanie:* $y\in[11,13]$.

**Z19.** Model $y=-3x+10$, $x\in[1,2]$. Podaj zakres $y$. *Rozwiązanie:* Funkcja maleje, więc $y\in[4,7]$.

**Z20.** Dla $f(x)=4x+2$ pomiar $x$ ma błąd nie większy niż 0,1. Maksymalny błąd wyniku? *Rozwiązanie:* $|4|\cdot0{,}1=0{,}4$.

**Z21.** Dwa niezależnie nieokreślone błędy bezwzględne są ograniczone przez 0,2 i 0,3. Granica błędu sumy? *Rozwiązanie:* 0,5, bez konieczności zakładania niezależności probabilistycznej.

**Z22.** Zaobserwowano $y=(2,4,6)$ dla $x=(1,2,3)$. Dopasuj $y=ax+b$. *Rozwiązanie:* Dane leżą dokładnie na $y=2x$, więc $a=2$, $b=0$, reszty 0.

**Z23.** Zaobserwowano $y=(1,2,5)$ przy $x=(0,1,2)$. Oblicz średnią $y$. *Rozwiązanie:* $\bar y=(1+2+5)/3=8/3$.

**Z24.** Dla danych Z23 wyznacz regresję najmniejszych kwadratów. *Rozwiązanie:* $\bar x=1$, $\bar y=8/3$, $\sum(x_i-\bar x)^2=2$, $\sum(x_i-\bar x)(y_i-\bar y)=4$. Zatem $a=2$, $b=2/3$.

**Z25.** Dla modelu Z24 oblicz reszty. *Rozwiązanie:* Prognozy to $(2/3,8/3,14/3)$, reszty $(1/3,-2/3,1/3)$, suma 0.

**Z26.** Dla Z25 oblicz sumę kwadratów reszt. *Rozwiązanie:* $1/9+4/9+1/9=2/3$.

**Z27.** Dla danych $y=(2,4,9)$ najlepsza stała w sensie najmniejszych kwadratów? *Rozwiązanie:* Średnia $c=5$.

**Z28.** Dla Z27 oblicz sumę kwadratów reszt. *Rozwiązanie:* $(2-5)^2+(4-5)^2+(9-5)^2=9+1+16=26$.

**Z29.** Model $y=2x+5$ przewiduje przy $x=4$ wartość 13, obserwacja to 12. Reszta? *Rozwiązanie:* $r=12-13=-1$.

**Z30.** Dla wartości prawdziwej 80 i prognozy 76 oblicz błędy. *Rozwiązanie:* Bezwzględny 4, względny $4/80=5\%$.

**Z31.** Dla wartości prawdziwej 0 i prognozy 1 oblicz błąd względny. *Rozwiązanie:* Jest niezdefiniowany; błąd bezwzględny wynosi 1.

**Z32.** Przewidywanie $y=3x+2$ skalibrowano na $x\in[0,10]$. Czy $x=15$ jest interpolacją? *Rozwiązanie:* Nie, to ekstrapolacja poza zakres kalibracji.

# F. Zadania rozwiązane — modele dyskretne i kontrola założeń

**Z33.** Populacja 1000 rośnie co okres o 5% w modelu geometrycznym. Stan po 2 okresach? *Rozwiązanie:* $1000(1{,}05)^2=1102{,}5$ jednostek modelowych; liczbę osób należy interpretować z regułą zaokrąglania.

**Z34.** Konto ma 200 zł, w każdym kroku dopisujemy 15 zł, bez odsetek. Po 8 krokach? *Rozwiązanie:* $200+8\cdot15=320$ zł.

**Z35.** Cena 100 zł wzrosła o 10%, następnie spadła o 10%. Cena końcowa? *Rozwiązanie:* $100\cdot1{,}1\cdot0{,}9=99$ zł.

**Z36.** Model $x_{n+1}=2x_n$, $x_0=3$. Oblicz $x_4$. *Rozwiązanie:* $3\cdot2^4=48$.

**Z37.** Model $x_{n+1}=x_n-4$, $x_0=25$. Oblicz $x_5$. *Rozwiązanie:* $25-20=5$.

**Z38.** Zużycie energii 2 kWh na godzinę przez 7 godzin. Wynik? *Rozwiązanie:* $2\,\mathrm{kWh/h}\cdot7\,\mathrm h=14\,\mathrm{kWh}$.

**Z39.** Ściana ma wymiary 3 m i 4 m. Potrzeba 0,2 l farby na m² na jedną warstwę. Ile na 2 warstwy? *Rozwiązanie:* $3\cdot4\cdot0{,}2\cdot2=4{,}8$ l, bez zapasu i strat.

**Z40.** Prostokąt 2 m na 5 m powiększamy w skali 3. Nowe pole? *Rozwiązanie:* $6\cdot15=90\,\mathrm{m}^2$, dziewięć razy większe niż początkowe $10\,\mathrm{m}^2$.

**Z41.** W klasie 24 osoby, 6 nieobecnych. Jaki procent obecnych? *Rozwiązanie:* $(24-6)/24=18/24=75\%$.

**Z42.** Odcinek długości 50 cm zmierzono jako 49 cm. Błąd bezwzględny i względny? *Rozwiązanie:* 1 cm i $1/50=2\%$.

**Z43.** Dla modelu $y=5x+7$ jaką jednostkę ma $5$, jeśli $y$ jest w zł, a $x$ w kg? *Rozwiązanie:* zł/kg; $7$ ma jednostkę zł.

**Z44.** Model $y=0{,}5x$ dla mas w kilogramach. Ile gramów wynosi $y$ przy $x=3$ kg? *Rozwiązanie:* $y=1{,}5$ kg = 1500 g.

**Z45.** Dwie identyczne pompy napełniają basen w 6 godzin. Przy idealnym dodawaniu wydajności trzy pompy? *Rozwiązanie:* $2\cdot6/3=4$ godziny.

**Z46.** Czas przejazdu 120 km przy 60 km/h i 80 km/h. *Rozwiązanie:* Odpowiednio 2 h i 1,5 h; oszczędność 0,5 h.

**Z47.** Oblicz średnią prędkość na dwóch odcinkach po 60 km z prędkościami 30 i 60 km/h. *Rozwiązanie:* Czasy 2 h i 1 h, więc $120/3=40$ km/h.

**Z48.** Dane $(0,1)$, $(1,2)$ pasują do $y=x+1$. Podaj inny model o tych samych wartościach. *Rozwiązanie:* $y=x+1+x(x-1)$, bo dodatkowy składnik znika dla $x=0,1$.

**Z49.** Model $K(q)=100+5q$ opisuje koszt produkcji. Czy $K(-2)=90$ zł jest sensowną prognozą? *Rozwiązanie:* Nie; dziedzina fizyczna wymaga $q\ge0$ i zwykle całkowitości.

**Z50.** Przy modelu $y=7x$ podwojenie $x$ powoduje jaką zmianę $y$? *Rozwiązanie:* $y(2x)=14x=2y(x)$.

**Z51.** Przy modelu $y=12/x$ dla $x>0$ podwojenie $x$ powoduje jaką zmianę $y$? *Rozwiązanie:* $12/(2x)=y(x)/2$.

**Z52.** Dla modelu $x_{n+1}=x_n+I_n-O_n$, $x_0=10$, dopływy $(3,2)$ i odpływy $(1,4)$ oblicz $x_2$. *Rozwiązanie:* $10+(3+2)-(1+4)=10$.

# G. Problemy przekrojowe z pełnym rozwiązaniem

**P1 (dwie taryfy).** Taryfa A kosztuje 10 zł plus 2 zł za jednostkę, taryfa B 4 zł plus 3 zł za jednostkę. Dla jakich nieujemnych całkowitych $q$ taryfa A jest nie droższa? *Rozwiązanie.* $10+2q\le4+3q$, czyli $q\ge6$. Przy $q=6$ koszty są równe 22 zł; dla $q>6$ tańsza jest A. Przy $q<6$ tańsza jest B.

**P2 (pomiar i decyzja).** Model masy produktu to $m=2x+5$ gramów, a pomiar $x$ ma zakres $[3{,}9,4{,}1]$. Czy można zagwarantować, że masa nie przekroczy 13 g? *Rozwiązanie.* Z T12 otrzymujemy $m\in[12{,}8,13{,}2]$ g. Nie można zagwarantować granicy 13 g, choć prognoza centralna wynosi 13 g.

**P3 (identyfikowalność).** Zmierzono $(x,y)=(1,2)$ i $(2,4)$. Zbuduj dwa różne modele zgodne z danymi, ale dające inne wyniki dla $x=3$. *Rozwiązanie.* Model $f(x)=2x$ daje $f(3)=6$. Model $g(x)=2x+(x-1)(x-2)$ ma $g(1)=2$, $g(2)=4$, ale $g(3)=8$. Dane nie wystarczają do wyboru modelu bez założeń lub walidacji.

**P4 (bilans i mieszanina).** Do zbiornika trafiają 2 kg roztworu 15% i 3 kg roztworu 25%; następnie odparowuje 1 kg czystej wody, bez utraty substancji. Jakie jest końcowe stężenie? *Rozwiązanie.* Początkowa masa substancji wynosi $2\cdot0{,}15+3\cdot0{,}25=1{,}05$ kg. Po odparowaniu masa całkowita to 4 kg, więc stężenie $1{,}05/4=0{,}2625=26{,}25\%$. Nie wolno stosować zwykłej średniej stężeń po odparowaniu.

**P5 (kalibracja a prognoza).** Obserwacje $(0,1)$, $(1,3)$, $(2,5)$ pasują do $y=2x+1$. Czy przewidywanie $y(100)=201$ jest logicznym następstwem samych obserwacji? *Rozwiązanie.* Nie. Jest następstwem obserwacji **oraz** dodatkowego założenia, że zależność afiniczna obowiązuje aż do $x=100$. Model alternatywny $g(x)=2x+1+x(x-1)(x-2)$ pasuje do trzech obserwacji, lecz daje inną wartość dla $x=100$.

# H. Odbiór i ograniczenia interpretacyjne

Weryfikacja modelu wymaga: (1) jednostek, (2) dziedziny fizycznej, (3) jawnych założeń, (4) identyfikacji danych kalibracyjnych, (5) osobnego sprawdzenia przewidywań, (6) analizy błędu i wrażliwości. Dobra zgodność z danymi treningowymi nie dowodzi poprawności ekstrapolacji ani związku przyczynowego. Regresja liniowa w T14–T16 jest deterministycznym zadaniem minimalizacji; bez modelu losowego nie przypisujemy współczynnikom przedziałów ufności. Opracowanie jest samodzielnym źródłem i nie jest jeszcze zintegrowane z monolitem 0.20. **Historyczny stan 585 stron bez zmian.** Dawne 1222 strony nie są wymogiem ukończenia. Końcowy PDF każdego tomu musi mieć rozmiar ściśle poniżej 99 000 000 bajtów. Nie tworzono końcowego spisu treści ani Tomu II.
