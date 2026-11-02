---
title: 'ONTOLOGIA LICZBY — TOM I'
subtitle: 'E1-02. Podzielność — liczby pierwsze, NWD, NWW i rozkład na czynniki'
author: 'Andrzej Mikulski'
date: '2 listopada 2026'
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
papersize: a4
---

**Przyporządkowanie:** E1-02, poziom I (szkoła podstawowa), minimum czterech stron według autorskiej taksonomii. Zakres: liczby pierwsze, największy wspólny dzielnik, najmniejsza wspólna wielokrotność, rozkład na czynniki. To identyfikator dydaktyczny, nie kod MSC2020. Rozdział łączy pojęcia szkolne z dowodami, bez zastępowania bardziej zaawansowanych F15.1 (ideały i wartościowania) oraz F15.2 (certyfikaty algorytmu Euklidesa).

# Część A. Teoria, dowody i kontrprzykłady

## 1. Co oznacza podzielność?

**Definicja 1 (podzielność).** Dla liczb całkowitych $a,b$ zapis $a\mid b$ oznacza, że istnieje całkowite $k$ spełniające $b=ak$. Mówimy wtedy, że $a$ jest dzielnikiem $b$, a $b$ wielokrotnością $a$. W rachunkach szkolnych badamy zwykle dodatnie dzielniki dodatnich liczb. Zachodzi $a\mid0$ dla każdego $a$, także $a=0$, ale $0\nmid b$ dla $b\ne0$.

**Definicja 2 (dzielenie z resztą).** Dla $n\ge0$ i $d>0$ istnieją jednoznaczne $q,r\ge0$ takie, że $n=dq+r$ oraz $0\le r<d$. Liczba $d$ dzieli $n$ dokładnie wtedy, gdy $r=0$. Istnienie i jednoznaczność zostały uzasadnione w E0-03; tutaj wykorzystujemy je jako narzędzie.

**Twierdzenie 1 (suma i różnica wielokrotności).** Jeżeli $d\mid a$ i $d\mid b$, to $d\mid(a+b)$ i $d\mid(a-b)$.

*Dowód.* Zapiszmy $a=du$, $b=dv$. Wówczas $a+b=d(u+v)$ i $a-b=d(u-v)$, przy czym $u+v,u-v$ są całkowite. $\square$

**Twierdzenie 2 (przechodniość).** Jeśli $a\mid b$ i $b\mid c$, to $a\mid c$.

*Dowód.* Równości $b=ak$ i $c=bl$ dają $c=a(kl)$. $\square$

**Twierdzenie 3 (ograniczenie dodatniego dzielnika).** Dla $n>0$ każdy dodatni dzielnik $d$ liczby $n$ spełnia $1\le d\le n$.

*Dowód.* Ponieważ $n=dk>0$ przy $d>0$, współczynnik $k$ jest dodatnią liczbą całkowitą, więc $k\ge1$ i $n=dk\ge d$. $\square$

**Kontrprzykład 1.** Z $4\mid12$ i $6\mid12$ nie wynika $24\mid12$. Iloczyn dzielników nie musi dzielić liczby, gdy dzielniki mają wspólny czynnik.

**Kontrprzykład 2.** Z $6\mid(2\cdot3)$ nie wynika $6\mid2$ ani $6\mid3$. Reguła „dzieli iloczyn, więc dzieli czynnik” jest fałszywa bez dodatkowych założeń.

## 2. Dzielniki i wielokrotności w praktyce

**Definicja 3 (dzielnik właściwy).** Dodatni dzielnik właściwy dodatniej liczby $n$ jest mniejszy od $n$. Liczba $1$ ma jeden dodatni dzielnik i nie ma dodatnich dzielników właściwych.

**Twierdzenie 4 (pary dzielników).** Jeżeli $d\mid n$ dla $n>0$, to również $n/d$ jest dodatnim dzielnikiem $n$; w każdej parze $d,n/d$ przynajmniej jeden element nie przekracza $\sqrt n$.

*Dowód.* Z $n=dk$ otrzymujemy $k=n/d\in\mathbb N$. Gdyby zarówno $d>\sqrt n$, jak i $k>\sqrt n$, to $dk>n$, sprzeczność. $\square$

**Przykład.** Dzielniki 36 można odnaleźć przez pary $(1,36)$, $(2,18)$, $(3,12)$, $(4,9)$, $(6,6)$. Otrzymujemy dziewięć różnych dodatnich dzielników: $1,2,3,4,6,9,12,18,36$.

**Definicja 4 (wspólny dzielnik).** Liczba dodatnia $d$ jest wspólnym dzielnikiem $a,b>0$, jeśli $d\mid a$ i $d\mid b$.

