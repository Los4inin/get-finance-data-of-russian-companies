# get-finance-data-of-russian-companies

# появилась задача получить доступ к финансовой отчетности компаний РФ
# i wanted to get access to the financial statements of Russian companies

# вся отчетность публикуется на сайте - https://www.gks.ru/opendata?division=&tag=&updated_from=&updated_to=&search=&search_by_name=on&sort=asc&per_page=10 
# all open data you can find on website - https://www.gks.ru/opendata?division=&tag=&updated_from=&updated_to=&search=&search_by_name=on&sort=asc&per_page=10 

# но формат выдачи очень неудобный - csv файла огромного объема, работать с которыми очень сложно
# but the output format is very inconvenient - a huge csv file, which is very difficult to work with

# финансовая отчетность обновляется через год в конце октября, то есть отчетность за 2019 год будет доступна в ноябре 2020
# the financial statements are updated every other year at the end of October, meaning the 2019 financial statements will be available in November 2020

# 1) выкачиваем отчетность за интересующий год
# 1) downloadinng out reports for the year of interest

# 2) перекодируем файлы из 1251 в utf8, код на Питоне
# 2) encoding files from 1251 to utf8, Python code:

with open('source_file.csv', 'r', encoding="1251") as f, open('result_file.csv', 'w') as f1:
    for line in f: f1.write(line)
    
# 3) выбираеем только необходимые данные (я выбрал ["name", "inn", "revenue", "profit"]), отсекаем фирмы "нулевки" с оборотом менее 10 млн рублей, и укорачиваем нейминг компаний ООО и так далее
# 3) select only the necessary data (I chose ["name", "inn", "revenue"," profit"]), cut off the company "zero revenue" with a revenue less than 10 million rubles, and shorten the naming of companies LLC and so on

import numpy as np
import pandas as pd
csv_filename = '2018_fd_utf8' # имя исходного цсв файла
data = pd.read_csv(csv_filename+'.csv', delimiter=';', header = None)
data = data.iloc[:,[0,5,82,116]]
data.columns = ["name", "inn", "revenue", "profit"]
data_10 = data.drop(np.where(data['revenue'] < 10000)[0])
data_10['name'] = data_10['name'].str.replace('ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ','ООО')
data_10['name'] = data_10['name'].str.replace('Общество с ограниченной ответственностью','ООО')
data_10['name'] = data_10['name'].str.replace('ОТКРЫТОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО','ОАО')
data_10['name'] = data_10['name'].str.replace('Открытое акционерное общество','ОАО')
data_10['name'] = data_10['name'].str.replace('ЗАКРЫТОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО','ЗАО')
data_10['name'] = data_10['name'].str.replace('Закрытое акционерное общество','ЗАО')
data_10['name'] = data_10['name'].str.replace('НЕПУБЛИЧНОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО','НеПАО')
data_10['name'] = data_10['name'].str.replace('Непубличное акционерное общество','НеПАО')
data_10['name'] = data_10['name'].str.replace('ПУБЛИЧНОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО','ПАО')
data_10['name'] = data_10['name'].str.replace('Публичное акционерное общество','ПАО')
data_10['name'] = data_10['name'].str.replace('АКЦИОНЕРНОЕ ОБЩЕСТВО','АО')
data_10['name'] = data_10['name'].str.replace('Акционерное общество','АО')
data_10['name'] = data_10['name'].str.replace('"','')
data_10['year'] = 2018  # год выборки
data_10.to_csv(csv_filename+'_cut10.csv')

# 4) перегоняем  CSV в SQlite 
# 4) CSV 2 SQlite

import sqlite3
conn = sqlite3.connect("fin_data.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS inn_revenue (id, inn, year, revenue, profit)")
with open('2018_fd_utf8_cut10.csv') as f:
    n=1363698
    for line in f:
        line_arr = line.split(',')
        if not line_arr[-4].isdigit(): continue
        try:
            line_arr[-3]=int(line_arr[-3])
            line_arr[-2]=int(line_arr[-2])
            line_arr[-1]=int(line_arr[-1])
        except:
            continue
        data = (n, line_arr[-4], line_arr[-1], line_arr[-3] ,line_arr[-2])
        #print(data)
        conn.execute('INSERT INTO inn_revenue VALUES (?,?,?,?,?)', data)
        n=n+1
        if n%1000==0:
            print(n)
            conn.commit()
    print(n)
    conn.commit()
    
