import requests
from bs4 import BeautifulSoup


#Добавление данных в БД
def add_stats(cur, names, line, popular, wins, bans, kdas, pentakills):
    cur.execute('''INSERT INTO league_of_legends(person, line, popularity_percent, winrate_percent, banrate_percent, kda, pentas_match)
                VALUES (?, ?, ?, ?, ?, ?, ?)''',(names, line, popular, wins, bans, kdas, pentakills))

def parser(cur, conn):
    #Скрапинг сайта
    url = 'https://www.leagueofgraphs.com/ru/champions/builds'
    header = {"User-Agent":
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}
    resp = requests.get(url, headers=header)
    soup = BeautifulSoup(resp.text, 'lxml')
    data = soup.find_all("tr")
    
    
    for block in data:
        if block.find("span", class_="name") != None:
            names = block.find("span", class_="name")
            final_names = names.text.replace(' ','').replace('\n','')
            lines = block.find("i")
            final_lines = lines.text.replace(' ','').replace('\n','')
        
            #Парсинг данных Популярности, Винрейта, Банпика из progressbar
            array_one = block.find_all('progressbar')
            for obj in array_one:
                if obj['data-color'] == 'wgblue':
                    populars = round(float(obj['data-value'])*100,1)
                elif obj['data-color'] == 'wggreen':
                    wins = round(float(obj['data-value'])*100,1)
                elif obj['data-color'] == 'wgred':
                    bans = round(float(obj['data-value'])*100,1)
            array_two = block.find_all("td", class_="text-center hide-for-small-down")
            for obj in array_two:
                if (obj.find("span", class_='kills')) != None:
                    kdas = obj.text.replace(' ','').replace('\n', '')
                else:
                    pentakills = float(obj.text. replace(' ','').replace('\n',''))
            add_stats(cur, final_names, final_lines, populars, wins, bans, kdas, pentakills)
            conn.commit()