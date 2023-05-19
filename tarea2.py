import pandas as pd

# Cargar los datos de casos COVID-19 en Chile
url = 'https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv'
df = pd.read_csv(url)

