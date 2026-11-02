---
title: "ONTOLOGIA LICZBY — TOM I"
subtitle: "E1-06. Planimetria — od własności figur do dowodów i zastosowań"
author: "Andrzej Mikulski"
date: "2 listopada 2026"
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Klasyfikacja:** E1-06, poziom I; minimum źródłowe 4 strony na punkt, odbiór wyłącznie po pełnej paginacji. Zakres: kąty, trójkąty, wielokąty, pola, podobieństwo, koło. E0-05 wprowadza punkty, odległość i figury; F17.3 bada geometrię dyskretną osi liczb całkowitych. Niniejszy tekst nie zastępuje ani nie zmienia tych opracowań. Pracujemy na płaszczyźnie euklidesowej.

# A. Definicje, twierdzenia, dowody

## 1. Długość, kąty, wielokąty

**Definicja 1 (łamana).** Łamana o wierzchołkach \(P_0,\ldots,P_n\) ma długość \(\sum_{i=1}^n|P_iP_{i-1}|\). Jeżeli \(P_n=P_0\), jest zamknięta. Jeżeli odcinki nie przecinają się poza wspólnymi końcami sąsiednich boków, nazywamy ją prostą.

**Definicja 2 (wielokąt prosty).** Wielokąt jest ograniczonym obszarem płaszczyzny wyznaczonym przez prostą łamaną zamkniętą wraz z jej wnętrzem. Obwód to suma długości boków.

**Definicja 3 (kąt).** Kąt mniejszy od pełnego obrotu jest częścią płaszczyzny między dwoma promieniami o wspólnym początku, wraz z miarą obrotu od jednego promienia do drugiego. Kąt prosty ma \(90^\circ\), pełny \(360^\circ\).

**Definicja 4 (trójkąt niezdegenerowany).** Trzy niewspółliniowe punkty \(A,B,C\) wyznaczają trójkąt o bokach \(a=|BC|\), \(b=|CA|\), \(c=|AB|\). Wysokość na bok jest odległością przeciwległego wierzchołka od prostej zawierającej bok.

**Twierdzenie 1 (nierówność trójkąta).** Dla boków niezdegenerowanego trójkąta zachodzą \(a<b+c\), \(b<c+a\), \(c<a+b\).

*Dowód.* Najkrótsza droga między dwoma punktami płaszczyzny euklidesowej jest odcinkiem. Łamana przez trzeci punkt ma długość większą od odcinka, ponieważ trzeci punkt nie leży na tym odcinku. Stosujemy argument do każdej pary wierzchołków. \(\square\)

**Twierdzenie 2 (istnienie trójkąta o danych bokach).** Dla dodatnich \(a,b,c\) istnieje trójkąt o takich bokach wtedy i tylko wtedy, gdy każdy bok jest mniejszy od sumy dwóch pozostałych.

*Dowód.* Konieczność daje T1. Dla dostateczności ustawmy \(A=(0,0)\), \(B=(c,0)\). Punkt \(C\) ma leżeć jednocześnie na okręgach o promieniach \(b\) wokół \(A\) i \(a\) wokół \(B\). Warunek przecięcia w dwóch punktach to \(|a-b|<c<a+b\), równoważny trzem nierównościom. Wybieramy jeden punkt przecięcia. \(\square\)

**Kontrprzykład 1.** Odcinki długości \(2,3,5\) nie tworzą trójkąta niezdegenerowanego, bo \(2+3=5\).

**Twierdzenie 3 (suma kątów trójkąta).** Suma miar kątów wewnętrznych trójkąta wynosi \(180^\circ\).

*Dowód.* Przez jeden wierzchołek prowadzimy prostą równoległą do przeciwległego boku. Kąty naprzemianległe przy pozostałych wierzchołkach są równe odpowiednim kątom przy tej prostej. Trzy kąty tworzą kąt półpełny. \(\square\)

**Twierdzenie 4 (suma kątów wielokąta wypukłego).** Dla wypukłego \(n\)-kąta, \(n\ge3\), suma kątów wewnętrznych wynosi \((n-2)180^\circ\).

*Dowód.* Przekątne poprowadzone z jednego wierzchołka dzielą wielokąt wypukły na dokładnie \(n-2\) trójkątów o rozłącznych wnętrzach. Sumujemy T3. \(\square\)

**Kontrprzykład 2.** Wzór \((n-2)180^\circ\) nie opisuje sumy kątów dowolnej samoprzecinającej się łamanej: pojęcie wnętrza i zwykłych kątów wielokąta wymaga odpowiedniej definicji.

