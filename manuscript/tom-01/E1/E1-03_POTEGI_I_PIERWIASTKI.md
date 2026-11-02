---
title: 'ONTOLOGIA LICZBY — TOM I'
subtitle: 'E1-03. Potęgi i pierwiastki — rachunek, sens i granice praw'
author: 'Andrzej Mikulski'
date: '2 listopada 2026'
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Taksonomia:** E1-03, poziom I (minimum 4 rzeczywiste strony na punkt; źródło: taksonomia, s. 9/637). Rozdział dydaktyczny obejmuje potęgi o wykładnikach naturalnych i całkowitych, pierwiastki kwadratowe i sześcienne, uproszczenia, oszacowania i zastosowania. Istniejące F21.1 zawiera już zaawansowaną teorię monoidów, wartościowań i wykładników wymiernych: niniejszy rozdział jej nie zastępuje ani nie przypisuje sobie jej rezultatów. **Status:** materiał źródłowy przed pełnym składem i odbiorem objętościowym.

# Część A. Teoria, twierdzenia i dowody

## 1. Potęga jako uporządkowany iloczyn

**Definicja 1.** Dla liczby rzeczywistej \(a\) i naturalnego \(n\ge1\) definiujemy \(a^n=\underbrace{a\cdot\ldots\cdot a}_{n\text{ czynników}}\). Dla każdego \(a\ne0\) przyjmujemy \(a^0=1\). W algebrze monoidów można również przyjąć \(0^0=1\) jako wartość pustego iloczynu, lecz nie stosujemy tej konwencji bez jawnego wskazania.

**Twierdzenie 1 (dodawanie wykładników).** Dla \(a\in\mathbb R\), \(m,n\in\mathbb N\), zachodzi \(a^ma^n=a^{m+n}\).

*Dowód.* Lewa strona jest iloczynem \(m\) kopii \(a\) i \(n\) kopii \(a\). Łączność mnożenia pozwala połączyć je w \(m+n\) czynników. \(\square\)

**Twierdzenie 2 (potęga potęgi).** Dla \(m,n\in\mathbb N\), \((a^m)^n=a^{mn}\).

*Dowód.* Po lewej mamy \(n\) grup po \(m\) czynników \(a\). Ich liczba wynosi \(mn\). \(\square\)

**Twierdzenie 3 (potęga iloczynu).** Dla \(a,b\in\mathbb R\) i \(n\in\mathbb N\), \((ab)^n=a^nb^n\).

*Dowód.* W \(\mathbb R\) mnożenie jest przemienne, więc możemy przegrupować \(n\) kopii \(ab\) w iloczyn \(n\) kopii \(a\) i \(n\) kopii \(b\). \(\square\)

**Kontrprzykład 1.** \((2+3)^2=25\), podczas gdy \(2^2+3^2=13\). Potęgowanie nie rozdziela się względem dodawania.

**Kontrprzykład 2.** \(2^{3^2}=2^9=512\), ale \((2^3)^2=64\). Nawiasy w piętrowych potęgach mają znaczenie.

**Definicja 2.** Dla \(a\ne0\) i \(n\in\mathbb N\) określamy \(a^{-n}=1/a^n\).

**Twierdzenie 4.** Dla \(a\ne0\) i \(m,n\in\mathbb Z\), \(a^ma^n=a^{m+n}\).

*Dowód.* Dla dodatnich wykładników jest to Twierdzenie 1. Jeżeli wykładniki mają przeciwne znaki, skracamy wspólne czynniki \(a\) z \(1/a\); dla dwóch ujemnych korzystamy z \(a^{-m}a^{-n}=1/(a^{m+n})\) przy \(m,n>0\). Przypadek wykładnika zero jest natychmiastowy. \(\square\)

**Kontrprzykład 3.** \(0^{-2}\) nie istnieje jako liczba rzeczywista, bo wymaga dzielenia przez zero.

**Przykład 1.** \(2^3\cdot2^{-5}=2^{-2}=1/4\).

## 2. Znak, porządek i szacowanie

**Twierdzenie 5 (parzystość wykładnika).** Dla \(a<0\), \(a^{2k}>0\) dla \(k\ge1\), natomiast \(a^{2k+1}<0\) dla \(k\ge0\).

*Dowód.* Każda para ujemnych czynników ma dodatni iloczyn. Przy nieparzystej liczbie czynników pozostaje jeden ujemny. \(\square\)

