---
title: 'ONTOLOGIA LICZBY — TOM I'
subtitle: 'E0-05. Figury i przestrzeń — od rozpoznawania kształtów do niezmienników symetrii'
author: 'Andrzej Mikulski'
date: '2 listopada 2026'
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Przyporządkowanie:** E0-05, poziom I: figury płaskie, bryły, symetrie, orientacja przestrzenna. To dydaktyczny kod autorski, nie kod MSC2020; związek z dziedziną MSC 51 i dydaktyką MSC 97 jest tematyczny. W części formalnej stosujemy płaszczyznę euklidesową \(\mathbb R^2\), ale przykłady zaczynają się od obiektów i siatek. **Status:** źródło przed integracją z monolitem 0.20. 

# Część A. Definicje, modele, twierdzenia i dowody

## 1. Obiekt, jego kształt i położenie

**Definicja 1 (punkt i układ współrzędnych).** Punkt na płaszczyźnie reprezentujemy parą \(P=(x,y)\). Współrzędna \(x\) wskazuje położenie wzdłuż osi poziomej, \(y\) — wzdłuż osi pionowej. Wybór osi i jednostki jest częścią modelu; punkt nie zmienia się tylko dlatego, że wybierzemy inny opis.

**Definicja 2 (odcinek).** Dla punktów \(A,B\) odcinek \([A,B]\) jest zbiorem punktów \((1-t)A+tB\), gdzie \(0\le t\le1\). Długość odcinka oznaczamy \(|AB|\).

**Definicja 3 (odległość euklidesowa).** Dla \(A=(x_1,y_1)\), \(B=(x_2,y_2)\) przyjmujemy
\[
d(A,B)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.
\]
Pierwiastek jest nieujemny. Dla poziomego odcinka długość to wartość bezwzględna różnicy współrzędnych poziomych.

**Twierdzenie 1 (symetria odległości).** Dla dowolnych punktów \(A,B\), \(d(A,B)=d(B,A)\), a \(d(A,B)=0\) wtedy i tylko wtedy, gdy \(A=B\).

*Dowód.* Zamiana kolejności punktów zmienia znaki różnic współrzędnych, lecz nie ich kwadraty. Suma dwóch kwadratów jest zerem dokładnie wtedy, gdy obie różnice są zerowe. \(\square\)

**Przykład 1.** Punkty \((2,3)\) i \((2,8)\) są oddalone o 5 jednostek. Punkty \((1,1)\) i \((4,5)\) o \(\sqrt{3^2+4^2}=5\).

**Kontrprzykład 1.** Samo porównanie współrzędnych \(x\) nie mierzy odległości w płaszczyźnie: punkty \((2,1)\) i \((2,9)\) mają tę samą pierwszą współrzędną, lecz nie są identyczne.

## 2. Kierunek, równoległość i prostopadłość

**Definicja 4 (wektor przesunięcia).** Dla \(A,B\) wektor \(\overrightarrow{AB}=B-A=(x_B-x_A,y_B-y_A)\). Opisuje kierunek i wielkość przesunięcia. Nie należy utożsamiać go z samym położeniem końca odcinka.

**Definicja 5 (prostopadłość i równoległość kierunków).** Dwa niezerowe wektory \(u,v\) są prostopadłe, gdy \(u_1v_1+u_2v_2=0\), i równoległe, gdy \(u_1v_2-u_2v_1=0\). Definicja dotyczy kierunków; odcinki mogą leżeć daleko od siebie.

**Twierdzenie 2 (osie są prostopadłe).** Wektory poziomy \((a,0)\) i pionowy \((0,b)\), gdzie \(a,b\ne0\), są prostopadłe.

*Dowód.* Ich iloczyn skalarny wynosi \(a\cdot0+0\cdot b=0\). \(\square\)

**Twierdzenie 3 (kierunki boków prostokąta).** Jeśli kolejne wierzchołki to \((0,0),(a,0),(a,b),(0,b)\) dla \(a,b>0\), to przeciwległe boki mają równoległe kierunki, a sąsiednie — prostopadłe.

