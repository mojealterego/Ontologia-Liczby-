---
title: 'ONTOLOGIA LICZBY — TOM I'
subtitle: 'E1-05. Równania liniowe — równoważność, parametry, dziedzina i weryfikacja'
author: 'Andrzej Mikulski'
date: '2 listopada 2026'
lang: pl-PL
fontsize: 11pt
geometry: margin=19mm
---

**Miejsce w taksonomii:** E1-05, poziom I. **Status:** nowy materiał źródłowy, nie włączony do monolitu 0.20. Nie zastępuje wcześniejszego F12.3 „Zadanie odwrotne — równania, translacje i granice odwracalności”, które bada odwracalność w grupach. Tutaj przedmiotem jest pełna elementarna semantyka równań liniowych w liczbach rzeczywistych, ze szczególnym naciskiem na warunki przekształceń, parametry i kontrolę wyniku.

# A. Teoria i dowody

## 1. Co znaczy rozwiązać równanie?

**Definicja D1 (równanie na dziedzinie).** Dla zbioru \(D\subseteq\mathbb R\) oraz funkcji \(L,R:D\to\mathbb R\), równanie \(L(x)=R(x)\) jest predykatem o zmiennej \(x\in D\). Jego **zbiorem rozwiązań** jest \(S_D(L=R)=\{x\in D:L(x)=R(x)\}\). Podanie samej wartości bez wskazania dziedziny może być niewystarczające.

**Definicja D2 (równoważność równań).** Dwa równania na tej samej dziedzinie \(D\) są równoważne, jeśli ich zbiory rozwiązań są identyczne. Zapis \(E_1\Longleftrightarrow E_2\) dotyczy równoważności, nie jedynie wynikania w jedną stronę.

**Definicja D3 (równanie liniowe jednej niewiadomej).** Jest to równanie \(ax+b=0\), gdzie \(a,b\in\mathbb R\) są stałymi, a \(x\in D\subseteq\mathbb R\). Dopuszczamy \(a=0\); przypadek ten należy rozpatrzyć osobno.

**Twierdzenie T1 (dodawanie tej samej funkcji).** Jeśli \(L,R,H:D\to\mathbb R\), to równania \(L(x)=R(x)\) i \(L(x)+H(x)=R(x)+H(x)\) są równoważne na \(D\).

*Dowód.* Dla ustalonego \(x\in D\), dodanie \(H(x)\) zachowuje równość. W przeciwną stronę od obu stron odejmujemy tę samą liczbę \(H(x)\). \(\square\)

**Twierdzenie T2 (mnożenie przez czynnik nigdzie niezerowy).** Jeśli \(G:D\to\mathbb R\) i \(G(x)\ne0\) dla każdego \(x\in D\), to \(L=R\) jest równoważne \(GL=GR\) na \(D\).

*Dowód.* Jedno wynikanie wynika z mnożenia. W drugą stronę, dla każdego \(x\in D\), dzielimy przez \(G(x)\ne0\). \(\square\)

**Kontrprzykład K1.** Równanie \(x=1\) ma zbiór rozwiązań \(\{1\}\). Po pomnożeniu obu stron przez \(x\) otrzymujemy \(x^2=x\), które ma rozwiązania \(\{0,1\}\). Mnożenie przez czynnik mogący przyjąć zero nie zachowuje równoważności.

**Kontrprzykład K2.** Z \(x^2=x\) nie wolno dzielić przez \(x\) bez osobnego sprawdzenia \(x=0\); utracilibyśmy poprawne rozwiązanie.

**Twierdzenie T3 (klasyfikacja równania liniowego).** Na \(D=\mathbb R\) równanie \(ax+b=0\) ma: (i) dokładnie jedno rozwiązanie \(x=-b/a\), jeśli \(a\ne0\); (ii) wszystkie liczby rzeczywiste jako rozwiązania, jeśli \(a=b=0\); (iii) brak rozwiązań, jeśli \(a=0\), \(b\ne0\).

*Dowód.* Dla \(a\ne0\) odejmujemy \(b\) i dzielimy przez \(a\); oba kroki są odwracalne. Dla \(a=0\) równanie redukuje się do \(b=0\), niezależnie od \(x\). \(\square\)

**Definicja D4 (tożsamość i sprzeczność).** Równanie prawdziwe dla każdego \(x\in D\) nazywamy tożsamościowym na \(D\); równanie bez rozwiązań — sprzecznym na \(D\).

