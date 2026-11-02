---
title: "Ontologia Liczby — Tom I"
subtitle: "E1-10. Prawdopodobieństwo elementarne: przestrzeń zdarzeń, rachunek i pułapki intuicji"
author: "Andrzej Mikulski"
date: "2026-11-02"
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Pozycja taksonomiczna:** E1-10, poziom I, po E1-09 (statystyka opisowa), przed E1-11 (modelowanie). **Status:** samodzielny materiał źródłowy do przyszłej integracji z monolitem 0.20; nie zastępuje wcześniejszych rozdziałów ani wstępu historycznego. Podstawowy model jest skończony. Wszędzie odróżniamy wynik doświadczenia od zdarzenia, a losowość od braku wiedzy o deterministycznym mechanizmie.

# A. Fundamenty i definicje

**D1 (doświadczenie i wynik).** Doświadczenie losowe ma ustalony zbiór możliwych wyników elementarnych $\Omega$. Wynik to pojedynczy element $\omega\in\Omega$. Słowo „losowe” opisuje model niepewności, nie musi oznaczać fizycznego braku determinizmu.

**D2 (przestrzeń skończona).** W tym rozdziale $\Omega$ jest niepustym zbiorem skończonym. Zdarzenie to podzbiór $A\subseteq\Omega$. Zdarzenie pewne to $\Omega$, niemożliwe to $\varnothing$.

**D3 (zdarzenia złożone).** $A\cup B$ oznacza „$A$ lub $B$”, $A\cap B$ oznacza „$A$ i $B$”, a $A^c=\Omega\setminus A$ oznacza „nie $A$”. Różnica $A\setminus B$ oznacza „$A$, ale nie $B$”.

**D4 (rozkład prawdopodobieństwa).** Funkcja wag $p:\Omega\to[0,1]$ spełnia $\sum_{\omega\in\Omega}p(\omega)=1$. Definiujemy $P(A)=\sum_{\omega\in A}p(\omega)$. Wagi mogą być różne; jednakowa liczba wyników nie wystarcza do ich jednakowej szansy.

**D5 (model klasyczny).** Jeśli każdy wynik jest jednakowo prawdopodobny, $p(\omega)=1/|\Omega|$, to $P(A)=|A|/|\Omega|$. Jest to szczególny przypadek D4, nie uniwersalna definicja prawdopodobieństwa.

**D6 (rozłączność).** Zdarzenia $A,B$ są rozłączne, gdy $A\cap B=\varnothing$. Nie mogą zajść równocześnie.

**D7 (próba z powtórzeniami).** Przy $n$ niezależnych rzutach uczciwą monetą przestrzeń wyników to $\{O,R\}^n$, zawierająca $2^n$ równoprawdopodobnych ciągów. Kolejność rzutów jest istotna.

**D8 (warunkowanie).** Gdy $P(B)>0$, $P(A\mid B)=P(A\cap B)/P(B)$. Warunkowanie zmienia rozkład odniesienia na wyniki należące do $B$.

**D9 (niezależność).** Zdarzenia $A,B$ są niezależne, jeśli $P(A\cap B)=P(A)P(B)$. Gdy $P(B)>0$, jest to równoważne $P(A\mid B)=P(A)$.

**D10 (liczba sprzyjających par).** Dla dwóch rozróżnialnych kostek wynik to para uporządkowana $(i,j)$ z $\{1,\ldots,6\}^2$. Jest 36 par, a nie 11 równie prawdopodobnych sum.

**D11 (losowanie bez zwracania).** Kolejne elementy pobieramy z ustalonego zbioru bez odkładania; szanse następnych wyborów mogą zależeć od wcześniejszych wyników.

**D12 (zmienna losowa).** Funkcja $X:\Omega\to\mathbb R$ przypisuje każdemu wynikowi liczbę. Zdarzenie $X=x$ to $\{\omega:X(\omega)=x\}$.

**D13 (wartość oczekiwana).** Dla skończonej przestrzeni $E[X]=\sum_{\omega\in\Omega}X(\omega)p(\omega)$. Jest to średnia ważona w modelu, nie obietnica wyniku pojedynczej próby.

**D14 (partycja).** Rodzina $B_1,\ldots,B_k$ jest partycją $\Omega$, gdy zdarzenia są parami rozłączne i ich suma zbiorowa równa się $\Omega$.