*Dowód.* Wektory kolejnych boków to \((a,0),(0,b),(-a,0),(0,-b)\). Wektory przeciwległe różnią się znakiem; iloczyn skalarny każdych dwóch sąsiednich wynosi zero. \(\square\)

**Kontrprzykład 2.** Dwa odcinki jednakowej długości nie muszą być równoległe: wektory \((1,0)\) i \((0,1)\) mają tę samą długość, lecz są prostopadłe.

## 3. Wielokąty i figury podstawowe

**Definicja 6 (wielokąt prosty).** Wielokąt prosty to obszar ograniczony zamkniętą łamaną o skończonej liczbie boków, bez samoprzecięć innych niż połączenie sąsiednich boków w wierzchołkach. Trójkąt ma trzy boki, czworokąt cztery.

**Definicja 7 (prostokąt i kwadrat).** Prostokąt jest czworokątem o czterech kątach prostych. Kwadrat jest prostokątem o czterech bokach równej długości. Ta konwencja oznacza, że **każdy kwadrat jest prostokątem**.

**Twierdzenie 4 (kwadrat jest prostokątem).** Każdy kwadrat spełnia definicję prostokąta.

*Dowód.* Jest to bezpośrednia konsekwencja definicji 7: kwadrat jest prostokątem z dodatkowym warunkiem równości boków. \(\square\)

**Kontrprzykład 3.** Prostokąt o bokach 2 cm i 5 cm nie jest kwadratem. Zatem twierdzenia 4 nie wolno odwracać.

**Definicja 8 (obwód).** Obwód wielokąta to suma długości jego boków, bez ponownego liczenia wspólnego wierzchołka. Dla prostokąta o bokach \(a,b\) zapisujemy \(P=2a+2b\).

**Twierdzenie 5 (obwód kwadratu).** Kwadrat o boku \(a\) ma obwód \(4a\).

*Dowód.* Ma cztery boki o długości \(a\), więc ich suma wynosi \(a+a+a+a=4a\). \(\square\)

**Twierdzenie 6 (pole prostokąta na siatce jednostkowej).** Prostokąt o całkowitych długościach boków \(m,n\ge1\), którego boki leżą na liniach siatki jednostkowej, zawiera \(mn\) kwadratów jednostkowych.

*Dowód.* Dzielimy go na \(m\) kolumn i \(n\) wierszy kwadratów jednostkowych. Każda para numerów kolumny i wiersza wyznacza dokładnie jeden kwadrat, stąd liczba wynosi \(m\cdot n\). Rozszerzenie wzoru na dowolne długości rzeczywiste wymaga osobnego uzasadnienia przez własności pola. \(\square\)

**Kontrprzykład 4.** Figury o jednakowym obwodzie nie muszą mieć jednakowego pola. Prostokąty \(1\times5\) i \(2\times4\) mają obwód 12, ale pola odpowiednio 5 i 8.

**Definicja 9 (koło i okrąg).** Dla środka \(O\) i promienia \(r>0\) *okrąg* to zbiór punktów w odległości dokładnie \(r\) od \(O\), a *koło* to zbiór punktów w odległości co najwyżej \(r\). W codziennym języku te pojęcia bywają mylone.

**Kontrprzykład 5.** Środek koła należy do koła, lecz nie należy do okręgu o dodatnim promieniu.

## 4. Symetrie i przekształcenia

**Definicja 10 (przesunięcie).** Dla \(v=(p,q)\) definiujemy \(T_v(x,y)=(x+p,y+q)\).

**Twierdzenie 7 (przesunięcie zachowuje odległość).** \(d(T_v(A),T_v(B))=d(A,B)\).

*Dowód.* Po przesunięciu różnica pierwszych współrzędnych punktów pozostaje \((x_B+p)-(x_A+p)=x_B-x_A\), analogicznie druga. Wzór na odległość nie zmienia się. \(\square\)

**Definicja 11 (odbicie względem osi pionowej).** \(S(x,y)=(-x,y)\). Oś odbicia stanowi prosta \(x=0\). Figurę \(F\) nazywamy osiowo symetryczną względem tej osi, gdy \(S(F)=F\).

