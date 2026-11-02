---
title: 'ONTOLOGIA LICZBY — TOM I'
subtitle: 'E1-01. Ułamki i liczby wymierne — części, proporcje, procenty'
author: 'Andrzej Mikulski'
date: '2 listopada 2026'
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
papersize: a4
---

**Przyporządkowanie:** E1-01, poziom I, minimum czterech stron opracowania według taksonomii autora. Treści: ułamki, liczby dziesiętne, stosunki, proporcje i procenty. Jest to kod dydaktyczny, nie kod MSC2020. Wcześniejsze materiały F14.3 (konstrukcja ciała wymiernych), F10.1 (zapis pozycyjny) i F19.1 (rozwinięcia dziesiętne) zachowują odrębny status; nie są tu przepisywane. Przyjmujemy $\mathbb Q$ jako zbiór liczb wymiernych, a mianownik zawsze różny od zera.

# Część A. Teoria, twierdzenia, dowody i granice modelu

## 1. Od części całości do liczby

**Definicja 1 (ułamek).** Dla $a\in\mathbb Z$ i $b\in\mathbb N$, $b>0$, zapis $a/b$ oznacza liczbę, otrzymaną jako $a$ kopii części o wielkości $1/b$ jednostki (z uwzględnieniem znaku licznika). W szkole podstawowej najpierw rozpatrujemy $0\le a\le b$, a potem ułamki niewłaściwe i ujemne.

**Definicja 2 (równość ułamków).** $a/b=c/d$ wtedy i tylko wtedy, gdy $ad=bc$ przy $b,d>0$. W szczególności $a/b=(ka)/(kb)$ dla dodatniego całkowitego $k$.

**Twierdzenie 1 (rozszerzanie).** Dla $b,k>0$ zachodzi $a/b=ka/kb$.

*Dowód.* Iloczyny krzyżowe są równe: $a(kb)=(ka)b$. Oba mianowniki są dodatnie. $\square$

**Twierdzenie 2 (skracanie).** Jeśli dodatnia liczba całkowita $k$ dzieli $a$ i $b$, to $a/b=(a/k)/(b/k)$.

*Dowód.* Oznaczmy $a=ku$, $b=kv$. Z twierdzenia 1 mamy $u/v=ku/kv=a/b$. $\square$

**Przykład 1.** $6/8=3/4$, ponieważ dzielimy licznik i mianownik przez 2. Nie odejmujemy 2 od obu liczb.

**Kontrprzykład 1.** $6/8\ne4/6$: odejmowanie tej samej liczby od licznika i mianownika nie zachowuje ułamka, bo $6\cdot6=36\ne32=8\cdot4$.

**Definicja 3 (liczba mieszana).** Dla $a\ge0$ i $b>0$ dzielenie $a=bq+r$ z $0\le r<b$ daje $a/b=q+r/b$. Zapis $q\;r/b$ jest skrótem sumy, a nie iloczynu.

**Twierdzenie 3 (rozkład mieszany).** Każdy nieujemny ułamek $a/b$ ma jednoznaczny zapis $q+r/b$ z $q\in\mathbb N_0$ i $0\le r<b$.

*Dowód.* Twierdzenie o dzieleniu z resztą daje jednoznaczne $q,r$ takie, że $a=bq+r$. Dzieląc równość przez $b>0$, dostajemy tezę. $\square$

**Przykład 2.** $17/5=3+2/5$. Trzy pełne opakowania po pięć przedmiotów i dwa dodatkowe przedmioty odpowiadają tej samej liczbie jednostek pięcioelementowych.

## 2. Porządek i działania

**Definicja 4 (porównywanie).** Przy dodatnich mianownikach $a/b<c/d$ wtedy i tylko wtedy, gdy $ad<bc$.

**Twierdzenie 4 (porównanie przez wspólny mianownik).** Dla $b,d>0$ porządek $a/b$ i $c/d$ jest taki sam jak porządek $ad$ i $bc$.

*Dowód.* Mnożenie nierówności przez dodatnie $bd$ zachowuje kierunek: $(a/b)bd=ad$ i $(c/d)bd=bc$. $\square$

**Kontrprzykład 2.** Z $3<5$ nie wynika $3/4<5/9$. W rzeczywistości $3\cdot9=27>20=5\cdot4$, więc $3/4>5/9$.

**Definicja 5 (działania).** Dla $b,d>0$ ustalamy $a/b+c/d=(ad+bc)/(bd)$, $a/b-c/d=(ad-bc)/(bd)$, $(a/b)(c/d)=ac/(bd)$ oraz $(a/b):(c/d)=ad/(bc)$, gdy $c\ne0$.

**Twierdzenie 5 (wspólny mianownik).** $a/b+c/b=(a+c)/b$.

*Dowód.* Z definicji 5 suma wynosi $(ab+bc)/b^2=b(a+c)/b^2$, a skrócenie przez $b$ daje $(a+c)/b$. $\square$

**Twierdzenie 6 (mnożenie przez odwrotność).** Dla $c\ne0$ dzielenie przez $c/d$ jest mnożeniem przez $d/c$.

*Dowód.* $(c/d)(d/c)=1$, a zatem $d/c$ jest elementem odwrotnym do $c/d$ w $\mathbb Q$. $\square$

**Przykład 3.** $2/3+3/4=8/12+9/12=17/12=1+5/12$.

**Przykład 4.** $(5/6):(10/9)=(5/6)(9/10)=3/4$.

**Kontrprzykład 3.** $1/2+1/3\ne2/5$. Prawidłowo $1/2+1/3=5/6$. Dodawanie liczników i mianowników nie jest regułą sumowania ułamków.

**Kontrprzykład 4.** $(1/2):(0/7)$ nie jest określone. Dzielenie przez zero pozostaje niedozwolone również w zapisie ułamkowym.

## 3. Liczby dziesiętne i dokładność

**Definicja 6 (ułamek dziesiętny).** Liczba z zapisem skończonym $d_0,d_1\ldots d_k$ ma wartość $d_0+\sum_{j=1}^{k}d_j10^{-j}$, gdzie każda cyfra $d_j\in\{0,\ldots,9\}$. Przecinek oddziela część całkowitą od ułamkowej.

**Twierdzenie 7 (zamiana zapisu).** Każda skończona liczba dziesiętna jest wymierna i ma postać $m/10^k$ dla pewnych $m\in\mathbb Z$ i $k\ge0$.

*Dowód.* Mnożenie przez $10^k$ przesuwa przecinek o $k$ miejsc, dając liczbę całkowitą $m$. Dzielenie przez $10^k$ odtwarza liczbę początkową. $\square$

**Twierdzenie 8 (kryterium skończoności w systemie dziesiętnym).** Ułamek nieskracalny $a/b$ z $b>0$ ma skończony zapis dziesiętny wtedy i tylko wtedy, gdy każdy dzielnik pierwszy $b$ jest równy 2 lub 5.

*Dowód.* Zapis skończony daje $a/b=m/10^k$, więc $b\mid10^k$ po skróceniu przez względnie pierwszy licznik; czynniki pierwsze $b$ mogą być tylko 2 i 5. Odwrotnie, gdy $b=2^u5^v$, to dla $k=\max(u,v)$ liczba $b$ dzieli $10^k$, a więc $a/b=(a10^k/b)/10^k$. $\square$

**Przykład 5.** $3/8=375/1000=0,375$. Natomiast $1/3=0,(3)$ ma nieskończony zapis okresowy.

**Definicja 7 (zaokrąglenie).** Zaokrąglenie do $k$ miejsc po przecinku w przyjętej regule „połowy w górę” jest najbliższą wielokrotnością $10^{-k}$, a przy dokładnym remisie wybieramy większą. Dla liczb ujemnych ta konwencja wymaga osobnego uwzględnienia kierunku osi.

**Twierdzenie 9 (granica błędu).** Dla nieujemnego $x$ i zaokrąglenia $R_k(x)$ do $k$ miejsc po przecinku zachodzi $|x-R_k(x)|\le\tfrac12 10^{-k}$.

*Dowód.* Kolejne wielokrotności $10^{-k}$ są oddalone o $10^{-k}$. Każdy punkt leży najwyżej w połowie odstępu od jednej z dwóch sąsiednich wielokrotności. $\square$

**Kontrprzykład 5.** $0,33$ nie jest dokładnie równe $1/3$. Różnica wynosi $1/300$, dlatego obliczeń z dokładnymi ułamkami nie wolno bez potrzeby zastępować zaokrągleniami.

## 4. Stosunki, proporcje i wielkości

**Definicja 8 (stosunek).** Dla wielkości $A,B$ tego samego rodzaju i $B\ne0$ stosunek $A:B$ jest bezwymiarową liczbą $A/B$ po sprowadzeniu jednostek do wspólnej miary. W zapisie $2:3$ dwukropek oznacza stosunek, nie koniecznie dzielenie całkowite.

**Definicja 9 (proporcja).** Równość $a/b=c/d$ przy $b,d\ne0$ nazywamy proporcją.

**Twierdzenie 10 (iloczyny skrajnych i środkowych).** Proporcja $a/b=c/d$ jest równoważna $ad=bc$.

*Dowód.* Mnożymy obie strony przez niezerowe $bd$; odwrotnie dzielimy równość $ad=bc$ przez $bd$. $\square$

