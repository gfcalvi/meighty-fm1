# Meighty — Manuale utente italiano

Edizione del 12 novembre 2026, aggiornata per Meighty 1.02. Questa guida accompagna la composizione su otto tracce: scelta dei suoni, Phrase e Chain, arrangiamento, modulazioni, mixer ed effetti. Il laboratorio mostra come combinare gli FX; il riferimento finale documenta tutti i comandi e le differenze nelle Table.

I nomi sul display restano in inglese. K1–K4 indicano i quattro encoder da sinistra a destra; i valori FX sono esadecimali. La guida descrive Meighty sul FM-1 fisico. Per installare, trasferire progetti e fare backup usa i tools da browser su Mac/PC o in MIDIWeb Browser su iPhone e iPad; il capitolo 8 spiega anche l’uso offline.

Per imparare, prepara una sola traccia, ascolta il risultato e aggiungi una trasformazione alla volta. Per lavorare su un brano esistente, salva prima uno stato nominato nell’app.


# Indice e percorsi di lettura

Primo utilizzo: capitoli 1–3, poi 8 per conservare il lavoro. Suoni e mix: capitoli 4–7. Table e generazione: capitoli 9–11. Per cercare un codice: indice FX nel capitolo 14 e riferimento per famiglie nel 12.

Gli esercizi H01–H24 sono percorsi musicali completi. Le ricette G01–G06 del capitolo 10 spiegano pool di due o tre note, estrazioni per step o per Phrase e performance evolutive, con sei percorsi guidati da ricostruire riga per riga. E01–E13 confrontano combinazioni e ordine degli FX; le tabelle riportate permettono di ricostruire ogni prova nello strumento. Ogni esercizio spiega preparazione, dati, risultato e una prova alternativa.


# 1 La prima sessione

L’obiettivo è scegliere un suono, scrivere una battuta, ascoltarla e salvarla. Prima di esplorare le trasformazioni, costruisci un collegamento semplice fra Song, Chain e Phrase. In seguito potrai riutilizzare gli stessi oggetti in un arrangiamento.


## Installare e aprire Meighty

1. Collega il FM-1 con un cavo USB dati. Apri **https://gfcalvi.github.io/meighty-fm1/** in Chrome su Mac/PC oppure in MIDIWeb Browser su iPhone/iPad USB-C. Il browser gestisce installazione e progetti; il suono viene prodotto dal FM-1.

2. Nella scheda Firmware scegli **Installa Meighty 1.02**, collega la porta quando richiesto e conferma. Mantieni alimentazione e cavo durante la scrittura. Dopo il riavvio apri Global per verificare la versione.

3. Per usare i tools in mobilità, mentre sei online apri la stessa pagina HTTPS in MIDIWeb Browser e scegli **Make Available Offline**. Prova poi la pagina senza rete, con il FM-1 collegato: il Mac non serve. L’archivio iOS non richiede launcher o file .command; il punto di accesso iniziale è la pagina HTTPS.

4. Per iniziare un brano scegli in Global uno slot libero e usa Load slot. Si apre un progetto vuoto, pronto per scrivere. Per sostituire un brano usa Clear slot con conferma. Salva il lavoro con Save slot; non serve inizializzare lo slot.


Tasto | Pagina o azione

FX | Song

SEL o SCL | Chain

ENV | Phrase

LFO o Instrument | Instrument; ripremi per cambiare sottopagina

EDIT | Table

HOME | Mixer con otto indicatori a LED

SEQ | Master FX

GLO | Global

PLAY | Avvio e Stop

SAVE | Salva nello slot progetto attivo

ARP | Catalogo preset in Instrument

REC | Azione contestuale della pagina

SELECT sceglie la traccia; ALGORITHM scorre le righe. Entrando in Chain da Song si apre la Chain assegnata alla traccia e alla riga selezionate. SELECT in Chain apre la Chain della nuova traccia; il numero C00–C1F è indicato in alto, C-- indica assenza di assegnazione. K3 permette sempre la scelta manuale dal pool. Nella pagina Phrase, SELECT apre anche la Phrase della nuova traccia: durante PLAY segue la posizione in esecuzione; da fermo usa la riga Song scelta e la posizione Chain scelta (la prima se arrivi direttamente da Song). Una posizione senza assegnazione mostra P-- / NO PHRASE e non modifica la Phrase precedente. K3 permette ancora di scegliere esplicitamente una Phrase dal pool, anche non assegnata. Le Phrase sono condivise: due tracce che richiamano lo stesso ID modificano lo stesso oggetto. K1–K4 sono i quattro rotativi: la legenda in basso indica la funzione nella pagina. PRESETS cambia vista e non carica un suono da solo.


## Scegliere un suono nello slot I00

1. Premi LFO per Instrument. Con K3 seleziona I00.

2. Ruota K4 per aprire e scorrere il catalogo. Scegli un preset semplice, poi premi REC: il preset viene caricato dentro I00.

3. Suona la tastiera per ascoltarlo. Il numero I00 è la destinazione del suono; il nome nel catalogo è il preset da copiare lì.

4. Per la prima prova lascia TABLE su FF e le profondità LFO neutre. Preferisci un pluck o un basso con attacco riconoscibile.


## Scrivere e collegare una battuta

1. Apri Phrase con ENV e scegli Phrase 00 con K3. K1 seleziona NTE, IN o uno dei due FX; K2 modifica quel campo. ALGORITHM sceglie la riga.

2. Scrivi gli eventi sotto. Le altre righe restano vuote. In Phrase la tastiera inserisce anche la nota sulla riga selezionata: per cambiare solo un valore usa K2.

3. Apri Chain 00: prima posizione Phrase 00, LENGTH 1. Apri Song: sulla riga 00 metti Chain 00 in T1, le altre celle vuote, Song LENGTH 1.

4. Premi PLAY e ascolta. Apri HOME e regola il livello di T1; scegli uno slot in Global e premi SAVE.

```
PHRASE 00
ROW NTE IN FX1    FX2
00  C-3 00 --- 00 --- 00
04  G-3 00 --- 00 --- 00
08  C-4 00 --- 00 --- 00
0C  G-3 00 --- 00 --- 00

CHAIN 00  00=Phrase 00  LENGTH 1
SONG 00   T1=Chain 00   LENGTH 1
```

Ora aggiungi CUT 40 sulla 00 e CUT C0 sulla 08. Confronta i due attacchi prima di aggiungere altri FX. Se non senti la battuta, verifica prima i tre collegamenti e solo dopo il suono.


# 2 Organizzare Phrase Chain e Song

Oggetto | Contenuto | Capacità

Instrument | Suono richiamato dalla colonna IN | 32 slot, 00–1F

Phrase | 16 righe di nota, strumento e due FX | 64 oggetti, 00–3F

Chain | Ordine delle Phrase | 32 oggetti, 00–1F; fino a 16 posizioni

Song | Una Chain per traccia e per sezione | 8 tracce, fino a 32 righe

Table | Programma associato a una voce | 16 oggetti, 00–0F; 16 righe

Progetto | Tutti questi oggetti, suoni e basi del mix | 8 slot interni

La Song non contiene le note: contiene numeri di Chain. La Chain non copia le Phrase: le richiama per ID. Se due parti usano Phrase 00, modificare Phrase 00 cambia entrambe. Per una variazione indipendente prepara Phrase 01 e cambia il riferimento della Chain desiderata.


## Dalla ripetizione alla variazione

```
CHAIN 00
POS PHRASE
00  00
01  00
02  00
03  01
LENGTH 4
```

Con Phrase 01 diversa nel finale, tre battute restano regolari e la quarta chiude con una variazione. Lo stesso principio permette di costruire sezioni con poche Phrase. Per creare una variazione indipendente copia tutte le righe con ARP come SHIFT, poi incollale in una Phrase libera: il procedimento è spiegato nel capitolo 3.


## Durate e indipendenza delle tracce

Una riga Phrase dura sei tick; sedici righe fanno una battuta di 4/4. Una Chain di quattro Phrase complete dura quattro battute. HOP e JMP possono accorciare o bloccare il percorso di una traccia: le altre continuano indipendentemente. Per sezioni che devono cambiare insieme, mantieni uguali le durate effettive delle Chain.

Una cella Song vuota spegne la voce e occupa il passaggio di una Phrase, non la durata di una Chain lunga delle altre tracce. Per un silenzio di quattro battute prepara una Chain lunga quattro: prima una Phrase con OFF, poi tre Phrase valide vuote. Per tenere un pad, usa Phrase valide vuote senza OFF. Questa distinzione evita sfasamenti nell’arrangiamento.


## Mute e solo durante il lavoro

In Song SELECT o K1 sceglie la traccia; OCT− commuta mute e OCT+ solo. Puoi mettere in solo più tracce. Mute prevale sul solo; le tracce escluse continuano ad avanzare. Il colore attenuato indica l’esclusione senza aggiungere etichette nel reticolo.


## Partire da una riga e saltare durante la performance

1. Premi FX per aprire Song. Da fermo, usa ALGORITHM per scegliere la riga dell’arrangiamento. Premi PLAY: tutte le otto tracce partono da quella riga, dalla prima posizione della propria Chain e dalla prima riga della Phrase.

2. Durante la riproduzione scorri fino alla riga desiderata con ALGORITHM. Il cursore di modifica non sposta da solo il trasporto. Premi REC: compare JUMP con la destinazione; tutte le tracce saltano insieme al successivo confine di riga Phrase, ogni sei tick.

3. Per sostituire una destinazione in attesa, scegli un’altra riga valida e premi REC di nuovo. STOP annulla il salto in attesa. PLAY durante l’esecuzione resta Stop; REC da fermo in Song non avvia la riproduzione.

La riga scelta deve rientrare in Song LENGTH: con LENGTH 08 sono valide le righe 00–07. OUTSIDE LEN segnala una selezione fuori lunghezza; PLAY non parte e REC non programma un nuovo salto. Allunga LENGTH con K3 se vuoi includere quella sezione. Le Chain vuote di una riga valida sono invece consentite e producono silenzio sulle rispettive tracce.

Esempio: con LENGTH 08, seleziona la riga 04 e premi PLAY per provare la seconda metà. Mentre suona, seleziona 02 e premi REC: il salto avviene entro una riga Phrase (a 120 BPM, al massimo circa 125 ms), senza cambiare il clock o tagliare le code di delay e riverbero. Non aspetta la fine della Chain o della battuta. Quando raggiunge il termine della Song, il ciclo torna alla riga 00.

L’avvio e il salto non simulano le sezioni precedenti: note di pad e comandi che si trovano soltanto prima della destinazione non vengono ricostruiti. Metti i trigger e le automazioni necessari all’inizio di una sezione che vuoi poter lanciare autonomamente. Il salto reinizializza le voci e i loro contatori, conservando i ritorni FX e le impostazioni operative del mixer; un nuovo PLAY da fermo azzera invece le code come prima. PLAY dalle altre pagine parte da 00: per scegliere la partenza usa Song.

Durante PLAY, Song scorre con la traccia selezionata; Phrase segue anche i cambi di Phrase nella Chain. FOLLOW o FOL indica l’inseguimento. Scorrere manualmente, modificare valori o scegliere un’altra Phrase ferma l’inseguimento e mostra EDIT. Per riprenderlo premi nuovamente FX in Song oppure ENV in Phrase. Un nuovo avvio con PLAY riattiva l’inseguimento.


# 3 Leggere e scrivere note e FX

Nelle ricette ROW indica dove scrivere; non è un parametro. NTE è la nota, IN lo slot Instrument. Dopo ogni sigla FX compare il suo byte valore. Una riga omessa lascia NTE --- e IN FF, con FX vuoti. I blocchi sono trascrizioni per l’editor, non comandi di una console.

```
ROW NTE IN FX1    FX2
00  C-4 00 CUT 40 PAN 20
04  --- FF CUT C0 --- 00
08  OFF FF --- 00 --- 00
```

La 00 avvia Do4 con I00, filtro 40 e pan 20. La 04 cambia il filtro senza un nuovo attacco. La 08 rilascia la voce. --- nella nota mantiene ciò che sta suonando; OFF avvia la Release e ferma Table/retrigger; KIL interrompe senza Release. La nuova nota di una traccia monofonica sostituisce la sua voce precedente.


## Esadecimale signed e due cifre indipendenti

Scrittura | Lettura corretta

10, 20, 40, 80, FF | 16, 32, 64, 128, 255 decimali

PIT 07 e PIT F9 | +7 e -7 semitoni; PIT accumula

REP F8 | Incremento -8, non 248

ARP 37 | +3 e +7 semitoni, due campi distinti

CHA 8F | 8/15 a sinistra e sempre a destra nella Phrase

Depth +16 o -16 | Decimale con segno nell’editor; 80 è lo zero memorizzato

TPO 78 | 120 BPM; Global mostra invece BPM decimali

FAL 00 e OR2 03 | Algoritmo 1 e rapporto 3; sono indici con liste diverse

Se una prova del riferimento usa IN 07 mentre la preparazione indica I00, prepara lo stesso suono anche nello slot 07 oppure cambia la colonna IN per usare I00. TABLE FF significa nessuna Table automatica; in lettura la schermata può mostrare --. Un valore FF dentro un FX non significa automaticamente vuoto: dipende dalla sigla.


## Cancellare, selezionare, copiare e annullare

In Song, Chain, Phrase e Table tieni premuto **ARP come SHIFT**. In Instrument ARP apre invece il catalogo preset.

Combinazione | Risultato
--- | ---
ARP + ALGORITHM | Estende la selezione sulle righe
ARP + K1 | Estende la selezione sulle colonne; in Song sceglie le tracce
ARP + K2 a destra | Seleziona righe intere
ARP + K2 a sinistra | Torna alla selezione per celle
ARP + OCT- | Cancella la cella o l’area selezionata
ARP + OCT+ | Copia la cella o l’area selezionata
ARP + REC | Incolla alla posizione scelta
ARP + HOME | Annulla l’ultima cancellazione o incolla nello stesso oggetto

Senza selezione il comando riguarda la cella corrente. Se scegli la sigla di un FX, copia e cancellazione comprendono anche il suo valore; scegliendo solo il parametro agisci su quel valore. Cancellare una nota toglie l’evento dalla Phrase, non invia una Release alla voce che sta già suonando: per questo servono OFF o KIL.

Esempio: duplicare Phrase 00 in Phrase 04. Vai alla riga 00 di Phrase 00; tieni ARP, ruota K2 a destra e ALGORITHM fino a 0F, poi premi OCT+ continuando a tenere ARP. Rilascia ARP, scegli Phrase 04 con K3 e la riga 00, quindi ARP + REC. Ora puoi cambiare il finale senza modificare Phrase 00.

Puoi incollare soltanto fra oggetti dello stesso tipo di pagina, con campi compatibili e spazio sufficiente. Un blocco di sedici righe va incollato dalla riga 00: non si avvolge al termine della Phrase. Il messaggio segnala un bordo o un tipo di campo incompatibile; non viene incollato mezzo blocco.

L’annullamento ha un solo livello e riguarda cancellazione o incolla, nello stesso oggetto. Le modifiche diventano permanenti nello slot soltanto con Save. La selezione sospende il FOLLOW visivo; premi nuovamente il tasto Song o Phrase per riprendere l’inseguimento del cursore in esecuzione.

## Tempo di una riga

Il clock usa 24 tick per quarto. A 120 BPM: tick 20,83 ms, riga 125 ms, Phrase completa 2 secondi. DEL, RET, ARC e TIC usano tick, ma controllano cose diverse. DEL ritarda la riga, RET riattacca la voce, ARC scandisce l’arpeggio, TIC scandisce la Table. Il delay audio appartiene invece agli effetti master.


## Ordine di esecuzione e combinazioni

1. La Phrase individua DEL prima di applicare la riga; valori 01–05 la rinviano, da 06 in su la saltano.

2. Quando la riga è eseguita, SED prepara il generatore e i gate stabiliscono quali eventi possono passare.

3. RNL modifica copie di nota, strumento o valore alla sua sinistra. La scala quantizza l’altezza eseguita.

4. La nuova nota carica il suono; gli FX operativi applicati dopo possono sostituire le sue basi. Le colonne vengono elaborate da sinistra a destra.

5. La Table attiva lavora dopo la Phrase nello stesso tick. Può quindi riscrivere cutoff, volume, pitch o mixer. Poi LFO e inviluppi contribuiscono al suono.

Ogni colonna ricorda il proprio ultimo FX operativo. REP, RND e RTO usano quella memoria, anche sulle righe senza nota. Le due colonne Phrase e le tre Table hanno memorie separate. RNL, invece, guarda immediatamente a sinistra sulla stessa riga. Il laboratorio E02–E04 rende udibili queste differenze.


# 4 Scegliere e costruire i suoni

I 177 preset del catalogo si caricano nei 32 slot Instrument. K3 sceglie lo slot; K4 apre e scorre il catalogo, K2 salta fra famiglie, REC conferma. Caricare un preset in I00 sostituisce I00: tutte le Phrase con IN 00 useranno il nuovo suono. Cambiare soltanto lo slot visualizzato non cambia gli IN scritti nelle Phrase.


## Sorgente famiglia e modello

Sorgente o famiglia | Modelli | Controlli caratteristici

SAMPLE | 33 colpi CR78 e MiniPops45 | Sample, livello, filtro e inviluppi

BASIC | SAW, PULSE, SINE, CHIP, NOISE | Pulse width su PULSE; timbri essenziali

BRAIDS | FM, FEEDBACK FM, VOSIM, CSAW, MORPH | Timbre e Color secondo il modello

BRAIDS analogici | SAW SQUARE, SAW SUB, SAW SYNC | Miscele, sub e sincronizzazione

BRAIDS percussivi | KICK, SNARE, CYMBAL | Timbre e Color sulle percussioni

FM4 | Quattro operatori e otto algoritmi | Index, feedback, ratio e inviluppo per operatore

DUAL WT | Due oscillatori wavetable | Pos1/Pos2, banchi, intervallo, detune, mix e sync

SOURCE sceglie SYNTH o SAMPLE per lo slot, indipendentemente dalla traccia. ENGINE raggruppa la famiglia; MODEL sceglie il modello. MDL nelle Phrase cambia il modello operativo, ma non trasforma una sorgente SAMPLE in SYNTH. I nomi Braids si riferiscono agli adattamenti presenti; non è incluso l’intero firmware Mutable Instruments né un motore Plaits completo.


## Le pagine Instrument

Il riquadro grande in alto a destra indica lo slot I00–I1F su tutte le pagine Instrument. Premi ripetutamente LFO/Instrument per Suono, Modulazioni e Motore. REC conferma il preset. K1 sceglie il campo, K2 il valore, K3 lo slot. Il parametro selezionato è riportato sopra la legenda.


## FM4 partendo da due operatori

Nell’algoritmo 1, OP4 modula OP3, che modula OP2, che modula OP1. Per una prima prova lascia OP3 e OP4 a livello zero: OP1 è la portante, OP2 il modulatore. Ratio 1 per OP1, Ratio 2 per OP2; apri il livello OP2 e poi Index. Con Index zero o modulatore spento non senti il cambiamento FM.

Algoritmo visualizzato | Percorso

1 | 4 > 3 > 2 > 1

2 | 3 e 4 > 2 > 1

3 | 3 > 2; 2 e 4 > 1

4 | 4 > 3; 2 e 3 > 1

5 | 2 > 1 più 4 > 3

6 | 4 > 1, 2 e 3

7 | 1 più 2 più 4 > 3

8 | Quattro portanti indipendenti

Le pagine Motore distinguono ratio, livello e ADSR di ogni operatore. Il loro ruolo dipende dall’algoritmo. L’ADSR comune del suono resta un ulteriore inviluppo di ampiezza; quello del filtro è ancora separato. OR1–OR4 cambiano i ratio durante la riproduzione; FAL cambia algoritmo. Vedi E11 e H15–H17.


## Che cosa contiene il dual wavetable

Banco | Percorso della scansione

CLASSIC | Sine, triangolare, saw, square, tre pulse e due spettri combinati

HOLLOW | Nove combinazioni di parziali e registri, anche pari

GLASS | Gruppi di armoniche che salgono nello spettro

FORMANT | Due picchi spettrali mobili con fondamentale stabile

Ogni banco contiene nove forme originali a ciclo singolo e sei livelli per limitare le armoniche alle note alte. Le posizioni interpolano fra le forme; non scelgono un campione audio lungo. OSC1 e OSC2 scelgono il banco separatamente. MIX 00 lascia solo OSC1, FF solo OSC2. SEMI 0 è l’unisono; DETUNE 80 è neutro nella memoria e appare con segno nell’editor. SYNC riavvia OSC2 al ciclo di OSC1.

Le forme visualizzate nella prima pagina mostrano le posizioni base. Il movimento degli LFO e degli FX si ascolta, ma non è rappresentato da una scansione animata completa. WTP/WT2 controllano le posizioni; OSM il mix, DTN il detune e SYN la sincronizzazione. E12 separa gradini e modulazione continua.


## Campioni e articolazioni

La sorgente SAMPLE usa lo stesso filtro, ADSR e LFO dei synth, ma una Release non può allungare il file finito. STA e LEN scelgono la regione del trigger; non fanno scrubbing continuo e non aggiungono un loop. Una traccia monofonica può alternare più strumenti sample cambiando IN a ogni nota. Sulla traccia scelta per la polifonia puoi sovrapporre fino a tre trigger dello stesso Instrument con CHD 00. Per un kit con più timbri sovrapposti organizza i colpi su tracce diverse. Il catalogo completo è nel capitolo 14.


## Tre voci su una traccia

Apri Global e scegli **Poly 3 track = T1 ... T8** con K2. La scelta assegna tre voci vere a quella traccia e viene salvata nel progetto. Le altre sette tracce restano monofoniche. OFF nel campo Global disabilita la polifonia; non è il comando musicale OFF della Phrase.

La traccia scelta mostra **3V**; Instrument indica anche il contesto della traccia accanto al numero Ixx. Seleziona la traccia polifonica prima di aprire Instrument, scegli un suono e premi tre tasti: le note suonano insieme e ogni rilascio della tastiera interessa il proprio tasto. Alla quarta nota viene riutilizzata una voce libera oppure sostituita la più vecchia.

Ogni voce ha il proprio stato di oscillatori, campione, filtro, inviluppi, LFO e Table. Mixer, pan, mute/solo e mandate sono condivisi dalla traccia. Tre stati separati non implicano uno sfasamento automatico: con le stesse impostazioni le modulazioni possono partire allineate.

Per una parte di accordi usa un unico Instrument sulla traccia polifonica. Se devi cambiare IN mentre rimangono note tenute o code di Release, interrompi prima il gruppo con KIL 00 oppure attendi che le voci siano terminate. Per strati con timbri indipendenti usa tracce distinte.

### Un pad maggiore che occupa solo T4

1. In Global scegli T4 come Poly 3 track; per questa prova imposta Scale su CHROMATIC e Root C.
2. In I00 carica un pad DUAL WT. Imposta AMP ON, Attack 40, Decay 40, Sustain C0, Release 80, filtro non troppo aperto e TABLE FF.
3. Collega la Phrase a una Chain e alla cella Song di T4. Scrivi queste righe; lascia vuote quelle non riportate.

```
ROW NTE IN FX1    FX2
00  C-4 00 CHD 47 DSN 80
08  F-4 00 --- 00 RSN 90
0C  OFF FF --- 00 --- 00
```

Sulla 00 suonano Do, Mi e Sol. CHD resta attivo: sulla 08 suonano Fa, La e Do, anche se il comando non viene riscritto. OFF sulla 0C rilascia il gruppo. Le mandate appartengono alla traccia; il Master FX deve avere i rispettivi ritorni aperti.

Il massimo rimane tre voci: un nuovo accordo non aggiunge altre tre code al precedente. Le voci vengono riutilizzate e una nota ancora in Release può essere sostituita. Per ascoltare tutta la coda inserisci OFF e lascia tempo prima del trigger seguente.

### Sovrapporre tre note senza scrivere un accordo fisso

```
ROW NTE IN FX1    FX2
00  C-4 00 CHD 00 --- 00
04  E-4 00 --- 00 --- 00
08  G-4 00 --- 00 --- 00
0C  OFF FF --- 00 --- 00
```

Con Sustain alto Do continua quando entra Mi, poi si aggiunge Sol. CHD 00 sceglie la sovrapposizione indipendente, non spegne le voci già attive. OFF sulla 0C rilascia tutte le note della traccia; dalla tastiera i rilasci restano invece individuali. Lo stesso principio sovrappone tre trigger dello stesso sample finché il materiale PCM non termina.

### Accordare, modulare e registrare

CHD 47 usa +4 e +7 semitoni; CHD 37 usa +3 e +7; CHD 57 usa +5 e +7. CHD 40 lascia fondamentale e terza; CHD 07 lascia fondamentale e quinta. Uno zero disabilita quella voce aggiuntiva e non duplica la fondamentale.

La scala quantizza separatamente tutte le note. CHROMATIC conserva gli intervalli esatti; con un’altra scala un intervallo non ammesso viene abbassato al grado consentito. SCA e SCG possono cambiare il contesto locale come sulle tracce monofoniche.

In Phrase la tastiera può registrare fino a tre note come fondamentale più CHD in **FX1**, sostituendo il contenuto precedente di FX1. Il formato registra intervalli entro 15 semitoni dalla nota più bassa; voicing più larghi restano suonabili live ma non entrano in questa codifica compatta.

