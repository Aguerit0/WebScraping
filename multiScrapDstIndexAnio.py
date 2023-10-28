import requests
from bs4 import BeautifulSoup
import re


for i in range(1947,2016):
    print('AÑO:', i)
    for j in range(12):
        print('MES', j+1)
        if j+1>9:
            url = f'https://wdc.kugi.kyoto-u.ac.jp/dst_final/2016{str(j + 1)}/index.html'
        else:
            url = f'https://wdc.kugi.kyoto-u.ac.jp/dst_final/20160{str(j+1)}/index.html'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        # Obtención de datos del texto
        data_text = soup.get_text()
        # Encontrar números enteros en el texto
        data_values = [int(value) for value in re.findall(r'-?\d+', data_text)]
        # Dividimos los datos en sublistas para cada día
        day_length = 24
        all_day_data = [data_values[i:i + day_length] for i in range(26, len(data_values), day_length + 1)]
        for j in range(len(all_day_data)):
            print('DÍA', j + 1, ':', all_day_data[j])