**Twierdzenie 8 (odbicie zachowuje odległość).** \(d(S(A),S(B))=d(A,B)\).

*Dowód.* Pierwsza różnica współrzędnych zmienia znak, druga pozostaje taka sama. Suma kwadratów różnic pozostaje niezmieniona. \(\square\)

**Twierdzenie 9 (dwukrotne odbicie).** \(S(S(P))=P\) dla każdego \(P\).

*Dowód.* \(S(-x,y)=(x,y)\). \(\square\)

**Definicja 12 (obrót o ćwierć pełnego obrotu).** \(R(x,y)=(-y,x)\). Jest to obrót o \(90^\circ\) przeciwnie do ruchu wskazówek zegara wokół początku układu.

**Twierdzenie 10 (obrót zachowuje odległość).** \(d(R(A),R(B))=d(A,B)\).

*Dowód.* Różnice współrzędnych \((\Delta x,\Delta y)\) przechodzą na \((-\Delta y,\Delta x)\). Suma ich kwadratów nie zmienia się. \(\square\)

**Twierdzenie 11 (cztery ćwierćobroty).** \(R^4(P)=P\).

*Dowód.* Kolejne obrazy \((x,y)\) to \((-y,x)\), \((-x,-y)\), \((y,-x)\), \((x,y)\). \(\square\)

**Twierdzenie 12 (dwie osie symetrii prostokąta).** Prostokąt osiowy \(F=[-a,a]\times[-b,b]\), \(a,b>0\), jest symetryczny względem osi poziomej i pionowej.

*Dowód.* Zmiana znaku \(x\) zachowuje nierówność \(-a\le x\le a\), a zmiana znaku \(y\) zachowuje \(-b\le y\le b\). Każde odbicie odwzorowuje więc cały prostokąt na siebie. \(\square\)

**Twierdzenie 13 (cztery ćwierćobroty kwadratu).** Kwadrat \(Q=[-a,a]\times[-a,a]\), \(a>0\), pozostaje niezmieniony przy każdym z obrotów \(R^0,R^1,R^2,R^3\).

*Dowód.* Obrót zamienia współrzędne miejscami i ewentualnie zmienia ich znaki; warunki \(|x|\le a\), \(|y|\le a\) są na te operacje odporne. \(\square\)

**Kontrprzykład 6.** Prostokąt \(2\times5\) ma dwie osie symetrii, lecz obrót o \(90^\circ\) nie pozostawia go w tym samym położeniu. Liczba osi symetrii nie wystarcza do rozpoznania kwadratu.

**Kontrprzykład 7.** Przesunięcie figury o wektor \((3,0)\) zachowuje jej kształt i wymiary, ale nie musi zachowywać jej położenia. „Ta sama figura” jako kształt nie oznacza „ten sam zbiór punktów”.

## 5. Orientacja, siatka i bryły

**Definicja 13 (ruch na siatce).** Na siatce kwadratowej krok w prawo zwiększa pierwszą współrzędną o 1, w lewo zmniejsza ją o 1, w górę zwiększa drugą o 1, w dół zmniejsza ją o 1. Liczbę kroków oznaczamy \(k\).

**Twierdzenie 14 (dolna granica kroków).** Każda droga po poziomych i pionowych krawędziach siatki z \(A=(x_1,y_1)\) do \(B=(x_2,y_2)\), przy całkowitych współrzędnych, ma co najmniej \(|x_2-x_1|+|y_2-y_1|\) kroków. Istnieje droga osiągająca tę granicę.

*Dowód.* Jeden krok zmienia tylko jedną współrzędną o 1. Aby osiągnąć zmianę \(\Delta x\), potrzeba co najmniej \(|\Delta x|\) kroków poziomych, analogicznie \(|\Delta y|\) pionowych. Wykonanie kolejno wszystkich potrzebnych kroków poziomych i pionowych osiąga sumę. \(\square\)

**Kontrprzykład 8.** Odległość wzdłuż krawędzi siatki nie jest odległością euklidesową: z \((0,0)\) do \((3,4)\) potrzeba 7 kroków, ale długość prostego odcinka wynosi 5.

