---
title: "Ontologia Liczby — Tom I"
subtitle: "E1-04. Algebra elementarna: wyrażenia, tożsamości i dziedziny"
author: "Andrzej Mikulski"
date: "2026-11-02"
lang: pl-PL
---

# E1-04. Algebra elementarna

**Umiejscowienie taksonomiczne:** poziom I, E1-04, **minimum 4 rzeczywistych stron na punkt** (źródło: „Taksonomia Matematyki”, strona 9/637). Tekst stanowi samodzielną warstwę elementarną. Istniejące F22.1 zawiera już zaawansowaną semantykę zmiennych, podstawienia, wielomiany formalne i ich ewaluację; F7.2 analizuje algebraiczne własności zera. Niniejszy rozdział nie zastępuje ani nie modyfikuje tamtych opracowań. Równania liniowe jako osobny temat należą do E1-05.

## Część A. Pojęcia, własności i dowody

### 1. Litera, wartość i wyrażenie

**Definicja D1 (zmienna i podstawienie).** Zmienna jest symbolem reprezentującym element ustalonej dziedziny liczbowej. Podstawienie \(\sigma\) przyporządkowuje każdej występującej zmiennej konkretną liczbę z tej dziedziny.

**Definicja D2 (wyrażenie algebraiczne).** Wyrażenie powstaje z liczb i zmiennych przez skończone stosowanie działań \(+,-,\cdot\), a także dzielenia tam, gdzie dzielnik jest różny od zera. Jego wartość jest określona tylko dla podstawień, przy których wszystkie działania są dopuszczalne.

**Definicja D3 (dziedzina wyrażenia).** Dziedzina \(D(E)\) to zbiór podstawień, dla których wyrażenie \(E\) ma określoną wartość. Równość wyrażeń na wspólnej dziedzinie nie musi oznaczać równości ich dziedzin.

**Definicja D4 (tożsamość na zbiorze).** Zapis \(E=F\) jest tożsamością na \(S\), jeżeli dla każdego podstawienia z \(S\) obie strony są określone i mają tę samą wartość. Warunek wspólnej określoności jest istotny.

**Twierdzenie T1 (zgodność podstawienia z dodawaniem).** Jeżeli \(E,F\) są określone dla \(\sigma\), to \((E+F)(\sigma)=E(\sigma)+F(\sigma)\).

*Dowód.* Jest to rekurencyjna reguła obliczania wartości wyrażenia zbudowanego przez dodawanie. Po obliczeniu składników stosujemy dodawanie liczb rzeczywistych. \(\square\)

**Twierdzenie T2 (zgodność podstawienia z mnożeniem).** Dla każdego dopuszczalnego \(\sigma\), \((EF)(\sigma)=E(\sigma)F(\sigma)\).

*Dowód.* Podstawienie zastępuje zmienne ich wartościami i zachowuje strukturę wyrażenia; ostatnią operacją jest mnożenie wartości obu czynników. \(\square\)

**Kontrprzykład K1 (dziedzina po skróceniu).** Wyrażenie \((x^2-1)/(x-1)\) jest określone tylko dla \(x\ne1\), mimo że po przekształceniu otrzymujemy \(x+1\), określone dla każdego \(x\). Są równe wyłącznie na pierwotnej dziedzinie \(x\ne1\).

**Kontrprzykład K2 (niedozwolone podstawienie).** Dla \(E(x)=1/(x-2)\) nie można obliczyć \(E(2)\); wynik nie jest „nieskończonością” w arytmetyce rzeczywistej.

### 2. Jednomiany i redukcja wyrazów podobnych

**Definicja D5 (jednomian).** Jednomianem w zmiennych \(x_1,\ldots,x_n\) nazywamy \(c x_1^{\alpha_1}\cdots x_n^{\alpha_n}\), gdzie \(c\in\mathbb R\), \(\alpha_i\in\mathbb N_0\). Współczynnik to \(c\), a wykładniki tworzą jego część literową.

**Definicja D6 (wyrazy podobne).** Jednomiany są podobne, gdy mają jednakowe wykładniki przy każdej zmiennej. Mogą różnić się współczynnikiem.

**Twierdzenie T3 (redukcja).** Dla jednomianu \(M\) i liczb \(a,b\) zachodzi \(aM+bM=(a+b)M\).

*Dowód.* Prawo rozdzielności mnożenia względem dodawania zastosowane w odwrotnym kierunku. \(\square\)