**Definicja 5 (NWD).** Największy wspólny dzielnik $a,b>0$ oznaczamy $\operatorname{NWD}(a,b)$ lub $\gcd(a,b)$. Jest to największa liczba dodatnia dzieląca oba argumenty. W szerszym rachunku przyjmuje się $\gcd(a,0)=|a|$ i $\gcd(0,0)=0$; zadania szkolne poniżej korzystają z dodatnich argumentów.

**Definicja 6 (NWW).** Najmniejsza wspólna wielokrotność $a,b>0$ to najmniejsza dodatnia liczba podzielna przez $a$ i przez $b$, oznaczana $\operatorname{NWW}(a,b)$ lub $\operatorname{lcm}(a,b)$.

**Przykład.** Wspólne dzielniki 18 i 24 to 1, 2, 3, 6, zatem $\gcd(18,24)=6$. Wspólne wielokrotności zaczynają się od 72, 144, 216, więc $\operatorname{lcm}(18,24)=72$.

**Twierdzenie 5 (wspólne dzielniki przy odejmowaniu).** Dla $a>b>0$ zbiór wspólnych dodatnich dzielników pary $(a,b)$ jest identyczny ze zbiorem wspólnych dodatnich dzielników $(a-b,b)$.

*Dowód.* Jeśli $d\mid a,b$, to z Twierdzenia 1 $d\mid a-b$. Odwrotnie, jeśli $d\mid a-b,b$, to $d\mid(a-b)+b=a$. Oba kierunki dają równość zbiorów. $\square$

**Twierdzenie 6 (krok Euklidesa).** Jeśli $a=bq+r$ oraz $0\le r<b$, to $\gcd(a,b)=\gcd(b,r)$, przy konwencji $\gcd(b,0)=b$ dla $b>0$.

*Dowód.* Wspólny dzielnik $a,b$ dzieli $r=a-bq$. Wspólny dzielnik $b,r$ dzieli $a=bq+r$. Zatem zbiory wspólnych dodatnich dzielników są równe. $\square$

**Twierdzenie 7 (zakończenie algorytmu Euklidesa).** Powtarzanie kroku $a=bq+r$ dla dodatnich argumentów kończy się po skończonej liczbie kroków; ostatnia niezerowa reszta jest NWD.

*Dowód.* Każda nowa dodatnia reszta jest ściśle mniejsza od poprzedniego dodatniego dzielnika. Nie istnieje nieskończony ściśle malejący ciąg dodatnich liczb całkowitych. NWD pozostaje niezmieniony w każdym kroku na mocy Twierdzenia 6, a ostatnia para ma postać $(g,0)$ i NWD równy $g$. $\square$

**Przykład z kontrolą.** $252=198+54$, $198=3\cdot54+36$, $54=36+18$, $36=2\cdot18+0$, więc $\gcd(252,198)=18$. Kontrola: $252/18=14$, $198/18=11$.

**Kontrprzykład 3.** Z $a>b$ nie wynika $\gcd(a,b)=a-b$: dla 15 i 10 różnica to 5 i NWD także 5, lecz dla 16 i 10 różnica to 6, a NWD to 2.

## 3. Liczby pierwsze i złożone

**Definicja 7 (liczba pierwsza).** Liczba naturalna $p>1$ jest pierwsza, jeśli jej jedynymi dodatnimi dzielnikami są $1$ i $p$.

**Definicja 8 (liczba złożona).** Liczba naturalna $n>1$ jest złożona, jeśli ma dodatni dzielnik $d$ spełniający $1<d<n$.

**Twierdzenie 8 (mały dzielnik liczby złożonej).** Jeśli $n>1$ jest złożona, to istnieje liczba pierwsza $p\mid n$ spełniająca $p\le\sqrt n$.

*Dowód.* Złożoność daje $n=ab$ z $1<a,b<n$. Co najmniej jeden czynnik, powiedzmy $a$, nie przekracza $\sqrt n$ na mocy Twierdzenia 4. Każda liczba całkowita $a>1$ ma dzielnik pierwszy: wybierzmy najmniejszy jej dzielnik większy od 1; gdyby był złożony, miałby mniejszy dzielnik większy od 1. Otrzymane $p$ dzieli $a$ i $n$, a $p\le a\le\sqrt n$. $\square$

**Przykład.** Aby sprawdzić, czy 97 jest pierwsza, wystarczy sprawdzić podzielność przez liczby pierwsze nie większe niż $\sqrt{97}<10$, czyli 2, 3, 5, 7. Żadna nie dzieli 97; zatem 97 jest pierwsza.

**Twierdzenie 9 (nieskończenie wiele liczb pierwszych).** Nie istnieje największa liczba pierwsza.