**D15 (zdarzenie co najmniej raz).** W serii prób „co najmniej jeden sukces” jest dopełnieniem „ani jednego sukcesu”. Ułatwia to rachunek przy niezależnych powtórzeniach.

**D16 (częstość empiryczna).** Po $n$ wykonaniach doświadczenia częstość zdarzenia $A$ wynosi $N_n(A)/n$. Sama obserwowana częstość nie jest logicznym dowodem równości z teoretycznym $P(A)$.

# B. Twierdzenia i dowody

**T1 (normalizacja).** $P(\varnothing)=0$ oraz $P(\Omega)=1$.

*Dowód.* Suma po zbiorze pustym wynosi zero. Suma wszystkich wag jest równa jeden z D4. $\square$

**T2 (addytywność rozłączna).** Jeśli $A\cap B=\varnothing$, to $P(A\cup B)=P(A)+P(B)$.

*Dowód.* Każdy wynik sumy zbiorowej należy dokładnie do jednego ze zbiorów, więc suma jego wagi występuje dokładnie raz. $\square$

**T3 (dopełnienie).** Dla każdego $A$, $P(A^c)=1-P(A)$.

*Dowód.* $A$ i $A^c$ są rozłączne, a ich suma zbiorowa to $\Omega$. Z T1–T2: $1=P(A)+P(A^c)$. $\square$

**T4 (monotoniczność).** Jeśli $A\subseteq B$, to $P(A)\le P(B)$.

*Dowód.* $B=A\cup(B\setminus A)$, a składniki są rozłączne. Ponieważ $P(B\setminus A)\ge0$, otrzymujemy nierówność. $\square$

**T5 (włączenia i wyłączenia).** $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.

*Dowód.* Rozbijamy $A\cup B$ na trzy rozłączne części $A\setminus B$, $B\setminus A$ i $A\cap B$. Dodając $P(A)$ i $P(B)$, część wspólną liczymy dwa razy, więc trzeba ją odjąć raz. $\square$

**T6 (ograniczenie sumy).** $P(A\cup B)\le P(A)+P(B)$.

*Dowód.* Z T5 odejmujemy nieujemne $P(A\cap B)$. $\square$

**T7 (różnica).** $P(A\setminus B)=P(A)-P(A\cap B)$.

*Dowód.* $A=(A\setminus B)\cup(A\cap B)$ jest sumą rozłączną. $\square$

**T8 (warunkowe mnożenie).** Dla $P(B)>0$, $P(A\cap B)=P(A\mid B)P(B)$.

*Dowód.* Mnożymy obie strony definicji D8 przez dodatnie $P(B)$. $\square$

**T9 (symetria niezależności).** Jeśli $A$ i $B$ są niezależne, to $A^c$ i $B$ także są niezależne.

*Dowód.* $P(A^c\cap B)=P(B)-P(A\cap B)=P(B)(1-P(A))=P(A^c)P(B)$. $\square$

**T10 (niemożliwość rozłącznej niezależności).** Jeśli $A,B$ są rozłączne i mają dodatnie prawdopodobieństwa, to nie są niezależne.

*Dowód.* Rozłączność daje $P(A\cap B)=0$, ale $P(A)P(B)>0$. $\square$

**T11 (co najmniej jeden sukces).** Jeśli $n$ prób jest niezależnych, a prawdopodobieństwo sukcesu w każdej wynosi $p$, to prawdopodobieństwo co najmniej jednego sukcesu wynosi $1-(1-p)^n$.

*Dowód.* Zdarzenie przeciwne to brak sukcesu we wszystkich $n$ próbach. Niezależność daje prawdopodobieństwo $(1-p)^n$; stosujemy T3. $\square$

**T12 (dokładnie jeden sukces w dwóch próbach).** Dla dwóch niezależnych prób o tej samej szansie sukcesu $p$, prawdopodobieństwo dokładnie jednego sukcesu to $2p(1-p)$.

*Dowód.* Rozłączne możliwości to sukces–porażka i porażka–sukces. Każda ma prawdopodobieństwo $p(1-p)$. $\square$

**T13 (prawo całkowitego prawdopodobieństwa).** Dla partycji $B_1,\ldots,B_k$ z $P(B_i)>0$, $P(A)=\sum_i P(A\mid B_i)P(B_i)$.

*Dowód.* Zdarzenia $A\cap B_i$ są rozłączne i ich suma to $A$. Stosujemy T2 i T8. $\square$

**T14 (wzór Bayesa).** Jeśli $P(A)>0$ i $B_i$ są jak w T13, to
$$P(B_j\mid A)=\frac{P(A\mid B_j)P(B_j)}{\sum_i P(A\mid B_i)P(B_i)}.$$

*Dowód.* Z definicji $P(B_j\mid A)=P(A\cap B_j)/P(A)$; licznik przepisujemy T8, mianownik T13. $\square$

**T15 (losowanie dwóch elementów bez zwracania).** W urnie jest $r$ czerwonych i $b$ niebieskich kul, $r+b\ge2$. Prawdopodobieństwo dwóch czerwonych przy losowaniu bez zwracania to $\frac{r}{r+b}\frac{r-1}{r+b-1}$, jeśli $r\ge1$.

*Dowód.* Pierwsza kula jest czerwona z szansą $r/(r+b)$. Warunkowo po jej wyjęciu pozostaje $r-1$ czerwonych wśród $r+b-1$ kul. Stosujemy T8. Dla $r=1$ wynik wynosi zero. $\square$

**T16 (liniowość wartości oczekiwanej).** Dla zmiennych losowych $X,Y$ i stałych $a,b$, $E[aX+bY]=aE[X]+bE[Y]$.

*Dowód.* Rozdzielamy skończoną sumę $\sum_\omega (aX(\omega)+bY(\omega))p(\omega)$. Nie jest potrzebna niezależność. $\square$

**T17 (wartość oczekiwana wskaźnika).** Dla $I_A(\omega)=1$ przy $\omega\in A$ i $0$ poza $A$, zachodzi $E[I_A]=P(A)$.

*Dowód.* W definicji D13 pozostają tylko wagi wyników należących do $A$. $\square$

**T18 (liczba sukcesów).** Dla $n$ prób, z których każda ma prawdopodobieństwo sukcesu $p$, oczekiwana liczba sukcesów wynosi $np$, nawet jeśli próby są zależne.

*Dowód.* Liczba sukcesów to suma $n$ wskaźników. Z T16–T17 $E[\sum_i I_i]=\sum_i p=np$. $\square$

**T19 (ograniczenie zdarzenia).** Dla dowolnych $A,B$ zachodzi $\max(P(A),P(B))\le P(A\cup B)\le\min(1,P(A)+P(B))$.

*Dowód.* Lewa nierówność wynika z T4, prawa z T6 oraz $P(A\cup B)\le P(\Omega)=1$. $\square$

**T20 (co najmniej jedno trafienie przy losowaniu bez zwracania).** Jeśli spośród $N$ obiektów $K$ jest wyróżnionych i losujemy $n\le N$ bez zwracania, to prawdopodobieństwo braku wyróżnionego wynosi $\binom{N-K}{n}/\binom Nn$ przy konwencji $\binom{m}{n}=0$ dla $n>m$.

*Dowód.* Wszystkie $n$-elementowe podzbiory są równoprawdopodobne. Wśród $\binom Nn$ podzbiorów dokładnie $\binom{N-K}n$ nie zawiera wyróżnionego obiektu. $\square$

# C. Kontrprzykłady i kontrola założeń

**K1.** Dwie kostki nie dają 11 jednakowo prawdopodobnych sum: suma 7 ma 6 reprezentacji, suma 2 tylko jedną.

**K2.** Zdarzenia rozłączne nie muszą być niezależne: w rzucie kostką $A=\{1\}$, $B=\{2\}$ mają iloczyn prawdopodobieństw $1/36$, a część wspólna ma prawdopodobieństwo 0.

**K3.** Zdarzenia niezależne nie muszą być rozłączne: przy dwóch rzutach monetą $A=$ „pierwszy orzeł”, $B=$ „drugi orzeł”; część wspólna ma szansę $1/4$.

**K4.** $P(A\cup B)$ nie musi równać się $P(A)+P(B)$: dla $A=B=\Omega$ lewa strona wynosi 1, prawa 2.

**K5.** $P(A\mid B)$ nie musi być równe $P(B\mid A)$: w kostce $A=\{1\}$, $B=\{1,2\}$ dają odpowiednio $1/2$ i $1$.

**K6.** Dwa rzuty monetą mają cztery, nie trzy równoprawdopodobne uporządkowane wyniki; „jedna reszka i jeden orzeł” ma dwa ustawienia.

**K7.** W losowaniu bez zwracania szanse się zmieniają: przy dwóch kulach różnych kolorów, po czerwonej następna musi być niebieska.

**K8.** Średnia oczekiwana nie musi być możliwym wynikiem: uczciwa kostka ma $E[X]=3{,}5$, choć na ściankach są tylko liczby całkowite.

**K9.** Z obserwacji trzech orłów z rzędu nie wynika, że czwarty rzut uczciwą monetą musi dać reszkę.

**K10.** Samo stwierdzenie „dwa wyniki” nie oznacza szansy $1/2$ dla każdego: wynik „6” i „nie 6” w rzucie kostką mają szanse $1/6$ i $5/6$.

**K11.** Jeśli $P(B)=0$, iloraz $P(A\cap B)/P(B)$ jest niezdefiniowany; nie wolno stosować D8 bez warunku.

**K12.** Częstość 7 sukcesów na 10 prób nie dowodzi, że $p=0{,}7$; to estymata, a nie tożsamość logiczna.

# D. Zadania rozwiązane

## D1. Jedna kostka i jedna moneta

**Z1.** Kostka: szansa parzystej liczby? *Rozwiązanie:* $\{2,4,6\}$, więc $3/6=1/2$.

**Z2.** Kostka: liczba większa niż 4? *Rozwiązanie:* $\{5,6\}$, więc $2/6=1/3$.

**Z3.** Kostka: liczba pierwsza? *Rozwiązanie:* $\{2,3,5\}$, więc $1/2$.

**Z4.** Kostka: liczba jednocześnie parzysta i pierwsza? *Rozwiązanie:* tylko 2, więc $1/6$.

**Z5.** Kostka: liczba nie większa niż 6? *Rozwiązanie:* zdarzenie pewne, $P=1$.

**Z6.** Kostka: liczba 7? *Rozwiązanie:* zdarzenie niemożliwe, $P=0$.

**Z7.** Moneta uczciwa: orzeł? *Rozwiązanie:* $1/2$.

**Z8.** Moneta: dwa orły w dwóch rzutach? *Rozwiązanie:* jeden z czterech ciągów, $1/4$.

**Z9.** Moneta: dokładnie jeden orzeł w dwóch rzutach? *Rozwiązanie:* $OR,RO$, więc $2/4=1/2$.

**Z10.** Moneta: co najmniej jeden orzeł w trzech rzutach? *Rozwiązanie:* $1-(1/2)^3=7/8$.

**Z11.** Moneta: ani jednej reszki w czterech rzutach? *Rozwiązanie:* tylko $OOOO$, więc $1/16$.

**Z12.** Kostka: parzysta lub większa niż 4? *Rozwiązanie:* $\{2,4,5,6\}$, więc $4/6=2/3$.

## D2. Dwie kostki

**Z13.** Suma 2? *Rozwiązanie:* tylko $(1,1)$, $1/36$.

**Z14.** Suma 7? *Rozwiązanie:* $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$, więc $6/36=1/6$.

**Z15.** Suma 12? *Rozwiązanie:* tylko $(6,6)$, $1/36$.

**Z16.** Dwie jednakowe liczby? *Rozwiązanie:* sześć par $(i,i)$, $6/36=1/6$.

**Z17.** Co najmniej jedna szóstka? *Rozwiązanie:* $1-(5/6)^2=11/36$.

**Z18.** Obie liczby parzyste? *Rozwiązanie:* $(3/6)^2=1/4$.

**Z19.** Dokładnie jedna szóstka? *Rozwiązanie:* $2(1/6)(5/6)=10/36=5/18$.

**Z20.** Pierwsza liczba większa od drugiej? *Rozwiązanie:* 15 par, tyle samo odwrotnych; 6 remisów, zatem $15/36=5/12$.

**Z21.** Suma parzysta? *Rozwiązanie:* obie parzyste albo obie nieparzyste: $1/4+1/4=1/2$.

