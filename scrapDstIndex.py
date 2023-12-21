from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Ingresar por teclado un año
año = input("Ingresar un año específico a consultar (1947-2016):\n ")
mes = input("Ingresar un mes específico a consultar (1-12):\n ")

if int(mes) >9:
    url = f'https://wdc.kugi.kyoto-u.ac.jp/dst_final/{año}{mes}/index.html'
else:
    url = f'https://wdc.kugi.kyoto-u.ac.jp/dst_final/{año}0{mes}/index.html'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# Obtención de datos del texto
data_text = soup.get_text()

# Encontrar números enteros en el texto
data_values = [int(value) for value in re.findall(r'-?\d+', data_text)]

# Dividimos los datos en sublistas para cada día
day_length = 24
all_day_data = [data_values[i:i+day_length] for i in range(26, len(data_values), day_length+1)]

dataframe = pd.DataFrame(all_day_data, index=range(1,len(all_day_data)+1), columns=range(1,len(all_day_data[0])+1))
print(dataframe)

# Nombre para el archivo exportado
nombre = 'datos('+año+'-'+mes+').xlsx'

# Exportar dataframe a excel
dataframe.to_excel('exports/'+nombre, engine='openpyxl', sheet_name='Indice DsT')

# Abrir archivo exportado
dataframe = pd.read_excel('exports/'+nombre)

# Grafico mapa de calor
plt.figure(figsize=(12,6))
sns.heatmap(dataframe.T, cmap='YlOrRd')
plt.xlabel('Dias')
plt.ylabel('Horas')
plt.title('MAPA DE CALOR: indice DsT')
#plt.show()

# Grafico
#dataframe.plot.scatter(x='Columna_X', y='Columna_Y', title='Índice DST Scatter Plot')
#lt.show()

#Funcion para extraer dstIndex diario
def tipoTormenta(all_day_data):
    vector = []
    vectorVerificar = []

    for i in range(len(all_day_data)):
        for j in range(len(all_day_data[i])):
            if all_day_data[i][j] < -100:
                vectorVerificar.append(2)
            elif all_day_data[i][j]>-100 and all_day_data[i][j]<-50:
                vectorVerificar.append(1)
            else:
                vectorVerificar.append(0)
        if 2 in vectorVerificar:
            vector.append("Intensa")
        elif 1 in vectorVerificar:
            vector.append("Moderada")
        else:
            vector.append("Debil")
        vectorVerificar.clear()

    # Creo un nuevo dataframe con el vector nuevo
    tipoTormentaDataFrame = pd.DataFrame(vector)
    tipoTormentaDataFrame.index +=1
    tipoTormentaDataFrame.columns = [f'Año {año}']
    with pd.ExcelWriter(f'exports/{nombre}', engine='openpyxl', mode='a') as writer:
        tipoTormentaDataFrame.to_excel(writer, sheet_name='Tipo de Tormenta')


tipoTormenta(all_day_data)