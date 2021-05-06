import pandas as pd



xls =  pd.ExcelFile('../excel/dataset_nuovo.xlsx')

df1 = pd.read_excel(xls, 'RA_30251')
df2 = pd.read_excel(xls, 'A_19859')
df3 = pd.read_excel(xls, 'OAV_60000')

archeo = df1[['descrizione', 'label']]
archit = df2[['descrizione', 'label']]
vaw    = df3[['descrizione', 'label']]

frames = [df1, df2, df3]


concat = pd.concat(frames)

total = concat[['descrizione', 'label']]



archeo.to_csv('RA_30251.csv',sep = ';',  index=False, header=False, encoding="utf-8")
archit.to_csv('A_19859.csv',sep = ';',  index=False, header=False, encoding="utf-8")
vaw.to_csv('OAV_60000.csv',sep = ';',  index=False, header=False, encoding="utf-8")
total.to_csv('total.csv',sep = ';',  index=False, header=False, encoding="utf-8")
