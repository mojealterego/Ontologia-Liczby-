---
title: "ONTOLOGIA LICZBY — TOM I"
subtitle: "E1-07. Stereometria — bryły, pola powierzchni i objętość"
author: "Andrzej Mikulski"
date: "2 listopada 2026"
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Taksonomia:** E1-07, poziom I, następuje po E1-06. Zakres: prostopadłościany, graniastosłupy, ostrosłupy, walce, stożki, kule, przekroje i skale. Wykorzystujemy twierdzenia o polach figur płaskich z E1-06 i wcześniejszą intuicję przestrzenną E0-05; ich tekst pozostaje nienaruszony. Wyniki dotyczą klasycznej przestrzeni euklidesowej \(\mathbb R^3\).

# A. Definicje, twierdzenia i dowody

## 1. Wymiary i bryły wielościenne

**Definicja 1 (odległość przestrzenna).** Dla \(A=(x_1,y_1,z_1)\) i \(B=(x_2,y_2,z_2)\) odległość wynosi \(d(A,B)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}\).

**Twierdzenie 1 (przekątna prostopadłościanu).** Prostopadłościan o krawędziach \(a,b,c>0\) ma przekątną przestrzenną długości \(d=\sqrt{a^2+b^2+c^2}\).

*Dowód.* Przekątna podstawy ma długość \(\sqrt{a^2+b^2}\) z twierdzenia Pitagorasa. Jest prostopadła do pionowej krawędzi długości \(c\). Drugie zastosowanie Pitagorasa daje \(d^2=(a^2+b^2)+c^2\). \(\square\)

**Definicja 2 (objętość).** Objętość \(V\) jest nieujemną miarą obszarów przestrzennych, addytywną dla brył o rozłącznych wnętrzach, niezmienniczą względem przystawania, z \(V([0,1]^3)=1\). Wzory dla brył o krzywych brzegach wymagają ciągłości miary.

**Definicja 3 (prostopadłościan).** Prostopadłościan jest bryłą ograniczoną sześcioma prostokątami, o trzech wzajemnie prostopadłych długościach krawędzi \(a,b,c>0\).

**Twierdzenie 2 (objętość prostopadłościanu).** \(V=abc\).

*Dowód.* Dla całkowitych długości bryłę można podzielić na \(abc\) sześcianów jednostkowych. Dla dodatnich wymiernych długości stosujemy wspólną drobniejszą siatkę, a dla rzeczywistych przybliżenia wymiernymi od dołu i od góry oraz ciągłość objętości. \(\square\)

**Twierdzenie 3 (pole powierzchni prostopadłościanu).** \(S=2(ab+ac+bc)\).

*Dowód.* Ściany występują w trzech parach przystających prostokątów o polach \(ab,ac,bc\). Sumujemy sześć pól. \(\square\)

**Kontrprzykład 1.** Bryły o jednakowej objętości nie muszą mieć jednakowego pola powierzchni: sześcian \(2\times2\times2\) ma \(V=8,S=24\), a prostopadłościan \(1\times2\times4\) ma \(V=8,S=28\).

**Definicja 4 (graniastosłup prosty).** Graniastosłup prosty ma dwie przystające, równoległe podstawy wielokątne oraz boczne ściany prostokątne, prostopadłe do podstaw. Wysokość \(h>0\) to odległość płaszczyzn podstaw.

**Twierdzenie 4 (objętość graniastosłupa prostego).** \(V=P_p h\), gdzie \(P_p\) jest polem podstawy.

*Dowód.* Rozcinamy podstawę na trójkąty. Każdy trójkątny graniastosłup można rozciąć na części i porównać z prostopadłościanami, a równoważnie stosujemy zasadę Cavalieriego: każdy przekrój równoległy do podstawy ma stałe pole \(P_p\) na wysokości od 0 do \(h\). Objętość jest więc \(P_p h\). \(\square\)

**Twierdzenie 5 (pole całkowite graniastosłupa prostego).** \(S=2P_p+O_p h\), gdzie \(O_p\) jest obwodem podstawy.

*Dowód.* Dwie podstawy dają \(2P_p\). Każdy bok podstawy długości \(s_i\) wyznacza ścianę boczną o polu \(s_i h\). Suma pól bocznych wynosi \(h\sum s_i=O_p h\). \(\square\)