*Dowód.* Załóżmy, że wszystkie liczby pierwsze to $p_1,\ldots,p_k$. Liczba $N=p_1\cdots p_k+1>1$ ma pewien dzielnik pierwszy $q$. Gdyby $q=p_i$, to dzieliłaby zarówno $N$, jak i iloczyn $p_1\cdots p_k$, więc dzieliłaby ich różnicę 1 — niemożliwe. Zatem $q$ nie występuje na liście, sprzeczność. $\square$

**Kontrprzykład 4.** Liczba 1 nie jest pierwsza ani złożona: ma tylko jeden dodatni dzielnik. Liczba 0 również nie jest pierwsza, choć dzieli się przez każdą dodatnią liczbę.

**Kontrprzykład 5.** Wszystkie liczby nieparzyste większe od 1 nie są pierwsze: $9=3\cdot3$, $15=3\cdot5$, $21=3\cdot7$.

**Definicja 9 (sito Eratostenesa).** Aby znaleźć liczby pierwsze nie większe od $N$, wypisujemy liczby od 2 do $N$ i kolejno wykreślamy wielokrotności niewykreślonych liczb $p$, zaczynając od $p^2$, dopóki $p^2\le N$.

**Twierdzenie 10 (poprawność sita).** Po zakończeniu sita pozostają dokładnie liczby pierwsze nie większe od $N$.

*Dowód.* Liczba pierwsza nie jest wielokrotnością mniejszej liczby $p>1$, więc nie zostaje wykreślona. Jeśli liczba $n\le N$ jest złożona, to według Twierdzenia 8 ma dzielnik pierwszy $p\le\sqrt n\le\sqrt N$ i zostanie wykreślona jako wielokrotność $p$ nie mniejsza od $p^2$ (mniejsze wielokrotności miały już mniejszy czynnik). $\square$

## 4. Rozkład na czynniki pierwsze

**Definicja 10 (rozkład pierwszy).** Rozkład dodatniej liczby $n>1$ to zapis $n=p_1\cdots p_k$ z liczbami pierwszymi $p_i$. Równe czynniki można grupować w potęgi, np. $360=2^3\cdot3^2\cdot5$.

**Twierdzenie 11 (istnienie rozkładu).** Każde $n>1$ jest iloczynem liczb pierwszych.

*Dowód.* Stosujemy silną indukcję po $n$. Jeśli $n$ jest pierwsza, stanowi jednoelementowy iloczyn. Jeśli jest złożona, $n=ab$ z $1<a,b<n$. Na mocy założenia indukcyjnego $a$ i $b$ mają rozkłady pierwsze; ich połączenie jest rozkładem $n$. $\square$

**Twierdzenie 12 (tożsamość Bézouta).** Dla dodatnich $a,b$ istnieją całkowite $u,v$ takie, że $au+bv=\gcd(a,b)$.

*Dowód.* Każdy krok algorytmu Euklidesa wyraża resztę jako różnicę dwóch całkowitych wielokrotności poprzednich liczb. Indukcyjnie każda reszta jest więc kombinacją całkowitą $a,b$. Ostatnia niezerowa reszta jest NWD na mocy Twierdzenia 7, stąd odpowiednia kombinacja. $\square$

**Twierdzenie 13 (lemat Euklidesa).** Jeśli liczba pierwsza $p$ dzieli $ab$, to dzieli $a$ lub $b$.

*Dowód.* Jeśli $p\nmid a$, to wspólny dodatni dzielnik $p$ i $a$ może wynosić tylko 1, więc $\gcd(p,a)=1$. Twierdzenie 12 daje $up+va=1$. Mnożąc przez $b$, otrzymujemy $upb+vab=b$. Oba składniki lewej strony dzielą się przez $p$, a zatem $p\mid b$. $\square$

**Twierdzenie 14 (jednoznaczność rozkładu).** Dwa rozkłady tej samej liczby $n>1$ na czynniki pierwsze mają te same czynniki z uwzględnieniem krotności, z dokładnością do kolejności.

*Dowód.* Niech $n=p_1\cdots p_k=q_1\cdots q_l$. Lemat Euklidesa zastosowany kolejno do czynników prawej strony pokazuje, że $p_1$ dzieli pewien $q_j$. Ponieważ obie liczby są pierwsze, $p_1=q_j$. Skracamy równy czynnik i powtarzamy argument dla krótszych rozkładów. Po skończonej liczbie kroków nie pozostaje żaden czynnik po żadnej stronie. $\square$

**Kontrprzykład 6.** Rozkład $12=2\cdot2\cdot3$ jest pierwszy, ale $12=2\cdot6$ nie jest rozkładem na same czynniki pierwsze, ponieważ 6 jest złożona.

## 5. NWD i NWW z rozkładu

**Definicja 11 (wykładnik czynnika).** W rozkładzie $n=\prod_p p^{e_p(n)}$ wykładnik $e_p(n)$ jest liczbą wystąpień pierwszej $p$; poza skończonym zbiorem pierwszych wykładnik wynosi zero.

