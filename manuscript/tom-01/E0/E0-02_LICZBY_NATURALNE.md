---
title: 'ONTOLOGIA LICZBY — TOM I'
subtitle: 'E0-02. Liczby naturalne — od liczebności do zapisu pozycyjnego'
author: 'Andrzej Mikulski'
date: '1 listopada 2026'
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Miejsce w korpusie:** poziom I, E0-02 „Liczby naturalne”, bezpośrednio po E0-01 „Klasyfikacja i relacje”. Zakres taksonomii: liczebność, zapis pozycyjny, oszacowania, porównania. Oznaczenie E0-02 jest autorską jednostką dydaktyczną, a nie kodem MSC2020. Powiązania tematyczne: arytmetyka elementarna i dydaktyka matematyki. Ten rozdział rozwija podstawy; zaawansowane konstrukcje teorii mnogości, obliczalności i teorii systemów pozycyjnych pozostają w istniejących opracowaniach F8–F10.

# Część A. Liczba jako wynik liczenia

## 1. Obiekt, zbiór i liczebność

**Definicja 1 (skończona kolekcja).** Rozpatrujemy zbiór $A$ rozróżnialnych obiektów. Jest skończony, gdy można jego elementy zestawić bez powtórzeń z kolekcją $[n]=\{1,2,\ldots,n\}$ dla pewnego $n\geq 0$, przy czym $[0]=\varnothing$. Wówczas piszemy $|A|=n$. Dla dziecka oznacza to możliwość wskazania każdego przedmiotu dokładnie raz.

**Definicja 2 (liczba naturalna).** W rozdziale przyjmujemy $\mathbb N_0=\{0,1,2,\ldots\}$, a $\mathbb N_+=\{1,2,\ldots\}$. Zero jest liczbą naturalną w przyjętej konwencji. W innych podręcznikach symbol $\mathbb N$ może zaczynać się od jedynki, dlatego zapis $\mathbb N_0$ usuwa niejednoznaczność.

**Twierdzenie 1 (niezależność liczebności od kolejności).** Jeżeli elementy skończonego zbioru $A$ policzono bez pominięć i powtórzeń w dwóch różnych kolejnościach, to wynik liczenia jest taki sam.

*Dowód.* Każda poprawna kolejność jest bijekcją $[n]\to A$. Złożenie jednej bijekcji z odwrotnością drugiej daje bijekcję $f:[n]\to[m]$. Wykażmy indukcyjnie, że wtedy $n=m$. Gdy $n=0$, zbiór $[n]$ jest pusty, więc surjektywność wymusza $m=0$. Gdy $n>0$, musi też zachodzić $m>0$. Możemy zamienić miejscami dwie wartości w zbiorze docelowym tak, aby $f(n)=m$; nadal otrzymujemy bijekcję. Jej ograniczenie do $[n-1]$ jest wtedy bijekcją na $[m-1]$. Z założenia indukcyjnego $n-1=m-1$, czyli $n=m$. Zatem wynik liczenia nie zależy od kolejności. $\square$

**Przykład.** Pięć kamieni liczymy od lewej lub od prawej. Każdy kamień ma inny numer porządkowy, ale zbiór ma w obu przypadkach pięć elementów. **Kontrprzykład 1 (liczenie z powtórzeniem).** Wskazanie tego samego kamienia dwa razy może dać pozornie sześć wskazań. Nie jest to poprawne liczenie pięciu obiektów.

**Twierdzenie 2 (dołożenie jednego nowego obiektu).** Jeżeli $A$ ma $n$ elementów, a $u\notin A$, to $A\cup\{u\}$ ma $n+1$ elementów.

*Dowód.* Niech $f:[n]\to A$ będzie bijekcją. Rozszerzamy ją przez $f(n+1)=u$. Nowa funkcja obejmuje każdy element $A\cup\{u\}$ i nie przyjmuje żadnej wartości dwukrotnie, ponieważ $u$ nie należał do $A$. Jest więc bijekcją. $\square$

**Kontrprzykład 2.** Jeżeli $u\in A$, to $A\cup\{u\}=A$; dołożenie *wskazania* już istniejącego przedmiotu nie zwiększa liczebności.