VOL agisce sulla voce corrente; quando un trigger CHD crea l’accordo il suo valore viene copiato nelle voci aggiunte. LEV controlla sempre il gruppo dal mixer. CUT, parametri di motore e vari comandi Phrase vengono applicati anche alle voci già attive; una Table lavora invece sullo stato della propria voce. LEV, PAN, DSN e RSN restano condivisi anche quando li scrive una Table.

Scegli la traccia polifonica prima di avviare la parte. Cambiare Poly 3 track durante PLAY azzera le due voci aggiuntive e la modalità CHD corrente; per riattivare un accordo riesegui una riga con CHD. Non è un controllo di trasposizione dal vivo.

# 5 Inviluppi filtro e LFO

Per una nota sostenuta attiva AMP, porta Sustain sopra zero e scegli Attack e Release adatti. Attack, Decay e Release non sono millisecondi: il byte controlla una curva quadratica. Indicativamente 40 corrisponde a circa 0,51 s, 80 a circa 2,05 s, C0 a circa 4,61 s. L’inviluppo non disegna una nota se il campione termina prima.

Fase | Che cosa cambia | Prova di ascolto

Attack | Tempo per raggiungere il picco | 00 per un pluck; 90 per un ingresso lento

Decay | Tempo dal picco al Sustain | Confronta 20 e 60 lasciando Sustain basso

Sustain | Livello tenuto finché la nota resta attiva | 00 decade; C0 resta sostenuto

Release | Discesa dopo OFF | Confronta 20 e 80 su una nota OFF

Una nuova nota riavvia gli inviluppi. Per un pad su più battute non riscrivere la nota a ogni inizio Phrase: continua con Phrase valide vuote. Una cella Song vuota interrompe invece la voce. Per un accordo lento usa più tracce oppure una struttura di sintesi che generi gli intervalli desiderati.


## Filtro e secondo inviluppo

Cutoff è una base 00–FF, non una frequenza in Hz. Resonance enfatizza la zona del filtro; i tipi sono Legacy, LP, BP e HP. CUT ENV ha ADSR e Depth separati: profondità positiva apre, negativa chiude rispetto alla base. Per imparare ascolta prima un CUT fisso con LFO e inviluppo filtro neutri; aggiungi poi il contorno.


## Assegnare due LFO

Ogni LFO offre rate, forma e fase; le destinazioni pan, pitch, cutoff e ampiezza hanno profondità indipendenti. Nel dual wavetable si aggiungono POS1 e POS2 per entrambi gli LFO. Le profondità mostrate con + o − sono decimali: zero è neutro. La fase 80 è opposta a 00.

Gli LFO sono liberi, non seguono le divisioni del delay. RATE 20 è circa 0,34 Hz; RATE 40 circa 1,30 Hz. Una nuova nota riavvia la fase configurata. Per controfase usa due LFO allo stesso rate con fasi 00 e 80, assegnati a destinazioni diverse. Sulla stessa destinazione, profondità uguali e fasi opposte possono annullarsi.

Esempio: DUAL WT con POS1/POS2 80 e MIX 80. LFO1 SIN RATE 20, POS1 +32; LFO2 SIN RATE 20 PHASE 80, POS2 +32. Le due onde si muovono in verso opposto. Prova H12 ed E12 prima di aggiungere cutoff e pan.


# 6 Mixer indicatori ed effetti master

Il Mixer mostra otto fader e otto barre a dieci LED. SELECT sceglie la traccia; K1 livello, K2 pan, K3 mandata delay, K4 mandata riverbero. Il valore esadecimale sotto il fader è il suo livello, non il livello misurato. I LED si muovono con il segnale audio.


## Come leggere i LED

Gli indicatori rilevano il picco del segnale della singola traccia dopo il livello e prima di pan, master e ritorni FX. I colpi brevi restano visibili per circa 64 ms, poi il livello scende gradualmente. Verde indica i livelli ordinari, giallo la zona alta e rosso i picchi vicini al fondo scala della corsia. Sono indicatori di picco, non VU analogici calibrati né una misura del loudness complessivo.

La scala dei dieci segmenti va circa da −42 a −1 dB rispetto al riferimento interno della corsia. Un segmento rosso non certifica clipping all’uscita master. Una mandata può avere ancora una coda udibile mentre il meter della traccia è sceso; il ritorno non attraversa quell’indicatore. Mute/solo attenuano il segnale e il meter scende con la sua breve inerzia. Stop lo azzera.


## Separare suono diretto mandata e ritorno

Il segnale passa da voce a livello e pan di traccia, quindi alimenta dry e mandate; delay e riverbero tornano al master. Per sentire un effetto devono essere aperti sia send sia return. VOL regola la voce; LEV il fader operativo della traccia. Entrambi influenzano quanto segnale arriva agli effetti.

Controllo | Azione

Delay time | Divisione sincronizzata al BPM

Feedback | Ripetizioni, massimo F0

Ping pong | Alternanza stereo

Delay return | Livello del ritorno delay

Reverb type | ROOM o AMBIENT più diffuso

Reverb decay | Durata, massimo E0

Reverb damp | Smorzamento delle alte frequenze

Reverb return | Livello del ritorno riverbero

Master level | Livello complessivo del progetto

D significa puntato, tempo moltiplicato per 1,5; T indica terzina, tempo moltiplicato per 2/3. A 120 BPM 1/8 dura 250 ms, 1/8D 375 ms e 1/8T circa 166,7 ms. Le divisioni vanno da 1/2 a 1/64 e seguono anche le variazioni TPO.


## Una partenza per sequenze e pad

Imposta delay 1/8D, feedback A0, ping-pong ON e return C0. Sul sequencer parti da DSN A0, poi lascia alcune pause. Per il pad scegli AMBIENT, decay D0, damp 90 e reverb return C0; prova RSN B0. Regola i livelli ascoltando insieme suono diretto e coda. Un effetto molto alto può confondere gli attacchi e nascondere l’evoluzione delle note.

DSN e RSN nelle Phrase creano override delle mandate: chiudere DSN ferma l’ingresso, non gli echi già nel buffer. I controlli manuali del mixer riprendono il parametro; Stop/Play ripristina le basi, e Stop azzera i buffer FX. E10 mostra un delay throw; H21 combina throw e coda ambient.


# 7 Global armonia e colori

GLO riunisce BPM, scala, tonica, Slot, Load slot, Save slot, Clear slot, Master FX e palette. K1 seleziona il campo, K2 il valore. REC esegue Load o Save. Clear slot richiede una seconda pressione di conferma. Un passo di K3 carica lo slot selezionato e un passo di K4 lo salva: non sono controlli di scorrimento innocui.

Parametro | Valori o uso

BPM | 30–300 decimali; TPO arriva fino a FF cioè 255

Scale | CHROMATIC, MAJ/IONIAN, DORIAN, PHRYGIAN, LYDIAN, MIXOLYDIAN, MIN/AEOLIAN, LOCRIAN, MIN PENT, MAJ PENT

Root | Tonica da C a B

Project slot | Destinazione 1–8 per Save e Load

Poly 3 track | OFF oppure T1–T8; tre voci sulla traccia scelta

Theme | NEON BLUE, SOFT BLUE, AURORA, AMBER

Title Selection Values FX colour | AUTO oppure uno dei 15 colori disponibili

La scala non trascrive le note in memoria: quantizza in esecuzione verso il grado ammesso inferiore. La tonica definisce i gradi, non è una trasposizione generale. SCA/SCG locali per maggiore o minore possono prevalere su Global; SCA 00 torna a seguirla. Per un pool esatto di altezze scegli una Table come in E13.


## Personalizzare la palette

NEON BLUE mantiene fondo blu, titoli e FX magenta, selezione verde acido, valori gialli e testo bianco. I quattro ruoli possono essere cambiati separatamente. AUTO richiama il default del ruolo; una combinazione diversa dai temi appare come CUSTOM. Scegliere un tema ripristina tutti e quattro i ruoli.

I colori sono nel progetto: SAVE li registra nello slot e il backup .meighty li conserva nel progetto. Caricare un altro progetto richiama la sua palette. I LED del meter mantengono verde, giallo e rosso per rendere leggibile il livello indipendentemente dal colore di selezione.


# 8 Progetti e otto slot

Gli otto slot sono sempre disponibili. Non esiste un’operazione Init da eseguire prima dell’uso. Il display del firmware indica **S1–S8**, cioè lo slot effettivamente aperto. **S--** indica un progetto temporaneo non associato a uno slot. Cambiare la destinazione in Global non cambia questa indicazione.

Operazione | Risultato
--- | ---
Load slot | Apre il brano scelto. Se il posto è vuoto, apre un progetto nuovo e vuoto.
Save slot | Salva il progetto aperto nella destinazione scelta e lo associa a quello slot.
Clear slot | Riporta lo slot a un progetto vuoto persistente, con conferma. Non occorre un Save successivo.

Salva con PLAY fermo: le scritture sulla memoria flash possono sospendere l’audio. Le modifiche ai parametri e la navigazione si possono invece usare durante PLAY.

Il tasto fisico SAVE salva nello slot attualmente aperto. Per salvare una copia in un altro slot, scegli la destinazione in Global e usa Save slot. K3 richiama Load, K4 Save. Clear slot si conferma con un secondo REC entro sette secondi; una modifica ai controlli annulla la conferma.

Clear su uno slot diverso da quello aperto non cambia il progetto in lavorazione. Clear sullo slot aperto aggiorna anche il display con il progetto vuoto. All’avvio viene aperto lo slot 1; non viene ricordato automaticamente l’ultimo slot. Le modifiche musicali restano in RAM fino a Save.

## Un nuovo progetto nello slot 2

Scegli 2 in Global e usa Load slot. Se è vuoto, puoi iniziare subito a lavorare e poi usare Save. Per azzerare un vecchio brano usa Clear slot con conferma. Non servono Init, New project o una sequenza di preparazione.

## I quattro tools offline

Le quattro schede sono **Firmware**, **Backup ed estrazione**, **Conversione**, **Ripristino / Caricamento**.

Firmware installa Meighty 1.02 con una conferma. Se è già installato, usa direttamente gli altri tools: il caricamento di un brano non reinstalla il firmware. L’intera suite funziona senza rete dopo Make Available Offline in MIDIWeb Browser.

Backup ed estrazione: Scarica backup conserva gli otto slot e il progetto in lavorazione. Scarica progetto aperto esporta solo la RAM. Puoi anche aprire un backup esistente e usare Estrai su uno degli otto slot oppure Estrai tutti i brani; lo ZIP contiene un indice anche delle posizioni vuote e la copia in lavorazione, se presente. Nessun backup è obbligatorio prima di un altro comando.

Conversione: scegli un file nella sua casella, il formato di uscita e Converti e scarica. È indipendente dai file aperti nelle altre schede. Per i formati che non contengono la copia RAM, quest’ultima è conservata separatamente nello ZIP.

Ripristino / Caricamento usa una sola griglia di otto destinazioni. Apri un backup o un set per riempirla nelle posizioni originali; per un singolo brano puoi scegliere il file direttamente nella casella desiderata. Nei menu puoi anche scegliere i brani estratti da altri backup, inclusa la copia in lavorazione. Premi **Carica gli slot selezionati**: vengono scritti e verificati solo quelli compilati, poi si apre il primo trasferito. Non serve un Load successivo. Sul firmware compare il suo S1–S8.

**Non modificare significa bypass, non cancellazione.** Se scegli un brano soltanto nella casella 2, viene sostituito solo lo slot 2 dell’FM-1; gli altri sette restano invariati. Con brani nelle caselle 2 e 7 vengono scritti solo 2 e 7. Un backup con tre brani aggiorna solo quelle tre posizioni. Una selezione completamente vuota non scrive nulla e segnala di scegliere almeno un brano. Azzera la selezione agisce soltanto sulla griglia locale, mai sullo strumento. Per cancellare uno slot usa Clear slot sul firmware.

Salva set su file conserva le destinazioni scelte, anche con meno di otto brani. Quando ricarichi quel file, le posizioni senza brano continuano a essere ignorate. Un progetto vuoto scelto esplicitamente come file è invece un contenuto e può sostituire lo slot scelto. Non ci sono Load/Save/Clear nei tools, modalità sostituisci tutti, inizializzazioni o sequenze di preparazione.

La pagina mostra un solo esito corrente; la cronologia è chiusa nei Dettagli tecnici. Dopo la generazione tenta il download e mantiene Salva il file / Condividi come alternativa su iOS. In MIDIWeb Browser apri la pagina HTTPS aggiornata e rinnova Make Available Offline. La pagina contiene codice e firmware senza iframe né servizi remoti necessari al funzionamento offline.

## Formati e ambienti

.meighty conserva una banca e l’eventuale copia in lavorazione; può contenere uno, più brani o tutti gli otto slot. .fm1tracker.json contiene un singolo progetto. .rfm1state e .fm1save sono formati di ambienti di emulazione; .fwsc è il firmware. Non usare un firmware come file brano.

I tools importano i formati compatibili e verificano integrità e struttura. Un progetto polifonico richiede la traccia selezionata e i comandi CHD: la conversione non li elimina per forzare un formato incompatibile. Per conservare tutto il lavoro del FM-1 scegli .meighty. Un progetto salvato non comprende il punto esatto del generatore casuale o le code audio in corso: per una sequenza ripetibile programma SED e gli eventi nella Phrase.

Per lavorare su iPhone senza Mac apri la pagina HTTPS in MIDIWeb Browser e usa Make Available Offline. Il contenuto dei file e le conversioni restano nel browser; per trasferire dati basta il collegamento USB al FM-1. Il pacchetto iOS non contiene .command, .cmd o launcher Python.

Gli esempi Oltre le dune e Orbite profonde hanno rispettivamente 98 e 82 BPM. Sono verificati dal client JavaScript verso dispatcher C e NOR simulata su tutti otto gli slot, anche con dati preesistenti. Questo non sostituisce il collaudo USB fisico.

# 9 Usare le Table come piccoli programmi

Una Table modifica una voce che esiste già. Non è una nona traccia e non è un’altra Phrase. Sulla traccia polifonica ogni voce mantiene il proprio stato Table; CHD si programma nella Phrase e non crea accordi da una Table. Le sue righe contengono PIT relativo, VL assoluto e tre FX. Puoi assegnarla nell’Instrument o avviarla con TBL sulla voce di una traccia.

```
TABLE 00
ROW PIT VL FX1    FX2    FX3
00  +00 C0 TIC 03 CUT 40 PAN 30
01  +04 C0 --- 00 CUT 80 PAN 80
02  +07 C0 --- 00 CUT C0 PAN D0
03  +12 C0 HOP 00 --- 00 --- 00

PHRASE
00 C-4 00 TBL 00 --- 00
0E OFF FF --- 00 --- 00
```

La nota Do4 riceve in sequenza trasposizioni 0, +4, +7 e +12, con filtro e pan diversi. TIC 03 tiene ogni riga per tre tick; HOP 00 torna a 00 senza limite. Il tempo della Phrase resta invariato. Per provare solo il filtro, metti PIT 0 in tutte le righe; per provare solo il pitch lascia CUT e PAN vuoti.


## Quattro regole che evitano gli errori comuni

1. Imposta VL intenzionalmente su ogni riga: non è una velocity opzionale. Un valore basso può prevalere su VOL della Phrase.

2. La nuova nota riavvia la Table. Per ascoltarne un percorso lungo, usa una nota sostenuta e righe Phrase vuote.

3. Le tre colonne hanno memorie separate per REP/RND/RTO. La Table viene eseguita dopo gli FX Phrase nello stesso tick.

4. STP ferma la Table lasciando la voce all’ultimo stato. La nota OFF rilascia la voce e ferma anche la Table; KIL la taglia.


## Tempo salti e loop finiti

TIC 06 corrisponde a una riga Table per riga Phrase; TIC 03 ne produce due. TIC 00 congela la lettura finché viene riattivata: non equivale a STP. THO sceglie una riga della Table attiva. HOP ha qui un significato diverso dalla Phrase: il nibble alto conta i ritorni, quello basso è la riga destinazione. HOP 20 fa due ritorni a 00 oltre al primo passaggio; HOP 00 torna senza limite.

```
TABLE 00
00 +00 C0 TIC 03 --- 00 --- 00
01 +07 C0 HOP 20 --- 00 --- 00
02 +12 C0 STP 00 --- 00 --- 00
```

Con una nota tenuta, Do e Sol si alternano tre volte in tutto, poi la voce resta al Do dell’ottava superiore. Non scrivere un altro trigger prima del termine se vuoi sentire il programma completo. H10 mostra i passaggi di questa prova; E09 aggiunge tre automazioni sincronizzate e E13 un pool di note con ingressi casuali.


## Phrase e Table non hanno sempre lo stesso significato

FX | Phrase | Table

HOP | Passa alla Phrase successiva, oppure FF ferma la traccia | Loop contato XY sulla riga Y

CHA | Due lati con probabilità X/15 e Y/15 | Byte XX/255 sul lato sinistro

RNL in prima colonna | Varia nota e Instrument | Varia PIT e VL

DEL | Ritarda o salta la riga | Non implementa quel ritardo

SNG | Salto relativo di riga Song della traccia | Non salta la Song

TBL FF | Nessuna nuova Table selezionata | Non è uno spegnimento: usa STP


# 10 Laboratorio musicale

Scegli una ricetta in base a ciò che vuoi ottenere. Prepara il suono e i collegamenti prima di scrivere gli FX. Le righe non mostrate restano vuote. I codici H conservano un riferimento stabile per ritrovare gli esercizi.


## Ritmo articolazione e variazioni


### H01 Costruire una batteria su quattro tracce

Creare un groove di una battuta separando kick, snare, hat e rim, così da avere mute e send indipendenti.

Preparazione. Global 120 BPM, CHROMATIC. Carica CR78 Kick in I00, CR78 Snare in I01, CR78 ClosedHat in I02 e CR78 Rimshot in I03. Tutte le note PCM sono C4.

1. Prepara Phrase 00–03 e Chain 00–03: ogni Chain contiene soltanto la Phrase con lo stesso ID, LENGTH 1.

2. In Song riga 00 assegna 00 a T1, 01 a T2, 02 a T3, 03 a T4; lascia T5–T8 vuote. Song LENGTH 1.

3. Inserisci gli eventi sotto, uno per riga indicata. Le righe omesse rimangono NTE --- e IN FF.

```
PHRASE 00 kick   00 C-4 00   08 C-4 00
PHRASE 01 snare  04 C-4 01   0C C-4 01
PHRASE 02 hat    00 02 04 06 08 0A 0C 0E
                 su ogni riga C-4 02
PHRASE 03 rim    06 C-4 03   0E C-4 03
```

Da ascoltare. Kick sui movimenti uno e tre, snare sul due e quattro, hat in ottavi e rim in levare. In Mixer riduci T3 a LEV 70 se copre il resto.

Prova successiva. Alterna VOL B0 e VOL 60 sulle righe hat per creare accenti. Da Song usa OCT− per togliere soltanto gli hat.

Se il risultato cambia. Se senti un solo suono, controlla gli IN delle quattro Phrase e i quattro riferimenti Song. Cambiare SELECT non cambia da solo lo strumento scritto nella Phrase.


### H02 Creare una variazione senza modificare il pattern originale

Alternare A e B conservando la prima Phrase.

Preparazione. Parti da H01 o da una sola traccia con Phrase 00 e Chain 00. Gli oggetti sono condivisi per ID.

1. Copia Phrase 00 in Phrase 04: dalla riga 00 tieni ARP, ruota K2 a destra per selezionare righe intere e ALGORITHM fino a 0F, poi OCT+ per copiare. Rilascia ARP, scegli Phrase 04 con K3 e la riga 00; ARP + REC incolla il blocco.

2. Cambia soltanto l’ultima nota di Phrase 04. In Chain 00 scrivi 00 alla posizione 00 e 04 alla 01, LENGTH 2.

3. Lascia la Song collegata a Chain 00. Ora il ciclo alterna le due Phrase.

```
CHAIN 00
POS  PHRASE
00   00
01   04
LENGTH 2

PHRASE 04 modifica di esempio
0E C-4 00 RET 03 --- 00
```

Da ascoltare. Il fill compare soltanto nella seconda battuta. Phrase 00 resta identica ovunque sia richiamata.

Prova successiva. Per quattro battute usa 00,00,00,04 nella Chain. Solo l’ultima è una variazione.

Se il risultato cambia. Se la variazione appare anche altrove, hai modificato un ID condiviso. Assegna un nuovo ID prima di cambiare i dati.


### H03 Distinguere una nota corta da una nota con rilascio

Ascoltare la differenza fra KIL netto e OFF con Release ADSR.

Preparazione. I00 BASIC PULSE, filtro LP aperto. AMP ON A 00 D 20 S C0 R 40, TABLE FF, tutti gli LFO neutri.

1. Crea una sola Phrase collegata a T1. Scrivi i due attacchi e i due modi di spegnimento.

2. Lascia NTE vuota fra gli eventi. Confronta le code senza delay o riverbero.

3. Poi allunga Release a 80 e ripeti: cambia solo il secondo spegnimento.

```
ROW NTE IN FX1    FX2
00  C-3 00 KIL 03 --- 00
08  C-3 00 --- 00 --- 00
0A  OFF FF --- 00 --- 00
```

Da ascoltare. Il primo Do dura tre tick e si interrompe; il secondo entra nella Release sulla 0A. La nuova nota del giro successivo può sostituire la coda.

Prova successiva. Per un basso staccato usa KIL 02 o 03; per un pad usa note OFF e Release più lunga.

Se il risultato cambia. Con Sustain 00 la voce può essere già decaduta prima di OFF. Nei sample la coda non può superare l’audio disponibile.


### H05 Programmare ratchet e shuffle su una percussione

Aggiungere un rullo e ritardi controllati senza cambiare i BPM.

Preparazione. I00 SAMPLE CR78 OpenHat o una snare abbastanza lunga; 120 BPM, TABLE FF.

1. Prima ascolta soltanto i due hat ritardati di un tick con DEL 01.

2. Aggiungi il roll sulla 0C; RET 03 ripete ogni tre tick con una piccola diminuzione di volume.

3. Sulla 0E disattiva RET e chiudi la voce con KIL 00.

```
ROW NTE IN FX1    FX2
00  C-4 00 --- 00 --- 00
02  C-4 00 DEL 01 --- 00
04  C-4 00 --- 00 --- 00
06  C-4 00 DEL 01 --- 00
0C  C-4 00 RET 03 VOL C0
0E  --- FF RET 00 KIL 00
```

Da ascoltare. Gli eventi sulla 02 e 06 sono circa 20,8 ms in ritardo. Il finale ha un rullo a intervalli di 62,5 ms.

Prova successiva. RET 02 rende il roll più fitto; RET 82 lo rende crescente anziché calante.

Se il risultato cambia. Un sample troppo breve termina prima del retrigger. Prova prima un suono SYNTH con sustain per verificare il ritmo.


### H06 Far rispondere un suono quando un altro non suona

Costruire una domanda probabilistica con una risposta condizionata.

Preparazione. I00 CR78 ClosedHat, I01 CR78 Snare; stessa traccia. Le coppie di righe devono essere adiacenti.

1. Metti CHN 80 in FX1 sulla riga della domanda. Questo condiziona nota e strumento, non FX2.

2. Metti PRV 00 sulla riga immediatamente successiva.

3. Ripeti la coppia sulle righe 04–05 e 08–09. Non inserire una riga vuota fra domanda e risposta.

```
ROW NTE IN FX1    FX2
00  C-4 00 CHN 80 --- 00
01  C-4 01 PRV 00 --- 00
04  C-4 00 CHN 80 --- 00
05  C-4 01 PRV 00 --- 00
```

Da ascoltare. Senti l’hat oppure una snare un sedicesimo dopo. PRV legge il consenso al trigger, non la durata del campione.

Prova successiva. Usa SED 2A in FX2 sulla 00 per rendere ripetibile il disegno di probabilità.

Se il risultato cambia. Non spostare CHN in FX2: lì controllerebbe solo il comando FX1, non la nota.


### H07 Far comparire un fill ogni quattro giri

Conservare la batteria regolare e aggiungere un finale solo nel quarto giro.

Preparazione. Una sola Phrase ripetuta sulla traccia snare, senza JMP/HOP. I00 snare.

1. Metti gli accenti regolari senza condizione sulle righe 04 e 0C.

2. Aggiungi gli eventi 0D,0E,0F con CND 44. Tutta la riga passa soltanto nel quarto giro su quattro.

3. Riparti con Stop/Play per riallineare il conteggio.

```
ROW NTE IN FX1    FX2
04  C-4 00 --- 00 --- 00
0C  C-4 00 --- 00 --- 00
0D  C-4 00 CND 44 VOL 70
0E  C-4 00 CND 44 VOL 90
0F  C-4 00 CND 44 VOL B0
```

Da ascoltare. Tre colpi crescenti completano soltanto il quarto giro. Nei primi tre passaggi le note aggiuntive non vengono attivate.

Prova successiva. CND 24 fa comparire il fill nel secondo giro di ogni gruppo di quattro.

Se il risultato cambia. Un JMP all’indietro fa avanzare il contatore. NTH 44 non è equivalente: passa già sul primo giro, con contatore zero.


### H09 Creare un ciclo di cinque passi contro una batteria regolare

Sfasare progressivamente un motivo monofonico rispetto a una Phrase da sedici righe.

Preparazione. T1 segue una Phrase regolare di sedici righe; T2 usa Phrase 01 e Chain 01, LENGTH 1. Un suono pluck distingue gli attacchi.

