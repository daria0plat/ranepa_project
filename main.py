# This is a sample Python script.
import pandas as pd
import script
fName=input('Введите название файла для очистки лишних символов из столбца с номерами телефонов:')
dataf= script.openexel(fName)
df= script.filterdf(dataf)
script.writedf(df)
