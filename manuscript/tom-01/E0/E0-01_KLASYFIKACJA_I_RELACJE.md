---
title: 'ONTOLOGIA LICZBY — TOM I'
subtitle: 'E0-01. Klasyfikacja i relacje — podstawa pojęcia liczby'
author: 'Andrzej Mikulski'
date: '1 listopada 2026'
lang: pl-PL
fontsize: 11pt
geometry: margin=18mm
---

**Taksonomia:** E0-01, poziom I; porządek, klasy równoliczne, cechy obiektów, regularności. Powiązania tematyczne z MSC 03, 06, 97 nie oznaczają, że E0-01 jest kodem MSC. **Status:** materiał merytoryczny w toku pełnego składu, bez doliczenia do 585/1222. Chroniony wstęp historyczny pozostaje nienaruszony.

# 1. Klasyfikacja poprzedza liczenie

**Definicja 1 (cecha).** Dla skończonej kolekcji rozróżnialnych obiektów \(X\) i zbioru wartości \(V\), cechą nazywamy funkcję \(c:X\to V\). Warunek bycia funkcją oznacza, że każdy obiekt ma dokładnie jedną ustaloną wartość wybranej cechy. Jeśli klocek ma kilka kolorów, należy sprecyzować, czy chodzi o kolor wskazanej ścianki, czy o zbiór kolorów.

**Definicja 2 (klasa cechy).** \(C_v=\{x\in X:c(x)=v\}\). Wartość \(v\) nie musi występować; wtedy \(C_v=\varnothing\). Rodzina niepustych klas to podział wyznaczony przez \(c\).

**Twierdzenie 1 (podział).** Niepuste klasy cechy są parami rozłączne i ich suma zbiorowa wynosi \(X\).

*Dowód.* Każdy \(x\) należy do \(C_{c(x)}\). Jeśli \(x\in C_v\cap C_w\), to \(c(x)=v=w\). Dwie klasy o różnych wartościach nie mają zatem wspólnego elementu. \(\square\)

**Twierdzenie 2 (kontrola liczebności).** Dla skończonego \(X\) zachodzi \(|X|=\sum_{v\in c(X)}|C_v|\).

*Dowód.* Na mocy Twierdzenia 1 każdy obiekt pojawia się dokładnie w jednej klasie; zsumowanie liczebności rozłącznych klas liczy go dokładnie raz. \(\square\)

**Przykład.** Dla sześciu kart kolory czerwony, niebieski, czerwony, zielony, niebieski, czerwony wyznaczają klasy o liczebnościach \(3,2,1\). Suma \(3+2+1=6\) kontroluje, czy nie pominięto karty.

**Kontrprzykład 1.** Zbiory „czerwone” i „okrągłe” nie muszą być rozłączne. Czerwone koło należy do obu; ich liczebności nie wolno bez korekty sumować jako liczby wszystkich obiektów.

**Definicja 3 (cecha złożona).** Dla cech \(c:X\to V\) i \(s:X\to W\) definiujemy \(d(x)=(c(x),s(x))\). Klasy \(d\) oznaczają wspólny kolor i kształt.

**Twierdzenie 3 (uszczegółowienie).** Każda klasa cechy złożonej \(d=(c,s)\) zawiera się w jednej klasie cechy \(c\) oraz w jednej klasie cechy \(s\).

*Dowód.* Równość \(d(x)=(v,w)\) pociąga \(c(x)=v\) i \(s(x)=w\). \(\square\)

**Kontrprzykład 2.** Dwa kolory i trzy kształty dają sześć *możliwych* par, lecz niekoniecznie sześć niepustych klas: niektóre pary mogą nie występować.

# 2. Relacje i klasy równoważności

**Definicja 4 (relacja).** Relacją na \(X\) nazywamy dowolny podzbiór \(R\subseteq X\times X\). Zapis \(xRy\) znaczy \((x,y)\in R\).

**Definicja 5 (własności).** Relacja jest zwrotna, gdy \(xRx\) dla każdego \(x\); symetryczna, gdy \(xRy\Rightarrow yRx\); przechodnia, gdy \(xRy\land yRz\Rightarrow xRz\).

**Twierdzenie 4 (równość cechy).** Relacja \(x\sim_c y\iff c(x)=c(y)\) jest zwrotna, symetryczna i przechodnia.