## 2. Pola i rozkłady

**Definicja 5 (pole).** Pole \(S\) jest nieujemną miarą obszaru płaskiego, niezmienniczą względem przystawania i addytywną dla rozkładów na części o rozłącznych wnętrzach. Przyjmujemy pole kwadratu jednostkowego równe 1.

**Definicja 6 (równoległobok).** Czworokąt jest równoległobokiem, gdy obie pary przeciwległych boków są równoległe. Jego wysokość względem podstawy \(a\) to prostopadła odległość między prostymi zawierającymi przeciwległe boki.

**Twierdzenie 5 (pole równoległoboku).** \(S=ah\), gdzie \(a\) jest długością podstawy, a \(h\) odpowiadającą jej wysokością.

*Dowód.* Odcinając trójkąt przy jednym końcu równoległoboku i przesuwając go na drugi koniec, otrzymujemy prostokąt o bokach \(a,h\). Przesunięcie zachowuje pole, a rozkład jest addytywny. Dla przesunięć wykraczających poza sąsiedni bok stosujemy podział na skończenie wiele pasów lub argument ścinania. \(\square\)

**Twierdzenie 6 (pole trójkąta).** \(S=\frac12 ah\).

*Dowód.* Dwie przystające kopie trójkąta składają się w równoległobok o tej samej podstawie i wysokości. Z T5 jego pole to \(ah\), więc pole jednej kopii wynosi połowę. \(\square\)

**Twierdzenie 7 (pole trapezu).** Trapez o równoległych podstawach \(a,b\) i wysokości \(h\) ma pole \(S=\frac12(a+b)h\).

*Dowód.* Dwie przystające kopie trapezu, złączone po obrocie, tworzą równoległobok o podstawie \(a+b\) i wysokości \(h\). Dzielimy pole przez dwa. \(\square\)

**Kontrprzykład 3.** Dwa prostokąty o obwodzie \(20\) mogą mieć różne pola: \(1\times9\) ma pole 9, a \(5\times5\) ma pole 25. Obwód nie wyznacza pola.

**Twierdzenie 8 (nierówność pola prostokąta).** Wśród prostokątów o ustalonym obwodzie \(P>0\) największe pole ma kwadrat, równe \(P^2/16\).

*Dowód.* Jeśli boki to \(a,b>0\), to \(a+b=P/2\). Z \((a-b)^2\ge0\) wynika \(4ab\le(a+b)^2=P^2/4\), więc \(ab\le P^2/16\). Równość wtedy i tylko wtedy, gdy \(a=b\). \(\square\)

## 3. Kąt prosty, podobieństwo i twierdzenie Pitagorasa

**Definicja 7 (trójkąt prostokątny).** Trójkąt jest prostokątny, gdy jeden jego kąt ma \(90^\circ\). Bok naprzeciw tego kąta to przeciwprostokątna.

**Twierdzenie 9 (Pitagoras).** W trójkącie prostokątnym o przyprostokątnych \(a,b\) i przeciwprostokątnej \(c\) zachodzi \(a^2+b^2=c^2\).

*Dowód.* Ułóżmy cztery przystające trójkąty prostokątne o przyprostokątnych \(a,b\) w kwadracie o boku \(a+b\), tak aby wewnątrz pozostawał kwadrat o boku \(c\). Jego kąty są proste, gdyż dwa ostre kąty trójkąta sumują się do \(90^\circ\). Porównanie pól daje \((a+b)^2=4\cdot ab/2+c^2\), a po uproszczeniu \(a^2+b^2=c^2\). \(\square\)

**Twierdzenie 10 (odwrotność Pitagorasa).** Jeżeli dodatnie boki trójkąta spełniają \(a^2+b^2=c^2\), to kąt naprzeciw boku \(c\) jest prosty.

*Dowód.* Budujemy trójkąt prostokątny o przyprostokątnych \(a,b\). Z T9 jego przeciwprostokątna ma długość \(c\). Z cechy przystawania trójkątów SSS dany trójkąt jest do niego przystający, zatem ma kąt prosty. \(\square\)

**Kontrprzykład 4.** Dla boków \(2,3,4\) mamy \(2^2+3^2=13\ne16=4^2\); trójkąt istnieje, ale nie jest prostokątny.

**Definicja 8 (podobieństwo).** Dwa wielokąty są podobne w skali \(k>0\), jeżeli odpowiednie kąty są równe, a odpowiednie długości boków są w stałym stosunku \(k\); dla trójkątów wystarcza równość dwóch odpowiednich kątów (cecha AA).

