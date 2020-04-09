import pandas as pd

df = pd.read_excel ('excel/dataset_nuovo.xlsx', sheet_name='RA_30251', skiprows='1')

df2 = df[['descrizione']]

print(df2)

df2.to_csv('csv_tint/RA_30251.csv',index=False)