**Twierdzenie 15 (kryterium podzielności).** Dla $a,b>0$ zachodzi $a\mid b$ wtedy i tylko wtedy, gdy $e_p(a)\le e_p(b)$ dla każdej liczby pierwszej $p$.

*Dowód.* Jeśli $b=ak$, rozkłady pierwsze dają $e_p(b)=e_p(a)+e_p(k)$. Odwrotnie, przy nierównościach różnice wykładników są nieujemne i ich iloczyn $\prod_p p^{e_p(b)-e_p(a)}$ jest liczbą całkowitą $k$ z $b=ak$. $\square$

**Twierdzenie 16 (minimum i maksimum wykładników).** Dla $a,b>0$:
\[
\gcd(a,b)=\prod_p p^{\min(e_p(a),e_p(b))},\qquad
\operatorname{lcm}(a,b)=\prod_p p^{\max(e_p(a),e_p(b))}.
\]

*Dowód.* Na mocy Twierdzenia 15 wspólny dzielnik ma dla każdej $p$ wykładnik nie większy od obu wykładników; największy dopuszczalny to ich minimum. Wspólna wielokrotność musi mieć wykładnik nie mniejszy od obu; najmniejszy dopuszczalny to maksimum. $\square$

**Twierdzenie 17 (iloczyn NWD i NWW).** Dla $a,b>0$:
\[
\gcd(a,b)\operatorname{lcm}(a,b)=ab.
\]

*Dowód.* Dla dowolnych liczb całkowitych nieujemnych $x,y$ zachodzi $\min(x,y)+\max(x,y)=x+y$. Po zastosowaniu Twierdzenia 16 do każdego wykładnika pierwszego oba iloczyny mają identyczne rozkłady pierwsze, więc są równe. $\square$

**Przykład.** $72=2^3\cdot3^2$, $90=2\cdot3^2\cdot5$. Stąd $\gcd(72,90)=2\cdot3^2=18$, a $\operatorname{lcm}(72,90)=2^3\cdot3^2\cdot5=360$. Kontrola: $18\cdot360=72\cdot90=6480$.

**Kontrprzykład 7.** Nie wolno liczyć NWW jako iloczynu liczb, gdy mają wspólny dzielnik: $\operatorname{lcm}(6,8)=24$, a nie 48.

**Definicja 12 (względna pierwszość).** Dwie dodatnie liczby są względnie pierwsze, jeśli ich NWD wynosi 1. Nie wymaga to, aby każda z nich była pierwsza.

**Twierdzenie 18 (kolejne liczby).** Dla $n\ge1$ liczby $n$ i $n+1$ są względnie pierwsze.

*Dowód.* Każdy wspólny dzielnik dzieli ich różnicę $(n+1)-n=1$, więc wynosi 1. $\square$

**Kontrprzykład 8.** Liczby 8 i 9 są względnie pierwsze, choć obie są złożone.

## 6. Kryteria podzielności jako twierdzenia

**Definicja 13 (zapis dziesiętny).** Dla cyfr $c_i\in\{0,\ldots,9\}$ liczba ma postać $n=\sum_{i=0}^m c_i10^i$. Wnioski o sumie cyfr wynikają z tej równości, a nie z samego wzoru cyfr.

**Twierdzenie 19 (kryteria 3 i 9).** Liczba dziesiętna jest podzielna przez 3 (odpowiednio 9) wtedy i tylko wtedy, gdy suma jej cyfr jest podzielna przez 3 (odpowiednio 9).

*Dowód.* Ponieważ $10-1=9$, dla $d\in\{3,9\}$ zachodzi $10\equiv1\pmod d$, a zatem $10^i\equiv1\pmod d$. Wobec tego $n\equiv\sum_i c_i\pmod d$. $\square$

**Twierdzenie 20 (kryterium 11).** Liczba jest podzielna przez 11 wtedy i tylko wtedy, gdy naprzemienna suma jej cyfr, liczona od jedności, jest podzielna przez 11.

*Dowód.* Ponieważ $10\equiv-1\pmod{11}$, mamy $10^i\equiv(-1)^i\pmod{11}$. Stąd $n\equiv c_0-c_1+c_2-\cdots\pmod{11}$. $\square$

**Twierdzenie 21 (kryteria 2, 5, 10).** O podzielności przez 2, 5 i 10 decyduje ostatnia cyfra: odpowiednio parzystość; cyfra 0 lub 5; cyfra 0.

*Dowód.* Zapis $n=10q+c_0$ pokazuje, że $n$ i $c_0$ mają tę samą resztę modulo każdy dzielnik 10. $\square$

**Kontrprzykład 9.** Liczba 111 jest podzielna przez 3, bo suma cyfr to 3, lecz nie przez 9. Nie wolno utożsamiać obu kryteriów.

