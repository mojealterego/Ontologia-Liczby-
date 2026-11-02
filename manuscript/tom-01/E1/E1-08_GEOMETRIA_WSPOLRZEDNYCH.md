---
title: "Ontologia Liczby — Tom I"
subtitle: "E1-08. Geometria współrzędnych: od punktu do certyfikatu geometrycznego"
author: "Andrzej Mikulski"
date: "2026-11-02"
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Klasyfikacja:** E1-08, poziom I (minimum 4 strony na punkt, weryfikowane dopiero po składzie). Rozdział szkolny: punkty, wektory przesunięcia, odległość, środek odcinka, nachylenie, proste, pola, symetrie i współrzędne w zadaniach. Nie zastępuje E0-05, E1-06 ani suplementu F24.1 o dokładnych predykatach obliczeniowych. **Stan:** samodzielny materiał przed integracją z monolitem 0.20.

# A. Definicje i konstrukcje

**D1 (układ współrzędnych).** W kartezjańskim układzie prostokątnym na płaszczyźnie punktowi \(P\) odpowiada para \((x_P,y_P)\in\mathbb R^2\); osie są prostopadłe i mają jednakową jednostkę długości.

**D2 (wektor przemieszczenia).** Dla \(A=(a_1,a_2)\), \(B=(b_1,b_2)\) określamy \(\overrightarrow{AB}=(b_1-a_1,b_2-a_2)\).

**D3 (długość wektora).** Dla \(v=(v_1,v_2)\), \(\|v\|=\sqrt{v_1^2+v_2^2}\).

**D4 (odległość punktów).** \(d(A,B)=\|\overrightarrow{AB}\|\).

**D5 (środek odcinka).** \(M(A,B)=((a_1+b_1)/2,(a_2+b_2)/2)\).

**D6 (punkt podziału).** Dla \(t\in\mathbb R\), \(P_t(A,B)=((1-t)a_1+tb_1,(1-t)a_2+tb_2)\). Dla \(0\le t\le1\) leży na odcinku \(AB\).

**D7 (iloczyn skalarny).** \(u\cdot v=u_1v_1+u_2v_2\).

**D8 (wyznacznik płaski).** \(\det(u,v)=u_1v_2-u_2v_1\). Jego znak rozróżnia orientację pary niezerowych, niekolinearnych wektorów.

**D9 (prosta w postaci ogólnej).** Dla \((a,b)\ne(0,0)\) zbiór \(L(a,b,c)=\{(x,y):ax+by+c=0\}\) jest prostą.

**D10 (współczynnik kierunkowy).** Prosta niepionowa ma postać \(y=mx+q\), gdzie \(m\) jest zmianą \(y\) przypadającą na jednostkową zmianę \(x\).

**D11 (kolinearność).** Trzy punkty \(A,B,C\) są współliniowe wtedy i tylko wtedy, gdy \(\det(\overrightarrow{AB},\overrightarrow{AC})=0\).

**D12 (pole zorientowane).** Dla trójkąta \(ABC\) określamy \(S_{\rm or}=\frac12\det(\overrightarrow{AB},\overrightarrow{AC})\); pole geometryczne wynosi \(|S_{\rm or}|\).

**D13 (okrąg).** Okrąg o środku \(O=(h,k)\) i promieniu \(r>0\) jest zbiorem \((x-h)^2+(y-k)^2=r^2\).

**D14 (symetrie osiowe).** Względem osi \(Ox\) punkt \((x,y)\) przechodzi w \((x,-y)\), względem \(Oy\) w \((-x,y)\), a względem początku układu w \((-x,-y)\).

# B. Twierdzenia i dowody

**T1 (wzór na odległość).** Dla \(A=(a_1,a_2)\), \(B=(b_1,b_2)\) mamy
\[
d(A,B)=\sqrt{(b_1-a_1)^2+(b_2-a_2)^2}.
\]
*Dowód.* Odcinki równoległe do osi o długościach \(|b_1-a_1|\) i \(|b_2-a_2|\) są przyprostokątnymi trójkąta prostokątnego o przeciwprostokątnej \(AB\). Twierdzenie Pitagorasa daje kwadrat odległości; wybieramy nieujemny pierwiastek. \(\square\)

**T2 (metryczne własności odległości).** \(d(A,B)\ge0\), \(d(A,B)=0\iff A=B\), \(d(A,B)=d(B,A)\).
*Dowód.* Suma kwadratów jest nieujemna i znika dokładnie wtedy, gdy obie różnice współrzędnych znikają. Zamiana kolejności zmienia znaki różnic, nie ich kwadraty. \(\square\)