**Definicja 3 (następnik).** Następnikiem liczby $n$ jest $S(n)=n+1$. W modelu kolekcji jest to liczba obiektów po dołożeniu jednego nowego elementu. Poprzednik istnieje dla każdej liczby dodatniej, lecz nie dla zera w $\mathbb N_0$.

**Twierdzenie 3 (jednoznaczność następnika).** Jeśli $S(a)=S(b)$, to $a=b$.

*Dowód.* Z równości $a+1=b+1$ odejmujemy tę samą jedynkę po obu stronach w liczbach całkowitych, otrzymując $a=b$. W konstrukcji Peana własność ta jest jednym z aksjomatów następnika. $\square$

**Przykład 2.** Po liczbie $39$ następuje $40$. Zmiana dwóch cyfr nie oznacza przeskoczenia dziesięciu liczb; oznacza przeniesienie do następnego rzędu zapisu.

## 2. Porównywanie przez parowanie i oś liczbowa

**Definicja 4 (porządek liczebności).** Dla skończonych zbiorów $A,B$ piszemy $|A|\leq |B|$, jeśli istnieje przyporządkowanie każdemu elementowi $A$ innego elementu $B$ (iniekcja). Gdy pozostaje wolny element $B$, a oba zbiory są skończone, mamy $|A|<|B|$.

**Twierdzenie 4 (porównywanie bez przeliczania).** Jeżeli każdemu z siedmiu kubków przyporządkowano inny z dziewięciu talerzy, to talerzy jest więcej, niezależnie od ich ustawienia.

*Dowód.* Siedem par zużywa dokładnie siedem talerzy, pozostawiając dwa. Stąd $7<9$. W ogólności bijekcja z podzbiorem właściwym zbioru skończonego daje ścisłą nierówność liczebności. $\square$

**Definicja 5 (odcinek liczbowy).** Na osi liczbowej odległość między $a,b\in\mathbb N_0$ wynosi $|a-b|$ jednostek. Wskazanie liczby na osi oznacza położenie, a nie liczbę narysowanych kresek. Od $0$ do $5$ jest pięć odcinków jednostkowych, chociaż zaznaczono sześć punktów: $0,1,2,3,4,5$.

**Twierdzenie 5 (położenie i nierówność).** Dla naturalnych $a,b$ zachodzi $a<b$ wtedy i tylko wtedy, gdy punkt $a$ leży na osi liczbowej na lewo od punktu $b$.

*Dowód.* Położenie liczby $n$ definiujemy jako odległość $n$ jednostek od zera w prawo. Jeżeli $a<b$, to $b=a+k$ dla pewnego dodatniego $k$, więc od punktu $a$ należy wykonać $k$ kroków w prawo. Odwrotnie dodatnia liczba takich kroków oznacza $b>a$. $\square$

**Kontrprzykład 3.** Sześć oznaczonych punktów od $0$ do $5$ nie wyznacza sześciu jednostkowych odstępów. Mylenie punktów z odstępami prowadzi do błędu o jeden.

## 3. Dziesiątkowy zapis pozycyjny

**Definicja 6 (cyfra i wartość cyfry).** Cyfry dziesiętne to $0,1,\ldots,9$. W zapisie $d_k\ldots d_1d_0$ cyfra $d_i$ oznacza $d_i$ jednostek rzędu $10^i$, a wartość liczby wynosi
$$V(d_k\ldots d_0)=\sum_{i=0}^{k}d_i10^i.$$
Słowo „cyfra” oznacza znak zapisu, „liczba” — jego wartość. Dziesięć jest liczbą, ale nie pojedynczą cyfrą dziesiętną.

**Przykład 3.** $4062=4\cdot1000+0\cdot100+6\cdot10+2$. Zero na miejscu setek jest istotne: bez niego zapis $462$ oznacza inną liczbę.

**Definicja 7 (zapis kanoniczny).** Zapis naturalnej liczby jest kanoniczny, gdy dla zera ma postać „0”, a dla liczby dodatniej zaczyna się cyfrą niezerową. Zera wiodące nie zmieniają wartości, lecz nie należą do zapisu kanonicznego.