**Twierdzenie 6 (monotoniczność dla podstaw dodatnich).** Jeśli \(0<a<b\) i \(n\in\mathbb N\), to \(a^n<b^n\).

*Dowód.* Mnożenie nierówności przez dodatnie czynniki zachowuje ich zwrot; można też indukcyjnie porównać \(a^{n+1}=a^na<b^nb=b^{n+1}\). \(\square\)

**Twierdzenie 7 (zależność od wykładnika).** Dla \(a>1\) ciąg \(a^n\) jest ściśle rosnący; dla \(0<a<1\) jest ściśle malejący.

*Dowód.* Iloraz kolejnych wyrazów wynosi \(a^{n+1}/a^n=a\), większy lub mniejszy od 1 odpowiednio. \(\square\)

**Kontrprzykład 4.** Nie jest prawdą, że zwiększenie wykładnika zawsze zwiększa potęgę: \((1/2)^3=1/8<1/4=(1/2)^2\).

**Przykład 2.** Bez mnożenia liczb \(1{,}01^{100}\) i \(1{,}01^{101}\) wiemy, że druga jest większa.

## 3. Pierwiastki jako działania odwrotne

**Definicja 3 (pierwiastek kwadratowy).** Dla \(x\ge0\) symbol \(\sqrt{x}\) oznacza jedyną liczbę \(y\ge0\), dla której \(y^2=x\).

**Definicja 4 (pierwiastek sześcienny).** Dla \(x\in\mathbb R\) symbol \(\sqrt[3]{x}\) oznacza jedyną liczbę \(y\in\mathbb R\), dla której \(y^3=x\).

**Twierdzenie 8.** Dla każdego \(a\in\mathbb R\), \(\sqrt{a^2}=|a|\).

*Dowód.* \(|a|\ge0\) i \(|a|^2=a^2\). Jedyność nieujemnego pierwiastka daje wynik. \(\square\)

**Kontrprzykład 5.** \(\sqrt{(-7)^2}=7\), a nie \(-7\). Wzór \(\sqrt{a^2}=a\) wymaga \(a\ge0\).

**Twierdzenie 9.** Dla \(a,b\ge0\), \(\sqrt{ab}=\sqrt a\sqrt b\).

*Dowód.* Iloczyn \(\sqrt a\sqrt b\) jest nieujemny, a jego kwadrat wynosi \(ab\); z jednoznaczności pierwiastka wynika równość. \(\square\)

**Twierdzenie 10.** Dla \(a\ge0\), \(b>0\), \(\sqrt{a/b}=\sqrt a/\sqrt b\).

*Dowód.* Prawa strona jest nieujemna, a jej kwadrat to \(a/b\). \(\square\)

**Kontrprzykład 6.** \(\sqrt{9+16}=5\), lecz \(\sqrt9+\sqrt{16}=7\). Pierwiastek nie jest addytywny.

**Kontrprzykład 7.** \(\sqrt{-9}\) nie jest liczbą rzeczywistą; tymczasem \(\sqrt[3]{-8}=-2\) istnieje.

**Twierdzenie 11 (monotoniczność pierwiastka).** Dla \(0\le a<b\), \(\sqrt a<\sqrt b\).

*Dowód.* Gdyby \(\sqrt a\ge\sqrt b\), to podnosząc nieujemne strony do kwadratu, uzyskalibyśmy \(a\ge b\), sprzeczność. \(\square\)

**Przykład 3.** Ponieważ \(49<60<64\), mamy \(7<\sqrt{60}<8\).

## 4. Wyłączanie czynnika i dokładność

**Definicja 5 (czynnik kwadratowy).** Dodatnia liczba naturalna \(d\) jest czynnikiem kwadratowym liczby naturalnej \(N\), gdy \(N=d^2m\) dla pewnego \(m\in\mathbb N\).

**Twierdzenie 12.** Jeśli \(N=d^2m\) i \(d,m\in\mathbb N\), to \(\sqrt N=d\sqrt m\).

*Dowód.* Z Twierdzenia 9: \(\sqrt{d^2m}=\sqrt{d^2}\sqrt m=d\sqrt m\). \(\square\)

**Przykład 4.** \(\sqrt{72}=\sqrt{36\cdot2}=6\sqrt2\).

