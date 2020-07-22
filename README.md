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

encoding2utf8.py
    
# 3) выбираеем только необходимые данные (я выбрал ["name", "inn", "revenue", "profit"]), отсекаем фирмы "нулевки" с оборотом менее 10 млн рублей, и укорачиваем нейминг компаний ООО и так далее
# 3) select only the necessary data (I chose ["name", "inn", "revenue"," profit"]), cut off the company "zero revenue" with a revenue less than 10 million rubles, and shorten the naming of companies LLC and so on

cut_fin_data.py

# 4) перегоняем  CSV в SQlite 
# 4) CSV 2 SQlite

csv2sql_fin_data.py
