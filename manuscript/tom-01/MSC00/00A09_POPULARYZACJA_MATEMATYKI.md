---
title: "Ontologia Liczby i Geometrii — Tom I"
subtitle: "MSC 00A09. Popularyzacja matematyki: od dowodu do odpowiedzialnej komunikacji"
author: "Andrzej Mikulski"
date: "2026-11-02"
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Metryka redakcyjna.** MSC2020 **00A09 — Popularization of mathematics**; rodzina A (zagadnienia ogólne), autorski poziom I; źródło: „Taksonomia Matematyki”, s. 9; minimum 4 strony. Rozdział dotyczy **przekładu wyników matematycznych na komunikaty zrozumiałe, lecz wierne warunkom twierdzeń**. Nie zastępuje kursów statystyki, prawdopodobieństwa ani modelowania z E1. Jest samodzielnym opracowaniem, a nie modyfikacją historycznego wstępu.

# 1. Język matematyczny i odpowiedzialność za twierdzenie

**D01 (twierdzenie komunikowane).** Komunikatem matematycznym nazywamy czwórkę $(H,C,U,E)$, gdzie $H$ to jawne założenia, $C$ — konkluzja, $U$ — zakres stosowalności, a $E$ — rodzaj uzasadnienia (dowód, obliczenie, symulacja albo hipoteza). Pominięcie składnika jest dopuszczalne stylistycznie, ale nie może zmieniać sensu twierdzenia.

**D02 (przykład).** Przykład jest konkretną instancją obiektu spełniającą warunki zdania. Nie stanowi dowodu zdania ogólnego, chyba że dziedzina została wyczerpana.

**D03 (kontrprzykład).** Kontrprzykład do zdania $\forall x\in S\,P(x)$ jest elementem $a\in S$ spełniającym $\neg P(a)$.

**D04 (dowód enumeracyjny).** Dowód enumeracyjny sprawdza wszystkie elementy jawnie określonej skończonej dziedziny; kontrola próbki nie jest takim dowodem.

**D05 (zmienna i jednostka).** Wielkość fizyczna jest reprezentowana przez liczbę i jednostkę. Iloraz dwóch wielkości o tych samych jednostkach jest bezwymiarowy.

**D06 (udział i punkt procentowy).** Udział $p\in[0,1]$ odpowiada $100p\%$. Zmiana z $p$ na $q$ wynosi $100(q-p)$ **punktów procentowych**, a względna zmiana, gdy $p>0$, wynosi $(q-p)/p$.

**D07 (ryzyko warunkowe).** Dla zdarzeń $A,B$ z $P(B)>0$ ryzyko $A$ w grupie $B$ to $P(A\mid B)=P(A\cap B)/P(B)$; należy podać mianownik.

**D08 (reprezentacja wykresowa).** Reprezentacja wykresowa przypisuje wartościom liczbowym pozycje, długości, pola lub barwy. Wierność reprezentacji zależy od jawnej reguły kodowania.

**D09 (skala liniowa i logarytmiczna).** Na osi liniowej różnica położeń jest proporcjonalna do $x-y$; na dodatniej osi logarytmicznej — do $\log_b(x/y)$, $b>1$.

**D10 (próba i populacja).** Populacja jest zbiorem obiektów, o których formułujemy wniosek. Próba jest podzbiorem lub losowym wyborem z populacji; reguła doboru stanowi część założeń uogólnienia.

**D11 (estymator udziału).** Dla niezależnych wskaźników Bernoulliego $X_i\in\{0,1\}$ o wspólnym parametrze $p$ estymatorem jest $\widehat p=n^{-1}\sum_{i=1}^n X_i$.

**D12 (odtwarzalność).** Wynik jest odtwarzalny obliczeniowo, gdy podano dane, reguły przekształceń, warunki brzegowe i dokładność pozwalające niezależnie uzyskać ten sam rezultat.

**D13 (ograniczenie wniosku).** Ograniczenie to jawny warunek, poza którym wynik nie musi obowiązywać, np. dodatniość mianownika, niezależność obserwacji lub losowość doboru próby.

