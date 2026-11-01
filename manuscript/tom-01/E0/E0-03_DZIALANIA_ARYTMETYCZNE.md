---
title: 'ONTOLOGIA LICZBY — TOM I'
subtitle: 'E0-03. Działania arytmetyczne — znaczenie, prawa, algorytmy i granice'
author: 'Andrzej Mikulski'
date: '1 listopada 2026'
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Taksonomia:** E0-03, poziom I — dodawanie, odejmowanie, mnożenie, dzielenie. Powiązania z MSC 11 i 97 są tematyczne, nie są identyfikatorami E0. **Status:** rozdział źródłowy, przed kontrolą paginacji i integracją. Przyjmujemy \(\mathbb N_0=\{0,1,2,\ldots\}\). Chroniony wstęp historyczny pozostaje nienaruszony.

# Część A. Znaczenie działań i ich uzasadnienie

## 1. Dodawanie: łączenie rozłącznych kolekcji

**Definicja 1 (suma liczebności).** Jeżeli \(A,B\) są skończonymi zbiorami rozłącznymi, to \(a+b:=|A\cup B|\) dla \(a=|A|\), \(b=|B|\). Niezależność od wyboru reprezentantów wynika z przeniesienia bijekcji na rozłączne kopie zbiorów.

**Twierdzenie 1 (przemienność).** \(a+b=b+a\).

*Dowód.* Dla rozłącznych reprezentantów \(A,B\) zbiory \(A\cup B\) i \(B\cup A\) są identyczne. Ich liczebności są równe. \(\square\)

**Twierdzenie 2 (łączność).** \((a+b)+c=a+(b+c)\).

*Dowód.* Wybierzmy trzy parami rozłączne zbiory o odpowiednich liczebnościach. Obie strony liczą elementy \(A\cup B\cup C\) dokładnie raz. \(\square\)

**Definicja 2 (zero).** Zero oznacza liczebność zbioru pustego. Stąd \(a+0=a\).

**Przykład 1.** Trzy czerwone i cztery niebieskie klocki dają siedem klocków, jeżeli żadnego nie zaliczono do obu grup. Warunek rozłączności jest częścią rozumowania, nie ozdobnikiem.

**Kontrprzykład 1.** Cztery osoby w kole fotograficznym i trzy w kole teatralnym nie muszą oznaczać siedmiu różnych osób. Jeżeli dwie należą do obu kół, suma różnych osób wynosi \(4+3-2=5\).

## 2. Odejmowanie: uzupełnienie do całości

**Definicja 3 (różnica w \(\mathbb N_0\)).** Dla \(a\ge b\) liczba \(a-b\) jest jedynym \(c\in\mathbb N_0\) spełniającym \(b+c=a\). Dla \(a<b\) różnica nie należy do \(\mathbb N_0\).

**Twierdzenie 3 (jednoznaczność różnicy).** Jeśli \(b+c=a=b+d\), to \(c=d\).

*Dowód.* Dla ustalonego \(b\) funkcja \(n\mapsto b+n\) jest ściśle rosnąca na \(\mathbb N_0\), co wynika z dodawania kolejnych jedności. Nie może więc przyjmować tej samej wartości w dwóch różnych argumentach. \(\square\)

**Przykład 2.** Z dziewięciu zdjęć wybrano sześć; trzy pozostały niewybrane, bo \(6+3=9\).

**Kontrprzykład 2.** W \(\mathbb N_0\) wyrażenie \(3-5\) nie ma wyniku. Liczba \(-2\) pojawia się dopiero po rozszerzeniu dziedziny do liczb całkowitych.

## 3. Mnożenie: jednakowo liczne grupy

**Definicja 4 (iloczyn).** \(a\cdot b\) jest liczebnością \(b\) parami rozłącznych grup, z których każda ma \(a\) elementów. Dla \(b=0\) nie ma żadnej grupy, więc \(a\cdot0=0\).

**Twierdzenie 4 (przemienność mnożenia).** \(ab=ba\).

*Dowód.* Rozważmy kratkę z \(a\) wierszami i \(b\) kolumnami. Liczenie komórek wierszami daje \(ab\), a kolumnami \(ba\). \(\square\)

**Twierdzenie 5 (rozdzielność).** \(a(b+c)=ab+ac\).

*Dowód.* Kratkę o \(a\) wierszach i \(b+c\) kolumnach rozcinamy na dwa prostokąty: o \(b\) oraz \(c\) kolumnach. Są rozłączne, a suma ich liczebności jest liczebnością całej kratki. \(\square\)

**Twierdzenie 6 (łączność mnożenia).** \((ab)c=a(bc)\).