**Przykład.** Dla 12342 suma cyfr to 12, więc liczba jest podzielna przez 3, ale nie przez 9. Naprzemienna suma $2-4+3-2+1=0$ pokazuje podzielność przez 11.

## 7. Rozumowanie o warunkach i zastosowania

**Twierdzenie 22 (względnie pierwsze czynniki).** Jeśli $\gcd(a,b)=1$ i $a\mid bc$, to $a\mid c$.

*Dowód.* Z Twierdzenia 12 istnieją $u,v\in\mathbb Z$ z $au+bv=1$. Po pomnożeniu przez $c$ mamy $auc+bvc=c$. Pierwszy składnik jest podzielny przez $a$, drugi także, bo $a\mid bc$. Zatem $a\mid c$. $\square$

**Twierdzenie 23 (wspólna wielokrotność względnie pierwszych).** Jeśli $\gcd(a,b)=1$ i $a\mid n$, $b\mid n$, to $ab\mid n$.

*Dowód.* Z $a\mid n$ mamy $n=ak$. Skoro $b\mid ak$ i $\gcd(a,b)=1$, z Twierdzenia 22 wynika $b\mid k$, czyli $k=bl$. Wtedy $n=abl$. $\square$

**Przykład modelowy.** Dwa sygnały powtarzają się co 12 i 18 minut. Wspólny moment ponownego wystąpienia po chwili startu nastąpi po $\operatorname{lcm}(12,18)=36$ minutach. NWD opisuje wielkość największej jednakowej porcji, a NWW najwcześniejszą wspólną powtarzalność; zamiana tych ról prowadzi do błędnego modelu.

**Ograniczenie dydaktyczne.** Rozdział przedstawia szkolne zastosowania podzielności. Zagadnienia ideałów, wartościowań $p$-adycznych, certyfikatów algorytmu i chińskiego twierdzenia o resztach zostały już rozwinięte w F15.1–F15.3; nie są ponownie wprowadzane jako nowe wyniki E1-02. Dowody nie są formalnie zmechanizowane.

\newpage

# Część B. Ćwiczenia i problemy z rozwiązaniami

Poniższe zadania są samodzielne. W każdym wskazano wynik i podstawę rachunku; przy zadaniach dowodowych podano pełny argument, a przy zadaniach z danymi — kontrolę warunków.

**Zadanie 1.** Wypisz dodatnie dzielniki 24.

*Rozwiązanie.* Są to 1, 2, 3, 4, 6, 8, 12, 24; pary iloczynów to (1,24), (2,12), (3,8), (4,6).

**Zadanie 2.** Wypisz dodatnie dzielniki 45.

*Rozwiązanie.* Są to 1, 3, 5, 9, 15, 45, ponieważ 45=3²·5.

**Zadanie 3.** Czy 7 dzieli 203?

*Rozwiązanie.* Tak: 203=7·29, reszta wynosi 0.

**Zadanie 4.** Czy 8 dzieli 150?

*Rozwiązanie.* Nie: 150=8·18+6, więc reszta wynosi 6.

**Zadanie 5.** Oblicz resztę z dzielenia 157 przez 12.

*Rozwiązanie.* 157=12·13+1, więc reszta to 1.

**Zadanie 6.** Podaj pięć dodatnich wielokrotności 9.

*Rozwiązanie.* 9, 18, 27, 36, 45.

**Zadanie 7.** Czy 1 jest liczbą pierwszą?

*Rozwiązanie.* Nie; liczba pierwsza ma dokładnie dwa różne dodatnie dzielniki, a 1 ma jeden.

**Zadanie 8.** Czy 2 jest liczbą pierwszą?

*Rozwiązanie.* Tak; jej jedyne dodatnie dzielniki to 1 i 2.

**Zadanie 9.** Czy 91 jest liczbą pierwszą?

*Rozwiązanie.* Nie, bo 91=7·13.

**Zadanie 10.** Sprawdź pierwszość 97.

*Rozwiązanie.* Wystarczy sprawdzić 2, 3, 5 i 7, gdyż √97<10. Żadna z tych liczb nie dzieli 97; liczba jest pierwsza.

**Zadanie 11.** Rozłóż 84 na czynniki pierwsze.

*Rozwiązanie.* 84=2·42=2²·21=2²·3·7.

**Zadanie 12.** Rozłóż 180 na czynniki pierwsze.

*Rozwiązanie.* 180=18·10=2²·3²·5.

**Zadanie 13.** Rozłóż 315 na czynniki pierwsze.

*Rozwiązanie.* 315=3·105=3²·35=3²·5·7.

**Zadanie 14.** Oblicz NWD(18,24) przez wypisanie dzielników.

*Rozwiązanie.* Wspólne dodatnie dzielniki to 1,2,3,6, więc NWD=6.