**D14 (metadane wyniku).** Minimalne metadane tabeli lub wykresu obejmują źródło, datę, definicję zmiennej, jednostkę, mianownik, sposób agregacji oraz informację o niepewności, gdy występuje.

# 2. Co wolno wnioskować z przykładów i obliczeń

**T01 (jeden kontrprzykład wystarcza).** Jeżeli istnieje $a\in S$ takie, że $\neg P(a)$, to zdanie $\forall x\in S\,P(x)$ jest fałszywe.

*Dowód.* Gdyby zdanie ogólne było prawdziwe, obowiązywałoby w szczególności dla $x=a$, co przeczy $\neg P(a)$. $\square$

**T02 (skończona weryfikacja).** Jeśli $S=\{s_1,\ldots,s_m\}$ i dla każdego $i$ sprawdzono $P(s_i)$, to $\forall x\in S\,P(x)$.

*Dowód.* Każdy $x\in S$ jest jednym z wymienionych $s_i$; dla tego indeksu zdanie zostało sprawdzone. Założenie, że wyliczenie obejmuje całe $S$, jest konieczne. $\square$

**T03 (niewystarczalność próbki).** Dla dowolnego skończonego $F\subset\mathbb N$ istnieją funkcje $f,g:\mathbb N\to\{0,1\}$ zgodne na $F$, lecz różne poza $F$.

*Dowód.* Niech $f(n)=0$ dla wszystkich $n$. Ponieważ $\mathbb N$ jest nieskończony, wybierzmy $k\notin F$ i określmy $g(k)=1$, a $g(n)=0$ dla $n\ne k$. Wtedy $f|_F=g|_F$, ale $f(k)\ne g(k)$. $\square$

**T04 (zmiana procentowa nie jest odwracalna przez przeciwny procent).** Dla $x>0$ i $0<p<1$ wzrost o $100p\%$, a następnie spadek o $100p\%$ daje $x(1-p^2)<x$.

*Dowód.* Pierwsza operacja mnoży przez $1+p$, druga przez $1-p$. Iloczyn to $1-p^2<1$. $\square$

**T05 (punkty procentowe a wzrost względny).** Dla $0<p<q\le1$ wzrost udziału wynosi $100(q-p)$ punktów procentowych, ale względny wzrost to $100(q-p)/p\%$.

*Dowód.* Pierwsza liczba jest różnicą na skali $0$–$100\%$. Druga jest ilorazem przyrostu i wartości początkowej; definicje dają wzory bez dodatkowych założeń. $\square$

**T06 (granica błędu zaokrąglenia).** Jeżeli rzeczywisty udział w procentach $u$ zaokrąglono do najbliższej liczby całkowitej $r$, to $|u-r|\le 0{,}5$ punktu procentowego; dla remisu obowiązuje ustalona reguła.

*Dowód.* Przedział liczb zaokrąglanych do $r$ jest zawarty w $[r-\tfrac12,r+\tfrac12]$. $\square$

# 3. Wykresy, skale i proporcje

**T07 (odczyt stosunku na osi logarytmicznej).** Dla $x,y>0$ i $b>1$ zachodzi $\log_b x-\log_b y=\log_b(x/y)$. Równe odległości na osi logarytmicznej odpowiadają równym ilorazom, nie równym różnicom.

*Dowód.* Z własności logarytmu ilorazu otrzymujemy równość. Dla stałej odległości $d$ zachodzi $x/y=b^d$. $\square$

**T08 (pole symbolu kołowego).** Jeśli promień koła reprezentującego wartość $x>0$ jest proporcjonalny do $x$, to jego pole jest proporcjonalne do $x^2$, a nie do $x$.

*Dowód.* Dla $r=kx$ pole wynosi $A=\pi r^2=\pi k^2x^2$. Aby pole było proporcjonalne do $x$, należy przyjąć $r=k\sqrt{x}$. $\square$

**T09 (zależność słupka od początku osi).** Dla dwóch wartości $0\le a<b$ i osi słupkowej rozpoczynającej się w $c<a$, stosunek długości słupków wynosi $(b-c)/(a-c)$; na osi od zera jest równy $b/a$ (dla $a>0$).