**Definicja 5 (ostrosłup).** Ostrosłup jest otoczką wypukłą wielokąta podstawy i punktu poza płaszczyzną podstawy, zwanego wierzchołkiem. Wysokość jest prostopadłą odległością wierzchołka od płaszczyzny podstawy.

**Twierdzenie 6 (objętość ostrosłupa).** \(V=P_p h/3\).

*Dowód.* Dla ostrosłupa o podstawie trójkątnej można rozciąć odpowiedni graniastosłup trójkątny na trzy czworościany o równych objętościach (po porównaniu podstaw i wysokości); stąd współczynnik \(1/3\). Dowolny ostrosłup rozcinamy płaszczyznami przechodzącymi przez wierzchołek i przekątne podstawy na ostrosłupy trójkątne. Sumując \(P_i h/3\), otrzymujemy \(P_p h/3\). Alternatywnie przekrój na wysokości \(t\) od podstawy ma pole \(P_p(1-t/h)^2\); zasada Cavalieriego i całkowanie \(\int_0^h(1-t/h)^2dt=h/3\) prowadzą do tej samej wartości. \(\square\)

**Kontrprzykład 2.** Ostrosłup i graniastosłup o tej samej podstawie i wysokości nie mają równych objętości: pierwszy ma jedną trzecią objętości drugiego.

## 2. Bryły obrotowe

**Definicja 6 (walec prosty).** Walec prosty ma dwie podstawy będące kołami o promieniu \(r>0\), leżące w równoległych płaszczyznach, oraz wysokość \(h>0\).

**Twierdzenie 7 (walec).** Walec prosty ma objętość \(V=\pi r^2h\) i pole całkowite \(S=2\pi r^2+2\pi rh\).

*Dowód.* Przekroje poziome walca mają stałe pole \(\pi r^2\), więc z zasady Cavalieriego \(V=\pi r^2h\). Po rozwinięciu powierzchni bocznej otrzymujemy prostokąt o bokach \(2\pi r\) i \(h\), zatem pole boczne to \(2\pi rh\); dodajemy dwa koła. \(\square\)

**Definicja 7 (stożek prosty).** Stożek prosty ma podstawę kołową promienia \(r>0\) i wierzchołek leżący na prostej prostopadłej do podstawy przechodzącej przez jej środek. Wysokość to \(h>0\), tworząca \(l=\sqrt{r^2+h^2}\).

**Twierdzenie 8 (objętość stożka).** \(V=\pi r^2h/3\).

*Dowód.* Przekrój stożka równoległy do podstawy na wysokości \(t\) od podstawy jest kołem o promieniu \(r(1-t/h)\), a więc polu \(\pi r^2(1-t/h)^2\). Ostrosłup o podstawie tej samej powierzchni i wysokości ma przekroje o dokładnie takich samych polach. Z zasady Cavalieriego objętości są równe; z T6 otrzymujemy wynik. \(\square\)

**Twierdzenie 9 (pole boczne stożka).** \(S_b=\pi rl\); pole całkowite \(S=\pi r^2+\pi rl\).

*Dowód.* Rozwinięta powierzchnia boczna jest wycinkiem koła o promieniu \(l\), którego łuk ma długość \(2\pi r\). Pole wycinka wynosi połowę iloczynu promienia i długości łuku, czyli \(\frac12 l(2\pi r)=\pi rl\). Dodajemy pole podstawy. \(\square\)

**Kontrprzykład 3.** Dla stożka \(r=3,h=4\) tworząca ma długość \(5\), a nie \(4\). Pole boczne to \(15\pi\), nie \(12\pi\).

**Definicja 8 (kula).** Kula o środku \(O\) i promieniu \(r>0\) jest zbiorem punktów przestrzeni odległych od \(O\) nie więcej niż \(r\). Sfera jest jej brzegiem.

**Twierdzenie 10 (objętość kuli).** \(V=4\pi r^3/3\).

*Dowód.* Na wysokości \(z\in[-r,r]\) przekrój kuli ma pole \(\pi(r^2-z^2)\). Objętość, jako suma graniczna pól przekrojów, wynosi \(\int_{-r}^r\pi(r^2-z^2)\,dz=\pi[r^2z-z^3/3]_{-r}^r=4\pi r^3/3\). Jest to dowód korzystający z całkowania, wykraczający formalnie poza poziom I; szkolny wzór jest jego konsekwencją. \(\square\)

**Twierdzenie 11 (pole sfery).** Pole sfery promienia \(r\) wynosi \(4\pi r^2\).