**Twierdzenie 6 (jednoznaczność zapisu dziesiętnego).** Każda liczba $n\in\mathbb N_0$ ma dokładnie jeden kanoniczny zapis dziesiętny.

*Dowód.* Dla $n=0$ zapis to „0”. Dla $n>0$ dzielimy $n$ przez $10$ z resztą: $n=10q+r$, $0\leq r<10$. Reszta $r$ jest jednoznaczną ostatnią cyfrą. Powtarzamy operację dla $q$, aż iloraz będzie zerem; ilorazy maleją dla liczb dodatnich, więc proces się kończy. Otrzymane reszty odczytane od końca tworzą zapis. Gdyby istniały dwa zapisy, oba miałyby tę samą ostatnią cyfrę (jedyną resztę z dzielenia przez $10$), a po jej usunięciu ten sam iloraz. Powtarzając, otrzymujemy identyczne wszystkie cyfry. $\square$

**Twierdzenie 7 (zakres liczb o danej długości).** Liczba dodatnia ma dokładnie $k\geq1$ cyfr w zapisie kanonicznym wtedy i tylko wtedy, gdy
$$10^{k-1}\leq n\leq10^k-1.$$

*Dowód.* Pierwsza cyfra jest co najmniej jedynką, zatem $n\geq10^{k-1}$. Wszystkie cyfry równe $9$ dają najwyżej $9(1+10+\cdots+10^{k-1})=10^k-1$. Liczby spoza tego przedziału wymagają odpowiednio mniej lub więcej cyfr. $\square$

**Kontrprzykład 4.** Zapisy „0047” i „47” mają tę samą wartość $47$, lecz różną długość jako ciągi znaków. Twierdzenie 7 dotyczy wyłącznie zapisów kanonicznych.

## 4. Porównywanie dużych liczb

**Twierdzenie 8 (porównanie długości).** Jeśli dodatnie liczby naturalne mają kanoniczne zapisy o odpowiednio $k$ i $l$ cyfrach i $k<l$, to pierwsza liczba jest mniejsza.

*Dowód.* Z Twierdzenia 7 pierwsza liczba nie przekracza $10^k-1$, a druga jest nie mniejsza niż $10^{l-1}\geq10^k$. Zatem pierwsza jest mniejsza. $\square$

**Twierdzenie 9 (pierwsza różniąca się cyfra).** Dwie liczby o tej samej liczbie cyfr porównujemy od lewej: większa jest ta, która ma większą pierwszą różniącą się cyfrę.

*Dowód.* Niech pierwsza różnica występuje na pozycji $j$ liczonej od zera z prawej. Różnica cyfr na tej pozycji ma wartość bezwzględną co najmniej $10^j$. Suma wszystkich możliwych różnic na pozycjach niższych jest nie większa niż $9(1+10+\cdots+10^{j-1})=10^j-1$. Niższe pozycje nie mogą więc zmienić znaku porównania. $\square$

**Przykład 4.** $58\,206<58\,260$, bo pierwsza różnica od lewej to cyfra dziesiątek: $0<6$. **Kontrprzykład 5.** Większa suma cyfr nie oznacza większej liczby: $99$ ma sumę cyfr $18$, lecz $100$ ma sumę cyfr $1$ i jest większa.

## 5. Oszacowania, zaokrąglenia i kontrola błędu

**Definicja 8 (przedział oszacowania).** Zapis $L\leq n\leq U$ oznacza, że znamy dolną i górną granicę wartości. Oszacowanie może być użyteczne bez znajomości dokładnego $n$.

**Definicja 9 (zaokrąglenie do wielokrotności $q$).** Dla $q\in\{10,100,1000,\ldots\}$ zaokrąglamy $n\in\mathbb N_0$ do najbliższej wielokrotności $q$. Przy dokładnym remisie wybieramy większą. Formalnie dla $n=aq+r$, $0\leq r<q$, przyjmujemy $R_q(n)=aq$ dla $r<q/2$, a $R_q(n)=(a+1)q$ dla $r\geq q/2$.

