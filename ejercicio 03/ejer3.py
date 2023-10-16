import pandas as pd 
#import sklearn
import matplotlib.pyplot as plt

#Lectura del dataset
if __name__ == "__main__":
    dt_spotify = pd.read_csv('./data/spotify.csv')
    print(dt_spotify.head(10))

columnas_especificas = ["Highest Charting Position", "Number of Times Charted", "Artist Followers","Popularity", "Danceability", "Energy","Loudness","Speechiness", "Liveness", "Valence"]

columnas_con_valores_faltantes = dt_spotify.columns[dt_spotify.isnull().any()] 

for columna in columnas_con_valores_faltantes:
    dt_spotify[columna] = pd.to_numeric(dt_spotify[columna], errors='coerce')
    media = dt_spotify[columna].mean()  # Calcula la media de la columna
    dt_spotify[columna].fillna(media, inplace=True)

print(dt_spotify.head(10))
print(media)