*Dowód.* Rozważmy cienką powłokę kuli promienia \(r\) o grubości \(\varepsilon>0\). Jej objętość wynosi \(\frac{4\pi}{3}[(r+\varepsilon)^3-r^3]\). Po podzieleniu przez \(\varepsilon\) i przejściu do granicy otrzymujemy \(4\pi r^2\). Utożsamienie tej granicy z polem powierzchni wymaga standardowego twierdzenia o objętości warstwy równoległej dla gładkiej sfery. \(\square\)

**Kontrprzykład 4.** Kula i sfera nie są tym samym: środek kuli nie leży na sferze o dodatnim promieniu.

## 3. Przekroje, skale, jednostki

**Definicja 9 (przekrój płaski).** Przekrój bryły płaszczyzną jest jej częścią wspólną z tą płaszczyzną; może być pusty, punktowy, odcinkowy lub dwuwymiarowy.

**Twierdzenie 12 (przekrój sześcianu).** Płaszczyzna równoległa do ściany sześcianu, przecinająca jego wnętrze, daje przekrój będący kwadratem przystającym do tej ściany.

*Dowód.* Współrzędne sześcianu możemy zapisać jako \([0,a]^3\). Płaszczyzna \(z=t\), \(0<t<a\), przecina go w \([0,a]\times[0,a]\times\{t\}\), czyli kwadracie o boku \(a\). \(\square\)

**Kontrprzykład 5.** Nie każdy przekrój sześcianu jest kwadratem; płaszczyzna przecinająca trzy krawędzie wychodzące z jednego wierzchołka może dać trójkąt.

**Definicja 10 (podobieństwo przestrzenne).** Bryły są podobne w skali \(k>0\), gdy odpowiadające im długości są pomnożone przez \(k\).

**Twierdzenie 13 (skala pól i objętości).** Przy podobieństwie przestrzennym o skali \(k\), pola powierzchni mnożą się przez \(k^2\), a objętości przez \(k^3\).

*Dowód.* Każda lokalna jednostka pola zawiera dwa niezależne kierunki długości, więc jej pole zmienia się \(k^2\) razy; dla brył wielościennych wynika to z triangulacji ścian. Dla objętości każdy elementarny prostopadłościan o bokach \(a,b,c\) zmienia się na \(ka,kb,kc\), więc jego objętość mnoży się przez \(k^3\). Przybliżenia wielościanami i ciągłość miary przenoszą wynik na regularne bryły. \(\square\)

**Kontrprzykład 6.** Dwukrotne powiększenie wszystkich wymiarów nie podwaja objętości, lecz zwiększa ją ośmiokrotnie.

**Definicja 11 (jednostka sześcienna).** \(1\,\mathrm{dm}^3\) jest objętością sześcianu o krawędzi 1 dm. Litr definiujemy jako \(1\,\mathrm{dm}^3\).

**Twierdzenie 14 (zamiana jednostek objętości).** \(1\,\mathrm{m}^3=1000\,\mathrm{dm}^3=1000\,\mathrm{l}\).

*Dowód.* \(1\,\mathrm m=10\,\mathrm{dm}\), zatem \((1\,\mathrm m)^3=(10\,\mathrm{dm})^3=1000\,\mathrm{dm}^3\). Z definicji litra wynika druga równość. \(\square\)

**Kontrprzykład 7.** \(1\,\mathrm m^3\ne100\,\mathrm{dm}^3\): w trzech wymiarach współczynnik przeliczenia jest sześcianem 10.

## 4. Własności wielościanów i ograniczenia

**Definicja 12 (wielościan wypukły).** Wielościan wypukły jest ograniczonym przecięciem skończenie wielu półprzestrzeni, mającym niepuste wnętrze. Jego ściany są wielokątami wypukłymi.

**Definicja 13 (siatka wielościanu).** Siatka jest płaskim układem wielokątów, które można złożyć w ściany wielościanu bez nakładania ich wnętrz.

**Twierdzenie 15 (pole sześcianu).** Sześcian o krawędzi \(a>0\) ma pole powierzchni \(6a^2\) i objętość \(a^3\).

*Dowód.* Ma sześć kwadratowych ścian o polu \(a^2\). Wzór na objętość jest przypadkiem T2 dla \(a=b=c\). \(\square\)