**Twierdzenie 10 (błąd zaokrąglenia).** Dla każdej naturalnej $n$ i powyższych $q$ zachodzi $|R_q(n)-n|\leq q/2$.

*Dowód.* Jeśli $r<q/2$, błąd wynosi $r<q/2$. W przeciwnym razie błąd to $q-r\leq q/2$. Oba przypadki wyczerpują możliwe reszty. $\square$

**Przykład 5.** $347$ zaokrąglone do dziesiątek daje $350$ (błąd $3$), do setek $300$ (błąd $47$). Wynik zaokrąglenia jest przybliżeniem, nie nową wartością dokładną liczby.

**Twierdzenie 11 (dodawanie oszacowań).** Jeśli $a\leq x\leq b$ oraz $c\leq y\leq d$, to $a+c\leq x+y\leq b+d$.

*Dowód.* Dodajemy nierówności $a\leq x$ i $c\leq y$, otrzymując $a+c\leq x+y$. Tak samo z $x\leq b$ i $y\leq d$ wynika druga nierówność. $\square$

**Twierdzenie 12 (błąd sumy dwóch zaokrągleń).** Jeżeli $x,y$ zaokrąglono oddzielnie do wielokrotności $q$, to
$$|(R_q(x)+R_q(y))-(x+y)|\leq q.$$

*Dowód.* Nierówność trójkąta daje lewą stronę nie większą niż $|R_q(x)-x|+|R_q(y)-y|$, a każdy składnik nie przekracza $q/2$ na mocy Twierdzenia 10. $\square$

**Kontrprzykład 6.** Suma zaokrąglonych składników nie musi być zaokrągleniem sumy: $R_{10}(14)+R_{10}(14)=10+10=20$, natomiast $R_{10}(28)=30$. Dlatego w obliczeniach wymagających dokładności najpierw dodajemy dokładne liczby, a dopiero potem zaokrąglamy wynik.

## 6. Przeniesienie wartości i sens zera

**Twierdzenie 13 (zamiana dziesięciu jednostek).** W dowolnym rzędzie dziesiętnym dziesięć jednostek tego rzędu ma wartość jednej jednostki rzędu następnego: $10\cdot10^j=10^{j+1}$.

*Dowód.* Wynika z reguły mnożenia potęg: $10\cdot10^j=10^1\cdot10^j=10^{j+1}$. Dla ucznia jest to matematyczne uzasadnienie wymiany dziesięciu patyczków na jedną wiązkę dziesięciu. $\square$

**Twierdzenie 14 (porównanie przez zaokrąglone granice).** Jeśli oszacowaliśmy $a$ z góry przez $U$ i $b$ z dołu przez $L$, a $U<L$, to na pewno $a<b$.

*Dowód.* Z $a\leq U<L\leq b$ przez przechodniość otrzymujemy $a<b$. $\square$

**Uwaga o zakresie.** Twierdzenia 1–14 formułujemy formalnie, ale ich modele (kamienie, oś, wiązki, karty z cyframi) są przeznaczone do edukacji wczesnoszkolnej. Materiał F10.1 zawiera osobną, znacznie bardziej zaawansowaną teorię kodowania i nie jest tu kopiowany. Bibliografia metodyczna: tekst źródłowy taksonomii (część 1, sekcja E0), klasyczne zasady arytmetyki pozycyjnej; odwołania do MSC 11 i 97 są tematyczne, nie identyfikują tego punktu jako MSC.

\newpage

# Część B. Ćwiczenia z pełnymi rozwiązaniami

Poniższe ćwiczenia są samodzielnym materiałem dydaktycznym: obejmują zadania konkretne, rozumowanie na modelach, poprawność zapisu, dowody proste i kontrolę błędów. Nie zastępują dowodów z części A.

## Blok 1. Liczenie i następnik

**Zadanie 1.** W pudełku jest pięć klocków. Uczeń policzył je od prawej, a drugi od lewej. Czy wyniki mogą być różne?

