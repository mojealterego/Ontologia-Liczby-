---
title: 'ONTOLOGIA LICZBY — TOM I'
subtitle: 'E0-04. Pomiar — wielkości, jednostki, skala i niepewność'
author: 'Andrzej Mikulski'
date: '1 listopada 2026'
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Mapa taksonomiczna:** E0-04, poziom I: jednostki, skala, długość, masa, pole i czas; powiązania tematyczne z MSC 51 i 97 nie oznaczają kodów MSC dla szkolnego tematu. **Status:** nowy rozdział źródłowy, bez wliczania stron do monolitu 0.20.

# Część A. Teoria, definicje i dowody

## 1. Co oznacza zmierzyć wielkość?

**Definicja 1 (wielkość mierzalna).** Wielkością nazywamy cechę obiektu lub zjawiska, której wartości można porównywać według określonej procedury. W rozdziale rozpatrujemy długość, masę, pole, objętość i czas trwania. Różne wielkości nie mogą być dodawane bez nadania operacji dodatkowego znaczenia: trzy metry plus dwie sekundy nie stanowią długości.

**Definicja 2 (jednostka i liczba miarowa).** Przy ustalonej jednostce \(u>0\) tej samej wielkości zapis \(Q=qu\) oznacza, że liczba \(q\ge0\) jest wartością liczbową wielkości \(Q\) wyrażonej w jednostce \(u\). Jednostka nie jest samą liczbą; \(3\,\mathrm m\) i \(3\,\mathrm{cm}\) oznaczają różne długości.

**Definicja 3 (konwersja jednostek).** Jeżeli jednostki tej samej wielkości spełniają \(u=kv\), gdzie \(k>0\), to \(qu=(qk)v\). Jest to przeliczenie liczby miarowej przy niezmienionej wielkości fizycznej.

**Twierdzenie 1 (niezmienniczość pomiaru przy zmianie jednostki).** Jeżeli \(Q=qu\), \(u=kv\), to \(Q=(qk)v\). Jeżeli \(Q_1\le Q_2\) w jednej jednostce, to porządek pozostaje taki sam po przeliczeniu obu wartości do drugiej jednostki.

*Dowód.* Z podstawienia \(Q=qu=q(kv)=(qk)v\). Ponieważ \(k>0\), z \(q_1\le q_2\) wynika \(q_1k\le q_2k\). \(\square\)

**Przykład 1.** \(2{,}4\,\mathrm m=240\,\mathrm{cm}=2400\,\mathrm{mm}\). Zapis \(2{,}4\,\mathrm m=2{,}4\,\mathrm{cm}\) jest fałszywy.

**Kontrprzykład 1 (niedozwolone dodawanie).** \(5\,\mathrm m+3\,\mathrm{kg}\) nie jest ani długością, ani masą. Samo dodanie liczb 5 i 3 nie rozwiązuje problemu niezgodnych wymiarów.

**Definicja 4 (dokładność zapisu i niepewność).** Zapis \(Q\in[a,b]u\) oznacza, że rzeczywista wartość leży między granicami \(a u\) i \(b u\). Bez informacji o sposobie pomiaru nie należy utożsamiać liczby zapisanych cyfr z gwarantowaną dokładnością.

## 2. Długość i odległość

**Definicja 5 (długość odcinka na osi).** Dla punktów o współrzędnych \(x,y\in\mathbb R\) długość odcinka wynosi \(d(x,y)=|x-y|\). Długość jest nieujemna i nie zależy od kierunku odczytu.

**Twierdzenie 2 (symetria i zerowanie odległości).** \(d(x,y)=d(y,x)\), a \(d(x,y)=0\) wtedy i tylko wtedy, gdy \(x=y\).

*Dowód.* \(|x-y|=|-(y-x)|=|y-x|\). Wartość bezwzględna liczby wynosi zero dokładnie wtedy, gdy liczba wynosi zero. \(\square\)