**Twierdzenie 16 (średnia gęstość).** Dla jednorodnej bryły o masie \(m>0\) i objętości \(V>0\), gęstość \(\rho=m/V\), więc \(m=\rho V\). Jeżeli dwie bryły są z tego samego jednorodnego materiału, stosunek mas równa się stosunkowi objętości.

*Dowód.* Pierwsza równość jest definicją gęstości. Dla stałego \(\rho\), \(m_1/m_2=(\rho V_1)/(\rho V_2)=V_1/V_2\). \(\square\)

**Kontrprzykład 8.** Dwie bryły o jednakowych wymiarach nie muszą mieć tej samej masy, gdy wykonano je z materiałów o różnych gęstościach.

**Definicja 14 (walec wydrążony).** Walec wydrążony współosiowo ma promień zewnętrzny \(R\), wewnętrzny \(r\), \(0\le r<R\), i wysokość \(h>0\).

**Twierdzenie 17 (objętość walca wydrążonego).** \(V=\pi(R^2-r^2)h\).

*Dowód.* Odejmujemy objętość walca wewnętrznego od objętości zewnętrznego, korzystając z addytywności objętości. \(\square\)

**Definicja 15 (przekrój centralny kuli).** Przekrój kuli płaszczyzną przechodzącą przez jej środek jest kołem wielkim.

**Twierdzenie 18 (pole przekroju kuli).** Płaszczyzna oddalona od środka kuli promienia \(R\) o \(d\), \(0\le d\le R\), daje przekrój kołowy o polu \(\pi(R^2-d^2)\).

*Dowód.* Promień \(s\) przekroju spełnia \(s^2+d^2=R^2\) na mocy Pitagorasa w przekroju osiowym. Pole to \(\pi s^2=\pi(R^2-d^2)\). \(\square\)

**Kontrprzykład 9.** Płaszczyzna oddalona od środka kuli o \(d>R\) nie przecina kuli, więc wzór na dodatnie pole kołowego przekroju nie obowiązuje poza dziedziną \(d\le R\).

# B. Zadania z pełnymi rozwiązaniami

## Zestaw 1 — prostopadłościany i graniastosłupy

**Zadanie 1.** Objętość prostopadłościanu \(2\times3\times5\)? *Rozwiązanie:* \(30\).

**Zadanie 2.** Pole powierzchni prostopadłościanu \(2\times3\times5\)? *Rozwiązanie:* \(2(6+10+15)=62\).

**Zadanie 3.** Przekątna prostopadłościanu \(3\times4\times12\)? *Rozwiązanie:* \(\sqrt{9+16+144}=13\).

**Zadanie 4.** Objętość sześcianu o krawędzi 7? *Rozwiązanie:* \(7^3=343\).

**Zadanie 5.** Pole sześcianu o krawędzi 7? *Rozwiązanie:* \(6\cdot49=294\).

**Zadanie 6.** Krawędź sześcianu o objętości 125? *Rozwiązanie:* \(\sqrt[3]{125}=5\).

**Zadanie 7.** Graniastosłup ma pole podstawy 18 i wysokość 9. Objętość? *Rozwiązanie:* \(18\cdot9=162\).

**Zadanie 8.** Graniastosłup prosty ma obwód podstawy 20, pole podstawy 24 i wysokość 5. Pole całkowite? *Rozwiązanie:* \(2\cdot24+20\cdot5=148\).

**Zadanie 9.** Akwarium \(40\times25\times30\) cm ma jaką objętość w litrach? *Rozwiązanie:* \(30000\,\mathrm{cm}^3=30\) l.

**Zadanie 10.** Jak zmienia się objętość prostopadłościanu po podwojeniu jednej krawędzi? *Rozwiązanie:* Podwaja się.

## Zestaw 2 — ostrosłupy

**Zadanie 11.** Ostrosłup ma pole podstawy 30 i wysokość 9. Objętość? *Rozwiązanie:* \(30\cdot9/3=90\).

**Zadanie 12.** Ostrosłup ma podstawę kwadratową o boku 6 i wysokość 10. Objętość? *Rozwiązanie:* \(36\cdot10/3=120\).

**Zadanie 13.** Ostrosłup o objętości 60 i podstawie pola 20 ma jaką wysokość? *Rozwiązanie:* \(h=3V/P_p=9\).

**Zadanie 14.** Ostrosłup i graniastosłup mają tę samą podstawę i wysokość. Stosunek objętości? *Rozwiązanie:* \(1:3\).