*Dowód.* Wszystkie trzy własności wynikają kolejno ze zwrotności, symetrii i przechodniości równości wartości funkcji. \(\square\)

**Definicja 6 (równoważność).** Relacja spełniająca trzy własności z Definicji 5 jest równoważnością. Jej klasa \([x]=\{y:y\sim x\}\).

**Twierdzenie 5 (klasy równoważności).** Dwie klasy równoważności są identyczne albo rozłączne.

*Dowód.* Jeśli \(z\in[x]\cap[y]\), to \(z\sim x\) i \(z\sim y\). Symetria i przechodniość dają \(x\sim y\). Dla dowolnego \(u\sim x\) otrzymujemy \(u\sim y\), więc \([x]\subseteq[y]\). Analogicznie \([y]\subseteq[x]\). \(\square\)

**Kontrprzykład 3.** Na \(X=\{1,2,3\}\) relacja \(|x-y|\le1\) jest zwrotna i symetryczna, ale nieprzechodnia: \(1R2\), \(2R3\), lecz nie \(1R3\). Nie tworzy klas równoważności.

**Definicja 7 (równoliczność).** Skończone zbiory \(A,B\) są równoliczne, gdy istnieje bijekcja \(f:A\to B\), czyli sparowanie bez pominięć i powtórzeń.

**Twierdzenie 6 (równoliczność jest równoważnością).** Równoliczność jest zwrotna, symetryczna i przechodnia.

*Dowód.* Tożsamość \(\operatorname{id}_A\) jest bijekcją. Odwrotność bijekcji jest bijekcją. Złożenie dwóch bijekcji jest bijekcją. \(\square\)

**Kontrprzykład 4.** Trzy łyżki i trzy kubki są równoliczne, ale nie są tym samym zbiorem. Równoliczność nie oznacza identyczności obiektów.

# 3. Porządek i regularności

**Definicja 8 (porządek częściowy).** Relacja \(\preceq\) jest porządkiem częściowym, gdy jest zwrotna, antysymetryczna (\(x\preceq y\land y\preceq x\Rightarrow x=y\)) i przechodnia. Jest liniowa, gdy każda para jest porównywalna.

**Twierdzenie 7 (zawieranie).** Relacja \(\subseteq\) na rodzinie podzbiorów ustalonego zbioru jest porządkiem częściowym.

*Dowód.* Każdy zbiór zawiera się w sobie. Dwa zbiory zawierające się wzajemnie są równe. Z \(A\subseteq B\subseteq C\) wynika \(A\subseteq C\). \(\square\)

**Kontrprzykład 5.** Zbiory \(\{1\}\) i \(\{2\}\) są nieporównywalne względem zawierania. Porządek częściowy nie musi być liniowy.

**Definicja 9 (minimalny i najmniejszy).** Element \(m\) jest minimalny, gdy nie ma elementu ściśle mniejszego. Jest najmniejszy, gdy \(m\preceq x\) dla każdego \(x\).

**Twierdzenie 8 (istnienie minimalnego).** Każdy skończony niepusty zbiór częściowo uporządkowany ma element minimalny.

*Dowód.* Z dowolnego elementu przechodzimy do ściśle mniejszego, jeśli istnieje. Nie można wrócić do już odwiedzonego elementu, gdyż powstałby cykl sprzeczny z antysymetrią i przechodniością. Ponieważ zbiór jest skończony, proces musi się zakończyć na elemencie minimalnym. \(\square\)

**Kontrprzykład 6.** Dwa różne sznurki tej samej długości spełniają „nie dłuższy niż” w obie strony. Ta relacja nie jest antysymetryczna na *sznurkach*, choć jest na klasach jednakowej długości.

**Definicja 10 (regularność).** Skończony wzór symboli jest funkcją \(a:\{0,\ldots,n-1\}\to S\). Reguła przedłużania jest dodatkowym założeniem; nie wynika z samego skończonego wzoru.

**Twierdzenie 9 (niejednoznaczność).** Jeśli \(S\) zawiera co najmniej dwa symbole, każdy skończony wzór ma co najmniej dwa różne nieskończone przedłużenia.

*Dowód.* Po ostatniej zadanej pozycji można wpisywać wyłącznie pierwszy albo wyłącznie drugi z dwóch różnych symboli. Oba ciągi mają ten sam zadany początek i różnią się na następnej pozycji. \(\square\)

