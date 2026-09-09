# meteo_parser.py — STUDENTE 2 — branch: feature/parser
# Funzioni: analizza_dati_storici(dati) e calcola_statistiche(previsioni)

def analizza_dati_storici(dati):
    """
    Trasforma il JSON grezzo in una lista di dizionari leggibili:
    [{"data": "2026-08-31", "temp_max": 29.1, "temp_min": 19.8}, ...]
    """
    giornaliero = dati["daily"]
    date = giornaliero["time"]
    temp_max = giornaliero["temperature_2m_max"]
    temp_min = giornaliero["temperature_2m_min"]

    previsioni = []

    for i in range(len(date)):
        dizionario_giorno = {
            "data": date[i],
            "temp_max": temp_max[i],
            "temp_min": temp_min[i]
        }
        previsioni.append(dizionario_giorno)

    return previsioni


def calcola_statistiche(previsioni):
    """
    Calcola media delle temperature massime, giorno piu' caldo
    e giorno piu' freddo (basandosi su temp_max e temp_min).
    Ritorna un dizionario con le statistiche.
    """
    if not previsioni:
        return {}

    totale = 0
    for giorno in previsioni:
        totale = totale + giorno["temp_max"]

    media = totale / len(previsioni)

    # Si parte dal primo elemento
    giorno_piu_caldo = previsioni[0]
    for giorno in previsioni:
        if giorno["temp_max"] > giorno_piu_caldo["temp_max"]:
            giorno_piu_caldo = giorno

    giorno_piu_freddo = previsioni[0]
    for giorno in previsioni:
        if giorno["temp_min"] < giorno_piu_freddo["temp_min"]:
            giorno_piu_freddo = giorno

    statistiche = {
        "media_max": media,
        "giorno_piu_caldo": giorno_piu_caldo,
        "giorno_piu_freddo": giorno_piu_freddo,
    }

    return statistiche


def confronta_citta(dati_multi_citta):
    """
    Riceve {nome_citta: dati_previsioni} e ritorna un dizionario con
    la citta' piu' calda e la citta' piu' fredda, in base alla media
    delle temperature massime.
    """
    medie_per_citta = {}

    for nome_citta in dati_multi_citta:
        dati_grezzi = dati_multi_citta[nome_citta]

        # 1. Analizziamo le previsioni della città corrente
        previsioni = analizza_previsioni(dati_grezzi)

        # 2. Calcoliamo la media usando il pattern accumulatore
        totale = 0
        for giorno in previsioni:
            totale += giorno["temp_max"]

        media_di_questa_citta = totale / len(previsioni)

        # 3. Salviamo la media nel dizionario
        medie_per_citta[nome_citta] = media_di_questa_citta

    # Se non ci sono città nel dizionario, ritorniamo un dizionario vuoto
    if not medie_per_citta:
        return {"citta_piu_calda": None, "citta_piu_fredda": None}

    # Ora confrontiamo le medie tra tutte le città
    # Prendiamo il primo nome di città come punto di partenza iniziale
    nomi_citta = list(medie_per_citta.keys())
    citta_piu_calda = nomi_citta[0]
    citta_piu_fredda = nomi_citta[0]

    # Scorriamo tutte le città per confrontare le medie
    for nome_citta in medie_per_citta:
        if medie_per_citta[nome_citta] > medie_per_citta[citta_piu_calda]:
            citta_piu_calda = nome_citta

        if medie_per_citta[nome_citta] < medie_per_citta[citta_piu_fredda]:
            citta_piu_fredda = nome_citta

    risultato = {
        "citta_piu_calda": citta_piu_calda,
        "citta_piu_fredda": citta_piu_fredda,
    }
    return risultato