*Dowód.* Policzmy trójki \((i,j,k)\), gdzie \(1\le i\le a\), \(1\le j\le b\), \(1\le k\le c\). Grupowanie najpierw po dwóch pierwszych, a potem po dwóch ostatnich współrzędnych nie zmienia liczby trójek. \(\square\)

**Przykład 3.** Sześć pudełek po cztery fotografie zawiera \(6\cdot4=24\) fotografie. Rozdzielenie na cztery pudełka i dwa pudełka daje \(4\cdot4+2\cdot4=24\).

**Kontrprzykład 3.** Z \(3+4=7\) nie wynika \(3\cdot4=7\). Dodawanie łączy dwie grupy, a mnożenie liczy równe grupy; działania mają odmienne znaczenia.

## 4. Dzielenie: równe części i grupowanie

**Definicja 5 (dzielenie dokładne).** Dla \(b>0\) iloraz \(a:b=q\) w \(\mathbb N_0\) istnieje wtedy i tylko wtedy, gdy \(a=bq\).

**Definicja 6 (iloraz i reszta).** Dla \(a\in\mathbb N_0\), \(b\in\mathbb N\) parą iloraz–reszta nazywamy \(q,r\in\mathbb N_0\) spełniające \(a=bq+r\) i \(0\le r<b\).

**Twierdzenie 7 (istnienie dzielenia z resztą).** Dla każdego \(a\ge0\) i \(b>0\) istnieją \(q,r\) z definicji 6.

*Dowód.* W zbiorze \(\{k\in\mathbb N_0:bk\le a\}\) jest zero i jest on skończony, bo \(k\le a\) dla \(b\ge1\). Niech \(q\) będzie jego największym elementem. Wówczas \(bq\le a<b(q+1)\). Przyjmując \(r=a-bq\), otrzymujemy \(0\le r<b\). \(\square\)

**Twierdzenie 8 (jednoznaczność).** Para \(q,r\) w twierdzeniu 7 jest jedyna.