*Rozwiązanie.* Nie, jeśli każdy klocek wskazano dokładnie raz. Obie kolejności tworzą bijekcję z pięcioelementową listą pozycji, więc liczebność wynosi 5.

**Zadanie 2.** Są cztery jabłka; jedno wskazano dwukrotnie. Licznik pokazał 5. Znajdź błąd.

*Rozwiązanie.* Pięć oznacza liczbę wskazań, nie obiektów. Należy ponownie policzyć każde z czterech różnych jabłek dokładnie raz; wynik to 4.

**Zadanie 3.** Z pustego koszyka wyjęto wszystkie przedmioty. Ile ich pozostało?

*Rozwiązanie.* Zero. Pusty zbiór ma liczebność 0; brak przedmiotów nie jest brakiem możliwości zapisania liczby.

**Zadanie 4.** W pudełku jest 8 guzików. Dokładamy jeden nowy. Ile jest guzików i dlaczego?

*Rozwiązanie.* 9. Z Twierdzenia 2 dołożenie elementu spoza dotychczasowego zbioru zmienia liczebność z 8 na 8+1.

**Zadanie 5.** W szeregu stoją 6 osób. Ile odstępów między sąsiednimi osobami?

*Rozwiązanie.* 5. Odstępy występują między parami kolejnych osób: 1–2, 2–3, 3–4, 4–5, 5–6.

**Zadanie 6.** Na osi zaznaczono punkty od 0 do 7. Ile jest punktów, a ile jednostkowych odcinków?

*Rozwiązanie.* Punktów jest 8: 0,1,2,3,4,5,6,7. Odcinków między kolejnymi punktami jest 7.

**Zadanie 7.** Do 7 filiżanek dopasowano 7 spodków bez powtórzeń. Co można stwierdzić?

*Rozwiązanie.* Zbiory są równoliczne: utworzone przyporządkowanie jest bijekcją, a oba zbiory mają po 7 elementów.

**Zadanie 8.** Do 6 kubków dopasowano różne talerze spośród 9. Ile talerzy pozostało?

*Rozwiązanie.* Pozostały 9-6=3 talerze. Iniekcja z sześciu kubków nie obejmuje trzech talerzy.

**Zadanie 9.** Jaka liczba następuje po 29? Wyjaśnij zmianę zapisu.

*Rozwiązanie.* 30. Jedna jednostka dodana do 29 daje 30; dziesięć jednostek zamienia się w jedną dziesiątkę.


## Blok 2. Cyfry i zapis pozycyjny

**Zadanie 10.** Podaj poprzednik 1 i wyjaśnij, dlaczego 0 nie ma poprzednika w N0.

*Rozwiązanie.* Poprzednikiem 1 jest 0. Liczba -1 nie należy do N0, więc 0 nie ma poprzednika w tej dziedzinie.

**Zadanie 11.** Która liczba jest większa: 73 czy 69? Uzasadnij przez rzędy.

*Rozwiązanie.* 73>69, ponieważ cyfra dziesiątek 7 jest większa niż 6. Cyfra jedności nie może odwrócić tego porównania.

**Zadanie 12.** Porównaj 408 i 480, wskazując pierwszą różniącą się cyfrę.

*Rozwiązanie.* 408<480. Cyfry setek są równe 4; na miejscu dziesiątek mamy 0<8.

**Zadanie 13.** Rozłóż 5072 na tysiące, setki, dziesiątki i jedności.

*Rozwiązanie.* 5072=5·1000+0·100+7·10+2. Zero oznacza brak setek, ale zachowuje pozycje pozostałych cyfr.

**Zadanie 14.** Czy 0074 i 74 oznaczają różne liczby? Czy są różnymi napisami?

*Rozwiązanie.* Oba zapisy oznaczają liczbę 74. Jako ciągi znaków są różne; kanoniczny zapis liczby to 74.

**Zadanie 15.** Podaj najmniejszą i największą liczbę trzycyfrową.

*Rozwiązanie.* Najmniejsza to 100, największa 999. Wynika to z 10²≤n≤10³−1.

**Zadanie 16.** Ile liczb dwucyfrowych istnieje?