**Przykład P1.** \(3x-7=11\Longleftrightarrow3x=18\Longleftrightarrow x=6\). Kontrola: \(3\cdot6-7=11\).

**Przykład P2.** \(4(x-2)=4x-8\) jest tożsamością; \(4(x-2)=4x-7\) jest sprzeczne.

## 2. Nawiasy, ułamki i warunki

**Twierdzenie T4 (postać kanoniczna).** Równanie \(ax+b=cx+d\) na \(\mathbb R\) jest równoważne \((a-c)x=d-b\).

*Dowód.* Odejmujemy \(cx+b\) od obu stron, korzystając z T1. \(\square\)

**Twierdzenie T5 (mianowniki stałe).** Jeżeli \(m,n\in\mathbb R\setminus\{0\}\), to równanie \(\frac{ax+b}{m}=\frac{cx+d}{n}\) jest równoważne \(n(ax+b)=m(cx+d)\).

*Dowód.* Mnożymy obie strony przez \(mn\ne0\) i redukujemy czynniki. \(\square\)

**Przykład P3.** \(\frac{x-1}{3}+\frac{x+2}{2}=5\). Mnożąc przez \(6\), dostajemy \(2x-2+3x+6=30\), stąd \(5x=26\), \(x=26/5\). Kontrola: \((21/5)/3+(36/5)/2=7/5+18/5=5\).

**Definicja D5 (dziedzina naturalna wyrażenia).** Jest to zbiór liczb rzeczywistych, dla których wszystkie działania tworzące wyrażenie są określone. Dla ilorazu \(A(x)/B(x)\) wykluczamy miejsca zerowe \(B\).

**Twierdzenie T6 (równanie wymierne z warunkiem).** Dla \(B(x)\ne0\) równanie \(\frac{A(x)}{B(x)}=C(x)\) jest równoważne \(A(x)=B(x)C(x)\), ale **wyłącznie na dziedzinie** \(D=\{x:B(x)\ne0\}\).

*Dowód.* Na \(D\) mnożenie przez \(B(x)\) jest odwracalne (T2). Poza \(D\) pierwsze równanie nie jest określone. \(\square\)

**Kontrprzykład K3.** \(\frac{x^2-1}{x-1}=2\) wymaga \(x\ne1\). Po pomnożeniu przez \(x-1\) otrzymujemy \(x^2-1=2x-2\), czyli \((x-1)^2=0\), skąd \(x=1\), ale liczba ta jest wykluczona. Zbiór rozwiązań oryginału jest pusty.

**Kontrprzykład K4.** \(\frac{x-2}{x-2}=1\) nie jest tożsamością na \(\mathbb R\), lecz na \(\mathbb R\setminus\{2\}\).

**Twierdzenie T7 (przecięcie z dziedziną).** Jeśli przekształcenia równania są równoważne na \(D\), a równanie końcowe ma zbiór rozwiązań \(S\) na \(\mathbb R\), to zbiór rozwiązań początkowego równania wynosi \(S\cap D\).

*Dowód.* Każdy element \(D\) spełnia oba równania jednocześnie lub żadnego. Kandydaci spoza \(D\) nie mogą być rozwiązaniami równania początkowego. \(\square\)

## 3. Równania z parametrem

**Definicja D6 (rodzina równań).** Parametr \(t\in P\subseteq\mathbb R\) oznacza ustaloną, choć dowolną liczbę. Rozwiązujemy osobne równanie dla każdego \(t\), a wynikiem jest funkcja przypisująca parametrowi zbiór rozwiązań.

**Twierdzenie T8 (pełna klasyfikacja parametryczna).** Dla \(a(t)x+b(t)=0\), \(t\in P\), zbiór rozwiązań to \(\{-b(t)/a(t)\}\), jeśli \(a(t)\ne0\); \(\mathbb R\), jeśli \(a(t)=b(t)=0\); \(\varnothing\), jeśli \(a(t)=0\ne b(t)\).

*Dowód.* Stosujemy T3 dla każdego ustalonego parametru \(t\). \(\square\)

**Przykład P4.** \((t-2)x=t^2-4\). Dla \(t\ne2\): \(x=(t^2-4)/(t-2)=t+2\). Dla \(t=2\) równanie ma postać \(0=0\), więc rozwiązaniem jest każde \(x\in\mathbb R\).