*Dowód.* Długość słupka to różnica wartości i punktu startowego, pomnożona przez wspólną dodatnią skalę. Po skróceniu skali dostajemy wzory. Zmiana $c$ może silnie zmienić wizualny stosunek. $\square$

**T10 (jednostki nie znikają przez opis).** Jeżeli $d$ ma jednostkę długości, a $t$ czasu, to iloraz $d/t$ ma jednostkę długości na czas. Nie można poprawnie dodać $d+t$ bez dodatkowej reguły przekształcenia jednostek.

*Dowód.* Przy zmianie jednostki długości o czynnik $\lambda$ liczba reprezentująca $d$ zmienia się o ten czynnik, natomiast liczba reprezentująca $t$ nie. Suma $d+t$ nie zachowuje niezależnego znaczenia fizycznego przy takiej zmianie. Iloraz ma jednoznaczną jednostkę pochodną. $\square$

# 4. Prawdopodobieństwo i ryzyko w komunikacji

**T11 (wzór Bayesa dla dodatniego testu).** Niech $D$ oznacza stan występujący z częstością $p$, czułość testu wynosi $s=P(+\mid D)$, a swoistość $c=P(-\mid\neg D)$. Gdy $sp+(1-c)(1-p)>0$,
$$
P(D\mid +)=\frac{sp}{sp+(1-c)(1-p)}.
$$

*Dowód.* Licznik $P(D\cap +)=P(+\mid D)P(D)=sp$. Mianownik $P(+)=sp+(1-c)(1-p)$ z rozłącznego podziału na $D$ i $\neg D$. Stosujemy definicję prawdopodobieństwa warunkowego. $\square$

**T12 (możliwy paradoks agregacji).** Istnieją dwie grupy, w każdej z których udział sukcesów metody A przewyższa udział metody B, choć po połączeniu grup udział A jest mniejszy od udziału B.

*Dowód przez konstrukcję.* W grupie 1 metoda A daje 9 sukcesów na 10 prób, B — 80 na 100, więc $90\%>80\%$. W grupie 2 A daje 10 na 100, B — 0 na 10, więc $10\%>0\%$. Po złączeniu A ma $19/110\approx17{,}27\%$, B ma $80/110\approx72{,}73\%$. Odwrócenie wynika z nierównych wag grup, a nie z błędu arytmetycznego. $\square$

**T13 (oszacowanie błędu częstości z próby).** Jeśli $X_1,\ldots,X_n$ są niezależnymi zmiennymi Bernoulliego o wspólnym parametrze $p$, to dla każdego $\varepsilon>0$
$$
P(|\widehat p-p|\ge\varepsilon)\le \frac{1}{4n\varepsilon^2}.
$$

*Dowód.* $E\widehat p=p$, a przez niezależność $\operatorname{Var}(\widehat p)=p(1-p)/n\le1/(4n)$, ponieważ $p(1-p)\le1/4$. Nierówność Czebyszewa daje tezę. Nie jest to automatycznie przedział ufności dla próby nielosowej. $\square$

**T14 (granica sumy ryzyk).** Dla dowolnych zdarzeń $A_1,\ldots,A_m$ zachodzi
$$
P\left(\bigcup_{i=1}^m A_i\right)\le\sum_{i=1}^m P(A_i).
$$

*Dowód.* Wskaźnik sumy zdarzeń jest punktowo nie większy od sumy ich wskaźników. Biorąc wartości oczekiwane obu stron, otrzymujemy nierówność. Niezależność nie jest wymagana. $\square$

# 5. Kontrprzykłady do popularnych skrótów myślowych

**K01. „Sprawdziłem tysiąc liczb, więc twierdzenie jest prawdziwe”.** Dla dowolnego $N$ funkcja $f(n)=0$ dla $n\le N$ i $f(N+1)=1$ przeczy temu wnioskowaniu (T03).

**K02. „Wzrost o 20% i spadek o 20% się znoszą”.** $100\mapsto120\mapsto96$, nie $100$.

**K03. „Z 2% do 4% to wzrost o 2%”.** To wzrost o 2 punkty procentowe, ale o 100% względnie.

