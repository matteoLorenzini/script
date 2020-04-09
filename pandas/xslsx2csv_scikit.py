import pandas as pd

df = pd.read_excel ('excel/dataset_nuovo.xlsx', sheet_name='A_19859_Test2561', skiprows='1')

df2 = df[['descrizione', 'label']]

print(df2)

df2.to_csv('A_19859_Test2561.csv',sep = ';',  index=False, header=False)