**Z22.** Iloczyn nieparzysty? *Rozwiązanie:* obie liczby nieparzyste: $1/4$.

**Z23.** Suma co najmniej 11? *Rozwiązanie:* sumy 11 i 12 mają 2+1 pary, więc $3/36=1/12$.

**Z24.** Suma 7 pod warunkiem, że pierwsza kostka pokazała 2? *Rozwiązanie:* druga musi pokazać 5, więc $1/6$.

## D3. Urny i karty

**Z25.** Urna 3 czerwone, 2 niebieskie; jedna czerwona? *Rozwiązanie:* $3/5$.

**Z26.** Z tej urny dwie czerwone bez zwracania? *Rozwiązanie:* $(3/5)(2/4)=3/10$.

**Z27.** Dwie niebieskie bez zwracania? *Rozwiązanie:* $(2/5)(1/4)=1/10$.

**Z28.** Dokładnie jedna czerwona w dwóch losowaniach bez zwracania? *Rozwiązanie:* $2(3/5)(2/4)=3/5$.

**Z29.** Co najmniej jedna czerwona? *Rozwiązanie:* $1-(2/5)(1/4)=9/10$.

**Z30.** Dwie czerwone ze zwracaniem? *Rozwiązanie:* $(3/5)^2=9/25$.

**Z31.** Talia 52 kart: as? *Rozwiązanie:* $4/52=1/13$.

**Z32.** Talia 52 kart: kier? *Rozwiązanie:* $13/52=1/4$.

**Z33.** As lub kier? *Rozwiązanie:* $(4+13-1)/52=4/13$.

**Z34.** Dwie karty bez zwracania, obie asy? *Rozwiązanie:* $(4/52)(3/51)=1/221$.

**Z35.** Z talii karta niebędąca asem? *Rozwiązanie:* $48/52=12/13$.

**Z36.** Trzy czerwone z urny 4 czerwone, 2 niebieskie, bez zwracania? *Rozwiązanie:* $(4/6)(3/5)(2/4)=1/5$.

## D4. Warunkowanie, decyzje i wartość oczekiwana

**Z37.** Kostka: liczba parzysta, gdy wiadomo, że jest większa od 3? *Rozwiązanie:* warunek $\{4,5,6\}$, sprzyjają $\{4,6\}$, zatem $2/3$.

**Z38.** Kostka: liczba większa od 3, gdy wiadomo, że jest parzysta? *Rozwiązanie:* $\{2,4,6\}$, sprzyjają $\{4,6\}$, zatem $2/3$.

**Z39.** Kostka: liczba pierwsza, gdy wiadomo, że jest nieparzysta? *Rozwiązanie:* warunek $\{1,3,5\}$, sprzyjają $\{3,5\}$, zatem $2/3$.

**Z40.** Kostka: czy zdarzenia „parzysta” i „większa niż 3” są niezależne? *Rozwiązanie:* $P(A\cap B)=2/6=1/3$, a $P(A)P(B)=1/4$; nie.

**Z41.** Dwa niezależne rzuty: szansa drugiego orła pod warunkiem pierwszego orła? *Rozwiązanie:* $1/2$.

**Z42.** Rzut uczciwą kostką: $E[X]$? *Rozwiązanie:* $(1+2+3+4+5+6)/6=7/2$.

**Z43.** Uczciwa moneta: $X=1$ za orła, $X=0$ za reszkę. *Rozwiązanie:* $E[X]=1/2$.

**Z44.** Gra: z prawdopodobieństwem $1/4$ zysk 12 zł, inaczej strata 4 zł. *Rozwiązanie:* $E[X]=(1/4)12+(3/4)(-4)=0$ zł.

**Z45.** Cztery próby, każda z szansą sukcesu $1/3$: oczekiwana liczba sukcesów? *Rozwiązanie:* $4/3$, niezależność nie jest potrzebna.

**Z46.** Trzy niezależne próby o szansie sukcesu $1/5$: co najmniej jeden sukces? *Rozwiązanie:* $1-(4/5)^3=61/125$.

**Z47.** Dwie niezależne próby o szansie sukcesu $2/5$: dokładnie jeden? *Rozwiązanie:* $2(2/5)(3/5)=12/25$.

