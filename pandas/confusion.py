import pandas as pd

# names of files to read from

r_filenameTSV = 'OAV_60000_Training48000.tsv'
r_filenameCSV = 'OAV8020Predict.csv'


tsv_read = pd.read_csv(r_filenameTSV, sep='\t',names=["vector"])
csv_read = pd.read_csv(r_filenameCSV,names=["label_predict"])

df = pd.DataFrame(tsv_read)
df2 = pd.DataFrame(csv_read)

df = pd.DataFrame(df.vector.str.split(' ',1).tolist(),
                                   columns = ['label','vector'])

print (df)
print (df2)

print (df[['label']])

#frames = ([df[['label']], df2])

result = pd.concat([pd.concat([df['label']], axis=0), pd.concat([df2], axis=0)], axis=1)

print (result)

with pd.ExcelWriter('output_label.xlsx') as writer:  
   		#df[['label']].to_excel(writer, sheet_name='Sheet_name_1')
  		result.to_excel(writer, sheet_name='Sheet_name_1')

   