**Definicja 6 (przedział pierwiastka).** Para \(L,U\ge0\) jest certyfikatem \(L\le\sqrt x\le U\), gdy \(L^2\le x\le U^2\).

**Twierdzenie 13.** Jeśli \(L,U\ge0\) i \(L^2\le x\le U^2\), to \(L\le\sqrt x\le U\).

*Dowód.* Jest to monotoniczność pierwiastka zastosowana do obu nierówności. \(\square\)

**Przykład 5.** \(1{,}4^2=1{,}96<2<2{,}25=1{,}5^2\); zatem \(1{,}4<\sqrt2<1{,}5\).

**Twierdzenie 14 (niewymierność \(\sqrt2\)).** \(\sqrt2\notin\mathbb Q\).

*Dowód.* Przypuśćmy, że \(\sqrt2=p/q\) w postaci nieskracalnej, \(q>0\). Wtedy \(p^2=2q^2\), więc \(p^2\) jest parzyste. Gdyby \(p\) było nieparzyste, jego kwadrat też byłby nieparzysty; stąd \(p=2k\). Podstawienie daje \(q^2=2k^2\), zatem \(q\) też jest parzyste. To przeczy nieskracalności. \(\square\)

**Kontrprzykład 8.** \(\sqrt{16}=4\) jest wymierny; nie każdy pierwiastek z liczby naturalnej jest niewymierny.

## 5. Notacja naukowa i zastosowania

**Definicja 7 (notacja naukowa).** Niezerową liczbę dziesiętną przedstawiamy jako \(m\cdot10^k\), gdzie \(k\in\mathbb Z\), \(1\le|m|<10\).

**Twierdzenie 15.** Dla \(m,n\ne0\), \((m10^k)(n10^\ell)=(mn)10^{k+\ell}\).

*Dowód.* Łączność i przemienność mnożenia oraz prawo dodawania wykładników. Jeśli \(|mn|\notin[1,10)\), wynik należy ponownie znormalizować. \(\square\)

**Przykład 6.** \((3\cdot10^4)(2\cdot10^{-2})=6\cdot10^2=600\).

**Definicja 8 (pole kwadratu).** Dla boku długości \(s\ge0\) pole kwadratu wynosi \(s^2\); odwrotnie bok kwadratu o polu \(P\ge0\) ma długość \(\sqrt P\).

**Przykład 7.** Kwadrat o polu \(50\,\mathrm{cm}^2\) ma bok \(5\sqrt2\,\mathrm{cm}\), a nie \(25\,\mathrm{cm}\).

**Kontrprzykład 9.** Podwojenie boku kwadratu nie podwaja pola: z \(s^2\) otrzymujemy \((2s)^2=4s^2\).

**Twierdzenie 16 (skalowanie).** Jeśli długość boku kwadratu mnożymy przez \(t\ge0\), jego pole mnoży się przez \(t^2\).

*Dowód.* \((ts)^2=t^2s^2\). \(\square\)

**Definicja 9 (pierwiastek stopnia \(n\)).** Dla parzystego \(n\ge2\) i \(x\ge0\), \(\sqrt[n]x\) to jedyny nieujemny \(y\) z \(y^n=x\). Dla nieparzystego \(n\ge3\) i \(x\in\mathbb R\) jest to jedyny rzeczywisty \(y\) z \(y^n=x\).

**Twierdzenie 17.** Dla \(n\ge2\) i dopuszczalnego \(x\), \((\sqrt[n]x)^n=x\).

*Dowód.* Wynika bezpośrednio z definicji pierwiastka. \(\square\)

**Kontrprzykład 10.** Dla \(n=4\), \(\sqrt[4]{(-3)^4}=3\), nie \(-3\). Przy parzystym stopniu wybieramy nieujemną gałąź.

**Definicja 10 (wykładnik wymierny dodatniej podstawy).** Dla \(a>0\), \(m\in\mathbb Z\), \(n\in\mathbb N\), definiujemy \(a^{m/n}=(\sqrt[n]a)^m\).

**Twierdzenie 18 (niezależność zapisu wykładnika).** Jeśli \(m/n=p/q\) i \(a>0\), to \((\sqrt[n]a)^m=(\sqrt[q]a)^p\).