**Kontrprzykład K5.** Bezwarunkowe skrócenie \((t-2)x=(t-2)(t+2)\) przez \(t-2\) błędnie usuwa przypadek \(t=2\), w którym rozwiązań jest nieskończenie wiele.

**Przykład P5.** \((t-3)x=t-3\). Dla \(t\ne3\) rozwiązanie \(x=1\); dla \(t=3\) wszystkie liczby rzeczywiste.

**Przykład P6.** \((t-3)x=t-2\). Dla \(t\ne3\) rozwiązanie \(x=(t-2)/(t-3)\); dla \(t=3\) sprzeczność \(0=1\).

**Twierdzenie T9 (stabilność rozwiązania).** Jeśli \(a\ne0\), rozwiązanie \(x=-b/a\) zmienia się przy perturbacji \(b\mapsto b+\delta\) o dokładnie \(-\delta/a\).

*Dowód.* Nowe rozwiązanie wynosi \(x'=-(b+\delta)/a\); odejmując \(x\), otrzymujemy \(x'-x=-\delta/a\). \(\square\)

**Wniosek.** Dla małego \(|a|\) ten sam błąd w wyrazie wolnym może powodować dużą zmianę rozwiązania. Nie jest to błąd rachunku, lecz własność zadania.

**Kontrprzykład K6.** Zbliżenie współczynnika do zera nie gwarantuje ograniczoności rozwiązań: \(t x=1\) ma \(x=1/t\) dla \(t\ne0\), a wartości te rosną bez ograniczenia przy \(t\to0\).

## 4. Równania w modelach

**Definicja D7 (bilans liniowy).** Model \(px+q=r\) wyraża, że \(x\) jednostek o cenie \(p\) i stały koszt \(q\) dają łączną wartość \(r\). Warunki praktyczne, np. \(x\in\mathbb N_0\), stanowią część dziedziny.

**Twierdzenie T10 (rozwiązanie w ograniczonej dziedzinie).** Dla \(a\ne0\) równanie \(ax+b=0\) na \(D\subseteq\mathbb R\) ma rozwiązanie wtedy i tylko wtedy, gdy \(-b/a\in D\); wówczas jest ono jedyne.

*Dowód.* Na \(\mathbb R\) jedynym kandydatem jest \(-b/a\) (T3). Ograniczenie dziedziny może go zachować albo wykluczyć. \(\square\)

**Przykład P7.** Bilet kosztuje 12 zł, opłata stała 5 zł, budżet 53 zł: \(12x+5=53\), więc \(x=4\) bilety. Rozwiązanie jest liczbą naturalną.

**Kontrprzykład K7.** \(12x+5=50\) daje \(x=45/12=3{,}75\). Równanie ma rozwiązanie w \(\mathbb R\), ale nie w dziedzinie całkowitej liczby biletów.

**Twierdzenie T11 (liniowa zależność dwóch wielkości).** Jeśli \(y=mx+b\), to dla dowolnych \(x_1,x_2\), \(y(x_2)-y(x_1)=m(x_2-x_1)\).

*Dowód.* Odejmujemy \(mx_1+b\) od \(mx_2+b\). \(\square\)

**Przykład P8.** Przy \(y=3x+7\) zwiększenie \(x\) o 4 zwiększa \(y\) o 12 niezależnie od wartości początkowej.

## 5. Sprawdzenie i granice metody

**Definicja D8 (certyfikat rozwiązania).** Dla równania \(L=R\) na \(D\) certyfikat liczby \(x_0\) obejmuje: \(x_0\in D\) oraz obliczenie obu stron dające \(L(x_0)=R(x_0)\). Sam certyfikat potwierdza poprawność kandydata, lecz nie dowodzi jego jedyności.

**Twierdzenie T12 (kontrola przez resztę).** Dla \(a\ne0\), \(r(x)=ax+b\) i dokładnego rozwiązania \(x_*=-b/a\), zachodzi \(|x-x_*|=|r(x)|/|a|\).

*Dowód.* \(r(x)=a(x-x_*)\). Po wzięciu wartości bezwzględnych i podzieleniu przez \(|a|\) otrzymujemy wzór. \(\square\)

**Przykład P9.** Dla \(0{,}01x-1=0\), kandydat \(x=99\) daje resztę \(-0{,}01\), ale błąd rozwiązania wynosi \(1\), ponieważ \(|r|/|a|=0{,}01/0{,}01=1\).