**Z48.** 100 losów, 5 wygrywających; jeden los? *Rozwiązanie:* $5/100=1/20$.

**Z49.** Z tych samych 100 losów losujemy 2 bez zwracania: co najmniej jedna wygrana? *Rozwiązanie:* $1-(95/100)(94/99)=97/990$.

**Z50.** Wybór z $\{1,\ldots,10\}$: liczba podzielna przez 2 lub 5? *Rozwiązanie:* wielokrotności 2: 5, wielokrotności 5: 2, wspólna 10: 1, więc $(5+2-1)/10=3/5$.

**Z51.** Przy dwóch uczciwych rzutach monetą czy zdarzenia „pierwszy orzeł” i „dokładnie jeden orzeł” są niezależne? *Rozwiązanie:* część wspólna $\{OR\}$ ma szansę $1/4$; iloczyn szans $1/2\cdot1/2=1/4$, więc tak.

**Z52.** Przy trzech rzutach monetą: dokładnie trzy orły? *Rozwiązanie:* tylko $OOO$, więc $1/8$.

## D5. Problemy syntetyczne

**Problem P1 (błąd hazardzisty).** Po pięciu reszkach z rzędu ktoś twierdzi, że orzeł w szóstym rzucie jest bardziej prawdopodobny. *Rozwiązanie:* przy założeniu niezależnych uczciwych rzutów $P(O_6\mid R_1\cap\cdots\cap R_5)=1/2$. Wcześniejszy ciąg nie zmienia prawdopodobieństwa kolejnego rzutu.

**Problem P2 (test diagnostyczny, rachunek dokładny).** Choroba występuje u $1/100$ osób. Test wykrywa ją u $9/10$ chorych i daje wynik dodatni u $1/10$ zdrowych. Jakie jest prawdopodobieństwo choroby przy wyniku dodatnim? *Rozwiązanie:* $P(D\cap +)=9/1000$, a $P(+)=9/1000+99/1000=108/1000$. Stąd $P(D\mid +)=9/108=1/12$. Wysoka czułość nie oznacza wysokiego prawdopodobieństwa choroby po dodatnim teście przy niskiej częstości choroby.

**Problem P3 (bez zwracania).** W pudełku jest 6 dobrych i 4 wadliwe elementy. Losujemy 3 bez zwracania. Oblicz szansę co najmniej jednego wadliwego. *Rozwiązanie:* przeciwne zdarzenie to trzy dobre: $(6/10)(5/9)(4/8)=1/6$. Wynik $1-1/6=5/6$.

**Problem P4 (liczenie podwójne).** W klasie 30 osób 18 uczy się języka A, 14 języka B, 6 obu. Losujemy jedną osobę. Jaka jest szansa, że uczy się co najmniej jednego? *Rozwiązanie:* $|A\cup B|=18+14-6=26$, więc $P=26/30=13/15$. Cztery osoby nie uczą się żadnego.

**Problem P5 (bez założenia niezależności).** W czterech próbach szanse sukcesu to kolejno $1/2$, $1/3$, $1/4$, $1/5$, a próby mogą być zależne. Oblicz oczekiwaną liczbę sukcesów. *Rozwiązanie:* suma wartości oczekiwanych wskaźników wynosi $1/2+1/3+1/4+1/5=77/60$. Nie można natomiast wyznaczyć szansy „co najmniej jeden sukces” bez informacji o zależności.

# E. Kontrola jakości i ograniczenia

Model klasyczny wymaga uzasadnienia równoprawdopodobności. Przy losowaniach bez zwracania nie wolno automatycznie mnożyć bezwarunkowych szans kolejnych wyników. Wartość oczekiwana i częstość empiryczna są różnymi pojęciami. Podane twierdzenia mają skończoną przestrzeń zdarzeń; nie deklaruje się tutaj teorii miary ani ogólnych twierdzeń granicznych. Rozdział nie jest jeszcze zintegrowany z kanonicznym monolitem 0.20, więc **historyczny bilans 585 stron pozostaje bez zmian**. Liczba 1222 stron nie jest już obowiązkowym celem. Każdy końcowy tom PDF musi mieć mniej niż 99 000 000 bajtów. Wstęp historyczny pozostaje chroniony, a finalny spis treści powstanie dopiero po ukończeniu Tomu I.
