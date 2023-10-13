from bs4 import BeautifulSoup
import requests
import re

for i in range (1947,2016):
    for j in range (12):
        url = 'https://wdc.kugi.kyoto-u.ac.jp/dst_final/' + str(i+1)+'0'+str(j+1) + '/index.html'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        # obtención de datos del texto
        data_text = soup.get_text()
        # encontrar números enteros en el texto
        data_values = [int(value) for value in re.findall(r'-?\d+', data_text)]
        # Dividimos los datos en sublistas para cada día
        day_length = 24
        all_day_data = [data_values[i:i+day_length] for i in range(26, len(data_values), day_length+1)]
        print(all_day_data)