**Twierdzenie 11 (skala pól).** Podobieństwo o współczynniku \(k\) mnoży obwód przez \(k\), a pole przez \(k^2\).

*Dowód.* Każdy bok jest \(k\) razy dłuższy, więc suma boków też. Triangulujemy wielokąt; każdy trójkąt ma podstawę i wysokość \(k\) razy większe, zatem pole \(k^2\) razy większe. Sumujemy pola. \(\square\)

**Twierdzenie 12 (Tales — proporcje).** W trójkącie \(ABC\), gdy \(D\in AB\), \(E\in AC\) oraz \(DE\parallel BC\), zachodzi \(AD/AB=AE/AC=DE/BC\).

*Dowód.* Kąty trójkątów \(ADE\) i \(ABC\) są parami równe przez równoległość, więc trójkąty są podobne (AA). Stosunki odpowiednich boków są równe. \(\square\)

**Kontrprzykład 5.** Podwojenie wszystkich boków trójkąta zwiększa pole czterokrotnie, a nie dwukrotnie.

## 4. Okręgi, koła i wielokąty foremne

**Definicja 9 (okrąg).** Okrąg o środku \(O\) i promieniu \(r>0\) to zbiór punktów \(P\) spełniających \(|OP|=r\). Koło zawiera także punkty o \(|OP|\le r\).

**Definicja 10 (liczba pi).** \(\pi\) jest stałą równą stosunkowi długości okręgu do jego średnicy w geometrii euklidesowej.

**Twierdzenie 13 (obwód okręgu).** Długość okręgu o promieniu \(r\) wynosi \(2\pi r\).

*Dowód.* Z definicji \(\pi=C/(2r)\); po przekształceniu otrzymujemy \(C=2\pi r\). \(\square\)

**Twierdzenie 14 (pole koła).** Pole koła promienia \(r\) wynosi \(\pi r^2\).

*Dowód.* Wpisujemy w koło foremne \(n\)-kąty. Dzieląc je na trójkąty o wierzchołku w środku, otrzymujemy \(S_n=\frac12 p_n h_n\), gdzie \(p_n\) jest obwodem wielokąta, a \(h_n=r\cos(\pi/n)\) jego apotemą. Dla \(n\to\infty\), \(p_n\to2\pi r\) oraz \(h_n\to r\). Wielokąty wyczerpują koło w granicy, więc \(S=\frac12(2\pi r)r=\pi r^2\). Przejście do granicy wymaga standardowej ciągłości miary pola. \(\square\)

**Twierdzenie 15 (kąt wpisany).** Kąt wpisany oparty na łuku niezawierającym jego wierzchołka ma miarę równą połowie miary odpowiadającego mu kąta środkowego.

*Dowód.* Łączymy wierzchołek kąta wpisanego ze środkiem okręgu. Powstają trójkąty równoramienne, w których kąty przy podstawie są równe. Rozpisując sumy kątów i rozważając położenie środka względem ramion kąta wpisanego, otrzymujemy dwukrotność kąta wpisanego jako kąt środkowy nad tym samym łukiem. \(\square\)

**Kontrprzykład 6.** Okrąg i koło nie są tym samym: środek należy do koła, ale dla \(r>0\) nie należy do okręgu.

**Definicja 11 (wycinek koła).** Wycinek o kącie środkowym \(\alpha\), \(0\le\alpha\le360^\circ\), stanowi część koła ograniczoną dwoma promieniami i odpowiednim łukiem.

**Twierdzenie 16 (pole wycinka).** \(S_\alpha=(\alpha/360^\circ)\pi r^2\).

*Dowód.* Pole koła jest proporcjonalne do miary kąta środkowego przy stałym promieniu: dla podziałów na równe kąty wynika to z przystawania wycinków, a dla dowolnego kąta z przybliżenia wymiernymi częściami obrotu i ciągłości pola. \(\square\)

**Definicja 12 (wielokąt foremny).** Wielokąt wypukły jest foremny, gdy ma równe wszystkie boki i kąty.

**Twierdzenie 17 (kąt wewnętrzny wielokąta foremnego).** W foremnym \(n\)-kącie kąt wewnętrzny ma miarę \((n-2)180^\circ/n\).

*Dowód.* Z T4 suma kątów to \((n-2)180^\circ\), a z foremności wszystkie kąty są równe. \(\square\)