**Zadanie 15.** Podwojono wysokość ostrosłupa bez zmiany podstawy. Objętość? *Rozwiązanie:* Podwaja się.

**Zadanie 16.** Podwojono długość boku kwadratowej podstawy przy stałej wysokości. Objętość? *Rozwiązanie:* Czterokrotna.

**Zadanie 17.** Podstawa ostrosłupa jest trójkątem o podstawie 8 i wysokości 5, a wysokość bryły to 12. Objętość? *Rozwiązanie:* \(P_p=20\), więc \(V=20\cdot12/3=80\).

**Zadanie 18.** Czy ostrosłup może mieć prostokątną podstawę? *Rozwiązanie:* Tak, definicja dopuszcza dowolny wielokąt podstawy.

## Zestaw 3 — walce i stożki

**Zadanie 19.** Objętość walca \(r=3,h=10\)? *Rozwiązanie:* \(90\pi\).

**Zadanie 20.** Pole całkowite walca \(r=3,h=10\)? *Rozwiązanie:* \(2\pi9+2\pi30=78\pi\).

**Zadanie 21.** Objętość stożka \(r=3,h=10\)? *Rozwiązanie:* \(30\pi\).

**Zadanie 22.** Tworząca stożka \(r=5,h=12\)? *Rozwiązanie:* \(l=13\).

**Zadanie 23.** Pole boczne stożka \(r=5,l=13\)? *Rozwiązanie:* \(65\pi\).

**Zadanie 24.** Pole całkowite stożka \(r=5,l=13\)? *Rozwiązanie:* \(25\pi+65\pi=90\pi\).

**Zadanie 25.** Walec o promieniu 4 i wysokości 7 ma jaką objętość? *Rozwiązanie:* \(112\pi\).

**Zadanie 26.** Stożek i walec mają te same \(r,h\). Jaki stosunek objętości? *Rozwiązanie:* \(1:3\).

**Zadanie 27.** Walec ma objętość \(48\pi\), promień 4. Wysokość? *Rozwiązanie:* \(h=48\pi/(16\pi)=3\).

**Zadanie 28.** Stożek ma objętość \(12\pi\), promień 3. Wysokość? *Rozwiązanie:* \(h=3\cdot12\pi/(9\pi)=4\).

## Zestaw 4 — kule i przekroje

**Zadanie 29.** Objętość kuli promienia 3? *Rozwiązanie:* \(4\pi27/3=36\pi\).

**Zadanie 30.** Pole sfery promienia 3? *Rozwiązanie:* \(4\pi9=36\pi\).

**Zadanie 31.** Objętość kuli promienia 6? *Rozwiązanie:* \(4\pi216/3=288\pi\).

**Zadanie 32.** Pole sfery promienia 6? *Rozwiązanie:* \(4\pi36=144\pi\).

**Zadanie 33.** Kula promienia 5 przecięta płaszczyzną odległą od środka o 3. Promień przekroju? *Rozwiązanie:* \(\sqrt{25-9}=4\).

**Zadanie 34.** Pole przekroju z Zadania 33? *Rozwiązanie:* \(16\pi\).

**Zadanie 35.** Kula promienia 5 przecięta płaszczyzną odległą o 5. Przekrój? *Rozwiązanie:* Jeden punkt, pole 0.

**Zadanie 36.** Płaszczyzna w odległości 7 od środka kuli promienia 5. Przekrój? *Rozwiązanie:* Pusty.

**Zadanie 37.** Jak zmieni się objętość kuli po podwojeniu promienia? *Rozwiązanie:* Ośmiokrotnie.

**Zadanie 38.** Jak zmieni się pole sfery po podwojeniu promienia? *Rozwiązanie:* Czterokrotnie.

## Zestaw 5 — jednostki, skala i modelowanie

**Zadanie 39.** Zamień \(2\,\mathrm{m}^3\) na litry. *Rozwiązanie:* \(2000\) l.

**Zadanie 40.** Zamień \(500\,\mathrm{cm}^3\) na litry. *Rozwiązanie:* \(0{,}5\) l.

**Zadanie 41.** Bryłę powiększono w skali 3. Jak zmienia się objętość? *Rozwiązanie:* \(3^3=27\) razy.

**Zadanie 42.** Bryłę powiększono w skali 3. Jak zmienia się pole powierzchni? *Rozwiązanie:* \(3^2=9\) razy.

