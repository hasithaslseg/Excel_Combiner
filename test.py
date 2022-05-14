import xlsxwriter
import os
import pandas as pd
import openpyexcel
i=0
directory = 'CV'
b=(os.listdir(directory))
print(b)


with xlsxwriter.Workbook('forecast1.xlsx') as workbook:
    worksheet=workbook.add_worksheet('all_data')
    for x in b:
        df=pd.read_excel(x)
        for row,column in df.iterrows():
            list1=[column[1],column[2]]
            worksheet.write_row(i,0,list1)
            i=i+1