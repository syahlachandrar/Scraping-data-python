# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup as bs
import csv

URL = 'https://proxyway.com/reviews'

titles_list = []


for page in range(1,4):
    req = requests.get(f'{URL}/page/{page}')
    soup = bs(req.text, 'html.parser')
    
    titles = soup.find_all('h3', class_='archive-list__title')

    for i, title in enumerate(titles, start=1):
        title_data = {
            'halaman ke-': f'{page}',
            'judul ke-': f'{i}',
            'judul': title.text.strip()
        }
        titles_list.append(title_data)

    filename = 'bismillah_coba5.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['halaman ke-', 'judul ke-', 'judul']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(titles_list)

print("Data berhasil disimpan")