**Zadanie 15.** Oblicz NWW(18,24) z rozkładów.

*Rozwiązanie.* 18=2·3², 24=2³·3; maksymalne wykładniki dają 2³·3²=72.

**Zadanie 16.** Oblicz NWD(48,60) algorytmem Euklidesa.

*Rozwiązanie.* 60=48+12, 48=4·12; ostatnia dodatnia reszta to 12.

**Zadanie 17.** Oblicz NWD(252,198).

*Rozwiązanie.* 252=198+54, 198=3·54+36, 54=36+18, 36=2·18; NWD=18.

**Zadanie 18.** Oblicz NWD(1071,462).

*Rozwiązanie.* 1071=2·462+147, 462=3·147+21, 147=7·21; NWD=21.

**Zadanie 19.** Oblicz NWW(12,18).

*Rozwiązanie.* NWD(12,18)=6, więc NWW=12·18/6=36.

**Zadanie 20.** Oblicz NWW(14,25).

*Rozwiązanie.* NWD=1, więc NWW=14·25=350.

**Zadanie 21.** Sprawdź równość NWD·NWW=ab dla 72 i 90.

*Rozwiązanie.* NWD=18, NWW=360; 18·360=6480=72·90.

**Zadanie 22.** Czy 8 i 9 są względnie pierwsze?

*Rozwiązanie.* Tak, ponieważ ich jedyny wspólny dodatni dzielnik to 1.

**Zadanie 23.** Czy 12 i 18 są względnie pierwsze?

*Rozwiązanie.* Nie, ponieważ NWD(12,18)=6.

**Zadanie 24.** Uzasadnij, że 31 i 32 są względnie pierwsze.

*Rozwiązanie.* Każdy wspólny dzielnik dzieli różnicę 32−31=1, więc NWD=1.

**Zadanie 25.** Podaj resztę z dzielenia 12345 przez 9.

*Rozwiązanie.* Suma cyfr to 1+2+3+4+5=15; reszta z 15 przez 9 wynosi 6.

**Zadanie 26.** Czy 123456 jest podzielne przez 3 i przez 9?

*Rozwiązanie.* Suma cyfr to 21: przez 3 tak, przez 9 nie.

**Zadanie 27.** Czy 12342 jest podzielne przez 11?

*Rozwiązanie.* Naprzemienna suma 2−4+3−2+1=0, więc tak.

**Zadanie 28.** Czy 1254 jest podzielne przez 11?

*Rozwiązanie.* 4−5+2−1=0, więc tak; kontrola 1254=11·114.

**Zadanie 29.** Czy 1255 jest podzielne przez 5 i 10?

*Rozwiązanie.* Przez 5 tak, bo kończy się cyfrą 5; przez 10 nie.

**Zadanie 30.** Wypisz liczby pierwsze nie większe od 30.

*Rozwiązanie.* 2,3,5,7,11,13,17,19,23,29.

**Zadanie 31.** Dlaczego sito może zacząć skreślanie wielokrotności p od p²?

*Rozwiązanie.* Każda mniejsza wielokrotność p ma postać p·k z 2≤k<p i była już skreślona jako wielokrotność mniejszego czynnika k (lub jego dzielnika pierwszego).

**Zadanie 32.** Znajdź NWD(36,60,84).

*Rozwiązanie.* NWD(36,60)=12, następnie NWD(12,84)=12.

**Zadanie 33.** Znajdź NWW(4,6,9).

*Rozwiązanie.* Rozkłady: 4=2², 6=2·3, 9=3²; NWW=2²·3²=36.

**Zadanie 34.** Dwie lampy migają co 8 i 12 sekund. Kiedy ponownie migną jednocześnie?

*Rozwiązanie.* Po NWW(8,12)=24 sekundach od wspólnego startu.

**Zadanie 35.** Wstążki długości 84 i 126 cm chcemy pociąć na najdłuższe równe kawałki bez reszty. Jaka długość?

*Rozwiązanie.* NWD(84,126)=42 cm; otrzymamy odpowiednio 2 i 3 kawałki.

**Zadanie 36.** Ile prostokątnych paczek po 6 kart można przygotować ze 100 kart i ile zostanie?

*Rozwiązanie.* 100=6·16+4, więc 16 pełnych paczek i 4 karty.

**Zadanie 37.** Czy 2·3·5·7+1 jest podzielne przez którąkolwiek z liczb 2,3,5,7?

*Rozwiązanie.* Nie; przy dzieleniu przez każdą z nich iloczyn ma resztę 0, więc liczba powiększona o 1 ma resztę 1.

**Zadanie 38.** Czy każda liczba postaci 2ⁿ+1 jest pierwsza?

*Rozwiązanie.* Nie; dla n=3 mamy 2³+1=9=3².