1. Su T2 scrivi cinque eventi e JMP 00 sulla riga 04. Quel comando salta dopo la riga corrente.

2. Lascia T1 senza salti. Le tracce avanzano indipendentemente.

3. Conta i sedicesimi: il ciclo da cinque righe riallinea l’inizio con quello da sedici dopo 80 righe, cinque battute.

```
PHRASE 01 su T2
ROW NTE IN FX1    FX2
00  C-4 00 --- 00 --- 00
01  G-4 00 --- 00 --- 00
02  C-5 00 --- 00 --- 00
03  G-4 00 --- 00 --- 00
04  E-4 00 JMP 00 --- 00
```

Da ascoltare. Un ciclo di cinque sedicesimi si muove rispetto al riferimento di quattro quarti. È un ciclo locale, non un cambio globale di metrica.

Prova successiva. Sposta JMP sulla 06 per un ciclo di sette righe. Il riallineamento con sedici arriva dopo 112 righe.

Se il risultato cambia. JMP 00 non passa alla Phrase successiva. Su quella traccia la Chain e la Song non avanzano finché il loop resta attivo.


### H19 Combinare una batteria sample con percussioni sintetiche

Usare la stabilità dei campioni e la variabilità timbrica di KICK SNARE CYMBAL.

Preparazione. T1 SAMPLE CR78 Kick, T2 BRAIDS SNARE, T3 SAMPLE ClosedHat, T4 BRAIDS CYMBAL. Prepara uno slot Instrument diverso per ogni ruolo.

1. Kick sample a C4; SNARE sintetica a C3; hat sample a C4; CYMBAL a C4.

2. Per CYMBAL usa AMP ON A 00 D 40 S 00 R 20: il motore continuo deve avere una forma di ampiezza percussiva.

3. Sulla SNARE alterna COL 30 e B0. Lascia basso il livello del cymbal e usa RSN con moderazione.

```
SNARE su una propria Phrase
04 C-3 01 COL 30 --- 00
0C C-3 01 COL B0 --- 00

CYMBAL su una propria Phrase
00 C-4 03 TIM 80 RSN 30
08 C-4 03 TIM C0 RSN 50
```

Da ascoltare. Il ritmo mantiene il riferimento PCM, mentre la snare e il piatto cambiano carattere fra gli accenti.

Prova successiva. Prova anche KICK sintetica a C2 con TIM diverso sui due colpi della battuta.

Se il risultato cambia. Non usare C2 sui campioni se vuoi la loro altezza originale: la root PCM è C4. Il pitch del sample cambia anche la durata.


### H20 Ricavare più articolazioni da un solo campione

Usare STA e LEN come selezione di regioni, senza supporre un motore di slicing con punti memorizzati.

Preparazione. I00 SAMPLE CR78 GuiroLong o un MiniPops FX abbastanza lungo, TABLE FF. Confronta a C4.

1. Metti STA e LEN sulla stessa riga di ogni nuovo trigger: una nota nuova ripristina la regione prima degli FX.

2. Primo trigger dall’inizio, secondo da un quarto, terzo da metà file.

3. Se un frammento è troppo debole, torna alla regione 00 e aumenta LEN prima di cambiare altri parametri.

```
ROW NTE IN FX1    FX2
00  C-4 00 STA 00 LEN 40
04  C-4 00 STA 40 LEN 40
08  C-4 00 STA 80 LEN 40
0C  C-4 00 STA C0 LEN 00
```

Da ascoltare. Quattro regioni producono articolazioni diverse dello stesso file. La regione finale viene sempre limitata alla fine del campione.

Prova successiva. Una Table può cambiare STA/LEN e usare RET come retrigger successivo; occorre che la voce sia ancora attiva.

Se il risultato cambia. Non ci sono slice marker, reverse o loop PCM in Meighty. STA su un campione già in corso non riposiziona subito la testina.


## Sintesi armonia e movimento


### H04 Creare un arpeggio ritmico su una sola voce

Alternare rapidamente le altezze con ARP. Per tre note simultanee usa invece CHD sulla traccia polifonica, come nel capitolo 4.

Preparazione. I00 BASIC PULSE, AMP Sustain C0, TABLE FF, Global CHROMATIC.

1. Scrivi una sola nota con ARP 47 e ARC 02. L’AMP deve rimanere aperto.

2. Ascolta prima i tre gradi maggiori, poi cambia ARP in 37 per la triade minore.

3. Se vuoi una sequenza di quattro o più altezze, spegni ARP con 00 e usa la Table mostrata sotto.

```
PHRASE
00 C-4 00 ARP 47 ARC 02
08 OFF FF --- 00 --- 00

ALTERNATIVA TABLE 00 con ARP 00
ROW PIT VL FX1    FX2    FX3
00  +00 C0 TIC 03 --- 00 --- 00
01  +04 C0 --- 00 --- 00 --- 00
02  +07 C0 --- 00 --- 00 --- 00
03  +12 C0 HOP 00 --- 00 --- 00
```

Da ascoltare. ARP produce Do Mi Sol; la Table aggiunge Do all’ottava superiore. Nessuno dei due crea nuovi attacchi d’inviluppo a ogni altezza.

Prova successiva. Imposta una diversa VL per ogni riga Table se vuoi anche accenti diversi.

Se il risultato cambia. Non lasciare ARP 47 mentre provi il PIT della Table: i due pitch si sommano.


### H08 Creare una melodia generativa ripetibile

Separare la casualità utile da una sequenza che cambia a ogni ascolto.

Preparazione. I00 SYNTH PULSE o FM4 BASS, TABLE FF. Global MIN PENT, tonica C. Lascia fisse le colonne IN.

1. Scrivi quattro Do con RNL 30: cambia solo l’altezza di ±3 semitoni, perché il nibble basso è zero.

2. Inserisci SED 2A solo sulla prima riga. La scala quantizza le altezze generate verso i gradi ammessi inferiori.

3. Ascolta più giri, poi cambia soltanto SED 2A in 63. Per un’evoluzione continua elimina SED dalla Phrase ripetuta.

```
ROW NTE IN FX1    FX2
00  C-4 00 RNL 30 SED 2A
04  C-4 00 RNL 30 --- 00
08  C-4 00 RNL 30 --- 00
0C  C-4 00 RNL 30 --- 00
```

Da ascoltare. Ogni giro ripete lo stesso disegno finché seme e consumo del generatore restano uguali. Le celle scritte rimangono Do.

Prova successiva. Combina la melodia con una Table filtro deterministica per cambiare timbro senza consumare altre estrazioni casuali.

Se il risultato cambia. RNL 33 varia anche lo strumento. Usa Y=0 se non hai preparato una zona di preset intercambiabili.


### H10 Usare una Table che termina e lascia il suono acceso

Fare una piccola salita ripetuta tre volte e poi tenere l’ottava finale.

Preparazione. I00 SYNTH con Sustain C0, TABLE FF, ARP 00. Phrase con una sola C4 e TBL 00.

1. Compila la Table qui sotto, con VL costante su tutte le righe.

2. HOP 20 significa due ritorni alla riga 00 oltre al primo passaggio.

3. STP sulla 02 interrompe la lettura della Table; la voce continua all’ultima altezza.

```
TABLE 00
ROW PIT VL FX1    FX2    FX3
00  +00 C0 TIC 03 --- 00 --- 00
01  +07 C0 HOP 20 --- 00 --- 00
02  +12 C0 STP 00 --- 00 --- 00

PHRASE
00 C-4 00 TBL 00 --- 00
0E OFF FF --- 00 --- 00
```

Da ascoltare. Si alternano Do e Sol per tre passaggi totali; poi la voce resta a Do5. L’ottava arriva al tick 18 dall’inizio.

Prova successiva. Sostituisci PIT con CUT se vuoi un contorno timbrico a loop finito.

Se il risultato cambia. HOP 00 non finisce mai. Se l’AMP muore prima del tick 18, aumenta Sustain o allunga il Decay.


### H11 Distinguere uno sweep da una variazione casuale

Confrontare REP, che accumula, e RND, che riparte da un riferimento.

Preparazione. I00 BRAIDS MORPH, LP aperto, AMP Sustain C0, TABLE FF. Usa due Phrase alternative nella stessa Chain.

1. Nella prima Phrase metti TIM 20 e REP 10 nella stessa colonna. RTO C0 pone il limite.

2. Nella seconda usa TIM 80 e più RND 20. Le estrazioni restano nella zona 60–A0 a passi di 10.

3. Ascolta prima ciascuna Phrase da sola, poi alternale nella Chain.

```
PHRASE 00 rampa
00 C-3 00 TIM 20 --- 00
01 --- FF REP 10 --- 00
04 --- FF RTO C0 --- 00

PHRASE 01 casuale intorno alla base
00 C-3 00 TIM 80 SED 2A
04 --- FF RND 20 --- 00
08 --- FF RND 20 --- 00
0C --- FF RND 20 --- 00
```

Da ascoltare. La prima si apre in modo ordinato; la seconda salta attorno allo stesso centro senza allontanarsene progressivamente.

Prova successiva. Per un dettaglio fine usa RND 02: vari soltanto il nibble basso.

Se il risultato cambia. RND non continua automaticamente sulle righe vuote. Per un nuovo valore a ogni riga devi scriverlo o usare una Table in loop.


### H12 Muovere due wavetable in direzioni opposte

Creare un timbro vivo con un solo LFO e profondità opposte.

Preparazione. I00 DUAL WT. OSC1 CLASSIC, OSC2 HOLLOW, SEMI 0, DETUNE 80, MIX 80, SYNC OFF, POS1/POS2 80. AMP ON A 00 D 20 S C0 R 40; TABLE FF.

1. Apri Modulazioni. LFO1 SIN, RATE 40, PHASE 00; POS1 +64 e POS2 -64. Lascia neutre le altre quattro profondità.

2. Lascia LFO2 POS1/POS2 a zero. Inserisci una nota lunga con OFF sulla 0E.

3. Il RATE 40 vale circa 1,30 Hz, un ciclo in circa 0,77 secondi. La nota dura abbastanza per sentirne due; poi prova RATE 20 per un movimento più lento.

```
PHRASE
00 C-3 00 --- 00 --- 00
0E OFF FF --- 00 --- 00

LFO1    SIN  RATE 40  PHASE 00
POS1    +64 decimale
POS2    -64 decimale
LFO2 POS1/POS2  0 decimale
```

Da ascoltare. OSC1 diventa più ricco mentre OSC2 si muove nella direzione opposta. La prima pagina Deep Blue mostra le forme alle posizioni base; ascolta il movimento prodotto dagli LFO.

Prova successiva. Due LFO allo stesso RATE, uno PHASE 00 e uno 80, possono muovere separatamente POS1 e POS2 in controfase. Se li mandi uguali alla stessa posizione si annullano.

Se il risultato cambia. Una nuova nota riavvia le fasi. MIX 00 nasconde OSC2; MIX FF nasconde OSC1. Vicino a 00/FF la modulazione viene limitata, non avvolta.


### H13 Combinare una scansione a gradini con il movimento continuo

Usare una Table come forma principale e un LFO come movimento locale.

Preparazione. DUAL WT, OSC1 GLASS, MIX 00, AMP Sustain C0. LFO1 SIN RATE 20 POS1 +16, altre profondità neutre. TABLE FF.

1. Compila Table 00 con quattro basi WTP. TIC 06 crea un cambio per riga Phrase.

2. Richiama la Table con TBL 00 sulla nota iniziale e non inserire altre note fino al termine del contorno.

3. HOP 00 ricomincia il percorso. Il LFO continua a oscillare intorno a ciascun gradino.

```
TABLE 00
ROW PIT VL FX1    FX2    FX3
00  +00 C0 WTP 30 TIC 06 --- 00
01  +00 C0 WTP 60 --- 00 --- 00
02  +00 C0 WTP 90 --- 00 --- 00
03  +00 C0 WTP C0 HOP 00 --- 00

PHRASE
00 C-3 00 TBL 00 --- 00
0E OFF FF --- 00 --- 00
```

Da ascoltare. Quattro zone spettrali vengono percorse a tempo; dentro ogni zona resta un piccolo movimento continuo. La Table non modifica il valore scritto in Instrument.

Prova successiva. Usa OSM in FX3 per bilanciare i due oscillatori, oppure WT2 per una seconda scansione indipendente.

Se il risultato cambia. Se WTP è anche nella Phrase sullo stesso tick, la Table può prevalere perché viene elaborata dopo. Le memorie REP di Table e Phrase sono separate.


### H14 Ottenere battimenti e poi un timbro hard sync

Confrontare un unisono leggermente stonato con il riavvio forzato di OSC2.

Preparazione. DUAL WT, due CLASSIC posizione C0, MIX 80, SEMI 0, AMP Sustain C0, TABLE FF.

1. Con SYNC OFF confronta DTN 80 e DTN 88: l’intervallo resta quasi unisono e compaiono battimenti.

2. Per la seconda prova imposta OSC2 SEMI +7 in Instrument e MIX C0.

3. Attiva SYN 01 e poi disattivalo sulla stessa nota, per isolare il cambiamento.

```
PROVA UNISONO
00 C-3 00 DTN 80 --- 00
08 --- FF DTN 88 --- 00

PROVA SYNC con OSC2 SEMI +7
00 C-3 00 OSM C0 SYN 00
04 --- FF SYN 01 --- 00
08 --- FF SYN 00 --- 00
```

Da ascoltare. Il primo confronto produce battimenti; il secondo passa a uno spettro vincolato al ciclo di OSC1.

Prova successiva. Prova OSC2 HOLLOW o GLASS per cambiare la risposta del sync. WT2 ne muove la forma; non cambia il suo intervallo.

Se il risultato cambia. DTN 00 è una stonatura negativa, non zero. Il sync può produrre componenti aspre: usa il filtro se desideri un risultato più morbido.


### H15 Programmare un basso FM a due operatori

Partire da una struttura FM leggibile prima di usare tutti e quattro gli operatori.

Preparazione. I00 FM4, algoritmo 1, feedback 00. AMP A 00 D 20 S C0 R 20, TABLE FF. Filtro LP cutoff C0, resonance 20.

1. OP1: Ratio 1, Level FF, A 00 D 20 S C0 R 20. È la portante finale.

2. OP2: Ratio 2, Level 90, A 00 D 30 S 20 R 20. OP3 e OP4: Level 00.

3. INDEX 60. Scrivi il basso; poi confronta FAI 20 e 90 sulla stessa nota.

```
ROW NTE IN FX1    FX2
00  C-2 00 FAI 20 --- 00
04  C-2 00 FAI 90 --- 00
08  G-2 00 FAI 40 --- 00
0C  C-3 00 FAI 70 --- 00
```

Da ascoltare. OP2 crea un attacco più brillante e poi si riduce verso Sustain 20. La portante mantiene il corpo del basso.

Prova successiva. OR2 03 usa rapporto 3 al posto di 2. Nell’editor scegli il rapporto reale; nella Phrase OR2 usa il suo indice.

Se il risultato cambia. Se OP2 ha livello zero o INDEX 00 non senti FM. Se l’AMP comune decade prima di OP2, la differenza fra inviluppi resta nascosta.


### H16 Creare una campana con quattro inviluppi

Separare la coda del corpo dall’attacco metallico usando due coppie FM.

Preparazione. FM4 algoritmo 5, cioè 2>1 più 4>3. INDEX 80, feedback 10. AMP A 00 D 20 S FF R 90, TABLE FF.

1. Portanti OP1 e OP3: Ratio 1 e 3, Level D0 e 80; A 00 D 90 S 00 R 80.

2. Modulatori OP2 e OP4: Ratio 7 e 11, Level B0 e 70; A 00 D 30 S 00 R 30.

3. Inserisci una sola nota per Phrase e un poco di RSN. I modulatori decadono prima delle portanti, togliendo brillantezza alla coda.

```
ROW NTE IN FX1    FX2
00  C-4 00 FAI 80 RSN 60
0E  OFF FF --- 00 --- 00
```

Da ascoltare. Un attacco metallico lascia una coda più semplice. Per ascoltarla intera, lascia proseguire il trasporto e dirada gli attacchi in più Phrase.

Prova successiva. Cambia OR4 da 0B a 0D per passare dal rapporto 11 a 14 e confrontare il colore della seconda coppia.

Se il risultato cambia. Ratio frazionari arbitrari non sono disponibili: la lista è 0,5;1–12;14;16. Il firmware non importa patch DX/TX.


### H17 Cambiare algoritmo FM senza cambiare nota

Usare una Table per confrontare tre strutture durante una nota sostenuta.

Preparazione. FM4 con tutti e quattro i Level e Sustain aperti; rapporti 1,2,3,4; INDEX 60. AMP Sustain C0, TABLE FF.

1. La pagina Instrument numera gli algoritmi 1–8, gli FX FAL usano 00–07.

2. Prepara i tre FAL e STP nella Table. TIC 0C dà dodici tick per struttura.

3. Richiama la Table con una nota lunga e ascolta il cambiamento senza nuovi attacchi.

```
TABLE 00
ROW PIT VL FX1    FX2    FX3
00  +00 C0 FAL 00 TIC 0C FAI 60
01  +00 C0 FAL 04 --- 00 --- 00
02  +00 C0 FAL 07 STP 00 --- 00

PHRASE
00 C-3 00 TBL 00 --- 00
0E OFF FF --- 00 --- 00
```

Da ascoltare. Serie di quattro operatori, poi due coppie, infine quattro portanti indipendenti. Nell’ultimo caso l’indice non crea modulazione fra operatori.

Prova successiva. Sostituisci FAL con OR2 per una sequenza di rapporti oppure FBK per un percorso del feedback.

Se il risultato cambia. I cambi di algoritmo possono essere bruschi; non promettono un crossfade. Se un operatore è già decaduto, potrebbe non partecipare al confronto.


### H18 Confrontare i modelli analogici Braids

Capire cosa cambia fra MORPH, SAW SUB e SAW SYNC a parità di nota.

Preparazione. SOURCE SYNTH, AMP Sustain C0, TABLE FF, filtro LP abbastanza aperto. Usa la stessa nota per il confronto.

1. MDL sceglie il modello operativo: 09 MORPH, 0B SAW SUB e 0C SAW SYNC.

2. Metti MDL in FX1 e TIM in FX2 sulla stessa riga. COLOR parte dalla base dello strumento dopo il cambio.

3. Ascolta prima i tre modelli; poi dedica una Phrase a ciascuno e muovi anche COL.

```
ROW NTE IN FX1    FX2
00  C-3 00 MDL 09 TIM 60
04  --- FF MDL 0B TIM 60
08  --- FF MDL 0C TIM 60
```

Da ascoltare. MORPH cambia forma, SAW SUB aggiunge il registro basso, SAW SYNC introduce la relazione master/slave. Il cambio ricrea lo stato del motore.

Prova successiva. Su SAW SUB confronta COL 20,80,E0: il centro cambia registro del sub e ne riduce il contributo.

Se il risultato cambia. TIM/COL non sono parametri identici su tutti i modelli. Non applicare i nomi INDEX o POS1 ai modelli analogici Braids.


## Spazio arrangiamento e performance


### H21 Creare un delay throw e una coda ambient

Mandare solo una nota al delay e conservare un ambiente più ampio sul pad.

Preparazione. Master: 1/8D, Feedback 80, Ping Pong ON, Delay Return 80; AMBIENT, Decay C0, Damp 70, Reverb Return 70.

1. Sulla traccia lead apri DSN soltanto sulla risposta e richiudilo alla riga successiva.

2. Su un’altra traccia con pad apri RSN 80 e dirada gli attacchi.

3. Lascia andare il trasporto durante l’ascolto delle code: Stop cancella i buffer.

```
LEAD
00 C-4 00 DSN 00 PAN 30
08 G-4 00 DSN C0 PAN D0
09 --- FF DSN 00 --- 00

PAD in un’altra traccia
00 C-3 01 RSN 80 --- 00
0C OFF FF --- 00 --- 00
```

Da ascoltare. Soltanto la risposta alimenta gli echi; il pad crea la coda diffusa. A 120 BPM il tempo 1/8D è 375 ms.

Prova successiva. Per uno spazio più asciutto diminuisci i send prima di abbassare i return: così valuti il contributo di una singola traccia.

Se il risultato cambia. Un LEV molto basso riduce anche il send post fader. Nessun comando Phrase di Meighty cambia direttamente decay o feedback master.


### H22 Simulare un pompaggio ritmico senza sidechain audio

Disegnare con una Table una riduzione e risalita del livello di traccia.

Preparazione. Pad DUAL WT o BASIC PULSE, AMP Sustain C0, TABLE FF. Kick su un’altra traccia con colpi ogni quattro righe. Questo è un inviluppo programmato, non un compressore che ascolta il kick.

1. Metti LEV nella Table, non VOL, per controllare il fader della traccia.

2. Con TIC 06 ogni riga Table dura un sedicesimo; HOP 00 crea un ciclo di quattro righe, un quarto.

3. Il pad parte con TBL 00 e resta aperto. Non introdurre nuovi trigger a ogni sedicesimo.

```
TABLE 00
ROW PIT VL FX1    FX2    FX3
00  +00 C0 LEV 20 TIC 06 --- 00
01  +00 C0 LEV 60 --- 00 --- 00
02  +00 C0 LEV A0 --- 00 --- 00
03  +00 C0 LEV D0 HOP 00 --- 00

PHRASE PAD
00 C-3 00 TBL 00 --- 00
```

Da ascoltare. Il pad si abbassa sul kick e risale a gradini. Le mandate post fader seguono il pompaggio, ma le code già create possono continuare.

Prova successiva. Aggiungi PAN in FX3 alle righe 01 e 02 per un movimento stereo coordinato.

Se il risultato cambia. Non usare un LFO libero come clock della prova: non è sincronizzato al BPM e il pompaggio si sfaserebbe.


### H23 Costruire un arrangiamento Berlin School su otto tracce

Costruire un arco con accordi sostenuti, sequenze e una pausa centrale prima del climax.

Preparazione. Global D MIN/AEOLIAN. Tre pad in I03–I05, AMP A 90 D 60 S C0 R 90; DUAL WT con detune lieve. Due pluck in I00–I01, basso I02, lead I06 e percussioni in I08–I0C.

1. Prepara Chain 00–07 lunghe quattro Phrase ciascuna. Per i pad usa una Phrase con la nota iniziale e poi Phrase 3F valida e vuota; non usare celle Song vuote per tenere il suono.

2. Distribuisci T1 sequenza, T2 risposta, T3 basso, T4–T6 pad, T7 lead, T8 percussioni alternate. Fai entrare prima i pad, poi la sequenza, poi il basso e infine la risposta e la batteria.

3. Prima del climax sostituisci le parti ritmiche con Chain di uguale durata contenenti OFF e poi righe vuote. Al ritorno usa una variante più fitta; nel finale riduci i LEV dei pad e rilascia le note.

```
PAD SU TRE TRACCE
Phrase 03  00 D-3 03 --- 00 --- 00
Phrase 04  02 F-3 04 --- 00 --- 00
Phrase 05  04 E-4 05 --- 00 --- 00
Phrase 3F  tutte le righe senza nota o FX

Chain 03  03 3F 3F 3F   LENGTH 4
Chain 04  04 3F 3F 3F   LENGTH 4
Chain 05  05 3F 3F 3F   LENGTH 4
```

Da ascoltare. Le tre voci compongono Re minore con nona aggiunta. Gli attacchi lenti non vengono azzerati a ogni battuta; la risposta e gli echi restano distinti dal fondo armonico.

Prova successiva. Usa le due Song di esempio come studio: Oltre le dune e Orbite profonde hanno 116 battute, una sospensione centrale e un finale scritto. Gli stati sono separati dagli esempi E00–E13.

Se il risultato cambia. Questo esempio usa tre pad con suoni separati; per armonizzare un solo Instrument su una traccia usa CHD e Poly 3 track. Una Phrase vuota tiene la voce, mentre una cella Song vuota la spegne e può avere una durata diversa dalle Chain delle altre tracce.


### H24 Preparare una performance e salvarla correttamente

Passare dalla prova alla conservazione del progetto senza perdere patch e automazioni.

Preparazione. Un progetto funzionante sul FM-1 e uno slot Global scelto consapevolmente.

1. In Song scegli la traccia con SELECT, OCT− commuta mute e OCT+ solo. Più solo possono essere attivi; mute prevale. Le tracce continuano ad avanzare mentre non si sentono.

2. In Mixer regola le basi LEV/PAN/send; un tocco manuale riprende il controllo del parametro rispetto al relativo override Phrase.

3. Premi STOP. In Global scegli la destinazione e usa Save slot; SAVE salva invece lo slot già aperto. Nei tools, Backup ed estrazione permette poi di scaricare il backup .meighty con un nome riconoscibile.

```
PRIMA DI CHIUDERE
1  Ferma e riavvia per verificare l’inizio della Song
2  Controlla mute e solo
3  Salva lo slot Global scelto
4  Esporta il file del proprio ambiente
5  Conserva copie nominate prima di sostituire brani o preset
```

Da ascoltare. Al caricamento ritrovi strumenti, LFO, Table, Song, mixer di base e impostazioni globali. Non viene ripreso il punto esatto del motore in esecuzione.

Prova successiva. Conserva progetti e backup con nomi progressivi prima di sostituire preset o provare nuove generazioni.

Se il risultato cambia. Caricare un preset sostituisce lo slot Instrument. Nei tools scegli soltanto le destinazioni da trasferire: un brano nella casella 2 sostituisce solo lo slot 2; le altre posizioni restano invariate.


