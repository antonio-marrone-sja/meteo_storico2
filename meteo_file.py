import csv
import json
import requests



def salva_json(previsioni, percorso):

    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(previsioni, f, indent=2, ensure_ascii=False)

    print(f"Salvate {len(previsioni)} previsioni in: {percorso}")


def scrivi_report(previsioni, statistiche, citta, percorso):

    with open(percorso, "w", encoding="utf-8") as f:
        # Intestazione con citta
        f.write(f"PREVISIONI STORICHE — {citta}\n")
        f.write("=" * 32 + "\n")
        f.write("GIORNO      | MAX (°C) | MIN (°C)\n")
        f.write("-" * 34 + "\n")

        # Ciclo for sulle previsioni
        for giorno in previsioni:
            f.write(f"{giorno['data']:<12}| {giorno['temp_max']:>8.1f} | {giorno['temp_min']:>8.1f}\n")

        # Riga vuota e blocco statistiche con le chiavi richieste
        f.write("\n")
        f.write("Statistiche:\n")
        f.write(f"  Media temperatura massima: {statistiche['media_max']:.1f}°C\n")
        f.write(f"  Giorno piu' caldo: {statistiche['giorno_piu_caldo']}\n")
        f.write(f"  Giorno piu' freddo: {statistiche['giorno_piu_freddo']}\n")

    print(f"Report scritto: {percorso}")

def esporta_csv(previsione, percorso):

    nomi_colonne = ["data", "temp_max", "temp_min", "consiglio"]

    with open(percorso, "w", newline="", encoding="utf-8") as f:

        scrittore = csv.DictWriter(f, fieldnames=nomi_colonne)

# --- BLOCCO DI TEST ---
if __name__ == "__main__":
    # 1. Il tuo elenco di previsioni reali
    mie_previsioni = [
        {
            "data": "2026-09-01",
            "temp_min": 19.2,
            "temp_max": 29.5,
            "condizioni": "Sereno",
            "precipitazioni_mm": 0.0,
            "umidita_pct": 55
        },
        {
            "data": "2026-09-02",
            "temp_min": 18.0,
            "temp_max": 27.3,
            "condizioni": "Poco nuvoloso",
            "precipitazioni_mm": 0.0,
            "umidita_pct": 62
        },
        {
            "data": "2026-09-03",
            "temp_min": 16.5,
            "temp_max": 23.0,
            "condizioni": "Pioggia",
            "precipitazioni_mm": 12.4,
            "umidita_pct": 85
        }
    ]

    # 2. Statistiche di prova coerenti con i tuoi dati
    mie_statistiche = {
        "media_max": 26.6,
        "giorno_piu_caldo": "2026-09-01 (29.5°C)",
        "giorno_piu_freddo": "2026-09-03 (16.5°C)"
    }

    print("Avvio del test...")

    # Chiamata alla Funzione 1
    salva_json(mie_previsioni, "previsioni_storiche.json")

    # Chiamata alla Funzione 2
    scrivi_report(mie_previsioni, mie_statistiche, "Agrigento", "report_meteo_storico.txt")

    print("Test completato con successo!")