**Definicja D9 (warunek równoważności kroku).** Krok przekształcenia równania nazywamy bezpiecznym, gdy jest odwracalny na całej aktualnej dziedzinie. Jeśli wymaga dodatkowego założenia, zapisujemy je przed wykonaniem kroku.

**Twierdzenie T13 (łańcuch bezpiecznych kroków).** Jeśli \(E_0\Longleftrightarrow E_1\Longleftrightarrow\cdots\Longleftrightarrow E_n\) na tej samej dziedzinie \(D\), to \(E_0\Longleftrightarrow E_n\) na \(D\).

*Dowód.* Równość zbiorów rozwiązań jest relacją przechodnią. \(\square\)

**Kontrprzykład K8.** Z \(x=2\) po podniesieniu obu stron do kwadratu otrzymujemy \(x^2=4\), które dopuszcza też \(x=-2\). Podnoszenie do parzystej potęgi nie jest odwracalne na całej \(\mathbb R\).

**Definicja D10 (równanie liniowe z wartością bezwzględną po rozbiciu).** Równanie \(|ax+b|=c\) jest równoważne alternatywie dwóch równań liniowych \(ax+b=c\) lub \(ax+b=-c\), pod warunkiem \(c\ge0\). Dla \(c<0\) zbiór rozwiązań jest pusty.

**Twierdzenie T14.** Jeśli \(c>0\) i \(a\ne0\), równanie \(|ax+b|=c\) ma dokładnie dwa różne rozwiązania \((c-b)/a\) i \((-c-b)/a\).

*Dowód.* Z definicji wartości bezwzględnej otrzymujemy dwie gałęzie. Rozwiązania są różne, bo ich różnica wynosi \(2c/a\ne0\). \(\square\)

**Kontrprzykład K9.** \(|x|=-1\) nie ma rozwiązań, mimo że formalne zapisanie \(x=\pm(-1)\) mogłoby sugerować dwa.

**Twierdzenie T15 (równanie \(ax=b\) w liczbach całkowitych).** Dla \(a,b\in\mathbb Z\), \(a\ne0\), równanie \(ax=b\) ma rozwiązanie \(x\in\mathbb Z\) wtedy i tylko wtedy, gdy \(a\mid b\).

*Dowód.* Jeśli \(x\in\mathbb Z\), to \(b=ax\), czyli \(a\mid b\). Jeśli \(a\mid b\), istnieje całkowite \(k\) z \(b=ak\); wtedy \(x=k\). \(\square\)

**Kontrprzykład K10.** \(2x=1\) ma rozwiązanie \(x=1/2\) w \(\mathbb Q\), lecz nie w \(\mathbb Z\).

**Twierdzenie T16 (równość liniowa dwóch funkcji).** Dla \(f(x)=ax+b\), \(g(x)=cx+d\), punkty przecięcia ich wykresów odpowiadają rozwiązaniom \((a-c)x=d-b\). Jeśli \(a=c\) i \(b\ne d\), wykresy nie mają punktów wspólnych; jeśli \(a=c,b=d\), pokrywają się.

*Dowód.* Punkt wspólny ma tę samą współrzędną \(x\) i tę samą wartość \(y\), więc \(f(x)=g(x)\). Następnie stosujemy T4 i T3. \(\square\)

**Twierdzenie T17 (dwa punkty określają funkcję liniowo-afiniczną).** Dla \(x_1\ne x_2\) oraz dowolnych \(y_1,y_2\) istnieje dokładnie jedna funkcja \(f(x)=ax+b\), dla której \(f(x_i)=y_i\). Jej współczynniki to \(a=(y_2-y_1)/(x_2-x_1)\) i \(b=y_1-ax_1\).

*Dowód.* Odejmując równania \(ax_1+b=y_1\) i \(ax_2+b=y_2\), otrzymujemy \(a(x_2-x_1)=y_2-y_1\). Ponieważ mianownik jest niezerowy, \(a\) jest wyznaczone jednoznacznie, a potem także \(b\). Podstawienie sprawdza istnienie. \(\square\)

**Kontrprzykład K11.** Dwa punkty o tej samej współrzędnej \(x\), lecz różnych \(y\), nie leżą na wykresie jednej funkcji; warunek \(x_1\ne x_2\) jest istotny.