**Twierdzenie 11 (podział w stosunku).** Jeżeli $T\ge0$ dzielimy na części $x,y\ge0$ o stosunku $m:n$, gdzie $m,n>0$, to $x=Tm/(m+n)$ i $y=Tn/(m+n)$.

*Dowód.* Z $x/y=m/n$ (dla $T>0$) wynika $nx=my$, a z $x+y=T$ otrzymujemy wskazane wzory. Gdy $T=0$, obie części są zerowe; stosunek $x/y$ nie jest wtedy określony, lecz formuły przydziału nadal działają. $\square$

**Przykład 6.** Kwotę 150 zł dzielimy w stosunku 2:3: otrzymujemy 60 zł i 90 zł.

**Kontrprzykład 6.** Stosunek 2 m do 50 cm nie wynosi $2/50$. Najpierw trzeba zamienić 2 m na 200 cm; prawidłowy stosunek to $200/50=4$.

**Definicja 10 (proporcjonalność prosta).** Wielkości $x,y$ są wprost proporcjonalne, jeżeli $y=kx$ ze stałą $k$ niezależną od $x$ w badanym zakresie.

**Twierdzenie 12 (stały iloraz).** Dla $x\ne0$ zależność $y=kx$ jest równoważna stałości $y/x=k$.

*Dowód.* Dzielimy równanie przez niezerowe $x$, a w przeciwną stronę mnożymy przez $x$. $\square$

**Kontrprzykład 7.** Opłata za przejazd $y=5+2x$ nie jest wprost proporcjonalna do odległości $x$, ponieważ $y/x=5/x+2$ zależy od $x$.

## 5. Procenty, zmiany i pułapki

**Definicja 11 (procent).** $p\%:=p/100$. Wyrażenie „$p\%$ liczby $B$” oznacza $(p/100)B$; $B$ jest podstawą procentowania.

**Twierdzenie 13 (zmiana procentowa).** Po zwiększeniu $B$ o $p\%$ otrzymujemy $B(1+p/100)$, a po zmniejszeniu o $p\%$ — $B(1-p/100)$.

*Dowód.* Dodajemy do $B$ odpowiednio $pB/100$ lub odejmujemy tę wielkość, po czym wyłączamy $B$ przed nawias. $\square$

**Twierdzenie 14 (kolejne zmiany).** Zwiększenie o $p\%$, a następnie zmniejszenie o $p\%$ dla $0<p<100$ daje $B(1-(p/100)^2)<B$.

*Dowód.* Iloczyn mnożników $(1+t)(1-t)=1-t^2$ dla $t=p/100$ jest mniejszy od 1. $\square$

**Przykład 7.** Cena 200 zł po podwyżce o 10% i obniżce o 10% wynosi $200\cdot1,1\cdot0,9=198$ zł, a nie 200 zł.

**Kontrprzykład 8.** Wzrost z 40 do 50 to 25%, bo podstawą jest 40. Spadek z 50 do 40 to 20%, bo podstawą jest 50. Te procenty nie są przeciwne względem tej samej podstawy.

**Definicja 12 (punkt procentowy).** Różnica udziałów wyrażonych w procentach, np. 20% i 25%, wynosi 5 punktów procentowych; względny wzrost udziału wynosi 25% wartości początkowej.

**Twierdzenie 15 (odtwarzanie podstawy).** Jeśli $p\ne0$ i $p\%$ pewnej liczby $B$ wynosi $C$, to $B=100C/p$.

*Dowód.* Równanie $C=pB/100$ mnożymy przez $100/p$. $\square$

**Przykład 8.** Jeśli 15% ceny to 30 zł, cena początkowa wynosi $30/0,15=200$ zł.

## 6. Dokładność modelowania i zakres stosowania

**Twierdzenie 16 (średnia ważona udziałów).** Jeśli $A,B\ge0$, $A+B>0$, a w dwóch grupach udział cechy wynosi odpowiednio $p$ i $q$ jako liczby z $[0,1]$, to łączny udział wynosi $(Ap+Bq)/(A+B)$ i należy do przedziału $[\min(p,q),\max(p,q)]$.

*Dowód.* Liczba obiektów z cechą to $Ap+Bq$, a liczba wszystkich to $A+B$. Dla $p\le q$ mamy $p(A+B)\le Ap+Bq\le q(A+B)$; dzielimy przez dodatnie $A+B$. $\square$

**Kontrprzykład 9.** Średnia arytmetyczna 20% i 80% nie musi być udziałem całej populacji. Gdy grupy liczą 10 i 90 osób, udział wynosi $(10\cdot0,2+90\cdot0,8)/100=74\%$, nie 50%.

