def stampa_previsioni(previsioni, citta):
    """
    Stampa a schermo la tabella delle temperature storiche.
    """
    print(f"PREVISIONI STORICHE — {citta}")
    print("=" * 34)
    print("GIORNO      | MAX (°C) | MIN (°C)")
    print("-" * 34)
    for giorno in previsioni:
        riga = f"{giorno['data']:<12}| {giorno['temp_max']:>8.1f} | {giorno['temp_min']:>8.1f}"
        print(riga)


def stampa_statistiche(statistiche):
    """
    Stampa a schermo media, giorno piu' caldo e giorno piu' freddo.
    """
    print()
    print("STATISTICHE")
    print("=" * 34)

    print(f"Media temperatura massima: {statistiche['media_max']:.1f}°C")

    caldo = statistiche["giorno_piu_caldo"]
    print(f"Giorno piu' caldo: {caldo['data']} ({caldo['temp_max']:.1f}°C)")

    freddo = statistiche["giorno_piu_freddo"]
    print(f"Giorno piu' freddo: {freddo['data']} ({freddo['temp_min']:.1f}°C)")