**K04. „Dwa razy większy promień oznacza dwa razy większe koło”.** Pole rośnie czterokrotnie (T08).

**K05. „Dodatni test oznacza 99% prawdopodobieństwa stanu, jeśli czułość wynosi 99%”.** Przy częstości $1\%$, czułości $99\%$ i swoistości $95\%$ prawdopodobieństwo po dodatnim wyniku wynosi $1/6$, nie $99\%$.

**K06. „Jeżeli A jest lepsza w każdej grupie, musi być lepsza w sumie”.** T12 daje jawny kontrprzykład przy nierównych wagach.

**K07. „Na wykresie logarytmicznym odległość 1–10 oznacza ten sam przyrost co 10–100”.** Obie odległości oznaczają mnożenie przez 10, lecz przyrosty to odpowiednio 9 i 90.

**K08. „Wielka liczba odpowiedzi internetowych to reprezentatywna próba”.** Jeśli w populacji jest 100 osób, z czego 10 należy do grupy X, a formularz wypełnia tylko 10 osób z X, udział w odpowiedziach wynosi 100%, choć w populacji 10%. Brak losowego doboru unieważnia uogólnienie.

**K09. „Korelacja zawsze dowodzi przyczynowości”.** Niech $Z$ będzie uczciwym rzutem monetą, a $X=Z$, $Y=Z$. Zmienne $X,Y$ są doskonale skorelowane, lecz model z wspólną przyczyną $Z$ nie zawiera strzałki przyczynowej $X\to Y$.

**K10. „0% ryzyka w próbie dowodzi zerowego ryzyka”.** Przy prawdziwym ryzyku $p=0{,}01$ prawdopodobieństwo braku zdarzeń w 10 niezależnych próbach wynosi $(0{,}99)^{10}>0$.

# 6. Zadania rozwiązane — laboratorium komunikacji

**Z01.** Popularny wpis głosi: „Wszystkie liczby nieparzyste są pierwsze; sprawdzono 3, 5, 7”. *Rozwiązanie:* $9$ jest nieparzyste i złożone ($9=3\cdot3$). Jeden kontrprzykład obala zdanie.

**Z02.** Wyjaśnij, kiedy komputerowy przegląd stanowi dowód. *Rozwiązanie:* dla jawnie wyliczonego skończonego $S$, gdy sprawdzono wszystkie elementy i poprawność programu; dla nieskończonej dziedziny bez dodatkowego argumentu nie.

**Z03.** Cena 200 zł rośnie o 10%, a potem maleje o 10%. *Rozwiązanie:* $200\cdot1{,}1\cdot0{,}9=198$ zł; ubytek 2 zł, czyli 1%.

**Z04.** Udział wzrósł z 12% do 15%. *Rozwiązanie:* o 3 punkty procentowe; względnie o $(15-12)/12=25\%$.

**Z05.** Wynik 37,49% opublikowano jako 37%. *Rozwiązanie:* błąd to 0,49 punktu procentowego. Nie wolno twierdzić, że błąd względny to 0,49%.

**Z06.** Koła na infografice mają promienie 2 cm i 4 cm. *Rozwiązanie:* pola to $4\pi$ i $16\pi$ cm², więc drugi symbol zajmuje cztery razy większe pole.

**Z07.** Na osi słupków od 90 wartości 95 i 100 mają długości 5 i 10. *Rozwiązanie:* stosunek wizualny to 2, podczas gdy stosunek wartości wynosi $100/95\approx1{,}0526$.

**Z08.** Porównaj na osi logarytmicznej 2, 20 i 200. *Rozwiązanie:* odległości między kolejnymi wartościami są równe, ponieważ obie pary mają stosunek 10; różnice wynoszą 18 i 180.

**Z09.** Samochód przejeżdża 150 km w 2,5 h. *Rozwiązanie:* $150/2{,}5=60$ km/h. Liczba 60 bez jednostki nie jest kompletną odpowiedzią.

**Z10.** Dla częstości 1%, czułości 99% i swoistości 95% policz szansę stanu po wyniku dodatnim. *Rozwiązanie:* $0{,}0099/(0{,}0099+0{,}0495)=1/6\approx16{,}67\%$.

