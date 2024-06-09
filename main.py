# This is a sample Python script.
import pandas as pd
import scripts
fName=input('Введите название файла для очистки лишних символов из столбца с номерами телефонов:')
dataf= scripts.openexel(fName)
df= scripts.filterdf(dataf)
scripts.writedf(df)