**Twierdzenie T4 (mnożenie jednomianów).** Dla \(a,b\in\mathbb R\), \(\alpha,\beta\in\mathbb N_0\) zachodzi \((ax^\alpha)(bx^\beta)=abx^{\alpha+\beta}\).

*Dowód.* Przemienność i łączność pozwalają zebrać współczynniki; prawo potęg \(x^\alpha x^\beta=x^{\alpha+\beta}\) kończy dowód. \(\square\)

**Kontrprzykład K3 (wyrazy niepodobne).** \(2x+3x^2\) nie jest równe \(5x^3\): dla \(x=2\) pierwsza wartość to \(16\), druga \(40\).

**Przykład P1.** \(3x^2-5x+2x^2+7x=5x^2+2x\).

### 3. Nawiasy, rozdzielność i znaki

**Twierdzenie T5 (rozdzielność).** \(a(b+c)=ab+ac\) dla \(a,b,c\in\mathbb R\).

*Dowód.* Jest to prawo rozdzielności w ciele liczb rzeczywistych. \(\square\)

**Twierdzenie T6 (odejmowanie sumy).** \(a-(b+c)=a-b-c\).

*Dowód.* \(a-(b+c)=a+(-1)(b+c)=a-b-c\) z T5. \(\square\)

**Twierdzenie T7 (mnożenie dwóch dwumianów).** \((a+b)(c+d)=ac+ad+bc+bd\).

*Dowód.* Stosujemy T5 najpierw do pierwszego, potem do drugiego nawiasu. \(\square\)

**Kontrprzykład K4 (minus przed nawiasem).** \(7-(2+3)=2\), ale \(7-2+3=8\). Usuwanie nawiasu po minusie zmienia znaki obu składników.

**Kontrprzykład K5 (brak rozdzielności potęgowania).** \((x+y)^2\ne x^2+y^2\) w ogólności: dla \(x=y=1\) otrzymujemy \(4\ne2\).

### 4. Wzory skróconego mnożenia i rozkład na czynniki

**Twierdzenie T8 (kwadrat sumy).** \((a+b)^2=a^2+2ab+b^2\).

*Dowód.* T7 przy \(c=a,d=b\) daje \(a^2+ab+ba+b^2=a^2+2ab+b^2\). \(\square\)

**Twierdzenie T9 (kwadrat różnicy).** \((a-b)^2=a^2-2ab+b^2\).

*Dowód.* Podstawiamy \(-b\) zamiast \(b\) w T8. \(\square\)

**Twierdzenie T10 (różnica kwadratów).** \(a^2-b^2=(a-b)(a+b)\).

*Dowód.* Prawa strona rozwija się do \(a^2+ab-ab-b^2=a^2-b^2\). \(\square\)

**Twierdzenie T11 (wspólny czynnik).** \(ab+ac=a(b+c)\).

*Dowód.* Jest to T5 czytane od prawej do lewej. \(\square\)

**Kontrprzykład K6 (błędna różnica).** \(a^2-b^2\) nie jest na ogół \((a-b)^2\). Dla \(a=3,b=2\) mamy odpowiednio \(5\) i \(1\).

**Przykład P2.** \(9x^2-25=(3x-5)(3x+5)\).

**Przykład P3.** \(6x^2+9x=3x(2x+3)\).

### 5. Wielomiany, współczynniki i stopień

**Definicja D7 (wielomian elementarny).** Wielomian w jednej zmiennej jest sumą skończenie wielu jednomianów \(a_kx^k\), gdzie \(k\in\mathbb N_0\). Współczynniki zerowe można pominąć.

**Definicja D8 (stopień).** Stopień niezerowego wielomianu to największy wykładnik z niezerowym współczynnikiem. Wielomianowi zerowemu nie przypisujemy tutaj stopnia naturalnego.

**Definicja D9 (współczynnik wiodący).** Współczynnik przy najwyższej potędze niezerowego wielomianu to jego współczynnik wiodący.

**Twierdzenie T12 (stopień sumy).** Dla niezerowych wielomianów \(P,Q\) o niezerowej sumie, \(\deg(P+Q)\le\max(\deg P,\deg Q)\).

*Dowód.* Przy potęgach większych od obu stopni współczynniki są zerowe. Współczynniki wiodące mogą się skasować, dlatego nie gwarantujemy równości. \(\square\)

**Twierdzenie T13 (stopień iloczynu nad liczbami rzeczywistymi).** Dla niezerowych wielomianów \(P,Q\in\mathbb R[x]\), \(\deg(PQ)=\deg P+\deg Q\).