## Generazione ed evoluzione controllata

Un pool stabilisce quali note possono uscire; una probabilità stabilisce quando cambiare; una memoria stabilisce che cosa resta al giro successivo. Separare queste tre scelte permette di costruire una parte musicale ripetibile e poi aprirla alla variazione.

Ricetta | Obiettivo | Controllo principale

G01 | Due note precise, estrazione a ogni evento | CHN decide se applicare una Table di trasposizione

G02 | Tre note precise, estrazione a ogni evento | RNL sceglie una fra tre Table di una sola riga

G03 | Una nota estratta per tutta la Phrase | Una sola estrazione sulla prima riga, poi nota tenuta

G04 | Generare una Phrase e ripeterla uguale | SED inizializza il generatore una volta per giro

G05 | Far evolvere raramente il percorso di un pool | RND salta nella Table soltanto quando CHN lo consente

G06 | Performance tipo Turing con blocco e rigenerazione | Seme fisso per il loop; cambio del seme dal vivo

Preparazione comune. Usa un progetto nuovo e ricostruisci i dati della ricetta scelta. Prima di sostituire un brano salva il lavoro e scarica un backup .meighty. Un file importato in una sola casella dei tools modifica solo quello slot. Tutti gli esempi usano una sola traccia: Song 00, T1=Chain 00, Song LENGTH 1; Chain 00 contiene Phrase 00, LENGTH 1. Le altre tracce restano vuote. Global: 120 BPM, CHROMATIC, Root C.

Suono comune. I00 SYNTH, per esempio BASIC PULSE o DUAL WT. TABLE FF nello strumento: le Table vengono scelte dagli FX. AMP ON, Attack 00, Decay 20, Sustain C0, Release 20; filtro aperto e tutte le profondità LFO di pitch a zero. ARP, PBN, PVB, PIT e TSP assenti. Così il pool non viene alterato da altre trasposizioni. Dopo la prova puoi scegliere scala, inviluppi e timbro; una scala diversa può modificare le altezze finali.

Come leggere le Table. PIT nella Table è uno scostamento in semitoni rispetto alla nota della Phrase: +03 significa tre semitoni decimali, non una nota MIDI. VL è il volume della riga. Ogni riga sotto riporta tre FX, perché l’editor Table dispone di tre colonne. Le righe non elencate della Phrase restano vuote.

Che cosa viene salvato. Gli esempi generano note durante l’esecuzione: le celle della Phrase restano quelle scritte. SAVE conserva le impostazioni, le Table e il seme eventualmente scritto in SED; non registra automaticamente le note casuali appena ascoltate. Un seme ripete il risultato se restano uguali anche ordine e numero delle estrazioni sulla stessa traccia.

Turing Machine. G06 spiega la performance disponibile con un seme. Il firmware attuale non possiede un registro a scorrimento che memorizzi le singole mutazioni e congeli l’ultimo giro casuale ascoltato. Bloccare un seme e bloccare quel giro sono due operazioni diverse: il limite è esplicitato nell’esempio, così non cerchi un controllo che ancora manca.


## G01 Due note fissate: Do4 oppure Sol4 a ogni step

Obiettivo. Ogni attacco sceglie fra C4 e G4, senza note intermedie e senza cambiare il ritmo. Il pool può contenere anche due note lontane, senza doverle ricavare da una scala.

Preparazione. Usa i collegamenti e il suono della pagina introduttiva. In Table 00 imposta LENGTH 1 e la riga sotto. STP ferma la Table dopo averne applicato PIT e VL: la nota continua a suonare.

```
TABLE 00  LENGTH 1
ROW PIT VL FX1    FX2    FX3
00  +07 C0 STP 00 --- 00 --- 00

PHRASE 00
ROW NTE IN FX1    FX2
00  C-4 00 TBL 00 CHN 80
04  C-4 00 TBL 00 CHN 80
08  C-4 00 TBL 00 CHN 80
0C  C-4 00 TBL 00 CHN 80
```

Perché funziona. Una nuova nota riparte da C4 e dalla TABLE FF dello strumento. CHN in FX2 decide soltanto se eseguire TBL in FX1. Se TBL non passa, senti C4; se passa, Table 00 applica +7 e senti G4. La nota non viene bloccata: tutti e quattro gli attacchi rimangono.

Probabilità. CHN 00 dà soltanto C4; CHN FF soltanto G4; CHN 80 circa metà per ciascuna. CHN 20 rende Sol raro, circa il 12,5%; CHN E0 lo rende frequente, circa l’87,8%. Queste sono probabilità su molti attacchi: un giro di quattro note può contenere ripetizioni.

1. Premi PLAY e ascolta almeno otto giri. Controlla che escano soltanto Do e Sol.

2. Porta il valore CHN della riga 08 a FF: quel solo step diventa sempre Sol, gli altri continuano a scegliere.

3. Porta CHN della riga 00 a 00: ottieni un Do fisso come punto d’appoggio. Lascia 80 sulle due posizioni rimanenti.

Cambiare il pool. Per Re4 e La4 scrivi D-4 al posto di C-4 e lascia PIT +07. Per Do4 e Mi♭4 lascia C-4 e cambia il PIT della Table a +03. Per due note discendenti puoi usare un PIT negativo, entro i limiti della Table.

Errore da evitare. CHN in FX1 controllerebbe il trigger della nota e potrebbe creare silenzi. Qui deve stare in FX2, a destra di TBL. TABLE nello strumento deve restare FF, altrimenti anche il ramo senza TBL potrebbe avviare una Table.


## G02 Tre note fissate: una scelta indipendente a ogni step

Obiettivo. Ogni attacco sceglie una nota del pool C4, E♭4, G4. Gli intervalli sono arbitrari: prepara tre Table di una sola riga, una per ciascuna altezza.

```
TABLE 00  LENGTH 1
00 +00 C0 STP 00 --- 00 --- 00
TABLE 01  LENGTH 1
00 +03 C0 STP 00 --- 00 --- 00
TABLE 02  LENGTH 1
00 +07 C0 STP 00 --- 00 --- 00

PHRASE 00
ROW NTE IN FX1    FX2
00  C-4 00 TBL 01 RNL 01
04  C-4 00 TBL 01 RNL 01
08  C-4 00 TBL 01 RNL 01
0C  C-4 00 TBL 01 RNL 01
```

Perché funziona. RNL in FX2 modifica il valore dell’FX alla sua sinistra, TBL 01. Il nibble alto 0 non cambia la cifra alta; quello basso 1 estrae uno scostamento −1, 0 oppure +1. Il comando eseguito diventa quindi TBL 00, 01 o 02. La Table applica rispettivamente 0, +3 o +7 semitoni e si ferma. I tre esiti hanno probabilità sostanzialmente uguali, con possibili ripetizioni consecutive.

Per step. Puoi lasciare il random soltanto su 04 e 0C. Per fissare il primo Do scrivi C-4 00 TBL 00 --- 00 sulla 00; per fissare il Sol scrivi TBL 02 senza RNL. La presenza del generatore in una riga non obbliga tutte le altre a essere casuali.

Cambiare o pesare il pool. Sostituisci i tre PIT: per C4, D4, A4 usa +00, +02, +09. Per un pool di due note con Do più frequente usa PIT +00, +00, +07: due Table su tre producono Do. Per due note con probabilità circa uguali usa invece G01.

Una sola destinazione. In questa ricetta RNL 01 varia l’ID della Table, non la nota della Phrase. Non metterlo in FX1: lì cambierebbe nota o Instrument secondo i suoi nibble, con un’altra semantica. Non aumentare il raggio a 02 senza preparare gli ulteriori ID raggiungibili.

Da ascoltare. Il ritmo resta regolare, mentre il profilo melodico cambia a ogni giro. Riduci il volume e aggiungi poco delay dopo avere verificato il pool asciutto: le ripetizioni degli effetti possono rendere difficile distinguere i nuovi attacchi.


## G03 Una scelta per Phrase: nota casuale mantenuta per un giro

Obiettivo. Un pad o un basso sostenuto sceglie una nota fra Do, Mi♭ e Sol all’inizio della Phrase, poi la mantiene fino al giro successivo. È una frequenza di estrazione diversa da G02: una scelta per Phrase, non una per attacco ritmico.

Preparazione. Usa le tre Table di G02, tutte LENGTH 1 con STP 00. AMP Sustain C0 e TABLE FF nello strumento. Su Phrase 00 scrivi soltanto la riga seguente; tutte le altre restano senza note e senza FX.

```
PHRASE 00
ROW NTE IN FX1    FX2
00  C-4 00 TBL 01 RNL 01

01–0F: NTE ---, IN FF, FX vuoti

POOL TABLE
00: PIT +00, VL C0, STP 00
01: PIT +03, VL C0, STP 00
02: PIT +07, VL C0, STP 00
```

Perché funziona. La prima riga sceglie una Table. La Table applica il proprio PIT una sola volta e STP la arresta: l’altezza scelta rimane nella voce. Le righe Phrase vuote non fanno nuove estrazioni e non spengono la nota. Al giro successivo la nuova C4 riavvia il suono e sceglie di nuovo.

1. Ascolta a 120 BPM: ogni Phrase dura circa due secondi e produce una nota tenuta. Due giri possono scegliere la stessa altezza.

2. Confronta con G02, che prende quattro decisioni nella stessa durata. Poi aggiungi la stessa riga anche sulla 08: ora scegli due volte per giro.

3. Per una nota fissa per due Phrase, prepara Phrase 01 completamente vuota e imposta Chain 00 = 00,01, LENGTH 2. La prima Phrase sceglie; la seconda conserva la nota. Non usare una cella Song vuota: spegnerebbe la voce.

Ripetibilità. Con queste due colonne occupate non c’è spazio per SED sulla stessa riga. Per un disegno ripetibile con più eventi usa la riga di inizializzazione separata di G04. Non aggiungere un presunto terzo FX alla Phrase: i terzi FX esistono soltanto nelle Table.

Suono. Per un pad prova Attack 50, Release 70, riverbero AMBIENT e una mandata moderata. Per un basso sostieni la nota con un suono semplice e abbassa il registro a C-2. La logica del pool rimane identica.


## G04 Generare un motivo nel pool e ripeterlo identico

Obiettivo. Ottenere quattro note casuali nel pool Do, Mi♭, Sol, ma ripetere la stessa frase a ogni giro. Puoi poi cambiare un solo valore per ottenere un’altra variante deterministica.

Preparazione. Le tre Table sono quelle di G02. La riga 00 serve soltanto a SED; gli attacchi sono su 01,05,09,0D. Questo crea volutamente un ingresso un sedicesimo dopo l’inizio della Phrase e lascia libere entrambe le colonne degli eventi.

```
PHRASE 00
ROW NTE IN FX1    FX2
00  --- FF SED 2A --- 00
01  C-4 00 TBL 01 RNL 01
05  C-4 00 TBL 01 RNL 01
09  C-4 00 TBL 01 RNL 01
0D  C-4 00 TBL 01 RNL 01

TABLE 00: PIT +00, VL C0, STP 00
TABLE 01: PIT +03, VL C0, STP 00
TABLE 02: PIT +07, VL C0, STP 00
Tutte LENGTH 1
```

Perché funziona. SED 2A riporta il generatore della traccia allo stesso stato sulla 00. Le quattro estrazioni successive seguono sempre lo stesso ordine: a ogni nuovo giro ritorna la stessa sequenza di quattro scelte. Le celle visualizzate restano C-4: non sono state riscritte con le note ascoltate.

Risultato verificato con questa preparazione: SED 2A produce Mi♭–Sol–Do–Mi♭; 2B produce Do–Sol–Sol–Mi♭. Sono le quattro estrazioni di T1 con questi soli eventi casuali. Se aggiungi altri comandi probabilistici sulla stessa traccia, il disegno può cambiare.

1. Ascolta quattro giri senza toccare nulla. Conta il profilo di altezze: deve ripetersi.

2. In Phrase seleziona il valore di SED sulla 00 e cambia 2A in 2B mentre suona. Dal prossimo passaggio sulla 00 verrà generata la variante associata al nuovo seme.

3. Lascia il valore fermo: quella variante continua a ripetersi. Torna a 2A per recuperare il primo motivo, se pool e altre estrazioni sono rimasti uguali.

4. Per un flusso che cambia a ogni giro elimina il comando SED dalla 00. Per tornare al motivo salvato riscrivi SED e il suo valore.

Controllo. Non usare CHN o CND per tentare di rendere probabilistico SED: nel motore SED viene elaborato prima dei gate. Per diradare le rigenerazioni cambia il seme manualmente a intervalli musicali, oppure prepara Phrase differenti con semi espliciti e disponile nella Chain.

Memoria. Reinserire SED richiama il motivo di quel seme; non cattura l’ultimo giro ascoltato durante il funzionamento libero. Aggiungere un altro random o una probabilità sulla stessa traccia può consumare estrazioni e cambiare il risultato. Le altre tracce possiedono generatori indipendenti.


## G05 Evoluzione rara del percorso dentro un pool

Obiettivo. Far girare un disegno di otto step e introdurre salti occasionali nel percorso, conservando sempre le stesse tre altezze. La probabilità controlla quanto spesso il percorso viene perturbato, non quanto lontano può uscire dal pool.

Preparazione. I00 con nota sostenuta e TABLE FF. Table 00 LENGTH 8: PIT +00,+03,+07,+03,+00,+07,+03,+07; VL C0 su tutte le righe. Scrivi TIC 06 in FX1 soltanto sulla riga 00 della Table, gli altri FX Table vuoti. La Table scorre una riga per riga Phrase e riparte automaticamente dopo la 07.

```
PHRASE 00
ROW NTE IN FX1    FX2
00  C-4 00 TBL 00 --- 00
01  --- FF THO 03 --- 00
04  --- FF RND 03 CHN 20
08  --- FF RND 03 CHN 20
0C  --- FF RND 03 CHN 20

TABLE 00  LENGTH 8
PIT: +00 +03 +07 +03 +00 +07 +03 +07
VL:  C0  su tutte le otto righe
00 FX1 = TIC 06; tutti gli altri FX vuoti
```

Perché funziona. THO 03 inizializza la memoria della colonna FX1 con un punto d’ingresso noto. RND 03 varia quel valore di ±3 nel nibble basso, richiedendo una riga fra 00 e 06. CHN in FX2 permette di eseguire RND soltanto circa nel 12,5% dei casi. Fra le richieste la Table continua normalmente; un salto viene consumato durante l’elaborazione Table, dopo la sua riga corrente.

1. Porta tutti e tre i CHN a 00: nessun salto casuale, stesso percorso a ogni giro.

2. Portali a 20: ascolta piccoli cambiamenti di ordine, distanziati nel tempo. Una richiesta può scegliere la stessa destinazione e non produrre un cambiamento evidente.

3. Prova 80 per un comportamento più mobile e FF per richiedere un salto a ogni punto scritto. Per tornare al percorso regolare rimetti i tre valori a 00.

Che cosa evolve. Cambiano ordine e ripetizioni delle altezze, non i PIT salvati nella Table. Il pool rimane Do, Mi♭, Sol anche quando il percorso torna indietro. È diverso da RNL sulla nota, che varia un’altezza attorno a una base e poi può essere quantizzato dalla scala.

Limite del blocco. Chiudere CHN ferma le nuove perturbazioni; non memorizza una copia dell’ultimo giro. Alla riga 00 successiva il trigger e TBL riavviano la Table. Per rendere permanente un nuovo ordine devi scriverlo nella Table e salvare il progetto.


## G06 Performance tipo Turing: blocco a seme e rigenerazione live

Obiettivo. Suonare un anello di otto note nel pool Do, Mi♭, Sol; tenerlo stabile; sostituirlo dal vivo con altre varianti e poter richiamare la prima. Questo esempio usa il generatore deterministico del tracker: è una performance a seme, non un registro Turing a mutazioni persistenti.

Preparazione. Tre Table di G02, LENGTH 1, rispettivamente PIT +00,+03,+07 e STP 00. Usa un pluck corto, delay 1/8D con poco feedback e una seconda traccia di basso fisso se vuoi un riferimento tonale. La prima prova va fatta sulla sola T1.

```
PHRASE 00
ROW NTE IN FX1    FX2
00  --- FF SED 2A --- 00
01  C-4 00 TBL 01 RNL 01
03  C-4 00 TBL 01 RNL 01
05  C-4 00 TBL 01 RNL 01
07  C-4 00 TBL 01 RNL 01
09  C-4 00 TBL 01 RNL 01
0B  C-4 00 TBL 01 RNL 01
0D  C-4 00 TBL 01 RNL 01
0F  C-4 00 TBL 01 RNL 01
```

1. BLOCCO. Lascia SED 2A: l’anello di otto estrazioni torna uguale a ogni giro. Seleziona già il byte 2A della riga 00, così puoi intervenire con K2 senza cambiare campo durante la performance.

2. RIGENERAZIONE. Dopo quattro giri porta il seme a 2B. Il nuovo motivo arriva al passaggio successivo sulla 00; lascia suonare due o quattro giri e poi prova 2C. Il pool e il ritmo restano quelli preparati.

3. RICHIAMO. Torna a 2A per recuperare l’anello iniziale. Conserva i semi preferiti come piccoli appunti oppure in Phrase diverse, ognuna con il proprio SED.

4. APERTURA. Elimina SED per lasciare avanzare il generatore: ogni giro può cambiare. Reinserisci un seme noto per tornare a un motivo ripetibile. Salva il progetto se vuoi conservare quel seme e le impostazioni.

Differenza rispetto a una vera Turing Machine. Qui cambiare seme può rigenerare tutte le otto scelte. Non esiste ancora una probabilità che riscriva e conservi soltanto uno o pochi step del giro precedente. Reinserire SED dopo il funzionamento libero non congela l’ultimo giro ascoltato. Il random agisce su copie operative, non sulla memoria delle celle.

Una mutazione davvero persistente si può fare manualmente: prepara un anello di otto PIT in una Table come in G05, senza salti casuali. Durante PLAY apri EDIT e cambia un solo PIT; il nuovo valore rimane nel ciclo ed è salvabile con SAVE. Le note intermedie attraversate dal rotativo possono essere udibili. Questa è una modifica live della memoria, ma non automatizza la mutazione Turing.


# 11 Combinare gli FX con un metodo di ascolto

Qui ogni esperimento isola una relazione: due parametri, due memorie, un gate oppure due sorgenti di modulazione. Gli esempi E01–E13 usano una sola traccia: imposta la preparazione e le righe riportate, premi PLAY e cambia soltanto il parametro indicato. Le spiegazioni distinguono il valore scritto da ciò che il motore esegue.


## E01 Aprire il filtro e spostare lo stesso suono

Preparazione. DUAL WT con Sustain C0, LP, cutoff e pan senza LFO. TABLE FF. Una sola nota lunga.

```
00 C-4 00 CUT 40 PAN 20
04 --- FF CUT C0 PAN E0
0E OFF FF --- 00 --- 00
```

Da ascoltare. La nota parte scura a sinistra e diventa più aperta a destra sulla 04. Non senti un secondo attacco.

Perché succede. CUT e PAN impostano parametri diversi. La riga senza NTE cambia la voce esistente; gli FX vengono applicati dopo il caricamento del suono della prima nota.

Confronto. Inverti soltanto i due valori PAN. Poi aggiungi una nuova C4 sulla 04 e confronta il retrigger.

Controllo. Se la nota muore prima della 04, alza Sustain. Se non senti lo spostamento, ascolta in stereo.


## E02 Confrontare memoria della colonna ed evento a sinistra

Preparazione. DUAL WT, MIX 00, POS1 80, Sustain C0. LFO POS neutri, TABLE FF.

```
00 C-4 00 WTP 80 --- 00
04 --- FF RND 20 --- 00
08 --- FF WTP 80 RNL 20
0C --- FF RND 20 --- 00
```

Da ascoltare. RND sulla 04 sceglie una posizione fra 60 e A0 a passi di 10. RNL sulla 08 varia il valore del WTP alla sua sinistra. La 0C usa come riferimento il WTP effettivamente ricordato sulla 08.

Perché succede. RND consulta la memoria della propria colonna; RNL trasforma una copia dell’evento subito a sinistra. La trasformazione RNL entra poi nella memoria come comando operativo eseguito.

Confronto. Sposta RND dalla colonna FX1 a FX2 sulla 04: senza un precedente comando operativo in FX2 non ottieni la stessa scansione.

Controllo. Non aspettarti una passeggiata casuale cumulativa da RND. La base cambia soltanto quando la colonna ricorda un nuovo comando operativo.


## E03 Due rampe indipendenti con limiti diversi

Preparazione. DUAL WT, nota sostenuta, LP e LFO neutri, TABLE FF. Ogni colonna avrà una propria memoria.

```
00 C-4 00 CUT 20 PAN E0
01 --- FF REP 08 REP F8
04 --- FF RTO 50 RTO A0
0A --- FF REP 00 REP 00
```

Da ascoltare. CUT sale di 8 e PAN scende di 8 per riga. CUT raggiunge 50 sulla 06; PAN raggiunge A0 sulla 08. Dopo i rispettivi limiti restano fermi.

Perché succede. REP 08 è positivo, REP F8 vale -8. RTO limita il repeater della stessa colonna: non imposta immediatamente il parametro.

Confronto. Scambia i due REP mantenendo i limiti: sentirai perché la direzione del limite conta. Poi torna ai dati originali.

Controllo. Le righe omesse continuano la rampa. Un FX operativo nuovo nella stessa colonna la interrompe e sostituisce la memoria.


## E04 Decidere se varia la nota oppure solo il suo cutoff

Preparazione. DUAL WT con attacco corto e sustain aperto, TABLE FF. Confronta quattro attacchi dello stesso Do.

```
00 C-4 00 CHN 80 CUT 30
04 C-4 00 CUT C0 CHN 80
08 C-4 00 CHA 8F CUT 30
0C C-4 00 CUT C0 CHA 8F
```

Da ascoltare. Sulla 00 CHN in FX1 decide il trigger; CUT passa sempre. Sulla 04 CHN in FX2 decide solo CUT: la nuova nota passa sempre. CHA sulla 08 decide nota/strumento con 8/15, lasciando CUT sempre attivo; sulla 0C decide insieme nota e CUT.

Perché succede. CHN usa il byte intero e, se non è in prima colonna, controlla solo l’FX immediatamente a sinistra. CHA legge due probabilità separate X e Y; in FX2 tutto il lato sinistro include anche la nota.

Confronto. Usa 00, 80 e FF per CHN; usa 0F, 8F e FF per CHA. Riparti con Stop/Play per confrontare lo stesso stato iniziale del generatore.

Controllo. Un trigger rifiutato può lasciare accesa la nota precedente. Ascolta l’attacco e guarda il contesto: una nota assente non implica voce spenta.


## E05 Melodia casuale in scala con una versione ripetibile

Preparazione. Global tonica C e MIN PENT. DUAL WT pluck, TABLE FF. Y di RNL resta zero per non cambiare strumento.

```
00 C-4 00 RNL 30 SED 2A
04 C-4 00 RNL 30 --- 00
08 C-4 00 RNL 30 --- 00
0C C-4 00 RNL 30 --- 00
```

Da ascoltare. Ogni giro ripete lo stesso disegno. Le note scritte restano Do, mentre quelle eseguite passano per variazione e quantizzazione. In questa preparazione il risultato può includere Sol3, Si♭3, Do4 e Mi♭4.

Perché succede. SED viene elaborato prima delle estrazioni anche se è in FX2. RNL varia di ±3 semitoni; poi la scala arrotonda al grado ammesso inferiore, che può stare sotto il limite grezzo A3.

Confronto. Rimuovi SED dalla Phrase ripetuta: il generatore continua fra i giri e il disegno evolve. Cambia il seme per un’altra versione ripetibile.

Controllo. Un’altra estrazione casuale sulla stessa traccia cambia la successione. Per un pool esatto di note non adiacenti usa E13.


## E06 Shuffle e probabilità sulla stessa riga

Preparazione. SAMPLE CR78 ClosedHat in I00, BPM 120, TABLE FF. Le righe 02 e 06 vengono ritardate.

```
00 C-4 00 --- 00 --- 00
02 C-4 00 DEL 01 CHA 8F
04 C-4 00 --- 00 --- 00
06 C-4 00 DEL 01 CHA 8F
```

Da ascoltare. Le note dispari del disegno arrivano un tick dopo, circa 20,8 ms a 120 BPM, e possono mancare. Le note sulle righe 00 e 04 restano regolari.

Perché succede. Il sequencer rileva DEL prima di eseguire il gate. Quando esegue la riga differita, CHA decide il consenso al trigger.

Confronto. Sostituisci CHA 8F con FF per sentire soltanto lo shuffle; poi passa a 4F per diradare gli eventi.

Controllo. DEL 06 salta la riga. DEL non è il delay audio: quello si ascolta con DSN e i ritorni master.


## E07 Separare durata della voce e movimento del timbro

Preparazione. DUAL WT, AMP ON A 00 D 20 S C0 R 60, LP e TABLE FF.

```
00 C-4 00 CUT 30 --- 00
04 --- FF CUT C0 --- 00
08 --- FF OFF 00 --- 00
0C C-4 00 CUT C0 KIL 03
```

Da ascoltare. La prima nota si apre senza retrigger e poi entra in Release sulla 08. L’ultima nota è tagliata dopo tre tick, senza coda ADSR.

