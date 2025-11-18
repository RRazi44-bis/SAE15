# malik

import pandas as pd
import folium

def cor():           # importation des éléments 
    data = pd.read_csv("data.csv", encoding='CP1252', sep=';')
    if not {"Expérimentateur", "Latitude", "Longitude","Bande de fréquences", "Fréquences attribuées (limite basse)", "Fréquences attribuées (limite haute)",  "Code INSEE", "Début", "Fin", }.issubset(data.columns):
        raise ValueError("Colonnes manquantes")

    result = []        # création liste 
    for _, row in data.iterrows():                    # conversion des coordonées      
        lat = float(str(row['Latitude']).replace(',', '.'))
        lon = float(str(row['Longitude']).replace(',', '.'))
        bdf = str(row['Bande de fréquences'])     
        result.append((row['Expérimentateur'], bdf, row["Fréquences attribuées (limite basse)"], row["Fréquences attribuées (limite haute)"], row["Code INSEE"], row["Début"], row["Fin"], lat, lon)) # ajout des élements a la liste
    return result

coords = cor() 

carte = folium.Map(location=[coords[0][7], coords[0][8]], zoom_start=6)  #création de la carte avec le rajout des coordonées de Latitude et de Latitude

for experimentateur, bande, freq_b, freq_h, insee, debut, fin, lat, lon in coords:
    folium.Marker(           # crétion des markers et rajout des elements des élèments
        location=[lat, lon],        
        popup=f"""<b>{experimentateur}</b>     
fréquences: {bande}<br>
limite basse: {freq_b}<br>
limite haute: {freq_h}<br>
INSEE: {insee}<br>
Début: {debut}<br>
Fin: {fin}<br> """, 
        tooltip=experimentateur
    ).add_to(carte)
    
carte
