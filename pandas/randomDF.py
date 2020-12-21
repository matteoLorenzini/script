import pandas as pd

df = pd.read_excel ('excel/dataset_nuovo1.1.xlsx', sheet_name=('OpereArteVisiva'),
 skiprows='1')

df1 = df.sample(n = 1500) 

print(df1)

df1.to_excel ('mibact.xlsx', index = None, header=True)