Perché succede. CUT modifica una base della voce; OFF 00 avvia il rilascio con ADSR attivo. KIL programma una chiusura netta. Il riverbero, se aperto, può continuare dopo entrambi.

Confronto. Azzera la mandata riverbero per distinguere la Release del suono dalla coda dell’effetto.

Controllo. Il comando FX OFF 00 e la nota OFF non sono identici: la nota OFF ferma anche Table e retrigger.


## E08 Arpeggio e Table si sommano

Preparazione. DUAL WT con Sustain C0. Table 00 LENGTH 2, PIT 0 e +12, VL C0; TIC 06 sulla prima riga, HOP 00 sulla seconda.

```
PHRASE
00 C-4 00 ARP 37 ARC 02
04 --- FF TBL 00 --- 00
0C --- FF ARP 00 --- 00

TABLE 00
00 +00 C0 TIC 06 --- 00 --- 00
01 +12 C0 HOP 00 --- 00 --- 00
```

Da ascoltare. Prima senti l’arpeggio minore Do Mi♭ Sol. Dalla 04 i suoi tre gradi si alternano anche fra due ottave. Dalla 0C rimane soltanto il salto d’ottava della Table.

Perché succede. ARP sceglie uno dei tre intervalli; il PIT della Table aggiunge una trasposizione separata. Non viene creato un accordo polifonico e gli inviluppi non ripartono a ogni altezza.

Confronto. Sostituisci il PIT +12 della Table con +07 per un secondo movimento armonico.

Controllo. Per ascoltare una sola sorgente di pitch spegni l’altra: ARP 00 oppure STP 00. TBL FF non spegne la Table.


## E09 Table timbrica a tre colonne e durata controllata

Preparazione. DUAL WT, nota lunga, nessun altro CUT o PAN nelle Phrase. Table 00 LENGTH 4.

```
PHRASE
00 C-3 00 TBL 00 --- 00
0E OFF FF --- 00 --- 00

TABLE 00
00 +00 C0 CUT 30 PAN 30 TIC 03
01 +00 C0 CUT 80 PAN 70 --- 00
02 +00 C0 CUT C0 PAN B0 --- 00
03 +00 C0 CUT 60 PAN E0 STP 00
```

Da ascoltare. Filtro e pan percorrono quattro stati a distanza di tre tick. STP ferma il programma dopo l’ultimo stato; la nota rimane accesa fino alla OFF della Phrase.

Perché succede. Le tre colonne Table agiscono sulla stessa voce. TIC cambia la cadenza di tutta la Table; PIT e VL sono assegnazioni eseguite insieme agli FX.

Confronto. Sostituisci STP con HOP 00 per un loop continuo. Poi prova TIC 06 per raddoppiare il tempo fra gli stati.

Controllo. Una nuova nota riavvia la Table. Se scrivi CUT anche nella Phrase, la Table può prevalere nello stesso tick.


## E10 Aprire una mandata senza alzare il suono diretto

Preparazione. DUAL WT pluck. Master FX: delay 1/8D, feedback A0, ping-pong ON, delay return C0. Mixer T1 delay 00; riverbero return aperto e mandata 60.

```
00 C-4 00 DSN 00 RSN 60
04 G-4 00 DSN E0 --- 00
05 --- FF REP F0 --- 00
08 --- FF RTO 80 --- 00
0C --- FF DSN 00 --- 00
```

Da ascoltare. La prima nota è quasi asciutta; il Sol sulla 04 genera ripetizioni stereo. La mandata scende per riga e viene chiusa sulla 0C, ma gli echi già nel buffer continuano.

Perché succede. DSN controlla il segnale inviato alla linea, non il suo ritorno. REP/RTO automatizzano DSN perché si trovano in FX1; RSN della prima riga resta separato in FX2.

Confronto. Cambia soltanto RSN in D0 per un gesto ambient. Confronta lo stesso pattern con delay return 00, poi ripristinalo.

Controllo. Chiudere DSN non cancella gli echi; Stop invece azzera i buffer. Se non senti delay, controlla sia send sia return.


## E11 Cambiare il carattere FM senza scrivere nuove note

Preparazione. FM4 algoritmo 1 nell’editor, OP1 Ratio 1 Level FF, OP2 Ratio 2 Level A0, OP3/4 Level 00. Sustain aperto e TABLE FF.

```
00 C-3 00 FAL 00 FAI 20
04 --- FF FAI 80 OR2 03
08 --- FF FAI 40 OR2 02
0C --- FF FBK 10 --- 00
```

Da ascoltare. La portante resta sulla stessa nota; indice e rapporto di OP2 cambiano il timbro. OR2 03 seleziona rapporto 3; OR2 02 rapporto 2.

Perché succede. FAI regola la profondità FM comune; OR2 sceglie un indice della lista dei rapporti. FAL 00 corrisponde all’algoritmo 1 mostrato nell’editor.

Confronto. Alza OP3/4 e prova FAL 04 per due coppie parallele. Prima pareggia i livelli, così il cambio di volume non nasconde il timbro.

Controllo. FBK agisce su OP4: con OP4 a zero o fuori dal percorso udibile può non produrre differenze. Questo è intenzionale nella prima prova.


## E12 Scansione di due wavetable con movimento continuo

Preparazione. DUAL WT, CLASSIC/HOLLOW, MIX 80, Sustain C0. LFO1 SIN RATE 20 POS1 +16 POS2 -16; LFO2 neutro.

```
00 C-3 00 WTP 30 WT2 C0
04 --- FF WTP 60 WT2 90
08 --- FF WTP 90 WT2 60
0C --- FF WTP C0 WT2 30
```

Da ascoltare. Le due basi si muovono a gradini in direzioni opposte, con una piccola oscillazione continua attorno a ciascuna base.

Perché succede. WTP e WT2 impostano posizioni operative, non banchi. Le profondità LFO si sommano a quelle basi e vengono limitate agli estremi.

Confronto. Aggiungi una Table di pan, mantenendo PIT 0 e VL C0 su ogni riga, per separare percorso spettrale e spazio stereo.

Controllo. Il disegno delle onde nella prima pagina mostra le basi, non una animazione della modulazione in corso. MIX 00 nasconde OSC2.


## E13 Usare un pool esatto e cambiare il punto di ingresso

Preparazione. DUAL WT con Sustain C0, Global CHROMATIC. Table 00 LENGTH 8: PIT 0,+3,+7,+10 ripetuti due volte; VL B0 su tutte le righe. TIC 06 soltanto sulla riga 00.

```
PHRASE
00 C-4 00 TBL 00 SED 2A
01 --- FF THO 03 --- 00
02 --- FF RND 03 --- 00
04 --- FF RND 03 --- 00
08 --- FF RND 03 --- 00
0E OFF FF --- 00 --- 00

TABLE PIT
00 +00  01 +03  02 +07  03 +10
04 +00  05 +03  06 +07  07 +10
```

Da ascoltare. Le altezze restano Do, Mi♭, Sol e Si♭, perché il pool è scritto nel PIT della Table. THO e i successivi RND cambiano il punto da cui la lettura riprende, fra le righe 00 e 06; fra i salti la Table prosegue normalmente.

Perché succede. RND usa la memoria THO 03 nella propria colonna: il nibble basso varia di ±3, senza uscire dalle otto righe valide. La doppia copia del pool conserva gli stessi quattro gradi in ogni punto raggiungibile.

Confronto. Elimina SED dalla Phrase ripetuta per cambiare percorso a ogni giro. Sostituisci soltanto i PIT della Table per un nuovo pool; con Global attivo i gradi vengono ulteriormente quantizzati.

Controllo. THO cambia la lettura della Table, non sposta fisicamente le note nelle celle Phrase. Non è un fill euclideo automatico né un editor che riscrive il pattern.


# 12 Riferimento dei comandi FX

Il repertorio comprende 57 comandi operativi e la colonna vuota ---. Cerca prima la famiglia, poi la sigla. Ogni scheda offre due prove e indica cosa cambia nelle Table. L’indice alfabetico finale rimanda alle schede dei comandi. Per programmare usa sigla e valore.


## Note durata e percorso


### Colonna vuota

Parametro. Il valore viene ignorato.

La colonna non introduce un nuovo comando. Una riga con nota vuota conserva la voce in corso; non equivale a Note Off. Se nella stessa colonna è attivo un REP, il repeater continua anche quando compare ---.

Preparazione delle prove. SYNTH SAW, LP aperto, AMP Sustain C0, TABLE FF.

Prova A

```
00 C-4 00 CUT 20 --- 00
01 --- FF REP 04 --- 00
02 --- FF --- 00 --- 00
```

CUT parte da 20, passa a 24 sulla riga 01 e a 28 sulla riga 02. Per arrestare lo sweep inserisci REP 00 nella colonna FX1, non una colonna vuota.

Prova B

```
00 C-4 00 PAN 20 --- 00
01 --- FF --- 00 --- 00
02 --- FF REP 10 --- 00
04 --- FF REP 00 --- 00
```

PAN resta 20 sulla 01, poi passa a 30 sulla 02 e 40 sulla 03. REP 00 ferma il movimento. Le celle vuote non sono un reset.

Nelle Table. Vale anche per ciascuna delle tre colonne Table. Una riga Table vuota continua comunque ad applicare i propri PIT e VL: impostali intenzionalmente.

Da controllare. Una colonna vuota conserva la rampa della propria colonna, non quella della colonna accanto.


### DEL Ritardo della riga

Parametro. 00 immediato; 01–05 ritardo in tick; 06–FF riga saltata.

Rinvia l’intera riga Phrase, inclusi nota, strumento e secondo FX. Un tick è un sesto di riga. Non è un microtiming espresso in millisecondi e non mette in coda ritardi oltre la riga corrente. Se ci sono due DEL, prevale quello più a destra.

Preparazione delle prove. SAMPLE CR78 ClosedHat in I00, BPM 120.

Prova A

```
00 C-4 00 DEL 02 CUT A0
```

La nota e CUT A0 arrivano due tick dopo l’inizio della riga. A 120 BPM sono circa 41,7 ms. Un CHN che blocca DEL non annulla il ritardo già individuato: per ritardare una nota probabilistica usa DEL e valuta il gate sulla riga differita.

Prova B

```
00 C-4 00 --- 00 --- 00
02 C-4 00 DEL 01 --- 00
04 C-4 00 --- 00 --- 00
06 C-4 00 DEL 01 --- 00
```

Gli hi hat sulle righe 02 e 06 arrivano un tick dopo, circa 20,8 ms a 120 BPM. Ripeti lo stesso schema su 08–0E per uno shuffle leggero.

Nelle Table. Non implementato nelle Table. Un DEL inserito lì non ritarda né nota né automazioni; scegli TIC per cambiare la durata delle righe.

Da controllare. DEL 06 non dà un ritardo di una riga: sopprime quella riga. Il delay audio è un altro effetto, regolato da DSN.


### KIL Interruzione immediata o programmata

Parametro. 00 taglia subito; 01–FF attesa in tick.

Termina la voce senza usare la Release. È utile per gate corti, percussioni troncate e pause nette. Si riferisce alla voce della traccia, non al progetto intero. Una nuova nota può sostituire la voce e azzerare il kill programmato.

Preparazione delle prove. SYNTH PULSE, AMP Sustain C0, TABLE FF.

Prova A

```
00 C-4 00 KIL 03 --- 00
04 G-4 00 KIL 00 --- 00
```

La prima nota viene troncata dopo tre tick. La nota sulla riga 04 viene spenta prima di produrre audio utile. Se desideri una coda morbida usa una nota OFF o OFF 00 con ADSR attivo.

Prova B

```
00 C-3 00 KIL 01 --- 00
04 C-3 00 KIL 03 --- 00
08 C-3 00 KIL 05 --- 00
```

Le tre note durano nominalmente 1, 3 e 5 tick: circa 20,8, 62,5 e 104,2 ms a 120 BPM. Il taglio è netto, senza Release.

Nelle Table. Funziona sulla voce della traccia. Una volta spenta la voce, la Table non prosegue come sequencer indipendente.

Da controllare. Un KIL breve nasconde lo sweep del filtro o l’inviluppo lungo: prima scegli il gate, poi il timbro.


### OFF Rilascio o spegnimento differito

Parametro. 00 avvia il rilascio; 01–FF programma un kill dopo quel numero di tick.

Con ADSR attivo, OFF 00 entra nella fase Release dell’ampiezza e del cutoff. Con inviluppo legacy avvia invece il decadimento, usando il parametro DECAY. OFF con valore positivo non attende per avviare una Release: programma un taglio netto, come KIL.

Preparazione delle prove. SYNTH con AMP ON, Sustain C0 e Release 60.

Prova A

```
00 C-4 00 --- 00 --- 00
08 --- FF OFF 00 --- 00
```

La nota viene rilasciata sulla riga 08 senza introdurre un nuovo evento. Per una coda udibile imposta AMP ADSR ON, Sustain positivo e Release non nullo. Se il campione PCM è già finito, l’inviluppo non può prolungarne l’audio.

Prova B

```
00 C-4 00 --- 00 --- 00
08 OFF FF --- 00 --- 00
```

Questa volta la nota OFF rilascia sulla 08 e ferma anche Table e retrigger. Confrontala con FX OFF 00 della prova A; usa invece OFF 03 nel campo FX per un taglio dopo tre tick.

Nelle Table. Si applica alla voce in corso. Una nota OFF nella colonna NTE della Phrase ha in più una funzione esplicita di arresto della Table e cancellazione dei retrigger; non è perfettamente intercambiabile con FX OFF 00.

Da controllare. La nota OFF in NTE ferma anche Table e retrigger; il comando FX OFF 00 ha una gestione distinta. Non usarli come sinonimi in una Table.


### RET Retrigger e rampa di volume

Parametro. XY: Y>0 ripete ogni Y tick; Y=0 esegue un retrigger dopo X tick.

Con Y positivo riavvia la voce e modifica il volume a ogni ripetizione. X=0–7 sottrae rispettivamente 8,16,…64 unità; X=8–F aggiunge 8,16,…64. Il volume resta fra 00 e FF. Non c’è un X neutro nella modalità periodica. Il retrigger riparte dall’inizio di inviluppi e campione.

Preparazione delle prove. SYNTH NOISE o percussione lunga; AMP abbastanza aperto.

Prova A

```
00 C-4 00 RET 03 --- 00
04 C-4 00 RET 30 --- 00
```

RET 03 ripete ogni tre tick e scende di 8 unità per ripetizione. RET 30 programma un solo retrigger dopo tre tick, senza rampa periodica. Una nuova nota o una nota OFF cancella la programmazione precedente. RET 00 la disabilita.

Prova B

```
00 C-4 00 RET 82 --- 00
04 --- FF RET 00 --- 00
```

I retrigger distano due tick e aumentano di 8 unità il volume a ogni colpo, fino al limite FF. La 04 interrompe la ripetizione.

Nelle Table. Programma lo stesso retrigger della voce. Non basta a far risorgere un one shot che è già terminato: la ripetizione avviene soltanto se la voce è ancora attiva.

Da controllare. Con Y>0 non esiste una rampa neutra: 0 diminuisce e 8 aumenta. Un campione finito può non ripartire.


### PSL Portamento fra note

Parametro. 00 disabilita; 01–FF durata nominale in tick.

Fa scivolare l’intonazione corrente verso le note successive invece di saltare direttamente alla loro frequenza. È un glide lineare; il tempo viene stimato usando il BPM quando viene assegnata la nuova destinazione. Non è una legatura: un nuovo evento nota può riavviare inviluppi e Table.

Preparazione delle prove. SYNTH SAW, AMP A 00 D 20 S C0 R 20.

Prova A

```
00 C-4 00 PSL 06 --- 00
04 G-4 00 --- 00 --- 00
08 C-5 00 PSL 00 --- 00
```

La nota G4 viene raggiunta in circa una riga, cioè sei tick. Sulla riga 08 il glide viene disabilitato. A 120 BPM sei tick corrispondono a circa 125 ms. Vale anche per la velocità di lettura PCM.

Prova B

```
00 C-3 00 PSL 0C --- 00
04 G-3 00 --- 00 --- 00
08 C-4 00 --- 00 --- 00
```

Dalla seconda nota la frequenza scivola verso la destinazione in circa dodici tick, cioè 250 ms a 120 BPM. L’inviluppo riparte comunque.

Nelle Table. Si applica alla voce della traccia. Cambi di trasposizione della Table possono creare nuove destinazioni; la Table non aggiunge altre voci.

Da controllare. Non inserire PSL solo dopo la nota da far scivolare: impostalo prima o sulla sua riga; non confonderlo con una legatura senza retrigger.


### HOP Passaggio alla Phrase successiva

Parametro. 00–FE usa il nibble basso Y come riga 0–F; FF arresta la traccia.

Nella Phrase abbrevia il pattern: al confine successivo di riga passa alla prossima Phrase della Chain e riparte dalla riga Y. Alla fine della Chain passa alla riga Song successiva. Non cambia le altre tracce. HOP FF resta fermo fino a un nuovo avvio del trasporto.

Preparazione delle prove. Chain 00 con Phrase 00 e Phrase 01, LENGTH 2.

Prova A

```
07 --- FF HOP 00 --- 00
```

La Phrase corrente dura otto righe, da 00 a 07; poi inizia la Phrase successiva da 00. HOP 04 inizierebbe invece da 04. Prepara almeno due riferimenti validi nella Chain per riconoscere chiaramente il passaggio.

Prova B

```
PHRASE 00
00 C-3 00 --- 00 --- 00
07 --- FF HOP 00 --- 00
PHRASE 01
00 G-3 00 --- 00 --- 00
07 --- FF HOP 00 --- 00
```

Ogni Phrase occupa otto righe. Ascolti prima Do, poi Sol; il ciclo di Chain dura sedici righe totali.

Nelle Table. Significato diverso: HOP XY salta alla riga Y per X volte; X=0 significa senza limite. HOP 20 sulla riga 01 esegue due ritorni a 00, poi continua a 02. HOP FF non arresta la traccia nella Table: usa STP.

Da controllare. Il nibble alto di HOP non è un contatore nelle Phrase. Nelle Table HOP ha invece il significato di loop contato.


### JMP Salto nella Phrase corrente

Parametro. Nibble basso Y: riga 0–F.

Alla fine della riga Phrase corrente porta il cursore della sola traccia alla riga Y della stessa Phrase. È diverso da HOP, che passa alla Phrase successiva. Un salto alla stessa riga o all’indietro incrementa il contatore usato dalle condizioni sui giri.

Preparazione delle prove. Una Phrase con note sulle righe 00,02,04.

Prova A

```
07 --- FF JMP 00 --- 00
```

Ripete le prime otto righe della Phrase corrente senza arrivare alla successiva Chain o riga Song. Il trasporto delle altre tracce continua. Usa una condizione se desideri uscire dal loop dopo alcuni giri.

Prova B

```
00 C-3 00 --- 00 --- 00
02 E-3 00 --- 00 --- 00
04 G-3 00 JMP 00 --- 00
```

Suona un ciclo locale di cinque righe. Il resto della Phrase non viene raggiunto finché il salto resta attivo.

Nelle Table. Salta nella Table corrente senza contatore, in modo analogo a THO. Per un numero finito di ritorni usa HOP XY; non confondere i due sistemi di salto.

Da controllare. Il salto all’indietro incrementa il contatore dei giri e modifica il comportamento di CND/NTH.


### SNG Salto relativo nella Song

Parametro. Byte signed: 01 avanti di una riga, FF indietro di una, 00 riga corrente.

Alla fine della riga Phrase cambia la riga Song della traccia, azzerando posizione nella Chain e nella Phrase. Lo scostamento si riferisce alla riga Song corrente, non all’ID Chain. La destinazione usa il modulo 32; viene applicata solo se rientra nella lunghezza Song attiva.

Preparazione delle prove. Song LENGTH 2, T1 con Chain 00 e 01; ciascuna Chain ha una Phrase.

Prova A

```
PHRASE 00
07 --- FF SNG 01 --- 00
```

Dalla riga Song 00 salta alla 01 dopo la riga Phrase 07, poi riparte dalla Chain assegnata a quella cella. Il salto riguarda soltanto questa traccia. La prova B aggiunge il ritorno relativo dalla seconda Phrase.

Prova B

```
PHRASE 00
07 --- FF SNG 01 --- 00
PHRASE 01
07 --- FF SNG FF --- 00
```

Su quella traccia il primo salto avanza di una riga Song e il secondo torna indietro di una. Le altre tracce non saltano insieme.

Nelle Table. Non implementato come salto Song dalle Table. Inseriscilo in una Phrase; gli altri canali non sono costretti a seguire la stessa destinazione.

Da controllare. Il byte è relativo e signed. SNG 01 non significa sempre riga assoluta 01 e non funziona come salto Song dentro una Table.


### INS Cambio strumento con retrigger

Parametro. 00–1F ID Instrument; altri valori ignorati.

Sostituisce lo strumento della voce e la retriggera. È utile su una riga senza nuova nota per cambiare il timbro mantenendo l’altezza di base corrente. Non è identico a scrivere nota e strumento: non ricarica tutti i valori operativi di volume, cutoff, modello e regioni come fa un nuovo evento nota.

Preparazione della prova A. I00 SAW e I05 PULSE con livelli simili, nota sostenuta e nessuna Table. La prova B usa invece I01 PULSE.

Prova A

```
00 C-4 00 --- 00 --- 00
04 --- FF INS 05 --- 00
```

Alla riga 04 la voce viene riavviata usando lo strumento 05, ma può conservare parametri operativi della voce precedente. Se desideri richiamare integralmente il suono memorizzato, scrivi C-4 05 come nuovo evento e lascia INS vuoto.

Prova B

Preparazione. I00 SAW e I01 PULSE preparati con livelli simili.

```
00 C-4 00 --- 00 --- 00
04 --- FF INS 01 --- 00
```

Sulla 04 ripartono inviluppi e lettura di I01, mantenendo la nota corrente. INS può conservare modello e volume operativi della voce precedente: per passare sicuramente alla patch PULSE completa scrivi C4 con IN 01 come nuova nota.

Nelle Table. Può riavviare inviluppi e lettura PCM della voce. Va usato con cautela se la Table modifica STA/LEN o se vuoi un movimento continuo senza retrigger.

Da controllare. INS non è un semplice cambio di etichetta o una selezione del catalogo preset: riattiva il motore della voce.


## Altezza e armonia


### PIT Trasposizione relativa della voce

Parametro. Byte signed in semitoni; FF=−1, F4=−12, 0C=+12.

Aggiunge lo scostamento alla trasposizione già accumulata della traccia, limitata fra −96 e +96. PIT 00 aggiunge zero: non ripristina la tonalità originaria. La trasposizione locale resta sulle note successive fino a una compensazione o al riavvio del trasporto.

Preparazione delle prove. SYNTH con sustain, Global CHROMATIC.

Prova A

```
00 C-4 00 PIT 0C --- 00
04 C-4 00 PIT F4 --- 00
```

La prima nota suona un’ottava sopra. La seconda sottrae dodici semitoni e torna alla base. Ripetere PIT 0C senza compensazione continuerebbe ad alzare la trasposizione a ogni passaggio. Global Scale può quantizzare il risultato.

Prova B

```
00 C-4 00 PIT 00 --- 00
04 --- FF PIT 07 --- 00
08 --- FF PIT F9 --- 00
```

La voce va da Do a Sol e torna a Do: +7 seguito da -7. PIT accumula; PIT 00 sulla 08 non annullerebbe il +7.

Nelle Table. È ancora cumulativo. È distinto dal campo PIT della Table, che assegna invece uno scostamento assoluto per quella riga rispetto alla nota di base.

Da controllare. La trasposizione cumulativa può proseguire oltre la nota successiva; per l’esercizio riparti con Stop/Play.


### CHD Accordi e sovrapposizione su tre voci

Parametro. XY è una coppia di intervalli in semitoni esadecimali rispetto alla nota fondamentale; il comando riguarda la traccia selezionata in Poly 3 track. Su altre tracce non aggiunge voci.

47 crea una triade maggiore; 37 una minore; 57 un sus4. Con X o Y uguale a zero quella voce aggiuntiva è disabilitata. CHD 00 passa alle note indipendenti sovrapposte, senza interrompere le note già in corso. Il valore resta attivo finché viene cambiato; non serve riscriverlo a ogni nota.

Preparazione. Poly 3 track = T4, Phrase assegnata a T4, I00 pad con AMP ON, Sustain C0, Release 60, TABLE FF e scala CHROMATIC.

Prova A: accordi e coda

```
00 C-4 00 CHD 47 CUT 50
04 --- FF CUT 70 --- 00
08 F-4 00 CHD 37 --- 00
0C OFF FF --- 00 --- 00
```

La 00 suona Do maggiore e la 04 apre il filtro del gruppo. La 08 suona Fa minore; OFF sulla 0C avvia la Release di tutte le voci. Scegli una scala che ammetta le note desiderate, oppure CHROMATIC per mantenere esattamente gli intervalli.

Prova B: note indipendenti e mandata

```
00 C-4 00 CHD 00 DSN 90
04 E-4 00 --- 00 --- 00
08 G-4 00 --- 00 --- 00
0C --- FF KIL 00 --- 00
```

Con sustain aperto le tre note si sovrappongono. KIL 00 spegne il gruppo senza Release; le code già prodotte dal delay master possono continuare. Per un rilascio morbido sostituisci KIL con OFF 00.

Nelle Table. CHD non cambia la modalità polifonica: viene ignorato. Imposta gli intervalli nella Phrase e usa la Table per pitch, volume e trasformazioni della singola voce già attiva.

