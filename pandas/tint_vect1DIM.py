import pandas as pd

df = pd.read_excel ('excel/dataset_nuovo.xlsx', sheet_name='A_19859', skiprows='1')

df2 = df[['label','lenght']]

df2.loc[df2['label'] == 'Good', 'label_match'] = '1'  
df2.loc[df2['label'] != 'Good', 'label_match'] = '0'

df3 = df2[['label_match', 'lenght']]

#df3['lenght']='1:' + df3['lenght']

df3['vect'] = df3['lenght'].apply(lambda x: "{}{}".format('1:', x))

df4 = df3[['label_match','vect']]

print(df4)

df4.to_csv('A_19874_lenght.tsv', sep = '\t', index=False, header=False)