**Uwaga metodologiczna.** Procent może opisywać udział w skończonej populacji, zmianę wielkości, stopę procentową albo prawdopodobieństwo; sens podstawy i jednostek trzeba ustalić osobno. Wzory ułamkowe są dokładne, lecz dane pomiarowe mogą być przybliżone. Konstrukcja ciała $\mathbb Q$ i okresowość rozwinięć w dowolnej podstawie zostały już opracowane w F14.3 i F19.1; ten punkt pozostaje wykładem szkolnym, nie duplikatem monografii algebraicznej.



## 7. Gęstość liczb wymiernych i pułapka reprezentacji

**Definicja 13 (przedział wymierny).** Dla liczb wymiernych $a<b$ otwarty przedział $(a,b)$ zawiera te liczby $x$, które spełniają obie nierówności $a<x$ oraz $x<b$. Zapis nie wskazuje liczby elementów przedziału.

**Twierdzenie 17 (liczba wymierna pomiędzy dwiema wymiernymi).** Dla dowolnych $a,b\in\mathbb Q$ z $a<b$ istnieje $c\in\mathbb Q$ spełniające $a<c<b$.

*Dowód.* Wybieramy $c=(a+b)/2$. Liczby wymierne są zamknięte na dodawanie i dzielenie przez niezerową liczbę całkowitą 2, zatem $c$ jest wymierna. Ponieważ $b-a>0$, mamy $c-a=(b-a)/2>0$ oraz $b-c=(b-a)/2>0$. $\square$

**Twierdzenie 18 (nieskończenie wiele wymiernych w przedziale).** Dla $a<b$ wymiernych przedział $(a,b)$ zawiera nieskończenie wiele różnych liczb wymiernych.

*Dowód.* Dla każdego $n\ge2$ przyjmijmy $c_n=a+(b-a)/n$. Wówczas $a<c_n<b$. Gdy $n<m$, mamy $(b-a)/n>(b-a)/m$, a więc $c_n>c_m$. Wszystkie wybrane liczby są różne; takich indeksów jest nieskończenie wiele. $\square$

**Przykład 9.** Między $1/2$ i $3/5$ leżą m.in. $11/20=0,55$ oraz $17/30\approx0,5667$. Wskazanie jednej liczby nie wyczerpuje przedziału.

**Kontrprzykład 10.** Między kolejnymi liczbami naturalnymi 4 i 5 nie ma liczby naturalnej, ale jest nieskończenie wiele liczb wymiernych. Własność „sąsiedztwa” zależy od rozpatrywanego zbioru.

## 8. Skąd bierze się okres rozwinięcia dziesiętnego?

**Definicja 14 (reszta w dzieleniu pisemnym).** Dla nieskracalnego ułamka $a/b$ z $0\le a<b$ i $b>0$ kolejne reszty wyznaczamy przez $r_0=a$, $d_n=\lfloor10r_{n-1}/b\rfloor$ i $r_n=10r_{n-1}-bd_n$. Każda reszta spełnia $0\le r_n<b$, a $d_n$ jest cyfrą dziesiętną.

**Twierdzenie 19 (skończoność albo okresowość).** Rozwinięcie dziesiętne dowolnego nieujemnego ułamka wymiernego jest skończone albo od pewnego miejsca okresowe.

*Dowód.* Część całkowitą oddzielamy przez dzielenie z resztą, więc wystarczy ułamek właściwy. W algorytmie z definicji 14 reszta jest jedną z $b$ liczb $0,1,\ldots,b-1$. Jeśli reszta stanie się zerem, dalsze cyfry są zerami i zapis się kończy. Jeśli zero nigdy nie wystąpi, wśród pierwszych $b+1$ reszt pewne dwie są równe. Następna cyfra i reszta zależą jednoznacznie od poprzedniej reszty, więc od powtórzenia cały ciąg cyfr i reszt się powtarza. $\square$

**Przykład 10.** Dla $1/7$ reszty po kolejnych cyfrach to $3,2,6,4,5,1$, a następnie ponownie $3$; zapis wynosi $0,(142857)$. Długość okresu 6 nie jest liczbą cyfr mianownika, lecz wynika z cyklu reszt.

**Kontrprzykład 11.** Nieskończony zapis dziesiętny nie musi oznaczać liczby niewymiernej. $1/7$ ma nieskończenie wiele cyfr, lecz jest wymierna. Z kolei liczby niewymierne nie mają rozwinięć ostatecznie okresowych.

**Twierdzenie 20 (odwrotność: okresowy zapis jest wymierny).** Jeżeli po $m$ cyfrach po przecinku następuje blok $k$ cyfr powtarzany bez końca, to reprezentowana liczba jest wymierna.