Da controllare. ARP alterna le altezze di una voce; CHD genera note simultanee. Il massimo è tre voci: l’arrivo di nuove note può sostituire voci ancora tenute o in Release. Per regolare il livello dell’intero accordo usa LEV; VOL può interessare soltanto la voce corrente.

### ARP Arpeggio monofonico a tre altezze

Parametro. XY: intervalli in semitoni +X e +Y; 00 disattiva.

Alterna nota base, base+X e base+Y. Sono tre intonazioni successive della stessa voce, non un accordo polifonico e non tre nuovi trigger degli inviluppi. La durata delle fasi si regola con ARC; la frequenza di aggiornamento rimane legata ai tick.

Preparazione delle prove. SYNTH con sustain e TABLE FF.

Prova A

```
00 C-4 00 ARP 47 ARC 02
```

La voce percorre C4, E4 e G4, dedicando circa due tick a ogni fase. ARP 37 produce invece C, E♭, G. Per una melodia più lunga o con volumi differenti per ogni altezza usa una Table.

Prova B

```
00 C-4 00 ARP 37 ARC 02
08 --- FF ARP 47 --- 00
0C --- FF ARP 00 --- 00
```

La triade minore diventa maggiore sulla 08 e si ferma sulla 0C. Gli inviluppi non ripartono a ogni altezza dell’arpeggio.

Nelle Table. Si somma alla trasposizione della Table. Se non vuoi sommare due arpeggi diversi, disabilita ARP con 00 prima di usare la sequenza PIT della Table.

Da controllare. ARP 00 ferma l’alternanza delle altezze. ARP lavora dentro una voce e non abilita o disabilita la polifonia; per gli accordi simultanei usa CHD sulla traccia scelta in Global.


### ARC Velocità dell’arpeggio

Parametro. Nibble basso Y: 1–F tick per fase; 0 trattato come 1. Nibble alto riservato.

Cambia la cadenza dell’ARP già attivo o impostato sulla stessa riga. Non definisce una nuova sequenza e non cambia i BPM del brano. Il firmware usa solo il nibble basso: ARC 12 e ARC 02 impostano la stessa velocità.

Preparazione delle prove. ARP 47 già impostato su una nota lunga.

Prova A

```
00 C-4 00 ARP 37 ARC 03
08 --- FF ARC 01 --- 00
```

L’arpeggio parte con tre tick per altezza e accelera a un tick sulla riga 08. La nota base resta la stessa, senza riavvio dell’inviluppo. L’effetto è ritmico e monofonico.

Prova B

```
00 C-4 00 ARP 47 ARC 06
04 --- FF ARC 03 --- 00
08 --- FF ARC 01 --- 00
```

Ogni altezza dura prima una riga, poi mezza riga e infine un tick. Non cambia il tempo della Song.

Nelle Table. Controlla sempre l’arpeggiatore della voce, non la velocità con cui vengono lette le righe Table. Per le righe Table serve TIC.

Da controllare. Solo il nibble basso conta; ARC 10 non significa sedici tick, ma Y=0 trattato come uno.


### PBN Deriva progressiva di intonazione

Parametro. Byte signed in sedicesimi di semitono per tick; 00 ferma la deriva.

Accumula una salita o discesa di pitch. Il valore 10 aggiunge un semitono per tick; F0 lo sottrae. Il percorso accumulato è limitato a circa ±96 semitoni. Il motore applica questo comando con risoluzione a tick e intonazione a gradini di semitono, non come pitch bend continuo ad alta risoluzione.

Preparazione delle prove. SYNTH con sustain, Global CHROMATIC.

Prova A

```
00 C-4 00 PBN 01 --- 00
08 --- FF PBN 00 --- 00
```

Con 01 l’accumulatore sale di un sedicesimo di semitono a tick; la nota cambia altezza a scalini. PBN 00 interrompe la salita ma conserva lo scostamento raggiunto. Una nuova nota azzera l’accumulatore; il valore di deriva può restare attivo fino a PBN 00.

Prova B

```
00 C-4 00 PBN 01 --- 00
08 --- FF PBN 00 --- 00
```

Il pitch sale a piccoli incrementi interni ma diventa udibile a gradini di semitono. Sulla 08 si ferma la deriva, conservando lo scostamento accumulato.

Nelle Table. Agisce sulla stessa intonazione della voce e si somma a PIT, ARP e PIT della Table. Per una modulazione fluida e periodica usa LFO PITCH.

Da controllare. PBN 00 non riporta automaticamente l’intonazione alla nota di partenza.


### PVB Vibrato a tick

Parametro. XY: X incremento della fase, Y profondità; 00 disattiva.

Modula l’altezza con una sinusoide campionata ai tick. Aumentare X accelera il movimento; aumentare Y ne aumenta l’ampiezza. La variazione viene quantizzata in semitoni prima del motore: profondità molto piccole possono risultare poco udibili. Non è il vibrato continuo dei due LFO Instrument.

Preparazione delle prove. SYNTH sostenuto, nessuna modulazione pitch LFO.

Prova A

```
00 C-4 00 PVB 4C --- 00
08 --- FF PVB 00 --- 00
```

Applica un vibrato marcato con velocità 4 e profondità C, poi lo elimina alla riga 08. La cadenza segue i BPM perché l’aggiornamento è ai tick. Se vuoi un vibrato lento e sottile, scegli LFO 1 → PITCH dalla pagina Modulazioni.

Prova B

```
00 C-4 00 PVB 6F --- 00
08 --- FF PVB 00 --- 00
```

Vibrato aggiornato a tick, con velocità 6 e profondità F. La 08 lo disattiva. Prova un valore più basso dopo aver riconosciuto l’effetto.

Nelle Table. La velocità Table non sostituisce la cadenza a tick interna del vibrato. Il comando cambia i parametri del vibrato della voce, non genera note aggiuntive.

Da controllare. Questo vibrato non è l’LFO continuo di Instrument e la sua profondità è quantizzata.


### SCA Scala locale della traccia

Parametro. XY: X tonica 0=C…B=B; Y=1 maggiore, Y=2 minore naturale; Y=0 segue Global.

Imposta una quantizzazione locale per la traccia. Le note non appartenenti alla scala vengono abbassate al grado ammesso precedente. Le scale locali maggiore e minore prevalgono su Global. I nibble di tonica validi sono 0–B; evita C–F.

Preparazione delle prove. Global CHROMATIC e una sola traccia di prova.

Prova A

```
00 C-4 00 SCA 22 --- 00
08 --- FF SCA 00 --- 00
```

SCA 22 imposta Re minore naturale sulla traccia. SCA 00 torna a seguire la scala Global: non forza il cromatismo se Global è non cromatica. Per Dorian, Lydian e gli altri modi usa Global. I dati nota della Phrase restano quelli scritti.

Prova B

```
00 C#4 00 SCA 01 --- 00
04 D#4 00 --- 00 --- 00
08 C#4 00 SCA 00 --- 00
```

SCA 01 impone Do maggiore: C# scende a C e D# a D. SCA 00 torna alla scala Global, qui cromatica.

Nelle Table. Continua a controllare la scala locale della traccia. La quantizzazione viene applicata al pitch risultante, inclusa la trasposizione della Table.

Da controllare. La quantizzazione sceglie una nota ammessa inferiore; non traspone una melodia mantenendone tutti gli intervalli.


### SCG Scala locale per tutte le tracce

Parametro. Stessa codifica XY di SCA.

Assegna simultaneamente il valore SCA alle otto voci di traccia. Non cambia il campo Scala mostrato in Global: è uno stato di esecuzione delle voci, azzerato al riavvio del trasporto. Può essere utile per un cambio armonico comune senza riscrivere otto Phrase.

Preparazione delle prove. Due tracce synth con note cromatiche; lascia fuori la batteria per il confronto.

Prova A

```
00 C-4 00 SCG 01 --- 00
08 --- FF SCG 00 --- 00
```

SCG 01 applica Do maggiore a tutte le tracce; SCG 00 restituisce tutte alla scala Global. Anche le note successive dei campioni possono essere quantizzate: per le percussioni verifica che l’altezza di riferimento non venga spostata involontariamente.

Prova B

```
00 C-4 00 SCG 92 --- 00
08 --- FF SCG 00 --- 00
```

Tutte le tracce ricevono La minore locale, X=9 e Y=2. La 08 le riporta a Global.

Nelle Table. Una Table di una sola traccia può agire sulle altre sette. Evita comandi SCA/SCG concorrenti se non vuoi che l’ordine delle tracce determini quale impostazione prevale.

Da controllare. SCG influenza anche le tracce campione e può cambiarne la velocità di lettura: usalo con cautela su una batteria.


### TSP Trasposizione globale

Parametro. Byte signed in semitoni; 00 torna a zero.

Imposta una trasposizione globale assoluta che si somma al pitch delle otto tracce. A differenza di PIT, non accumula: due TSP 0C consecutivi mantengono +12, non +24. La scala può quantizzare il risultato. Non sposta la tonica visualizzata in Global.

Preparazione delle prove. Due tracce SYNTH e Global CHROMATIC.

Prova A

```
00 C-4 00 TSP 0C --- 00
08 --- FF TSP 00 --- 00
```

Tutto il brano viene alzato di un’ottava e poi torna alla base. La lettura dei campioni cambia velocità e altezza insieme: anche le percussioni vengono trasposte. Il riavvio del trasporto azzera TSP.

Prova B

```
00 C-4 00 TSP 00 --- 00
08 --- FF TSP 0C --- 00
```

Da metà Phrase tutte le tracce sono un’ottava sopra. TSP F4 le porterebbe un’ottava sotto, TSP 00 ripristina la base globale.

Nelle Table. Resta globale. Usa il campo PIT della Table per spostare soltanto la sua voce senza trasporre il resto del brano.

Da controllare. A differenza di PIT, TSP è assoluto e globale. Anche i campioni seguono la trasposizione.


## Condizioni e casualità


### CHA Probabilità dei lati della riga

Parametro. Phrase XY: X e Y sono probabilità 0–F; F sempre, 0 mai.

Controlla separatamente gli eventi a sinistra e a destra del comando. In FX1 il lato sinistro comprende nota e strumento; il lato destro comprende FX2. In FX2 il lato sinistro comprende anche FX1. Le probabilità sono X/15 e Y/15; 8 vale circa 53%, non esattamente metà.

Preparazione delle prove. SAMPLE snare in I00 e nessuna Table.

Prova A

```
00 C-4 00 CHA 8F PAN E0
04 E-4 00 CUT A0 CHA 0F
```

Nella prima riga la nota ha circa il 53% di probabilità, ma PAN E0 passa sempre. Nella seconda riga nota e CUT vengono bloccati. Bloccare il trigger conserva l’eventuale voce precedente: non crea automaticamente silenzio.

Prova B

```
04 C-4 00 CHA FF VOL C0
0C C-4 00 CHA 4F VOL 70
```

La snare sulla 04 scatta sempre; sulla 0C il trigger passa circa 4/15 delle volte. VOL 70 passa comunque: può modificare una voce precedente ancora attiva.

Nelle Table. Usa l’intero byte come probabilità XX/255 e controlla solo ciò che è a sinistra, inclusi PIT e VL. Non applicare alla Table la lettura X/15 e Y/15 propria delle Phrase.

Da controllare. CHA 80 non significa probabilità del byte 128/255 nella Phrase: decide separatamente i due lati 8 e 0.


### CHN Probabilità dell’evento immediatamente a sinistra

Parametro. 00–FF probabilità XX/255; 00 mai, FF sempre.

In FX1 decide se eseguire nota e strumento; in FX2 decide se eseguire il solo FX1. Non controlla tutta la riga e non controlla il comando alla sua destra. 80 è circa il 50%. È utile per rendere probabile una nota o una singola automazione mantenendo il resto regolare.

Preparazione delle prove. SAMPLE hat I00 e pan udibile in stereo.

Prova A

```
00 C-4 00 CHN 80 PAN 20
04 E-4 00 CUT C0 CHN 80
```

Nella prima riga la nota è probabile e PAN passa sempre. Nella seconda la nota passa sempre e soltanto CUT è probabile. Le decisioni di gate vengono risolte prima delle azioni: puoi condizionare anche un salto posto a sinistra.

Prova B

```
00 C-4 00 CHN FF PAN 20
04 C-4 00 CHN 00 PAN E0
```

La prima nota passa e la seconda no; il pan viene comunque aggiornato in entrambe. È un confronto deterministico prima di provare CHN 80.

Nelle Table. In FX1 controlla PIT/VL; negli altri FX controlla il comando immediatamente a sinistra. Non attribuire a CHN lo stesso comportamento di CHA o CND.

Da controllare. In FX2 CHN condiziona soltanto FX1. Non decide allora se suonare o meno la nota.


### CND Condizione sul giro

Parametro. AB con A e B fra 1 e F e A≤B.

Consente l’intera riga soltanto nel giro A di ogni gruppo di B giri. Il primo giro usa il contatore zero, quindi 12 significa primo di due e 22 secondo di due. Un valore con A=0, B=0 o A>B non soddisfa mai la condizione.

Preparazione delle prove. Una sola Phrase ripetuta, SAMPLE snare I00.

Prova A

```
00 C-4 00 CND 12 --- 00
04 G-4 00 CND 22 --- 00
```

La prima riga scatta sui giri 1, 3, 5; la seconda sui giri 2, 4, 6. Il contatore appartiene alla traccia e avanza a ogni fine Phrase o salto locale all’indietro: non è un contatore separato per ciascun ID Phrase. Stop e Play lo azzerano.

Prova B

```
04 C-4 00 CND 14 --- 00
0C C-4 00 CND 44 RET 03
```

La 04 suona nel primo giro su quattro; la 0C e il suo roll passano nel quarto. Riparti con Stop/Play per riallineare il contatore.

Nelle Table. Usa il contatore dei giri della Table, che avanza al ritorno alla prima riga o con salti all’indietro. Una condizione fallita non impedisce al cursore Table di avanzare.

Da controllare. Un salto locale all’indietro incrementa i giri: con JMP il concetto di quarto giro può cambiare.


### PRV Condizione sull’esito precedente

Parametro. 00 richiede esito falso; 01 richiede vero. Ogni valore non nullo equivale a vero.

Legge l’esito logico della riga Phrase precedente: il consenso al trigger dopo i gate. Non controlla se il suono è ancora attivo, se il campione ha finito o se hai effettivamente udito una nota. Anche una riga senza nota può registrare esito vero.

Preparazione delle prove. SAMPLE hat I00 e snare I01; usa righe adiacenti.

Prova A

```
00 C-4 00 CHN 80 --- 00
01 G-4 00 PRV 00 --- 00
```

G4 passa se il trigger della riga 00 è stato rifiutato. Se C4 è passato, G4 viene bloccato. Un CND fallito registra esito falso. Questo permette risposte alternate a eventi probabilistici, non un test sull’ampiezza audio.

Prova B

```
00 C-4 00 CHN 80 --- 00
01 C-4 01 PRV 00 --- 00
```

Se il primo trigger è rifiutato, la snare risponde un sedicesimo dopo. Se passa, la seconda riga è bloccata.

Nelle Table. Legge ancora la storia delle Phrase della traccia. Le righe Table non riscrivono PRV: non usarlo come memoria dell’esito della riga Table precedente.

Da controllare. Una riga vuota intermedia può aggiornare PRV: la risposta deve leggere davvero l’esito della riga desiderata.


### NTH Esecuzione periodica dei lati

Parametro. XY: lato sinistro ogni X giri, lato destro ogni Y; 0 sempre.

Applica una condizione periodica ai lati del comando, con la stessa suddivisione spaziale di CHA nelle Phrase. Il contatore parte da zero: con X=2 il lato passa al primo, terzo, quinto giro. Non significa “soltanto al secondo giro”. Per selezionare il giro A di B usa CND AB.

Preparazione delle prove. Un’unica Phrase ripetuta, SAMPLE snare I00.

Prova A

```
00 C-4 00 NTH 23 CUT C0
```

Nota e strumento passano sui giri 1,3,5,…; CUT passa sui giri 1,4,7,… . I due lati possono quindi agire separatamente. Il contatore appartiene alla traccia e segue anche i salti all’indietro, come spiegato per CND.

Prova B

```
04 C-4 00 NTH 24 RSN 80
```

La nota a sinistra passa ogni due giri, il send a destra ogni quattro. Il contatore iniziale è zero: entrambi passano già nel primo giro.

Nelle Table. Usa il contatore Table e controlla il lato sinistro; il lato destro non riceve il gate separato delle Phrase. NTH 00 lascia sempre passare i lati, ma non annulla altri gate presenti.

Da controllare. NTH 24 non significa secondo giro su quattro come CND 24: X e Y sono due divisori indipendenti.


### RNL Variazione dell’evento a sinistra

Parametro. XY: profondità X per nota o nibble alto, Y per strumento o nibble basso.

In FX1 modifica una copia della nota di ±X semitoni e dello strumento di ±Y slot, entro i limiti validi. In FX2 varia i due nibble del valore di FX1, invece di cercare un comando ricordato. La trasformazione avviene sulla copia eseguita: i dati scritti restano invariati.

Preparazione della prova A. I00 SYNTH PULSE, Global CHROMATIC, TABLE FF. La prova B attiva invece C MIN PENT.

Prova A

```
00 C-4 00 RNL 30 SED 2A
04 C-4 00 CUT 80 RNL 40
```

La prima riga sceglie una nota fra A3 ed E♭4, lasciando lo strumento 00 invariato. La seconda varia CUT 80 fra 40 e C0 a passi esadecimali di 10. Per melodie in tonalità attiva una scala Global; la quantizzazione segue la variazione.

Prova B

Preparazione. I00 SYNTH PULSE, scala Global C MIN PENT per contenere le altezze.

```
00 C-4 00 RNL 20 SED 2A
04 C-4 00 RNL 20 --- 00
08 C-4 00 RNL 20 --- 00
```

RNL in FX1 varia solo la nota di ±2 semitoni; Y=0 impedisce cambi di strumento. La scala quantizza poi il risultato. Il seme rende ripetibile la successione.

Nelle Table. Nel primo FX varia PIT di ±X semitoni e VL di ±Y unità; negli altri FX modifica il valore del comando immediatamente precedente. Non cambia strumento attraverso la colonna PIT.

Da controllare. Y diverso da zero varia anche lo slot Instrument e può richiamare suoni non preparati.


### SED Inizializzazione del generatore casuale

Parametro. 00–FF seme del generatore della traccia.

Rende ripetibili le estrazioni successive di CHA, CHN, RND e RNL sulla traccia. Ogni traccia ha un generatore indipendente. SED viene letto prima delle condizioni e delle estrazioni della riga, anche quando è in FX2 o quando un gate della riga fallisce.

Preparazione delle prove. Usa la ricetta RNL appena sopra, con un solo generatore sulla traccia.

Prova A

```
00 C-4 00 RNL 50 SED 2A
04 C-4 00 RNL 50 --- 00
```

A parità di contesto le due estrazioni riproducono la stessa successione a ogni ritorno sulla riga 00. Spostando SED fuori dal loop la sequenza continua invece a evolvere. Cambiare numero o ordine delle estrazioni sulla stessa traccia cambia la successione successiva.

Prova B

```
00 C-4 00 RNL 30 SED 11
04 C-4 00 RNL 30 --- 00
08 C-4 00 RNL 30 --- 00
```

Ripetendo il giro ricompare lo stesso disegno. Cambia soltanto SED 11 in SED 12 per confrontare una seconda sequenza deterministica.

Nelle Table. Condivide il generatore della propria traccia con le Phrase. Le estrazioni della Table influenzano quelle successive della Phrase sulla stessa traccia; non influenzano le altre tracce.

Da controllare. Aggiungere CHN, RND o altre estrazioni sulla stessa traccia cambia il consumo del generatore e quindi la sequenza.


## Memorie e progressioni


### RND Variazione casuale del comando ricordato

Parametro. XY: ampiezza simmetrica del nibble alto X e del basso Y.

Riprende l’ultimo FX operativo memorizzato nella stessa colonna, ne varia i due nibble e applica il risultato per quella riga. Ciascun nibble viene limitato fra 0 e F. Non modifica la Phrase salvata né il valore di riferimento ricordato. Non varia automaticamente il comando della colonna accanto.

Preparazione delle prove. SYNTH DUAL WT, OSC MIX 00, TABLE FF, LFO POS neutri.

Prova A

```
00 C-4 00 CUT 80 --- 00
01 --- FF RND 40 --- 00
02 --- FF RND 40 --- 00
```

Ogni RND sceglie un cutoff fra 40 e C0 a passi di 10 esadecimale, ripartendo dal riferimento 80. Non è una passeggiata casuale cumulativa. RND 00 riapplica il riferimento senza scostamento. Serve prima un comando operativo nella colonna.

Prova B

```
00 C-4 00 WTP 80 --- 00
04 --- FF RND 20 --- 00
08 --- FF RND 20 --- 00
0C --- FF RND 20 --- 00
```

Le posizioni possibili sono 60, 70, 80, 90 e A0. Ogni estrazione riparte da 80; non si accumula sulla precedente.

Nelle Table. Le tre memorie delle Table sono separate dalle due delle Phrase. Un RND nella Table non riprende il CUT memorizzato in una Phrase.

Da controllare. RND in FX2 non trova il WTP scritto in FX1. Conserva tutti e quattro gli eventi nella stessa colonna.


### REP Ripetizione con incremento

Parametro. Byte signed: 01–7F aumenta, 80–FF diminuisce, 00 arresta.

Attiva una progressione dell’ultimo FX operativo ricordato nella stessa colonna. L’incremento si applica già sulla riga REP e sulle successive righe vuote della colonna. I valori si fermano a 00 o FF, oppure al limite impostato da RTO. Un nuovo comando operativo sostituisce la memoria e ferma il repeater.

Preparazione delle prove. DUAL WT, OSC MIX 00, AMP Sustain C0, TABLE FF.

Prova A

```
00 C-4 00 CUT 20 --- 00
01 --- FF REP 08 --- 00
02 --- FF --- 00 --- 00
03 --- FF RTO 40 --- 00
```

CUT assume 20, 28, 30 e 38; il limite 40 impostato sulla riga 03 viene raggiunto alla riga 04. REP F8 scende di 8, non di 248. La riga vuota non interrompe la progressione; REP 00 sì.

Prova B

```
00 C-4 00 WTP 20 --- 00
01 --- FF REP 10 --- 00
04 --- FF RTO 80 --- 00
08 --- FF REP 00 --- 00
```

POS1 percorre 20,30,40,50,60,70,80, poi resta a 80. Il limite si imposta sulla 04 e viene raggiunto sulla 06.

Nelle Table. Avanza una volta per riga Table, quindi la velocità dipende da TIC. Ogni colonna Table ha il proprio repeater. I gate possono impedire l’esecuzione di una colonna su quella riga.

Da controllare. Una nuova nota può ricaricare la posizione Instrument anche mentre la colonna continua il suo repeater.


### RTO Limite del repeater

Parametro. 00–FF limite assoluto per il REP della stessa colonna.

Imposta un punto di arresto per il repeater già attivo. Non imposta il cutoff o il volume direttamente e non avvia REP da solo. Sulla riga RTO la progressione compie ancora un passo; quando raggiunge o supera il limite nella direzione del movimento viene fermata esattamente a quel valore.

Preparazione delle prove. SYNTH con sustain; TABLE FF.

Prova A

```
00 C-4 00 CUT 20 --- 00
01 --- FF REP 10 --- 00
02 --- FF RTO 60 --- 00
```

Il cutoff assume 20, 30 e 40 sulle tre righe mostrate; prosegue a 50 e poi 60, dove si ferma. Per una discesa poni un limite inferiore al riferimento e usa un incremento signed negativo. Un nuovo REP rimuove il limite precedente.

Prova B

```
00 C-4 00 PAN C0 --- 00
01 --- FF REP F0 --- 00
03 --- FF RTO 80 --- 00
```

Il pan scende di 10 esadecimale: C0,B0,A0,90,80. RTO 80 è un limite raggiunto sulla 04, non un salto immediato a 80.

Nelle Table. Il limite appartiene alla singola colonna Table. Inserire RTO in FX2 non limita un REP attivo in FX1.

Da controllare. Un limite nella direzione opposta può fermare la rampa in modo inatteso. Per scendere parti sopra il limite.


## Table e tempo


### TBL Selezione e riavvio della Table

Parametro. 00–0F ID Table; 10–FF non selezionano una Table valida.

Attiva la Table indicata dalla riga 00 e ne azzera contatori di salto e memorie FX. Può sostituire quella assegnata allo strumento. Una nuova nota riprende prima l’assegnazione Instrument: per richiamare sempre una Table diversa, usa TBL sulla stessa riga del trigger.

Preparazione della prova A. I00 SYNTH con Sustain C0. Prepara Table 02 LENGTH 4, PIT 0,+4,+7,+12 e VL C0; TIC 03 sulla riga 00 e HOP 00 sulla 03.

Prova A

```
00 C-4 00 TBL 02 --- 00
```

Lo strumento 00 suona e la Table 02 inizia dal principio, anche se il campo TABLE dello strumento è FF. Per disattivare la Table usa STP; TBL FF non è un comando di spegnimento.

Prova B

Preparazione. Prepara Table 00 con PIT 0,+7 e HOP 00; Table 01 con PIT 0,+12 e HOP 00.

```
00 C-4 00 TBL 00 --- 00
08 --- FF TBL 01 --- 00
```

