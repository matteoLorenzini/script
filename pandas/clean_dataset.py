# importing pandas package
import pandas as pd

# making data frame from csv file
dataset = pd.read_csv("CH_IT/dataset.csv",names=['DESCRIPTION', 'LABEL_','DOMAIN'])

input = pd.DataFrame(dataset)

print(input)

def data_massage

    if:
        # dropping ALL duplicte values
        target=input.drop_duplicates(subset=['DESCRIPTION'])
        black = target.reset_index(drop=True)
        black1 = black[~black['DESCRIPTION'].str.contains('<span|<br|<p|')]
        return df = black1.reset_index(drop=True)
        print(df)

    else:
        
        return df = input
        
    df.loc[df['LABEL'] == 'Good', 'LABEL_'] = 'High_Quality'  
    df.loc[df['LABEL'] != 'Good', 'LABEL_'] = 'Low_Quality'

    datasetTOTAL = df[['DESCRIPTION','LABEL','DOMAIN' ]]

    print(datasetTOTAL)

    dfFT = df[['DESCRIPTION', 'LABEL']]


    vaw = df.loc[df['DOMAIN'] == 'OpereArteVisiva']
    vaw.loc[vaw['LABEL'] == 'Good', 'LABEL_'] = 'High_Quality'  
    vaw.loc[vaw['LABEL'] != 'Good', 'LABEL_'] = 'Low_Quality'

    datasetVAW = vaw[['DESCRIPTION','LABEL','DOMAIN' ]]

    print(datasetVAW)
    vawFT = vaw[['DESCRIPTION', 'LABEL']]

    Ar = df.loc[df['DOMAIN'] == 'RepertoArcheologico']
    Ar.loc[Ar['LABEL'] == 'Good', 'LABEL_'] = 'High_Quality'  
    Ar.loc[Ar['LABEL'] != 'Good', 'LABEL_'] = 'Low_Quality'

    datasetAr = Ar[['DESCRIPTION','LABEL','DOMAIN' ]]

    print(datasetAr)

    ArFT = Ar[['DESCRIPTION', 'LABEL']]

    A = df.loc[df['DOMAIN'] == 'Architettura']
    A.loc[A['LABEL'] == 'Good', 'LABEL_'] = 'High_Quality'  
    A.loc[A['LABEL'] != 'Good', 'LABEL_'] = 'Low_Quality'

    datasetA = A[['DESCRIPTION','LABEL','DOMAIN' ]]

    print(datasetA)

    AFT = A[['DESCRIPTION', 'LABEL']]

    print(df)


    datasetVAW.to_csv('CH_IT/CSV/vaw/vaw.csv',sep = ',',  index=False, header=False, encoding="utf-8")
    datasetAr.to_csv('CH_IT/CSV/Ar/Ar.csv',sep = ',',  index=False, header=False, encoding="utf-8")
    datasetA.to_csv('CH_IT/CSV/A/A.csv',sep = ',',  index=False, header=False, encoding="utf-8")
    datasetTOTAL.to_csv('CH_IT/CSV/total/all.csv',sep = ',',  index=False, header=False, encoding="utf-8")

    vawFT.to_csv('CH_IT/FT/oa/oaFT.csv',sep = ',',  index=False, header=False, encoding="utf-8")
    ArFT.to_csv('CH_IT/FT/Ar/ArFT.csv',sep = ',',  index=False, header=False, encoding="utf-8")
    AFT.to_csv('CH_IT/FT/A/AFT.csv',sep = ',',  index=False, header=False, encoding="utf-8")
    dfFT.to_csv('CH_IT/FT/total/totalFT.csv',sep = ',',  index=False, header=False, encoding="utf-8")

