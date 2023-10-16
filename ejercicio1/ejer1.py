import pandas as pd 
#import sklearn
import matplotlib.pyplot as plt

#Lectura del dataset
if __name__ == "__main__":
    dt_spotify = pd.read_csv('./dataset/spotify.csv')
#seleccionamos las columnas a evaluar:
columnas_especificas = ["Highest Charting Position", "Number of Times Charted", "Artist Followers","Popularity", "Danceability", "Energy","Loudness","Speechiness", "Liveness", "Valence"]
#Convertimos los valores de cada columna en numericos
for columna in columnas_especificas:
    dt_spotify[columna] = pd.to_numeric(dt_spotify[columna], errors='coerce')
#Calculamos la media, moda, cuartiles de datos y de percentiles por columna
media_columna = dt_spotify[columnas_especificas].mean()
moda_columna = dt_spotify[columnas_especificas].mode().iloc[0]
cuartiles_columna = dt_spotify[columnas_especificas].quantile([0.25, 0.50, 0.75])
percentiles_columna = dt_spotify[columnas_especificas].quantile([0.10, 0.25, 0.75])

# Mostramos los resultados
print("Media:")
print(media_columna)
print("\nModa:")
print(moda_columna)
print("\nCuartiles:")
print(cuartiles_columna)
print("\nPercentiles (10% y 90%):")
print(percentiles_columna)

#Graficamos sin usar numpy ni pandas
for columna in columnas_especificas:
    plt.figure()  # Crear una nueva figura para cada gráfico
    plt.hist(dt_spotify[columna].dropna(), bins=20)  # Creamos un histograma
    plt.xlabel(columna)  # Ponemos la etiqueta del eje x
    plt.ylabel("Frecuencia")  # Ponemos la etiqueta del eje y
    plt.title(f"Histograma de {columna}")  # Aca pondemos el título del gráfico

# Mostramos los gráficos
plt.show()