**Zadanie 43.** Objętość sześcianu wzrosła 64 razy. Jaki współczynnik skali? *Rozwiązanie:* \(\sqrt[3]{64}=4\).

**Zadanie 44.** Prostopadłościan ma objętość 120 i podstawę o polu 24. Wysokość? *Rozwiązanie:* \(h=120/24=5\).

**Zadanie 45.** Walec wydrążony \(R=5,r=3,h=10\). Objętość materiału? *Rozwiązanie:* \(\pi(25-9)10=160\pi\).

**Zadanie 46.** Klocek o objętości \(200\,\mathrm{cm}^3\) i gęstości \(2{,}5\,\mathrm{g/cm}^3\). Masa? *Rozwiązanie:* \(500\) g.

**Zadanie 47.** Czy równe pola powierzchni oznaczają równe objętości? *Rozwiązanie:* Nie. Sześcian o krawędzi 1 ma \(S=6,V=1\), a prostopadłościan o wymiarach \(1/2,1/2,11/4\) ma \(S=2(1/4+11/8+11/8)=6\), ale \(V=11/16\).

**Zadanie 48.** Czy objętość sześcianu o krawędzi 0,1 m wynosi 0,1 m³? *Rozwiązanie:* Nie, \((0{,}1)^3=0{,}001\) m³.

**Zadanie 49.** Pole sfery ma wartość \(100\pi\). Promień? *Rozwiązanie:* \(4\pi r^2=100\pi\), więc \(r=5\).

**Zadanie 50.** Objętość walca to \(100\pi\), wysokość 4. Promień? *Rozwiązanie:* \(\pi r^2\cdot4=100\pi\), więc \(r=5\).

## Problemy syntetyczne

**Problem A (projekt pojemnika).** Zamknięty prostopadłościan ma podstawę kwadratową o boku 4 cm i objętość \(96\,\mathrm{cm}^3\). Oblicz wysokość i całkowite pole powierzchni.

*Rozwiązanie.* \(16h=96\), więc \(h=6\) cm. Pole: \(2(16+24+24)=128\,\mathrm{cm}^2\).

**Problem B (porównanie dwóch pojemników).** Walec i stożek mają promień 6 cm i wysokość 8 cm. O ile większa jest objętość walca?

*Rozwiązanie.* Walec: \(288\pi\); stożek: \(96\pi\); różnica \(192\pi\,\mathrm{cm}^3\).

**Problem C (kontrola jednostek).** Zbiornik ma \(1{,}2\,\mathrm m\times0{,}5\,\mathrm m\times0{,}4\,\mathrm m\). Ile litrów wody mieści się do pełna?

*Rozwiązanie.* \(V=0{,}24\,\mathrm m^3=240\) l.

**Problem D (przekrój i Pitagoras).** Kula promienia 13 cm ma przekrój o promieniu 12 cm. Jaka jest odległość płaszczyzny przekroju od środka?

*Rozwiązanie.* \(d=\sqrt{13^2-12^2}=\sqrt{25}=5\) cm.

**Problem E (różne materiały).** Dwa jednakowe sześciany mają objętość 64 cm³, lecz gęstości \(2\) i \(3\,\mathrm{g/cm}^3\). Wyznacz masy.

*Rozwiązanie.* \(m_1=128\) g, \(m_2=192\) g. Jednakowa geometria nie wymusza jednakowej masy.

**Problem F (skalowanie modelu).** Model bryły w skali \(1:5\) ma objętość 40 cm³. Jaką objętość ma oryginał?

*Rozwiązanie.* Skala objętości wynosi \(1:125\), więc oryginał ma \(40\cdot125=5000\) cm³.

# C. Ograniczenia odbioru

Twierdzenia o kuli, stożku i bryłach obrotowych wykorzystują ciągłość objętości, zasadę Cavalieriego lub rachunek całkowy; włączenie dowodu do tekstu szkolnego ma charakter pomostowy. Żaden wynik nie stanowi deklaracji formalizacji w systemie dowodowym. Opracowanie nie zmienia E0-05, E1-06 ani wcześniejszych źródeł. Liczba stron zostanie ustalona po pełnym składzie i kontroli. Historyczny stan zintegrowanego Tomu I: 585 stron; 1222 nie jest wymaganym progiem, a końcowy PDF tomu musi być mniejszy niż 99 000 000 bajtów.