**Twierdzenie 3 (nierówność trójkąta na osi).** Dla dowolnych \(x,y,z\in\mathbb R\) zachodzi \(d(x,z)\le d(x,y)+d(y,z)\).

*Dowód.* Jeśli \(y\) leży między \(x\) i \(z\), to obie strony są równe. Jeśli \(y\) leży poza odcinkiem o końcach \(x,z\), droga przez \(y\) zawiera odcinek \(xz\) oraz dodatkowy odcinek pokonywany dwukrotnie; stąd nierówność. Formalnie jest to \(|(x-y)+(y-z)|\le|x-y|+|y-z|\). \(\square\)

**Przykład 2.** Odległość między punktami \(-3\) i \(5\) wynosi \(|5-(-3)|=8\), nie 2.

**Kontrprzykład 2 (odległość a przemieszczenie).** Po przejściu 4 m w prawo i 4 m w lewo droga wynosi 8 m, lecz przemieszczenie od początku do końca wynosi 0 m. Nie wolno używać tych pojęć zamiennie.

**Twierdzenie 4 (addytywność długości na odcinku).** Jeżeli \(x\le y\le z\), to \(d(x,z)=d(x,y)+d(y,z)\).

*Dowód.* \(z-x=(y-x)+(z-y)\), a wszystkie trzy różnice są nieujemne. \(\square\)

**Przykład 3.** Taśma ma długość 1 m 35 cm, a drugi fragment 85 cm. Suma wynosi \(135+85=220\) cm, czyli 2 m 20 cm.

## 3. Masa i ważenie

**Definicja 6 (model addytywny masy).** Dla dwóch rozłącznych, nieoddziałujących w istotny sposób porcji materii o masach \(m_1,m_2\) przyjmujemy w szkolnym modelu \(m_{\mathrm{razem}}=m_1+m_2\). Wynik odnosi się do masy porcji, a nie do wskazania wagi obarczonego błędem przyrządu.

**Twierdzenie 5 (niezależność sumy mas od kolejności).** Dla trzech porcji masy \(m_1,m_2,m_3\) suma nie zależy od kolejności łączenia.

*Dowód.* \((m_1+m_2)+m_3=m_1+(m_2+m_3)\) na mocy łączności dodawania liczb rzeczywistych. \(\square\)

**Przykład 4.** \(2\,\mathrm{kg}\,350\,\mathrm g+750\,\mathrm g=2350\,\mathrm g+750\,\mathrm g=3100\,\mathrm g=3\,\mathrm{kg}\,100\,\mathrm g\).

**Kontrprzykład 3 (masa a ciężar).** Masa 2 kg nie jest siłą 2 N. Ciężar jest siłą i zależy od przyspieszenia grawitacyjnego; szkolne ważenie nie upoważnia do utożsamienia tych jednostek.

## 4. Pole: jednostki kwadratowe

**Definicja 7 (pole prostokąta).** Dla boków długości \(a,b\ge0\), wyrażonych w tej samej jednostce długości, pole prostokąta definiujemy jako \(P=ab\) jednostek kwadratowych. Jednostka \(\mathrm m^2\) jest polem kwadratu o boku 1 m.

**Twierdzenie 6 (pole prostokąta z kratki).** Prostokąt o całkowitych bokach \(a,b\) jednostek długości zawiera dokładnie \(ab\) kwadratów jednostkowych.

*Dowód.* Każdy z \(a\) rzędów zawiera \(b\) kwadratów, a rzędy są rozłączne. Łącznie \(a\cdot b\) kwadratów. \(\square\)

**Twierdzenie 7 (zmiana jednostki pola).** Jeżeli jednostka długości \(u=kv\), to \(1u^2=k^2v^2\). W szczególności \(1\,\mathrm m^2=10\,000\,\mathrm{cm}^2\).

*Dowód.* Kwadrat o boku \(u\) ma w jednostkach \(v\) bok \(k\); jego pole wynosi \(k\cdot k=k^2\) kwadratów jednostkowych. Dla metra i centymetra \(k=100\). \(\square\)