La nota non viene ritiggerata sulla 08; cambia invece il piccolo programma che la modifica. Le memorie della nuova Table ripartono.

Nelle Table. Permette di passare a un’altra Table. Il nuovo contenuto parte al tick successivo, non viene eseguito ricorsivamente nello stesso tick. Un TBL ripetuto riparte sempre da 00.

Da controllare. Una nuova nota può riavviare la Table assegnata nello strumento: colloca TBL sulla sua riga se vuoi sostituirla.


### THO Salto a una riga della Table

Parametro. Usa il nibble basso Y come riga 0–F.

Sposta la lettura all’interno della Table corrente senza selezionarne un’altra. Serve una Table attiva e una voce ancora in esecuzione. Non riavvia nota, inviluppi o campione. Il passaggio viene consumato durante l’elaborazione della Table, dopo la riga Table corrente.

Preparazione della prova A. I00 SYNTH sostenuto. Table 02 LENGTH 16, PIT da 0 a +15 semitoni decimali, VL C0 su ogni riga e TIC 06 sulla 00. La riga 08 produce +8.

Prova A

```
00 C-4 00 TBL 02 --- 00
04 --- FF THO 08 --- 00
```

Sulla riga Phrase 04 la Table 02 proseguirà dalla sua riga 08 alla successiva occasione utile. Se la Table è congelata con TIC 00, riattivala con un TIC positivo per consumare il salto.

Prova B

Preparazione. Table 00 con quattro righe riconoscibili, nota lunga attiva.

```
00 C-4 00 TBL 00 TIC 06
04 --- FF THO 02 --- 00
```

La Table prosegue dalla riga 02 al successivo aggiornamento utile. THO non sceglie la Table 02: sceglie la riga 02 di quella attiva.

Nelle Table. Salta alla riga Y dopo avere eseguito i parametri e gli FX della riga corrente. Non ha il contatore di ripetizioni di HOP XY.

Da controllare. Un TIC 00 congela la lettura; prima riattivala con un TIC positivo.


### TIC Durata delle righe Table

Parametro. 01–FF tick per riga; 00 congela la lettura.

Imposta la durata delle righe della Table della traccia. Non cambia i sei tick per riga Phrase. A ogni nuova nota la velocità Table riparte da un tick, salvo TIC sulla stessa riga o dentro la Table. Un’attesa già avviata può terminare prima che una nuova velocità diventi udibile.

Preparazione della prova A. I00 SYNTH sostenuto. Table 02 LENGTH 4, PIT 0,+4,+7,+12 e VL C0; HOP 00 sulla 03. Lascia gli altri FX Table vuoti, così TIC della Phrase resta il solo controllo della cadenza.

Prova A

```
00 C-4 00 TBL 02 TIC 03
08 --- FF TIC 00 --- 00
```

La Table 02 avanza ogni tre tick, quindi due righe Table per riga Phrase. Alla riga 08 si congela sul valore raggiunto: la nota continua. Un TIC successivo positivo riprende la lettura. A 120 BPM TIC 03 dura circa 62,5 ms.

Prova B

Preparazione. Table 00 di quattro altezze in loop e sustain aperto.

```
00 C-4 00 TBL 00 TIC 06
04 --- FF TIC 03 --- 00
08 --- FF TIC 01 --- 00
```

La Table accelera da una riga per riga Phrase a due e poi sei. L’esatto primo confine dipende dal conto alla rovescia già in corso.

Nelle Table. Se inserito nella prima riga Table, regola anche le righe successive. TIC FF vale 255 tick, non una modalità automatica o ad altissima frequenza.

Da controllare. TIC non cambia ARC, BPM o durata delle righe Phrase. Tutte le colonne Table condividono la stessa cadenza.


### STP Arresto della Table

Parametro. Il byte viene ignorato; usa convenzionalmente 00.

Disattiva la Table della traccia. Non ferma il trasporto e non spegne la nota: l’ultimo cutoff, pan o volume impostato può restare sulla voce. Non è uno Stop globale. Un nuovo trigger nota può riattivare la Table assegnata allo strumento.

Preparazione delle prove. Table 00 attiva e SYNTH con sustain.

Prova A

```
00 C-4 00 TBL 00 --- 00
08 --- FF STP 00 --- 00
```

La Table muove il suono fino alla riga 08, poi la voce resta sullo stato raggiunto. Per riprenderla dal principio usa TBL 00. Per fermare anche la nota scegli una nota OFF o KIL, secondo la coda desiderata.

Prova B

```
00 C-4 00 TBL 00 --- 00
08 --- FF STP 00 --- 00
```

La Table si ferma sulla 08, ma la nota continua con i valori già raggiunti. Un nuovo trigger può riavviare la Table automatica.

Nelle Table. Consente di costruire una Table a esecuzione singola: scrivi STP sull’ultima riga desiderata. Le altre colonne di quella riga possono ancora essere elaborate: tienile vuote se non servono.

Da controllare. STP non cancella gli FX già applicati e non è il pulsante Stop del trasporto.


### TPO Tempo globale

Parametro. 1E–FF significa 30–255 BPM; valori inferiori vengono limitati a 30.

Imposta il BPM di tutto il progetto, anche se il comando si trova su una sola traccia. Il valore è esadecimale, mentre il campo BPM di Global si legge normalmente in decimale. Le durate musicali del delay seguono il BPM. TPO modifica anche il BPM del progetto in RAM.

Preparazione delle prove. Solo una traccia deve scrivere il tempo, per evitare conflitti.

Prova A

```
00 C-4 00 TPO 78 --- 00
08 --- FF TPO 60 --- 00
```

Il brano parte a 120 BPM e passa a 96 BPM. Per 108 BPM usa 6C. Per 256–300 BPM usa Global: non entrano in un byte FX. Se salvi il progetto dopo TPO, salvi il BPM corrente; Stop non ripristina un BPM precedente.

Prova B

```
00 C-4 00 TPO 78 --- 00
04 --- FF TPO 90 --- 00
08 --- FF TPO A0 --- 00
```

Il brano accelera da 120 a 144 e poi 160 BPM. Anche il delay sincronizzato segue il nuovo tempo. Global mostra gli stessi BPM in decimale.

Nelle Table. Resta globale: una Table di una sola traccia può cambiare il tempo di tutte. Evita più TPO concorrenti se vuoi un risultato facile da prevedere.

Da controllare. TPO FF vale 255 BPM; Global consente fino a 300 ma un byte FX non li rappresenta. Stop non ripristina il BPM precedente.


## Volume filtro mixer e campioni


### VOL Volume della voce

Parametro. 00–FF livello assoluto; 00 muto, FF massimo.

Agisce sulla voce corrente prima del mixer e delle mandate. Non è un parametro velocity relativo al volume Instrument. Su una nuova nota viene prima ricaricato il volume Instrument e poi applicato VOL, se presente. Non riscrive i parametri del preset.

Preparazione delle prove. I00 SYNTH con sustain; Mixer LEV stabile.

Prova A

```
00 C-4 00 VOL C0 --- 00
04 --- FF VOL 40 --- 00
```

La stessa nota scende da 192 a 64 senza retrigger. Il livello finale dipende anche da inviluppo, LFO AMP e LEV del mixer. Per un fade dell’intera traccia, persistente fra note successive, usa LEV o il relativo repeater.

Prova B

```
00 C-4 00 VOL C0 --- 00
04 --- FF VOL 60 --- 00
08 --- FF VOL 20 --- 00
```

La voce scende di livello senza cambiare il fader della traccia. Una nuova nota riprende il volume Instrument.

Nelle Table. Può essere sovrascritto dal VL della riga Table successiva. Ogni riga Table applica un VL assoluto; tienine conto quando combini Table e automazioni Phrase.

Da controllare. VOL non è LEV: se vuoi conservare una riduzione fra note nuove, automatizza il mixer con LEV.


### CUT Apertura del filtro

Parametro. 00–FF valore assoluto del cutoff della voce.

Imposta la base del filtro della voce in esecuzione. Il byte non esprime hertz e la risposta dipende dal tipo di filtro. L’inviluppo cutoff e gli LFO si sommano alla base: un CUT fisso può quindi produrre comunque movimento. Una nuova nota riprende la base Instrument, poi applica gli FX della nuova riga.

Preparazione delle prove. SYNTH SAW, filtro LP, CUT ENV OFF e LFO CUT neutri.

Prova A

```
00 C-4 00 CUT 30 --- 00
04 --- FF CUT C0 --- 00
```

La nota parte scura e si apre sulla riga 04 senza retrigger. Per sentire nettamente la differenza scegli filtro LP, disattiva temporaneamente CUT ENV e le modulazioni del cutoff. CUT non riscrive il preset dello strumento.

Prova B

```
00 C-3 00 CUT 20 --- 00
04 --- FF CUT 60 --- 00
08 --- FF CUT A0 --- 00
0C --- FF CUT E0 --- 00
```

La stessa nota si apre in quattro gradini, senza ripartire. Con una nuova nota sulla 08 il filtro riprenderebbe la base prima del CUT di quella riga.

Nelle Table. Utilissimo per contorni del filtro a gradini. Se Phrase e Table scrivono CUT nello stesso tick, la Table viene eseguita dopo e può prevalere.

Da controllare. Cutoff 20 è un valore interno, non 32 Hz. LP e HP producono risultati diversi.


### PWM Larghezza dell’impulso

Parametro. 00–FF soglia assoluta dell’oscillatore PULSE.

Cambia il rapporto fra la parte alta e bassa dell’onda impulsiva. 80 è vicino al 50%; valori come 20 e E0 producono impulsi stretti e timbri diversi. Ha un effetto diretto sul modello PULSE; non è un parametro generico di tutti gli oscillatori o del campionatore.

Preparazione delle prove. SYNTH BASIC PULSE; AMP Sustain C0.

Prova A

```
00 C-4 00 MDL 01 PWM 30
08 --- FF PWM C0 --- 00
```

La riga 00 seleziona PULSE e imposta un impulso stretto. Sulla riga 08 cambia il duty cycle senza retrigger. PWM 00 può portare a una componente quasi costante: preferisci valori lontani dagli estremi durante le prime prove.

Prova B

```
00 C-3 00 PWM 20 --- 00
04 --- FF PWM 80 --- 00
08 --- FF PWM E0 --- 00
```

La larghezza dell’impulso passa da sottile a simmetrica e torna sottile sul lato opposto. Mantieni il modello PULSE per il confronto.

Nelle Table. Permette una sequenza di timbri per riga, oppure uno sweep con REP. Una nuova nota ricarica la pulse width Instrument prima degli FX della propria riga.

Da controllare. Non usare PWM come comando generico per i modelli Braids o il dual wavetable: lì servono TIM/COL o WTP/WT2.


### LEV Livello del mixer della traccia

Parametro. 00–FF; 00 muto, FF massimo.

Imposta un override del fader di traccia. A differenza di VOL, non viene sostituito dal volume Instrument a ogni nuova nota. Agisce anche sulle mandate post fader. La base salvata del mixer non cambia; una modifica manuale del fader riprende il controllo e il riavvio del trasporto ripristina la base.

Preparazione delle prove. SYNTH o SAMPLE, più note nella stessa traccia, nessuna Table mixer.

Prova A

```
00 C-4 00 LEV 40 --- 00
08 G-4 00 LEV C0 --- 00
```

Il fader passa da circa un quarto a tre quarti. Per un fade graduale metti LEV C0, poi REP F8 nella stessa colonna e un RTO 20 più avanti. LEV 00 non equivale a cancellare l’automazione: mantiene l’override a zero.

Prova B

```
00 C-4 00 LEV 40 --- 00
04 E-4 00 --- 00 --- 00
08 G-4 00 LEV C0 --- 00
```

Il fader runtime resta basso anche sulla nota nuova della 04 e aumenta sulla 08. I VOL delle singole note restano indipendenti.

Nelle Table. Può trasformare una Table in automazione del mixer. I repeater Table avanzano alla velocità TIC e condividono il risultato con il fader visualizzato.

Da controllare. Se il volume sembra ripartire a ogni nota stai probabilmente usando VOL; LEV è il livello della traccia.

Se il fader del mixer risale quando avvii PLAY, cerca invece LEV nelle Phrase e nelle Table: ogni esecuzione del comando prevale sul fader manuale. Esempio nel file originale di Oltre le dune: T4 ha LEV E1 nella Phrase 18, riga 00; T5 nella Phrase 1F, riga 02; T6 nella Phrase 26, riga 04. Nella prima riga Song di Oltre le dune, T4 richiama Chain 0C: contiene 18, 3B, 3B, 3B. Chain 00 contiene invece 00, 01, 00, 01. La pagina Chain mostra il riferimento della cella Song selezionata; Cxx è il numero della Chain aperta. K3 permette anche di sceglierne un’altra dal pool. Sono ID e righe esadecimali: P18 significa Phrase numero 18 in base 16 (24 decimale), non traccia 18; riga 00 è il primo step. E1 è 225/255, circa 88%. Eliminare VOL non elimina questa automazione. Per bilanciare liberamente la traccia, rimuovi LEV anche nelle variazioni successive e nelle eventuali Table; per conservare l’arco programmato, modifica i valori LEV. LEV 00 silenzia la traccia: non cancella il comando. STOP ripristina il livello base salvato nel mixer.


### PAN Posizione stereo della traccia

Parametro. 00 sinistra; 80 centro; FF destra.

Imposta un override del pan del mixer. Opera su tutta la traccia e sulle sue mandate post pan; non cambia il pan delle altre tracce. Gli LFO PAN Instrument aggiungono movimento intorno alla base. Come LEV, l’override dura fino a una modifica manuale o al reset del trasporto.

Preparazione delle prove. SYNTH con sustain, delay e reverb send a zero per il primo ascolto.

Prova A

```
00 C-4 00 PAN 20 --- 00
08 G-4 00 PAN E0 --- 00
```

La prima nota è prevalentemente a sinistra, la seconda a destra. Per una distribuzione stereo regolare usa una Table; per un movimento continuo usa LFO PAN. Se senti il suono ancora al centro, controlla anche i ritorni stereo di delay e riverbero.

Prova B

```
00 C-4 00 PAN 00 --- 00
04 --- FF PAN 80 --- 00
08 --- FF PAN FF --- 00
```

Ascolti sinistra, centro, destra. Poi riapri il riverbero per sentire la differenza fra posizione diretta e coda stereo.

Nelle Table. Permette percorsi di pan a gradini. Phrase e Table scrivono lo stesso parametro mixer: evita due automazioni in conflitto sullo stesso tick.

Da controllare. I ritorni degli effetti possono rimanere su entrambi i lati anche se la voce diretta è tutta a sinistra.


### DSN Mandata al delay master

Parametro. 00–FF quantità inviata dalla traccia.

Regola la mandata post fader e post pan al delay condiviso. Non regola la divisione musicale, il feedback o il ritorno master: questi si scelgono in Master FX. Serve un DELAY RETURN maggiore di zero. L’override segue le stesse regole di LEV e PAN.

Preparazione delle prove. Master delay 1/8D, feedback 80, return 80, ping pong ON.

Prova A

```
00 C-4 00 DSN 00 --- 00
0C G-4 00 DSN C0 --- 00
0D --- FF DSN 00 --- 00
```

La nota sulla riga 0C viene inviata al delay fino alla riga successiva; le altre rimangono asciutte. DSN 00 interrompe i nuovi invii, ma non cancella gli echi già nella linea. È un effetto “throw” controllato per riga.

Prova B

```
00 C-4 00 DSN 00 --- 00
08 G-4 00 DSN C0 --- 00
09 --- FF DSN 00 --- 00
```

Sol alimenta gli echi soltanto per una riga. Gli echi già generati continuano dopo DSN 00.

Nelle Table. Può creare accenti e sequenze di invio senza riscrivere le note. La coda continua anche quando la mandata torna a zero; Stop del trasporto azzera invece il bus FX.

Da controllare. Un return master a zero rende muto il delay anche con DSN FF; Stop tronca le code.


### RSN Mandata al riverbero master

Parametro. 00–FF quantità inviata dalla traccia.

Regola la mandata al riverbero condiviso ROOM o AMBIENT. Il tipo, il decay, il damping e REVERB RETURN sono parametri Master FX. Il valore è post fader: abbassare LEV riduce anche ciò che viene inviato. Non aggiunge un riverbero separato per ogni strumento.

Preparazione delle prove. Master AMBIENT, decay C0, damp 70 e return 80.

Prova A

```
00 C-4 00 RSN 20 --- 00
08 G-4 00 RSN C0 --- 00
09 --- FF RSN 00 --- 00
```

La prima nota riceve poco ambiente; la seconda genera una coda più ampia. Chiudere RSN non tronca la coda già generata. Per sentire il risultato scegli AMBIENT e un REVERB RETURN non nullo, mantenendo il livello master moderato.

Prova B

```
00 C-4 00 RSN 00 --- 00
08 G-4 00 RSN A0 --- 00
0A --- FF RSN 00 --- 00
```

La seconda nota lascia una coda mentre la prima resta asciutta. La 0A chiude l’alimentazione, non il riverbero già avviato.

Nelle Table. Può articolare il riverbero nel tempo della nota. Usa una sola sorgente di automazione per evitare che una Table riscriva immediatamente una mandata impostata dalla Phrase.

Da controllare. RSN non cambia il tempo di decadimento: quel parametro è condiviso in Master FX.


### STA Inizio della regione PCM

Parametro. 00–FF frazione del campione: XX/256.

Determina il punto da cui iniziare il successivo trigger del campione. 80 è circa metà del file; FF è vicino alla fine. Serve una sorgente SAMPLE. Una nuova nota Phrase azzera STA e LEN prima di applicare gli FX della propria riga: colloca STA sulla stessa riga della nota da tagliare.

Preparazione della prova A. I07 SAMPLE con un colpo lungo, per esempio CR78 GuiroLong. La prova B prepara lo stesso tipo di suono in I00.

Prova A

```
00 C-4 07 STA 80 LEN 40
```

Lo strumento 07 deve essere SAMPLE. La riproduzione parte da metà file e usa circa un quarto della sua lunghezza totale. La regione viene limitata alla fine del file. Se scegli un colpo già molto corto, il frammento può risultare appena udibile.

Prova B

Preparazione. I00 SAMPLE con un colpo lungo, per esempio CR78 GuiroLong.

```
00 C-4 00 STA 00 LEN 40
04 C-4 00 STA 40 LEN 40
08 C-4 00 STA 80 LEN 40
```

Tre trigger leggono regioni diverse dello stesso file. Ogni frammento dura circa un quarto del campione totale, con limite alla fine del file.

Nelle Table. Cambiare STA mentre il campione suona non sposta subito la testina. Occorre un successivo retrigger, per esempio RET o INS; una nuova nota Phrase senza STA lo riporterebbe invece a zero.

Da controllare. STA cambia la regione del trigger, non la posizione di una testina che sta già leggendo.


### LEN Lunghezza della regione PCM

Parametro. 01–FF frazione XX/255 del file; 00 fino alla fine.

Limita quanto campione viene letto dal punto STA. La misura è una frazione della lunghezza totale del file, non del solo tratto rimanente; la fine effettiva viene comunque troncata al termine del file. Non è il parametro Release e non mette il campione in loop.

Preparazione della prova A. I07 SAMPLE CR78 OpenHat, nota C4. La prova B prepara il campione in I00.

Prova A

```
00 C-4 07 STA 40 LEN 80
04 C-4 07 LEN 00 --- 00
```

La prima nota parte da circa un quarto del file e ne percorre circa metà. La seconda nota riparte dall’inizio e suona fino alla fine, perché ogni nuovo trigger nota ripristina la regione prima degli FX.

Prova B

Preparazione. I00 SAMPLE CR78 OpenHat; nota C4.

```
00 C-4 00 LEN 20 --- 00
04 C-4 00 LEN 80 --- 00
08 C-4 00 LEN 00 --- 00
```

Ascolti una frazione corta, circa metà file e infine tutto il campione. La durata dipende dal file e dall’altezza.

Nelle Table. Come STA, ha effetto sulla prossima inizializzazione della lettura, non sulla testina già attiva. In modalità SYNTH non controlla la durata dell’oscillatore.

Da controllare. LEN 00 significa resto del campione, non silenzio e non zero millisecondi.


## Modelli e parametri dei motori

I parametri dei motori sono override della voce durante la riproduzione. Non riscrivono Instrument. La nuova nota ricarica le basi; una Table può poi applicare subito altri valori. Le memorie REP/RND/RTO sono disponibili anche qui.


### MDL Modello di sintesi della voce

Parametro. 00–04 BASIC; 05–0F BRAIDS; 10 FM4; 11 DUAL WT, in esadecimale.

Cambia l’oscillatore della voce attiva senza modificare il modello salvato nell’Instrument. Usa 00–11 esadecimali: l’interprete applica un modulo 18 ai valori superiori, ma non è un modo utile per nominare i modelli. I controlli TIMBRE e COLOR provengono comunque dallo strumento corrente.

Preparazione delle prove. SOURCE SYNTH, AMP Sustain C0, TABLE FF.

Prova A

```
00 C-4 00 MDL 01 PWM 40
08 --- FF MDL 05 --- 00
```

La nota parte PULSE e passa al modello BR FM sulla riga 08. Una nuova nota ricarica il modello Instrument. MDL non commuta SAMPLE in SYNTH: per farlo modifica SOURCE nello strumento. I modelli Braids sono undici adattamenti; non è l’intero catalogo Braids o Plaits. MDL ricrea lo stato interno del nuovo motore, i suoi inviluppi di operatore e i parametri di base; non riavvia l’AMP comune.

Prova B

```
00 C-3 00 MDL 08 TIM 60
08 --- FF MDL 09 TIM 60
```

La nota passa da CSAW a MORPH. MDL ricarica lo stato del motore, poi TIM imposta il nuovo parametro sulla stessa riga.

Nelle Table. Può sequenziare i modelli all’interno di una sola nota. Su una sorgente SAMPLE non sostituisce il lettore PCM con un oscillatore.

Da controllare. Usa gli ID globali, non l’indice del menu Braids. MDL 10 indica FM4, non il decimo modello Braids.


### TIM Timbre del motore

Parametro. 00–FF, valore assoluto.

Regola TIMBRE nei modelli Braids, l’indice globale nel motore FM4 e la posizione della prima wavetable nel dual. Lavora sulla voce della traccia, indipendentemente dagli altri strumenti. Nei modelli BASIC e SAMPLE non cambia la generazione.

Preparazione delle prove. BRAIDS MORPH, AMP Sustain C0, TABLE FF.

Prova A

```
00 C-3 00 TIM 20 --- 00
02 --- FF REP 08 --- 00
08 --- FF RTO C0 --- 00
```

Con un Braids MORPH, la forma cambia lungo la nota. In FM4 la stessa sequenza rende crescente la modulazione. Una nuova nota ricarica il TIMBRE dello strumento.

Prova B

```
00 C-3 00 TIM C0 --- 00
01 --- FF REP F0 --- 00
08 --- FF RTO 40 --- 00
```

Il timbro scende di 10 esadecimale per riga verso 40. Lo stesso comando agisce da indice in FM4 e da POS1 nel dual.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. TIM non è una destinazione LFO universale in Meighty. Le mandate LFO POS sono specifiche del dual.


### COL Color del modello Braids

Parametro. 00–FF, valore assoluto.

Controlla COLOR: rapporto/modulazione nei modelli FM e VOSIM, filtro e saturazione in MORPH, miscela in SAW SQUARE e SYNC, intervallo e quantità del sub in SAW SUB, carattere delle percussioni. Nel dual equivale a WT2; in FM4 usa FAI e FBK per i controlli dedicati.

Preparazione delle prove. BRAIDS SAW SQUARE con sustain; ascolta prima senza filtro chiuso.

Prova A

```
00 C-3 00 COL 20 --- 00
04 --- FF COL 80 --- 00
08 --- FF COL E0 --- 00
```

Con Braids SAW SYNC varia il bilanciamento tra master e slave. Con SAW SUB il centro separa il sub a −24 e −12 semitoni e riduce la sua quantità.

Prova B

```
00 C-3 00 COL 00 --- 00
08 --- FF COL FF --- 00
```

Confronti i due estremi del bilanciamento del modello. Per FM4 usa FBK se desideri feedback: COL non è un alias di FBK.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. Il significato di COLOR dipende dal modello; non descriverlo sempre come un cutoff.


### FAI Indice globale FM4

Parametro. 00–FF. 00 rimuove la modulazione fra operatori.

Regola la profondità di modulazione degli operatori FM4. Non cambia rapporto, livello o inviluppi dei singoli operatori. Nell’algoritmo con quattro portanti indipendenti l’indice non ha connessioni FM su cui agire; il feedback resta indipendente.

Preparazione delle prove. FM4 algoritmo 1; OP1/2 Ratio 1/2 e livelli FF/90, OP3/4 livello 00, sustain C0.

Prova A

```
00 C-3 00 FAI 10 --- 00
02 --- FF REP 10 --- 00
08 --- FF RTO D0 --- 00
```

Con algoritmo 1 con i modulatori attivi il suono passa da semplice a ricco di armoniche. Percepire il movimento richiede che i modulatori abbiano un livello e un sustain sufficienti.

Prova B

```
00 C-3 00 FAI 00 --- 00
04 --- FF FAI 40 --- 00
08 --- FF FAI A0 --- 00
```

Passi da una portante semplice a una modulazione più intensa. OP2 resta aperto perché ha Sustain C0.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. Se usi l’algoritmo 8, le quattro portanti sono indipendenti: FAI non ha collegamenti di modulazione su cui agire.


