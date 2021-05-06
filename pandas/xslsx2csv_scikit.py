import pandas as pd
'''
df = pd.read_excel ('../excel/dataset_nuovo1.1.xlsx', sheet_name=['Archeologia', 'OpereArteVisiva', 'Architettura'],
 skiprows='1')
'''

xls = pd.ExcelFile('../excel/dataset_nuovo1.1.xlsx')

df1 = pd.read_excel(xls,'Archeologia')
df2 = pd.read_excel(xls,'Architettura')
df3 = pd.read_excel(xls,'OpereArteVisiva')

df4 = pd.concat([df1,df2,df3])

df1.to_csv('Archeologia.csv',sep = ';',  index=False, header=False)
df2.to_csv('Architettura.csv',sep = ';',  index=False, header=False)
df3.to_csv('OpereArteVisiva.csv',sep = ';',  index=False, header=False)
#df4.to_csv('total.csv',sep = ';',  index=False, header=False)