**Kontrprzykład 4 (błąd liniowego przeliczenia pola).** \(1\,\mathrm m^2\ne100\,\mathrm{cm}^2\). Mnożnik 100 dotyczy długości, a mnożnik 10 000 — pola.

**Twierdzenie 8 (addytywność pól bez nakładania).** Jeśli prostokąt rozcięto pionowo na części o szerokościach \(b,c\) i wspólnej wysokości \(a\), to \(a(b+c)=ab+ac\).

*Dowód.* Obie strony wyrażają pole tego samego prostokąta, a równość jest prawem rozdzielności mnożenia względem dodawania. \(\square\)

**Przykład 5.** Pokój o wymiarach 4 m na 3,5 m ma pole \(14\,\mathrm m^2\). Po zmianie jednostek: \(400\mathrm{cm}\cdot350\mathrm{cm}=140\,000\,\mathrm{cm}^2=14\,\mathrm m^2\).

## 5. Objętość i skala

**Definicja 8 (objętość prostopadłościanu).** Dla krawędzi \(a,b,c\) w tej samej jednostce długości objętość wynosi \(V=abc\) jednostek sześciennych. \(1\,\mathrm{dm}^3=1\,\mathrm l\) jest relacją definicyjną jednostek objętości.

**Twierdzenie 9 (przeliczenie jednostek objętości).** Jeśli \(u=kv\), to \(u^3=k^3v^3\). Zatem \(1\,\mathrm m^3=1000\,\mathrm{dm}^3=1000\,\mathrm l\).

*Dowód.* Sześcian jednostkowy ma po zmianie jednostki trzy krawędzie długości \(k\), więc jego objętość ma wartość liczbową \(k^3\). Dla \(1\mathrm m=10\mathrm{dm}\) otrzymujemy \(10^3=1000\). \(\square\)

**Definicja 9 (skala liniowa).** Skala \(1:n\) dla \(n>0\) oznacza, że 1 jednostka długości na rysunku odpowiada \(n\) takim samym jednostkom w rzeczywistości. Zakładamy brak zniekształceń i jednakową skalę w obu kierunkach.

**Twierdzenie 10 (skala pola).** W rysunku podobnym o skali liniowej \(1:n\) pole jest \(n^2\) razy mniejsze od pola rzeczywistego.

*Dowód.* Każdy bok prostokąta zostaje podzielony przez \(n\), więc pole dzieli się przez \(n\cdot n=n^2\). Dla figur złożonych z prostokątów wynika to z addytywności pól; ogólne figury wymagają odpowiedniego uzasadnienia przez przybliżenia. \(\square\)

**Przykład 6.** Na mapie w skali 1:50 000 odległość 3 cm odpowiada \(3\cdot50\,000=150\,000\) cm, czyli 1,5 km.

**Kontrprzykład 5 (skala powierzchni).** Skala 1:100 nie oznacza, że pole jest 100 razy mniejsze; dla figur podobnych pole jest 10 000 razy mniejsze.

## 6. Czas: chwila i czas trwania

**Definicja 10 (chwila i czas trwania).** Chwila jest punktem na osi czasu, a czas trwania między chwilami \(t_1\le t_2\) wynosi \(\Delta t=t_2-t_1\). Godzina na zegarze jest etykietą chwili, nie długością trwania.

**Twierdzenie 11 (addytywność czasu trwania).** Jeśli \(t_1\le t_2\le t_3\), to \(t_3-t_1=(t_2-t_1)+(t_3-t_2)\).

*Dowód.* Po rozwinięciu prawej strony składniki \(t_2\) skracają się. \(\square\)

**Przykład 7.** Zajęcia trwają od 09:45 do 11:10 tego samego dnia: 15 minut do 10:00, 60 minut do 11:00, 10 minut do 11:10, razem 85 minut.

**Kontrprzykład 6 (przejście przez północ).** Od 23:50 do 00:20 następnego dnia mija 30 minut, nie „minus 23 godziny 30 minut”. Trzeba uwzględnić datę.

