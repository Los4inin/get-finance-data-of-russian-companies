# id name inn revenue profit year

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