**T3 (środek jest równoodległy).** \(d(A,M(A,B))=d(M(A,B),B)=d(A,B)/2\).
*Dowód.* \(\overrightarrow{AM}=\frac12\overrightarrow{AB}=\overrightarrow{MB}\), a długość wektora po pomnożeniu przez \(1/2\) dzieli się przez dwa. \(\square\)

**T4 (odcinek parametryczny).** Dla \(0\le t\le1\) zachodzi \(d(A,P_t)=t\,d(A,B)\) i \(d(P_t,B)=(1-t)d(A,B)\).
*Dowód.* \(\overrightarrow{AP_t}=t\overrightarrow{AB}\), a \(\overrightarrow{P_tB}=(1-t)\overrightarrow{AB}\); oba współczynniki są nieujemne. \(\square\)

**T5 (równoległość z wyznacznika).** Dwa niezerowe wektory \(u,v\) są równoległe wtedy i tylko wtedy, gdy \(\det(u,v)=0\).
*Dowód.* Jeśli \(v=tu\), wyznacznik znika przez rachunek. Odwrotnie, gdy \(u_1\ne0\), przyjmij \(t=v_1/u_1\); z \(u_1v_2-u_2v_1=0\) wynika \(v_2=tu_2\). Gdy \(u_1=0\), mamy \(u_2\ne0\), a równość wyznacznika wymusza \(v_1=0\), więc również \(v=tu\). \(\square\)

**T6 (pole trójkąta).** \(S(ABC)=\frac12|\det(B-A,C-A)|\).
*Dowód.* Wybierz wektor podstawy \(u=B-A\). Wysokość z \(C\) jest wartością bezwzględną składowej \(C-A\) prostopadłej do \(u\). Zatem \(|\det(u,C-A)|=\|u\|h\); dzieląc przez dwa, dostajemy pole. Przypadek \(u=0\) daje obie strony równe zero. \(\square\)

**T7 (równanie prostej przez dwa punkty).** Dla \(A\ne B\), punkt \(P=(x,y)\) leży na prostej \(AB\) dokładnie wtedy, gdy
\[
(b_2-a_2)(x-a_1)-(b_1-a_1)(y-a_2)=0.
\]
*Dowód.* Warunek jest równoważny \(\det(B-A,P-A)=0\), a T5 mówi, że wektory są równoległe. \(\square\)

**T8 (nachylenie).** Dla \(a_1\ne b_1\), prosta przez \(A,B\) ma \(m=(b_2-a_2)/(b_1-a_1)\).
*Dowód.* Z T7, po podzieleniu przez niezerowe \(b_1-a_1\), otrzymujemy \(y-a_2=m(x-a_1)\). \(\square\)

**T9 (prostopadłość).** Dwa niezerowe wektory \(u,v\) są prostopadłe wtedy i tylko wtedy, gdy \(u\cdot v=0\).
*Dowód.* Tożsamość \(\|u+v\|^2=\|u\|^2+2u\cdot v+\|v\|^2\) wynika z rozwinięcia kwadratów. Z twierdzenia Pitagorasa i jego odwrotności dla trójkąta z bokami \(u,v,u+v\) otrzymujemy równoważność. \(\square\)

**T10 (równoległość prostych o nachyleniu).** Dwie różne proste niepionowe \(y=m_1x+q_1\) i \(y=m_2x+q_2\) są równoległe wtedy i tylko wtedy, gdy \(m_1=m_2\).
*Dowód.* Ich wektory kierunkowe to \((1,m_1)\), \((1,m_2)\). Z T5 równoległość zachodzi wtedy i tylko wtedy, gdy wyznacznik \(m_2-m_1\) znika. \(\square\)

**T11 (odległość od prostej).** Dla \(L:ax+by+c=0\), \((a,b)\ne(0,0)\), i \(P=(p,q)\):
\[
d(P,L)=\frac{|ap+bq+c|}{\sqrt{a^2+b^2}}.
\]
*Dowód.* Wektor normalny \(n=(a,b)\). Punkt \(Q=P-\frac{ap+bq+c}{a^2+b^2}n\) spełnia równanie prostej. Odcinek \(PQ\) jest do niej prostopadły, a jego długość to podany iloraz. \(\square\)