**Twierdzenie T18 (przecięcie dwóch prostych nierównoległych).** Dla \(f(x)=ax+b\), \(g(x)=cx+d\), jeśli \(a\ne c\), wykresy mają dokładnie jeden punkt wspólny o współrzędnej \(x=(d-b)/(a-c)\).

*Dowód.* Równanie przecięcia ma niezerowy współczynnik przy \(x\), więc na mocy T3 ma dokładnie jedno rozwiązanie. \(\square\)

**Kontrprzykład K12.** Z \(x+2=3\) nie wynika \(x=3+2\); przeniesienie składnika na drugą stronę wymaga zmiany znaku, ponieważ w istocie odejmujemy 2 od obu stron.

# B. Rozwiązane zadania

## Zestaw 1. Przekształcenia podstawowe

**Z1.** \(x+7=19\). *Rozwiązanie:* \(x=12\). Kontrola: \(12+7=19\).

**Z2.** \(5x=45\). *Rozwiązanie:* \(x=9\).

**Z3.** \(3x-8=16\). *Rozwiązanie:* \(3x=24\), \(x=8\).

**Z4.** \(7-2x=1\). *Rozwiązanie:* \(-2x=-6\), \(x=3\).

**Z5.** \(4x+5=2x+17\). *Rozwiązanie:* \(2x=12\), \(x=6\).

**Z6.** \(9x-3=6x+12\). *Rozwiązanie:* \(3x=15\), \(x=5\).

**Z7.** \(2(x+3)=18\). *Rozwiązanie:* \(x+3=9\), \(x=6\).

**Z8.** \(3(2x-1)=15\). *Rozwiązanie:* \(6x-3=15\), \(x=3\).

**Z9.** \(4(x-2)+3=2x+1\). *Rozwiązanie:* \(4x-5=2x+1\), \(x=3\).

**Z10.** \(5-(x-4)=12\). *Rozwiązanie:* \(9-x=12\), \(x=-3\).

## Zestaw 2. Ułamki i znaki

**Z11.** \(x/3=7\). *Rozwiązanie:* \(x=21\).

**Z12.** \(x/4+2=5\). *Rozwiązanie:* \(x/4=3\), \(x=12\).

**Z13.** \((x-2)/5=3\). *Rozwiązanie:* \(x-2=15\), \(x=17\).

**Z14.** \((2x+1)/3=5\). *Rozwiązanie:* \(2x+1=15\), \(x=7\).

**Z15.** \(x/2+x/3=10\). *Rozwiązanie:* \(3x+2x=60\), \(x=12\).

**Z16.** \((x+1)/2-(x-1)/3=2\). *Rozwiązanie:* \(3x+3-2x+2=12\), \(x=7\).

**Z17.** \((3x-2)/4=(x+2)/2\). *Rozwiązanie:* \(3x-2=2x+4\), \(x=6\).

**Z18.** \(-3x=12\). *Rozwiązanie:* \(x=-4\).

**Z19.** \(-2(x-5)=6\). *Rozwiązanie:* \(x-5=-3\), \(x=2\).

**Z20.** \(0{,}2x+1=2\). *Rozwiązanie:* \(0{,}2x=1\), \(x=5\).

## Zestaw 3. Przypadki szczególne

**Z21.** \(2x+1=2x+1\). *Rozwiązanie:* każde \(x\in\mathbb R\).

**Z22.** \(2x+1=2x+2\). *Rozwiązanie:* brak rozwiązań, bo \(1\ne2\).

**Z23.** \(0x=0\). *Rozwiązanie:* wszystkie \(x\in\mathbb R\).

**Z24.** \(0x=5\). *Rozwiązanie:* \(\varnothing\).

**Z25.** \((t-1)x=t-1\). *Rozwiązanie:* \(x=1\) dla \(t\ne1\); wszystkie \(x\) dla \(t=1\).

**Z26.** \((t-1)x=2\). *Rozwiązanie:* \(x=2/(t-1)\) dla \(t\ne1\); brak rozwiązań dla \(t=1\).

**Z27.** \(tx=t^2\). *Rozwiązanie:* \(x=t\) dla \(t\ne0\); wszystkie \(x\) dla \(t=0\).

**Z28.** \((t+2)x=0\). *Rozwiązanie:* \(x=0\) dla \(t\ne-2\); wszystkie \(x\) dla \(t=-2\).

**Z29.** \(2x=3\) w dziedzinie \(\mathbb Z\). *Rozwiązanie:* brak rozwiązań całkowitych.