**Twierdzenie 10 (powtarzanie bloku).** Przy regule cyklicznego powtarzania bloku \(b_0,\ldots,b_{p-1}\) symbol na pozycji \(k\) jest równy \(b_{k\bmod p}\).

*Dowód.* Dzielimy \(k=qp+r\), \(0\le r<p\). Po \(q\) pełnych blokach pozostaje pozycja \(r\). \(\square\)

# 4. Zadania z pełnymi rozwiązaniami

**Zadanie 1.** Kolory kart \(a,b,c,d,e\) to czerwony, zielony, czerwony, niebieski, zielony. Utwórz klasy i sprawdź sumę. *Rozwiązanie:* \(\{a,c\},\{b,e\},\{d\}\), odpowiednio \(2+2+1=5\); klasy są rozłączne i pokrywają kolekcję.

**Zadanie 2.** Figury: czerwone koło \(a\), czerwony trójkąt \(b\), niebieskie koło \(c\), czerwone koło \(d\). Podziel według koloru i pary (kolor, kształt). *Rozwiązanie:* kolory \(\{a,b,d\},\{c\}\); pary \(\{a,d\},\{b\},\{c\}\). Każda nowa klasa zawiera się w jednej starej.

**Zadanie 3.** W pudełku nie ma zielonych klocków. Czy \(C_{\rm zielony}\) istnieje? *Rozwiązanie:* jest zdefiniowana i pusta. Nie należy do rodzin klas niepustych.

**Zadanie 4.** Polecenie „połącz podobne figury” daje różne wyniki. Czy musi istnieć błąd? *Rozwiązanie:* nie; kryterium „podobne” jest nieokreślone. Trzeba wskazać np. tę samą barwę lub kształt.

**Zadanie 5.** Cztery kubki i pięć spodków: można dopasować każdemu kubkowi inny spodek. Czy zbiory są równoliczne? *Rozwiązanie:* nie; jeden spodek pozostaje wolny. Iniekcja nie jest bijekcją.

**Zadanie 6.** Wykaż, że trzy jabłka i trzy kubki są równoliczne, ale różne. *Rozwiązanie:* sparuj je po jednym. Zbiory nie są równe, ponieważ jabłko nie jest kubkiem.

**Zadanie 7.** Sprawdź przechodniość relacji \(|x-y|\le1\) na \(\{1,2,3\}\). *Rozwiązanie:* \(1R2\), \(2R3\), ale nie \(1R3\), więc relacja nie jest przechodnia.

**Zadanie 8.** Podziel \(\{1,2,3,4,5,6\}\) według parzystości. *Rozwiązanie:* \(\{1,3,5\}\) i \(\{2,4,6\}\). Są rozłączne, pokrywają całość, obie mają po trzy elementy.

**Zadanie 9.** W rodzinie \(\{\{1\},\{2\},\{1,2\}\}\) znajdź elementy minimalne względem zawierania. *Rozwiązanie:* \(\{1\}\) i \(\{2\}\); żaden z nich nie jest najmniejszy, bo są nieporównywalne.

**Zadanie 10.** Czy „nie dłuższy niż” jest porządkiem częściowym na dwóch różnych sznurkach długości 20 cm? *Rozwiązanie:* nie; zachodzi w obie strony, choć sznurki są różne. Na klasach jednakowej długości antysymetria jest przywrócona.

**Zadanie 11.** Reguła powtarza blok \(K,K,T\). Co występuje na pozycji 20 liczonej od zera? *Rozwiązanie:* \(20=6\cdot3+2\), więc \(T\).

**Zadanie 12.** Podano \(A,B,A,B\). Czy piątym symbolem musi być \(A\)? *Rozwiązanie:* nie. Reguła naprzemienna daje \(A\), ale reguła „od piątej pozycji zawsze \(B\)” daje \(B\).

**Zadanie 13.** Czerwone figury są kołami lub trójkątami. Czy klasa czerwonych musi zawierać się w jednej klasie kształtu? *Rozwiązanie:* nie; czerwone koło i czerwony trójkąt mają tę samą barwę, ale różne kształty.

**Zadanie 14.** W pięciu figurach są trzy czerwone i trzy koła, w tym dwa czerwone koła. Ile figur jest czerwonych lub okrągłych? *Rozwiązanie:* \(3+3-2=4\). Nie wolno podwójnie liczyć przecięcia.

