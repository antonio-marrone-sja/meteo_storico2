import requests

URL_GEOCODING = "https://geocoding-api.open-meteo.com/v1/search" # End Point
URL_ARCHIVIO = "https://archive-api.open-meteo.com/v1/archive" # End Point

def cerca_coordinate(nome_citta):
    """
    Chiede all'API di geocoding le coordinate di una citta'.
    Ritorna una coppia (latitudine, longitudine), oppure None
    se la citta' non viene trovata.
    """
    parametri = {
        "name": nome_citta,
        "count": 1,
        "language": "it",
        "format": "json"
    }

    risposta = requests.get(URL_GEOCODING, params=parametri, timeout=10)
    dati = risposta.json()

    if "results" in dati:
        primo_risultato = dati["results"][0]
        latitudine = primo_risultato["latitude"]
        longitudine = primo_risultato["longitude"]
        return latitudine, longitudine
    else:
        print(f"Citta' non trovata: {nome_citta}")
        return None


def scarica_dati_storici(latitudine, longitudine, data_inizio, data_fine):
    """
    Chiama l'API Open-Meteo Archive e ritorna il dizionario JSON
    con le temperature storiche nell'intervallo richiesto.
    Ritorna None se c'e' un errore.
    """
    parametri = {
        "latitude": latitudine,
        "longitude": longitudine,
        "start_date": data_inizio,
        "end_date": data_fine,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "Europe/Rome"
    }

    try:
        risposta = requests.get(URL_ARCHIVIO, params=parametri, timeout=10)

        if risposta.status_code == 200:
            dati = risposta.json()
            return dati
        else:
            print(f"Errore HTTP: {risposta.status_code}")
            return None

    except requests.exceptions.Timeout:
        print("Errore: il server non risponde (timeout)")
        return None

    except requests.exceptions.ConnectionError:
        print("Errore: nessuna connessione a Internet")
        return None

    except requests.exceptions.RequestException:
        print("Errore: errore nella richiesta")

    except Exception as e:
        print(f"Errore: {e}")