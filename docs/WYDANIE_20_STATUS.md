# Wydanie 0.20 — stan publikacji i synchronizacji (30 października 2026)

**Wersja wydawnicza:** jeden monolit PDF, **864 strony**.  
**Niezmieniony wstęp historyczny:** strony **1–33**, porównanie 33/33 stron tekstowo zgodnych z 0.19.  
**Taksonomia jako spis treści:** strony **34–113**, 80 stron indeksu, 6006 unikalnych kodów MSC2020 i 514 podtematów autorskich.  
**Materiał zachowany MSC2020:** strony **668–864**, 197/197 stron tekstowo identycznych z 0.19.  
**Stan treści Tomu I przed spisem:** 585 stron; 80 stron nawigacji nie zwiększa progu 1222 stron naukowych.  
**Test:** dwie kompilacje XeLaTeX pomyślne; kontrola struktury i porównanie tekstów automatyczne. Brak niezależnej recenzji naukowej.

## Integralność artefaktów lokalnych

- `ONTOLOGIA_LICZBY_WYDANIE_20.pdf`, SHA256 `ea888d112cc255856c03cead7428d4f817ad2c692d0e6e6d61f46ae17738dd43`
- `ONTOLOGIA_LICZBY_SPIS_TRESCI_TAKSONOMIA_2026.pdf`, SHA256 `099346fb4730c584b36844d3a5db25782e51934d5d9d0e911cb688c632d96447`
- `TAKSONOMIA_MATEMATYKI_WYDANIE_JEDNOLITE_PELNE_2026.pdf`, 637 stron, SHA256 `0fcf0ee0fe92a3b23a43cd15bbea103bb48a9a1b65ec04273bcf55e1e6710ae5`

## Co rzeczywiście znajduje się w tym repo

- `README.md`: obowiązująca kolejność redakcyjna i minima.
- `docs/SPIS_TRESCI_NADRZEDNY.md`: nadrzędna nawigacja po wstępie.
- `taxonomy/TEKST_ZRODLOWY_01.md` … `taxonomy/TEKST_ZRODLOWY_10.md`: pełny tekstowy eksport 637-stronicowego PDF, bez warstwy graficznej.
- `taxonomy/index/MSC_LEVEL_I.tsv` … `MSC_LEVEL_V.tsv`: 6006 kodów z przypisaniem autorskiego poziomu i numerem strony źródła.
- `taxonomy/index/AUT_514.tsv`: 514 autorskich pozycji.

**Ważne:** binarne pliki `.pdf` nie zostały jeszcze przesłane do GitHub. Powyższe wartości SHA służą do zweryfikowania późniejszej kopii; nie są dowodem jej obecności w repo. Nie wolno oznaczać repo jako zsynchronizowanego z wydaniem PDF, dopóki pliki nie pojawią się w drzewie `main`.

## Reguła obowiązująca

`Okładka → wstęp historyczny bez zmian → taksonomia jako spis treści → indywidualne opracowania`. Pozycje indeksowe nie są gotowymi monografiami. Docelowe strony Tomu I: **1222 stron naukowej treści**; rozdziału ani dowodu nie należy rozcinać między tomami.