*Dowód.* Niech $x$ oznacza część ułamkową, $A$ — wartość pierwszych $m$ cyfr, a $B$ — wartość powtarzanego bloku długości $k$ (dopuszczamy zera wiodące). Wtedy $x=A/10^m+B/(10^m(10^k-1))$. Jest to suma dwóch liczb wymiernych. Wzór wynika z szeregu geometrycznego $1+10^{-k}+10^{-2k}+\cdots=1/(1-10^{-k})$. $\square$

**Przykład 11.** $0,(27)=27/99=3/11$. Zapis $0,1(6)$ oznacza $1/10+6/(10\cdot9)=1/6$. Nawias oznacza powtarzanie, a nie mnożenie.

## 9. Kontrola podstawy procentowania

**Twierdzenie 21 (zmiana podstawy).** Jeśli wielkość wzrosła z $A>0$ do $B>A$, to procent wzrostu względem $A$ wynosi $100(B-A)/A$, a procent spadku przy powrocie z $B$ do $A$ wynosi $100(B-A)/B$. Pierwszy procent jest większy.

*Dowód.* Wzory wynikają z definicji procentu. Ponieważ $0<A<B$ i $B-A>0$, zachodzi $(B-A)/A>(B-A)/B$. $\square$

**Przykład 12.** Zmiana z 80 na 100 to wzrost o 25%; powrót z 100 na 80 to spadek o 20%. W obu przypadkach różnica bezwzględna wynosi 20, ale podstawa procentowania jest inna.

**Kontrprzykład 12.** Nie wolno wyznaczać procentowej zmiany przez samo odjęcie dwóch procentowych wskaźników bez określenia podstaw. Zmiana udziału z 15% na 18% to 3 punkty procentowe, ale 20% wzrostu względem początkowych 15%.

\newpage

# Część B. Zadania rozwiązane

## Ułamki i porządek

**Zadanie 1.** Skróć $18/24$. *Rozwiązanie:* NWD wynosi 6, więc $18/24=3/4$.

**Zadanie 2.** Rozszerz $5/7$ do mianownika 42. *Rozwiązanie:* Mnożymy licznik i mianownik przez 6, otrzymując $30/42$.

**Zadanie 3.** Porównaj $7/12$ i $5/8$. *Rozwiązanie:* $7\cdot8=56<60=5\cdot12$, zatem $7/12<5/8$.

**Zadanie 4.** Zapisz $23/6$ jako liczbę mieszaną. *Rozwiązanie:* $23=3\cdot6+5$, więc $23/6=3+5/6$.

**Zadanie 5.** Zamień $2+3/5$ na ułamek niewłaściwy. *Rozwiązanie:* $(2\cdot5+3)/5=13/5$.

**Zadanie 6.** Oblicz $3/8+1/4$. *Rozwiązanie:* $3/8+2/8=5/8$.

**Zadanie 7.** Oblicz $5/6-1/9$. *Rozwiązanie:* $15/18-2/18=13/18$.

**Zadanie 8.** Oblicz $(3/5)(10/9)$. *Rozwiązanie:* $30/45=2/3$.

**Zadanie 9.** Oblicz $(4/7):(8/21)$. *Rozwiązanie:* $(4/7)(21/8)=3/2$.

**Zadanie 10.** Czy $2/3=8/12$? *Rozwiązanie:* Tak, bo $2\cdot12=3\cdot8=24$.

## Zapis dziesiętny

**Zadanie 11.** Zapisz $7/20$ dziesiętnie. *Rozwiązanie:* $7/20=35/100=0,35$.

**Zadanie 12.** Zapisz $0,125$ jako ułamek nieskracalny. *Rozwiązanie:* $125/1000=1/8$.

**Zadanie 13.** Czy $11/40$ ma zapis skończony? *Rozwiązanie:* Tak, $40=2^3\cdot5$, więc $11/40=0,275$.

**Zadanie 14.** Czy $5/12$ ma zapis skończony? *Rozwiązanie:* Nie, ponieważ po skróceniu mianownik 12 zawiera czynnik 3.

**Zadanie 15.** Zaokrąglij $2,746$ do setnych. *Rozwiązanie:* $2,75$.

**Zadanie 16.** Oszacuj błąd zaokrąglenia do setnych. *Rozwiązanie:* Wartość bezwzględna błędu nie przekracza $0,005$.

**Zadanie 17.** Porównaj $0,7$ i $0,68$. *Rozwiązanie:* $0,70>0,68$.

**Zadanie 18.** Oblicz $0,25\cdot0,4$. *Rozwiązanie:* $(25/100)(4/10)=100/1000=0,1$.

**Zadanie 19.** Oblicz $1,2:0,3$. *Rozwiązanie:* $(12/10):(3/10)=12/3=4$.

**Zadanie 20.** Czy $0,333$ jest równe $1/3$? *Rozwiązanie:* Nie, różnica wynosi $1/3000$.

## Proporcje i procenty