*Dowód.* Oznaczmy \(u=(\sqrt[n]a)^m\), \(v=(\sqrt[q]a)^p\). Obie liczby są dodatnie. Po podniesieniu do potęgi \(nq\) otrzymujemy \(u^{nq}=a^{mq}\) oraz \(v^{nq}=a^{pn}\). Ponieważ \(mq=pn\), wyniki są równe. Funkcja \(t\mapsto t^{nq}\) jest ściśle rosnąca na liczbach dodatnich, więc \(u=v\). \(\square\)

**Kontrprzykład 11.** Wyrażenie \((-8)^{1/2}\) nie ma wartości rzeczywistej. Dla ujemnych podstaw reguły wykładników wymiernych wymagają osobnych ograniczeń.

**Twierdzenie 19 (porównywanie pierwiastków tego samego stopnia).** Dla \(0\le a<b\) i \(n\ge2\), \(\sqrt[n]a<\sqrt[n]b\).

*Dowód.* Funkcja \(t\mapsto t^n\) jest ściśle rosnąca na \(t\ge0\), a więc jej odwrotność także zachowuje porządek. \(\square\)

**Definicja 11 (dokładny wynik).** Wynik zawierający symbol \(\sqrt n\) pozostaje dokładny, dopóki nie zastąpimy go przybliżeniem dziesiętnym. Oszacowanie należy podawać z kontrolą błędu lub przedziałem.

**Przykład 8.** \(3\sqrt2\) jest wartością dokładną; \(4{,}2\) jest jedynie przybliżeniem, bo \(3\cdot1{,}4<3\sqrt2<3\cdot1{,}5\).

# Część B. Zadania z rozwiązaniami

## Zestaw I. Potęgi naturalne

**Zadanie 1.** Oblicz \(2^5\). *Rozwiązanie.* \(2^5=32\).

**Zadanie 2.** Oblicz \(3^4\). *Rozwiązanie.* \(3^4=81\).

**Zadanie 3.** Uprość \(5^3\cdot5^2\). *Rozwiązanie.* \(5^5=3125\).

**Zadanie 4.** Uprość \((2^3)^4\). *Rozwiązanie.* \(2^{12}=4096\).

**Zadanie 5.** Oblicz \((-2)^4\). *Rozwiązanie.* \(16\).

**Zadanie 6.** Oblicz \(-2^4\). *Rozwiązanie.* \(-(2^4)=-16\).

**Zadanie 7.** Oblicz \((-3)^3\). *Rozwiązanie.* \(-27\).

**Zadanie 8.** Porównaj \(4^3\) i \(3^4\). *Rozwiązanie.* \(64<81\).

**Zadanie 9.** Uprość \(7^0\). *Rozwiązanie.* \(1\), bo podstawa jest niezerowa.

**Zadanie 10.** Czy \(0^0\) ma tu zdefiniowaną wartość? *Rozwiązanie.* Nie; przyjęta definicja \(a^0=1\) wymaga \(a\ne0\).

## Zestaw II. Potęgi całkowite

**Zadanie 11.** Oblicz \(2^{-3}\). *Rozwiązanie.* \(1/8\).

**Zadanie 12.** Oblicz \(10^{-4}\). *Rozwiązanie.* \(1/10000\).

**Zadanie 13.** Uprość \(3^5/3^7\). *Rozwiązanie.* \(3^{-2}=1/9\).

**Zadanie 14.** Oblicz \((-2)^{-3}\). *Rozwiązanie.* \(-1/8\).

**Zadanie 15.** Uprość \(5^{-2}\cdot5^4\). *Rozwiązanie.* \(5^2=25\).

**Zadanie 16.** Oblicz \((1/2)^{-3}\). *Rozwiązanie.* \(2^3=8\).

**Zadanie 17.** Dlaczego \(0^{-1}\) jest niedozwolone? *Rozwiązanie.* Wymagałoby \(1/0\).

**Zadanie 18.** Uprość \(2^4\cdot2^{-4}\). *Rozwiązanie.* \(2^0=1\).

**Zadanie 19.** Oblicz \((3/4)^{-2}\). *Rozwiązanie.* \((4/3)^2=16/9\).

**Zadanie 20.** Uprość \(10^6/10^2\). *Rozwiązanie.* \(10^4\).

## Zestaw III. Pierwiastki

**Zadanie 21.** Oblicz \(\sqrt{81}\). *Rozwiązanie.* \(9\).

**Zadanie 22.** Oblicz \(\sqrt{(-9)^2}\). *Rozwiązanie.* \(9\).