**Uwaga o modelu czasu.** Rachunek godzinami lokalnymi podczas zmian czasu urzędowego wymaga strefy czasowej i daty. Zadania poniżej przyjmują dobę bez zmiany czasu urzędowego.

## 7. Zaokrąglenia i granice błędu

**Definicja 11 (zaokrąglenie do kroku).** Zaokrąglenie wartości \(x\) do najbliższej wielokrotności kroku \(h>0\) daje wynik \(\widehat x\). W przypadku remisu wybieramy większą wielokrotność. Dla \(x\ge0\) błąd nie przekracza \(h/2\).

**Twierdzenie 12 (błąd sumy).** Jeżeli \(|x-\widehat x|\le\varepsilon\) oraz \(|y-\widehat y|\le\delta\), to \(|(x+y)-(\widehat x+\widehat y)|\le\varepsilon+\delta\).

*Dowód.* Lewa strona to \(|(x-\widehat x)+(y-\widehat y)|\), co nie przekracza \(|x-\widehat x|+|y-\widehat y|\) na mocy nierówności trójkąta. \(\square\)

**Twierdzenie 13 (przedział sumy).** Jeśli \(a\le x\le b\) i \(c\le y\le d\), to \(a+c\le x+y\le b+d\).

*Dowód.* Dodanie lewych i prawych nierówności zachowuje ich kierunek. \(\square\)

**Twierdzenie 14 (błąd pomiaru a decyzja).** Jeżeli \(x\in[a,b]\), to wniosek \(x\le T\) jest gwarantowany, gdy \(b\le T\), a wniosek \(x>T\) jest gwarantowany, gdy \(a>T\). W pozostałych przypadkach sam przedział może nie wystarczać do decyzji.

*Dowód.* Pierwsze dwie implikacje wynikają bezpośrednio z przechodniości porządku. Jeśli \(a\le T<b\), przedział dopuszcza wartości po obu stronach progu, zatem sam zapis nie rozstrzyga, która wystąpiła. \(\square\)

**Przykład 8.** Dwie deski mają długości odpowiednio \(120\pm1\) cm i \(85\pm2\) cm. Ich łączna długość należy do \([119+83,121+87]=[202,208]\) cm. Zapis 205 cm jest wartością centralną, nie gwarancją dokładnego wyniku.

**Kontrprzykład 7 (pozorna precyzja).** Pomiar wykonany linijką z podziałką co 1 cm i odczytany jako „około 8 cm” nie uzasadnia sam przez się zapisu 8,000000 cm.

## 8. Pomiar w praktyce i kontrola jednostek

**Twierdzenie 15 (jednostka iloczynu).** Jeśli \(a\) wyrażono w metrach, a \(b\) w metrach, to iloczyn \(ab\) ma jednostkę metr kwadratowy. Jeżeli \(a\) wyrażono w metrach, a \(b\) w sekundach, iloczyn ma jednostkę metrosekunda, nie metr kwadratowy.

*Dowód.* Formalny zapis \(a=(\alpha\,\mathrm m)\), \(b=(\beta\,\mathrm m)\) daje \(ab=\alpha\beta\,\mathrm m^2\); analogicznie dla różnych jednostek. \(\square\)

**Twierdzenie 16 (niezmienność pola przy zgodnej konwersji).** Jeśli \(a,b\) podano w metrach, a następnie obie długości przeliczono na centymetry, to po przeliczeniu wyniku z \(\mathrm{cm}^2\) na \(\mathrm m^2\) otrzymuje się to samo pole.

*Dowód.* \((100a)(100b)\mathrm{cm}^2=10\,000ab\,\mathrm{cm}^2=ab\,\mathrm m^2\). \(\square\)

**Przykład 9.** Na planie w skali 1:200 ściana ma długość 4,5 cm. W rzeczywistości ma 900 cm = 9 m. Jeśli jej wysokość wynosi 3 m, pole ściany to 27 \(\mathrm m^2\), a nie 13,5 \(\mathrm{cm}^2\).