**Zadanie 15.** Na \(\{2,3,6\}\) uporządkuj przez podzielność. *Rozwiązanie:* minimalne są \(2,3\), największy \(6\), najmniejszy nie istnieje.

**Zadanie 16.** Sześć kart podzielono na rozłączne klasy o liczebnościach \(2,3,2\). Czy protokół jest poprawny? *Rozwiązanie:* nie, bo suma \(7\ne6\). Co najmniej jedno z założeń (rozłączność, liczebności, rozmiar kolekcji) jest błędne.

**Zadanie 17.** Cztery obiekty mają etykiety \(a,a,b,a\). Ile jest uporządkowanych par z tą samą etykietą? *Rozwiązanie:* klasy mają rozmiary \(3,1\); liczba par to \(3^2+1^2=10\).

**Zadanie 18.** Czy podział \(\{\{a,b\},\{c\},\{d,e\}\}\) uszczegóławia \(\{\{a,b,c\},\{d,e\}\}\)? *Rozwiązanie:* tak; każda klasa pierwszego podziału mieści się w jednej klasie drugiego.

**Zadanie 19.** Dwa pomiary długości sznurków dają naprzemiennie \(10{,}0\) i \(10{,}1\) cm. Czy można dowieść, który jest krótszy? *Rozwiązanie:* nie bez informacji o niepewności i metodzie pomiaru.

**Zadanie 20.** Książki \(k_1,k_2,k_3\) są w twardej oprawie, \(k_4,k_5\) w miękkiej; ilustrowane są \(k_1,k_4\). Utwórz klasy pary cech. *Rozwiązanie:* \(\{k_1\},\{k_2,k_3\},\{k_4\},\{k_5\}\). Każda książka należy dokładnie do jednej klasy.

**Zadanie 21.** Ala, Bartek, Celina stoją na miejscach 1,2,3. Czy „stoi nie później niż” jest porządkiem liniowym? *Rozwiązanie:* tak; relacja na numerach miejsc jest zwrotna, antysymetryczna, przechodnia i każda para numerów jest porównywalna.

**Zadanie 22.** Dziesięć klocków podzielono na trzy niepuste klasy. Udowodnij, że jedna ma co najmniej cztery elementy. *Rozwiązanie:* gdyby każda miała najwyżej trzy, razem byłoby co najwyżej dziewięć; sprzeczność.

**Zadanie 23.** Zmieniono różnowartościowo nazwy etykiet \(A,B,C\) na \(X,Y,Z\). Czy klasy się zmienią? *Rozwiązanie:* nie; zachowana jest równość i nierówność wartości. Połączenie dwóch nazw w jedną może jednak scalić klasy.

**Zadanie 24.** Cztery obiekty mają kolory zielony, zielony, żółty, czerwony. Podaj liczbę obiektów, klas i par o jednakowym kolorze. *Rozwiązanie:* odpowiednio \(4,3,2^2+1^2+1^2=6\).

# 5. Weryfikacja i powiązania

Na poziomie wczesnoszkolnym najpierw pracujemy na przedmiotach, parach i grupach; język funkcji i relacji jest warstwą ścisłego uzasadnienia. Należy oddzielić poprawność reguły klasyfikacji od poprawności zliczania i od umiejętności wyjaśnienia, dlaczego wynik jest jednoznaczny. Dla pustej kolekcji istnieje zero klas niepustych; dla kolekcji jednoelementowej jedna klasa niepusta. Zamiana nazw etykiet bijekcją nie zmienia podziału, natomiast scalenie etykiet może go zmienić.

**Źródła orientacyjne:** „Taksonomia Matematyki”, wydanie jednolite 2026, poziom I, E0-01 (s. 6 i 9 eksportu); G. Pólya, *How to Solve It*; K. H. Rosen, *Discrete Mathematics and Its Applications*; F9.1 istniejącego manuskryptu Tomu I. Nie odtwarzano tekstów źródłowych.

**Ograniczenia:** dowody wymagają niezależnej kontroli redakcyjnej; testy przypadków skończonych nie są formalną mechanizacją twierdzeń. Osobny podgląd PDF nie stanowi integracji z wydaniem 0.20. Oficjalny bilans pozostaje 585/1222.