*Dowód.* Najwyższy wyraz iloczynu ma współczynnik równy iloczynowi współczynników wiodących, który jest niezerowy, ponieważ liczby rzeczywiste nie mają dzielników zera. Wyższe potęgi nie powstają. \(\square\)

**Kontrprzykład K7 (stopień sumy).** Dla \(P=x^2+1\), \(Q=-x^2+x\) mamy \(\deg P=\deg Q=2\), lecz \(\deg(P+Q)=1\).

**Przykład P4.** \((2x^2+3)(x-4)=2x^3-8x^2+3x-12\).

### 6. Dziedzina wyrażeń wymiernych i przekształcenia

**Definicja D10 (wyrażenie wymierne).** Wyrażenie \(P(x)/Q(x)\), gdzie \(P,Q\) są wielomianami i \(Q\) nie jest wielomianem zerowym, jest określone dla tych \(x\in\mathbb R\), dla których \(Q(x)\ne0\).

**Twierdzenie T14 (skracanie z warunkiem).** Jeśli \(A,B,C\) są wielomianami i \(B(x)C(x)\ne0\), to \(\frac{A(x)C(x)}{B(x)C(x)}=\frac{A(x)}{B(x)}\).

*Dowód.* W ciele liczb rzeczywistych wolno skrócić niezerowy czynnik \(C(x)\). Założenie gwarantuje także określoność obu ułamków. \(\square\)

**Kontrprzykład K8 (skracanie sumy).** \((x+2)/x\ne2\) dla ogólnego \(x\ne0\). Dla \(x=2\) lewa strona wynosi \(2\), ale dla \(x=1\) wynosi \(3\).

**Twierdzenie T15 (wspólny mianownik).** Jeżeli \(b,d\ne0\), to \(\frac ab+\frac cd=\frac{ad+bc}{bd}\).

*Dowód.* Rozszerzamy pierwszy ułamek przez \(d\), drugi przez \(b\), a następnie dodajemy liczniki. \(\square\)

**Przykład P5.** \(\frac{x}{x-1}+\frac1{x-1}=\frac{x+1}{x-1}\), wyłącznie dla \(x\ne1\).

### 7. Nierówności algebraiczne i kontrola wyniku

**Definicja D11 (forma kwadratowa jednego wyrażenia).** Kwadratem wyrażenia \(E\) nazywamy \(E^2=E\cdot E\), określony tam, gdzie \(E\) jest określone.

**Twierdzenie T16 (nieujemność kwadratu).** Dla każdego rzeczywistego \(x\), \(x^2\ge0\), z równością dokładnie dla \(x=0\).

*Dowód.* Dla \(x\ge0\) iloczyn \(x\cdot x\) jest nieujemny; dla \(x<0\) oba czynniki są ujemne, więc ich iloczyn jest dodatni. \(\square\)

**Twierdzenie T17 (nierówność dwukwadratowa).** Dla \(a,b\in\mathbb R\), \(a^2+b^2\ge2ab\), a równość zachodzi dokładnie dla \(a=b\).

*Dowód.* \(a^2+b^2-2ab=(a-b)^2\ge0\). Równość zachodzi, gdy \(a-b=0\). \(\square\)

**Twierdzenie T18 (tożsamość sumy sześcianów).** \(a^3+b^3=(a+b)(a^2-ab+b^2)\).

*Dowód.* Po wymnożeniu otrzymujemy \(a^3-a^2b+ab^2+a^2b-ab^2+b^3=a^3+b^3\). \(\square\)

**Twierdzenie T19 (tożsamość różnicy sześcianów).** \(a^3-b^3=(a-b)(a^2+ab+b^2)\).

*Dowód.* Rozwinięcie prawej strony daje \(a^3+a^2b+ab^2-a^2b-ab^2-b^3=a^3-b^3\). \(\square\)

**Definicja D12 (kontrola podstawieniem).** Kontrola numeryczna to sprawdzenie równości wyrażeń dla wybranych dopuszczalnych wartości zmiennych. Może obalić błędną tożsamość, lecz skończona liczba zgodnych podstawień nie dowodzi tożsamości na całej dziedzinie.

**Kontrprzykład K9 (zgodność w jednym punkcie).** \(x^2=x\) dla \(x=0\) i \(x=1\), ale nie dla \(x=2\). Dwa udane testy nie dowodzą tożsamości.