**Zadanie 23.** Oblicz \(\sqrt[3]{-125}\). *Rozwiązanie.* \(-5\).

**Zadanie 24.** Uprość \(\sqrt{50}\). *Rozwiązanie.* \(5\sqrt2\).

**Zadanie 25.** Uprość \(\sqrt{108}\). *Rozwiązanie.* \(6\sqrt3\).

**Zadanie 26.** Oblicz \(\sqrt{25\cdot36}\). *Rozwiązanie.* \(5\cdot6=30\).

**Zadanie 27.** Oblicz \(\sqrt{49/64}\). *Rozwiązanie.* \(7/8\).

**Zadanie 28.** Oszacuj \(\sqrt{30}\) między kolejnymi liczbami naturalnymi. *Rozwiązanie.* \(25<30<36\), więc \(5<\sqrt{30}<6\).

**Zadanie 29.** Czy \(\sqrt{16+9}=\sqrt{16}+\sqrt9\)? *Rozwiązanie.* Nie: \(5\ne7\).

**Zadanie 30.** Czy \(\sqrt{-4}\) istnieje w \(\mathbb R\)? *Rozwiązanie.* Nie, bo kwadrat liczby rzeczywistej jest nieujemny.

## Zestaw IV. Wyrażenia i zastosowania

**Zadanie 31.** Oblicz \(2^3+3^2\). *Rozwiązanie.* \(8+9=17\).

**Zadanie 32.** Oblicz \((2+3)^2\). *Rozwiązanie.* \(25\).

**Zadanie 33.** Uprość \(3\sqrt8\). *Rozwiązanie.* \(3\cdot2\sqrt2=6\sqrt2\).

**Zadanie 34.** Uprość \(\sqrt{12}+\sqrt{27}\). *Rozwiązanie.* \(2\sqrt3+3\sqrt3=5\sqrt3\).

**Zadanie 35.** Pole kwadratu wynosi \(72\text{ cm}^2\). Znajdź bok. *Rozwiązanie.* \(\sqrt{72}=6\sqrt2\text{ cm}\).

**Zadanie 36.** Bok kwadratu wzrósł trzykrotnie. Ile razy wzrosło pole? *Rozwiązanie.* Dziewięciokrotnie.

**Zadanie 37.** Zapisz \(0{,}00045\) w notacji naukowej. *Rozwiązanie.* \(4{,}5\cdot10^{-4}\).

**Zadanie 38.** Zapisz \(7200000\) w notacji naukowej. *Rozwiązanie.* \(7{,}2\cdot10^6\).

**Zadanie 39.** Oblicz \((4\cdot10^3)(2\cdot10^{-2})\). *Rozwiązanie.* \(8\cdot10^1=80\).

**Zadanie 40.** Oblicz \(27^{2/3}\). *Rozwiązanie.* \((\sqrt[3]{27})^2=3^2=9\).

**Zadanie 41.** Oblicz \(16^{3/4}\). *Rozwiązanie.* \((\sqrt[4]{16})^3=2^3=8\).

**Zadanie 42.** Uprość \(a^{1/2}a^{3/2}\) dla \(a>0\). *Rozwiązanie.* \(a^2\).

**Zadanie 43.** Udowodnij, że \(2^n\) jest parzyste dla \(n\ge1\). *Rozwiązanie.* \(2^n=2\cdot2^{n-1}\).

**Zadanie 44.** Czy \(3^{2n}\) jest kwadratem liczby całkowitej? *Rozwiązanie.* Tak, \(3^{2n}=(3^n)^2\).

**Zadanie 45.** Wykaż, że \(\sqrt2\) nie jest liczbą wymierną. *Rozwiązanie.* Zakładamy nieskracalny ułamek \(p/q\). Równość \(p^2=2q^2\) wymusza parzystość \(p\), a następnie \(q\), sprzeczność.

**Zadanie 46.** Wykaż \(2<\sqrt5<3\). *Rozwiązanie.* \(4<5<9\), a pierwiastek jest rosnący.

**Zadanie 47.** Znajdź \(n\), gdy \(2^n=128\). *Rozwiązanie.* \(128=2^7\), więc \(n=7\).

**Zadanie 48.** Znajdź \(n\in\mathbb N\), gdy \(3^{n+1}=81\). *Rozwiązanie.* \(81=3^4\), zatem \(n=3\).

