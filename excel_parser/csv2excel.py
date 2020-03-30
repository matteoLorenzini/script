import pandas as pd

read_file = pd.read_csv ('1.csv')
read_file.to_excel ('1.xlsx', index = None, header=True)