**Kontrprzykład K10 (mnożenie nierówności).** Z \(-2<-1\) nie wynika \((-2)(-3)<(-1)(-3)\): rzeczywiście \(6>3\). Przy mnożeniu nierówności przez liczbę ujemną odwracamy znak.

## Część B. Rozwiązane zadania

### Zestaw I — podstawienia i jednomiany

**Z1.** Oblicz \(3x+2\) dla \(x=4\). **Rozwiązanie:** \(3\cdot4+2=14\).

**Z2.** Oblicz \(x^2-2x\) dla \(x=-3\). **Rozwiązanie:** \(9+6=15\).

**Z3.** Uprość \(4a+7a-2a\). **Rozwiązanie:** \(9a\).

**Z4.** Uprość \(3x^2+2x-5x^2+8x\). **Rozwiązanie:** \(-2x^2+10x\).

**Z5.** Pomnóż \((2x^3)(-4x^2)\). **Rozwiązanie:** \(-8x^5\).

**Z6.** Pomnóż \(3a^2b\cdot2ab^3\). **Rozwiązanie:** \(6a^3b^4\).

**Z7.** Oblicz \(2(x+5)\) dla \(x=-1\). **Rozwiązanie:** \(2\cdot4=8\).

**Z8.** Uprość \(5-(2x-3)\). **Rozwiązanie:** \(8-2x\).

**Z9.** Uprość \(3(x-2)-2(x+1)\). **Rozwiązanie:** \(3x-6-2x-2=x-8\).

**Z10.** Czy \(2x+3x^2=5x^3\)? **Rozwiązanie:** Nie; dla \(x=1\) obie strony są równe \(5\), ale dla \(x=2\) mamy \(16\ne40\).

### Zestaw II — wzory i rozkład

**Z11.** Rozwiń \((x+4)^2\). **Rozwiązanie:** \(x^2+8x+16\).

**Z12.** Rozwiń \((2x-3)^2\). **Rozwiązanie:** \(4x^2-12x+9\).

**Z13.** Rozłóż \(x^2-49\). **Rozwiązanie:** \((x-7)(x+7)\).

**Z14.** Rozłóż \(4a^2-9b^2\). **Rozwiązanie:** \((2a-3b)(2a+3b)\).

**Z15.** Rozłóż \(8x+12\). **Rozwiązanie:** \(4(2x+3)\).

**Z16.** Rozłóż \(6x^2-9x\). **Rozwiązanie:** \(3x(2x-3)\).

**Z17.** Rozwiń \((x+2)(x+5)\). **Rozwiązanie:** \(x^2+7x+10\).

**Z18.** Rozwiń \((x-3)(x+3)\). **Rozwiązanie:** \(x^2-9\).

**Z19.** Uprość \((x+1)^2-(x-1)^2\). **Rozwiązanie:** \(4x\).

**Z20.** Rozłóż \(x^2+6x+9\). **Rozwiązanie:** \((x+3)^2\).

### Zestaw III — wielomiany i dziedziny

**Z21.** Podaj stopień \(5x^4-2x+1\). **Rozwiązanie:** \(4\).

**Z22.** Podaj współczynnik wiodący \(-7x^3+4x^2\). **Rozwiązanie:** \(-7\).

**Z23.** Dodaj \(x^2+3x\) i \(2x^2-x+4\). **Rozwiązanie:** \(3x^2+2x+4\).

**Z24.** Odejmij \(2x^2-x\) od \(5x^2+2x+1\). **Rozwiązanie:** \(3x^2+3x+1\).

**Z25.** Pomnóż \((x+2)(x-4)\). **Rozwiązanie:** \(x^2-2x-8\).

**Z26.** Znajdź dziedzinę \(1/(x-5)\). **Rozwiązanie:** \(\mathbb R\setminus\{5\}\).

**Z27.** Znajdź dziedzinę \((x+1)/(x^2-4)\). **Rozwiązanie:** \(\mathbb R\setminus\{-2,2\}\).

**Z28.** Uprość \((x^2-4)/(x-2)\). **Rozwiązanie:** \(x+2\) z zachowaniem warunku \(x\ne2\).

**Z29.** Uprość \(x/(x+1)+1/(x+1)\). **Rozwiązanie:** \(1\) dla \(x\ne-1\).

**Z30.** Czy \((x^2-1)/(x-1)\) i \(x+1\) mają tę samą dziedzinę? **Rozwiązanie:** Nie; pierwsze wyrażenie wyklucza \(x=1\).