**Zadanie 39.** Uzasadnij, że liczba 6k+3 jest podzielna przez 3.

*Rozwiązanie.* 6k+3=3(2k+1), więc 3 jest dzielnikiem dla każdego całkowitego k.

**Zadanie 40.** Uzasadnij, że jeżeli 4 dzieli a i b, to 4 dzieli a−b.

*Rozwiązanie.* Zapisz a=4u i b=4v; wtedy a−b=4(u−v).

**Zadanie 41.** Podaj kontrprzykład do zdania: jeśli a dzieli bc, to a dzieli b.

*Rozwiązanie.* Weź a=6, b=2, c=3. Zachodzi 6|6, lecz 6 nie dzieli 2.

**Zadanie 42.** Jeśli NWD(a,b)=1, a|bc, pokaż, że a|c.

*Rozwiązanie.* Z Bézouta istnieją u,v z au+bv=1. Po pomnożeniu przez c obie części auc i bvc są wielokrotnościami a, zatem a|c.

**Zadanie 43.** Wykaż, że NWW(15,20)=60.

*Rozwiązanie.* 15=3·5, 20=2²·5; bierzemy maksymalne wykładniki: 2²·3·5=60.

**Zadanie 44.** Rozłóż 1001 na czynniki pierwsze.

*Rozwiązanie.* 1001=7·143=7·11·13.

**Zadanie 45.** Oblicz liczbę dodatnich dzielników 72.

*Rozwiązanie.* 72=2³·3²; wykładnik czynnika 2 wybieramy na 4 sposoby, a 3 na 3 sposoby, więc 4·3=12.

**Zadanie 46.** Znajdź najmniejszą liczbę dodatnią podzielną przez 6, 8 i 15.

*Rozwiązanie.* NWW(6,8,15)=2³·3·5=120.

**Zadanie 47.** Wykaż, że jeśli p>3 jest pierwsza, to nie dzieli się przez 2 ani 3.

*Rozwiązanie.* Gdyby dzieliła się przez 2 lub 3, miałaby dzielnik właściwy większy od 1, co przeczy pierwszości.

**Zadanie 48.** Dwie grupy mają 48 i 72 osoby. Na ile największych równych zespołów można podzielić każdą grupę, aby liczba osób w zespole była taka sama?

*Rozwiązanie.* Największy rozmiar zespołu to NWD(48,72)=24; powstaną odpowiednio 2 i 3 zespoły.

**Zadanie 49.** Czy liczba 1001 jest podzielna przez 11?

*Rozwiązanie.* Tak: naprzemienna suma 1−0+0−1=0; także 1001=11·91.

**Zadanie 50.** Uzasadnij, że dla a,b>0 NWD(a,b)≤min(a,b).

*Rozwiązanie.* NWD jest dodatnim dzielnikiem obu liczb, a dodatni dzielnik dodatniej liczby nie może jej przekraczać.

**Zadanie 51.** Czy NWW(8,12) może wynosić 12?

*Rozwiązanie.* Nie, bo 12 nie jest podzielne przez 8. Najmniejsza wspólna wielokrotność to 24.

**Zadanie 52.** Oblicz NWD(100,75) i NWW(100,75).

*Rozwiązanie.* NWD=25; NWW=100·75/25=300.

**Zadanie 53.** Wskaż błąd w rozumowaniu: 1 jest pierwsza, więc rozkład 12=1·2²·3 jest niejednoznaczny.

*Rozwiązanie.* Jedynka nie jest pierwsza. Rozkład pierwszy dopuszcza wyłącznie czynniki większe od 1 mające dokładnie dwa dodatnie dzielniki.

**Zadanie 54.** Uzasadnij, że liczba 221 jest złożona.

*Rozwiązanie.* 221=13·17, oba czynniki są większe od 1 i mniejsze od 221.

**Zadanie 55.** Znajdź NWD(143,1001).

*Rozwiązanie.* 1001=7·143, więc NWD=143.

**Zadanie 56.** Oblicz NWW(21,28).

*Rozwiązanie.* 21=3·7, 28=2²·7, zatem NWW=2²·3·7=84.


## Problemy syntetyczne

**Problem A (pełny certyfikat NWD).** Wyznacz $\gcd(414,662)$ i przedstaw go jako kombinację całkowitą tych liczb.

*Rozwiązanie.* $662=414+248$, $414=248+166$, $248=166+82$, $166=2\cdot82+2$, $82=41\cdot2$. Zatem NWD wynosi 2. Cofamy podstawienia: $2=166-2\cdot82=166-2(248-166)=3\cdot166-2\cdot248=3(414-248)-2\cdot248=3\cdot414-5\cdot248=3\cdot414-5(662-414)=8\cdot414-5\cdot662$. Kontrola: $3312-3310=2$.