**T12 (symetria zachowuje odległości).** Odbicie \((x,y)\mapsto(x,-y)\) zachowuje odległość dowolnej pary punktów.
*Dowód.* Różnica pierwszych współrzędnych nie zmienia się, druga zmienia znak. Ich kwadraty są takie same; T1 kończy dowód. \(\square\)

**T13 (przesunięcie zachowuje pola).** Dla \(v\in\mathbb R^2\), \(S(A+v,B+v,C+v)=S(A,B,C)\).
*Dowód.* Wektory różnicowe po przesunięciu pozostają \(B-A\) i \(C-A\). Stosujemy T6. \(\square\)

**T14 (równanie okręgu).** Punkt \(P=(x,y)\) leży na okręgu o środku \((h,k)\) i promieniu \(r>0\) dokładnie wtedy, gdy \((x-h)^2+(y-k)^2=r^2\).
*Dowód.* Warunek \(d(P,O)=r\) jest równoważny wskazanej równości po zastosowaniu T1 i podniesieniu obu nieujemnych stron do kwadratu. \(\square\)

**T15 (przecięcie dwóch nieparalelnych prostych).** Układ \(a_1x+b_1y=c_1,\ a_2x+b_2y=c_2\) ma dokładnie jedno rozwiązanie, gdy \(\Delta=a_1b_2-a_2b_1\ne0\), mianowicie
\[
x=\frac{c_1b_2-c_2b_1}{\Delta},\qquad
y=\frac{a_1c_2-a_2c_1}{\Delta}.
\]
*Dowód.* Pomnożenie pierwszego równania przez \(b_2\), drugiego przez \(b_1\) i odjęcie eliminuje \(y\), dając \(\Delta x=c_1b_2-c_2b_1\). Analogiczna eliminacja \(x\) daje wzór na \(y\). Każde rozwiązanie musi mieć te współrzędne, a podstawienie potwierdza, że są rozwiązaniem. \(\square\)

**T16 (wzór sznurowadłowy).** Dla kolejnych wierzchołków prostego wielokąta \(P_1,\ldots,P_n\) jego pole jest równe
\[
\frac12\left|\sum_{i=1}^{n}(x_i y_{i+1}-x_{i+1}y_i)\right|,\quad P_{n+1}=P_1.
\]
*Dowód.* Zsumuj zorientowane pola trójkątów \(OP_iP_{i+1}\), gdzie \(O=(0,0)\). Wewnętrzne odcinki triangulacji redukują się parami; suma pozostaje zorientowanym polem wielokąta. Dla wielokąta prostego o spójnej orientacji wartość bezwzględna daje pole geometryczne. \(\square\)

# C. Kontrprzykłady i kontrola dziedziny

**K1.** Dla \(A=(1,2),B=(4,6)\) odległość wynosi \(5\), a nie \(|4-1|+|6-2|=7\). Suma różnic to inna metryka.

**K2.** Współczynnik kierunkowy prostej \(x=3\) nie jest zerem; jest niezdefiniowany. Nachylenie \(0\) ma prosta pozioma.

**K3.** Proste \(y=2x+1\) i \(y=2x+3\) nie są tą samą prostą mimo równego nachylenia.

**K4.** Współliniowość \(A,B,C\) nie oznacza, że \(B\) leży między \(A\) i \(C\): \((0,0),(3,0),(1,0)\) są współliniowe, ale \(B\) nie leży na odcinku \(AC\).

**K5.** Pole zorientowane może być ujemne: \(\det((0,1),(1,0))=-1\); pole geometryczne pozostaje nieujemne.

**K6.** Z równości \(u\cdot v=0\) nie wolno wnioskować o kącie prostym, gdy jeden wektor jest zerowy; definicja kąta dwóch niezerowych wektorów tego nie obejmuje.

**K7.** Równanie \(0x+0y+1=0\) nie wyznacza prostej, lecz zbiór pusty; wymagamy \((a,b)\ne(0,0)\).

**K8.** Punkty \((1,0)\) i \((0,1)\) są jednakowo odległe od początku, ale nie są tym samym punktem.

**K9.** Równość pól nie oznacza przystawania: trójkąty o podstawach \(2\), \(4\) i wysokościach \(4\), \(2\) mają jednakowe pole \(4\).

**K10.** Równość wyznaczników \(0\) dla dwóch wektorów nie oznacza ich prostopadłości: \((1,0)\), \((2,0)\) są równoległe.

# D. Zadania z rozwiązaniami
**Zadanie 1.** Wyznacz wektor od A=(2,-1) do B=(5,3).

