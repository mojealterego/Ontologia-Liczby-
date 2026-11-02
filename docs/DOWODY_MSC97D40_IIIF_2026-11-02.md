# Protokół wykonawczy — MSC 97D40 III-F, 2 listopada 2026

## Zapis źródeł na main

- Manuskrypt: `manuscript/tom-01/MSC97/97D40_IIIF_LOSOWANIE_I_WNIOSKOWANIE.md`, commit `b080141a30f37408934aba6eb2ca4c4526765927`. Zakres D57–D66, T66–T76 (11 twierdzeń z dowodami), K35–K40, Z81–Z96.
- Testy: `tests/test_msc97d40_sampling.py`, commit `e6dbd26a561cbcaadc5945f1c5252187ab087a2e`. Lokalnie wykonano `python /mnt/data/test_msc97d40_sampling.py -v`: **6 testów OK**. Testy obejmują enumerację wszystkich prób dla N=2..5 i wszystkich przypisań przy małych skończonych populacjach, a także wariancję Horvitza–Thompsona i Neymana.
- Poprawka testu nieobciążoności i MSE w `tests/test_msc97d40_measurement.py`: commit `1c55d8dc613ccb9ae863f04bbe5e3dee4a809b08`; zastąpiono tautologiczną asercję porównaniem rzeczywistych momentów dwupunktowego rozkładu. Osobno lokalnie sprawdzono 330 równości dla tego rozkładu.
- Workflow `.github/workflows/tom1-msc97d40.yml`: commit `083a8870588a296779dfd0a8e01313f36683682c` dodaje część III-F i nowy test; commit `9b3cd21309241d0f7a93a752e4c5b091ad707565` dodaje diagnostykę błędów kontroli PDF. **Nie oznaczać CI jako zielonego przed sprawdzeniem przebiegu.**

## Kompilacja i integracja lokalna

- Zbudowano XeLaTeX/Pandoc **2-stronicowy podgląd kontrolny wybranych twierdzeń III-F**: `ONTOLOGIA_MSC97D40_IIIF_PODGLAD_KONTROLNY.pdf`, SHA-256 `e83fb0b0c295c3c168f1eae6d5a02b8f1142960c552fd1c67f1a509c8de5791a`. Obie strony obejrzano; 0 słów poza marginesem 5 pt.
- Do wcześniej istniejącego podglądu 647 stron (SHA-256 `d6bc2d8b3964b05ac598f8541d79f38b1ba967fd0178784b9866cce4e07288d7`) dołączono 2 strony kontrolne III-F. Wynik **649 stron**, **8 073 493 bajty**, SHA-256 `63aa50c2b9e0eb01b1385dbe3e97de40ab04227cbfd6bbb545634984aa518065`.
- Kontrola po scaleniu: **647/647 wcześniejszych stron identycznych tekstowo**, 589/589 zakładek, 4/4 odsyłacze, 0 naruszeń marginesu w nowych stronach. Oryginalny historyczny wstęp zachowany bez ingerencji.
- Plik `ONTOLOGIA_TOM_I_IIIF_MANIFEST.json` dokumentuje identyfikatory, sumy SHA-256, liczbę stron i ograniczenia.

## Granice i blokady

- Podgląd 649 stron **nie jest pełną kompilacją aktualnego HEAD rozdziału**: zawiera wcześniejsze 647 stron i **wybrane** fragmenty III-F, a nie całość III-D/III-E/III-F w jednym nowym składzie. Pełny skład ma być weryfikowany przez GitHub Actions.
- Wcześniejszy CI `41468837230` zakończył się **failure** w kroku kontroli skompilowanego PDF mimo zielonych testów; uruchomiono diagnostykę. Wpis nie potwierdza zielonego CI nowej wersji.
- Brakuje kanonicznego binarnego monolitu 0.20, opisanego jako 864 strony; dostarczony plik źródłowy ma 629 stron. Historyczne **585 stron nie zwiększono**. Minimum poziomu III: **44 strony** — nadal otwarte. Bez końcowego spisu treści i bez Tomu II.


## Aneks odbiorczy — pełny PDF z CI, 19 stron

- **GitHub Actions:** [run 41474366935](https://github.com/mojealterego/Ontologia-Liczby-/actions/runs/41474366935), commit źródłowy `9b3cd21309241d0f7a93a752e4c5b091ad707565`, wynik **success**. Z logów pobrano siedem wyników unittest: 17+10+7+10+8+8+6 = **66/66 testów OK**. Kompilacja XeLaTeX/Pandoc, kontrola 13 znaczników manuskryptu bez braków. Artefakt GitHub Actions ID **13157635325**.
- **Pełny MSC 97D40:** `MSC97D40_PELNY_ROZDZIAL.pdf` z artefaktu CI, **19 stron A4, 153 890 B**, SHA-256 `8e8940ab95a178e6f0c212c3c55e5f6842ed7880fe3531dad8e4066ff5aae634`. W składzie znajdują się główny manuskrypt i części III-D, III-E, III-F. Przekroczono wcześniejszy etap wybranych fragmentów; to kompilacja całego aktualnego rozdziału, choć minimum 44 stron poziomu III pozostaje otwarte.
- **Nowa książka robocza:** 641 stron wcześniejszego podglądu (629 oryginalnych + 6 MSC 97C20 + 6 MSC 97C30) + **19 stron pełnego 97D40 z CI** = **660 stron**, **8 088 173 B**, SHA-256 `1e31fa92a4f3d09d7c99fa0464198ffd405e577a5910961db9d978e532f34a44`. Sprawdzono **641/641** stron bazowych i **19/19** stron nowego rozdziału tekstowo, 588/588 zakładek, 4/4 odsyłacze, 0 naruszeń marginesu 5 pt na nowych stronach. Przejrzano wizualnie ostatnią stronę.
- **Granica kanoniczna:** nadal brak binarnego 0.20, dlatego 660-stronicowa książka jest wydaniem **roboczym**, nie wydaniem 0.20. Historyczny bilans 585 stron nie został zmieniony. Bez końcowego spisu treści i bez Tomu II.