**Z11.** W grupach A i B porównaj metody na danych T12. *Rozwiązanie:* A jest lepsza w każdej grupie (90% > 80%, 10% > 0%), lecz po agregacji B ma wyższy udział (72,73% > 17,27%). Należy publikować liczebności i zasady ważenia.

**Z12.** Dla $n=400$ i $\varepsilon=0{,}1$ oszacuj ryzyko błędu częstości co najmniej 10 punktów procentowych. *Rozwiązanie:* T13 daje górne ograniczenie $1/(4\cdot400\cdot0{,}01)=1/16=6{,}25\%$, przy niezależności i wspólnym $p$.

**Z13.** Trzy możliwe błędy mają prawdopodobieństwa nie większe niż 0,01, 0,02 i 0,03. *Rozwiązanie:* prawdopodobieństwo co najmniej jednego błędu jest nie większe niż 0,06 (T14), nawet bez niezależności.

**Z14.** W 10 próbach nie zaobserwowano wypadku. Czy dowodzi to ryzyka 0? *Rozwiązanie:* nie. Przy ryzyku 1% na próbę brak zdarzeń ma prawdopodobieństwo $0{,}99^{10}\approx90{,}44\%$.

**Z15.** Wykres kołowy ma reprezentować udziały 25% i 75%. *Rozwiązanie:* kąty sektorów wynoszą $90^\circ$ i $270^\circ$; suma to $360^\circ$. Pole całego koła nie zmienia się wraz z udziałem.

**Z16.** Zaprojektuj minimalny opis wyników „40 na 50 osób odpowiedziało TAK”. *Rozwiązanie:* udział $40/50=80\%$; należy podać pytanie, datę, populację, sposób doboru 50 respondentów, ewentualne braki odpowiedzi i brak podstaw do uogólnienia na populację bez reprezentatywnego doboru.

**Z17.** Podaj dwa różne wnioski z tej samej liczby „50”. *Rozwiązanie:* „50 osób” to liczność; „50%” to udział i wymaga mianownika. Przy 50 z 100 jest 50%, przy 50 z 1000 jest 5%.

**Z18.** Przepisz komunikat „Model dowodzi, że jutro będzie 20°C”. *Rozwiązanie:* „Przy podanych danych wejściowych i założeniach model przewiduje 20°C; prognoza jest obarczona niepewnością”. Obliczenie modelowe nie jest dowodem obserwacji przyszłej.

# 7. Procedura redakcyjna i granice metody

Dla każdej popularnonaukowej tezy redaktor sprawdza kolejno: **(1)** dziedzinę i kwantyfikatory, **(2)** jednostki i mianowniki, **(3)** rodzaj uzasadnienia, **(4)** reprezentatywność próby, **(5)** skalę wykresu, **(6)** niepewność, **(7)** możliwość skonstruowania kontrprzykładu, **(8)** odtwarzalność rachunku. Ten protokół nie zastępuje recenzji naukowej ani nie przekształca symulacji w dowód.

**Ograniczenie.** T13 wymaga niezależnych obserwacji Bernoulliego o tym samym parametrze. T11 wymaga określonej częstości bazowej i jakości testu. T12 dowodzi możliwości paradoksu agregacji, nie jego nieuchronności. Pojęcia przyczynowości w K09 są ilustracją modelu, nie twierdzeniem o każdej korelacji.

**Bibliografia i punkty odniesienia:** MSC2020, klasyfikacja 00A09 (Mathematical Reviews / zbMATH); G. Pólya, *How to Solve It* (1945); J. Allen Paulos, *Innumeracy* (1988); E. Tufte, *The Visual Display of Quantitative Information* (1983); D. Spiegelhalter, *The Art of Statistics* (2019). Bibliografia jest orientacją metodologiczną; wszystkie rachunki i dowody w tym rozdziale zapisano samodzielnie.

**Status wydawniczy:** samodzielny materiał Tomu I. Nie jest integracją z kanonicznym monolitem 0.20; licznik 585 stron pozostaje bez zmian. Bez finalnego spisu treści i bez Tomu II.