**Zadanie 21.** Podziel 240 w stosunku 3:5. *Rozwiązanie:* Suma części to 8; otrzymujemy 90 i 150.

**Zadanie 22.** Rozwiąż $x/9=4/3$. *Rozwiązanie:* $3x=36$, zatem $x=12$.

**Zadanie 23.** Oblicz 15% z 320. *Rozwiązanie:* $0,15\cdot320=48$.

**Zadanie 24.** Jakim procentem 80 jest 20? *Rozwiązanie:* $20/80=1/4=25\%$.

**Zadanie 25.** Cena 500 zł wzrosła o 8%. *Rozwiązanie:* $500\cdot1,08=540$ zł.

**Zadanie 26.** Cena 500 zł spadła o 8%. *Rozwiązanie:* $500\cdot0,92=460$ zł.

**Zadanie 27.** Po rabacie 20% cena wynosi 160 zł. Ile wynosiła przed rabatem? *Rozwiązanie:* $0,8B=160$, więc $B=200$ zł.

**Zadanie 28.** Udział wzrósł z 12% do 15%. Podaj wzrost w punktach procentowych i względny. *Rozwiązanie:* 3 punkty procentowe oraz $(15-12)/12=25\%$.

**Zadanie 29.** Oblicz $2\%$ z 1,5 kg. *Rozwiązanie:* $0,02\cdot1,5=0,03$ kg, czyli 30 g.

**Zadanie 30.** Dwie grupy po 20 osób mają frekwencję 50% i 80%. Jaka jest frekwencja łączna? *Rozwiązanie:* $(10+16)/40=65\%$.

## Problemy przekrojowe

**Problem A (zmiana podstawy).** Liczba osób w grupie wzrosła z 24 do 30, a następnie spadła do 24. Oblicz oba procenty zmian.

*Rozwiązanie.* Wzrost to $6/24=25\%$, spadek to $6/30=20\%$. Odmienne podstawy wyjaśniają, dlaczego wartości procentowe nie są jednakowe.

**Problem B (skala i jednostki).** Odcinek na mapie ma 4 cm, a skala wynosi 1:25000. Jaka jest odległość w terenie?

*Rozwiązanie.* $4\cdot25000=100000$ cm = 1000 m = 1 km. Zapis 1:25000 oznacza stosunek długości w tych samych jednostkach.

**Problem C (średnia ważona).** W grupie A liczącej 20 osób 75% zdało test, a w grupie B liczącej 80 osób 50% zdało. Jaki procent zdał łącznie?

*Rozwiązanie.* W A zdało 15 osób, w B 40, razem 55 na 100, czyli 55%. Prosta średnia 62,5% byłaby błędna, ponieważ grupy nie są równoliczne.

**Problem D (granica informacji).** Dwa ułamki po zaokrągleniu do jednej cyfry po przecinku dają 0,3. Czy muszą być równe?

*Rozwiązanie.* Nie. Przykładowo $1/4=0,25$ i $1/3=0,333\ldots$ po zaokrągleniu „połowy w górę” dają 0,3, lecz $1/4\ne1/3$. Zaokrąglenie nie jest operacją odwracalną.


## Rozszerzony warsztat rachunkowy — kontrola rozumowania

**Zadanie 31 (część nieznanej całości).** $3/8$ kolekcji to 21 obiektów. Ile obiektów zawiera kolekcja? *Rozwiązanie.* Jedna ósma to $21:3=7$ obiektów, więc całość to $8\cdot7=56$. Kontrola: $56\cdot3/8=21$.

**Zadanie 32 (dwa etapy).** Zużyto $1/4$ zapasu, a potem $1/3$ pozostałej części. Jaka część początkowego zapasu pozostała? *Rozwiązanie.* Po pierwszym etapie pozostało $3/4$. Drugi etap zabiera $1/3$ z $3/4$, czyli $1/4$ zapasu początkowego. Pozostaje $1/2$.

**Zadanie 33 (błędne dodawanie).** Uczeń napisał $2/5+1/10=3/15$. Wskaż błąd i popraw wynik. *Rozwiązanie.* Mianowniki opisują rozmiar części i nie sumują się. Po rozszerzeniu $2/5=4/10$ otrzymujemy $5/10=1/2$.

**Zadanie 34 (liczba między ułamkami).** Podaj ułamek ściśle między $1/3$ i $1/2$. *Rozwiązanie.* Średnia $(1/3+1/2)/2=5/12$ spełnia $1/3<5/12<1/2$, bo $4/12<5/12<6/12$.

**Zadanie 35 (gęstość wymiernych — przypadek).** Dlaczego między dwoma różnymi ułamkami $a<b$ leży kolejny wymierny? *Rozwiązanie.* Liczba $(a+b)/2$ jest wymierna, gdyż suma i dzielenie przez 2 zachowują wymierność; z $a<b$ wynika $a<(a+b)/2<b$.