**Problem B (wspólny cykl).** Trzy automaty rozpoczynają pracę razem i powtarzają czynność co 18, 24 i 30 minut. Po ilu minutach po raz pierwszy znów wykonają ją równocześnie?

*Rozwiązanie.* $18=2\cdot3^2$, $24=2^3\cdot3$, $30=2\cdot3\cdot5$. NWW to $2^3\cdot3^2\cdot5=360$ minut, czyli 6 godzin. Sprawdzenie: 360 dzieli się przez 18, 24 i 30; mniejsza dodatnia liczba nie może zawierać wszystkich wymaganych maksymalnych wykładników.

**Problem C (minimalna liczba paczek).** Dwie partie liczą 96 i 144 przedmioty. Chcemy przygotować identyczne, możliwie duże paczki, nie mieszając partii i bez reszty. Ile przedmiotów w paczce i ile paczek powstanie?

*Rozwiązanie.* $96=2^5\cdot3$, $144=2^4\cdot3^2$. NWD to $2^4\cdot3=48$. Pierwsza partia daje 2 paczki, druga 3, razem 5. Gdyby paczka miała więcej niż 48 przedmiotów, jej wielkość nie byłaby wspólnym dzielnikiem obu partii.

**Problem D (odrzucenie fałszywej reguły).** Czy z $a\mid bc$ i $a\mid bd$ wynika $a\mid b(c+d)$? Czy wynika $a\mid(c+d)$?

*Rozwiązanie.* Pierwszy wniosek jest prawdziwy, bo $a\mid bc+bd=b(c+d)$ na mocy Twierdzenia 1. Drugi jest fałszywy: dla $a=6$, $b=6$, $c=d=1$ oba założenia są prawdziwe, ale $6\nmid2$. Dodatkowe założenie $\gcd(a,b)=1$ pozwoliłoby skrócić czynnik $b$.

**Problem E (dowód z rozkładu).** Dla $a=2^4\cdot3^2$ i $b=2^2\cdot3^3\cdot5$ oblicz NWD i NWW oraz sprawdź tożsamość iloczynową.

*Rozwiązanie.* NWD to $2^2\cdot3^2=36$, NWW to $2^4\cdot3^3\cdot5=2160$. Iloczyn $36\cdot2160=77760$. Jednocześnie $a=144$, $b=540$, więc $ab=77760$.

**Problem F (czy liczba jest pierwsza?).** Rozstrzygnij, czy 149 jest liczbą pierwszą, nie sprawdzając wszystkich mniejszych liczb.

*Rozwiązanie.* Ponieważ $12^2<149<13^2$, wystarczy sprawdzić pierwsze $2,3,5,7,11$. Liczba 149 jest nieparzysta, suma cyfr to 14, nie kończy się na 0 ani 5, $149=7\cdot21+2$ oraz $149=11\cdot13+6$. Żadna z wymienionych pierwszych jej nie dzieli. Z Twierdzenia 8 wynika, że 149 jest pierwsza.

**Problem G (szukanie liczby).** Znajdź najmniejszą dodatnią liczbę $n$ podzielną przez 12 i 20, której reszta z dzielenia przez 7 wynosi 4.

*Rozwiązanie.* $n$ musi być wielokrotnością NWW$(12,20)=60$, więc $n=60k$ z $k\ge1$. Ponieważ $60\equiv4\pmod7$, warunek brzmi $4k\equiv4\pmod7$, czyli $k\equiv1\pmod7$. Najmniejsze dodatnie $k$ to 1, stąd $n=60$; kontrola $60=7\cdot8+4$.

**Problem H (model i ograniczenia).** Wyjaśnij różnicę między dzieleniem 47 przedmiotów na 6 równych grup a pakowaniem 47 przedmiotów do pudełek mieszczących najwyżej 6 sztuk.

*Rozwiązanie.* Dzielenie z resztą daje $47=6\cdot7+5$. Przy siedmiu pełnych grupach pozostaje pięć przedmiotów, więc nie da się utworzyć sześciu grup o jednakowej całkowitej liczebności obejmujących wszystkie 47. Przy pakowaniu po maksymalnie sześć sztuk potrzeba ośmiu pudełek: siedem pełnych i jedno z pięcioma. Iloraz 7 nie jest liczbą wszystkich potrzebnych pudełek.

## Kontrola źródeł i status wydawniczy

Zachowano i nie nadpisano wcześniejszych opracowań F15.1–F15.3. E1-02 jest samodzielną warstwą dydaktyczną: pojęcia, dowody, przykłady i zadania od podstaw, bez deklarowania nowych odkryć w teorii liczb. Nie doliczać stron do bilansu **585/1222** przed rzeczywistą integracją z monolitem 0.20 i kontrolą całego składu. Nie ingerowano w historyczny wstęp.
