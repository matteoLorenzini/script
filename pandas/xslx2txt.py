import pandas as pd

df=pd.read_csv("OAV_60000.csv")

df.insert(0, 'id', range(1, 1 + len(df)))

print(df)

i=0

for index, row in df.iterrows():
    if i > len(df):
       break
    else:
       f = open(str(i)+'.txt', 'w')
       f.write(str(row[1]))
       f.close()
       i+=1