### Zestaw IV — dowody i rozumowanie

**Z31.** Udowodnij \((a+b)^2-(a-b)^2=4ab\). **Rozwiązanie:** Odejmujemy rozwinięcia \(a^2+2ab+b^2\) i \(a^2-2ab+b^2\).

**Z32.** Wykaż \(x^2+1>0\). **Rozwiązanie:** \(x^2\ge0\), więc \(x^2+1\ge1>0\).

**Z33.** Wykaż \(x^2-2x+1\ge0\). **Rozwiązanie:** \((x-1)^2\ge0\).

**Z34.** Znajdź najmniejszą wartość \(x^2-4x+7\). **Rozwiązanie:** \((x-2)^2+3\ge3\), równość dla \(x=2\).

**Z35.** Czy \(x^2+y^2\ge2xy\)? **Rozwiązanie:** Tak, bo \((x-y)^2\ge0\).

**Z36.** Kiedy zachodzi równość w Z35? **Rozwiązanie:** Dokładnie gdy \(x=y\).

**Z37.** Rozłóż \(a^3-b^3\). **Rozwiązanie:** \((a-b)(a^2+ab+b^2)\).

**Z38.** Rozłóż \(x^3+8\). **Rozwiązanie:** \((x+2)(x^2-2x+4)\).

**Z39.** Podaj kontrprzykład do \((a+b)^2=a^2+b^2\). **Rozwiązanie:** \(a=b=1\), gdyż \(4\ne2\).

**Z40.** Podaj kontrprzykład do twierdzenia, że \(\deg(P+Q)=\max(\deg P,\deg Q)\) zawsze. **Rozwiązanie:** \(P=x^2\), \(Q=-x^2+x\); suma ma stopień \(1\), składniki stopień \(2\).

### Problemy syntetyczne

**Problem S1 (model kosztu).** Bilet normalny kosztuje \(p\) zł, ulgowy \(q\) zł. Kupiono \(n\) biletów normalnych i \(m\) ulgowych. Podaj koszt i oblicz go dla \(p=24,q=15,n=3,m=4\).

*Rozwiązanie.* Koszt \(C=np+mq\); podstawienie daje \(C=3\cdot24+4\cdot15=132\) zł. Jednostki każdego składnika są takie same, więc dodawanie jest poprawne.

**Problem S2 (pole ramki).** Duży kwadrat ma bok \(a+b\), a wycięty ma bok \(a\), gdzie \(a,b\ge0\). Wyznacz pole ramki.

*Rozwiązanie.* \(P=(a+b)^2-a^2=2ab+b^2=b(2a+b)\). Obie postacie są równoważne; dla \(a=2,b=1\) wynik wynosi \(5\).

**Problem S3 (odwracalne przekształcenie).** Dla jakich \(x\) wolno zastąpić \((x^2-9)/(x-3)\) przez \(x+3\)?

*Rozwiązanie.* Faktoryzacja licznika daje \((x-3)(x+3)\). Skrócenie jest poprawne tylko dla \(x\ne3\). Po skróceniu zachowujemy pierwotne wykluczenie, mimo że \(x+3\) jako osobne wyrażenie jest określone również w \(3\).

**Problem S4 (fałszywy dowód).** Rozumowanie: \(a=b\ne0\), zatem \(a^2=ab\), \(a^2-b^2=ab-b^2\), \((a-b)(a+b)=b(a-b)\), więc \(a+b=b\), a stąd \(2=1\). Wskaż błąd.

*Rozwiązanie.* Z \(a=b\) wynika \(a-b=0\). Przejście od \((a-b)(a+b)=b(a-b)\) do \(a+b=b\) jest dzieleniem przez zero. Poprzednie równości są poprawne, lecz ostatnie skrócenie nie jest dozwolone.

## Granice opracowania i odbiór

Materiał zawiera 12 definicji, 19 twierdzeń z dowodami, 10 kontrprzykładów, 40 zadań z rozwiązaniami i 4 problemy syntetyczne. Są to jednostki treści, **nie strony wydawnicze**. Należy wykonać pełny skład, sprawdzić czy minimum 4 rzeczywistych stron z taksonomii jest osiągnięte, oraz przeprowadzić odbiór matematyczny. Rozdział nie zastępuje wcześniejszego F22.1 ani F7.2. Licznik monolitu 0.20 pozostaje **585/1222** do rzeczywistej integracji.
