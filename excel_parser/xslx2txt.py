import pandas ad pd

df=pd.read_excel("excel/export.csv", sheetname='OAV_60000')

for index in range(len(df)):
     with open(df["oggetto"][index] +  '.txt', 'w') as output:
        output.write(df["descrizione"][index])