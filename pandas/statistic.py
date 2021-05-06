import pandas as pd

#dataset
set = pd.read_csv ('T.csv',sep=',',names=['descriptions', 'etichetta', 'dominio'])

df = pd.DataFrame(set)

print(df)

stat = df.groupby(['etichetta', 'dominio']).size().reset_index(name='counts')

print(stat)

stat_dominio = df.groupby(['dominio']).size().reset_index(name='counts')



print(stat_dominio)