*Rozwiązanie.* \((3,4)\).

**Zadanie 2.** Oblicz odległość między (0,0) a (6,8).

*Rozwiązanie.* \(\sqrt{36+64}=10\).

**Zadanie 3.** Oblicz odległość między (-2,3) a (1,-1).

*Rozwiązanie.* \(\sqrt{9+16}=5\).

**Zadanie 4.** Wyznacz środek odcinka o końcach (2,4) i (8,10).

*Rozwiązanie.* \((5,7)\).

**Zadanie 5.** Wyznacz środek odcinka o końcach (-5,7) i (3,-1).

*Rozwiązanie.* \((-1,3)\).

**Zadanie 6.** Wyznacz punkt w 1/4 drogi od (0,0) do (8,12).

*Rozwiązanie.* \((2,3)\).

**Zadanie 7.** Wyznacz punkt w 3/4 drogi od (2,2) do (10,6).

*Rozwiązanie.* \((8,5)\).

**Zadanie 8.** Sprawdź, czy (0,0),(2,2),(5,5) są współliniowe.

*Rozwiązanie.* Tak, \(\det((2,2),(5,5))=10-10=0\).

**Zadanie 9.** Sprawdź, czy (0,0),(2,2),(5,4) są współliniowe.

*Rozwiązanie.* Nie, wyznacznik wynosi \(8-10=-2\).

**Zadanie 10.** Wyznacz pole trójkąta (0,0),(4,0),(0,3).

*Rozwiązanie.* \(\frac12|4\cdot3|=6\).

**Zadanie 11.** Wyznacz pole trójkąta (1,1),(5,1),(1,4).

*Rozwiązanie.* \(\frac12|4\cdot3|=6\).

**Zadanie 12.** Wyznacz nachylenie prostej przez (1,2),(3,8).

*Rozwiązanie.* \(m=(8-2)/(3-1)=3\).

**Zadanie 13.** Wyznacz prostą przez (1,2) o nachyleniu 3.

*Rozwiązanie.* \(y-2=3(x-1)\), czyli \(y=3x-1\).

**Zadanie 14.** Wyznacz równanie prostej przez (2,1),(2,5).

*Rozwiązanie.* \(x=2\); jest pionowa.

**Zadanie 15.** Czy proste y=2x+1 i y=2x-4 są równoległe?

*Rozwiązanie.* Tak, obie mają nachylenie \(2\), a różne wyrazy wolne.

**Zadanie 16.** Czy wektory (2,3),(-3,2) są prostopadłe?

*Rozwiązanie.* Tak, \(2(-3)+3(2)=0\).

**Zadanie 17.** Czy wektory (1,2),(2,4) są równoległe?

*Rozwiązanie.* Tak, wyznacznik \(1\cdot4-2\cdot2=0\).

**Zadanie 18.** Oblicz odległość (0,0) od prostej 3x+4y-20=0.

*Rozwiązanie.* \(20/\sqrt{9+16}=4\).

**Zadanie 19.** Oblicz odległość (2,1) od prostej x=5.

*Rozwiązanie.* \(3\).

**Zadanie 20.** Podaj obraz (3,-4) w symetrii względem Ox.

*Rozwiązanie.* \((3,4)\).

**Zadanie 21.** Podaj obraz (3,-4) w symetrii względem Oy.

*Rozwiązanie.* \((-3,-4)\).

**Zadanie 22.** Podaj obraz (3,-4) w symetrii względem początku.

*Rozwiązanie.* \((-3,4)\).

**Zadanie 23.** Sprawdź, czy (3,4) leży na okręgu x²+y²=25.

*Rozwiązanie.* Tak, \(9+16=25\).

**Zadanie 24.** Wyznacz promień okręgu (x-2)²+(y+1)²=49.

*Rozwiązanie.* \(r=7\), środek \((2,-1)\).

**Zadanie 25.** Rozwiąż układ x+y=5, x-y=1.

*Rozwiązanie.* Dodajemy równania: \(2x=6\), \(x=3\), \(y=2\).

**Zadanie 26.** Rozwiąż układ 2x+y=7, x-y=2.

*Rozwiązanie.* Z drugiego \(y=x-2\), stąd \(3x=9\), więc \((x,y)=(3,1)\).

**Zadanie 27.** Oblicz pole prostokąta o wierzchołkach (0,0),(5,0),(5,2),(0,2).

*Rozwiązanie.* Boki mają długości \(5,2\), więc pole \(10\).