**Z30.** \(2x=4\) w dziedzinie \(\mathbb N_0\). *Rozwiązanie:* \(x=2\).

## Zestaw 4. Dziedzina i równoważność

**Z31.** \((x-1)/(x-1)=1\). *Rozwiązanie:* dziedzina \(x\ne1\); każde \(x\ne1\) jest rozwiązaniem.

**Z32.** \((x-2)/(x-2)=0\). *Rozwiązanie:* dziedzina \(x\ne2\); lewa strona równa 1, więc brak rozwiązań.

**Z33.** \(x/(x-1)=2\). *Rozwiązanie:* \(x\ne1\), \(x=2x-2\), stąd \(x=2\), dopuszczalne.

**Z34.** \((x+1)/(x-2)=1\). *Rozwiązanie:* \(x\ne2\); równanie \(x+1=x-2\) jest sprzeczne.

**Z35.** \((x^2-4)/(x-2)=4\). *Rozwiązanie:* \(x\ne2\); po skróceniu dla \(x\ne2\) dostajemy \(x+2=4\), więc jedyny kandydat \(x=2\) jest wykluczony. Brak rozwiązań.

**Z36.** \(|x-3|=2\). *Rozwiązanie:* \(x-3=2\) lub \(x-3=-2\), czyli \(x\in\{1,5\}\).

**Z37.** \(|2x+1|=3\). *Rozwiązanie:* \(2x+1=\pm3\), więc \(x=1\) lub \(x=-2\).

**Z38.** \(|x|=0\). *Rozwiązanie:* \(x=0\).

**Z39.** \(|x+2|=-1\). *Rozwiązanie:* brak rozwiązań.

**Z40.** Czy podniesienie \(x=3\) do kwadratu zachowuje równoważność? *Rozwiązanie:* nie, ponieważ \(x^2=9\) dopuszcza także \(x=-3\).

## Zestaw 5. Modelowanie i weryfikacja

**Z41.** Cztery identyczne zeszyty i opłata 6 zł kosztują 34 zł. *Rozwiązanie:* \(4x+6=34\), więc \(x=7\) zł.

**Z42.** Temperatura w stopniach Fahrenheita to \(F=9C/5+32\). Znajdź \(C\), gdy \(F=68\). *Rozwiązanie:* \(68-32=9C/5\), więc \(C=20\).

**Z43.** Prostokąt ma obwód 30 cm i jeden bok 6 cm. *Rozwiązanie:* \(2(x+6)=30\), więc \(x=9\) cm.

**Z44.** Takie samo równanie \(2(x+6)=30\) w dziedzinie długości dodatnich. *Rozwiązanie:* \(x=9>0\), wynik dopuszczalny.

**Z45.** Suma trzech kolejnych liczb całkowitych wynosi 48. *Rozwiązanie:* \(x+(x+1)+(x+2)=48\), \(3x=45\), liczby 15, 16, 17.

**Z46.** Zwiększenie argumentu funkcji \(y=5x-2\) o 3 zmienia wartość o ile? *Rozwiązanie:* o \(5\cdot3=15\).

**Z47.** Znajdź punkt przecięcia \(y=2x+1\) i \(y=-x+7\). *Rozwiązanie:* \(2x+1=-x+7\), \(x=2\), \(y=5\).

**Z48.** Czy proste \(y=2x+1\) i \(y=2x+3\) się przecinają? *Rozwiązanie:* nie, ponieważ \(2x+1=2x+3\) jest sprzeczne.

**Z49.** Wyznacz \(f(x)=ax+b\) przez punkty \((0,2)\) i \((3,11)\). *Rozwiązanie:* \(b=2\), \(3a+2=11\), więc \(a=3\), \(f(x)=3x+2\).

**Z50.** Dla \(0{,}01x-1=0\) sprawdź \(x=100\). *Rozwiązanie:* reszta \(0{,}01\cdot100-1=0\), więc kandydat jest dokładnym rozwiązaniem.

**Z51.** Dla \(0{,}01x-1=0\) sprawdź \(x=99\). *Rozwiązanie:* reszta \(-0{,}01\); błąd względem dokładnego rozwiązania 100 wynosi 1.

**Z52.** Czy \(6x=15\) ma rozwiązanie całkowite? *Rozwiązanie:* nie, ponieważ \(6\nmid15\).

