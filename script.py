import re

import pandas as pd

def openexel(fileName):
    df=pd.read_excel(fileName)
    return df

def filterdf(df):
    return (df['phone_number'].apply(lambda x:re.sub(r"[^0-9]",'',str(x))))

def writedf(df:pd.DataFrame):
    df.to_excel("output.xlsx",startcol=0,index=False)