**Ograniczenia matematyczne i fizyczne.** Równości długości i pól są dokładne w idealnym modelu geometrii euklidesowej; pomiary rzeczywiste mają niepewność. Addytywność masy jest adekwatna do typowych szkolnych doświadczeń, nie stanowi twierdzenia o wszystkich układach fizycznych. Skala mapy na powierzchni Ziemi może zależeć od odwzorowania kartograficznego.

# Część B. Ćwiczenia rozwiązane

## Zestaw I — długość i jednostki

**Zadanie 1.** Zamień 3,2 m na centymetry. *Rozwiązanie.* \(3{,}2\cdot100=320\) cm.

**Zadanie 2.** Zamień 4500 mm na metry. *Rozwiązanie.* \(4500:1000=4{,}5\) m.

**Zadanie 3.** Dodaj 2 m 35 cm i 85 cm. *Rozwiązanie.* \(235+85=320\) cm = 3 m 20 cm.

**Zadanie 4.** Oblicz różnicę 5 km i 750 m. *Rozwiązanie.* \(5000-750=4250\) m = 4,25 km.

**Zadanie 5.** Punkt A ma współrzędną -4, B ma 9. Podaj odległość. *Rozwiązanie.* \(|9-(-4)|=13\).

**Zadanie 6.** Turysta idzie 3 km na wschód i 3 km na zachód. Ile przeszedł i jaka jest odległość od startu? *Rozwiązanie.* Droga 6 km, odległość od startu 0 km.

**Zadanie 7.** Na odcinku od 2 do 17 zaznaczono punkt 8. Oblicz długości części. *Rozwiązanie.* \(8-2=6\) oraz \(17-8=9\), razem 15.

**Zadanie 8.** Czy 240 cm jest większe niż 2,5 m? *Rozwiązanie.* Nie, bo 2,5 m = 250 cm.

**Zadanie 9.** Wyznacz długość sznurka z trzech części: 0,7 m, 25 cm, 150 mm. *Rozwiązanie.* 70+25+15=110 cm = 1,1 m.

**Zadanie 10.** Czy odległości 2, 3 i 6 mogą być bokami trójkąta? *Rozwiązanie.* Nie, bo \(2+3<6\); naruszają nierówność trójkąta.

## Zestaw II — masa, pole i objętość

**Zadanie 11.** Dodaj 1 kg 600 g i 750 g. *Rozwiązanie.* \(1600+750=2350\) g = 2 kg 350 g.

**Zadanie 12.** Odejmij 450 g od 2 kg. *Rozwiązanie.* \(2000-450=1550\) g = 1 kg 550 g.

**Zadanie 13.** Oblicz pole prostokąta 7 cm na 12 cm. *Rozwiązanie.* \(7\cdot12=84\,\mathrm{cm}^2\).

**Zadanie 14.** Zamień 3 \(\mathrm m^2\) na \(\mathrm{cm}^2\). *Rozwiązanie.* \(3\cdot10\,000=30\,000\,\mathrm{cm}^2\).

**Zadanie 15.** Czy 5000 \(\mathrm{cm}^2\) to pół metra kwadratowego? *Rozwiązanie.* Tak, \(5000/10\,000=0{,}5\).

**Zadanie 16.** Prostokąt ma pole 48 \(\mathrm{cm}^2\), jeden bok 6 cm. Znajdź drugi. *Rozwiązanie.* \(48:6=8\) cm.

**Zadanie 17.** Podziel prostokąt 5 m na 8 m na części o szerokościach 3 m i 5 m. Sprawdź pola. *Rozwiązanie.* \(5\cdot3+5\cdot5=15+25=40\,\mathrm m^2\).

**Zadanie 18.** Sześcian ma krawędź 4 cm. Oblicz objętość. *Rozwiązanie.* \(4^3=64\,\mathrm{cm}^3\).

**Zadanie 19.** Zamień 2,5 litra na mililitry. *Rozwiązanie.* \(2{,}5\cdot1000=2500\) ml.