**Z53.** Czy \(6x=18\) ma rozwiązanie całkowite? *Rozwiązanie:* tak, \(x=3\).

**Z54.** Cena jednostkowa wynosi 8 zł, koszt stały 10 zł, a łączny koszt 66 zł. *Rozwiązanie:* \(8x+10=66\), \(x=7\) sztuk.

**Z55.** Wiek pewnej osoby za 5 lat będzie równy dwukrotności wieku sprzed 7 lat. *Rozwiązanie:* \(x+5=2(x-7)\), stąd \(x=19\).

**Z56.** Znajdź \(x\), jeśli \(5(x-1)=2(2x+3)\). *Rozwiązanie:* \(5x-5=4x+6\), \(x=11\).

**Z57.** Rozwiąż \(4-3(2x-1)=1\). *Rozwiązanie:* \(7-6x=1\), \(x=1\).

**Z58.** Rozwiąż \((x-3)/4+(x+1)/2=5\). *Rozwiązanie:* \(x-3+2x+2=20\), \(3x=21\), \(x=7\).

**Z59.** Rozwiąż \((2x-1)/5-(x+2)/10=1\). *Rozwiązanie:* \(2(2x-1)-(x+2)=10\), \(3x-4=10\), \(x=14/3\).

**Z60.** Dla \(t=0\) rozwiąż \((t^2-1)x=t+1\). *Rozwiązanie:* \(-x=1\), więc \(x=-1\). W ogólności dla \(t\ne\pm1\), \(x=1/(t-1)\); dla \(t=-1\) wszystkie \(x\), a dla \(t=1\) brak rozwiązań.

## Problemy syntetyczne

**Problem S1 (bezpieczna redukcja).** Rozwiąż \((x^2-9)/(x-3)=6\) w \(\mathbb R\).

*Rozwiązanie.* Dziedzina \(x\ne3\). Na tej dziedzinie \((x^2-9)/(x-3)=x+3\). Równanie \(x+3=6\) daje \(x=3\), lecz jest to liczba wykluczona. Zatem \(S=\varnothing\).

**Problem S2 (pełna klasyfikacja).** Rozwiąż \((t^2-4)x=t+2\) w zależności od \(t\).

*Rozwiązanie.* Dla \(t\ne-2,2\), \(x=(t+2)/[(t-2)(t+2)]=1/(t-2)\). Dla \(t=-2\) obie strony są zerowe, więc \(S=\mathbb R\). Dla \(t=2\) mamy \(0x=4\), więc \(S=\varnothing\). Każdy przypadek wynika z T8; nie wolno skracać przed rozpatrzeniem zerowych czynników.

**Problem S3 (certyfikat numeryczny).** Dla równania \(0{,}002x-3=0\) kandydat wynosi \(1499\). Oszacuj dokładnie błąd.

*Rozwiązanie.* Reszta \(r=0{,}002\cdot1499-3=-0{,}002\). Na mocy T12 błąd wynosi \(|r|/0{,}002=1\); rozwiązaniem dokładnym jest \(1500\).

**Problem S4 (model całkowitoliczbowy).** Sklep sprzedaje jednakowe paczki po 14 zł, pobierając 5 zł za przesyłkę. Czy rachunek 100 zł jest możliwy?

*Rozwiązanie.* \(14x+5=100\), czyli \(14x=95\). Liczba \(95\) nie jest podzielna przez 14; brak rozwiązania w \(x\in\mathbb N_0\). Rozwiązanie rzeczywiste \(95/14\) nie ma sensu jako liczba całych paczek.

# Uwagi do weryfikacji i składu

1. Równoważność przekształceń należy zawsze odnosić do aktualnej dziedziny. W szczególności mnożenie przez wyrażenie z zerami i potęgowanie parzyste nie są automatycznie równoważne.
2. Testy obliczeniowe mogą sprawdzać przypadki i własności, lecz nie zastępują matematycznych dowodów twierdzeń T1–T18.
3. Wydawniczy limit końcowego PDF każdego tomu wynosi **ściśle poniżej 99 000 000 bajtów**. Objętość tomu nie ma już sztywnego celu 1222 stron. Historyczne 585 stron nie zmienia się bez integracji z monolitem 0.20.
4. Nie zmieniono wstępu historycznego, rozdziałów F ani wcześniejszych rozdziałów E. Nie tworzono końcowego spisu treści.
