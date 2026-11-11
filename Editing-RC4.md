# Editing rapido — Meighty 1.01 RC4 / HW13 candidata

Questi comandi richiedono la build candidata RC4/HW13, ora proposta dall’installer pubblico. La precedente RC3/HW12 resta disponibile per il ritorno. Non è stato eseguito un flash sul dispositivo durante questa pubblicazione; il collaudo dei tasti fisici è ancora da fare.

## Comandi del pannello

Nelle pagine **Song, Phrase, Chain e Table**, tenere premuto **ARP** equivale a
SHIFT. In Instrument, ARP continua ad aprire il catalogo preset.

| Combinazione | Azione |
|---|---|
| ARP + ALGORITHM | Estende la selezione verticalmente dalla cella iniziale. |
| ARP + K1 | Estende la selezione fra colonne; in Song fra tracce. |
| ARP + K2 verso destra | Include tutte le colonne delle righe selezionate, anche una sola riga. Non sposta il cursore verticalmente. |
| ARP + K2 verso sinistra | Torna alla selezione rettangolare di celle. |
| ARP + OCT− | Cancella la cella o l'area selezionata. |
| ARP + OCT+ | Copia la cella o l'area selezionata. |
| ARP + REC | Incolla. Non inserisce una nota REC e non accoda un salto Song. |
| ARP + HOME | Annulla l'ultima cancellazione o incolla, nello stesso oggetto. |
| ARP premuto e rilasciato senza altre azioni | Toglie la selezione. La copia negli appunti resta disponibile. |

La selezione resta evidenziata quando rilasci ARP. La testata indica l'intervallo
di righe; il LED ARP indica SHIFT o una selezione attiva. Le azioni confermano
COPIED, CLEARED, PASTED o UNDONE sul display.

Per scegliere la destinazione, sposta il cursore **senza ARP**: la selezione si
chiude, gli appunti restano. Se invece incolli mentre la selezione è ancora
attiva, il blocco parte dal suo angolo superiore sinistro. Copia → cancella →
incolla senza muoversi ripristina quindi il blocco nello stesso punto.

## Esempi

**Togliere un delay da una riga:** in Phrase seleziona il comando FX interessato,
poi ARP + OCT−. Comando e valore vengono azzerati insieme; nota e strumento
restano intatti. Se selezioni soltanto VAL, viene azzerato soltanto il valore.

**Duplicare quattro righe complete:** parti dalla prima riga, tieni ARP e dai
uno scatto positivo a K2. Con ALGORITHM avanza di tre righe, sempre tenendo ARP.
Rilascia ARP, premi ARP + OCT+ e poi vai alla destinazione senza ARP.
ARP + REC incolla le quattro righe con nota, strumento e tutti gli FX.

**Creare una variazione in un'altra Phrase:** copia il blocco, cambia ID Phrase
con K3 senza ARP e seleziona la riga di arrivo. ARP + REC incolla. I riferimenti
agli Instrument sono conservati: non vengono duplicati i suoni.

**Copiare solo una sequenza di note:** seleziona NOTE nella prima riga, tieni
ARP e usa solo ALGORITHM per estendere verticalmente. Copia, scegli NOTE alla
destinazione e incolla. Gli Instrument e gli FX di destinazione restano intatti.

**Copiare una Phrase intera:** parti dalla riga 00, ARP + K2 positivo per tutte
le colonne, ARP + ALGORITHM fino a 0F, quindi copia. Nel nuovo ID Phrase parti
dalla riga 00 e incolla.

## Comportamenti e limiti

- La cancellazione di NOTE produce `---`, non `OFF`: non scrive un evento di rilascio.
- La cancellazione di Instrument produce lo strumento vuoto; non cancella il preset.
- Song cancella i riferimenti alle Chain. Chain cancella i riferimenti alle Phrase;
  LEN resta invariato. Una copia in Chain riguarda soltanto i riferimenti, non le Phrase richiamate.
- In Table il valore neutro di trasposizione è 0 e quello di velocity è FF.
- Le coppie comando/valore FX vengono copiate insieme quando la selezione include il comando.
- Si incolla fra oggetti della stessa pagina e in colonne compatibili:
  per esempio FX1 può andare in FX2, ma una nota non può diventare un comando FX.
- Le righe complete si incollano dalla prima colonna, indipendentemente dal campo corrente.
- Se il blocco supera l'ultima riga o colonna, l'incolla viene rifiutato interamente:
  niente troncamenti e niente ritorno alla prima riga.
- Gli appunti restano fra pagine e oggetti dello stesso progetto. Load, New project
  e inizializzazione della RAM li azzerano. Non sono salvati negli slot.
- L'annullamento è di un solo livello, per l'ultima cancellazione/incolla.
  Un successivo inserimento di note o una modifica manuale di valore lo invalida.
- Tutte le modifiche sono in RAM: usa Save slot per conservarle.
- Senza ARP, OCT−/OCT+ continuano a fare mute/solo in Song; PLAY e gli altri
  comandi normali mantengono il loro comportamento.

## Collaudo

Il dispatcher del pannello e il rendering 240×240 sono stati provati con
controlli e NOR simulati, con AddressSanitizer e UndefinedBehaviorSanitizer.
I casi comprendono selezioni inverse, righe complete, rettangoli, coppie FX,
incolla fra Phrase, controlli sui limiti/tipi, Undo e assenza di effetti collaterali
su mute, solo, REC e cambi pagina. La prova sui tasti fisici è ancora da fare.