**Zadanie 20.** Ile litrów mieści prostopadłościan 20 cm × 10 cm × 5 cm? *Rozwiązanie.* \(1000\,\mathrm{cm}^3=1\,\mathrm{dm}^3=1\) l.

## Zestaw III — skala i czas

**Zadanie 21.** Na mapie 1:10 000 odcinek ma 6 cm. Jaka jest odległość rzeczywista? *Rozwiązanie.* \(60\,000\) cm = 600 m.

**Zadanie 22.** Droga ma 2 km. Jaką długość ma na mapie 1:50 000? *Rozwiązanie.* \(200\,000:50\,000=4\) cm.

**Zadanie 23.** Plan 1:100 przedstawia pokój 5 cm × 4 cm. Jakie są wymiary rzeczywiste? *Rozwiązanie.* 5 m × 4 m.

**Zadanie 24.** Jaka jest powierzchnia pokoju z zadania 23? *Rozwiązanie.* \(5\cdot4=20\,\mathrm m^2\).

**Zadanie 25.** Czy skala 1:100 zmniejsza pole 100 razy? *Rozwiązanie.* Nie, \(100^2=10\,000\) razy.

**Zadanie 26.** Ile minut trwa okres od 08:35 do 09:20? *Rozwiązanie.* 25+20=45 min.

**Zadanie 27.** Zajęcia zaczęły się o 11:45 i trwały 95 min. Kiedy się skończyły? *Rozwiązanie.* 95 min = 1 h 35 min, więc o 13:20.

**Zadanie 28.** Od 22:50 do 00:10 następnego dnia ile minut mija? *Rozwiązanie.* 70 min do północy i 10 min po północy, razem 80 min.

**Zadanie 29.** Ile sekund ma 2 min 15 s? *Rozwiązanie.* \(2\cdot60+15=135\) s.

**Zadanie 30.** Na planie 1:250 długość 8 cm oznacza ile metrów? *Rozwiązanie.* \(8\cdot250=2000\) cm = 20 m.

## Zestaw IV — niepewność i weryfikacja

**Zadanie 31.** Pomiar wynosi \(10\pm0{,}5\) cm. Podaj przedział. *Rozwiązanie.* \([9{,}5,10{,}5]\) cm.

**Zadanie 32.** Dwie długości należą do \([9,11]\) cm i \([14,16]\) cm. Podaj przedział sumy. *Rozwiązanie.* \([23,27]\) cm.

**Zadanie 33.** Półka ma udźwig 20 kg, a masa przedmiotu należy do \([18,21]\) kg. Czy można zagwarantować, że masa nie przekroczy udźwigu? *Rozwiązanie.* Nie, bo dopuszczalna wartość 21 kg przekracza 20 kg.

**Zadanie 34.** Zaokrąglono długość do najbliższego centymetra i otrzymano 8 cm. Podaj gwarantowaną granicę błędu zaokrąglenia. *Rozwiązanie.* Co najwyżej 0,5 cm, przy założeniu dokładnej wartości wejściowej.

**Zadanie 35.** Obie długości zaokrąglono do 1 cm. Jaki jest maksymalny błąd ich sumy po dodaniu zaokrągleń? *Rozwiązanie.* \(0{,}5+0{,}5=1\) cm.

**Zadanie 36.** Oblicz pole kwadratu o boku 20 cm w metrach kwadratowych. *Rozwiązanie.* \(400\,\mathrm{cm}^2=0{,}04\,\mathrm m^2\).

**Zadanie 37.** Czy \(2\,\mathrm m\cdot3\,\mathrm m=6\,\mathrm m\)? *Rozwiązanie.* Nie, wynik ma jednostkę \(\mathrm m^2\).

**Zadanie 38.** Waga pokazuje 1,20 kg. Czy bez dodatkowych informacji można uznać błąd za mniejszy niż 0,005 kg? *Rozwiązanie.* Nie; liczba cyfr nie zastępuje danych o dokładności przyrządu.

