#!/usr/bin/env python
# coding: utf-8

# In[10]:


import requests
from bs4 import BeautifulSoup
import sqlite3

#Создание БД
def create_table(cur, conn):
    cur.execute('DROP TABLE IF EXISTS anime')

    cur.executescript('''CREATE TABLE anime (
            id INTEGER PRIMARY KEY,
            name_anime VARCHAR(255),
            series VARCHAR(255),
            url_image VARCHAR(255)
        )
    ''')
    conn.commit()


#Добавление данных в БД
def add_anime(cur, names, series, info):
    cur.execute('''INSERT INTO anime(name_anime, series, url_image) VALUES (?, ?, ?)''', (names, series, info))


with sqlite3.connect('example.db') as conn:
    cur = conn.cursor()
    create_table(cur, conn)
    
    #Скрапинг сайта
    url = 'https://jut.su/anime/'
    header = {"User-Agent":
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}
    resp = requests.get(url, headers=header)
    soup = BeautifulSoup(resp.text, 'lxml')
    data = soup.find_all("div", class_="all_anime")

    for block in data:
        names = block.find("div", class_="aaname").text
        series = block.find("div", class_="aailines").text
        info = block.find("div", class_="all_anime_image").get("style")
        
        #Добавление актуальных данной в БД
        add_anime(cur, names, series, info)
        conn.commit()
        
    #Вывод БД
    query = '''
        SELECT anime.name_anime, anime.series, anime.url_image
        FROM anime
    '''
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        name_anime, series, url_image = row
        print(name_anime, series, url_image, '\n')


# In[ ]:




