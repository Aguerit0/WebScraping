
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

ano = int(input("ingrese el año: "))
mes = int(input("ingrese el mes: "))

if mes > 9:
    url = f'https://wdc.kugi.kyoto-u.ac.jp/dst_final/{ano}{mes}/index.html'
else:
    url = f'https://wdc.kugi.kyoto-u.ac.jp/dst_final/{ano}0{mes}/index.html'


page = requests.get(url)  # Descarga el contenido de la página
soup = BeautifulSoup(page.content, 'html.parser')  # Parsea el contenido con BeautifulSoup

# Esto lo hacemos para poder identificar distintos objetos del HTML
datos = soup.find_all('pre', class_='data')
data_text = soup.get_text()

data_values = [int(value) for value in re.findall(r'-?\d+', data_text)]
day_length = 24
aux = []
vector = list()
indice = -1

for i in range(26,len(data_values),day_length+1):
    aux = []
    vector[indice +1] = [vector.append(str(datos))]#
    #print(vector)

all_day_data = [data_values[i:i+day_length] for i in range(26, len(data_values), day_length+1)]
                
                
c = 0
for j in range(len(all_day_data)):
    c = c +1
    print("Dia", c, all_day_data[j])

#la
#for i in range(len(all_day_data)):
print("\n")
df = pd.DataFrame(all_day_data, index=range(1, len(all_day_data) + 1), columns=range(1,len(all_day_data[0]) + 1 ))
df.to_excel('exports/dataFrame.lsx', engine = 'openpyxl')
print(df)
    