**Kontrprzykład 7.** Równość wszystkich boków nie wystarcza do foremności: romb o kątach \(60^\circ\) i \(120^\circ\) nie jest kwadratem.

## 5. Własności przekątnych i osi symetrii

**Definicja 13 (przekątna).** Przekątna wielokąta łączy dwa niekolejne wierzchołki.

**Twierdzenie 18 (liczba przekątnych).** W wypukłym \(n\)-kącie, \(n\ge3\), liczba przekątnych wynosi \(n(n-3)/2\).

*Dowód.* Każdy z \(n\) wierzchołków łączy się przekątną z \(n-3\) wierzchołkami, gdy pominiemy jego samego i dwóch sąsiadów. Każdą przekątną policzono dwa razy. \(\square\)

**Definicja 14 (symetria osiowa).** Odbicie względem prostej \(l\) przyporządkowuje punktowi \(P\) punkt \(P'\), tak że \(l\) jest symetralną odcinka \(PP'\), a punkty na \(l\) pozostają nieruchome.

**Twierdzenie 19 (niezmienniczość odległości).** Odbicie osiowe zachowuje długości odcinków i pola figur.

*Dowód.* Po ustawieniu osi odbicia jako osi \(x\), odbicie ma postać \((x,y)\mapsto(x,-y)\). Kwadraty różnic współrzędnych nie zmieniają się, więc odległości pozostają te same. Odbicie jest izometrią; pole jest niezmiennicze względem przystawania. \(\square\)

**Kontrprzykład 8.** Nie każdy prostokąt ma cztery osie symetrii. Prostokąt niebędący kwadratem ma dokładnie dwie.

**Definicja 15 (środek symetrii).** Punkt \(O\) jest środkiem symetrii figury, gdy obrót o \(180^\circ\) wokół \(O\) odwzorowuje figurę na nią samą.

**Twierdzenie 20 (równoległobok).** Przekątne równoległoboku przecinają się w swoich środkach.

*Dowód.* W równoległoboku \(ABCD\) mamy \(\vec{AB}=\vec{DC}\), więc \(A+C=B+D\) w zapisie wektorowym. Zatem środki przekątnych \(AC\) i \(BD\), równe odpowiednio \((A+C)/2\) i \((B+D)/2\), pokrywają się. \(\square\)

**Kontrprzykład 9.** Przekątne dowolnego czworokąta nie muszą przecinać się w połowie: w trapezie o nierównych podstawach na ogół tak nie jest.

# B. Zadania rozwiązane — geometria obliczeniowa

## Zestaw 1: kąty i trójkąty

**Zadanie 1.** Czy boki \(4,5,8\) tworzą trójkąt? **Rozwiązanie:** Tak, \(4+5>8\), a pozostałe nierówności są oczywiste.

**Zadanie 2.** Czy boki \(2,6,9\) tworzą trójkąt? **Rozwiązanie:** Nie, \(2+6<9\).

**Zadanie 3.** Dwa kąty trójkąta mają \(45^\circ,65^\circ\). Trzeci? **Rozwiązanie:** \(180-45-65=70^\circ\).

**Zadanie 4.** Suma kątów sześciokąta wypukłego? **Rozwiązanie:** \((6-2)180^\circ=720^\circ\).

**Zadanie 5.** Kąt foremnego ośmiokąta? **Rozwiązanie:** \(6\cdot180^\circ/8=135^\circ\).

**Zadanie 6.** Liczba przekątnych siedmiokąta? **Rozwiązanie:** \(7(7-3)/2=14\).

**Zadanie 7.** Trójkąt równoramienny ma kąt wierzchołkowy \(40^\circ\). Kąty podstawy? **Rozwiązanie:** Po \(70^\circ\).

**Zadanie 8.** Trójkąt prostokątny ma jeden kąt ostry \(32^\circ\). Drugi? **Rozwiązanie:** \(58^\circ\).

**Zadanie 9.** Długości \(3,4,5\) — czy trójkąt prostokątny? **Rozwiązanie:** \(3^2+4^2=25=5^2\), więc tak.

**Zadanie 10.** Długości \(5,12,13\) — czy trójkąt prostokątny? **Rozwiązanie:** \(25+144=169\), więc tak.

## Zestaw 2: pola i obwody

**Zadanie 11.** Pole trójkąta o podstawie 10 i wysokości 7? **Rozwiązanie:** \(10\cdot7/2=35\).

**Zadanie 12.** Pole równoległoboku o podstawie 12 i wysokości 5? **Rozwiązanie:** \(60\).

**Zadanie 13.** Pole trapezu o podstawach 6 i 10 oraz wysokości 4? **Rozwiązanie:** \((6+10)4/2=32\).

**Zadanie 14.** Pole prostokąta \(8\times3\)? **Rozwiązanie:** \(24\).

**Zadanie 15.** Obwód prostokąta \(8\times3\)? **Rozwiązanie:** \(2(8+3)=22\).

**Zadanie 16.** Prostokąt ma obwód 24 i jeden bok 5. Drugi? **Rozwiązanie:** \(a+b=12\), więc \(b=7\).

**Zadanie 17.** Największe pole prostokąta o obwodzie 24? **Rozwiązanie:** \(24^2/16=36\), dla kwadratu \(6\times6\).

**Zadanie 18.** Pole rombu o przekątnych 8 i 10? **Rozwiązanie:** \(8\cdot10/2=40\), gdyż przekątne rombu są prostopadłe.

**Zadanie 19.** Pole trójkąta prostokątnego o przyprostokątnych 9 i 12? **Rozwiązanie:** \(54\).

**Zadanie 20.** Pole trójkąta o podstawie 20 i wysokości 0? **Rozwiązanie:** \(0\); figura jest zdegenerowana.

## Zestaw 3: Pitagoras i podobieństwo

**Zadanie 21.** Przekątna prostokąta \(6\times8\)? **Rozwiązanie:** \(\sqrt{36+64}=10\).

**Zadanie 22.** Przeciwprostokątna przy \(a=7,b=24\)? **Rozwiązanie:** \(\sqrt{49+576}=25\).

**Zadanie 23.** Brakująca przyprostokątna przy \(c=13,a=5\)? **Rozwiązanie:** \(\sqrt{169-25}=12\).

**Zadanie 24.** Drabina 5 m oparta 3 m od ściany. Wysokość? **Rozwiązanie:** \(\sqrt{25-9}=4\) m.

**Zadanie 25.** Długości boków podobnych figur są w stosunku \(3:4\). Stosunek pól? **Rozwiązanie:** \(9:16\).

**Zadanie 26.** Figura o polu 20 jest powiększona dwukrotnie. Pole? **Rozwiązanie:** \(20\cdot4=80\).

**Zadanie 27.** Obwód 30 po zmniejszeniu w skali \(1:3\)? **Rozwiązanie:** \(10\).

**Zadanie 28.** W trójkącie odcinek równoległy do podstawy ma długość 6, a skala mniejszego trójkąta to \(2/3\). Podstawa? **Rozwiązanie:** \(6/(2/3)=9\).

**Zadanie 29.** Dwa boki trójkąta prostokątnego mają 8 i 15 jako przyprostokątne. Trzeci bok? **Rozwiązanie:** \(17\).

**Zadanie 30.** Czy \(1,1,\sqrt2\) tworzą trójkąt prostokątny? **Rozwiązanie:** Tak, \(1^2+1^2=(\sqrt2)^2\).

## Zestaw 4: koło i okrąg

**Zadanie 31.** Obwód okręgu promienia 5? **Rozwiązanie:** \(10\pi\).

**Zadanie 32.** Pole koła promienia 5? **Rozwiązanie:** \(25\pi\).

**Zadanie 33.** Pole koła średnicy 12? **Rozwiązanie:** Promień 6, więc \(36\pi\).

**Zadanie 34.** Promień koła o polu \(49\pi\)? **Rozwiązanie:** \(7\).

**Zadanie 35.** Obwód okręgu o średnicy 14? **Rozwiązanie:** \(14\pi\).

**Zadanie 36.** Pole półkola promienia 4? **Rozwiązanie:** \(8\pi\).

**Zadanie 37.** Pole ćwiartki koła promienia 8? **Rozwiązanie:** \(16\pi\).

**Zadanie 38.** Pole wycinka \(60^\circ\) promienia 6? **Rozwiązanie:** \((60/360)\pi36=6\pi\).

**Zadanie 39.** Długość łuku \(90^\circ\) promienia 10? **Rozwiązanie:** \((90/360)2\pi10=5\pi\).

**Zadanie 40.** Kąt wpisany oparty na łuku \(100^\circ\)? **Rozwiązanie:** \(50^\circ\).

## Zestaw 5: dowodzenie i kontrola założeń

**Zadanie 41.** Wykaż, że w trójkącie równobocznym każdy kąt ma \(60^\circ\). **Rozwiązanie:** Kąty są równe i sumują się do \(180^\circ\), więc każdy to \(60^\circ\).