**Zadanie 36 (odwracanie).** Wyznacz odwrotność $-7/9$ i sprawdź wynik. *Rozwiązanie.* Odwrotność to $-9/7$, gdyż $(-7/9)(-9/7)=1$. Zero nie ma odwrotności.

**Zadanie 37 (wartość wyrażenia).** Oblicz $1/2+(3/4):(9/8)$. *Rozwiązanie.* Dzielenie daje $(3/4)(8/9)=2/3$, a suma $1/2+2/3=7/6$.

**Zadanie 38 (równanie).** Rozwiąż $x-3/5=7/10$. *Rozwiązanie.* Dodajemy $3/5=6/10$ do obu stron i otrzymujemy $x=13/10$; podstawienie potwierdza równość.

**Zadanie 39 (przedział).** Czy $0,58$ należy do przedziału $[1/2,3/5]$? *Rozwiązanie.* Tak, ponieważ $0,5\le0,58\le0,6$. Porównanie wykonano po zamianie krańców na dokładne ułamki dziesiętne.

**Zadanie 40 (mianownik).** Znajdź $n\in\mathbb N$ takie, że $3/n=1/4$. *Rozwiązanie.* Z $3\cdot4=n$ wynika $n=12$. Mianownik jest dodatni, więc rozwiązanie jest dopuszczalne.

**Zadanie 41 (liczba dziesiętna).** Zapisz $0,0625$ jako ułamek nieskracalny. *Rozwiązanie.* $625/10000=1/16$ po podzieleniu przez 625; mianownik jest potęgą 2.

**Zadanie 42 (okresowość).** Dlaczego $2/11$ nie ma skończonego zapisu dziesiętnego? *Rozwiązanie.* Mianownik 11 jest względnie pierwszy z 10. Dzielenie pisemne daje $0,(18)$, co kontroluje $18/99=2/11$.

**Zadanie 43 (oszacowanie).** Liczbę $x$ zaokrąglono do setnych, otrzymując $1,24$. Podaj dopuszczalny przedział $x$ przy regule połowy w górę. *Rozwiązanie.* $1,235\le x<1,245$. Lewy koniec daje remis zaokrąglany do $1,24$, prawy do $1,25$.

**Zadanie 44 (błąd względny).** Pomiar 20 cm różni się od wartości 19 cm o 1 cm. Ile wynosi błąd względny liczony względem wartości 19 cm? *Rozwiązanie.* $1/19\approx5,263\%$. Nie wolno zastąpić mianownika 20 bez zmiany definicji błędu.

**Zadanie 45 (przecinek).** Oblicz $0,06:0,002$. *Rozwiązanie.* Mnożymy dzielną i dzielnik przez 1000: $60:2=30$. Mnożenie obu liczb przez ten sam niezerowy czynnik nie zmienia ilorazu.

**Zadanie 46 (stosunek jednostek).** Porównaj 750 g do 2 kg. *Rozwiązanie.* Po przeliczeniu 2 kg na 2000 g stosunek wynosi $750/2000=3/8$. Sam zapis $750/2$ jest błędny wymiarowo.

**Zadanie 47 (podział trzech części).** Podziel 360 w stosunku 2:3:4. *Rozwiązanie.* Suma wag wynosi 9; jednostka wagi to 40. Części wynoszą 80, 120 i 160, a ich suma to 360.

**Zadanie 48 (skala).** Odległość 2,4 cm na planie w skali 1:5000 odpowiada ilu metrom? *Rozwiązanie.* $2,4\cdot5000=12000$ cm, czyli 120 m. Zmiana jednostki następuje po użyciu skali.

**Zadanie 49 (proporcja).** Rozwiąż $7/12=x/36$. *Rozwiązanie.* Mnożymy przez 36: $x=21$. Kontrola: $21/36=7/12$ po skróceniu przez 3.

**Zadanie 50 (brak proporcjonalności).** Czy koszt $K(n)=10+4n$ jest wprost proporcjonalny do $n$? *Rozwiązanie.* Nie, bo $K(1)/1=14$, a $K(2)/2=9$. Stała opłata 10 niszczy proporcjonalność.

**Zadanie 51 (procent z procentu).** Ile wynosi 30% z 40% liczby 500? *Rozwiązanie.* $0,3\cdot0,4\cdot500=60$. To 12% początkowej liczby.

**Zadanie 52 (podwyżka i rabat).** Cena 100 zł wzrosła o 20%, a następnie zmalała o 20%. *Rozwiązanie.* $100\cdot1,2\cdot0,8=96$ zł. Różnica wynosi 4 zł, czyli 4% początkowej ceny.