**Zadanie 28.** Oblicz pole trójkąta (0,0),(2,0),(1,3) wzorem wyznacznika.

*Rozwiązanie.* \(\frac12|2\cdot3|=3\).

**Zadanie 29.** Czy (1,1) należy do prostej 2x+3y=5?

*Rozwiązanie.* Tak, \(2+3=5\).

**Zadanie 30.** Czy (1,2) należy do prostej 2x+3y=5?

*Rozwiązanie.* Nie, \(2+6=8\ne5\).

**Zadanie 31.** Wyznacz brakujący koniec odcinka, gdy środek to (3,4), a A=(1,7).

*Rozwiązanie.* Z \(B=2M-A\) otrzymujemy \(B=(5,1)\).

**Zadanie 32.** Oblicz pole trójkąta (0,0),(4,1),(1,4).

*Rozwiązanie.* \(\frac12|16-1|=15/2\).

**Zadanie 33.** Wyznacz odległość (1,1) od prostej x+y=0.

*Rozwiązanie.* \(2/\sqrt2=\sqrt2\).

**Zadanie 34.** Zbadaj położenie punktu (0,0) względem okręgu o środku (3,4), promieniu 6.

*Rozwiązanie.* Odległość od środka to \(5<6\), więc punkt leży wewnątrz koła, nie na okręgu.

**Zadanie 35.** Wykaż, że przesunięcie o (7,-3) zachowuje długość odcinka.

*Rozwiązanie.* Dla końców \(A,B\) różnica \((B+v)-(A+v)=B-A\), zatem odległość się nie zmienia.

**Zadanie 36.** Wyznacz współrzędne środka ciężkości trójkąta (0,0),(6,0),(0,9).

*Rozwiązanie.* Średnia współrzędnych wierzchołków daje \((2,3)\); przecięcie środkowych wynika z podziału w stosunku \(2:1\).

# E. Zagadnienia przekrojowe i granice dowodów

**Problem 1 (rekonstrukcja trójkąta).** Punkty \(A=(0,0)\), \(B=(6,0)\), \(C=(2,4)\). Znajdź pole, długości boków i wysokość do \(AB\).

*Rozwiązanie.* Pole \(S=\frac12|6\cdot4|=12\). Boki: \(AB=6\), \(AC=\sqrt{20}=2\sqrt5\), \(BC=\sqrt{32}=4\sqrt2\). Wysokość do poziomej podstawy to \(|4|=4\), co potwierdza \(S=6\cdot4/2\).

**Problem 2 (certyfikat współliniowości).** Dla wymiernych współrzędnych wykaż, że wynik testu wyznacznika jest dokładny bez obliczeń zmiennoprzecinkowych.

*Rozwiązanie.* Wyznacznik to suma i różnica iloczynów liczb wymiernych. Działania te pozostają w \(\mathbb Q\); po sprowadzeniu do wspólnego mianownika znak wyznacznika jest znakiem całkowitego licznika. Nie trzeba stosować przybliżeń. Rozwinięcie do odpornej arytmetyki geometrycznej jest opisane w istniejącym F24.1.

**Problem 3 (kwadrat bez rysunku).** Punkty \(A=(0,0),B=(2,1),C=(1,3),D=(-1,2)\). Udowodnij, że tworzą kwadrat.

*Rozwiązanie.* \(\overrightarrow{AB}=(2,1)\), \(\overrightarrow{BC}=(-1,2)\), \(\overrightarrow{CD}=(-2,-1)\), \(\overrightarrow{DA}=(1,-2)\). Każdy bok ma długość \(\sqrt5\); iloczyn skalarny sąsiednich boków to \(-2+2=0\). Zatem figura ma cztery równe boki i kąt prosty, więc jest kwadratem.

**Uwagi o zakresie.** Definicje pól wielokątów i interpretacja wyznacznika korzystają ze standardowej geometrii euklidesowej. Wzór sznurowadłowy wymaga *prostego* wielokąta i kolejności wierzchołków wzdłuż jego brzegu; dla samoprzecinającej się łamanej suma daje pole algebraiczne, nie sumę pól obszarów. Nie deklaruje się formalizacji maszynowej twierdzeń. Wstęp historyczny i wcześniejsze rozdziały pozostają nietknięte. Nowe strony nie są zaliczane do historycznych 585 przed integracją z rzeczywistym monolitem 0.20. Docelowy PDF tomu ma mieć mniej niż 99 000 000 bajtów.