**Zadanie 39.** Na mapie 1:25 000 odcinek ma 8 cm. Oblicz odległość. *Rozwiązanie.* \(8\cdot25\,000=200\,000\) cm = 2 km.

**Zadanie 40.** Czy odcinki o długościach 5 cm, 8 cm i 14 cm mogą być bokami trójkąta? *Rozwiązanie.* Nie, bo \(5+8=13<14\).

## Problemy przekrojowe

**Problem A (wykładzina).** Pokój ma 4 m × 3,5 m. Jedna paczka pokrywa 2 \(\mathrm m^2\). Ile paczek potrzeba, nie uwzględniając odpadów?

*Rozwiązanie.* Pole to \(4\cdot3{,}5=14\,\mathrm m^2\). Liczba paczek \(14:2=7\). W praktyce zapas zależy od sposobu cięcia, którego zadanie nie określa.

**Problem B (skala i pole).** Na planie 1:200 prostokąt ma boki 3 cm i 5 cm. Wyznacz rzeczywiste pole.

*Rozwiązanie.* Długości rzeczywiste: \(3\cdot200=600\) cm = 6 m i \(5\cdot200=1000\) cm = 10 m. Pole \(60\,\mathrm m^2\). Kontrola: pole na planie \(15\,\mathrm{cm}^2\), pomnożone przez \(200^2=40\,000\), daje \(600\,000\,\mathrm{cm}^2=60\,\mathrm m^2\).

**Problem C (czas i droga).** Fotograf przeszedł 1200 m w 20 minut, potem 600 m w 15 minut. Oblicz łączną drogę, czas i średnią szybkość w m/min.

*Rozwiązanie.* Droga \(1200+600=1800\) m, czas \(20+15=35\) min. Średnia szybkość \(1800/35=360/7\approx51{,}43\) m/min. Nie wolno uśredniać arytmetycznie szybkości z etapów o różnym czasie bez uwzględnienia wag.

**Problem D (decyzja przy niepewności).** Dwie paczki mają masy \(4{,}0\pm0{,}2\) kg oraz \(5{,}0\pm0{,}3\) kg. Limit wynosi 9,5 kg. Czy suma na pewno mieści się w limicie?

*Rozwiązanie.* Pierwsza masa należy do \([3{,}8,4{,}2]\), druga do \([4{,}7,5{,}3]\). Suma należy do \([8{,}5,9{,}5]\) kg. Tak, przy założeniu poprawności obu przedziałów, maksymalna masa równa się limitowi i go nie przekracza.

## Uwagi do kontroli wydawniczej

Twierdzenia są elementarnymi wnioskami w idealnym modelu matematycznym; nie stanowią certyfikacji rzeczywistych przyrządów. Podział na część A i B służy niezależnej kontroli minimum treści teoretycznej i ćwiczeniowej. Dopiero skład dokładnego źródła oraz ocena niepustych stron pozwolą potwierdzić objętość. **Nie dodawać stron do bilansu 585/1222 przed integracją z monolitem 0.20.**

## Powiązania z zachowanym manuskryptem

- **F20.3 — Skala i wymiar:** istniejący rozdział obejmuje typowaną algebrę wymiarów, homotetię, skalowanie wielkości i certyfikaty błędu na poziomie bardziej formalnym. E0-04 wykorzystuje te same podstawowe prawa w zakresie wczesnoszkolnym, bez przepisywania zaawansowanych konstrukcji F20.3.
- **F13.2 — Model prostokątny:** istniejący rozdział obejmuje enumerację podprostokątów i certyfikaty siatki. E0-04 ogranicza się do interpretacji pola prostokąta przez kwadraty jednostkowe, wymaganej na poziomie I.
- Przed integracją redakcyjną należy skontrolować, czy przykłady nie dublują tekstu wcześniejszego monolitu, i pozostawić tylko potrzebne dydaktycznie odesłania. Żadnego z wymienionych rozdziałów nie zmieniono.