**Definicja 14 (prostopadłościan i sześcian).** Prostopadłościan to bryła o sześciu prostokątnych ścianach, połączonych parami wzdłuż krawędzi. Sześcian jest prostopadłościanem, którego wszystkie krawędzie mają tę samą długość.

**Twierdzenie 15 (elementy prostopadłościanu).** Prostopadłościan ma 6 ścian, 12 krawędzi i 8 wierzchołków.

*Dowód.* W modelu \([0,a]\times[0,b]\times[0,c]\), gdzie \(a,b,c>0\), każda współrzędna wierzchołka jest jednym z dwóch końców odpowiedniego przedziału: \(2^3=8\) wierzchołków. Ściany powstają przez ustalenie jednej z trzech współrzędnych na jednym z dwóch końców: \(3\cdot2=6\). Krawędzie powstają przez ustalenie dwóch współrzędnych na końcach i pozostawienie jednej zmiennej: \(3\cdot2^2=12\). \(\square\)

**Twierdzenie 16 (zależność Eulera dla prostopadłościanu).** Dla liczby wierzchołków \(V\), krawędzi \(E\) i ścian \(F\) prostopadłościanu zachodzi \(V-E+F=2\).

*Dowód.* Na mocy twierdzenia 15: \(8-12+6=2\). Nie jest to dowód wzoru Eulera dla wszystkich wielościanów. \(\square\)

**Definicja 15 (siatka bryły).** Siatka sześcianu to płaski układ sześciu kwadratów, połączonych całymi bokami w sposób pozwalający złożyć bez nakładania wnętrz sześć ścian sześcianu. Nie każdy spójny układ sześciu kwadratów spełnia ten warunek.

**Kontrprzykład 9.** Prostokątna siatka \(2\times3\) z sześciu kwadratów nie składa się do sześcianu: cztery wewnętrzne styki tworzą cykl i nie można uzyskać sześciu różnych ścian bez konfliktu zgięć.

**Uwaga metodologiczna.** Własności przekształceń udowodniono w modelu współrzędnych. Przy pracy z uczniami należy równolegle stosować składanie papieru, kratki, klocki, modele brył i rysunki, a formalny zapis traktować jako kontrolę intuicji. Uogólnienia dotyczące dowolnych wielokątów, wielościanów i wszystkich możliwych siatek wymagają dodatkowych założeń.

# Część B. Ćwiczenia i rozwiązania

## Zestaw I — figury, punkty, odcinki

**Zadanie 1.** Podaj długość odcinka od \((1,2)\) do \((1,9)\). *Rozwiązanie.* Różnica drugich współrzędnych to \(9-2=7\), zatem długość 7.

**Zadanie 2.** Wyznacz długość odcinka od \((0,0)\) do \((6,8)\). *Rozwiązanie.* \(\sqrt{36+64}=10\).

**Zadanie 3.** Czy odcinki od \((0,0)\) do \((3,0)\) i od \((0,0)\) do \((0,3)\) są równoległe? *Rozwiązanie.* Nie; ich wektory są prostopadłe.

**Zadanie 4.** Podaj wektor od \(A=(2,5)\) do \(B=(7,3)\). *Rozwiązanie.* \((7-2,3-5)=(5,-2)\).

**Zadanie 5.** Podaj wierzchołki prostokąta o bokach 4 i 3, z jednym wierzchołkiem w początku układu, bokami wzdłuż dodatnich osi. *Rozwiązanie.* \((0,0),(4,0),(4,3),(0,3)\).

**Zadanie 6.** Czy każdy kwadrat jest prostokątem? *Rozwiązanie.* Tak, na mocy definicji prostokąta i kwadratu.

**Zadanie 7.** Czy każdy prostokąt jest kwadratem? *Rozwiązanie.* Nie; \(2\times5\) jest kontrprzykładem.

**Zadanie 8.** Oblicz obwód kwadratu o boku 7 cm. *Rozwiązanie.* \(4\cdot7=28\) cm.

**Zadanie 9.** Oblicz obwód prostokąta \(4\times9\). *Rozwiązanie.* \(2\cdot4+2\cdot9=26\).