**Zadanie 49.** Czy \((ab)^2=a^2b^2\) dla rzeczywistych \(a,b\)? *Rozwiązanie.* Tak, bo \(abab=aabb\) dzięki przemienności.

**Zadanie 50.** Oblicz \(\sqrt[4]{81}\). *Rozwiązanie.* \(3\).

**Zadanie 51.** Oblicz \(\sqrt[3]{64/125}\). *Rozwiązanie.* \(4/5\).

**Zadanie 52.** Czy \(\sqrt{x^2}=x\) dla każdego rzeczywistego \(x\)? *Rozwiązanie.* Nie; dla \(x<0\) wynik to \(-x\). Ogólnie \(|x|\).

**Zadanie 53.** Wykaż \(\sqrt{ab}\le(a+b)/2\) dla \(a,b\ge0\). *Rozwiązanie.* \(0\le(\sqrt a-\sqrt b)^2=a+b-2\sqrt{ab}\), więc nierówność zachodzi.

**Zadanie 54.** Kiedy w Zadaniu 53 zachodzi równość? *Rozwiązanie.* Gdy \(\sqrt a=\sqrt b\), czyli \(a=b\).

**Zadanie 55.** Oblicz \(2^{-2}+2^{-3}\). *Rozwiązanie.* \(1/4+1/8=3/8\).

**Zadanie 56.** Czy \((-1)^{1001}=1\)? *Rozwiązanie.* Nie, wykładnik jest nieparzysty, więc wynik to \(-1\).

**Zadanie 57.** Porównaj \((1/3)^2\) i \((1/3)^3\). *Rozwiązanie.* \(1/9>1/27\).

**Zadanie 58.** Oblicz \(100^{1/2}\). *Rozwiązanie.* \(10\).

**Zadanie 59.** Oblicz \(8^{1/3}\). *Rozwiązanie.* \(2\).

**Zadanie 60.** Czy \(0^{1/2}=0\)? *Rozwiązanie.* Tak, pierwiastek z zera to zero, choć definicja potęg wymiernych dodatniej podstawy nie obejmuje zera; zapis interpretuje się tu bezpośrednio jako pierwiastek.

## Problemy przekrojowe

**Problem A (odkrywanie błędu).** Uczeń twierdzi: \(\sqrt{a^2+b^2}=a+b\) dla \(a,b\ge0\). Ustal, kiedy to prawda.

*Rozwiązanie.* Obie strony są nieujemne. Podnosząc do kwadratu, dostajemy \(a^2+b^2=a^2+2ab+b^2\), czyli \(ab=0\). Równość zachodzi dokładnie wtedy, gdy co najmniej jedna z liczb jest zerem.

**Problem B (certyfikat oszacowania).** Podaj przedział długości najwyżej \(0{,}01\) zawierający \(\sqrt2\).

*Rozwiązanie.* \(1{,}41^2=1{,}9881<2\), a \(1{,}42^2=2{,}0164>2\). Stąd \(1{,}41<\sqrt2<1{,}42\), przedział ma długość \(0{,}01\).

**Problem C (pole i skala).** Dwa kwadraty mają boki w stosunku \(2:5\). W jakim stosunku są ich pola?

*Rozwiązanie.* Pola są proporcjonalne do kwadratów boków: \(2^2:5^2=4:25\).

**Problem D (potęgi i podzielność).** Wykaż, że dla każdego \(n\ge1\) liczba \(10^n-1\) jest podzielna przez 9.

*Rozwiązanie.* \(10^n-1=(10-1)(10^{n-1}+10^{n-2}+\cdots+10+1)\), więc zawiera czynnik 9. Alternatywnie indukcja: \(10^{n+1}-1=10(10^n-1)+9\).

## Uwagi redakcyjne i granice

Rozdział dotyczy szkolnego znaczenia działań i realnej osi liczbowej. Zagadnienia monoidów nieprzemiennych, wartościowań pierwszych i kryteriów wymierności potęg pozostają w istniejącym F21.1; są uzupełnieniem, a nie treścią zastępowaną. Dla ujemnych podstaw nie rozszerzamy bezwarunkowo reguł wykładników wymiernych. Nie deklaruje się ukończenia wymaganego minimum stron przed pełnym składem, testami i integracją. Bilans 585/1222 bez zmian.
