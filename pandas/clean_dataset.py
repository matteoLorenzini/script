# importing pandas package
import pandas as pd

# making data frame from csv file
input = pd.read_csv("dataset.csv")

print(input)

# dropping ALL duplicte values
target=input.drop_duplicates(subset=['DESCRIPTION'])
df = target.reset_index(drop=True)
print(df)
dfFT = df[['DESCRIPTION', 'LABEL']]


vaw = df.loc[df['DOMAIN'] == 'OpereArteVisiva']
print(vaw)
vawFT = vaw[['DESCRIPTION', 'LABEL']]

Ar = df.loc[df['DOMAIN'] == 'RepertoArcheologico']
print(Ar)
ArFT = Ar[['DESCRIPTION', 'LABEL']]

A = df.loc[df['DOMAIN'] == 'Architettura']
print(A)
AFT = A[['DESCRIPTION', 'LABEL']]

print(df)

vaw.to_csv('vaw.csv',sep = ',',  index=False, header=False, encoding="utf-8")
Ar.to_csv('Ar.csv',sep = ',',  index=False, header=False, encoding="utf-8")
A.to_csv('A.csv',sep = ',',  index=False, header=False, encoding="utf-8")
df.to_csv('total.csv',sep = ',',  index=False, header=False, encoding="utf-8")

vawFT.to_csv('../CSV/vaw/vawFT.csv',sep = ',',  index=False, header=False, encoding="utf-8")
ArFT.to_csv('../CSV/Ar/ArFT.csv',sep = ',',  index=False, header=False, encoding="utf-8")
AFT.to_csv('../CSV/A/AFT.csv',sep = ',',  index=False, header=False, encoding="utf-8")
dfFT.to_csv('../CSV/total/totalFT.csv',sep = ',',  index=False, header=False, encoding="utf-8")