**Zadanie 10.** Prostokąty \(1\times5\) i \(2\times4\) mają jednakowy obwód. Czy mają jednakowe pole? *Rozwiązanie.* Nie, pola wynoszą 5 i 8.

## Zestaw II — pola, klasyfikacja, koło

**Zadanie 11.** Ile kwadratów jednostkowych jest w prostokącie \(6\times7\) na siatce? *Rozwiązanie.* \(6\cdot7=42\).

**Zadanie 12.** Ile kwadratów jednostkowych jest w kwadracie o boku 9 jednostek? *Rozwiązanie.* \(9^2=81\).

**Zadanie 13.** Podaj przykład dwóch figur o tym samym polu i różnym obwodzie. *Rozwiązanie.* Prostokąty \(1\times12\) i \(3\times4\) mają pole 12, obwody 26 i 14.

**Zadanie 14.** Czy środek koła należy do okręgu o promieniu 4? *Rozwiązanie.* Nie; jego odległość od środka wynosi 0, a nie 4.

**Zadanie 15.** Czy punkt oddalony o 3 od środka należy do koła o promieniu 5? *Rozwiązanie.* Tak, ponieważ \(3\le5\).

**Zadanie 16.** Ile boków ma sześciokąt? *Rozwiązanie.* Sześć, zgodnie z nazwą i definicją wielokąta.

**Zadanie 17.** Czy figura złożona z dwóch nachodzących na siebie prostokątów musi być prostokątem? *Rozwiązanie.* Nie; można ułożyć je w kształt litery L.

**Zadanie 18.** Czy dwa różne punkty mogą wyznaczać odcinek zerowej długości? *Rozwiązanie.* Nie; z twierdzenia 1 wynika, że odległość zerowa wymaga równości punktów.

**Zadanie 19.** Kwadrat ma obwód 36 cm. Ile ma bok? *Rozwiązanie.* \(36:4=9\) cm.

**Zadanie 20.** Prostokąt ma pole 24 kwadratów jednostkowych i 4 wiersze. Ile ma kolumn? *Rozwiązanie.* \(24:4=6\).

## Zestaw III — odbicia i obroty

**Zadanie 21.** Odbij \((3,5)\) względem osi \(x=0\). *Rozwiązanie.* \((-3,5)\).

**Zadanie 22.** Odbij \((-4,-2)\) względem osi \(x=0\). *Rozwiązanie.* \((4,-2)\).

**Zadanie 23.** Odbij dwukrotnie punkt \((7,-1)\) względem osi \(x=0\). *Rozwiązanie.* Najpierw \((-7,-1)\), następnie \((7,-1)\).

**Zadanie 24.** Przesuń punkt \((2,3)\) o \((-5,4)\). *Rozwiązanie.* \((-3,7)\).

**Zadanie 25.** Obróć \((2,5)\) o \(90^\circ\) przeciwnie do ruchu wskazówek zegara. *Rozwiązanie.* \((-5,2)\).

**Zadanie 26.** Obróć \((1,2)\) dwa razy o \(90^\circ\). *Rozwiązanie.* \((-1,-2)\).

**Zadanie 27.** Obróć \((3,4)\) cztery razy o \(90^\circ\). *Rozwiązanie.* \((3,4)\).

**Zadanie 28.** Czy przesunięcie zmienia długość odcinka? *Rozwiązanie.* Nie, na mocy twierdzenia 7.

**Zadanie 29.** Czy odbicie może zmienić pole kwadratu? *Rozwiązanie.* Nie; odbicie jest izometrią, a obraz kwadratu ma takie same długości boków.

**Zadanie 30.** Czy prostokąt \(2\times5\) ma symetrię obrotową o \(90^\circ\)? *Rozwiązanie.* Nie; zamieniłaby wymiary kierunkowe, nie zachowując tego samego zbioru punktów.

## Zestaw IV — orientacja i bryły

**Zadanie 31.** Ile kroków siatkowych potrzeba minimalnie z \((1,1)\) do \((5,4)\)? *Rozwiązanie.* \(4+3=7\).