**Zadanie 42.** Czy romb musi być kwadratem? **Rozwiązanie:** Nie; romb z kątem \(60^\circ\) ma wszystkie boki równe, lecz nie ma kątów prostych.

**Zadanie 43.** Czy każdy kwadrat jest prostokątem? **Rozwiązanie:** Tak, ma cztery kąty proste.

**Zadanie 44.** Czy każdy prostokąt jest kwadratem? **Rozwiązanie:** Nie, prostokąt \(2\times3\) nie ma równych boków.

**Zadanie 45.** Ile przekątnych ma dziesięciokąt? **Rozwiązanie:** \(10\cdot7/2=35\).

**Zadanie 46.** Czy figura o większym obwodzie zawsze ma większe pole? **Rozwiązanie:** Nie: prostokąt \(1\times9\) ma obwód 20 i pole 9, a kwadrat \(4\times4\) ma obwód 16 i pole 16.

**Zadanie 47.** Wykaż, że środek okręgu nie należy do okręgu promienia dodatniego. **Rozwiązanie:** Jego odległość od siebie wynosi 0, a nie \(r>0\).

**Zadanie 48.** Jak zmienia się pole koła przy potrojeniu promienia? **Rozwiązanie:** \(S'=\pi(3r)^2=9S\).

**Zadanie 49.** Jak zmienia się obwód okręgu przy potrojeniu promienia? **Rozwiązanie:** \(C'=2\pi(3r)=3C\).

**Zadanie 50.** Wykaż, że przekątne prostokąta są równe. **Rozwiązanie:** Każda jest przeciwprostokątną trójkąta o przyprostokątnych \(a,b\), więc obie mają długość \(\sqrt{a^2+b^2}\).

## Problemy syntetyczne

**Problem A (projekt ogrodzenia).** Prostokątny ogród ma obwód 40 m. Jakie wymiary maksymalizują pole i ile ono wynosi?

*Rozwiązanie.* \(a+b=20\). Z \((a-b)^2\ge0\) mamy \(ab\le100\). Maksimum to 100 m² dla kwadratu \(10\times10\) m.

**Problem B (dokładne pole).** W trójkącie prostokątnym przeciwprostokątna ma 10, jedna przyprostokątna 6. Oblicz pole.

*Rozwiązanie.* Druga przyprostokątna ma \(\sqrt{100-36}=8\). Pole to \(6\cdot8/2=24\).

**Problem C (mapa).** Skala mapy wynosi \(1:25000\). Odcinek 8 cm odpowiada jakiej odległości rzeczywistej?

*Rozwiązanie.* \(8\cdot25000=200000\) cm = 2000 m = 2 km. Skalowanie dotyczy długości; powierzchnie skalują się kwadratowo.

**Problem D (wycinek).** Koło promienia 12 podzielono na trzy wycinki o kątach \(90^\circ\), \(120^\circ\) i pozostałym. Oblicz pola.

*Rozwiązanie.* Pozostały kąt to \(150^\circ\). Pole całego koła to \(144\pi\); pola kolejno: \(36\pi\), \(48\pi\), \(60\pi\). Ich suma wynosi \(144\pi\).

**Problem E (triangulacja).** Wypukły siedmiokąt rozcięto przekątnymi z jednego wierzchołka. Ile powstało trójkątów i jaka jest suma kątów?

*Rozwiązanie.* Powstaje \(7-2=5\) trójkątów; suma kątów to \(5\cdot180^\circ=900^\circ\).

**Problem F (kryterium równości pól).** Dwa trójkąty mają tę samą podstawę i tę samą wysokość, lecz różne kształty. Czy mają równe pola?

*Rozwiązanie.* Tak. Każdy ma pole \(ah/2\). Sama równość pola nie oznacza przystawania.

# C. Zakres weryfikacji i ograniczenia

Dowody korzystają z klasycznej geometrii euklidesowej, własności miary pola, przystawania i podobieństwa. Argument graniczny dla pola koła wymaga ciągłości miary; nie jest dowodem w aksjomatyce ograniczonej do samych konstrukcji elementarnych. Rozdział nie zastępuje E0-05 ani F17.3. Status: materiał opracowany; pełny skład PDF, CI, kontrola 4 stron oraz integracja z monolitem 0.20 wymagają odrębnych dowodów. Historycznie zintegrowane 585 stron bez zmian; 1222 nie jest obowiązkowym celem; finalny PDF tomu musi mieć mniej niż 99 000 000 bajtów.
