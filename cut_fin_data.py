import numpy as np
import pandas as pd

csv_filename = '2018_fd_utf8'
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

data_10['year'] = 2018

data_10.to_csv(csv_filename+'_cut10.csv')
