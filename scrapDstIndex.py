from bs4 import BeautifulSoup
import requests
import re

url = 'https://wdc.kugi.kyoto-u.ac.jp/dst_final/201601/index.html'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

#obtención de datos del texto
data_text = soup.get_text()

#encontrar números enteros en el texto
data_values = [int(value) for value in re.findall(r'-?\d+', data_text)]


# Dividimos los datos en sublistas para cada día
day_length = 24
all_day_data = [data_values[i:i+day_length] for i in range(26, len(data_values), day_length+1)]
j=0
for i in range(len(all_day_data)):
    j=j+1
    print('DÍA',j,':',all_day_data[i])