*Rozwiązanie.* Od 10 do 99 włącznie, zatem 99−10+1=90 liczb.

**Zadanie 17.** Zapisz liczbę 4009 słowami i w rozkładzie pozycyjnym.

*Rozwiązanie.* Cztery tysiące dziewięć. 4009=4·1000+0·100+0·10+9; oba zera są istotne dla pozycji.

**Zadanie 18.** Wyznacz liczbę z cyfr: 6 tysięcy, 2 setki, 0 dziesiątek, 5 jedności.

*Rozwiązanie.* 6205. Rachunek: 6·1000+2·100+0·10+5=6205.


## Blok 3. Porządek i porównywanie

**Zadanie 19.** Ułóż największą liczbę z cyfr 2, 8, 0, 5 użytych po razie.

*Rozwiązanie.* 8520. Aby zmaksymalizować wartość, umieszczamy największe cyfry od lewej: 8,5,2,0.

**Zadanie 20.** Ułóż najmniejszą czterocyfrową liczbę z cyfr 0, 1, 3, 7 użytych po razie.

*Rozwiązanie.* 1037. Pierwsza cyfra nie może być zerem; wybieramy 1, a dalej najmniejsze pozostałe: 0,3,7.

**Zadanie 21.** Porównaj 1000 i 999 bez wykonywania odejmowania.

*Rozwiązanie.* 1000>999, ponieważ pierwszy zapis ma 4 cyfry, a drugi 3, przy obu zapisach kanonicznych.

**Zadanie 22.** Porównaj 53218 i 53199 bez kalkulatora.

*Rozwiązanie.* 53218>53199: pierwsza różna cyfra od lewej to setki (2>1).

**Zadanie 23.** Zaokrąglij 342 do dziesiątek i oblicz błąd bezwzględny.

*Rozwiązanie.* 340, bo reszta z dzielenia przez 10 to 2<5. Błąd |340−342|=2.

**Zadanie 24.** Zaokrąglij 345 do dziesiątek według przyjętej reguły remisu.

*Rozwiązanie.* 350. Liczba 345 leży dokładnie pośrodku 340 i 350; w tym rozdziale remis rozstrzygamy w górę.

**Zadanie 25.** Zaokrąglij 149 do setek. Czy błąd przekracza 50?

*Rozwiązanie.* 100, bo reszta 49<50. Błąd 49 nie przekracza 50.

**Zadanie 26.** Zaokrąglij 950 do setek. Wyjaśnij regułę remisu.

*Rozwiązanie.* 1000. Odległość od 900 i 1000 jest taka sama (50), więc wybieramy większą wielokrotność 100.

**Zadanie 27.** Podaj oszacowanie liczby 378 do setek w postaci przedziału.

*Rozwiązanie.* 300≤378≤400. To poprawne granice, choć nie najwęższe; dokładniejsze to 370≤378≤380.


## Blok 4. Oszacowania i zastosowania

**Zadanie 28.** Liczba A jest między 200 a 240, B między 30 a 50. Oszacuj A+B.

*Rozwiązanie.* Dodając granice otrzymujemy 230≤A+B≤290. Wartości skrajne wynikają z Twierdzenia 11.

**Zadanie 29.** Czy suma zaokrągleń 14 i 14 do dziesiątek równa się zaokrągleniu ich sumy?

*Rozwiązanie.* Nie. Osobno: 10+10=20. Dokładna suma: 28, po zaokrągleniu do dziesiątek 30.

**Zadanie 30.** Oszacuj błąd sumy dwóch liczb zaokrąglonych do setek.

*Rozwiązanie.* Każdy błąd ma moduł najwyżej 50, więc błąd sumy nie przekracza 50+50=100.

**Zadanie 31.** Czy 99 ma większą wartość od 100, skoro suma jego cyfr jest większa?

*Rozwiązanie.* Nie. 99<100. Suma cyfr (18 wobec 1) nie wyznacza wartości liczby pozycyjnej.

**Zadanie 32.** Masz 23 patyczki. Ile pełnych wiązek po 10 i ile pojedynczych patyczków?