### FAL Algoritmo dei quattro operatori

Parametro. 00–07. Il pannello li mostra come algoritmi 1–8.

Cambia le connessioni FM4 durante la nota, senza riavviare le quattro fasi o i loro inviluppi. 00: 4→3→2→1; 01: (3+4)→2→1; 02: 3→2 e (2+4)→1; 03: 4→3 e (2+3)→1; 04: due coppie 2→1 e 4→3; 05: 4 modula 1,2,3; 06: 1 e 2 indipendenti più 4→3; 07: quattro portanti. Fuori intervallo usa i tre bit bassi.

Preparazione delle prove. FM4 con tutti e quattro gli operatori a livello e sustain udibili.

Prova A

```
00 C-3 00 FAL 00 --- 00
04 --- FF FAL 04 --- 00
08 --- FF FAL 07 --- 00
```

La stessa nota passa dalla catena completa alle due coppie, poi alla somma delle quattro portanti. Il cambio può essere netto: usalo su nuove note se vuoi evitare una discontinuità.

Prova B

```
00 C-3 00 FAL 00 FAI 70
04 --- FF FAL 04 --- 00
08 --- FF FAL 07 --- 00
```

Confronti algoritmo 1 in serie, algoritmo 5 a due coppie e algoritmo 8 a portanti indipendenti. La pagina Instrument numera da 1; l’FX usa 00–07.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. FAL non riavvia gli inviluppi: se i modulatori sono già decaduti, il confronto può sembrare poco evidente.


### FBK Feedback dell operatore quattro

Parametro. 00–FF. 00 disabilita il feedback.

Rimanda l’uscita media dei due campioni precedenti dell’operatore 4 alla sua fase. Il risultato dipende dall’algoritmo, dal livello e dall’inviluppo di OP4. Valori alti producono armoniche dense e anche aliasing; filtro e volume aiutano a contenerle.

Preparazione delle prove. FM4 algoritmo 1, OP4 aperto e collegato, INDEX 70.

Prova A

```
00 C-3 00 FBK 00 FAI 60
04 --- FF FBK 40 --- 00
08 --- FF FBK B0 --- 00
```

Con OP4 attivo il suono diventa progressivamente più ruvido. Non cambia il feedback del delay master.

Prova B

```
00 C-3 00 FBK 00 --- 00
04 --- FF FBK 30 --- 00
08 --- FF FBK 80 --- 00
```

Il feedback di OP4 aggiunge armoniche al percorso in serie. Il suo livello e inviluppo restano importanti.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. Un OP4 a livello zero o decaduto rende inefficace il confronto. Feedback alti possono produrre timbri ruvidi.


### WTP Posizione della prima wavetable

Parametro. 00–FF, dalla prima all’ultima forma del banco.

Scorre in modo interpolato tra le nove forme della wavetable di OSC1. Non cambia il banco CLASSIC, HOLLOW, GLASS o FORMANT: quello si sceglie nella pagina Motore. Per ascoltare OSC1 da solo imposta OSM 00.

Preparazione delle prove. DUAL WT, OSC1 CLASSIC, MIX 00; tutte le profondità LFO POS a zero.

Prova A

```
00 C-4 00 WTP 00 OSM 00
01 --- FF REP 10 --- 00
0F --- FF RTO F0 --- 00
```

Una sola nota attraversa il banco scelto. Le righe vuote con REP continuano lo spostamento; le nuove note lo riportano alla posizione base dello strumento.

Prova B

```
00 C-3 00 WTP 00 --- 00
04 --- FF WTP 40 --- 00
08 --- FF WTP 80 --- 00
0C --- FF WTP C0 --- 00
```

Ascolti quattro posizioni di CLASSIC. Per raggiungere l’ultima forma prova FF: la scansione interpola sempre e non seleziona un preset intero.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. Con MIX FF ascolti solo OSC2: WTP può muoversi senza risultato udibile.


### WT2 Posizione della seconda wavetable

Parametro. 00–FF.

Come WTP, ma per OSC2. COL usa la stessa destinazione nel dual. Per isolare OSC2 imposta OSM FF. OSC2 mantiene semitoni, detune ed eventuale hard sync definiti nello strumento o modificati dagli FX.

Preparazione delle prove. DUAL WT, OSC2 FORMANT, MIX FF; profondità LFO POS neutre.

Prova A

```
00 C-4 00 WT2 20 OSM FF
04 --- FF WT2 80 --- 00
08 --- FF WT2 E0 --- 00
```

Tre posizioni del banco di OSC2 sulla stessa nota. Se il bilanciamento è tutto su OSC1, la variazione di WT2 non si sente.

Prova B

```
00 C-3 00 WT2 20 --- 00
04 --- FF WT2 60 --- 00
08 --- FF WT2 A0 --- 00
0C --- FF WT2 E0 --- 00
```

Si sposta il gruppo di armoniche del banco FORMANT. Con LFO2 > POS2 +32 la scansione continua intorno a ciascuna di queste basi.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. Non confondere WT2 con OSC2 BANK: il banco si sceglie in Instrument, il comando ne percorre le forme.


### DTN Detune del secondo oscillatore

Parametro. 80 centrale; 00 negativo; FF positivo.

Regola l’offset fine di OSC2 attorno all’intervallo in semitoni della pagina Motore. L’intervallo totale è circa ±50 cent; 80 equivale a nessun detune. Non trasporta OSC1 e non modifica il PAN.

Preparazione delle prove. DUAL WT, stesso banco e posizione per i due oscillatori; MIX 80, SEMI 0, SYNC OFF.

Prova A

```
00 C-4 00 OSM 80 DTN 80
04 --- FF DTN 90 --- 00
08 --- FF DTN 70 --- 00
```

Con i due oscillatori all’unisono compaiono battimenti nei due sensi. HARD SYNC può cambiare la percezione del detune perché OSC1 riavvia la fase di OSC2.

Prova B

```
00 C-3 00 DTN 80 --- 00
04 --- FF DTN 88 --- 00
08 --- FF DTN 98 --- 00
```

Si passa dall’unisono a battimenti via via più veloci. Sono scostamenti fini; DTN 80 è neutro, non DTN 00.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. Con SYNC ON il comportamento cambia perché OSC2 viene riavviato da OSC1.


### OSM Bilanciamento dei due oscillatori

Parametro. 00 solo OSC1; 80 circa metà; FF solo OSC2.

Imposta il mix lineare delle due wavetable prima del filtro, dell’inviluppo d’ampiezza e delle mandate di traccia. I livelli dei motori si sommano con compensazione tramite crossfade: non raddoppiano al centro.

Preparazione delle prove. DUAL WT, OSC1 CLASSIC posizione 00 e OSC2 GLASS posizione C0.

Prova A

```
00 C-4 00 OSM 00 --- 00
04 --- FF OSM 80 --- 00
08 --- FF OSM FF --- 00
```

Si ascolta OSC1, la miscela e OSC2. Il comando ha effetto solo nel motore dual wavetable.

Prova B

```
00 C-3 00 OSM 00 --- 00
01 --- FF REP 10 --- 00
0F --- FF RTO F0 --- 00
```

Il mix passa progressivamente da OSC1 verso OSC2. Le posizioni restano quelle impostate: stai cambiando il bilanciamento, non i banchi.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. Due onde uguali rendono poco evidente il crossfade: prepara timbri diversi prima della prova.


### SYN Hard sync dei due oscillatori

Parametro. 00 OFF; qualsiasi valore diverso da zero ON.

Nel dual wavetable, ogni riavvio della fase di OSC1 azzera la fase di OSC2. Per un effetto evidente cambia l’intervallo o il detune di OSC2 e ascolta almeno parte di OSC2. Non è una sincronizzazione del clock o del delay.

Preparazione delle prove. DUAL WT, OSC2 SEMI +7, MIX C0 e cutoff aperto.

Prova A

```
00 C-3 00 OSM C0 SYN 00
04 --- FF SYN 01 --- 00
08 --- FF SYN 00 --- 00
```

Con OSC2 a +7 semitoni il passaggio a sync introduce un carattere più aspro. Anche un cambiamento di sync può creare una discontinuità intenzionale.

Prova B

```
00 C-3 00 SYN 00 WT2 80
04 --- FF SYN 01 --- 00
08 --- FF SYN 00 --- 00
```

Confronti l’intervallo libero con il riavvio forzato di OSC2. Il timbro dipende dalla sua forma; il pitch dominante resta ancorato a OSC1.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. SYN non aggancia gli LFO o il sequencer al BPM e non attiva il ping pong del delay.


### OR1 Rapporto di frequenza di OP1

Parametro. 00–0E: 0,5; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 14; 16.

Cambia il rapporto di OP1 rispetto alla nota suonata nel motore FM4. Non azzera la fase o l’inviluppo. Il suo ruolo di portante o modulatore dipende da FAL. Il byte seleziona un indice della lista, non un numero in Hz. Valori superiori a 0E vengono ridotti modulo 15.

Preparazione delle prove. FM4; operatore 1 aperto; scegli algoritmo 8 per confrontare le portanti o 1 per la modulazione.

Prova A

```
00 C-3 00 OR1 01 FAI 70
04 --- FF OR1 02 --- 00
08 --- FF OR1 05 --- 00
```

OP1 passa ai rapporti 1, 2 e 5. Se è un modulatore cambia soprattutto il contenuto armonico; se è una portante cambia anche la nota percepita. Un operatore a livello zero non produce un cambiamento udibile.

Prova B

```
00 C-3 00 OR1 01 --- 00
04 --- FF OR1 03 --- 00
08 --- FF OR1 0D --- 00
```

Gli indici 01,03,0D significano rapporti 1,3,14. Nell’algoritmo 8 cambia l’altezza della portante; in altri algoritmi può cambiare soprattutto il timbro.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. Il parametro è un indice: 0C vale rapporto 12, 0D vale 14 e 0E vale 16; 0F riparte da indice 00 per il modulo 15.


### OR2 Rapporto di frequenza di OP2

Parametro. 00–0E: 0,5; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 14; 16.

Cambia il rapporto di OP2 rispetto alla nota suonata nel motore FM4. Non azzera la fase o l’inviluppo. Il suo ruolo di portante o modulatore dipende da FAL. Il byte seleziona un indice della lista, non un numero in Hz. Valori superiori a 0E vengono ridotti modulo 15.

Preparazione delle prove. FM4; operatore 2 aperto; scegli algoritmo 8 per confrontare le portanti o 1 per la modulazione.

Prova A

```
00 C-3 00 OR2 01 FAI 70
04 --- FF OR2 02 --- 00
08 --- FF OR2 05 --- 00
```

OP2 passa ai rapporti 1, 2 e 5. Se è un modulatore cambia soprattutto il contenuto armonico; se è una portante cambia anche la nota percepita. Un operatore a livello zero non produce un cambiamento udibile.

Prova B

```
00 C-3 00 OR2 01 --- 00
04 --- FF OR2 03 --- 00
08 --- FF OR2 0D --- 00
```

Gli indici 01,03,0D significano rapporti 1,3,14. Nell’algoritmo 8 cambia l’altezza della portante; in altri algoritmi può cambiare soprattutto il timbro.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. Il parametro è un indice: 0C vale rapporto 12, 0D vale 14 e 0E vale 16; 0F riparte da indice 00 per il modulo 15.


### OR3 Rapporto di frequenza di OP3

Parametro. 00–0E: 0,5; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 14; 16.

Cambia il rapporto di OP3 rispetto alla nota suonata nel motore FM4. Non azzera la fase o l’inviluppo. Il suo ruolo di portante o modulatore dipende da FAL. Il byte seleziona un indice della lista, non un numero in Hz. Valori superiori a 0E vengono ridotti modulo 15.

Preparazione delle prove. FM4; operatore 3 aperto; scegli algoritmo 8 per confrontare le portanti o 1 per la modulazione.

Prova A

```
00 C-3 00 OR3 01 FAI 70
04 --- FF OR3 02 --- 00
08 --- FF OR3 05 --- 00
```

OP3 passa ai rapporti 1, 2 e 5. Se è un modulatore cambia soprattutto il contenuto armonico; se è una portante cambia anche la nota percepita. Un operatore a livello zero non produce un cambiamento udibile.

Prova B

```
00 C-3 00 OR3 01 --- 00
04 --- FF OR3 03 --- 00
08 --- FF OR3 0D --- 00
```

Gli indici 01,03,0D significano rapporti 1,3,14. Nell’algoritmo 8 cambia l’altezza della portante; in altri algoritmi può cambiare soprattutto il timbro.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. Il parametro è un indice: 0C vale rapporto 12, 0D vale 14 e 0E vale 16; 0F riparte da indice 00 per il modulo 15.


### OR4 Rapporto di frequenza di OP4

Parametro. 00–0E: 0,5; 1; 2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 14; 16.

Cambia il rapporto di OP4 rispetto alla nota suonata nel motore FM4. Non azzera la fase o l’inviluppo. Il suo ruolo di portante o modulatore dipende da FAL. Il byte seleziona un indice della lista, non un numero in Hz. Valori superiori a 0E vengono ridotti modulo 15.

Preparazione delle prove. FM4; operatore 4 aperto; scegli algoritmo 8 per confrontare le portanti o 1 per la modulazione.

Prova A

```
00 C-3 00 OR4 01 FAI 70
04 --- FF OR4 02 --- 00
08 --- FF OR4 05 --- 00
```

OP4 passa ai rapporti 1, 2 e 5. Se è un modulatore cambia soprattutto il contenuto armonico; se è una portante cambia anche la nota percepita. Un operatore a livello zero non produce un cambiamento udibile.

Prova B

```
00 C-3 00 OR4 01 --- 00
04 --- FF OR4 03 --- 00
08 --- FF OR4 0D --- 00
```

Gli indici 01,03,0D significano rapporti 1,3,14. Nell’algoritmo 8 cambia l’altezza della portante; in altri algoritmi può cambiare soprattutto il timbro.

Nelle Table. Operativo nelle Table, alla velocità TIC. Si applicano le regole comuni degli override del motore descritte all’inizio della famiglia.

Da controllare. Il parametro è un indice: 0C vale rapporto 12, 0D vale 14 e 0E vale 16; 0F riparte da indice 00 per il modulo 15.


# 13 Risolvere i problemi durante il lavoro

Quando il risultato non è chiaro, isola una traccia, una nota lunga e un solo parametro. Prima controlla i collegamenti, poi la sorgente sonora, infine le trasformazioni. Se togli tutto insieme perdi il riferimento di ciò che causava il problema.

Sintomo | Controllo pratico

Non sento la nota | Song richiama una Chain valida, la Chain una Phrase e IN uno strumento preparato. Controlla mute/solo, VOL, LEV e master.

Il meter si muove ma sento poco | Il meter è prima di pan e master. Controlla uscita, MASTER e sorgente audio dell’app; non è un indicatore dell’uscita finale.

Il preset non cambia in I00 | K3 deve scegliere I00, K4 il nome nel catalogo e REC confermare il caricamento.

CUT o VOL sembra ignorato | Disattiva Table, LFO e cutoff envelope per una prova. Una Table può applicare un altro CUT o VL subito dopo la Phrase.

Non sento il movimento del filtro | Usa una nota sostenuta e un filtro LP, non un one shot già finito. Confronta basi molto diverse prima di provare profondità piccole.

Non sento il secondo oscillatore | Nel dual controlla MIX. 00 lascia solo OSC1, FF solo OSC2.

FM4 resta una sinusoide | Controlla algoritmo, livello dei modulatori, Index e durata dei loro inviluppi.

Il pad pulsa o si tronca | Nuove note riavviano l’ADSR. Usa note iniziali e poi Phrase valide vuote. Evita celle Song vuote e KIL.

Il delay non si sente | Apri send di traccia e return master. Lascia una pausa dopo la nota; controlla di non premere Stop durante la coda.

Le tracce si sfasano | Confronta lunghezze reali delle Chain e salti HOP/JMP. Una cella Song vuota non equivale a una Chain lunga quattro Phrase.

La Table riparte troppo presto | Ogni nuova nota può riavviarla. Prova un solo trigger e Sustain alto.

RND non fa niente | Prima serve un FX operativo ricordato nella stessa colonna. Non confonderlo con RNL.

Il fill compare nel giro sbagliato | CND e NTH contano diversamente; i salti all’indietro incrementano i giri. Riallinea con Stop/Play.

Il brano cambia anche altrove | Stai modificando un ID Phrase, Chain o Instrument condiviso. Prepara un ID diverso per una variazione indipendente.

Load segnala slot vuoto o corrotto | Carica uno stato noto nell’app oppure salva prima un progetto valido nello slot. Controlla l’ambiente e il formato del file.


## Tre confronti utili prima di correggere il pattern

Suono troppo corto: togli KIL/RET, porta AMP Sustain a C0 e scrivi OFF soltanto in fondo. Suono sempre uguale: spegni la Table e prova due valori molto distanti dello stesso parametro. Risultato casuale difficile da ripetere: aggiungi SED una volta nella Phrase e riduci le altre estrazioni sulla stessa traccia.


# 14 Indici cataloghi e glossario


## Indice alfabetico dei comandi FX

Ogni sigla corrisponde alla scheda del capitolo 12. Nel PDF le sigle dell’indice sono collegamenti interni; i segnalibri consentono di aprire anche la singola scheda. Per imparare le combinazioni usa il laboratorio del capitolo 11.

FX | Argomento
--- | ---
[---](#fx-none) | Colonna vuota
[ARC](#fx-arc) | Velocità dell’arpeggio
[ARP](#fx-arp) | Arpeggio monofonico a tre altezze
[CHA](#fx-cha) | Probabilità dei lati della riga
[CHD](#fx-chd) | Accordi e sovrapposizione su tre voci
[CHN](#fx-chn) | Probabilità dell’evento immediatamente a sinistra
[CND](#fx-cnd) | Condizione sul giro
[COL](#fx-col) | Color del modello Braids
[CUT](#fx-cut) | Apertura del filtro
[DEL](#fx-del) | Ritardo della riga
[DSN](#fx-dsn) | Mandata al delay master
[DTN](#fx-dtn) | Detune del secondo oscillatore
[FAI](#fx-fai) | Indice globale FM4
[FAL](#fx-fal) | Algoritmo dei quattro operatori
[FBK](#fx-fbk) | Feedback dell operatore quattro
[HOP](#fx-hop) | Passaggio alla Phrase successiva
[INS](#fx-ins) | Cambio strumento con retrigger
[JMP](#fx-jmp) | Salto nella Phrase corrente
[KIL](#fx-kil) | Interruzione immediata o programmata
[LEN](#fx-len) | Lunghezza della regione PCM
[LEV](#fx-lev) | Livello del mixer della traccia
[MDL](#fx-mdl) | Modello di sintesi della voce
[NTH](#fx-nth) | Esecuzione periodica dei lati
[OFF](#fx-off) | Rilascio o spegnimento differito
[OR1](#fx-or1) | Rapporto di frequenza di OP1
[OR2](#fx-or2) | Rapporto di frequenza di OP2
[OR3](#fx-or3) | Rapporto di frequenza di OP3
[OR4](#fx-or4) | Rapporto di frequenza di OP4
[OSM](#fx-osm) | Bilanciamento dei due oscillatori
[PAN](#fx-pan) | Posizione stereo della traccia
[PBN](#fx-pbn) | Deriva progressiva di intonazione
[PIT](#fx-pit) | Trasposizione relativa della voce
[PRV](#fx-prv) | Condizione sull’esito precedente
[PSL](#fx-psl) | Portamento fra note
[PVB](#fx-pvb) | Vibrato a tick
[PWM](#fx-pwm) | Larghezza dell’impulso
[REP](#fx-rep) | Ripetizione con incremento
[RET](#fx-ret) | Retrigger e rampa di volume
[RND](#fx-rnd) | Variazione casuale del comando ricordato
[RNL](#fx-rnl) | Variazione dell’evento a sinistra
[RSN](#fx-rsn) | Mandata al riverbero master
[RTO](#fx-rto) | Limite del repeater
[SCA](#fx-sca) | Scala locale della traccia
[SCG](#fx-scg) | Scala locale per tutte le tracce
[SED](#fx-sed) | Inizializzazione del generatore casuale
[SNG](#fx-sng) | Salto relativo nella Song
[STA](#fx-sta) | Inizio della regione PCM
[STP](#fx-stp) | Arresto della Table
[SYN](#fx-syn) | Hard sync dei due oscillatori
[TBL](#fx-tbl) | Selezione e riavvio della Table
[THO](#fx-tho) | Salto a una riga della Table
[TIC](#fx-tic) | Durata delle righe Table
[TIM](#fx-tim) | Timbre del motore
[TPO](#fx-tpo) | Tempo globale
[TSP](#fx-tsp) | Trasposizione globale
[VOL](#fx-vol) | Volume della voce
[WT2](#fx-wt2) | Posizione della seconda wavetable
[WTP](#fx-wtp) | Posizione della prima wavetable


## Trovare una combinazione

Obiettivo | Esperimento

Due parametri sulla stessa nota | E01 CUT e PAN

Memoria ed evento vicino | E02 RND e RNL

Due rampe con fine controllata | E03 REP e RTO

Probabilità e ordine dei campi | E04 CHA e CHN

Melodia casuale ripetibile | E05 RNL SED e scala

Shuffle probabilistico | E06 DEL e CHA

Durata e rilascio | E07 CUT OFF e KIL

Due sorgenti di pitch | E08 ARP ARC e Table

Tre automazioni sincronizzate | E09 Table CUT PAN e TIC

Throw e coda stereo | E10 DSN RSN REP e RTO

Variazione FM su nota tenuta | E11 FAL FAI e OR2

Scansione a gradini e continua | E12 WTP WT2 e LFO

Pool di note e percorso variabile | E13 TBL THO RND e SED


## Catalogo dei 33 campioni

Slot | Campione | Slot | Campione

00 | CR78-Kick | 11 | CR78-GuiroShort

01 | CR78-Snare | 12 | CR78-GuiroLong

02 | CR78-OpenHat | 13 | CR78-TambShort

03 | CR78-Tom | 14 | CR78-TambLong

04 | MP45-Snare | 15 | CR78-KickB

05 | MP45-OpenHat | 16 | CR78-KickAccent

06 | MP45-FX3 | 17 | CR78-SnareB

07 | MP45-FX4 | 18 | CR78-SnrAccent

08 | CR78-ClosedHat | 19 | MP45-Snare3

09 | CR78-HatAccent | 1A | MP45-RimHat2

0A | CR78-MetalHat | 1B | MP45-RimHat1

0B | CR78-Rimshot | 1C | MP45-SmallSnare

0C | CR78-BongoHi | 1D | MP45-OpenHat1

0D | CR78-BongoLo | 1E | MP45-FX5Kick

0E | CR78-CongaLo | 1F | MP45-FX6Hat

0F | CR78-Cowbell | 20 | MP45-FX3HatRide

10 | CR78-Cymbal |  | 

Il catalogo conserva i primi otto riferimenti usati dalle demo, poi aggiunge articolazioni CR78 e MiniPops. I numeri sono slot sample, distinti dagli slot Instrument: caricare sample 15 in Instrument 00 non richiede IN 15 nella Phrase. Devi richiamare IN 00.


## Glossario essenziale

Voce. Un suono con i propri oscillatori, filtro e inviluppi. La traccia selezionata in Poly 3 track contiene fino a tre voci; un motore con due oscillatori non crea da solo due voci polifoniche.

Preset e Instrument. Il preset è una voce del catalogo; Instrument è la copia modificabile in uno slot del progetto.

Trigger. Un nuovo evento nota che avvia o riavvia il suono.

Override. Un valore operativo che prevale temporaneamente sulla base del progetto senza riscriverla.

Send e return. La mandata alimenta l’effetto; il ritorno riporta il suo segnale al mix.

Tick e riga. Il tick è una frazione del quarto; sei tick formano una riga Phrase.

Scala e trasposizione. La scala sceglie i gradi ammessi; la trasposizione sposta le altezze.

Progetto e backup. Un progetto descrive un brano; un backup .meighty può conservare gli otto slot e la copia in lavorazione. Non è una registrazione del suono né del punto esatto del motore in esecuzione.


## Capacità e limiti

Otto tracce, di cui una a scelta può suonare tre voci simultanee e le altre sette restano monofoniche; 64 Phrase, 32 Chain, 32 righe Song, 32 Instrument, 16 Table, 33 campioni e 177 preset. Sono presenti 18 modelli, quattro banchi wavetable, due LFO per suono, ADSR comune e del filtro, quattro inviluppi operatore FM4, delay e riverbero master. Il progetto occupa 11944 byte; il file .meighty conserva anche la scelta della traccia polifonica e tutti i comandi CHD.

Le probabilità non riscrivono le note della Phrase. Non esiste un comando che riempia automaticamente una Phrase con un ritmo euclideo, né un editor automatico che sposti le celle: puoi scrivere il disegno, usare cicli locali o variare il percorso di una Table. Un generatore esterno deve esportare dati compatibili, non un file di un altro tracker da aprire direttamente.

Meighty 1.02 è il firmware per il FM-1 fisico. Gli ambienti di emulazione sono separati: la possibilità di importare un formato non implica che quell’ambiente riproduca tutte le funzioni, in particolare la polifonia e CHD. Il convertitore rifiuta esportazioni che perderebbero dati musicali.

I controlli del FM-1 sono fisici: le manopole e gli inviluppi disegnati sullo schermo forniscono un riscontro dei parametri, non un’interfaccia touch.
