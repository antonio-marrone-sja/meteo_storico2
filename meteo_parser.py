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