**Zadanie 32.** Czy z \((0,0)\) do \((3,4)\) można dojść w 5 krokach po krawędziach siatki? *Rozwiązanie.* Nie; minimum wynosi 7.

**Zadanie 33.** Ile ścian ma sześcian? *Rozwiązanie.* Sześć.

**Zadanie 34.** Ile wierzchołków ma prostopadłościan? *Rozwiązanie.* Osiem.

**Zadanie 35.** Ile krawędzi ma prostopadłościan? *Rozwiązanie.* Dwanaście.

**Zadanie 36.** Sprawdź zależność \(V-E+F\) dla prostopadłościanu. *Rozwiązanie.* \(8-12+6=2\).

**Zadanie 37.** Czy każdy sześcian jest prostopadłościanem? *Rozwiązanie.* Tak, jest jego szczególnym przypadkiem.

**Zadanie 38.** Czy każdy prostopadłościan jest sześcianem? *Rozwiązanie.* Nie; bryła o wymiarach \(2\times3\times4\) nim nie jest.

**Zadanie 39.** Ile kwadratów musi zawierać siatka sześcianu? *Rozwiązanie.* Sześć, po jednym na każdą ścianę.

**Zadanie 40.** Czy każdy układ sześciu sklejonych bokami kwadratów jest siatką sześcianu? *Rozwiązanie.* Nie; prostokąt \(2\times3\) nie jest prawidłową siatką.

## Problemy przekrojowe

**Problem A (plan ekspozycji).** Sala ma w planie postać prostokąta \(8\times5\) jednostek. Wyznacz pole, obwód i położenie środka symetrii, gdy dolny lewy wierzchołek ma współrzędne \((0,0)\).

*Rozwiązanie.* Pole \(8\cdot5=40\), obwód \(2(8+5)=26\), środek \((4,2{,}5)\). Odbicie względem prostych \(x=4\) i \(y=2{,}5\) zachowuje prostokąt.

**Problem B (trasa po kratkach).** Fotograf zaczyna w \((2,1)\), przechodzi trzy pola w prawo, cztery w górę i jedno w lewo. Gdzie kończy i czy trasa jest najkrótsza?

*Rozwiązanie.* Punkt końcowy to \((2+3-1,1+4)=(4,5)\). Droga ma 8 kroków, natomiast minimum to \(|4-2|+|5-1|=6\); droga nie jest najkrótsza.

**Problem C (odróżnianie kształtu od położenia).** Punkty \(A=(1,1)\), \(B=(4,1)\) przesunięto o \((5,-2)\). Oblicz końce nowego odcinka i porównaj długości.

*Rozwiązanie.* \(A'=(6,-1)\), \(B'=(9,-1)\). Oba odcinki mają długość 3. Położenia są różne, ale kształt i rozmiar nie uległy zmianie.

**Problem D (model pudełka).** Prostopadłościan ma krawędzie długości 2, 3 i 4 jednostek. Ile ma ścian, krawędzi i wierzchołków? Ile wynosi suma pól ścian?

*Rozwiązanie.* Ma 6 ścian, 12 krawędzi i 8 wierzchołków. Pary ścian mają pola \(2\cdot3=6\), \(2\cdot4=8\) i \(3\cdot4=12\), zatem suma wynosi \(2(6+8+12)=52\) jednostki kwadratowe.

## Granice, powiązania i status

- F13.2 rozwija zaawansowaną kombinatorykę siatek i podprostokątów; E0-05 korzysta wyłącznie z podstawowego liczenia kwadratów jednostkowych.
- F17.3 rozwija geometrię dyskretną osi liczb całkowitych; E0-05 rozróżnia siatkową długość trasy od euklidesowej odległości w płaszczyźnie.
- E0-04 rozwija jednostki i pomiar; E0-05 bada przede wszystkim kształt, położenie, symetrię i klasyfikację.
- Związek \(V-E+F=2\) sprawdzono tylko dla prostopadłościanu; nie przypisuje się mu dowodu dla dowolnych brył.
- **Nie doliczać stron do 585/1222** przed składem dokładnego źródła i integracją z kanonicznym monolitem 0.20. Nie modyfikować historycznego wstępu ani wcześniejszych rozdziałów.
