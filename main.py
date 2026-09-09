from meteo_api import scarica_previsioni_multi_citta
from meteo_parser import analizza_previsioni, confronta_citta, suggerisci_attivita
from meteo_file import scrivi_report_multi_citta, esporta_csv
from meteo_display import stampa_previsioni_con_consiglio, stampa_confronto_citta

testo_citta = input("Quali città vuoi confrontare? (separate da virgola) ")
lista_nomi_citta = testo_citta.split(",")

# Pulisce eventuali spazi attorno ai nomi digitati
lista_nomi_citta_pulita = []
for nome in lista_nomi_citta:
    lista_nomi_citta_pulita.append(nome.strip())

dati_multi_citta = scarica_previsioni_multi_citta(lista_nomi_citta_pulita)

previsioni_elaborate_per_citta = {}

for nome_citta in dati_multi_citta:
    dati_grezzi = dati_multi_citta[nome_citta]
    previsioni = analizza_previsioni(dati_grezzi)

    for giorno in previsioni:
        giorno["consiglio"] = suggerisci_attivita(giorno)

    previsioni_elaborate_per_citta[nome_citta] = previsioni

    stampa_previsioni_con_consiglio(previsioni, nome_citta)
    esporta_csv(previsioni, f"previsioni_{nome_citta}.csv")

risultato_confronto = confronta_citta(dati_multi_citta)
stampa_confronto_citta(risultato_confronto)

scrivi_report_multi_citta(previsioni_elaborate_per_citta, "report_multi_citta.txt")