*Rozwiązanie.* Dwie wiązki i trzy pojedyncze patyczki: 23=2·10+3. Nie można utworzyć trzeciej pełnej wiązki.

**Zadanie 33.** Z 9 dziesiątek i 12 jedności zbuduj poprawny zapis dziesiętny.

*Rozwiązanie.* 9·10+12=102. Dziesięć z 12 jedności zamieniamy na jedną dziesiątkę; powstaje 10 dziesiątek, czyli 1 setka, 0 dziesiątek i 2 jedności.

**Zadanie 34.** Na półce jest co najmniej 17 i najwyżej 20 książek. Dokładamy dokładnie 5. Jaki jest nowy przedział?

*Rozwiązanie.* Dodajemy 5 do obu granic: 22≤liczba książek≤25.

**Zadanie 35.** Porównaj 87 i 102 na podstawie oszacowań.

*Rozwiązanie.* 87≤99<100≤102, zatem 87<102. Nie trzeba odejmować ani znać odległości na osi.

**Zadanie 36.** Uzasadnij, że 9999 jest największą liczbą czterocyfrową.

*Rozwiązanie.* Każda cyfra jest co najwyżej 9; największa suma wag to 9·1000+9·100+9·10+9=9999.


## Syntetyczne sprawdzenie rozumienia

**Problem A (dowód przez wymianę).** Uzasadnij, dlaczego przy ustalonej liczbie cyfr zamiana miejscami dwóch różnych cyfr $a>b$, gdy $a$ stoi po prawej stronie $b$, zwiększa wartość liczby.

*Rozwiązanie.* Niech $i>j$ będą numerami pozycji od prawej, z cyframi $b$ na pozycji $i$ i $a$ na pozycji $j$. Po zamianie różnica wartości wynosi $(a-b)(10^i-10^j)>0$. Wynik uzasadnia ustawianie cyfr malejąco, aby otrzymać największą liczbę, o ile nie łamiemy warunku niezerowej pierwszej cyfry.

**Problem B (odtworzenie liczby z oszacowania).** Liczba trzycyfrowa $n$ ma cyfrę setek 4, cyfrę jedności 7 i spełnia $450<n<480$. Jakie są możliwości?

*Rozwiązanie.* Ma postać $n=407+10t$, gdzie $t\in\{0,\ldots,9\}$. Warunek daje $450<407+10t<480$, czyli $43<10t<73$. Stąd $t\in\{5,6,7\}$ i $n\in\{457,467,477\}$.

**Problem C (granica metody).** Czy z samego zaokrąglenia liczby do setek, równego 500, można odzyskać liczbę dokładną?

*Rozwiązanie.* Nie. W przyjętej regule liczby naturalne od 450 do 549 włącznie zaokrąglają się do 500, czyli istnieje sto możliwych wartości. Trzeba uzyskać dodatkową informację.

**Problem D (kontrola sumy).** Dwie liczby naturalne po zaokrągleniu do dziesiątek dały 40 i 70. Podaj przedział dla ich dokładnej sumy.

*Rozwiązanie.* Pierwsza leży między 35 a 44, druga między 65 a 74 (końce włącznie, ponieważ remisy idą w górę). Suma leży więc między 100 a 118. Każda liczba z tego przedziału jest osiągalna jako suma odpowiednio dobranych liczb z podanych przedziałów.

## Kontrola merytoryczna i status

Rozdział obejmuje definicje, dowody, kontrprzykłady, ćwiczenia z rozwiązaniami i zakres ograniczeń. Twierdzenia o skończonych kolekcjach korzystają ze standardowej arytmetyki liczb naturalnych; nie są niezależną aksjomatyzacją teorii mnogości. Zaokrąglanie przy remisach jest tu jawnie zdefiniowane, gdyż inne konwencje (np. do parzystej) prowadzą do innych wyników brzegowych.

**Nie wliczać stron tego samodzielnego rozdziału do bilansu 585/1222** przed rzeczywistą integracją z monolitem 0.20, usunięciem powtórzeń i weryfikacją całego składu. Chroniony wstęp historyczny i istniejące opracowania F8–F10 pozostają bez zmian.