**Zadanie 53 (odtwarzanie ceny).** Po podwyżce o 25% cena wynosi 250 zł. Ile wynosiła przed podwyżką? *Rozwiązanie.* $1,25B=250$, zatem $B=200$ zł. Nie odejmujemy 25% od 250, bo to inna podstawa.

**Zadanie 54 (punkty procentowe).** Udział wzrósł z 40% do 50%. Podaj oba typy wzrostu. *Rozwiązanie.* Wzrost to 10 punktów procentowych; względem początkowych 40% jest to $10/40=25\%$.

**Zadanie 55 (część i całość).** 18 uczniów stanowi 60% klasy. Ilu uczniów liczy klasa? *Rozwiązanie.* $18/0,6=30$; sprawdzenie: $0,6\cdot30=18$.

**Zadanie 56 (udziały ważone).** W grupach liczących 40 i 60 osób zdawalność wynosi 75% i 50%. *Rozwiązanie.* Zdających jest $30+30=60$ na 100 osób, czyli 60%. Średnia 62,5% nie uwzględnia różnych liczebności.

**Zadanie 57 (dane niemożliwe).** Czy w grupie 7 osób dokładnie 25% może stanowić liczba całkowita osób? *Rozwiązanie.* Nie, bo $0,25\cdot7=1,75$, a liczba osób jest całkowita. Wartość 25% może być jedynie przybliżeniem udziału.

**Zadanie 58 (porównanie rabatów).** Co daje niższą cenę: jednorazowy rabat 30% czy dwa rabaty po 15%? *Rozwiązanie.* Pierwszy mnożnik to 0,7, drugi $0,85^2=0,7225$. Tańszy jest pierwszy wariant.

**Zadanie 59 (mieszanie).** Zmieszano 2 l roztworu o stężeniu 10% i 3 l o stężeniu 20%. Oblicz stężenie mieszaniny, zakładając addytywność objętości. *Rozwiązanie.* Ilość substancji to $2\cdot0,1+3\cdot0,2=0,8$ l, łączna objętość 5 l; stężenie wynosi 16%. Założenie o addytywności jest częścią modelu.

**Zadanie 60 (dokładność).** Czy z wartości zaokrąglonych 1,2 i 2,3 można wywnioskować, że suma dokładna to 3,5? *Rozwiązanie.* Nie. Przy zaokrągleniu do dziesiątych wartości leżą odpowiednio w $[1,15,1,25)$ i $[2,25,2,35)$, więc suma leży w $[3,40,3,60)$. Wartość 3,5 jest tylko sumą zapisów przybliżonych.

**Problem E (podział budżetu).** Budżet 1200 zł dzieli się na trzy cele w stosunku 2:3:5. Z ostatniej części wydano 20%, a z pierwszej 25%. Ile pozostało łącznie?

*Rozwiązanie.* Części wynoszą 240, 360 i 600 zł. Wydano $0,25\cdot240=60$ zł oraz $0,2\cdot600=120$ zł. Pozostało $1200-180=1020$ zł. Nie sumujemy procentów 25% i 20%, ponieważ dotyczą różnych podstaw.

**Problem F (skala dwóch map).** Na mapie A w skali 1:10000 odcinek ma 6 cm. Jaką długość ma na mapie B w skali 1:25000?

*Rozwiązanie.* Odległość terenowa wynosi 60000 cm. Na mapie B odcinek ma $60000/25000=2,4$ cm. Mniejsza skala oznacza krótszy odcinek na papierze dla tej samej odległości terenowej.

**Problem G (mylące średnie).** Dwie klasy mają zdawalność 90% i 60%, lecz razem 70%. Czy to możliwe? Podaj liczebności.

*Rozwiązanie.* Tak. Niech pierwsza klasa liczy 10 osób, druga 20. Zdających jest $9+12=21$ na 30 osób, czyli 70%. Średnia nieważona 75% byłaby błędna.

**Problem H (błąd pomiaru i procent).** Długość podano jako 8,0 cm po zaokrągleniu do dziesiątych. Jaki przedział długości jest zgodny z tym wynikiem i jaki jest największy błąd bezwzględny?

*Rozwiązanie.* Przy regule połowy w górę dla nieujemnych długości mamy $7,95\le L<8,05$ cm. Błąd względem wartości podanej nie przekracza 0,05 cm. Granica 8,05 nie należy do przedziału, ponieważ zaokrągliłaby się do 8,1 cm.

**Status:** Rozdział E1-01 stanowi nowe opracowanie źródłowe; nie zastępuje F14.3, F10.1 ani F19.1. Żadna liczba stron nie jest doliczana do oficjalnego bilansu 585/1222 bez integracji z rzeczywistym monolitem 0.20 i kontroli składu.