*Dowód.* Gdy \(bq+r=bq'+r'\), to \(b(q-q')=r'-r\). Ponieważ \(-(b-1)\le r'-r\le b-1\), jedyną wielokrotnością \(b\) w tym przedziale jest zero. Zatem \(q=q'\) i \(r=r'\). \(\square\)

**Przykład 4.** Siedemnaście kart rozłożonych po pięć daje trzy pełne grupy i dwie pozostałe karty: \(17=5\cdot3+2\).

**Kontrprzykład 4.** Równość \(17=5\cdot2+7\) jest prawdziwa, ale liczba 7 nie jest resztą z dzielenia przez 5, bo \(7\not<5\).

**Kontrprzykład 5.** Dzielenie przez zero nie ma określonego ilorazu: równanie \(0\cdot q=5\) nie ma rozwiązań, a \(0\cdot q=0\) ma ich nieskończenie wiele. Żadne nie daje jednoznacznego działania odwrotnego.

## 5. Kolejność działań, własności i rachunek pisemny

**Definicja 7 (wartość wyrażenia).** Nawiasy ustalają kolejność; bez nawiasów mnożenie i dzielenie wykonujemy przed dodawaniem i odejmowaniem, a działania o jednakowym priorytecie kolejno od lewej strony, jeżeli nie zaznaczono inaczej.

**Przykład 5.** \(3+4\cdot5=23\), lecz \((3+4)\cdot5=35\).

**Kontrprzykład 6.** Odejmowanie nie jest łączne: \((9-4)-2=3\), natomiast \(9-(4-2)=7\).

**Definicja 8 (przeniesienie dziesiątkowe).** W kolumnie dodawania cyfr \(x_i,y_i\in\{0,\ldots,9\}\) i przeniesienia \(c_i\) obliczamy \(t_i=x_i+y_i+c_i\), cyfrę \(d_i=t_i\bmod10\) oraz \(c_{i+1}=\lfloor t_i/10\rfloor\).

**Twierdzenie 9 (niezmiennik dodawania pisemnego).** Po obliczeniu pierwszych \(j\) kolumn zachodzi
\[
\sum_{i<j}(x_i+y_i)10^i=\sum_{i<j}d_i10^i+c_j10^j.
\]

*Dowód.* Dla \(j=0\) obie strony są zerem, ponieważ \(c_0=0\). Z równania \(x_j+y_j+c_j=d_j+10c_{j+1}\) wynika \((x_j+y_j)10^j=d_j10^j+c_{j+1}10^{j+1}-c_j10^j\). Dodając do założenia indukcyjnego, otrzymujemy tezę dla \(j+1\). \(\square\)

**Przykład 6.** \(487+568\): jedności \(7+8=15\), dziesiątki \(8+6+1=15\), setki \(4+5+1=10\); wynik \(1055\). Kontrola: \(1055-568=487\).

**Twierdzenie 10 (kontrola przez działanie odwrotne).** Jeżeli \(a+b=c\), to dla \(c\ge b\) zachodzi \(c-b=a\). Jeżeli \(a=bq+r\), to ponowne pomnożenie i dodanie reszty odtwarza \(a\).

*Dowód.* Pierwsze wynika z jednoznaczności różnicy, drugie jest definicją ilorazu i reszty. \(\square\)

## 6. Szacowanie, reszty i błędy

**Definicja 9 (przedział oszacowania).** Zapis \(L\le x\le U\) oznacza, że dokładny wynik \(x\) leży w podanym przedziale. Oszacowanie jest certyfikatem tylko wtedy, gdy nierówności wynikają z uzasadnionych granic danych.

**Twierdzenie 11 (przenoszenie granic sumy).** Jeśli \(a\le x\le b\) i \(c\le y\le d\), to \(a+c\le x+y\le b+d\).

*Dowód.* Dodajemy stronami odpowiednie nierówności, korzystając z monotoniczności dodawania. \(\square\)

**Twierdzenie 12 (granice iloczynu nieujemnego).** Dla \(0\le a\le x\le b\) i \(0\le c\le y\le d\) mamy \(ac\le xy\le bd\).

*Dowód.* Mnożenie przez liczbę nieujemną zachowuje porządek: \(ac\le xc\le xy\le xd\le bd\). \(\square\)

**Przykład 7.** Jeśli w każdym z siedmiu pudełek jest od 18 do 20 kart, łączna liczba należy do \([126,140]\). Nie wolno bez pomiaru twierdzić, że wynosi 133.

**Definicja 10 (parzystość).** Liczba jest parzysta, jeśli ma postać \(2k\), a nieparzysta, jeśli ma postać \(2k+1\), dla \(k\in\mathbb N_0\).

**Twierdzenie 13 (parzystość sumy).** Suma dwóch nieparzystych liczb jest parzysta.

*Dowód.* \((2k+1)+(2l+1)=2(k+l+1)\). \(\square\)

**Twierdzenie 14 (parzystość iloczynu).** Iloczyn jest nieparzysty wtedy i tylko wtedy, gdy oba czynniki są nieparzyste.

*Dowód.* Iloczyn \((2k+1)(2l+1)=2(2kl+k+l)+1\) jest nieparzysty. Jeżeli jeden czynnik ma postać \(2k\), to iloczyn ma postać \(2(km)\), więc jest parzysty. \(\square\)

**Twierdzenie 15 (reszta sumy).** Jeżeli \(a=bq+r\), \(c=bs+t\), to reszta z dzielenia \(a+c\) przez \(b\) jest równa reszcie z dzielenia \(r+t\) przez \(b\).

*Dowód.* \(a+c=b(q+s)+(r+t)\). Zastosowanie dzielenia z resztą do \(r+t\) daje ten sam składnik resztowy co dzielenie całej sumy. \(\square\)

**Przykład 8.** Reszta z dzielenia \(28+39\) przez 5 wynosi 2, ponieważ reszty składników wynoszą 3 i 4, a \(3+4=5+2\).

**Uwaga o granicach modelu.** Liczba obiektów jest naturalna, lecz wynik pomiaru długości może być niecałkowity; model dzielenia z resztą nie zastępuje dzielenia liczb wymiernych. Liczba pudełek, w których zmieści się całość, zależy od tego, czy dopuszczamy niepełne pudełko: przy 17 kartach i pojemności 5 potrzeba czterech pudełek, mimo że iloraz całkowity wynosi trzy.

# Część B. Ćwiczenia z pełnymi rozwiązaniami

## Zestaw 1 — dodawanie i odejmowanie

**Zadanie 1.** W dwóch rozłącznych grupach jest 18 i 27 osób. Ile osób jest łącznie? *Rozwiązanie:* \(18+27=45\).

**Zadanie 2.** W zbiorze 18 osób 5 należy również do drugiego zbioru liczącego 27 osób. Ile jest różnych osób? *Rozwiązanie:* \(18+27-5=40\).

**Zadanie 3.** Oblicz \(356+489\). *Rozwiązanie:* \(6+9=15\), \(5+8+1=14\), \(3+4+1=8\); wynik \(845\).

**Zadanie 4.** Oblicz \(900-478\). *Rozwiązanie:* \(478+422=900\), więc różnica to \(422\).

**Zadanie 5.** Rozwiąż \(x+38=91\) w \(\mathbb N_0\). *Rozwiązanie:* \(x=91-38=53\); kontrola \(53+38=91\).

**Zadanie 6.** Czy istnieje \(x\in\mathbb N_0\), dla którego \(x+12=9\)? *Rozwiązanie:* Nie, bo \(x+12\ge12>9\).

**Zadanie 7.** Porównaj \((24+16)+9\) oraz \(24+(16+9)\). *Rozwiązanie:* Obie wartości wynoszą \(49\); równość gwarantuje łączność.

**Zadanie 8.** Oblicz \(1000-1-1\) od lewej strony. *Rozwiązanie:* \((1000-1)-1=998\).

**Zadanie 9.** Wyjaśnij, dlaczego \(8-(5-2)\ne(8-5)-2\). *Rozwiązanie:* Lewa strona to \(8-3=5\), prawa to \(3-2=1\).

**Zadanie 10.** Liczba zdjęć zwiększyła się z 68 do 105. O ile? *Rozwiązanie:* \(105-68=37\).

## Zestaw 2 — mnożenie i rozdzielność

**Zadanie 11.** Ile pól ma prostokąt 8 na 13? *Rozwiązanie:* \(8\cdot13=104\).

**Zadanie 12.** Oblicz \(17\cdot6\) przez rozdzielność. *Rozwiązanie:* \((10+7)\cdot6=60+42=102\).

**Zadanie 13.** Oblicz \(25\cdot16\). *Rozwiązanie:* \(25(4\cdot4)=(25\cdot4)\cdot4=400\).

**Zadanie 14.** W pięciu pudełkach są po 24 karty. Ile kart? *Rozwiązanie:* \(5\cdot24=120\).

**Zadanie 15.** Uzupełnij \(7(x+3)=7x+\square\). *Rozwiązanie:* \(\square=21\).

**Zadanie 16.** Czy \(a\cdot0=0\) także dla \(a=9999\)? *Rozwiązanie:* Tak, bo zero grup nie zawiera żadnego elementu.

**Zadanie 17.** Oblicz \(9\cdot11\) jako \(9(10+1)\). *Rozwiązanie:* \(90+9=99\).

**Zadanie 18.** Ile trójek można utworzyć, wybierając jedną z 2 koszulek, 3 czapek i 4 par butów? *Rozwiązanie:* \(2\cdot3\cdot4=24\).

**Zadanie 19.** Porównaj \(4(8+2)\) i \(4\cdot8+2\). *Rozwiązanie:* \(40\ne34\); rozdzielność wymaga przemnożenia obu składników.

**Zadanie 20.** Podaj liczbę kwadratów jednostkowych w układzie 12 wierszy i 7 kolumn. *Rozwiązanie:* \(12\cdot7=84\).

## Zestaw 3 — dzielenie z resztą

**Zadanie 21.** Podziel 29 przez 6 z resztą. *Rozwiązanie:* \(29=6\cdot4+5\), iloraz 4, reszta 5.

**Zadanie 22.** Podziel 48 przez 8. *Rozwiązanie:* \(48=8\cdot6+0\), iloraz 6, reszta 0.

**Zadanie 23.** Podziel 0 przez 7. *Rozwiązanie:* \(0=7\cdot0+0\), iloraz 0, reszta 0.

**Zadanie 24.** Czy \(31=5\cdot5+6\) jest poprawnym zapisem ilorazu i reszty? *Rozwiązanie:* Nie, bo \(6\ge5\); poprawnie \(31=5\cdot6+1\).

**Zadanie 25.** Ile pudełek pojemności 6 trzeba na 31 kart? *Rozwiązanie:* \(31=6\cdot5+1\), zatem potrzeba sześciu pudełek, ostatnie niepełne.

**Zadanie 26.** Podaj wszystkie możliwe reszty przy dzieleniu przez 4. *Rozwiązanie:* \(0,1,2,3\).

**Zadanie 27.** Dla dzielnika 9 i ilorazu 7 podaj najmniejszą i największą dzielną. *Rozwiązanie:* \(9\cdot7+0=63\) oraz \(9\cdot7+8=71\).

**Zadanie 28.** Reszty liczb \(a,b\) z dzielenia przez 6 wynoszą 4 i 5. Jaka jest reszta sumy? *Rozwiązanie:* \(4+5=9=6+3\), więc 3.

**Zadanie 29.** Czy istnieje reszta 10 przy dzieleniu przez 10? *Rozwiązanie:* Nie; reszta musi być mniejsza od dzielnika.

**Zadanie 30.** Rozwiąż \(5q+r=43\) przy \(0\le r<5\). *Rozwiązanie:* \(43=5\cdot8+3\), więc \(q=8,r=3\).

## Zestaw 4 — szacowanie, parzystość, rozumowanie

**Zadanie 31.** W sześciu pudełkach jest od 9 do 11 elementów. Oszacuj sumę. *Rozwiązanie:* \(54\le S\le66\).

**Zadanie 32.** Dwie liczby należą do przedziałów \([4,7]\) i \([10,12]\). Oszacuj sumę. *Rozwiązanie:* \(14\le S\le19\).

**Zadanie 33.** Oszacuj iloczyn liczb z przedziałów \([2,4]\) i \([3,5]\). *Rozwiązanie:* \(6\le P\le20\).

**Zadanie 34.** Czy suma 101 i 203 jest parzysta? *Rozwiązanie:* Tak, obie są nieparzyste, a \(101+203=304\).

**Zadanie 35.** Czy iloczyn 17 i 24 jest parzysty? *Rozwiązanie:* Tak, bo jeden czynnik jest parzysty: \(17\cdot24=408\).

**Zadanie 36.** Znajdź błąd: \(52+39=811\). *Rozwiązanie:* Dziewięć jedności i dwie jedności daje 11, więc zapisujemy 1 i przenosimy 1 do dziesiątek; \(52+39=91\).

**Zadanie 37.** Oblicz \(3+2\cdot(7-4)\). *Rozwiązanie:* Najpierw \(7-4=3\), potem \(2\cdot3=6\), na końcu \(3+6=9\).

**Zadanie 38.** Czy liczba 27 może być sumą dwóch parzystych? *Rozwiązanie:* Nie, bo \(2a+2b=2(a+b)\) jest parzyste, a 27 nie.

**Zadanie 39.** Liczba ma resztę 2 przy dzieleniu przez 5. Jaka jest reszta jej podwojenia? *Rozwiązanie:* \(2\cdot2=4\), więc reszta 4.

**Zadanie 40.** Uzasadnij, że \(a(b+1)=ab+a\). *Rozwiązanie:* Jest to szczególny przypadek rozdzielności: \(a(b+1)=ab+a\cdot1=ab+a\).

## Problemy syntetyczne

**Problem A (karty w albumach).** 137 fotografii układamy po 12 na stronie. Ile pełnych stron i ile zdjęć na ostatniej? Ile stron łącznie?

*Rozwiązanie.* \(137=12\cdot11+5\). Mamy 11 pełnych stron i 5 zdjęć na ostatniej, razem 12 stron. Błędem byłoby utożsamienie ilorazu 11 z liczbą potrzebnych stron.

**Problem B (weryfikacja dwóch metod).** Oblicz \(48\cdot25\) na dwa sposoby.

*Rozwiązanie.* Metoda 1: \((50-2)\cdot25=1250-50=1200\). Metoda 2: \(48\cdot(100:4)=4800:4=1200\); dzielenie jest dokładne. Zgodność wyników kontroluje rachunek.

**Problem C (nieznana reszta).** Dzielna jest mniejsza od 50, dzielnik wynosi 7, iloraz 6. Jakie dzielne są możliwe?

*Rozwiązanie.* \(a=42+r\), \(0\le r<7\), zatem \(a\in\{42,43,44,45,46,47,48\}\); wszystkie spełniają \(a<50\).

**Problem D (sprawdzanie danych).** W klasie jest 30 uczniów. W zajęciach plastycznych uczestniczy 18, a muzycznych 17. Czy możliwe, że nikt nie chodzi na oba zajęcia?

*Rozwiązanie.* Nie, bo wówczas rozłączne grupy miałyby \(18+17=35>30\) osób. Co najmniej \(18+17-30=5\) uczniów musi należeć do obu grup. Nie zakładamy, że każdy uczeń uczestniczy w którymś z zajęć.

## Kontrola redakcyjna

**Istniejące materiały:** F10.2 zawiera już formalny niezmiennik przeniesienia dla dowolnej podstawy. W E0-03 przedstawiono tylko wersję dziesiętną, właściwą dydaktycznie dla poziomu I; nie przypisuje się jej autorstwa całej teorii algorytmów pozycyjnych. Inne rozdziały F pozostają nietknięte.

**Ograniczenia:** Definicje oparte na liczebności dotyczą skończonych zbiorów; dzielenie w \(\mathbb N_0\) wymaga dodatniego dzielnika. Brak niezależnego dowodu formalnego i zweryfikowanego składu wydawniczego. Nie doliczać stron przed rzeczywistą integracją z monolitem 0.20.