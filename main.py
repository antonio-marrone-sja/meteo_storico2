# main.py — fornito dal capogruppo, coordina tutto il progetto
from meteo_api import cerca_coordinate, scarica_dati_storici
from meteo_parser import analizza_dati_storici, calcola_statistiche
from meteo_file import salva_json, scrivi_report
from meteo_display2 import stampa_previsioni, stampa_statistiche

DATA_INIZIO = "2026-08-31"
DATA_FINE = "2026-09-06"

# STEP 0 — Studente 1: chiede il nome della citta' e trova le coordinate
CITTA = input("Di quale citta' vuoi il meteo storico? ")
coordinate = cerca_coordinate(CITTA)

if coordinate is None:
    print("Citta' non trovata. Programma terminato.")
else:
    latitudine, longitudine = coordinate

    # STEP 1 — Studente 1: scarica i dati grezzi dall'API
    dati = scarica_dati_storici(latitudine, longitudine, DATA_INIZIO, DATA_FINE)

    if dati is None:
        print("Impossibile scaricare i dati. Programma terminato.")
    else:
        # STEP 2 — Studente 2: trasforma il JSON e calcola le statistiche
        previsioni = analizza_dati_storici(dati)
        statistiche = calcola_statistiche(previsioni)

        # STEP 3 — Studente 3: salva su file
        salva_json(previsioni, "previsioni_storiche.json")
        scrivi_report(previsioni, statistiche, CITTA, "report_meteo_storico.txt")

        # STEP 4 — Studente 4: stampa a schermo
        stampa_previsioni(previsioni, CITTA)
        stampa_statistiche(statistiche)